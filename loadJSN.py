import json
import time
import csv
import pandas as pd

data = []
count = 0
list_columns = ["hands", "pointables"]
for line in open('C:/Users/Iris/Documents/leap_websocket/recording.txt', 'r'):
    linetxt = json.loads(line)
    for lc in list_columns:
        new_dict = {}
        for count, pt in enumerate(linetxt[lc]):
            for items in pt:
                obj = pt[items]
                if isinstance(obj, list):
                    for idx, letter in enumerate(['x','y','z']):
                        new_dict[lc +str(count) + "_" + str(items) + "_" + letter] = obj[idx]
                else:
                    new_dict[lc +str(count) + "_" + str(items)] = pt[items]

        linetxt = linetxt | new_dict



    data.append((linetxt))
df = pd.json_normalize(data, sep='_')

df.to_csv(r'C:/Users/Iris/Documents/leap_websocket/recording.csv', index = None)

# data_file.close()