def main():
    while True:
        menu()
        opc=input("Opção: ").strip()
        if opc == '0':
            adicionar_filme()
        elif opc == '1':
            contar_filmes()
        elif opc == '2':
            info_por_titulo()
        elif opc == '3':
            filmes_por_diretor()
        elif opc == "4":
            filmes_por_genero()
        elif opc == "5":
            media_de-duração()
        elif opc == '6':
            print('saindo...')
            break
        else:
            print('opção invalida. tente novamente')


def menu() -> None:
    print('***MENU INICIAL***')
    print('ESCOLHA UMA OPÇÃO:')
    print('1 - QUANTIDADE DE FILMES')
    print('2 - FILME POR TITULO')
    print('3 - FILMES POR DIRETOR')
    print('4 - FILMES POR GÊNERO')
    print('5 - MEDIA DE DURAÇÃO')
    print('6 - SAIR')

def contar_filmes():
    contador=0
    with open('filmes.txt', 'r', encoding="utf-8") as arquivo:
        for linha in arquivo:
            if linha.strip().startswith('Título'):
                contador=contador+1
    print(f'Quantidade de filmes : {contador}')

def info_por_titulo():
    titulo_busca = input('Título: ').strip().lower()
    encontrado = False
    try:
        with open("filmes.txt", encoding='utf-8') as f:
            for linha in f:
                if linha.strip().startswith('Título:'):
                    titulo = linha.split(':', 1)[1]. strip()
                    if titulo.lower() == titulo_busca:
                        print(f'Título: {titulo}')
                        try:
                            ano=next(f).strip()
                            diretor=next(f).strip()
                            genero=next(f).strip()
                            duração=next(f).strip()
                        except StopIteration:
                            print('Registro incompleto para ese título.')
                            return
                    
                        print(ano)
                        print(diretor)
                        print(genero)
                        print(duração)
                        encontrado = True
                        break
    except FileNotFoundError:
        print("Arquivo'filmes.txt'não encontrado.")
        return
    if not encontrado:
        print('filme não encontrado.')
                        
                        

        
if __name__ == "__main__":
    main()

   