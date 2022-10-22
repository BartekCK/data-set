from enum import Enum
from faker import Faker
import random
import pandas as pd
from datetime import datetime
import numpy as np

fake = Faker()


class TeamType(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class ContractType(Enum):
    FULL_TIME = 1
    PART_TIME = 2
    HOURS = 3


def rand_contract_type() -> ContractType:
    value = random.randint(1, 100)

    if value <= 50:
        return ContractType.FULL_TIME
    if value <= 80:
        return ContractType.PART_TIME

    return ContractType.HOURS


def create_employee(employee_id: int, contract_type: ContractType):
    return {
        'id': employee_id,
        'name': fake.name(),
        "employment_date": fake.date_between_dates(date_start=datetime(1950, 1, 1), date_end=datetime(1990, 12, 31)),
        "contract_type": contract_type.name,
        "team": TeamType(random.randint(1, len(TeamType))).name
    }


def create_employee_list(employee_number: int):
    employee_list = []

    for i in range(employee_number):
        contract_type = rand_contract_type()
        employee_id = i + 1

        employee = create_employee(employee_id, contract_type)
        employee_list.append(employee)

    return employee_list


def map_array_into_data_frame(arr):
    return pd.DataFrame(arr)


employee_list = create_employee_list(5000)
worker_df = map_array_into_data_frame(employee_list)

# SECOND LECTURE

def make_widget_data(num):
    
    fake_widgets = [{'Item Number':id(y),
                     'Step 1':np.random.gamma(shape=3, scale=1),
                     'Step 2':np.random.normal(5), 
                     'Step 3':np.random.exponential(4)} for y in range(num)]
    
    return fake_widgets


dfs_list = []

for index, row in worker_df.iterrows():
    

    
    if row['contract_type'] == ContractType.FULL_TIME:
        num_widgets = random.randrange(500, 1000)
    elif row['contract_type'] == ContractType.PART_TIME:
        num_widgets = random.randrange(100, 500)
    else:
        num_widgets = random.randrange(1, 1000)
    
    # make widgets for each worker
    tmp_widgets = pd.DataFrame(make_widget_data(num=num_widgets))
    
    tmp_widgets['Worker ID'] = row['id']
    

    tmp_widgets['Item Number'] = tmp_widgets['Item Number'].astype('str')+ '-' + tmp_widgets['Worker ID'].astype('str')
    

    dfs_list.append(tmp_widgets)
    
widget_df = pd.concat(dfs_list)
print(widget_df.shape)
widget_df.head()

worker_df.to_csv('./workers.csv', index=False)
widget_df.to_csv('./widgets.csv', index=False)