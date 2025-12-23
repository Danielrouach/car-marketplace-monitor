import time


class RateLimiter:
    def __init__(self, delay_seconds: float):
        self.delay = delay_seconds
        self._last_call = 0.0

    def wait(self):
        elapsed = time.time() - self._last_call
        if elapsed < self.delay:
            time.sleep(self.delay - elapsed)
        self._last_call = time.time()
