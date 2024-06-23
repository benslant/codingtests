import pytest
from ratelimiter.solution import RateLimiter

test_data = [(1, [], True)]

@pytest.mark.parametrize("customer_id, request_data, expected", test_data)
def test_should_rate_limit_if_requests_per_period_are_exceeded(customer_id, request_data, expected):
    rate_limter = RateLimiter()
    assert rate_limter.rateLimit(customer_id) == expected