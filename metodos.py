from inventario import jogos

@staticmethod
def procurar_jogo(nome_jogo):
    if any(nome_jogo == nome for nome in jogos):
        return True
    else:
        return False

@staticmethod
def verificar_lista():
    if len(jogos) > 0:
        return True
    else:
        return False
    
@staticmethod
def continuar():
    while True:
        try:
            opc = int(input(' Deseja continuar?\n1 - Sim\n2 - Não\n'))
            if opc == 1:
                return True
            elif opc == 2:
                return False
            else:
                print(' Opção inválida! Tente novamente.')
        except:
            print(' Por favor, insira um valor inteiro.')