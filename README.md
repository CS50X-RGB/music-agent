## Change to Neon DB
uv run alembic init migrations
alembic revision --autogenerate -m "Add new table"
alembic upgrade head 
## Start the app
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8080