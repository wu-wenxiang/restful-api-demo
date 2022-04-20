#!/bin/sh

nginx
gunicorn_pecan config.py
