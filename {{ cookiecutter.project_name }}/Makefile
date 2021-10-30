test:
	autopep8 -ria apps/
	flake8 apps/
	pytest
	DJANGO_SETTINGS_MODULE=nissan_ws.settings.test python manage.py behave


