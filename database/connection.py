"""
Gerenciador de conexão com o banco de dados Neon.tech com proteção contra travamentos.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from config.settings import Settings
from utils.logger import get_logger

logger = get_logger(__name__)

Base = declarative_base()

try:
    # Adicionamos connect_args para evitar que a aplicação trave infinitamente se o banco estiver dormindo
    engine = create_engine(
        Settings.DATABASE_URL, 
        pool_pre_ping=True,
        pool_size=5,
        max_overflow=10,
        connect_args={
            "connect_timeout": 10, # Limita a espera de conexão a 10 segundos
            "options": "-c statement_timeout=15000" # Limita a espera de consultas a 15 segundos
        }
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
except Exception as e:
    logger.critical(f"Falha ao inicializar o motor do banco de dados: {str(e)}")
    raise e

def get_db_session() -> Session:
    """Cria e retorna uma nova sessão síncrona do banco de dados."""
    session = SessionLocal()
    return session