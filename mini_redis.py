import time

class MiniRedis:
    def __init__(self):
        self.database = {}        # { key: value }
        self.expiry_times = {}    # { key: expiry_timestamp }

    # ----------------------
    # Helper methods
    # ----------------------
    def _is_expired(self, key):
        if key in self.expiry_times and time.time() > self.expiry_times[key]:
            del self.database[key]
            del self.expiry_times[key]
            return True
        return False

    def _cleanup_expired(self):
        for key in list(self.expiry_times.keys()):
            self._is_expired(key)

    # ----------------------
    # String commands
    # ----------------------
    def set_key(self, key, value, ex=None):
        self.database[key] = value
        if ex is not None:
            self.expiry_times[key] = time.time() + ex
        elif key in self.expiry_times:
            del self.expiry_times[key]
        return "OK"

    def get_key(self, key):
        if self._is_expired(key):
            return None
        return self.database.get(key, None)

    def del_key(self, key):
        if key in self.database:
            del self.database[key]
            self.expiry_times.pop(key, None)
            return 1
        return 0

    def exists_key(self, key):
        if self._is_expired(key):
            return 0
        return 1 if key in self.database else 0
    
    

    # ----------------------
    # List commands
    # ----------------------
    def lpush(self, key, value):
        if key not in self.database or not isinstance(self.database[key], list):
            self.database[key] = []
        self.database[key].insert(0, value)
        return len(self.database[key])

    def rpush(self, key, value):
        if key not in self.database or not isinstance(self.database[key], list):
            self.database[key] = []
        self.database[key].append(value)
        return len(self.database[key])

    def lpop(self, key):
        if key in self.database and isinstance(self.database[key], list) and self.database[key]:
            return self.database[key].pop(0)
        return None

    def rpop(self, key):
        if key in self.database and isinstance(self.database[key], list) and self.database[key]:
            return self.database[key].pop()
        return None

    def lrange(self, key, start, end):
        if key in self.database and isinstance(self.database[key], list):
            return self.database[key][start:end+1]
        return []

# ----------------------
# Set commands
# ----------------------
def sadd_key(self, key: str, *values: str):
    if key not in self.database or not isinstance(self.database[key], set):
        self.database[key] = set()
    added = 0
    for v in values:
        if v not in self.database[key]:
            self.database[key].add(v)
            added += 1
    return added

def smembers_key(self, key: str):
    if key in self.database and isinstance(self.database[key], set):
        return list(self.database[key])
    return []

def srem_key(self, key: str, *values: str):
    if key in self.database and isinstance(self.database[key], set):
        removed = 0
        for v in values:
            if v in self.database[key]:
                self.database[key].remove(v)
                removed += 1
        return removed
    return 0

def scard_key(self, key: str):
    if key in self.database and isinstance(self.database[key], set):
        return len(self.database[key])
    return 0

def sismember_key(self, key: str, value: str):
    if key in self.database and isinstance(self.database[key], set):
        return 1 if value in self.database[key] else 0
    return 0
