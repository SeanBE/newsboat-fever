import os
import fcntl
from flask import Flask
from functools import wraps


DB_PATH = os.environ["NB_DB_PATH"]
LOCKFILE_PATH = os.environ["NB_LOCKFILE_PATH"]

app = Flask(__name__)


def attempt_cache_lock(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        with open(LOCKFILE_PATH, "a+") as fd:
            try:
                # F_TLOCK == LOCK_EX bitwise OR LOCK_NB (no block)
                fcntl.lockf(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except IOError as e:
                return "", 503
            except Exception as e:
                return str(e), 500

            rtn_value = fn(*args, **kwargs)
            fcntl.lockf(fd, fcntl.LOCK_UN)

        os.unlink(LOCKFILE_PATH)
        return rtn_value

    return wrapper


@app.get("/fever/")
@attempt_cache_lock
def fever_endpoint():
    # TODO implement query params routing + auth
    return "hello world"
