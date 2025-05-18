import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    nf = visits[~visits['visit_id'].isin(transactions['visit_id'])]
    return nf['customer_id'].value_counts().reset_index(name='count_no_trans')