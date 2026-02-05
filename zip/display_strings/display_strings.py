from collections import defaultdict
from typing import Dict


def translate(s: str) -> str:
  return f"Translated: {s}"

def translate_map(str_map: Dict[str, str]) -> None:
    for value in str_map.values():
        if value[-3:] == "_id":
            return
    
    for key, value in str_map.items():
        new_str = translate(value)
        str_map[key] = new_str
        
def is_valid_for_change(str_map) -> bool:
        for value in str_map.values():
            if isinstance(value, str):
                if value[-3:] == "_id":
                    return False
            else:
                if not is_valid_for_change(value):
                    return False
        return True
    
def translate_nested(str_map) -> None:
    if not str_map:
        return
    
    def change_nested(str_map) -> None:
        if not str_map:
            return
        
        for key, value in str_map.items():
            if isinstance(value, str):
                new_str = translate(value)
                str_map[key] = new_str
            else:
                change_nested(value)
        
    if is_valid_for_change(str_map):
        change_nested(str_map)
        
def find_most_freq(str_map) -> str:
    if not str_map or not is_valid_for_change(str_map):
        return ""

    freq_map = defaultdict(int)
    def count_values(value):
        if isinstance(value, str):
            freq_map[value] += 1
        else:
            for str_value in value.values():
                count_values(str_value)
    
    count_values(str_map)
    max_count = max(freq_map.values())
    for key, value in freq_map.items():
        if value == max_count:
            return key
        
    return ""
                    
        

        

        
                


def print_map(str_map):
    for key, value in str_map.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    map1 = {
        
        'id_1': 'Bakery goods',
        'id_2': 'Ice cream',
        }
    
    map2 = {
        'id_1': 'bakery_id',
        'id_2': 'Ice cream',
        }
    
    map3 = {
        'id_1': 'bakery_id',
        'id_2': 'Ice cream',
    }
