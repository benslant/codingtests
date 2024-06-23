from typing import Dict, List
from datetime import datetime


class RequestTime():

    def __init__(self, time: datetime) -> None:
        self.request_time = time

class Customer():

    def __init__(self, id: int) -> None:
        self.id = id

class Request():

    def __init__(self, time: RequestTime) -> None:
        pass

class RequestTimer():

    def __init__(self):
        pass

    def get_time():
        return datetime.now()


class RateLimiter():
    '''
    Each customer is limited to x number of requests every y seconds
    '''
    def __init__(self, request_timer: RequestTimer, x_requests: int, y_seconds: int) -> None:
        self.request_timer = request_timer
        self.x_requests = x_requests
        self.y_requests = y_seconds
        self.customer_requests: Dict[int, List[Request]] = {} 

    def rateLimit(self, customer_id: int) -> bool:
        self.customer_requests[customer_id].append(Request(self.request_timer.get_time()))
        return self._should_create_limit(self.customer_requests[customer_id])

    def _should_create_limit(self, requests: List[Request]) -> bool:
        if not requests or len(requests) == 1 or self.y_seconds == 0: return False
        time_delta = requests[:-1] - requests[0]
        time_delta_secs = 0
        #get in seconds
        number_requests = len(requests)
        rate = time_delta_secs/self.y_seconds
        return number_requests/rate > self.x_request