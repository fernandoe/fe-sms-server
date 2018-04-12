build:
	docker build -t fernandoe/fe-sms-server:local .

docker-build:
	docker build -t fernandoe/fe-sms-server:local .

build-no-cache:
	docker build --no-cache -t fernandoe/fe-sms-server:local .

test:
	cd src; pytest -s

makemigrations:
	cd src; python manage.py makemigrations --settings server.settings.test

docker.build:
	docker build --no-cache -t fernandoe/fe-sms-server:latest .

travis.test:
	docker run --rm -it '${TRAVIS_REPO_SLUG}:${COMMIT}' pytest -s
