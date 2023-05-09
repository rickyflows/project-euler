#!/usr/bin/env python3
import requests
import csv

scoring_dict = { chr(i): i + 1 - ord('A') for i in range(ord('A'), ord('Z') + 1) }
def word_value(s):
    return sum(map(lambda c: scoring_dict[c], s))

def get_triangle_numbers(n):
    triangle_numbers = set()
    t = 1
    while (T := (t*(t+1))//2) <= n:
        triangle_numbers.add(T)
        t += 1
    return triangle_numbers

url = "https://projecteuler.net/project/resources/p042_words.txt"
response = requests.get(url)
if response.status_code != 200:
    print("Failed to get data.")
    exit()
data = response.text
words = list(csv.reader(data.splitlines()))[0]

maximum_score = 26 * max(map(lambda s: len(s), words))
triangle_numbers = get_triangle_numbers(maximum_score + 1)
scores = map(word_value, words)
print(sum(map(lambda x: x in triangle_numbers, scores)))
