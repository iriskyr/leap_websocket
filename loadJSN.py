import json
#import thread
import time
import csv
import pandas as pd

# df = pd.read_json(r'C:/Users/Iris/Documents/leap_websocket/recording.json', lines=True)
# df.to_csv(r'C:/Users/Iris/Documents/leap_websocket/recording.csv', index = None)


#json_file = 'C:/Users/Iris/Documents/leap_websocket/recording.json'
#with open('C:/Users/Iris/Documents/leap_websocket/recording.txt') as json_file:
    #data = json.loads(json_file.read())
data = []
for line in open('C:/Users/Iris/Documents/leap_websocket/recording.txt', 'r'):
    linetxt = json.loads(line)
    data.append((linetxt))

df = pd.DataFrame(data)

df.to_csv(r'C:/Users/Iris/Documents/leap_websocket/recording.csv', index = None)


# data_file = open('C:/Users/Iris/Documents/leap_websocket/recording.csv', 'w')
 
# csv_writer = csv.writer(data_file)

 
# data_file.close()