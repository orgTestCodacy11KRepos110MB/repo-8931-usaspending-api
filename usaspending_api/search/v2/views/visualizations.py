from rest_framework.response import Response
from rest_framework.views import APIView

from usaspending_api.common.exceptions import InvalidParameterException
from usaspending_api.awards.v2.filters.transaction import transaction_filter
import ast
from usaspending_api.common.helpers import generate_fiscal_year, generate_fiscal_period, generate_fiscal_month


class SpendingOverTimeVisualizationViewSet(APIView):

    def post(self, request):
        """Return all budget function/subfunction titles matching the provided search text"""
        json_request = request.data
        group = json_request.get('group', None)
        filters = json_request.get('filters', None)

        if group is None:
            raise InvalidParameterException('Missing one or more required request parameters: group')
        if filters is None:
            raise InvalidParameterException('Missing one or more required request parameters: filters')
        potential_groups = ["quarter", "fiscal_year", "month", "fy", "q", "m"]
        if group not in potential_groups:
            raise InvalidParameterException('group does not have a valid value')

        # build sql query filters
        queryset = transaction_filter(filters)

        # define what values are needed in the sql query
        queryset = queryset.values('action_date', 'federal_action_obligation')

        # build response
        response = {'group': group, 'results': []}

        # key is time period (defined by group), value is federal_action_obligation
        group_results = {}  # '{"fy": "2017", "quarter": "3"}' : 1000
        for trans in queryset:
            key = {}
            if group == "fy" or group == "fiscal_year":
                fy = generate_fiscal_year(trans.action_date)
                key = {"fiscal_year": str(fy)}
            elif group == "m" or group == 'month':
                fy = generate_fiscal_year(trans.action_date)
                m = generate_fiscal_month(trans.action_date)
                key = {"fiscal_year": str(fy), "month": str(m)}
            else:  # quarter
                fy = generate_fiscal_year(trans.action_date)
                q = generate_fiscal_period(trans.action_date)
                key = {"fiscal_year": str(fy), "quarter": str(q)}
            # python cant have a dict as a key
            key = str(key)
            if group_results.get(key) is None:
                group_results[key] = trans.federal_action_obligation
            else:
                group_results[key] = group_results.get(key) + trans.federal_action_obligation

        # convert result into expected format
        results = []
        # [{
        # "time_period": {"fy": "2017", "quarter": "3"},
        # 	"aggregated_amount": "200000000"
        # }]
        for key, value in group_results.items():
            key = ast.literal_eval(key)
            result = {"time_period": key, "aggregated_amount": float(value)}
            results.append(result)
        response['results'] = results

        return Response(response)


class SpendingByCategoryVisualizationViewSet(APIView):

    def post(self, request):
        """Return all budget function/subfunction titles matching the provided search text"""
        json_request = request.data
        category = json_request.get('category', None)
        scope = json_request.get('scope', None)
        filters = json_request.get('filters', None)
        limit = json_request.get('limit', None)
        page = json_request.get('page', None)

        if category is None:
            raise InvalidParameterException('Missing one or more required request parameters: group')
        if scope is None & category != "cfda_programs":
            raise InvalidParameterException('Missing one or more required request parameters: group')
        if limit is None:
            limit = 10
        if page is None:
            page = 0
        if filters is None:
            raise InvalidParameterException('Missing one or more required request parameters: filters')
        potential_scopes = ["agency", "subagency", "offices"]
        if scope not in potential_scopes:
            raise InvalidParameterException('scope does not have a valid value')

        # filter queryset
        queryset = transaction_filter(filters)

        # build response
        response = {'category': category, 'scope': scope, 'limit': limit, 'page': page, 'results': []}

        # filter the transactions by category
        if category == "funding_agency" | category == "awarding_agency":
            # filter the transactions by scope name
            name_dict = {}  # {ttname: {aggregated_amount: 1000, abbreviation: "tt"}
            # define what values are needed in the sql query
            queryset = queryset.values('federal_action_obligation', 'funding_agency', 'awarding_agency')

            if scope == 'agency':
                for trans in queryset:
                    ttname = trans[category].toptier_agency.name
                    if name_dict.get(ttname):
                        name_dict[ttname]["aggregated_amount"] += trans.federal_action_obligation
                    else:
                        name_dict[ttname] = {"aggregated_amount": trans.federal_action_obligation,
                                             "abbreviation": trans[category].toptier_agency.abbreviation}

            elif scope == 'subagency':
                for trans in queryset:
                    if trans[category].subtier_agency:
                        stname = trans[category].subtier_agency.name
                        if name_dict.get(stname):
                            name_dict[stname]["aggregated_amount"] += trans.federal_action_obligation
                        else:
                            name_dict[stname] = {"aggregated_amount": trans.federal_action_obligation,
                                                 "abbreviation": trans[category].toptier_agency.abbreviation}
            else:  # offices
                for trans in queryset:
                    if trans[category].office_agency:
                        oname = trans[category].office_agency.name
                        if name_dict.get(oname):
                            name_dict[oname]["aggregated_amount"] += trans.federal_action_obligation
                        else:
                            name_dict[oname] = {"aggregated_amount": trans.federal_action_obligation,
                                                "abbreviation": trans[category].toptier_agency.abbreviation}

        elif category == "recipient":
            # filter the transactions by scope name
            name_dict = {}  # {recipient_name: {legal_entity_id: "1111", aggregated_amount: "1111"}
            # define what values are needed in the sql query
            queryset = queryset.values('federal_action_obligation', 'recipient')
            if scope == "duns":
                for trans in queryset:
                    if trans.get('recipient'):
                        r_name = trans.recipient.recipient_name
                        if name_dict.get(r_name):
                            name_dict[r_name]["aggregated_amount"] += trans.federal_action_obligation
                        else:
                            name_dict[r_name] = {"aggregated_amount": trans.federal_action_obligation,
                                                 "legal_entity_id": trans.recipient.get('legal_entity_id')}
            elif scope == "parent_duns":
                for trans in queryset:
                    if trans.get('recipient'):
                        r_name = trans.recipient.recipient_name
                        if name_dict.get(r_name):
                            name_dict[r_name]["aggregated_amount"] += trans.federal_action_obligation
                        else:
                            name_dict[r_name] = {"aggregated_amount": trans.federal_action_obligation,
                                                 "parent_recipient_unique_id":
                                                     trans.recipient.get('parent_recipient_unique_id')}
            else:  # recipient_type
                raise InvalidParameterException('recipient type is not yet implemented')

        elif category == "cfda_programs":
            pass
            # filter the transactions by scope name
            name_dict = {}  # {recipient_name: {legal_entity_id: "1111", aggregated_amount: "1111"}
            # define what values are needed in the sql query
            queryset = queryset.values('federal_action_obligation', 'assistance_data__cgac')
            for trans in queryset:
                if trans.get('assistance_data'):
                    cfda_program_number = trans.assistance_data.cfda.program_number
                    if name_dict.get(cfda_program_number):
                        name_dict[cfda_program_number]["aggregated_amount"] += trans.federal_action_obligation
                    else:
                        name_dict[cfda_program_number] = {"aggregated_amount": trans.federal_action_obligation,
                                                          "program_title": trans.assistance_data.cfda.get('program_title'),
                                                          "popular_name": trans.assistance_data.cfda.get('popular_name')}
        else:  # industry_codes
            pass

        # build results
        results = []
        # [{
        # "agency_name": ttname,
        # "agency_abbreviation": ttabrev,
        # 	"aggregated_amount": "200000000"
        # }]
        for key, value in name_dict:
            results.append({"agency_name": key, "agency_abbreviation":value["abbreviation"],
                            "aggregated_amount": value["aggregated_amount"]})

        response['results'] = results
        return Response(response)
