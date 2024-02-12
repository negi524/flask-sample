main:
	poetry run flask --app app run

export:
	poetry export -f requirements.txt --output requirements.txt