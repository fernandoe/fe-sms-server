DJANGO_SETTINGS_MODULE ?= 'server.settings.test'

sendsms:
	python manage.py sendsms --settings=$(DJANGO_SETTINGS_MODULE)

migrate:
	python manage.py migrate --settings=$(DJANGO_SETTINGS_MODULE)

makemigrations:
	python manage.py makemigrations --settings=$(DJANGO_SETTINGS_MODULE)
