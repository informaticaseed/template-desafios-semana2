"""
Testes de verificação de entrega - Desafios Semana 02
Beecrowd 1010, 1013, 1017, 1018, 1021

Cada desafio é testado individualmente para permitir nota parcial.
Cada teste vale 20 pontos (5 desafios x 20 = 100 pontos).
"""

import os
import ast

# Diretório raiz do projeto
DIRETORIO_RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def verificar_arquivo(nome_arquivo):
    """
    Verifica se o arquivo existe, não está vazio,
    tem código Python válido e contém input() ou print().
    """
    caminho = os.path.join(DIRETORIO_RAIZ, nome_arquivo)

    # 1. Arquivo existe?
    assert os.path.exists(caminho), \
        f"Arquivo '{nome_arquivo}' não encontrado. Você criou o arquivo?"

    # 2. Arquivo não está vazio?
    with open(caminho, 'r', encoding='utf-8') as f:
        codigo = f.read().strip()

    # Remover docstrings e comentários para contar código real
    linhas_codigo = [
        linha for linha in codigo.split('\n')
        if linha.strip()
        and not linha.strip().startswith('#')
        and not linha.strip().startswith('"""')
        and not linha.strip().startswith("'''")
    ]

    assert len(linhas_codigo) > 0, \
        f"Arquivo '{nome_arquivo}' não contém código além do template. Implemente sua solução!"

    # 3. Código Python válido?
    try:
        ast.parse(codigo)
    except SyntaxError as e:
        raise AssertionError(
            f"Arquivo '{nome_arquivo}' tem erro de sintaxe na linha {e.lineno}: {e.msg}"
        )

    # 4. Contém input() ou print()?
    tem_input = 'input(' in codigo
    tem_print = 'print(' in codigo
    assert tem_input or tem_print, \
        f"Arquivo '{nome_arquivo}' não contém input() ou print(). Você implementou a solução?"


def test_desafio_1010():
    """Beecrowd 1010 - Cálculo Simples"""
    verificar_arquivo('desafio_1010.py')


def test_desafio_1013():
    """Beecrowd 1013 - O Maior"""
    verificar_arquivo('desafio_1013.py')


def test_desafio_1017():
    """Beecrowd 1017 - Gasto de Combustível"""
    verificar_arquivo('desafio_1017.py')


def test_desafio_1018():
    """Beecrowd 1018 - Cédulas"""
    verificar_arquivo('desafio_1018.py')


def test_desafio_1021():
    """Beecrowd 1021 - Notas e Moedas"""
    verificar_arquivo('desafio_1021.py')
