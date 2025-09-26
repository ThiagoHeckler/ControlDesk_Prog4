import os
import logging
from dotenv import load_dotenv

load_dotenv()  # Carregar variáveis do .env

# 🔧 Ajuste automático do DATABASE_URL
db_url = os.getenv("DATABASE_URL")

if db_url and db_url.startswith("postgresql://"):
    # Força usar psycopg3, que é o driver mais comum
    db_url = db_url.replace("postgresql://", "postgresql+psycopg://", 1)

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "sua_chave_secreta")
    SQLALCHEMY_DATABASE_URI = db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "sua_chave_secreta")
    JWT_ACCESS_TOKEN_EXPIRES = 7200  # 2 horas
    
    # Configurações de segurança
    SESSION_COOKIE_SECURE = True      # Apenas HTTPS
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    PREFERRED_URL_SCHEME = "https"

    # Configuração de log (produção)
    LOG_LEVEL = logging.WARNING
