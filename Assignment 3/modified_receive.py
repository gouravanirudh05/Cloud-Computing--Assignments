import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connection.channel()

channel.queue_declare(queue='hello', durable=True)

def callback(ch, method, properties, body):
    message = body.decode()

    word_count = len(message.split())

    print(f" [x] Received: {message}")
    print(f"     Word count: {word_count}")

channel.basic_consume(
    queue='hello',
    on_message_callback=callback,
    auto_ack=True
)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()