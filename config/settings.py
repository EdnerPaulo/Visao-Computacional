"""
Módulo de Configuração Estática da Aplicação.
Centraliza as credenciais de bancos de dados gratuitos e caminhos de upload.
"""
import os

class Settings:
    # URL padrão para instância gratuita do Neon.tech (PostgreSQL)
    # Substitua pelos dados da sua própria instância string gerada no painel do Neon
    DATABASE_URL: str = "postgresql+psycopg://neondb_owner:npg_X1abcDEfG2hi@ep-cool-flower-a5v8abc.us-east-2.aws.neon.tech/neondb?sslmode=require"
    
    # Pastas do sistema
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    UPLOAD_FOLDER: str = os.path.join(BASE_DIR, "assets", "images")
    LOG_FOLDER: str = os.path.join(BASE_DIR, "logs")

    @classmethod
    def init_directories(cls) -> None:
        """Garante a existência física dos diretórios necessários para a aplicação."""
        os.makedirs(cls.UPLOAD_FOLDER, exist_ok=True)
        os.makedirs(cls.LOG_FOLDER, exist_ok=True)

Settings.init_directories()