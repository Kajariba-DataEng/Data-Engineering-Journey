
-- Step 1: Create the 'Suitcase' (Array) of data
WITH raw_years AS (
  SELECT ['2000', '2021', 'bad_data', '2024'] AS year_list
)

-- Step 2: Unpack and Clean the data
SELECT 
  -- Use SAFE_CAST so 'bad_data' becomes NULL instead of crashing the query
  SAFE_CAST(year_val AS INT64) AS cleaned_year,
  
  -- Apply the same Leap Year logic you wrote in Python
  CASE 
    WHEN MOD(SAFE_CAST(year_val AS INT64), 400) = 0 THEN 'Leap Year'
    WHEN MOD(SAFE_CAST(year_val AS INT64), 100) = 0 THEN 'Not a Leap Year'
    WHEN MOD(SAFE_CAST(year_val AS INT64), 4) = 0 THEN 'Leap Year'
    ELSE 'Normal Year'
  END AS leap_status
FROM raw_years, 
-- This is the "Correlated Join" that unpacks the suitcase
UNNEST(year_list) AS year_val
WHERE SAFE_CAST(year_val AS INT64) IS NOT NULL;
