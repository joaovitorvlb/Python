import requests
import time

api="api thingspeak"
def sender():
    for x in range(5):
        payload = {'api_key': api, 'field1' : str(x), 'field2' : str(x), 'field3' : str(x), 'field4' : str(x)}
        print "X is: "+str(x)
        r = requests.post("https://api.thingspeak.com/update",params=payload)
        print r.text
        time.sleep(16)

def main():
    sender()
    return 0

if __name__ == '__main__':
    main()
