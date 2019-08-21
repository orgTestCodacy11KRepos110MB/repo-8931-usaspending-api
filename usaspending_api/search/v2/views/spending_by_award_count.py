import copy
import json

from django.conf import settings
from django.db.models import Count
from rest_framework.response import Response
from rest_framework.views import APIView

from usaspending_api.awards.v2.filters.sub_award import subaward_filter
from usaspending_api.awards.v2.lookups.lookups import assistance_type_mapping
from usaspending_api.common.api_versioning import api_transformations, API_TRANSFORM_FUNCTIONS
from usaspending_api.common.cache_decorator import cache_response
from usaspending_api.common.exceptions import InvalidParameterException, NoIntersectionException
from usaspending_api.common.helpers.orm_helpers import category_to_award_materialized_views
from usaspending_api.common.validator.award_filter import AWARD_FILTER
from usaspending_api.common.validator.pagination import PAGINATION
from usaspending_api.common.validator.tinyshield import TinyShield
from usaspending_api.common.data_connectors.async_spending_by_award_count import async_fetch_category_counts


@api_transformations(api_version=settings.API_VERSION, function_list=API_TRANSFORM_FUNCTIONS)
class SpendingByAwardCountVisualizationViewSet(APIView):
    """This route takes award filters, and returns the number of awards in each award type.

    (Contracts, Loans, Grants, etc.)
    """

    endpoint_doc = "usaspending_api/api_contracts/contracts/search/SpendingByAwardCount.md"

    @cache_response()
    def post(self, request):
        models = [{"name": "subawards", "key": "subawards", "type": "boolean", "default": False}]
        models.extend(copy.deepcopy(AWARD_FILTER))
        models.extend(copy.deepcopy(PAGINATION))
        json_request = TinyShield(models).block(request.data)
        filters = json_request.get("filters", None)
        subawards = json_request["subawards"]

        if filters is None:
            raise InvalidParameterException("Missing required request parameters: 'filters'")

        results = {"contracts": 0, "idvs": 0, "grants": 0, "direct_payments": 0, "loans": 0, "other": 0}
        if subawards:
            results = {"subcontracts": 0, "subgrants": 0}

        if "award_type_codes" in filters and "no intersection" in filters["award_type_codes"]:
            # "Special case": there will never be results when the website provides this value
            raise NoIntersectionException(json.loads(json.dumps({"results": results})))

        if not subawards:
            results = async_fetch_category_counts(filters, category_to_award_materialized_views())
        else:
            queryset = subaward_filter(filters).values("prime_award_type").annotate(category_count=Count("subaward_id"))

            for award in queryset:
                result_key = "subcontracts"
                if award["prime_award_type"] in assistance_type_mapping.keys():
                    result_key = "subgrants"
                results[result_key] += award["category_count"]

        return Response({"results": results})
