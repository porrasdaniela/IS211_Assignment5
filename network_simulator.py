import random
import time
from collections import deque

class Request:
    def __init__(self, id, arrival_time):
        self.id = id
        self.arrival_time = arrival_time

class Server:
    def __init__(self, processing_rate):
        self.processing_rate = processing_rate # Requests processed per second

    def process_request(self, request):
        time_to_process = 1 / self.processing_rate
        time.sleep(time_to_process)  # Simulate processing time
        return time_to_process

def simulate_network(num_requests, processing_rate):
    queue = deque()
    server = Server(processing_rate)
    total_wait_time = 0

    for i in range(num_requests):
        arrival_time = time.time()
        request = Request(i, arrival_time)
        queue.append(request)
        print(f"Request {request.id} arrived at {arrival_time:.2f}")

        # Process the request if the server is free
        if len(queue) > 0:
            current_request = queue.popleft()
            wait_time = time.time() - current_request.arrival_time
            total_wait_time += wait_time
            processing_time = server.process_request(current_request)
            print(f"Request {current_request.id} processed in {processing_time:.2f} seconds. Waited {wait_time:.2f} seconds.")

    average_wait_time = total_wait_time / num_requests
    print(f"Average wait time: {average_wait_time:.2f} seconds")

if __name__ == "__main__":
    num_requests = 10  # Number of requests to simulate
    processing_rate = 2  # Requests per second
    simulate_network(num_requests, processing_rate)
