import pika
import uuid
import time 
from config import CONFIG_RPC

host = CONFIG_RPC.RABBITMQ_IP
port = CONFIG_RPC.RABBITMQ_PORT
username = CONFIG_RPC.RABBITMQ_USERNAME
password = CONFIG_RPC.RABBITMQ_PASSWORD
ttl = CONFIG_RPC.RABBITMQ_TTL

class RpcClient:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=host,
            port=port,
            credentials=pika.PlainCredentials(username, password)
        )) 

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True
        )

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, massage):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=str(massage)
        )
        start_time = time.time()
        while self.response is None:
            self.connection.process_data_events()
            if time.time() - start_time > ttl:
                print("Timeout: No response received within 60 seconds.")
                return None
        return self.response
