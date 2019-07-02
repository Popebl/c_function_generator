#coding: utf-8
import sys
import csv

from config import hFile

def generate_function_header(func_obj):
    with open(hFile, 'a') as file_object:
        file_object.write(func_obj.get_function_type() + ' ')
        file_object.write(func_obj.get_function_name() + '(')
        loop_cnt = 0
        for para_tuple in func_obj.para_list:
            if loop_cnt > 0:
                file_object.write(', ')
            file_object.write(para_tuple[0] + ' ' + para_tuple[1])
            loop_cnt += 1

        file_object.write(');\n')

