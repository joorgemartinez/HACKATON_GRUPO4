import base64
import time

def array_order(event, context):

    inicio = time.time()

    pubsub_message = sorted(base64.b64decode(int(event['data']["jsonPayload"]["challenges"]["challengePayload"]))).decode('utf-8')

    print(pubsub_message)

    fin = time.time()
    print(fin-inicio) 