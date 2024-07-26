# Importando bibliotecas
import os

# Importando classes
from inventario import Inventario

while True:
    try:
        opcao = int(input('''Inventário de jogos\n
Selecione uma opção\n
1 - Adicionar novo jogo
2 - Remover um jogo
3 - Listar todos os jogos
4 - Listar jogos por titulo
5 - Listar jogos por gênero
6 - Listar jogos por lançamento
7 - Sair
'''))
        
        match opcao:
            case 1:
                Inventario.adicionar_jogo()

            case 2:
                Inventario.remover_jogo()

            case 3:
                Inventario.listar_jogos()

            case 4:
                Inventario.listar_por_titulo()

            case 5:
                Inventario.listar_por_genero()

            case 6:
                Inventario.listar_por_release()

            case 7:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Encerrando...')
                exit()

    except ValueError:
        print('Por favor, insira um valor inteiro')