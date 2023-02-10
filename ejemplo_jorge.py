import base64
from google.cloud import pubsub_v1

def hello_pubsub(event, context):
    message = base64.b64decode(event['data']).decode('utf-8')
    print("Mensaje recibido: {}".format(message))
    
    # Crea una instancia del cliente de Pub/Sub
    publisher = pubsub_v1.PublisherClient()
    
    # Define el tópico de salida
    topic_name = "projects/<project-id>/topics/output"
    
    # Publica el mensaje en el tópico de salida
    publisher.publish(topic_name, data=message.encode('utf-8'))
    
    return "Mensaje publicado en el tópico de salida: {}".format(message)
