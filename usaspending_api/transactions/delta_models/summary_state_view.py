SUMMARY_STATE_VIEW_COLUMNS = {
    "duh": "STRING",
    "action_date": "DATE",
    "fiscal_year": "INTEGER",
    "type": "STRING",
    "distinct_awards": "ARRAY<STRING>",
    "pop_country_code": "STRING",
    "pop_state_code": "STRING",
    "generated_pragmatic_obligation": "NUMERIC(23,2)",
    "federal_action_obligation": "NUMERIC(23,2)",
    "original_loan_subsidy_cost": "NUMERIC(23,2)",
    "face_value_loan_guarantee": "NUMERIC(23,2)",
    "counts": "INTEGER",
}

summary_state_view_create_sql_string = fr"""
    CREATE OR REPLACE TABLE {{DESTINATION_TABLE}} (
        {", ".join([f'{key} {val}' for key, val in SUMMARY_STATE_VIEW_COLUMNS.items()])}
    )
    USING DELTA
    LOCATION 's3a://{{SPARK_S3_BUCKET}}/{{DELTA_LAKE_S3_PATH}}/{{DESTINATION_DATABASE}}/{{DESTINATION_TABLE}}'
"""

summary_state_view_string = rf"

 CREATE OR REPLACE TABLE {{DESTINATION_TABLE}} (

 SELECT,

      -- Deterministic Unique Hash (DUH) created for view concurrent refresh,

      MD5(array_to_string(sort(array_agg(transaction_normalized.id::int)), ' '))::uuid AS duh,,

      transaction_normalized.action_date,,

      transaction_normalized.fiscal_year,,

      transaction_normalized.type,,

      array_to_string(array_agg(DISTINCT transaction_normalized.award_id), ',') AS distinct_awards,,

    ,

      COALESCE(transaction_fpds.place_of_perform_country_c, transaction_fabs.place_of_perform_country_c, 'USA') AS pop_country_code,,

      COALESCE(transaction_fpds.place_of_performance_state, transaction_fabs.place_of_perfor_state_code) AS pop_state_code,,

    ,

      COALESCE(SUM(CASE,

        WHEN transaction_normalized.type IN('07','08') THEN transaction_normalized.original_loan_subsidy_cost,

        ELSE transaction_normalized.federal_action_obligation,

      END), 0)::NUMERIC(23, 2) AS generated_pragmatic_obligation,,

      COALESCE(SUM(transaction_normalized.federal_action_obligation), 0)::NUMERIC(23, 2) AS federal_action_obligation,,

      COALESCE(SUM(transaction_normalized.original_loan_subsidy_cost), 0)::NUMERIC(23, 2) AS original_loan_subsidy_cost,,

      COALESCE(SUM(transaction_normalized.face_value_loan_guarantee), 0)::NUMERIC(23, 2) AS face_value_loan_guarantee,,

      count(*) AS counts,

    FROM,

      transaction_normalized,

    LEFT OUTER JOIN,

      transaction_fpds ON (transaction_normalized.id = transaction_fpds.transaction_id),

    LEFT OUTER JOIN,

      transaction_fabs ON (transaction_normalized.id = transaction_fabs.transaction_id),

    WHERE,

      transaction_normalized.action_date >= '2007-10-01' AND,

      COALESCE(transaction_fpds.place_of_perform_country_c, transaction_fabs.place_of_perform_country_c, 'USA') = 'USA' AND,

      COALESCE(transaction_fpds.place_of_performance_state, transaction_fabs.place_of_perfor_state_code) IS NOT NULL,

    GROUP BY,

      transaction_normalized.action_date,,

      transaction_normalized.fiscal_year,,

      transaction_normalized.type,,

      pop_country_code,,

      pop_state_code\\

    )

    USING DELTA

    LOCATION 's3a://{{SPARK_S3_BUCKET}}/{{DELTA_LAKE_S3_PATH}}/{{DESTINATION_DATABASE}}/{{DESTINATION_TABLE}}'
"
