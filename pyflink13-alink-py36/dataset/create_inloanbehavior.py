from process_schema import *
import csv
import os

column_names, column_types = get_columns_and_types()
column_types_set = list(set(column_types))
column_types_list_lower = list(map(lambda x: str(x).lower(), column_types))
# print(column_types_list_lower)

in_loan_behavior_file = "./in_loan_behavior.csv"

value_map = {
    'varchar': "i love meituan",
    'datetime': "2021-01-01 00:00:00",
    'int': 123,
    'decimal': 10.123456789,
    'double': 123.456,
    'bigint': 123456789,
}

example_value_list = []
for type_str in column_types_list_lower:
    example_value_list.append(value_map[type_str])


# print(len(example_value_list))
# print(example_value_list)


def create_inloanbehavior():
    with open(in_loan_behavior_file, 'w') as f:
        writer = csv.writer(f)
        num = 1000000
        while num > 0:
            writer.writerow(example_value_list)
            num -= 1
    print(os.path.getsize(in_loan_behavior_file)/float(1024*1024))


create_inloanbehavior()
