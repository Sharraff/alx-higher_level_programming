#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx >= len(my_list) or idx < 0:
        copylist = my_list.copy()
        return copylist
    else:
        del(my_list[idx])
        copylist = my_list.copy()
    return copylist
