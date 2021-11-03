#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 15:38:46 2021

@author: lulu
"""

import csv

file = open("/Users/lulu/Desktop/Ynov/Ydays/Git/ia/Breast_cancer Dataset/breast_cancer.csv")
csvreader = csv.reader(file)
header = next(csvreader)

print(header)

rows = []
for row in csvreader:
    rows.append(row)
    
print(rows)

file.close()