from celery import Celery
import consumer

app_name = 'consumer'  # take the celery app name
app = Celery(app_name, broker=consumer.redis_url)

# produce
for i in range(100):
    a = 1
    b = 2
    consumer.consume.delay(a, b)
