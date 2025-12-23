class InMemoryCache:
    def __init__(self):
        self._seen = set()

    def is_new(self, key: str) -> bool:
        if key in self._seen:
            return False
        self._seen.add(key)
        return True
