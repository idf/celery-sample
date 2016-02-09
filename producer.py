from celery import Celery
import consumer

redis_url = 'redis://localhost:6379/0'
app = Celery('consumer', broker=redis_url)  # take the celery app name

# produce
for i in range(100):
    a = 1
    b = 2
    consumer.consume.delay(a, b)
