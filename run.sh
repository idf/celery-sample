celery_start() {
    # start the worker
    celery -A consumer worker --loglevel=info
    # -A for celery application name
}

producer_run() {
    python producer.py
}
