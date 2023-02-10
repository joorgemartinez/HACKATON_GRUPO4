import base64
import time
import json

def array_order(event, context):

    inicio = time.time()

    pubsub_message = base64.b64decode(event['data']).decode('utf-8')

    array = json.loads(pubsub_message["jsonPayload"]["challenges"][0]["challengePayload"])++++++++++++++++++++++++++++

    array_ordenado = sorted(array)

    print(array_ordenado)

    fin = time.time()
    print(fin-inicio) 

