#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 19:09:32 2021

@author: howardjiang
"""

# Test using Sample CSV files

import pandas as pd

df1 = pd.read_csv("/Users/howardjiang/Documents/Submit/Test/Test 1.csv")
df2 = pd.read_csv("/Users/howardjiang/Documents/Submit/Test/Test 2A.csv")
df3 = pd.read_csv("/Users/howardjiang/Documents/Submit/Test/Test 2B.csv")

frames = [df1, df2,df3]

result = pd.concat(frames)
result.to_csv("/Users/howardjiang/Documents/Submit/Test/Combine Test.csv", index = False)

# This script still produces one extra column header with Normal CSV file
