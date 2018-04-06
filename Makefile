docker-build:
	docker build -t fernandoe/fe-pessoa-server:local .

compose-bash:
	docker-compose run --rm pessoa /bin/sh

compose-build:
	docker-compose build pessoa

compose-up:
	docker-compose up pessoa

compose-stop:
	docker-compose stop

compose-rm:
	docker-compose rm

compose-migrate:
	docker-compose run --rm pessoa python manage.py migrate

compose-createsuperuser:
	docker-compose run --rm pessoa python manage.py createsuperuser
