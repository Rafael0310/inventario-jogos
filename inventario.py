# Importando classes e métodos
from jogo import Jogo
from metodos import ( continuar, limpar_tela )

# Importando bibliotecas
from dataclasses import dataclass
import os

jogos = []

@dataclass
class Inventario:
    
    @classmethod
    def adicionar_jogo(cls):
        limpar_tela()
        titulo = input('Insira o nome do jogo que deseja adicionar: ').lower().strip()

        if not cls.procurar_jogo(titulo):
            try:
                genero = input('Insira o gênero do jogo: ')
                release = int(input('Insira o ano de lançamento do jogo:'))
                jogos.append(Jogo(titulo=titulo, genero=genero, release=release))

                print(f'\nNovo jogo adicionado!\nNome: {jogos[-1].titulo}\nGênero: {jogos[-1].genero}\nLançamento: {jogos[-1].release}\n')

            except ValueError:
                print('Valor inválido.\n')

        else:
            print('Esse jogo já foi incluido no inventário.')
            

    @classmethod
    def remover_jogo(cls):
        limpar_tela()
        if cls.verificar_lista():
            titulo = input('Insira o nome do jogo que deseja excluir: ').lower().strip()
            if not cls.procurar_jogo(titulo):
                pass

    @classmethod
    def listar_jogos(cls):
        limpar_tela()
        if cls.verificar_lista():
            pass

    @classmethod
    def listar_por_titulo(cls):
        limpar_tela()
        if cls.verificar_lista():
            pass

    @classmethod
    def listar_por_genero(cls):
        limpar_tela()
        if cls.verificar_lista():
            pass

    @classmethod
    def listar_por_release(cls):
        limpar_tela()
        if cls.verificar_lista():
            pass

    
    @staticmethod
    def procurar_jogo(titulo_jogo):
        limpar_tela()
        if any(titulo_jogo == titulo for titulo in jogos):
            return True
        else:
            return False

    @staticmethod
    def verificar_lista():
        limpar_tela()
        if len(jogos) > 0:
            return True
        else:
            print('Por favor, inclua pelo menos um jogo no inventário antes de executar esta função.\n')
            return False