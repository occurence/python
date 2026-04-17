import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=datacamp;" "Trusted_Connection=True;" )

query = """
SELECT 
  InvoiceLineId,
  UnitPrice, 
  quantity,
  BillingState
  -- Specify the source table
FROM invoiceline
  -- Complete the join to the invoice table
LEFT JOIN invoice
ON invoiceline.InvoiceId = invoice.InvoiceId;
"""

df = pd.read_sql(query, conn)
print(df)
conn.close()