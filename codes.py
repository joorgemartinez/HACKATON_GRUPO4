#Import libraries
from base64 import b64decode
from json import loads
from logging import getLogger, setLevel, INFO
from google.cloud import pubsub_v1



#Read from PubSub (decode from Base64) & load as json
def read(event, context):
    getLogger().setLevel(INFO)
    pubsub_message = b64decode(event['data']).decode('utf-8')
    message = loads(pubsub_message)


# change "message"
    """..."""

# Publish to new PubSub

    project_id = "noble-stratum-377414"
    topic_id = "Hackaton_Output"
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)

    message = "Hello"
    message = message.encode("utf-8")
    future1 = publisher.publish(topic_path, message)
