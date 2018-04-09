docker-build:
	docker build -t fernandoe/fe-sms-server:local .

test:
	cd src; pytest -s

makemigrations:
	cd src; python manage.py makemigrations --settings server.settings.test


docker.build:
	docker build --no-cache -t fernandoe/fe-sms-server:latest .


docker.test:
	docker run --rm -it fernandoe/fe-sms-server:latest pytest -s
