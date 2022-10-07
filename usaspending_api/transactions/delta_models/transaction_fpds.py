from usaspending_api.common.data_classes import TransactionColumn

TRANSACTION_FPDS_COLUMN_INFO = [
    TransactionColumn("a_76_fair_act_action", "a_76_fair_act_action", "STRING", False),
    TransactionColumn("a_76_fair_act_action_desc", "a_76_fair_act_action_desc", "STRING", False),
    TransactionColumn("action_date", "action_date", "STRING", False),
    TransactionColumn("action_type", "action_type", "STRING", False),
    TransactionColumn("action_type_description", "action_type_description", "STRING", False),
    TransactionColumn("agency_id", "agency_id", "STRING", False),
    TransactionColumn("airport_authority", "airport_authority", "BOOLEAN", False),
    TransactionColumn("alaskan_native_owned_corpo", "alaskan_native_owned_corpo", "BOOLEAN", False),
    TransactionColumn("alaskan_native_servicing_i", "alaskan_native_servicing_i", "BOOLEAN", False),
    TransactionColumn("american_indian_owned_busi", "american_indian_owned_busi", "BOOLEAN", False),
    TransactionColumn("annual_revenue", "annual_revenue", "STRING", False),
    TransactionColumn("asian_pacific_american_own", "asian_pacific_american_own", "BOOLEAN", False),
    TransactionColumn("award_description", "award_description", "STRING", False),
    TransactionColumn("award_modification_amendme", "award_modification_amendme", "STRING", False),
    TransactionColumn("award_or_idv_flag", "award_or_idv_flag", "STRING", False),
    TransactionColumn("awardee_or_recipient_legal", "awardee_or_recipient_legal", "STRING", False),
    TransactionColumn("awardee_or_recipient_uei", "awardee_or_recipient_uei", "STRING", False),
    TransactionColumn("awardee_or_recipient_uniqu", "awardee_or_recipient_uniqu", "STRING", False),
    TransactionColumn("awarding_agency_code", "awarding_agency_code", "STRING", False),
    TransactionColumn("awarding_agency_name", "awarding_agency_name", "STRING", False),
    TransactionColumn("awarding_office_code", "awarding_office_code", "STRING", False),
    TransactionColumn("awarding_office_name", "awarding_office_name", "STRING", False),
    TransactionColumn("awarding_sub_tier_agency_c", "awarding_sub_tier_agency_c", "STRING", False),
    TransactionColumn("awarding_sub_tier_agency_n", "awarding_sub_tier_agency_n", "STRING", False),
    TransactionColumn("base_and_all_options_value", "base_and_all_options_value", "STRING", False),
    TransactionColumn("base_exercised_options_val", "base_exercised_options_val", "STRING", False),
    TransactionColumn("black_american_owned_busin", "black_american_owned_busin", "BOOLEAN", False),
    TransactionColumn("c1862_land_grant_college", "c1862_land_grant_college", "BOOLEAN", False),
    TransactionColumn("c1890_land_grant_college", "c1890_land_grant_college", "BOOLEAN", False),
    TransactionColumn("c1994_land_grant_college", "c1994_land_grant_college", "BOOLEAN", False),
    TransactionColumn("c8a_program_participant", "c8a_program_participant", "BOOLEAN", False),
    TransactionColumn("cage_code", "cage_code", "STRING", False),
    TransactionColumn("city_local_government", "city_local_government", "BOOLEAN", False),
    TransactionColumn("clinger_cohen_act_pla_desc", "clinger_cohen_act_pla_desc", "STRING", False),
    TransactionColumn("clinger_cohen_act_planning", "clinger_cohen_act_planning", "STRING", False),
    TransactionColumn("commercial_item_acqui_desc", "commercial_item_acqui_desc", "STRING", False),
    TransactionColumn("commercial_item_acquisitio", "commercial_item_acquisitio", "STRING", False),
    TransactionColumn("commercial_item_test_desc", "commercial_item_test_desc", "STRING", False),
    TransactionColumn("commercial_item_test_progr", "commercial_item_test_progr", "STRING", False),
    TransactionColumn("community_developed_corpor", "community_developed_corpor", "BOOLEAN", False),
    TransactionColumn("community_development_corp", "community_development_corp", "BOOLEAN", False),
    TransactionColumn("consolidated_contract", "consolidated_contract", "STRING", False),
    TransactionColumn("consolidated_contract_desc", "consolidated_contract_desc", "STRING", False),
    TransactionColumn("construction_wage_rat_desc", "construction_wage_rat_desc", "STRING", False),
    TransactionColumn("construction_wage_rate_req", "construction_wage_rate_req", "STRING", False),
    TransactionColumn("contingency_humanitar_desc", "contingency_humanitar_desc", "STRING", False),
    TransactionColumn("contingency_humanitarian_o", "contingency_humanitarian_o", "STRING", False),
    TransactionColumn("contract_award_type", "contract_award_type", "STRING", False),
    TransactionColumn("contract_award_type_desc", "contract_award_type_desc", "STRING", False),
    TransactionColumn("contract_bundling", "contract_bundling", "STRING", False),
    TransactionColumn("contract_bundling_descrip", "contract_bundling_descrip", "STRING", False),
    TransactionColumn("contract_financing", "contract_financing", "STRING", False),
    TransactionColumn("contract_financing_descrip", "contract_financing_descrip", "STRING", False),
    TransactionColumn("contracting_officers_desc", "contracting_officers_desc", "STRING", False),
    TransactionColumn("contracting_officers_deter", "contracting_officers_deter", "STRING", False),
    TransactionColumn("contracts", "contracts", "BOOLEAN", False),
    TransactionColumn("corporate_entity_not_tax_e", "corporate_entity_not_tax_e", "BOOLEAN", False),
    TransactionColumn("corporate_entity_tax_exemp", "corporate_entity_tax_exemp", "BOOLEAN", False),
    TransactionColumn("cost_accounting_stand_desc", "cost_accounting_stand_desc", "STRING", False),
    TransactionColumn("cost_accounting_standards", "cost_accounting_standards", "STRING", False),
    TransactionColumn("cost_or_pricing_data", "cost_or_pricing_data", "STRING", False),
    TransactionColumn("cost_or_pricing_data_desc", "cost_or_pricing_data_desc", "STRING", False),
    TransactionColumn("council_of_governments", "council_of_governments", "BOOLEAN", False),
    TransactionColumn("country_of_product_or_desc", "country_of_product_or_desc", "STRING", False),
    TransactionColumn("country_of_product_or_serv", "country_of_product_or_serv", "STRING", False),
    TransactionColumn("county_local_government", "county_local_government", "BOOLEAN", False),
    TransactionColumn("created_at", "created_at", "TIMESTAMP", False),
    TransactionColumn("current_total_value_award", "current_total_value_award", "STRING", False),
    TransactionColumn("detached_award_proc_unique", "detached_award_proc_unique", "STRING", False),
    TransactionColumn("detached_award_procurement_id", "detached_award_procurement_id", "INTEGER", False),
    TransactionColumn("division_name", "division_name", "STRING", False),
    TransactionColumn("division_number_or_office", "division_number_or_office", "STRING", False),
    TransactionColumn("dod_claimant_prog_cod_desc", "dod_claimant_prog_cod_desc", "STRING", False),
    TransactionColumn("dod_claimant_program_code", "dod_claimant_program_code", "STRING", False),
    TransactionColumn("domestic_or_foreign_e_desc", "domestic_or_foreign_e_desc", "STRING", False),
    TransactionColumn("domestic_or_foreign_entity", "domestic_or_foreign_entity", "STRING", False),
    TransactionColumn("domestic_shelter", "domestic_shelter", "BOOLEAN", False),
    TransactionColumn("dot_certified_disadvantage", "dot_certified_disadvantage", "BOOLEAN", False),
    TransactionColumn("economically_disadvantaged", "economically_disadvantaged", "BOOLEAN", False),
    TransactionColumn("educational_institution", "educational_institution", "BOOLEAN", False),
    TransactionColumn("emerging_small_business", "emerging_small_business", "BOOLEAN", False),
    TransactionColumn("entity_data_source", "entity_data_source", "STRING", False),
    TransactionColumn("epa_designated_produc_desc", "epa_designated_produc_desc", "STRING", False),
    TransactionColumn("epa_designated_product", "epa_designated_product", "STRING", False),
    TransactionColumn("evaluated_preference", "evaluated_preference", "STRING", False),
    TransactionColumn("evaluated_preference_desc", "evaluated_preference_desc", "STRING", False),
    TransactionColumn("extent_compete_description", "extent_compete_description", "STRING", False),
    TransactionColumn("extent_competed", "extent_competed", "STRING", False),
    TransactionColumn("fair_opportunity_limi_desc", "fair_opportunity_limi_desc", "STRING", False),
    TransactionColumn("fair_opportunity_limited_s", "fair_opportunity_limited_s", "STRING", False),
    TransactionColumn("fed_biz_opps", "fed_biz_opps", "STRING", False),
    TransactionColumn("fed_biz_opps_description", "fed_biz_opps_description", "STRING", False),
    TransactionColumn(
        "federal_action_obligation", "federal_action_obligation", "NUMERICTransactionColumn(23,2)", False
    ),
    TransactionColumn("federal_agency", "federal_agency", "BOOLEAN", False),
    TransactionColumn("federally_funded_research", "federally_funded_research", "BOOLEAN", False),
    TransactionColumn("for_profit_organization", "for_profit_organization", "BOOLEAN", False),
    TransactionColumn("foreign_funding", "foreign_funding", "STRING", False),
    TransactionColumn("foreign_funding_desc", "foreign_funding_desc", "STRING", False),
    TransactionColumn("foreign_government", "foreign_government", "BOOLEAN", False),
    TransactionColumn("foreign_owned_and_located", "foreign_owned_and_located", "BOOLEAN", False),
    TransactionColumn("foundation", "foundation", "BOOLEAN", False),
    TransactionColumn("funding_agency_code", "funding_agency_code", "STRING", False),
    TransactionColumn("funding_agency_name", "funding_agency_name", "STRING", False),
    TransactionColumn("funding_office_code", "funding_office_code", "STRING", False),
    TransactionColumn("funding_office_name", "funding_office_name", "STRING", False),
    TransactionColumn("funding_sub_tier_agency_co", "funding_sub_tier_agency_co", "STRING", False),
    TransactionColumn("funding_sub_tier_agency_na", "funding_sub_tier_agency_na", "STRING", False),
    TransactionColumn("government_furnished_desc", "government_furnished_desc", "STRING", False),
    TransactionColumn("government_furnished_prope", "government_furnished_prope", "STRING", False),
    TransactionColumn("grants", "grants", "BOOLEAN", False),
    TransactionColumn("hispanic_american_owned_bu", "hispanic_american_owned_bu", "BOOLEAN", False),
    TransactionColumn("hispanic_servicing_institu", "hispanic_servicing_institu", "BOOLEAN", False),
    TransactionColumn("historically_black_college", "historically_black_college", "BOOLEAN", False),
    TransactionColumn("historically_underutilized", "historically_underutilized", "BOOLEAN", False),
    TransactionColumn("hospital_flag", "hospital_flag", "BOOLEAN", False),
    TransactionColumn("housing_authorities_public", "housing_authorities_public", "BOOLEAN", False),
    TransactionColumn("idv_type", "idv_type", "STRING", False),
    TransactionColumn("idv_type_description", "idv_type_description", "STRING", False),
    TransactionColumn("indian_tribe_federally_rec", "indian_tribe_federally_rec", "BOOLEAN", False),
    TransactionColumn("information_technolog_desc", "information_technolog_desc", "STRING", False),
    TransactionColumn("information_technology_com", "information_technology_com", "STRING", False),
    TransactionColumn("inherently_government_desc", "inherently_government_desc", "STRING", False),
    TransactionColumn("inherently_government_func", "inherently_government_func", "STRING", False),
    TransactionColumn("initial_report_date", "initial_report_date", "STRING", False),
    TransactionColumn("inter_municipal_local_gove", "inter_municipal_local_gove", "BOOLEAN", False),
    TransactionColumn("interagency_contract_desc", "interagency_contract_desc", "STRING", False),
    TransactionColumn("interagency_contracting_au", "interagency_contracting_au", "STRING", False),
    TransactionColumn("international_organization", "international_organization", "BOOLEAN", False),
    TransactionColumn("interstate_entity", "interstate_entity", "BOOLEAN", False),
    TransactionColumn("joint_venture_economically", "joint_venture_economically", "BOOLEAN", False),
    TransactionColumn("joint_venture_women_owned", "joint_venture_women_owned", "BOOLEAN", False),
    TransactionColumn("labor_standards", "labor_standards", "STRING", False),
    TransactionColumn("labor_standards_descrip", "labor_standards_descrip", "STRING", False),
    TransactionColumn("labor_surplus_area_firm", "labor_surplus_area_firm", "BOOLEAN", False),
    TransactionColumn("last_modified", "last_modified", "STRING", False),
    TransactionColumn("legal_entity_address_line1", "legal_entity_address_line1", "STRING", False),
    TransactionColumn("legal_entity_address_line2", "legal_entity_address_line2", "STRING", False),
    TransactionColumn("legal_entity_address_line3", "legal_entity_address_line3", "STRING", False),
    TransactionColumn("legal_entity_city_name", "legal_entity_city_name", "STRING", False),
    TransactionColumn("legal_entity_congressional", "legal_entity_congressional", "STRING", False),
    TransactionColumn("legal_entity_country_code", "legal_entity_country_code", "STRING", False),
    TransactionColumn("legal_entity_country_name", "legal_entity_country_name", "STRING", False),
    TransactionColumn("legal_entity_county_code", "legal_entity_county_code", "STRING", False),
    TransactionColumn("legal_entity_county_name", "legal_entity_county_name", "STRING", False),
    TransactionColumn("legal_entity_state_code", "legal_entity_state_code", "STRING", False),
    TransactionColumn("legal_entity_state_descrip", "legal_entity_state_descrip", "STRING", False),
    TransactionColumn("legal_entity_zip4", "legal_entity_zip4", "STRING", False),
    TransactionColumn("legal_entity_zip5", "legal_entity_zip5", "STRING", False),
    TransactionColumn("legal_entity_zip_last4", "legal_entity_zip_last4", "STRING", False),
    TransactionColumn("limited_liability_corporat", "limited_liability_corporat", "BOOLEAN", False),
    TransactionColumn("local_area_set_aside", "local_area_set_aside", "STRING", False),
    TransactionColumn("local_area_set_aside_desc", "local_area_set_aside_desc", "STRING", False),
    TransactionColumn("local_government_owned", "local_government_owned", "BOOLEAN", False),
    TransactionColumn("major_program", "major_program", "STRING", False),
    TransactionColumn("manufacturer_of_goods", "manufacturer_of_goods", "BOOLEAN", False),
    TransactionColumn("materials_supplies_article", "materials_supplies_article", "STRING", False),
    TransactionColumn("materials_supplies_descrip", "materials_supplies_descrip", "STRING", False),
    TransactionColumn("minority_institution", "minority_institution", "BOOLEAN", False),
    TransactionColumn("minority_owned_business", "minority_owned_business", "BOOLEAN", False),
    TransactionColumn("multi_year_contract", "multi_year_contract", "STRING", False),
    TransactionColumn("multi_year_contract_desc", "multi_year_contract_desc", "STRING", False),
    TransactionColumn("multiple_or_single_aw_desc", "multiple_or_single_aw_desc", "STRING", False),
    TransactionColumn("multiple_or_single_award_i", "multiple_or_single_award_i", "STRING", False),
    TransactionColumn("municipality_local_governm", "municipality_local_governm", "BOOLEAN", False),
    TransactionColumn("naics", "naics", "STRING", False),
    TransactionColumn("naics_description", "naics_description", "STRING", False),
    TransactionColumn("national_interest_action", "national_interest_action", "STRING", False),
    TransactionColumn("national_interest_desc", "national_interest_desc", "STRING", False),
    TransactionColumn("native_american_owned_busi", "native_american_owned_busi", "BOOLEAN", False),
    TransactionColumn("native_hawaiian_owned_busi", "native_hawaiian_owned_busi", "BOOLEAN", False),
    TransactionColumn("native_hawaiian_servicing", "native_hawaiian_servicing", "BOOLEAN", False),
    TransactionColumn("nonprofit_organization", "nonprofit_organization", "BOOLEAN", False),
    TransactionColumn("number_of_actions", "number_of_actions", "STRING", False),
    TransactionColumn("number_of_employees", "number_of_employees", "STRING", False),
    TransactionColumn("number_of_offers_received", "number_of_offers_received", "STRING", False),
    TransactionColumn("officer_1_amount", "high_comp_officer1_amount", "NUMERICTransactionColumn(23,2)", True),
    TransactionColumn("officer_1_name", "high_comp_officer1_full_na", "STRING", False),
    TransactionColumn("officer_2_amount", "high_comp_officer2_amount", "NUMERICTransactionColumn(23,2)", True),
    TransactionColumn("officer_2_name", "high_comp_officer2_full_na", "STRING", False),
    TransactionColumn("officer_3_amount", "high_comp_officer3_amount", "NUMERICTransactionColumn(23,2)", True),
    TransactionColumn("officer_3_name", "high_comp_officer3_full_na", "STRING", False),
    TransactionColumn("officer_4_amount", "high_comp_officer4_amount", "NUMERICTransactionColumn(23,2)", True),
    TransactionColumn("officer_4_name", "high_comp_officer4_full_na", "STRING", False),
    TransactionColumn("officer_5_amount", "high_comp_officer5_amount", "NUMERICTransactionColumn(23,2)", True),
    TransactionColumn("officer_5_name", "high_comp_officer5_full_na", "STRING", False),
    TransactionColumn("ordering_period_end_date", "ordering_period_end_date", "STRING", False),
    TransactionColumn("organizational_type", "organizational_type", "STRING", False),
    TransactionColumn("other_minority_owned_busin", "other_minority_owned_busin", "BOOLEAN", False),
    TransactionColumn("other_not_for_profit_organ", "other_not_for_profit_organ", "BOOLEAN", False),
    TransactionColumn("other_statutory_authority", "other_statutory_authority", "STRING", False),
    TransactionColumn("other_than_full_and_o_desc", "other_than_full_and_o_desc", "STRING", False),
    TransactionColumn("other_than_full_and_open_c", "other_than_full_and_open_c", "STRING", False),
    TransactionColumn("parent_award_id", "parent_award_id", "STRING", False),
    TransactionColumn("partnership_or_limited_lia", "partnership_or_limited_lia", "BOOLEAN", False),
    TransactionColumn("performance_based_se_desc", "performance_based_se_desc", "STRING", False),
    TransactionColumn("performance_based_service", "performance_based_service", "STRING", False),
    TransactionColumn("period_of_perf_potential_e", "period_of_perf_potential_e", "STRING", False),
    TransactionColumn("period_of_performance_curr", "period_of_performance_curr", "STRING", False),
    TransactionColumn("period_of_performance_star", "period_of_performance_star", "STRING", False),
    TransactionColumn("piid", "piid", "STRING", False),
    TransactionColumn("place_of_manufacture", "place_of_manufacture", "STRING", False),
    TransactionColumn("place_of_manufacture_desc", "place_of_manufacture_desc", "STRING", False),
    TransactionColumn("place_of_perf_country_desc", "place_of_perf_country_desc", "STRING", False),
    TransactionColumn("place_of_perfor_state_desc", "place_of_perfor_state_desc", "STRING", False),
    TransactionColumn("place_of_perform_city_name", "place_of_perform_city_name", "STRING", False),
    TransactionColumn("place_of_perform_country_c", "place_of_perform_country_c", "STRING", False),
    TransactionColumn("place_of_perform_country_n", "place_of_perform_country_n", "STRING", False),
    TransactionColumn("place_of_perform_county_co", "place_of_perform_county_co", "STRING", False),
    TransactionColumn("place_of_perform_county_na", "place_of_perform_county_na", "STRING", False),
    TransactionColumn("place_of_perform_state_nam", "place_of_perform_state_nam", "STRING", False),
    TransactionColumn("place_of_perform_zip_last4", "place_of_perform_zip_last4", "STRING", False),
    TransactionColumn("place_of_performance_congr", "place_of_performance_congr", "STRING", False),
    TransactionColumn("place_of_performance_locat", "place_of_performance_locat", "STRING", False),
    TransactionColumn("place_of_performance_state", "place_of_performance_state", "STRING", False),
    TransactionColumn("place_of_performance_zip4a", "place_of_performance_zip4a", "STRING", False),
    TransactionColumn("place_of_performance_zip5", "place_of_performance_zip5", "STRING", False),
    TransactionColumn("planning_commission", "planning_commission", "BOOLEAN", False),
    TransactionColumn("port_authority", "port_authority", "BOOLEAN", False),
    TransactionColumn("potential_total_value_awar", "potential_total_value_awar", "STRING", False),
    TransactionColumn("price_evaluation_adjustmen", "price_evaluation_adjustmen", "STRING", False),
    TransactionColumn("private_university_or_coll", "private_university_or_coll", "BOOLEAN", False),
    TransactionColumn("product_or_service_co_desc", "product_or_service_co_desc", "STRING", False),
    TransactionColumn("product_or_service_code", "product_or_service_code", "STRING", False),
    TransactionColumn("program_acronym", "program_acronym", "STRING", False),
    TransactionColumn("program_system_or_equ_desc", "program_system_or_equ_desc", "STRING", False),
    TransactionColumn("program_system_or_equipmen", "program_system_or_equipmen", "STRING", False),
    TransactionColumn("pulled_from", "pulled_from", "STRING", False),
    TransactionColumn("purchase_card_as_paym_desc", "purchase_card_as_paym_desc", "STRING", False),
    TransactionColumn("purchase_card_as_payment_m", "purchase_card_as_payment_m", "STRING", False),
    TransactionColumn("receives_contracts_and_gra", "receives_contracts_and_gra", "BOOLEAN", False),
    TransactionColumn("recovered_materials_s_desc", "recovered_materials_s_desc", "STRING", False),
    TransactionColumn("recovered_materials_sustai", "recovered_materials_sustai", "STRING", False),
    TransactionColumn("referenced_idv_agency_desc", "referenced_idv_agency_desc", "STRING", False),
    TransactionColumn("referenced_idv_agency_iden", "referenced_idv_agency_iden", "STRING", False),
    TransactionColumn("referenced_idv_agency_name", "referenced_idv_agency_name", "STRING", False),
    TransactionColumn("referenced_idv_modificatio", "referenced_idv_modificatio", "STRING", False),
    TransactionColumn("referenced_idv_type", "referenced_idv_type", "STRING", False),
    TransactionColumn("referenced_idv_type_desc", "referenced_idv_type_desc", "STRING", False),
    TransactionColumn("referenced_mult_or_si_desc", "referenced_mult_or_si_desc", "STRING", False),
    TransactionColumn("referenced_mult_or_single", "referenced_mult_or_single", "STRING", False),
    TransactionColumn("referenced_multi_or_single", "referenced_mult_or_single", "STRING", False),
    TransactionColumn("research", "research", "STRING", False),
    TransactionColumn("research_description", "research_description", "STRING", False),
    TransactionColumn("sam_exception", "sam_exception", "STRING", False),
    TransactionColumn("sam_exception_description", "sam_exception_description", "STRING", False),
    TransactionColumn("sba_certified_8_a_joint_ve", "sba_certified_8_a_joint_ve", "BOOLEAN", False),
    TransactionColumn("school_district_local_gove", "school_district_local_gove", "BOOLEAN", False),
    TransactionColumn("school_of_forestry", "school_of_forestry", "BOOLEAN", False),
    TransactionColumn("sea_transportation", "sea_transportation", "STRING", False),
    TransactionColumn("sea_transportation_desc", "sea_transportation_desc", "STRING", False),
    TransactionColumn("self_certified_small_disad", "self_certified_small_disad", "BOOLEAN", False),
    TransactionColumn("service_disabled_veteran_o", "service_disabled_veteran_o", "BOOLEAN", False),
    TransactionColumn("small_agricultural_coopera", "small_agricultural_coopera", "BOOLEAN", False),
    TransactionColumn("small_business_competitive", "small_business_competitive", "BOOLEAN", False),
    TransactionColumn("small_disadvantaged_busine", "small_disadvantaged_busine", "BOOLEAN", False),
    TransactionColumn("sole_proprietorship", "sole_proprietorship", "BOOLEAN", False),
    TransactionColumn("solicitation_date", "solicitation_date", "DATE", True),
    TransactionColumn("solicitation_identifier", "solicitation_identifier", "STRING", False),
    TransactionColumn("solicitation_procedur_desc", "solicitation_procedur_desc", "STRING", False),
    TransactionColumn("solicitation_procedures", "solicitation_procedures", "STRING", False),
    TransactionColumn("state_controlled_instituti", "state_controlled_instituti", "BOOLEAN", False),
    TransactionColumn("subchapter_s_corporation", "subchapter_s_corporation", "BOOLEAN", False),
    TransactionColumn("subcontinent_asian_asian_i", "subcontinent_asian_asian_i", "BOOLEAN", False),
    TransactionColumn("subcontracting_plan", "subcontracting_plan", "STRING", False),
    TransactionColumn("subcontracting_plan_desc", "subcontracting_plan_desc", "STRING", False),
    TransactionColumn("the_ability_one_program", "the_ability_one_program", "BOOLEAN", False),
    TransactionColumn("total_obligated_amount", "total_obligated_amount", "STRING", False),
    TransactionColumn("township_local_government", "township_local_government", "BOOLEAN", False),
    TransactionColumn("transaction_id", None, "LONG NOT NULL", False),
    TransactionColumn("transaction_number", "transaction_number", "STRING", False),
    TransactionColumn("transit_authority", "transit_authority", "BOOLEAN", False),
    TransactionColumn("tribal_college", "tribal_college", "BOOLEAN", False),
    TransactionColumn("tribally_owned_business", "tribally_owned_business", "BOOLEAN", False),
    TransactionColumn("type_of_contract_pric_desc", "type_of_contract_pric_desc", "STRING", False),
    TransactionColumn("type_of_contract_pricing", "type_of_contract_pricing", "STRING", False),
    TransactionColumn("type_of_idc", "type_of_idc", "STRING", False),
    TransactionColumn("type_of_idc_description", "type_of_idc_description", "STRING", False),
    TransactionColumn("type_set_aside", "type_set_aside", "STRING", False),
    TransactionColumn("type_set_aside_description", "type_set_aside_description", "STRING", False),
    TransactionColumn("ultimate_parent_legal_enti", "ultimate_parent_legal_enti", "STRING", False),
    TransactionColumn("ultimate_parent_uei", "ultimate_parent_uei", "STRING", False),
    TransactionColumn("ultimate_parent_unique_ide", "ultimate_parent_unique_ide", "STRING", False),
    TransactionColumn("undefinitized_action", "undefinitized_action", "STRING", False),
    TransactionColumn("undefinitized_action_desc", "undefinitized_action_desc", "STRING", False),
    TransactionColumn("unique_award_key", "unique_award_key", "STRING", False),
    TransactionColumn("updated_at", "updated_at", "TIMESTAMP", False),
    TransactionColumn("us_federal_government", "us_federal_government", "BOOLEAN", False),
    TransactionColumn("us_government_entity", "us_government_entity", "BOOLEAN", False),
    TransactionColumn("us_local_government", "us_local_government", "BOOLEAN", False),
    TransactionColumn("us_state_government", "us_state_government", "BOOLEAN", False),
    TransactionColumn("us_tribal_government", "us_tribal_government", "BOOLEAN", False),
    TransactionColumn("vendor_alternate_name", "vendor_alternate_name", "STRING", False),
    TransactionColumn("vendor_alternate_site_code", "vendor_alternate_site_code", "STRING", False),
    TransactionColumn("vendor_doing_as_business_n", "vendor_doing_as_business_n", "STRING", False),
    TransactionColumn("vendor_enabled", "vendor_enabled", "STRING", False),
    TransactionColumn("vendor_fax_number", "vendor_fax_number", "STRING", False),
    TransactionColumn("vendor_legal_org_name", "vendor_legal_org_name", "STRING", False),
    TransactionColumn("vendor_location_disabled_f", "vendor_location_disabled_f", "STRING", False),
    TransactionColumn("vendor_phone_number", "vendor_phone_number", "STRING", False),
    TransactionColumn("vendor_site_code", "vendor_site_code", "STRING", False),
    TransactionColumn("veteran_owned_business", "veteran_owned_business", "BOOLEAN", False),
    TransactionColumn("veterinary_college", "veterinary_college", "BOOLEAN", False),
    TransactionColumn("veterinary_hospital", "veterinary_hospital", "BOOLEAN", False),
    TransactionColumn("woman_owned_business", "woman_owned_business", "BOOLEAN", False),
    TransactionColumn("women_owned_small_business", "women_owned_small_business", "BOOLEAN", False),
]

TRANSACTION_FPDS_COLUMNS = [col.silver_name for col in TRANSACTION_FPDS_COLUMN_INFO]

transaction_fpds_sql_string = rf"""
    CREATE OR REPLACE TABLE {{DESTINATION_TABLE}} (
        {", ".join([f'{col.silver_name} {col.delta_type}' for col in TRANSACTION_FPDS_COLUMN_INFO])}
    )
    USING DELTA
    LOCATION 's3a://{{SPARK_S3_BUCKET}}/{{DELTA_LAKE_S3_PATH}}/{{DESTINATION_DATABASE}}/{{DESTINATION_TABLE}}'
    """
