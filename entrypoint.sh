#!/bin/sh
set -e

# Сначала миграции
alembic upgrade head

# Потом запуск бота
exec python main.py
