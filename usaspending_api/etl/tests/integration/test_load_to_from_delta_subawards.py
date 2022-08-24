from datetime import datetime, date
from decimal import Decimal

from pytest import mark

from usaspending_api.etl.tests.integration.test_load_to_from_delta import (
    create_and_load_all_delta_tables,
    verify_delta_table_loaded_to_delta,
)


@mark.django_db(transaction=True)
def test_load_table_to_delta_for_subawards(
    spark,
    s3_unittest_data_bucket,
    broker_server_dblink_setup,
    populate_broker_data_to_delta,
    populate_data_for_transaction_search,
):
    tables_to_load = [
        "awards",
        "sam_recipient",
        "transaction_normalized",
        "transaction_fabs",
        "transaction_fpds",
        "recipient_lookup",
        "financial_accounts_by_awards",
    ]
    create_and_load_all_delta_tables(spark, s3_unittest_data_bucket, tables_to_load)
    verify_delta_table_loaded_to_delta(spark, "broker_subaward", s3_unittest_data_bucket)

    expected_dummy_data = [
        {
            "broker_created_at": datetime(2019, 6, 11, 18, 27, 37, 76916),
            "broker_updated_at": datetime(2019, 6, 11, 18, 27, 37, 76916),
            "broker_subaward_id": 211,
            "unique_award_key": None,
            "award_piid_fain": "asfasfasfs",
            "parent_award_id": None,
            "award_amount": Decimal("1937.00"),
            "action_date": date(2011, 7, 5),
            "fy": "FY2011",
            "awarding_agency_code": None,
            "awarding_agency_name": None,
            "awarding_sub_tier_agency_c": None,
            "awarding_sub_tier_agency_n": None,
            "awarding_office_code": None,
            "awarding_office_name": None,
            "funding_agency_code": None,
            "funding_agency_name": None,
            "funding_sub_tier_agency_co": None,
            "funding_sub_tier_agency_na": None,
            "funding_office_code": None,
            "funding_office_name": None,
            "awardee_or_recipient_uniqu": "323233",
            "awardee_or_recipient_uei": None,
            "awardee_or_recipient_legal": "A PLACE",
            "dba_name": "FHI 360",
            "ultimate_parent_unique_ide": "52545",
            "ultimate_parent_uei": None,
            "ultimate_parent_legal_enti": "a nother place",
            "legal_entity_country_code": "USA",
            "legal_entity_country_name": "UNITED STATES",
            "legal_entity_state_code": "NC",
            "legal_entity_state_name": None,
            "legal_entity_zip": "27701",
            "legal_entity_congressional": "01",
            "legal_entity_foreign_posta": None,
            "legal_entity_city_name": "DURHAM",
            "legal_entity_address_line1": "an address",
            "business_types": None,
            "place_of_perform_country_co": "NG",
            "place_of_perform_country_na": None,
            "place_of_perform_state_code": "00",
            "place_of_perform_state_name": None,
            "place_of_performance_zip": None,
            "place_of_perform_congressio": None,
            "place_of_perform_city_name": "FORGN",
            "place_of_perform_street": "789 street st",
            "award_description": "do things for us please",
            "naics": None,
            "naics_description": None,
            "cfda_numbers": "98.001",
            "cfda_titles": "USAID Foreign Assistance for Programs Overseas",
            "subaward_type": "sub-grant",
            "subaward_report_year": 2014,
            "subaward_report_month": 7,
            "subaward_number": "SDAFASFSDF",
            "subaward_amount": Decimal("747.00"),
            "sub_action_date": date(2014, 2, 27),
            "sub_awardee_or_recipient_uniqu": "23452543",
            "sub_awardee_or_recipient_uei": None,
            "sub_awardee_or_recipient_legal_raw": "YOLO",
            "sub_dba_name": None,
            "sub_ultimate_parent_unique_ide": None,
            "sub_ultimate_parent_uei": None,
            "sub_ultimate_parent_legal_enti_raw": None,
            "sub_legal_entity_country_code_raw": "NG",
            "sub_legal_entity_country_name_raw": None,
            "sub_legal_entity_state_code": "00",
            "sub_legal_entity_state_name": None,
            "sub_legal_entity_zip": None,
            "sub_legal_entity_congressional_raw": None,
            "sub_legal_entity_foreign_posta": None,
            "sub_legal_entity_city_name": "YOLA",
            "sub_legal_entity_address_line1": "YOLA TOWN",
            "sub_business_types": None,
            "sub_place_of_perform_country_co_raw": "NG",
            "sub_place_of_perform_country_na": None,
            "sub_place_of_perform_state_code": "00",
            "sub_place_of_perform_state_name": None,
            "sub_place_of_performance_zip": None,
            "sub_place_of_perform_congressio_raw": None,
            "sub_place_of_perform_city_name": "ADAMAWA",
            "sub_place_of_perform_street": "987 STREET ST",
            "subaward_description": "MORE STUFF",
            "sub_high_comp_officer1_full_na": None,
            "sub_high_comp_officer1_amount": None,
            "sub_high_comp_officer2_full_na": None,
            "sub_high_comp_officer2_amount": None,
            "sub_high_comp_officer3_full_na": None,
            "sub_high_comp_officer3_amount": None,
            "sub_high_comp_officer4_full_na": None,
            "sub_high_comp_officer4_amount": None,
            "sub_high_comp_officer5_full_na": None,
            "sub_high_comp_officer5_amount": None,
            "prime_id": 144029,
            "internal_id": "ASDFASFSADFSDASFD",
            "date_submitted": datetime(2014, 7, 24, 14, 27, 49),
            "report_type": None,
            "transaction_type": None,
            "program_title": None,
            "contract_agency_code": None,
            "contract_idv_agency_code": None,
            "grant_funding_agency_id": None,
            "grant_funding_agency_name": None,
            "federal_agency_name": None,
            "treasury_symbol": None,
            "dunsplus4": None,
            "recovery_model_q1": None,
            "recovery_model_q2": None,
            "compensation_q1": True,
            "compensation_q2": True,
            "high_comp_officer1_full_na": None,
            "high_comp_officer1_amount": None,
            "high_comp_officer2_full_na": None,
            "high_comp_officer2_amount": None,
            "high_comp_officer3_full_na": None,
            "high_comp_officer3_amount": None,
            "high_comp_officer4_full_na": None,
            "high_comp_officer4_amount": None,
            "high_comp_officer5_full_na": None,
            "high_comp_officer5_amount": None,
            "sub_id": 845063,
            "sub_parent_id": 144029,
            "sub_federal_agency_id": None,
            "sub_federal_agency_name": None,
            "sub_funding_agency_id": None,
            "sub_funding_agency_name": None,
            "sub_funding_office_id": None,
            "sub_funding_office_name": None,
            "sub_naics": None,
            "sub_cfda_numbers": "98.001 USAID Foreign Assistance for Programs Overseas",
            "sub_dunsplus4": None,
            "sub_recovery_subcontract_amt": None,
            "sub_recovery_model_q1": None,
            "sub_recovery_model_q2": None,
            "sub_compensation_q1": False,
            "sub_compensation_q2": False,
            "award_id": None,
            "prime_award_group": "grant",
            "prime_award_type": None,
            "piid": None,
            "fain": "asfasfasfs",
            "latest_transaction_id": None,
            "last_modified_date": None,
            "awarding_agency_id": None,
            "awarding_toptier_agency_name": None,
            "awarding_toptier_agency_abbreviation": None,
            "awarding_subtier_agency_name": None,
            "awarding_subtier_agency_abbreviation": None,
            "funding_agency_id": None,
            "funding_subtier_agency_abbreviation": None,
            "funding_subtier_agency_name": None,
            "funding_toptier_agency_abbreviation": None,
            "funding_toptier_agency_name": None,
            "cfda_id": None,
            "cfda_number": None,
            "cfda_title": None,
            "sub_fiscal_year": 2014,
            "sub_total_obl_bin": "<1M",
            "sub_awardee_or_recipient_legal": "YOLO",
            "sub_ultimate_parent_legal_enti": None,
            "business_type_code": None,
            "business_categories": [],
            "treasury_account_identifiers": None,
            "pulled_from": None,
            "type_of_contract_pricing": None,
            "type_set_aside": None,
            "extent_competed": None,
            "product_or_service_code": None,
            "product_or_service_description": None,
            "sub_legal_entity_country_code": "NG",
            "sub_legal_entity_country_name": None,
            "sub_legal_entity_county_code": None,
            "sub_legal_entity_county_name": None,
            "sub_legal_entity_zip5": "",
            "sub_legal_entity_city_code": None,
            "sub_legal_entity_congressional": None,
            "place_of_perform_scope": None,
            "sub_place_of_perform_country_co": "NG",
            "sub_place_of_perform_country_name": None,
            "sub_place_of_perform_county_code": None,
            "sub_place_of_perform_county_name": None,
            "sub_place_of_perform_zip5": "",
            "sub_place_of_perform_city_code": None,
            "sub_place_of_perform_congressio": None,
        },
        {
            "broker_created_at": datetime(2019, 6, 11, 18, 27, 37, 76916),
            "broker_updated_at": datetime(2019, 6, 11, 18, 27, 37, 76916),
            "broker_subaward_id": 3241450,
            "unique_award_key": "asdfasfasfsadfsad",
            "award_piid_fain": "asdfasdfasdfs",
            "parent_award_id": None,
            "award_amount": Decimal("25000.00"),
            "action_date": date(2017, 9, 17),
            "fy": "FY2017",
            "awarding_agency_code": "019",
            "awarding_agency_name": "Department of State (DOS)",
            "awarding_sub_tier_agency_c": "1900",
            "awarding_sub_tier_agency_n": "Department of State",
            "awarding_office_code": None,
            "awarding_office_name": None,
            "funding_agency_code": None,
            "funding_agency_name": None,
            "funding_sub_tier_agency_co": None,
            "funding_sub_tier_agency_na": None,
            "funding_office_code": None,
            "funding_office_name": None,
            "awardee_or_recipient_uniqu": "2345235",
            "awardee_or_recipient_uei": None,
            "awardee_or_recipient_legal": "COMPANY B",
            "dba_name": "asdfsafd",
            "ultimate_parent_unique_ide": "54235",
            "ultimate_parent_uei": None,
            "ultimate_parent_legal_enti": "company c",
            "legal_entity_country_code": "USA",
            "legal_entity_country_name": "UNITED STATES",
            "legal_entity_state_code": "NC",
            "legal_entity_state_name": "North Carolina",
            "legal_entity_zip": "27701",
            "legal_entity_congressional": "01",
            "legal_entity_foreign_posta": None,
            "legal_entity_city_name": "DURHAM",
            "legal_entity_address_line1": "redacted",
            "business_types": None,
            "place_of_perform_country_co": "USA",
            "place_of_perform_country_na": "UNITED STATES",
            "place_of_perform_state_code": "NC",
            "place_of_perform_state_name": "North Carolina",
            "place_of_performance_zip": "27707",
            "place_of_perform_congressio": "01",
            "place_of_perform_city_name": "DURHAM",
            "place_of_perform_street": "000 street st",
            "award_description": "FY 2017 things",
            "naics": None,
            "naics_description": None,
            "cfda_numbers": "19.421",
            "cfda_titles": "Academic Exchange Programs - English Language Programs",
            "subaward_type": "sub-grant",
            "subaward_report_year": 2019,
            "subaward_report_month": 2,
            "subaward_number": "DASFASF",
            "subaward_amount": Decimal("898.00"),
            "sub_action_date": date(2019, 3, 23),
            "sub_awardee_or_recipient_uniqu": "124243",
            "sub_awardee_or_recipient_uei": None,
            "sub_awardee_or_recipient_legal_raw": "OVER HERE",
            "sub_dba_name": "OVER THERE",
            "sub_ultimate_parent_unique_ide": "3435",
            "sub_ultimate_parent_uei": None,
            "sub_ultimate_parent_legal_enti_raw": "SOMETHING ELSE",
            "sub_legal_entity_country_code_raw": "USA",
            "sub_legal_entity_country_name_raw": "UNITED STATES",
            "sub_legal_entity_state_code": "IA",
            "sub_legal_entity_state_name": "IOWA",
            "sub_legal_entity_zip": "50011",
            "sub_legal_entity_congressional_raw": "04",
            "sub_legal_entity_foreign_posta": None,
            "sub_legal_entity_city_name": "AMES",
            "sub_legal_entity_address_line1": "ADDRESS",
            "sub_business_types": "2F, G6, M8, OH, QU",
            "sub_place_of_perform_country_co_raw": "USA",
            "sub_place_of_perform_country_na": "UNITED STATES",
            "sub_place_of_perform_state_code": "IA",
            "sub_place_of_perform_state_name": "IOWA",
            "sub_place_of_performance_zip": "50011",
            "sub_place_of_perform_congressio_raw": "04",
            "sub_place_of_perform_city_name": "AMES",
            "sub_place_of_perform_street": "999 STREET ST",
            "subaward_description": "FY17 AE E-TEACHER PROGRAM AY18-19 COURSE DELIVERY (USING EDUCATIONAL TECHNOLOGY)",
            "sub_high_comp_officer1_full_na": None,
            "sub_high_comp_officer1_amount": None,
            "sub_high_comp_officer2_full_na": None,
            "sub_high_comp_officer2_amount": None,
            "sub_high_comp_officer3_full_na": None,
            "sub_high_comp_officer3_amount": None,
            "sub_high_comp_officer4_full_na": None,
            "sub_high_comp_officer4_amount": None,
            "sub_high_comp_officer5_full_na": None,
            "sub_high_comp_officer5_amount": None,
            "prime_id": 618687,
            "internal_id": "ASDFASFSAFSDFSFSD",
            "date_submitted": datetime(2019, 4, 4, 15, 59, 11),
            "report_type": None,
            "transaction_type": None,
            "program_title": None,
            "contract_agency_code": None,
            "contract_idv_agency_code": None,
            "grant_funding_agency_id": None,
            "grant_funding_agency_name": None,
            "federal_agency_name": "STATE, DEPARTMENT OF",
            "treasury_symbol": None,
            "dunsplus4": None,
            "recovery_model_q1": None,
            "recovery_model_q2": None,
            "compensation_q1": True,
            "compensation_q2": True,
            "high_comp_officer1_full_na": None,
            "high_comp_officer1_amount": None,
            "high_comp_officer2_full_na": None,
            "high_comp_officer2_amount": None,
            "high_comp_officer3_full_na": None,
            "high_comp_officer3_amount": None,
            "high_comp_officer4_full_na": None,
            "high_comp_officer4_amount": None,
            "high_comp_officer5_full_na": None,
            "high_comp_officer5_amount": None,
            "sub_id": 3641300,
            "sub_parent_id": 618687,
            "sub_federal_agency_id": "1900",
            "sub_federal_agency_name": "STATE, DEPARTMENT OF",
            "sub_funding_agency_id": None,
            "sub_funding_agency_name": None,
            "sub_funding_office_id": None,
            "sub_funding_office_name": None,
            "sub_naics": None,
            "sub_cfda_numbers": "19.421 Academic Exchange Programs - English Language Programs",
            "sub_dunsplus4": None,
            "sub_recovery_subcontract_amt": None,
            "sub_recovery_model_q1": None,
            "sub_recovery_model_q2": None,
            "sub_compensation_q1": False,
            "sub_compensation_q2": False,
            "award_id": None,
            "prime_award_group": "grant",
            "prime_award_type": None,
            "piid": None,
            "fain": "asdfasdfasdfs",
            "latest_transaction_id": None,
            "last_modified_date": None,
            "awarding_agency_id": None,
            "awarding_toptier_agency_name": None,
            "awarding_toptier_agency_abbreviation": None,
            "awarding_subtier_agency_name": None,
            "awarding_subtier_agency_abbreviation": None,
            "funding_agency_id": None,
            "funding_subtier_agency_abbreviation": None,
            "funding_subtier_agency_name": None,
            "funding_toptier_agency_abbreviation": None,
            "funding_toptier_agency_name": None,
            "cfda_id": None,
            "cfda_number": None,
            "cfda_title": None,
            "sub_fiscal_year": 2019,
            "sub_total_obl_bin": "<1M",
            "sub_awardee_or_recipient_legal": "OVER HERE",
            "sub_ultimate_parent_legal_enti": "SOMETHING ELSE",
            "business_type_code": None,
            "business_categories": [],
            "treasury_account_identifiers": None,
            "pulled_from": None,
            "type_of_contract_pricing": None,
            "type_set_aside": None,
            "extent_competed": None,
            "product_or_service_code": None,
            "product_or_service_description": None,
            "sub_legal_entity_country_code": "USA",
            "sub_legal_entity_country_name": "UNITED STATES",
            "sub_legal_entity_county_code": None,
            "sub_legal_entity_county_name": None,
            "sub_legal_entity_zip5": "50011",
            "sub_legal_entity_city_code": None,
            "sub_legal_entity_congressional": "04",
            "place_of_perform_scope": None,
            "sub_place_of_perform_country_co": "USA",
            "sub_place_of_perform_country_name": "UNITED STATES",
            "sub_place_of_perform_county_code": None,
            "sub_place_of_perform_county_name": None,
            "sub_place_of_perform_zip5": "50011",
            "sub_place_of_perform_city_code": None,
            "sub_place_of_perform_congressio": "04",
        },
        {
            "broker_created_at": datetime(2019, 6, 12, 12, 45, 58, 789296),
            "broker_updated_at": datetime(2019, 6, 12, 12, 45, 58, 789296),
            "broker_subaward_id": 3613892,
            "unique_award_key": "UNIQUE AWARD KEY A",
            "award_piid_fain": "0000",
            "parent_award_id": "000111000",
            "award_amount": Decimal("671.00"),
            "action_date": date(2010, 2, 15),
            "fy": "FY2010",
            "awarding_agency_code": "999",
            "awarding_agency_name": None,
            "awarding_sub_tier_agency_c": "1700",
            "awarding_sub_tier_agency_n": "DEPT OF THE NAVY",
            "awarding_office_code": "N62473",
            "awarding_office_name": "NAVFAC SOUTHWEST",
            "funding_agency_code": "999",
            "funding_agency_name": None,
            "funding_sub_tier_agency_co": "1700",
            "funding_sub_tier_agency_na": "DEPT OF THE NAVY",
            "funding_office_code": "M67399",
            "funding_office_name": "COMMANDING OFFICER",
            "awardee_or_recipient_uniqu": "12345",
            "awardee_or_recipient_uei": None,
            "awardee_or_recipient_legal": "12345 AGAIN",
            "dba_name": None,
            "ultimate_parent_unique_ide": "54321",
            "ultimate_parent_uei": None,
            "ultimate_parent_legal_enti": "54321 company",
            "legal_entity_country_code": "USA",
            "legal_entity_country_name": "UNITED STATES",
            "legal_entity_state_code": "OR",
            "legal_entity_state_name": None,
            "legal_entity_zip": "97223",
            "legal_entity_congressional": "01",
            "legal_entity_foreign_posta": None,
            "legal_entity_city_name": "TIGARD",
            "legal_entity_address_line1": "an address",
            "business_types": "Architecture and Engineering (A&E),Contracts,For-Profit Organization,SBA Certified Small Disadvantaged Business,Woman-Owned Business",
            "place_of_perform_country_co": "USA",
            "place_of_perform_country_na": "UNITED STATES",
            "place_of_perform_state_code": "CA",
            "place_of_perform_state_name": None,
            "place_of_performance_zip": "93517",
            "place_of_perform_congressio": "25",
            "place_of_perform_city_name": "San Diego",
            "place_of_perform_street": "456 street st",
            "award_description": "things and stuff",
            "naics": "541330",
            "naics_description": "ENGINEERING SERVICES",
            "cfda_numbers": None,
            "cfda_titles": None,
            "subaward_type": "sub-contract",
            "subaward_report_year": 2010,
            "subaward_report_month": 7,
            "subaward_number": "32324",
            "subaward_amount": Decimal("20.00"),
            "sub_action_date": date(2008, 2, 10),
            "sub_awardee_or_recipient_uniqu": "34143",
            "sub_awardee_or_recipient_uei": None,
            "sub_awardee_or_recipient_legal_raw": "O HAI",
            "sub_dba_name": None,
            "sub_ultimate_parent_unique_ide": "45545454",
            "sub_ultimate_parent_uei": None,
            "sub_ultimate_parent_legal_enti_raw": "TOENAIL TECHNOLOGY",
            "sub_legal_entity_country_code_raw": "USA",
            "sub_legal_entity_country_name_raw": "UNITED STATES",
            "sub_legal_entity_state_code": "CA",
            "sub_legal_entity_state_name": None,
            "sub_legal_entity_zip": "92124",
            "sub_legal_entity_congressional_raw": "52",
            "sub_legal_entity_foreign_posta": None,
            "sub_legal_entity_city_name": "SAN DIEGO",
            "sub_legal_entity_address_line1": "ANOTHER ADDRESS",
            "sub_business_types": "ARCHITECTURE AND ENGINEERING (A&E),CONTRACTS,FOR-PROFIT ORGANIZATION",
            "sub_place_of_perform_country_co_raw": "USA",
            "sub_place_of_perform_country_na": "UNITED STATES",
            "sub_place_of_perform_state_code": "CA",
            "sub_place_of_perform_state_name": None,
            "sub_place_of_performance_zip": "93517",
            "sub_place_of_perform_congressio_raw": "25",
            "sub_place_of_perform_city_name": "SAN DIEGO",
            "sub_place_of_perform_street": "654 STREET ST",
            "subaward_description": "ENGINEERING CONSULTING SERVICES",
            "sub_high_comp_officer1_full_na": None,
            "sub_high_comp_officer1_amount": None,
            "sub_high_comp_officer2_full_na": None,
            "sub_high_comp_officer2_amount": None,
            "sub_high_comp_officer3_full_na": None,
            "sub_high_comp_officer3_amount": None,
            "sub_high_comp_officer4_full_na": None,
            "sub_high_comp_officer4_amount": None,
            "sub_high_comp_officer5_full_na": None,
            "sub_high_comp_officer5_amount": None,
            "prime_id": 8,
            "internal_id": "ASDFASFSAFSADFSAFSDF",
            "date_submitted": datetime(2010, 11, 12, 18, 54, 7),
            "report_type": "regular",
            "transaction_type": "Federally Awarded Contract",
            "program_title": "Drainage Improvements",
            "contract_agency_code": "9700",
            "contract_idv_agency_code": "9700",
            "grant_funding_agency_id": None,
            "grant_funding_agency_name": None,
            "federal_agency_name": None,
            "treasury_symbol": "17-1106-",
            "dunsplus4": None,
            "recovery_model_q1": True,
            "recovery_model_q2": False,
            "compensation_q1": None,
            "compensation_q2": None,
            "high_comp_officer1_full_na": "person a",
            "high_comp_officer1_amount": Decimal("4600.00"),
            "high_comp_officer2_full_na": "person b",
            "high_comp_officer2_amount": Decimal("420.00"),
            "high_comp_officer3_full_na": "person c",
            "high_comp_officer3_amount": Decimal("4120.00"),
            "high_comp_officer4_full_na": "person q",
            "high_comp_officer4_amount": Decimal("4123.00"),
            "high_comp_officer5_full_na": "last person",
            "high_comp_officer5_amount": Decimal("4130.00"),
            "sub_id": 14,
            "sub_parent_id": 8,
            "sub_federal_agency_id": None,
            "sub_federal_agency_name": None,
            "sub_funding_agency_id": "1700",
            "sub_funding_agency_name": "DEPT OF THE NAVY",
            "sub_funding_office_id": "M67399",
            "sub_funding_office_name": "COMMANDING OFFICER",
            "sub_naics": "541330",
            "sub_cfda_numbers": None,
            "sub_dunsplus4": None,
            "sub_recovery_subcontract_amt": None,
            "sub_recovery_model_q1": False,
            "sub_recovery_model_q2": False,
            "sub_compensation_q1": None,
            "sub_compensation_q2": None,
            "award_id": None,
            "prime_award_group": "procurement",
            "prime_award_type": None,
            "piid": "0000",
            "fain": None,
            "latest_transaction_id": None,
            "last_modified_date": None,
            "awarding_agency_id": None,
            "awarding_toptier_agency_name": None,
            "awarding_toptier_agency_abbreviation": None,
            "awarding_subtier_agency_name": None,
            "awarding_subtier_agency_abbreviation": None,
            "funding_agency_id": None,
            "funding_subtier_agency_abbreviation": None,
            "funding_subtier_agency_name": None,
            "funding_toptier_agency_abbreviation": None,
            "funding_toptier_agency_name": None,
            "cfda_id": None,
            "cfda_number": None,
            "cfda_title": None,
            "sub_fiscal_year": 2008,
            "sub_total_obl_bin": "<1M",
            "sub_awardee_or_recipient_legal": "O HAI",
            "sub_ultimate_parent_legal_enti": "TOENAIL TECHNOLOGY",
            "business_type_code": None,
            "business_categories": [],
            "treasury_account_identifiers": None,
            "pulled_from": None,
            "type_of_contract_pricing": None,
            "type_set_aside": None,
            "extent_competed": None,
            "product_or_service_code": None,
            "product_or_service_description": None,
            "sub_legal_entity_country_code": "USA",
            "sub_legal_entity_country_name": "UNITED STATES",
            "sub_legal_entity_county_code": None,
            "sub_legal_entity_county_name": None,
            "sub_legal_entity_zip5": "92124",
            "sub_legal_entity_city_code": None,
            "sub_legal_entity_congressional": "52",
            "place_of_perform_scope": None,
            "sub_place_of_perform_country_co": "USA",
            "sub_place_of_perform_country_name": "UNITED STATES",
            "sub_place_of_perform_county_code": None,
            "sub_place_of_perform_county_name": None,
            "sub_place_of_perform_zip5": "93517",
            "sub_place_of_perform_city_code": None,
            "sub_place_of_perform_congressio": "25",
        },
        {
            "broker_created_at": datetime(2019, 6, 12, 12, 45, 58, 789296),
            "broker_updated_at": datetime(2019, 6, 12, 12, 45, 58, 789296),
            "broker_subaward_id": 3625475,
            "unique_award_key": None,
            "award_piid_fain": "0725",
            "parent_award_id": "PARENT_AWARD_ID_1",
            "award_amount": Decimal("7070.00"),
            "action_date": date(2017, 8, 29),
            "fy": "FY2017",
            "awarding_agency_code": None,
            "awarding_agency_name": None,
            "awarding_sub_tier_agency_c": "2100",
            "awarding_sub_tier_agency_n": "DEPT OF THE ARMY",
            "awarding_office_code": "W58RGZ",
            "awarding_office_name": "W6QK ACC-RSA",
            "funding_agency_code": None,
            "funding_agency_name": None,
            "funding_sub_tier_agency_co": "1700",
            "funding_sub_tier_agency_na": "DEPT OF THE NAVY",
            "funding_office_code": "N00024",
            "funding_office_name": "NAVSEA HQ",
            "awardee_or_recipient_uniqu": "12345",
            "awardee_or_recipient_uei": None,
            "awardee_or_recipient_legal": "12345 RECIPIENT",
            "dba_name": None,
            "ultimate_parent_unique_ide": None,
            "ultimate_parent_uei": None,
            "ultimate_parent_legal_enti": None,
            "legal_entity_country_code": "USA",
            "legal_entity_country_name": "UNITED STATES",
            "legal_entity_state_code": "AL",
            "legal_entity_state_name": None,
            "legal_entity_zip": "35806",
            "legal_entity_congressional": "05",
            "legal_entity_foreign_posta": None,
            "legal_entity_city_name": "HUNTSVILLE",
            "legal_entity_address_line1": "ADDRESS LINE 1",
            "business_types": "",
            "place_of_perform_country_co": "USA",
            "place_of_perform_country_na": "UNITED STATES",
            "place_of_perform_state_code": "AL",
            "place_of_perform_state_name": None,
            "place_of_performance_zip": "35806",
            "place_of_perform_congressio": "05",
            "place_of_perform_city_name": "HUNTSVILLE",
            "place_of_perform_street": "123 street st",
            "award_description": None,
            "naics": "336413",
            "naics_description": None,
            "cfda_numbers": None,
            "cfda_titles": None,
            "subaward_type": "sub-contract",
            "subaward_report_year": 2018,
            "subaward_report_month": 3,
            "subaward_number": "SUBAWARDNUM1",
            "subaward_amount": Decimal("621.04"),
            "sub_action_date": date(2018, 3, 21),
            "sub_awardee_or_recipient_uniqu": "54321",
            "sub_awardee_or_recipient_uei": None,
            "sub_awardee_or_recipient_legal_raw": "HI MOM",
            "sub_dba_name": None,
            "sub_ultimate_parent_unique_ide": None,
            "sub_ultimate_parent_uei": None,
            "sub_ultimate_parent_legal_enti_raw": None,
            "sub_legal_entity_country_code_raw": "USA",
            "sub_legal_entity_country_name_raw": "UNITED STATES",
            "sub_legal_entity_state_code": "CA",
            "sub_legal_entity_state_name": None,
            "sub_legal_entity_zip": "90501",
            "sub_legal_entity_congressional_raw": "36",
            "sub_legal_entity_foreign_posta": None,
            "sub_legal_entity_city_name": "TORRANCE",
            "sub_legal_entity_address_line1": "ANOTHER ADDRESS",
            "sub_business_types": "FOR-PROFIT ORGANIZATION,MANUFACTURER OF GOODS",
            "sub_place_of_perform_country_co_raw": "USA",
            "sub_place_of_perform_country_na": "UNITED STATES",
            "sub_place_of_perform_state_code": "CA",
            "sub_place_of_perform_state_name": None,
            "sub_place_of_performance_zip": "90501",
            "sub_place_of_perform_congressio_raw": "36",
            "sub_place_of_perform_city_name": "TORRANCE",
            "sub_place_of_perform_street": "321 STREET ST",
            "subaward_description": "MATERIALS IN SUPPORT OF THE RDS CONTRACT.",
            "sub_high_comp_officer1_full_na": None,
            "sub_high_comp_officer1_amount": None,
            "sub_high_comp_officer2_full_na": None,
            "sub_high_comp_officer2_amount": None,
            "sub_high_comp_officer3_full_na": None,
            "sub_high_comp_officer3_amount": None,
            "sub_high_comp_officer4_full_na": None,
            "sub_high_comp_officer4_amount": None,
            "sub_high_comp_officer5_full_na": None,
            "sub_high_comp_officer5_amount": None,
            "prime_id": 186875,
            "internal_id": "ABCDEF",
            "date_submitted": datetime(2018, 3, 23, 15, 1, 30),
            "report_type": "regular",
            "transaction_type": "Federally Awarded Contract",
            "program_title": None,
            "contract_agency_code": "9700",
            "contract_idv_agency_code": "9700",
            "grant_funding_agency_id": None,
            "grant_funding_agency_name": None,
            "federal_agency_name": None,
            "treasury_symbol": "17-1611",
            "dunsplus4": None,
            "recovery_model_q1": False,
            "recovery_model_q2": False,
            "compensation_q1": None,
            "compensation_q2": None,
            "high_comp_officer1_full_na": None,
            "high_comp_officer1_amount": None,
            "high_comp_officer2_full_na": None,
            "high_comp_officer2_amount": None,
            "high_comp_officer3_full_na": None,
            "high_comp_officer3_amount": None,
            "high_comp_officer4_full_na": None,
            "high_comp_officer4_amount": None,
            "high_comp_officer5_full_na": None,
            "high_comp_officer5_amount": None,
            "sub_id": 179029,
            "sub_parent_id": 186875,
            "sub_federal_agency_id": None,
            "sub_federal_agency_name": None,
            "sub_funding_agency_id": "1700",
            "sub_funding_agency_name": "DEPT OF THE NAVY",
            "sub_funding_office_id": "N00024",
            "sub_funding_office_name": "NAVSEA HQ",
            "sub_naics": "336413",
            "sub_cfda_numbers": None,
            "sub_dunsplus4": None,
            "sub_recovery_subcontract_amt": None,
            "sub_recovery_model_q1": False,
            "sub_recovery_model_q2": False,
            "sub_compensation_q1": None,
            "sub_compensation_q2": None,
            "award_id": None,
            "prime_award_group": "procurement",
            "prime_award_type": None,
            "piid": "0725",
            "fain": None,
            "latest_transaction_id": None,
            "last_modified_date": None,
            "awarding_agency_id": None,
            "awarding_toptier_agency_name": None,
            "awarding_toptier_agency_abbreviation": None,
            "awarding_subtier_agency_name": None,
            "awarding_subtier_agency_abbreviation": None,
            "funding_agency_id": None,
            "funding_subtier_agency_abbreviation": None,
            "funding_subtier_agency_name": None,
            "funding_toptier_agency_abbreviation": None,
            "funding_toptier_agency_name": None,
            "cfda_id": None,
            "cfda_number": None,
            "cfda_title": None,
            "sub_fiscal_year": 2018,
            "sub_total_obl_bin": "<1M",
            "sub_awardee_or_recipient_legal": "HI MOM",
            "sub_ultimate_parent_legal_enti": None,
            "business_type_code": None,
            "business_categories": [],
            "treasury_account_identifiers": None,
            "pulled_from": None,
            "type_of_contract_pricing": None,
            "type_set_aside": None,
            "extent_competed": None,
            "product_or_service_code": None,
            "product_or_service_description": None,
            "sub_legal_entity_country_code": "USA",
            "sub_legal_entity_country_name": "UNITED STATES",
            "sub_legal_entity_county_code": None,
            "sub_legal_entity_county_name": None,
            "sub_legal_entity_zip5": "90501",
            "sub_legal_entity_city_code": None,
            "sub_legal_entity_congressional": "36",
            "place_of_perform_scope": None,
            "sub_place_of_perform_country_co": "USA",
            "sub_place_of_perform_country_name": "UNITED STATES",
            "sub_place_of_perform_county_code": None,
            "sub_place_of_perform_county_name": None,
            "sub_place_of_perform_zip5": "90501",
            "sub_place_of_perform_city_code": None,
            "sub_place_of_perform_congressio": "36",
        },
    ]
    verify_delta_table_loaded_to_delta(
        spark,
        "subaward_search",
        s3_unittest_data_bucket,
        load_command="load_query_to_delta",
        dummy_data=expected_dummy_data,
    )
