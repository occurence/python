-- Find the minimum number of affected customers
SELECT 
  MIN(affected_customers) AS min_affected_customers 
FROM 
  grid
-- Only retrieve rows where demand_loss_mw has a value
WHERE
  --demand_loss_mw IS NOT NULL;
  demand_loss_mw <> '';

-- Find the maximum number of affected customers
SELECT 
  MAX(affected_customers) AS max_affected_customers 
FROM 
  grid
-- Only retrieve rows where demand_loss_mw has a value
WHERE 
  -- demand_loss_mw IS NOT NULL;
  demand_loss_mw <> '';

-- Find the average number of affected customers
SELECT 
  -- AVG(affected_customers) AS avg_affected_customers
  AVG(CAST (affected_customers AS FLOAT)) AS avg_affected_customers
FROM 
  grid
-- Only retrieve rows where demand_loss_mw has a value
WHERE 
  -- demand_loss_mw IS NOT NULL;
  demand_loss_mw <> '';