docker-build:
	docker build -t fernandoe/fe-sms-server:local .

test:
	cd src; pytest -s
