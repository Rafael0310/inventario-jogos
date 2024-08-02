# Importando classes e métodos
from jogo import Jogo
from metodos import ( continuar, limpar_tela )

# Importando bibliotecas
from dataclasses import dataclass

jogos = []

@dataclass
class Inventario:
    
    @classmethod
    def adicionar_jogo(cls):
        while True:
            limpar_tela()
            titulo = input('Insira o nome do jogo que deseja adicionar: ').upper().strip()

            if not cls.procurar_jogo(titulo):
                try:
                    genero = input('Insira o gênero do jogo: ').upper().strip()
                    release = int(input('Insira o ano de lançamento do jogo: '))
                    jogos.append(Jogo(titulo=titulo, genero=genero, release=release))

                    print(f'\nNovo jogo adicionado!\nNome: {jogos[-1].titulo}\nGênero: {jogos[-1].genero}\nLançamento: {jogos[-1].release}\n')

                except ValueError:
                    print('Valor inválido.\n')

            else:
                print('Esse jogo já foi incluido no inventário.')

            if not continuar():
                break
            

    @classmethod
    def remover_jogo(cls):
        while True:
            limpar_tela()

            if cls.verificar_lista():
                titulo = input('Insira o nome do jogo que deseja excluir: ').upper().strip()

                if cls.procurar_jogo(titulo):
                    print('Jogo não localizado.')

                else:
                    for item in jogos:
                        if item.titulo == titulo:
                            jogos.remove(item)
                            print('Jogo removido.')
                            break

    @classmethod
    def listar_jogos(cls):
        limpar_tela()
        if cls.verificar_lista():
            for item in jogos:
                print(f'Jogo: {item.titulo}\nGênero: {item.genero}\nLançamento: {item.release}\n\n')

    @classmethod
    def listar_por_titulo(cls):
        limpar_tela()
        if cls.verificar_lista():
            jogos_ordem_titulo = sorted(jogos, key=lambda x: x.titulo)
            for item in jogos_ordem_titulo:
                print(f'Jogo: {item.titulo}\nGênero: {item.genero}\nLançamento: {item.release}\n\n')

    @classmethod
    def listar_por_genero(cls):
        limpar_tela()
        if cls.verificar_lista():
            jogos_ordem_genero = sorted(jogos, key=lambda x: x.genero)
            for item in jogos_ordem_genero:
                print(f'Jogo: {item.titulo}\nGênero: {item.genero}\nLançamento: {item.release}\n\n')

    @classmethod
    def listar_por_release(cls):
        limpar_tela()

        if cls.verificar_lista():
            jogos_ordem_release = sorted(jogos, key=lambda x: x.release)
            for item in jogos_ordem_release:
                print(f'Jogo: {item.titulo}\nGênero: {item.genero}\nLançamento: {item.release}\n\n')

    
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