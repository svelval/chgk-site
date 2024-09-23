db-up:
	docker compose up

db-down:
	docker compose down

db-reset:
	docker compose down -v

django-server:
	cd src && python manage.py runserver

migrations:
	cd src && python manage.py makemigrations

migrate:
	cd src && python manage.py migrate

shell:
	cd src && python manage.py shell

createsuperuser:
	cd src && python manage.py createsuperuser