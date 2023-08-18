import pika
import time
from db_config import get_clients

start_time = time.time()

def seconds_to_minutes(seconds):
    return seconds / 60

def callback(ch, method, properties, body):
    num_iterations = 165000
    print(f" [x] Received the message. Executing {num_iterations} x...")

    for i in range(num_iterations):
        clients = get_clients()
        print(f"Iteration {i+1}: {len(clients)} clients")

        elapsed_time = time.time() - start_time
        average_time_per_iteration = elapsed_time / (i + 1)
        remaining_iterations = num_iterations - (i + 1)
        estimated_completion_time = start_time + (average_time_per_iteration * remaining_iterations)

        print(f"Time: {seconds_to_minutes(elapsed_time):.2f} minutes")
        print(f"Time for conclusion: {seconds_to_minutes(estimated_completion_time):.2f} minutes")

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='get_clients_queue')

channel.basic_consume(queue='get_clients_queue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. Press Ctrl+C for logout')
channel.start_consuming()
