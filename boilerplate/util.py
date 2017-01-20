import time
from pymongo.errors import AutoReconnect
from werkzeug.exceptions import InternalServerError


def autoreconnect(f):
    RETRY_COUNT = 5

    def wrapper(*args, **kwargs):
        for i in range(RETRY_COUNT):
            try:
                return f(*args, **kwargs)
            except AutoReconnect:
                print("Connection failed. AutoReconnect attempt {}".format(i + 1))
                delay = pow(2, i)
                time.sleep(delay)

        raise InternalServerError("AutoReconnect failed after {} attempts.".format(RETRY_COUNT))

    return wrapper
