import base64
import time
from google.cloud import pubsub_v1
import json
        
        
def array_order(event, context):
    inicio = time.time()

    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    array = json.loads(pubsub_message["jsonPayload"]["challenges"][0]["challengePayload"])
    

    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

    print(array)
    fin = time.time()
    print(fin-inicio) 
    
    pubsub_message2 = {"requestId": event['data']["jsonPayload"]["requestId"],
                "timeOfReception": inicio, 
                "team": "team4all",
                "responses":[
                {
                "challengeId": event['data']["jsonPayload"]["challenges"][0]["challengeId"],
                "challegePayload": event['data']["jsonPayload"]["challenges"][0]["challengePayload"],
                "challengeType": type(event['data']["jsonPayload"]["challenges"][0]["challengePayload"]),
                "payload": array, 
                "timeStart": inicio, 
                "timeEnd": fin
                }
                ]
                }

    project_id = "your-project-id"
    topic_id = "test-topic"

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)

    # The message must be a bytestring.
    message2 = pubsub_message2.encode("utf-8")

    # When you publish a message, the client returns a future.
    future1 = publisher.publish(topic_path, message2)
    print(future1.result())

