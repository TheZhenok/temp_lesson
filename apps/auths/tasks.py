from celery import app

from .services import re_zero_counts_service

@app.shared_task(name='update_counts')
def update_counts():
    re_zero_counts_service()
