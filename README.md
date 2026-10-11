uv run alembic init migrations
alembic revision --autogenerate -m "Add new table"
alembic upgrade head 
## Change to Neon DB