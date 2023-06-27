port=5001

run:
	FLASK_APP=app/init.py FLASK_DEBUG=1 flask run --port $(port)

migrate:
	python app/migrate.py