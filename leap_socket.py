import websocket
import json
#import thread
import time
import csv


count  =0

def on_message(ws, message):
    global count, out

    with open('C:/Users/Iris/Documents/leap_websocket/recording.txt','a') as json_file:
        if count>0:
            json_file.write(message+'\n')
            
    count = count+1
    

def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    global out, columns
    backgroundJSON = json.dumps({"background": True})
    ws.send(backgroundJSON)
    optimizeHMDmessage = json.dumps({"optimizeHMD": True})
    ws.send(optimizeHMDmessage)
    

if __name__ == "__main__":
    websocket.enableTrace(True)
    hostname = "localhost"
    port = 6437
    websocket_resource_url = f"ws://{hostname}:{port}"
    ws = websocket.WebSocketApp(websocket_resource_url,
                          on_message = on_message,
                          on_error = on_error,
                          on_close = on_close,
                          on_open = on_open)
    ws.run_forever()