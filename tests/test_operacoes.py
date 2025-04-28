# tests/test_operacoes.py

from app.operacoes import (
    cadastrar_usuario,
    somar_valores,
    validar_login,
    calcular_desconto,
    pode_enviar_pedido
)

def test_cadastrar_usuario():
    assert cadastrar_usuario("Matheus") == "Usuário Matheus cadastrado com sucesso."

def test_somar_valores():
    assert somar_valores(10, 20) == 30

def test_validar_login():
    assert validar_login("admin", "1234") is True
    assert validar_login("user", "senhaerrada") is False

def test_calcular_desconto():
    assert calcular_desconto(100, 10) == 90

def test_pode_enviar_pedido():
    assert pode_enviar_pedido(5) is True
    assert pode_enviar_pedido(0) is False
