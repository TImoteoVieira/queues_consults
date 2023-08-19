# Project: RabbitMQ Message Processing

### Description
This project demonstrates how to implement a simple message processing system using RabbitMQ as the message broker. The system consists of a producer, an intermediate service, and a consumer, all communicating through RabbitMQ to process messages asynchronously.

## Requirements

Python3 (3.x)
pika library (for RabbitMQ interaction)
RabbitMQ server (can be installed locally or via Docker)

## Project Structure

producer.py - Sends messages to the RabbitMQ queue.
consumer.py -  Consumes messages from the processed queue.
orchestrator.py - Orchestrates the execution sequence of producer, and consumer.
config_db.py - Contains the function get_clients() for simulating database queries.

## How to Run
Create venv
```
     python3 -m venv venv
```
Active venv
```
    source venv/bin/activate
```
Install libs
```
    pip install requirements.txt
```
Install RabbitMQ
```
    docker compose up -d --build
```
Ensure RabbitMQ server is running either locally or through Docker using:
```
    docker ps
```
Execute the following command to start the process:
bash
Copy code
```
    python3 orchestrator.py
```

## Usage

The producer sends random messages to the RabbitMQ queue.
The intermediate service processes the messages and publishes them to another queue.
The consumer receives and displays the processed messages.
