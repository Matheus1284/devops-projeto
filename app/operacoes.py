# app/operacoes.py

def cadastrar_usuario(nome):
    return f"Usuário {nome} cadastrado com sucesso."

def somar_valores(valor1, valor2):
    return valor1 + valor2

def validar_login(usuario, senha):
    return usuario == "admin" and senha == "1234"

def calcular_desconto(valor, porcentagem):
    return valor * (1 - porcentagem / 100)

def pode_enviar_pedido(estoque):
    return estoque > 0
