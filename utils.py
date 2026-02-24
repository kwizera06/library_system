
from datetime import datetime
from functools import wraps


def track_access(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().isoformat(timespec="microseconds")
        print(f"[LOG] {timestamp} | Method: {func.__name__} | "
              f"Args: {args[1:]} | Kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper


def permission_check(required_role):
    def decorator(func):
        @wraps(func)
        def wrapper(self, user, *args, **kwargs):
            if user.role != required_role:
                raise PermissionError(
                    f"Access denied. '{required_role}' role required."
                )
            return func(self, user, *args, **kwargs)
        return wrapper
    return decorator

class User:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    def __str__(self):
        return f"{self.name} ({self.role})"
