def mesclar_e_contar(lista, lista_temporaria, esquerda, meio, direita):
    i = esquerda      
    j = meio + 1      
    k = esquerda      
    contagem_inversoes = 0

    while i <= meio and j <= direita:
        if lista[i] <= lista[j]:
            lista_temporaria[k] = lista[i]
            i += 1
        else:
            lista_temporaria[k] = lista[j]
            contagem_inversoes += (meio - i + 1)
            j += 1
        k += 1

    while i <= meio:
        lista_temporaria[k] = lista[i]
        i += 1
        k += 1

    while j <= direita:
        lista_temporaria[k] = lista[j]
        j += 1
        k += 1

    for indice in range(esquerda, direita + 1):
        lista[indice] = lista_temporaria[indice]

    return contagem_inversoes


def ordenar_e_contar(lista, lista_temporaria, esquerda, direita):
    contagem_inversoes = 0
    if esquerda < direita:
        meio = (esquerda + direita) // 2
        contagem_inversoes += ordenar_e_contar(lista, lista_temporaria, esquerda, meio)
        contagem_inversoes += ordenar_e_contar(lista, lista_temporaria, meio + 1, direita)
        contagem_inversoes += mesclar_e_contar(lista, lista_temporaria, esquerda, meio, direita)
    return contagem_inversoes


def contar_inversoes(lista):
    lista_temporaria = [0] * len(lista)
    return ordenar_e_contar(lista, lista_temporaria, 0, len(lista) - 1)

def exibir_menu():
    print("\n" + "="*50)
    print("MATCHFLIX - FILTRO COLABORATIVO")
    print("="*50)
    print("[ 1 ] Cadastrar meu Top Filmes")
    print("[ 2 ] Inserir preferências do Outro Usuário")
    print("[ 3 ] Verificar Afinidade")
    print("[ 4 ] Sair")
    print("="*50)

def main():
    meus_filmes = []
    preferencias_outro_numeros = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("--- CADASTRAR MEU TOP FILMES ---")
            quantidade = int(input("Quantos filmes deseja adicionar no seu Top? "))
            meus_filmes = []
            for i in range(quantidade):
                filme = input(f"{i + 1}º Filme: ").strip()
                meus_filmes.append(filme)
            
            preferencias_outro_numeros = []
            print("\nTop filmes cadastrados com sucesso!")
            print(f"Sua ordem ideal: {meus_filmes}")

        elif opcao == '2':
            if not meus_filmes:
                print("Erro: Você precisa cadastrar seus filmes primeiro (Opção 1).")
                continue

            print("--- PREFERÊNCIAS DO OUTRO USUÁRIO ---")
            print("Rankeie os filmes abaixo de 1 a", len(meus_filmes))
            
            preferencias_outro_numeros = [0] * len(meus_filmes)
            filmes_disponiveis = meus_filmes.copy()
            
            for i in range(len(meus_filmes)):
                print(f"\nQual posição o filme '{meus_filmes[i]}' ocupa para o outro usuário?")
                while True:
                    try:
                        posicao = int(input("Posição: "))
                        if posicao < 1 or posicao > len(meus_filmes):
                            print(f"Por favor, digite um número entre 1 e {len(meus_filmes)}.")
                        elif posicao in preferencias_outro_numeros:
                            print("Essa posição já foi usada! Tente outra.")
                        else:
                            preferencias_outro_numeros[i] = posicao
                            break
                    except ValueError:
                        print("Por favor, digite um número válido.")
            
            print("\nPreferências do outro usuário cadastradas!")
            print(f"Vetor gerado para o algoritmo: {preferencias_outro_numeros}")

        elif opcao == '3':
            if not meus_filmes or not preferencias_outro_numeros:
                print("Erro: Certifique-se de preencher as Opções 1 e 2 primeiro.")
                continue

            print("--- RESULTADO DA AFINIDADE ---")
            
            lista_para_ordenar = preferencias_outro_numeros.copy()
            total_inversoes = contar_inversoes(lista_para_ordenar)
            
            n = len(preferencias_outro_numeros)
            max_inversoes = (n * (n - 1)) // 2
            
            print(f"Seus filmes: {meus_filmes}")
            print(f"Ordem do outro usuário (em números): {preferencias_outro_numeros}")
            print(f"Total de inversões encontradas: {total_inversoes}")
            print(f"Inversões máximas possíveis para {n} itens: {max_inversoes}")
            print("-" * 30)
            
            if total_inversoes <= (max_inversoes / 2):
                print("RESULTADO: Os usuários têm gostos SIMILARES.")
                print("O sistema liberaria as recomendações cruzadas!")
            else:
                print("RESULTADO: Os usuários têm gostos MUITO DIFERENTES.")
                print("O sistema evitaria recomendar os mesmos filmes.")

        elif opcao == '4':
            print("Saindo do MatchFlix... Até logo!\n")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()