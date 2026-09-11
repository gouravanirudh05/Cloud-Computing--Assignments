import pika
import sys

filename = sys.argv[1]

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.exchange_declare(
    exchange='logs',
    exchange_type='fanout'
)

with open(filename) as file:
    for line in file:
        message = line.strip()

        if not message:
            continue

        channel.basic_publish(
            exchange='logs',
            routing_key='',
            body=message
        )

        print(f" [x] Sent '{message}'")

connection.close()