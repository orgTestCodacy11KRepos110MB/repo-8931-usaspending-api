import pytest

from model_mommy import mommy

from usaspending_api.references.models import DisasterEmergencyFundCode
from usaspending_api.submissions.models import SubmissionAttributes
from usaspending_api.disaster.tests.fixtures.object_class_data import major_object_class_with_children


@pytest.fixture
def basic_object_class_faba_with_loan_value(award_count_sub_schedule, award_count_submission, defc_codes):
    award = _normal_award()

    basic_object_class = major_object_class_with_children("001", [1])

    mommy.make(
        "awards.FinancialAccountsByAwards",
        award=award,
        parent_award_id="basic award",
        disaster_emergency_fund=DisasterEmergencyFundCode.objects.filter(code="M").first(),
        submission=SubmissionAttributes.objects.all().first(),
        object_class=basic_object_class[0],
        gross_outlays_delivered_orders_paid_total_cpe=8,
    )


def _normal_award():
    return mommy.make("awards.Award", type="A", total_loan_value=5)
