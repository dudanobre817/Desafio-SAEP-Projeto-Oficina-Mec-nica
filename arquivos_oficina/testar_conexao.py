"""Testar conexao com o banco de dados testar_conexao.py"""
from db import testar_conexao
try: 
    print("Conexao OK:", testar_conexao())
except Exception as e:
    print("Falha na conexao:", e)