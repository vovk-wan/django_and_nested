migrate:
	./manage.py makemigrations
	./manage.py migrate
run:
	./manage.py runserver 0.0.0.0:8888
lints:
	isort . --profile=black
	black .
shell:
	./manage.py shell_plus --plain