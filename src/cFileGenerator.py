#coding: utf-8
import sys
import csv

from sys import version_info
from config import csvFile, author_name

from cFunctionDescription import generate_function_description
from cFunctionBody import generate_function
from cFunctionHeader import generate_function_header
class function:
    def __init__(self, func_ldFlag, func_type, func_prefix, func_operate, func_target, func_author):
        self.func_ldFlag = func_ldFlag
        self.func_type = func_type
        self.func_prefix = func_prefix
        self.func_operate = func_operate
        self.func_target = func_target
        self.func_author = func_author
        self.para_list = []

    def get_function_ldFlag(self):
        return self.func_ldFlag

    def get_function_type(self):
        return self.func_type

    def get_function_name(self):
        return self.func_prefix + '_' + self.func_operate + '_' + self.func_target
    
    def get_function_author(self):
        return self.author

    def add_para(para_tuple):
        self.para_list.append(para_tuple)

func_obj_list = []

if __name__ == "__main__":
    if version_info.major != 3:
        raise Exception("Olny work on python 3.x")

    csv_file = csv.reader(open(csvFile, 'r'))
    for line in csv_file:
        new_function_obj = \
            function(line[0],line[1],line[2],line[3],line[4],author_name)
        
        for para_loopCnt in range(5,len(line),2):
            if line[para_loopCnt] and line[para_loopCnt]:
                para_tuple = (line[para_loopCnt], line[para_loopCnt + 1])
                new_function_obj.para_list.append(para_tuple)

        func_obj_list.append(new_function_obj)


    for func_obj in func_obj_list:
        generate_function_description(func_obj)
        generate_function(func_obj)
        generate_function_header(func_obj)


