import os
from sqlalchemy import create_engine
from alembic import context
from dotenv import load_dotenv
from app.core.database import Base
from app.model import User, Playlist, PlaylistSong, SongFeedback


load_dotenv()
# Load DATABASE_URL from .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Create engine with Neon-specific settings
engine = create_engine(
    DATABASE_URL,
    connect_args={"sslmode": "require"},
    pool_pre_ping=True  # Critical for Neon's serverless cold starts
)

target_metadata = Base.metadata  # Or your Base.metadata if using declarative models

def run_migrations_offline():
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"}
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()   