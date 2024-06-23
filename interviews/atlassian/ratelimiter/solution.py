from typing import Dict, List, Optional
from datetime import datetime

class Request():

    def __init__(self, time: datetime) -> None:
        self.time = time

class RequestClock():

    def __init__(self, start_time: datetime):
        self.start_time = start_time

    def now(self) -> datetime:
        return self.start_time

class RateLimiter():
    '''
    Each customer is limited to x number of requests every y seconds
    '''
    def __init__(self, x_requests: int, y_seconds: int, clock: RequestClock, request_history: Optional[Dict[int, List[Request]]] = None) -> None:
        self.allowed_requests = x_requests
        self.y_seconds = y_seconds
        self.customer_requests: Dict[int, List[Request]] = request_history 
        self.clock = clock

    def rateLimit(self, customer_id: int) -> bool:
        self.customer_requests[str(customer_id)].append(Request(datetime.now()))
        return self._should_limit(self.customer_requests[str(customer_id)])

    def _should_limit(self, requests: List[Request]) -> bool:
        if not requests or len(requests) == 1 or self.y_seconds == 0: return False
        now = self.clock.now()
        bucket_requests = [(r.time - now).seconds for r in requests if (r.time - now).seconds <= self.y_seconds]
        number_requests = len(bucket_requests)
        return number_requests > self.allowed_requests