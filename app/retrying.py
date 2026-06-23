import time
from functools import wraps


def retry(times=3, delay=0.1, backoff=2.0):
    """Retry a callable with exponential backoff."""

    def deco(fn):
        @wraps(fn)
        def wrapper(*a, **k):
            wait, last = delay, None
            for _ in range(times):
                try:
                    return fn(*a, **k)
                except Exception as e:
                    last = e
                    time.sleep(wait)
                    wait *= backoff
            raise last

        return wrapper

    return deco
