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
            media_duracao()
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
            if linha.strip().startswith("Título"):
                contador =+ 1

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
                        
                        

def filmes_por_diretor():
    diretor_busca=input('Diretor: ').strip().lower
    contador = 0
    try:
        with open("filmes.txt", encoding="utf-8") as f:
            ultimo_titulo=""
            for linha in f:
                s = linha.strip()
                if s.startswith('Título:'):
                    ultimo_titulo= s.split(':', 1)[1].strip()
                elif s.startswith('Diretor:'):
                    diretor = s.split(':',1)[1].strip()
                    if diretor.lower() == diretor_busca:
                        contador += 1
                        print (f'-{ultimo_titulo}')
    except FileNotFoundError:
        print("Arquivo'filmes.txt não encontrado")
        return
    print(f"total de filmes do diretor {diretor_busca}:{contador}")
    return contador

def filmes_por_genero():
    genero_busca=input('Gênero,').strip().lower
    contador = 0
    try:
        with open("filmes.txt", encoding="utf-8") as f:
            ultimo_titulo=""
            for linha in f:
                s = linha.strip()
                if s.startswith('Título:'):
                    ultimo_titulo= s.split(':', 1)[1].strip()
                elif s.startwith('Gênero:'):
                    genero = s.split(':', 1)[1].strip()
                    if genero_busca in genero.lower() :
                        contador += 1
                        print (f'-{ultimo_titulo}')
    except FileNotFoundError:
        print("Arquivo'filmes.txt não encontrado")
        return
    print(f"total de filmes do diretor' {genero_busca}':{contador}")
    return contador




def media_duracao():
    soma = 0
    cont = 0
    try:
        with open("filmes.txt", encoding="utf-8") as f:
            for linha in f:
                s = linha.strip()
                if s.startswith("Duração:"):
                    try:
                        minutos= int (s.split(':',1)[1].strip().split()[0])
                    except (ValueError,IndexError):
                        continue
                    soma += minutos
                    cont += 1
    except FileNotFoundError:
        print("Arquivo'filmes.txt'não encontrado.")
        return

    if cont== 0:
        print("Nenhuma duração válida encontrada.")
    else:
        media= soma/cont
        print(f"Média de duração: {media:.2f} minutos")
        return media


def adicionar_filme():
    print("** ADICIONAR FILME **")
    titulo = input("-> Digite o nome do filme: ").strip()
    ano = int(input('-> Digite o ano do filme: '))
    diretor = input('-> Digite o diretor do filme: ').strip()
    genero = input('-> Digite o gênero do filme: ').strip()
    duracao = int(input('-> Digite o a duração do filme: '))

    try: 
        with open("filmes.txt", "a", encoding="utf-8") as file:
            file.write("\n")
            file.write(f"Título: {titulo}\n")
            file.write(f"Ano: {ano}\n")
            file.write(f"Diretor: {diretor}\n")
            file.write(f"Gênero: {genero}\n")
            file.write(f"Duração: {duracao} minutos\n")
    except FileNotFoundError:
        print("Arquivo 'filmes.txt' não econtrado")

    print("Filme adicionado com sucesso!")





if __name__ == "__main__":
    main()