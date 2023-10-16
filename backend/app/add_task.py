#!/usr/bin/env python
# encoding: utf-8
from datetime import timedelta
from redisbeat.scheduler import RedisScheduler
from app.core.celery_app import celery_app as app


if __name__ == "__main__":
    schduler = RedisScheduler(app=app)
    schduler.add(**{
        'name': 'sub-perminute',
        'task': 'app.worker.tests.hello_world',
        'schedule': timedelta(seconds=3),
        'args': ("hello", )
    })
    print(schduler.list())
