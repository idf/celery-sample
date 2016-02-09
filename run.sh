function celery_start() {
    celery -A consumer worker --loglevel=info;
    # -A for celery application name
}

function producer_run() {
    python producer.py;
}
