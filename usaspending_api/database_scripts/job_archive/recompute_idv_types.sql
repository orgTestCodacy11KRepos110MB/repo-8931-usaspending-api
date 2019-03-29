-- Created Date: 2018-11-26 (jira ticket)
-- Last Modified: 2019-04-01
-- Expected CLI: psql -v ON_ERROR_STOP=1 -c '\timing' -f recompute_idv_types.sql $DATABASE_URL
--
-- Purpose: Recalculate the IDV IDC sub-types (IDV_B_*) using `type_of_idc_description` which is
--    more populated than `type_of_idc`. Fallback is to store IDV_B as currently.
--    For generic IDV_B types, store 'Indefinite Delivery Contract' as the `type_description`

DO $$ BEGIN RAISE NOTICE 'Updating transaction_normalized'; END $$;
BEGIN;
UPDATE transaction_normalized tn
SET
    type = CASE
        WHEN pulled_from IS DISTINCT FROM 'IDV' THEN contract_award_type
        WHEN idv_type = 'B' AND type_of_idc IS NOT NULL THEN CONCAT('IDV_B_', type_of_idc::text)
        WHEN idv_type = 'B' AND type_of_idc IS NULL and type_of_idc_description = 'INDEFINITE DELIVERY / REQUIREMENTS' THEN 'IDV_B_A'
        WHEN idv_type = 'B' AND type_of_idc IS NULL and type_of_idc_description = 'INDEFINITE DELIVERY / INDEFINITE QUANTITY' THEN 'IDV_B_B'
        WHEN idv_type = 'B' AND type_of_idc IS NULL and type_of_idc_description = 'INDEFINITE DELIVERY / DEFINITE QUANTITY' THEN 'IDV_B_C'
        ELSE CONCAT('IDV_', idv_type::text) END,
    type_description = CASE
        WHEN pulled_from IS DISTINCT FROM 'IDV' THEN contract_award_type_desc
        WHEN idv_type = 'B' AND (type_of_idc_description IS DISTINCT FROM NULL AND type_of_idc_description <> 'NAN') THEN type_of_idc_description
        WHEN idv_type = 'B' THEN 'INDEFINITE DELIVERY CONTRACT'
        ELSE idv_type_description END
FROM transaction_fpds t
WHERE t.transaction_id = tn.id AND t.pulled_from = 'IDV' and t.idv_type = 'B';

DO $$ BEGIN RAISE NOTICE 'Completed transaction_normalized'; END $$;
DO $$ BEGIN RAISE NOTICE 'Updating awards'; END $$;

WITH temp_type_and_category AS (
    SELECT
        tn.id,
        tn.type,
        tn.type_description,
        CASE
            WHEN tn.type = '09' THEN 'insurance'
            WHEN tn.type = '11' THEN 'other'
            WHEN tn.type in ('06', '10') THEN 'direct payment'
            WHEN tn.type in ('07', '08') THEN 'loans'
            WHEN tn.type IN ('A', 'B', 'C', 'D') THEN 'contract'
            WHEN tn.type IN ('02', '03', '04', '05') THEN 'grant'
            WHEN tn.type ~~ 'IDV%' THEN 'idv'
            ELSE NULL END AS category
    FROM transaction_normalized tn
)
UPDATE awards a
SET
    category = t.category,
    type = t.type,
    type_description = t.type_description
FROM
    temp_type_and_category t
WHERE
    t.id = a.latest_transaction_id AND
    (t.category IS DISTINCT FROM a.category OR t.type IS DISTINCT FROM a.type);

DO $$ BEGIN RAISE NOTICE 'Completed awards'; END $$;
DO $$ BEGIN RAISE NOTICE 'Updating subaward'; END $$;

UPDATE subaward
SET prime_award_type = a.type
FROM awards a
WHERE
    subaward.award_id = a.id AND
    subaward.prime_award_type IS DISTINCT FROM a.type;

DO $$ BEGIN RAISE NOTICE 'Completed subaward'; END $$;
DO $$ BEGIN RAISE NOTICE 'Committing'; END $$;

COMMIT;

DO $$ BEGIN RAISE NOTICE 'Running three `vacuum analyze` statements'; END $$;

VACUUM ANALYZE transaction_normalized;
VACUUM ANALYZE awards;
VACUUM ANALYZE subaward;