#!/usr/bin/env python
import sys
from celery import Celery

results = []
celery = Celery()
celery.config_from_object('celeryconfig')

results.append(celery.send_task("tasks.embed_string", [sys.argv[1]]))
