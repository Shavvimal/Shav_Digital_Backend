#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.core.management.commands.runserver import Command as runserver
from django.core.management.base import BaseCommand

runserver.default_port = os.environ.get('PORT', 3000)
runserver.default_addr = '0.0.0.0'

class Command(runserver):
    def handle(self, *args, **options):
        options.setdefault('addrport', '0.0.0.0:8001')
        super(Command, self).handle(*args, **options)


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
