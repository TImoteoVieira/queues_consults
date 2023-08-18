import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='get_clients_queue')

num_iterations = 165000

for i in range(num_iterations):
    message = str(i)
    channel.basic_publish(exchange='', routing_key='get_clients_queue', body=message)

print(f" [x] Send {num_iterations} messages for queue.")

connection.close()
