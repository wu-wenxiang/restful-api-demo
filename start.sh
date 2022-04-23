#!/bin/sh

nginx
gunicorn_pecan production_config.py
