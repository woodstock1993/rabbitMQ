import pika

# 연결 하고자 하는 rabbitMQ Server 를 지정 한다.
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue="test2")
channel.basic_publish(
    exchange="",
    routing_key="hello",
    body=b"Hello World!",
)

connection.close()