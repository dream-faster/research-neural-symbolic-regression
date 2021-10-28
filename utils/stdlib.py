
from typing import List

def flatten(list_of_lists: List) -> List:
    if not isinstance(list_of_lists, list):
        return [list_of_lists]

    flat_list = []
    for item in list_of_lists:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)

    return flat_list

def flatten_and_pad(list_of_lists: List, start_token, end_token) -> List:
    '''Flatten an abritrary nested list and pad the lists with start_token and end_token'''
    if not isinstance(list_of_lists, list):
        return [list_of_lists]

    flat_list = [start_token]
    for item in list_of_lists:
        if isinstance(item, list):
            flat_list.extend(flatten_and_pad(item, start_token, end_token))
        else:
            flat_list.append(item)
    flat_list.append(end_token)

    return flat_list