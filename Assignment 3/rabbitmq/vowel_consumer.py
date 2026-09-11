import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connection.channel()

channel.exchange_declare(
    exchange='logs',
    exchange_type='fanout'
)

# Create a temporary, exclusive queue
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# Bind the queue to the fanout exchange
channel.queue_bind(exchange='logs',queue=queue_name
)

print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    message = body.decode()
    vowel_count = 0
    for char in message.lower():
        if char in 'aeiou':
            vowel_count += 1

    print(f" [x] Received: {message}")
    print(f"Vowel count: {vowel_count}")


channel.basic_consume(
    queue=queue_name,
    on_message_callback=callback,
    auto_ack=True)

channel.start_consuming()