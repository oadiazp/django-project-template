test:
	autopep8 -ria apps/
	flake8 apps/
	pytest
	DJANGO_SETTINGS_MODULE={{ cookiecutter.project_name }}.settings.test python manage.py behave


