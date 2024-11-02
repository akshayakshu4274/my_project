# main.py
import threading
from word_frequency import word_frequency
from circular_queue import CircularQueue
from password_validator import validate_passwords

def run_word_frequency():
    with open("inputs/input.txt", "r") as file:
        line = file.readline().strip()
    result = word_frequency(line)
    print("Word Frequency:", result)

def run_circular_queue():
    cq = CircularQueue()
    for i in range(7):
        cq.enqueue(f"Element-{i}")
    print("Circular Queue:", cq.display())

def run_password_validator():
    input_passwords = "asqwr1234@1,aF145#,2w3E*,2We3345"
    result = validate_passwords(input_passwords)
    print("Valid Passwords:", result)

if __name__ == "__main__":
    threads = []
    threads.append(threading.Thread(target=run_word_frequency))
    threads.append(threading.Thread(target=run_circular_queue))
    threads.append(threading.Thread(target=run_password_validator))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

