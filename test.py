import numpy as np

data_arr = [
    {1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {
        1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {1, 2, 3, 4, 5}
]

dictionary = {
    "1": [1, 2, 3],
    "2": [4, 5, 6]
}

print(len(data_arr))
print(10/500)
title = "word-docTitle.txt"
start = 4428
with open(title, "r") as file:
    for _ in range(start-1):
        file.readline()
    lines = [file.readline().strip() for _ in range(num_lines)]
print(lines)
