# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 14:54:05 2022

@author: Arthur
"""

with open("D:/adventOfCode2022/aoc_input_1") as file: # Use file to refer to the file object
   data = file.read()

data = data.split("\n\n")

for (i in 0:len(data)-1){
        data[i] = data[i].split()
        }

