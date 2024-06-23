import pytest
from datetime import datetime, timedelta
from ratelimiter.solution import RateLimiter, Request, RequestClock

test_data = [(3, 2, 1, 
              {"3": [Request(datetime.now()), 
                     Request(datetime.now()),
                     Request(datetime.now()),
                     Request(datetime.now()),
                     Request(datetime.now() - timedelta(seconds=20)), 
                     Request(datetime.now() - timedelta(seconds=20))]}, 
              True),
              (3, 5, 1, 
              {"3": [Request(datetime.now()), 
                     Request(datetime.now()),
                     Request(datetime.now()),
                     Request(datetime.now()),
                     Request(datetime.now() - timedelta(seconds=20)), 
                     Request(datetime.now() - timedelta(seconds=20))]}, 
              False),
              (3, 10000, 100, 
              {"3": [Request(datetime(2023, 7, 1, 1, 1, 0))] * 10000}, 
              False),
              (3, 10000, 120, 
              {"3": ([Request(datetime(2023, 7, 1, 1, 1, 0))] * 10000) + [Request(datetime(2023, 7, 1, 2, 1, 0))] * 10000 }, 
              False)]

@pytest.mark.parametrize("customer_id, requests, period, request_data, expected", test_data)
def test_should_rate_limit_if_requests_per_period_are_exceeded(customer_id, requests, period, request_data, expected):
    clock = RequestClock(request_data[str(customer_id)][0].time)
    rate_limter = RateLimiter(requests, period, clock=clock, request_history=request_data)
    assert rate_limter.rateLimit(customer_id) == expected