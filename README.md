# G29_Dividir-e-Conquistar_PA-26.1

Número da lista: 29

Conteúdo da disciplina: *Counting Inversions*

## Alunos 
| Nome | Matrícula |
|------|-----------|
| Alan Farias Braga | 251005909 |
| Vilmar José Fagundes | 231026590 |

## Sobre 

Este projeto implementa o algorítimo de Dividir e Conquistar Counting Inversions para resolver o problema em questão

Imagine a Netflix ou o Spotify. Para recomendar filmes ou músicas, eles precisam encontrar usuários com gostos parecidos com os seus. Se você rankeia 5 filmes na ordem [A, B, C, D, E], e outro usuário rankeia os mesmos filmes na ordem [B, A, E, D, C], o sistema usa o *Counting Inversions* para medir a similaridade entre vocês. Quanto menor o número de inversões, mais parecidos são os gostos, e logo, o que ele gostou tem alta chance de ser recomendado para você.

O programa roda o algoritmo e descobre o total de inversões. Depois, ele calcula o pior cenário possível (uma lista totalmente invertida) usando a fórmula de análise combinatória: 

$$
\frac{n*(n-1)}{2} 
$$

O programa compara as inversões reais com o máximo possível. A lógica estipulada foi: se a discordância for menor ou igual à metade do pior caso possível, o sistema os considera "similares" e aprova a recomendação cruzada.

## Screenshots

As imagens a seguir representa o menu inicial exibido no terminal, junto com a primeira execução do sistema.

Foram executados testes manuais com o sistema. A seguir, são apresentadas as capturas de tela relacionadas à execução dos testes para demonstrar a eficácia do algoritmo de contagem de inversões.

### Teste 1: Cadastrar uma lista base de filmes
**Passos:**
1. Escolher a opção 1.
2. Digitar a quantidade: 5.
3. Inserir os nomes dos filmes em ordem de preferência (ex: a, b, c, d, e).

**Resultado Esperado:** O sistema deve exibir "Top filmes cadastrados com sucesso!" e mostrar a ordem ideal que servirá de base para o algoritmo.

**Imagem 1: Adição da lista base**
![Teste 1: Cadastrar Filmes](assets/Captura%20de%20tela%201.png)


### Teste 2: Inserir preferências similares (Poucas Inversões)
**Passos:**
1. Escolher a opção 2.
2. Rankear os filmes previamente cadastrados com uma ordem muito parecida com a original: 1, 2, 4, 3, 5.

**Resultado Esperado:** O sistema deve capturar a entrada sem erros, mapear a posição dada pelo outro usuário e exibir o "Vetor gerado para o algoritmo".

**Imagem 2: Entrada de preferências do segundo usuário**
![Teste 2: Inserir Preferências Similares](assets/Captura%20de%20tela%202.png)


### Teste 3: Verificar Afinidade com Resultado Positivo (Match)
**Passos:**
1. Escolher a opção 3.

**Resultado Esperado:** O algoritmo modificado deve contar exatamente 1 inversão (já que apenas o 3 e o 4 trocaram de lugar). Como 1 é menor ou igual à metade do limite máximo de inversões (10), o sistema deve exibir "RESULTADO: Os usuários têm gostos SIMILARES".

**Imagem 3: Resultado de Afinidade Positiva**
![Teste 3: Verificar Afinidade Positiva](assets/Captura%20de%20tela%203.png)


### Teste 4: Inserir preferências divergentes (Muitas Inversões)
**Passos:**
1. Escolher a opção 2 novamente para sobrescrever as preferências.
2. Rankear os filmes com uma ordem quase oposta à original: 5, 4, 1, 3, 2.

**Resultado Esperado:** O sistema deve atualizar o vetor de mapeamento com sucesso para a nova ordem solicitada.

**Imagem 4: Entrada de preferências divergentes**
![Teste 4: Inserir Preferências Divergentes](assets/Captura%20de%20tela%204.png)


### Teste 5: Verificar Afinidade com Resultado Negativo (Sem Match)
**Passos:**
1. Escolher a opção 3.

**Resultado Esperado:** O algoritmo deve varrer o novo vetor e encontrar 8 inversões. Como 8 ultrapassa a tolerância (metade de 10), o sistema deve exibir "RESULTADO: Os usuários têm gostos MUITO DIFERENTES" e bloquear as recomendações.

**Imagem 5: Resultado de Afinidade Negativa**
![Teste 5: Verificar Afinidade Negativa](assets/Captura%20de%20tela%205.png)

## Instalação 
Linguagem: *Python*

## Gravação
A gravação pode ser acessada através do link