#!/bin/bash

# Script para iniciar o projeto ControlDesk
echo "🚀 Iniciando ControlDesk..."

# Ativa o ambiente virtual
source venv/bin/activate

# Inicia o Flask
FLASK_APP=wsgi.py python -m flask run --debug