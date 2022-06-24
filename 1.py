import json
from math import fabs

with open("1.txt", "r") as f:
    data = f.read()

data = [i.split("=") for i in data.split("&")]
with open("1.json", 'w') as f:
    for i in data:
        f.write(f"\"{i[0].strip()}\": \"{i[1].strip()}\",\n")