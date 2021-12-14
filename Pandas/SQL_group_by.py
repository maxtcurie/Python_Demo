from SQL_table_reader import sql_table_to_df
import pandas as pd

order_df=sql_table_to_df('Order.txt')
print(order_df)
#similar to JOIN in df
output=order_df.groupby(['customer_id','product_id']).count()
print(output)