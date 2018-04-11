build:
	docker build -t fernandoe/fe-sms-server:local .

docker-build:
	docker build -t fernandoe/fe-sms-server:local .

test:
	cd src; pytest -s

makemigrations:
	cd src; python manage.py makemigrations --settings server.settings.test
