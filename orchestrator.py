import subprocess
import time

def run_service(command):
    return subprocess.Popen(["python", command], shell=False)

if __name__ == "__main__":
    print("Starting producer...")
    produtor_process = run_service("producer.py")
    produtor_process.wait()

    time.sleep(3)

    print("Starting consumer...")
    consumidor_process = run_service("consumer.py")
    consumidor_process.wait()
