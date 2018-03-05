--------------------------------------------------------
-- Created using matview_sql_generator.py             --
--    The SQL definition is stored in a json file     --
--    Look in matview_generator for the code.         --
--                                                    --
--         !!DO NOT DIRECTLY EDIT THIS FILE!!         --
--------------------------------------------------------
ALTER MATERIALIZED VIEW IF EXISTS summary_view_psc_codes RENAME TO summary_view_psc_codes_old;
ALTER INDEX IF EXISTS idx_cb0c2fed$c2f_unique_pk RENAME TO idx_cb0c2fed$c2f_unique_pk_old;
ALTER INDEX IF EXISTS idx_cb0c2fed$c2f_action_date RENAME TO idx_cb0c2fed$c2f_action_date_old;
ALTER INDEX IF EXISTS idx_cb0c2fed$c2f_type RENAME TO idx_cb0c2fed$c2f_type_old;
ALTER INDEX IF EXISTS idx_cb0c2fed$c2f_pulled_from RENAME TO idx_cb0c2fed$c2f_pulled_from_old;

ALTER MATERIALIZED VIEW summary_view_psc_codes_temp RENAME TO summary_view_psc_codes;
ALTER INDEX idx_cb0c2fed$c2f_unique_pk_temp RENAME TO idx_cb0c2fed$c2f_unique_pk;
ALTER INDEX idx_cb0c2fed$c2f_action_date_temp RENAME TO idx_cb0c2fed$c2f_action_date;
ALTER INDEX idx_cb0c2fed$c2f_type_temp RENAME TO idx_cb0c2fed$c2f_type;
ALTER INDEX idx_cb0c2fed$c2f_pulled_from_temp RENAME TO idx_cb0c2fed$c2f_pulled_from;
