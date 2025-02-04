-- Retrieve all columns
SELECT 
  * 
FROM 
  grid 
  -- Return only rows where demand_loss_mw is missing or unknown  
WHERE 
  -- demand_loss_mw IS NULL;
  demand_loss_mw = '';

-- Retrieve all columns
SELECT 
  * 
FROM 
  grid 
  -- Return rows where demand_loss_mw is not missing or unknown   
WHERE 
  -- demand_loss_mw IS NOT NULL;
  demand_loss_mw <> '';