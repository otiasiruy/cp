import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    filtered = students[students['student_id'] == 101]
    return filtered[['name', 'age']]