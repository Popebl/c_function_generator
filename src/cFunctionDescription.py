#coding: utf-8
import sys
import csv

from config import cFile

def generate_function_description(func_obj):
    with open(cFile, 'a') as file_object:
        file_object.write('/*******************************************************************************\n')
        #file_object.write('* @brief ' + func_obj.get_function_type() + ' ')
        file_object.write('* @brief ' + func_obj.get_function_name() + '\n\n')
        for para_tuple in func_obj.para_list:
            file_object.write('* @param ' + para_tuple[1] + '\n')
        file_object.write('* \n')
        file_object.write('* @return \n')
        file_object.write('* \n')
        file_object.write('*******************************************************************************/\n')

