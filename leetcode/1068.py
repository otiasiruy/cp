import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(sales, product, on='product_id', how='left')
    return merged[['product_name', 'year', 'price']]