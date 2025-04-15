SELECT 
  nerc_region, 
  SUM(CAST(demand_loss_mw AS FLOAT)) AS demand_loss 
FROM 
  grid 
  -- Remove the WHERE clause
-- WHERE demand_loss_mw  IS NOT NULL
GROUP BY 
  nerc_region 
  -- Enter a new HAVING clause so that the sum of demand_loss_mw is greater than 10000
HAVING 
  SUM(CAST(demand_loss_mw AS FLOAT)) > 10000
ORDER BY 
  demand_loss DESC;