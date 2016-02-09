from celery import Celery

redis_url = 'redis://localhost:6379/0'
app = Celery('overridden by celery command', broker=redis_url)

@app.task
def consume(a, b):
    print "consume a+b = %d" % (a + b)
    return a + b
