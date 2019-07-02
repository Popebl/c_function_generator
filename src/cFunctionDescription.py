#coding: utf-8
import sys
import csv

from config import cFile

def generate_function_description(func_obj):
    with open(cFile, 'a') as file_object:
        file_object.write('/*************\n')
        file_object.write(func_obj.get_function_type() + ' ')
        file_object.write(func_obj.get_function_name() + '(')
        loop_cnt = 0
        for para_tuple in func_obj.para_list:

        file_object.write('****************/\n')

