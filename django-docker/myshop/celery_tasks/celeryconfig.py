# coding=utf-8

from kombu import Exchange, Queue

BROKER_URL = 'redis://redisdb:6379/2'
CELERY_RESULT_BACKEND = 'redis://redisdb:6379/3'
