"""
Name:  FileToList.py
Author:  Lee Brown
Created:  11/10/2020
Last Updated:  11/11/2020
Purpose:  To convert a file such as .txt to a list.
Description:  This module will take a file, split it using '\n', and return the
              result.

Functions:
 - read_to_list(file):  Input the exact location of a file.  Get a list of each
                        line's content.  List[0] will correspond to line 0's
                        content, List[1] will correspond to line 1's content,
                        etc.  Input must be in the following format:
                        'C:\\...\\fileName.extention'
"""

def read_to_list(input_file):
    input_file = open(input_file, 'r')
    file_data = input_file.read()
    file_data_list = file_data.split("\n")
    input_file.close()

    return file_data_list
