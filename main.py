from enum import Enum
from faker import Faker
import random
import pandas as pd
from datetime import datetime

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
employee_list_data_frame = map_array_into_data_frame(employee_list)
print(employee_list_data_frame)
