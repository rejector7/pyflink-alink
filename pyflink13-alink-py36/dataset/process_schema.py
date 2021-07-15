import csv

raw_schema_file = "./IN_LOAN_BEHAVIOR.txt"
processed_schema_file = "./IN_LOAN_BEHAVIOR_02.txt"
# columns_types_file = "./columns_types.csv"
processed_schema = []


def all_alpnum_underline(words: str) -> bool:
    if '.' in words:
        return False
    for w in words.strip():
        if '\u4e00' <= w <= '\u9fff':
            return False
        else:
            continue
    return True


# print(exist_chinese('fa_dfas'))
# print(exist_chinese('测试'))
def process_schema():
    with open(raw_schema_file, encoding='utf-8') as input_f:
        lines = input_f.readlines()
        for line in lines:
            if all_alpnum_underline(line):
                processed_schema.append(line)
            else:
                continue
    with open(processed_schema_file, 'w') as output_f:
        for line in processed_schema:
            output_f.write(line)


# process_schema()

def get_columns_and_types():
    column_names = []
    column_types = []
    with open(processed_schema_file) as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if i % 2 == 0:
                column_names.append(line.strip())
            else:
                column_types.append(line.strip())
    return column_names, column_types


#

