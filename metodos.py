import os

@staticmethod
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

@staticmethod
def continuar():
    limpar_tela()
    while True:
        try:
            opc = int(input('Deseja continuar?\n1 - Sim\n2 - Não\n'))
            if opc == 1:
                return True
            elif opc == 2:
                return False
            else:
                print('\nOpção inválida! Tente novamente.\n')
        except:
            print('\nPor favor, insira um valor inteiro.\n')
