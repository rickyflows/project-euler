#!/usr/bin/env python3

import requests
import csv

url = "https://projecteuler.net/project/resources/p022_names.txt"
response = requests.get(url)

if response.status_code == 200:
    data = response.text
else:
    print("Failed to get data.")

names = list(csv.reader(data.splitlines()))[0]
names.sort()
score_dict = {chr(c): c-ord('A')+1 for c in range(ord('A'), ord('Z') + 1)}
S = 0

for i, name in enumerate(names):
    S += (i+1) * sum(map(lambda c: score_dict[c], name))
print(S)
