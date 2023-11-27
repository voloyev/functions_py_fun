from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Table:
    file_path: str
    class_name: str
    method_name: str

def get_sub_table(item: str, value: str):
    return [Table(item, value, '1')]

def get_location(file_path: Optional[str], class_name: Optional[str] = None, method_name: Optional[str] = None) -> List[Optional[str]]:
    return [file_path, class_name, method_name]

def location(item: str, value: str):
    sub_table = get_sub_table(item, value)
    if(len(sub_table) == 0):
        raise Exception
    else:
        first_row = sub_table[0]
    match item:
        case 'class':
            return get_location(first_row.file_path, first_row.class_name, None)
        case 'method':
            return get_location(first_row.file_path, first_row.class_name, first_row.method_name)
        case 'file':
            return get_location(first_row.file_path, None, None)
        case _:
            raise Exception("Item must be :class, :method, or :file")



def location_v2(item: str, value: str):
    sub_table = get_sub_table(item, value)
    assert_sub_table_has_data(item, sub_table, value)
    first_row = sub_table[0]

    match item:
        case 'class':
            return get_location(first_row.file_path, first_row.class_name, None)
        case 'method':
            return get_location(first_row.file_path, first_row.class_name, first_row.method_name)
        case 'file':
            return get_location(first_row.file_path, None, None)
        case _:
            raise Exception("Item must be :class, :method, or :file")

def assert_sub_table_has_data(item, sub_table, value):
    if (sub_table.length==0):
        raise Exception(f"The {item} '{value}' does not have any rows in the analysis table")
