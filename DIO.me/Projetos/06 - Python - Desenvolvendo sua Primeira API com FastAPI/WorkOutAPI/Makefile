.PHONY: run create-migrations run-migrations first-run

create-migrations:
	@alembic -c alembic.ini revision --autogenerate -m "$(m)"

run-migrations:
	@alembic -c alembic.ini upgrade head

run:
	@uvicorn api.main:app --reload --port 8080

first-run: 
	@make create-migrations && make run-migrations && make run
	