#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 16:17:13 2021

@author: lulu
"""

import pandas as pd

data = pd.read_csv("/Users/lulu/Desktop/Ynov/Ydays/Git/ia/Breast_cancer Dataset/breast_cancer.csv", ';')



print(data.loc[data['ETAT'] == 'non-cancer'])
