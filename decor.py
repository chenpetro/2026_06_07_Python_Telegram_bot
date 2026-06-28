import logging

logger = logging.getLogger(__name__)

from functools import wraps

def async_log_function_call(func):
    # Decorator to log the call of an async function, including its arguments and return value.
    @wraps(func)
    async def wrapper(*args, **kwargs):
        msg = f"Calling async function '{func.__name__}' with args: {args} and kwargs: {kwargs}"
        logger.info(msg=msg)
        return await func(*args, **kwargs)
    return wrapper

def sync_log_function_call(func):
    # Decorator to log the call of a sync function, including its arguments and return value.
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(__name__)
        logger.info(f"Calling sync function '{func.__name__}' with args: {args} and kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper


def user_message_log(func):
#decorator for async functions to log the messages
    async def wrapper(*args, **kwargs):
        msg = f"User send a message"
        logger.info(msg=msg)
        return await func(*args, **kwargs)
    return wrapper