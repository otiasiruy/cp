import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    bonus = []
    for s in employees['salary']:
        bonus.append(s*2)
    employees['bonus'] = bonus
    return employees