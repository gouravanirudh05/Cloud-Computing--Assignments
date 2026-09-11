import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connection.channel()

channel.queue_declare(queue='hello', durable=True)

if len(sys.argv) != 2:
    print("Usage: python send.py <input_file>")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, 'r') as file:
    for line in file:
        message = line.strip()

        if message:
            channel.basic_publish(
                exchange='',
                routing_key='hello',
                body=message
            )

            print(f" [x] Sent '{message}'")

connection.close()