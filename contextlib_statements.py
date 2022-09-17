import logging
from contextlib import contextmanager
from threading import Lock

@contextmanager
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(old_level)



@contextmanager
def log_level(level, name):
    logger = logging.getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)

with log_level(logging.DEBUG, 'my-log') as logger:
    logging.debug('This is the global logger')
    logger.debug('This is the my-log logger')

logger = logging.getLogger('my-log')
logger.debug('Does not print anything')
logger.error('this will')





@contextmanager
def swallow_exception(cls):
    try:
        yield
    except cls:
        logging.exception('Swallowing exception')


value = 20

with swallow_exception(ZeroDivisionError):
    value /= 0

print('done')





logging.getLogger().setLevel(logging.WARNING)
def my_function():
    logging.debug('Some debug info')
    logging.error(' A real error!')
    logging.debug('More debugging')

print('before contextmanager:')
my_function()
print('after contextmanager:')


with debug_logging(logging.DEBUG):
    my_function()



my_function()




lock = Lock()
with lock:
    print('Lock is held')



lock.acquire()
try:
    print('Lock is also held')
finally:
    lock.release()
