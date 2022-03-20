import psycopg2
from psycopg2 import extensions

from gevent.socket import wait_read, wait_write


def monkey_patch():
    """Configure psycopg2 to be used with gevent in non-blocking way."""

    extensions.set_wait_callback(gevent_wait_callback)


def gevent_wait_callback(conn, timeout=None):
    """A wait callback useful to allow gevent to work with Psycopg."""

    while True:
        state = conn.poll()
        if state == extensions.POLL_OK:
            break
        elif state == extensions.POLL_READ:
            wait_read(conn.fileno(), timeout=timeout)
        elif state == extensions.POLL_WRITE:
            wait_write(conn.fileno(), timeout=timeout)
        else:
            raise psycopg2.OperationalError(
                "Bad result from poll: %r" % state)