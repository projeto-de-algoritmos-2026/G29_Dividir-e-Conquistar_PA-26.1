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

## Screenshot

## Instalação 
Linguagem: *Python*

## Gravação
A gravação pode ser acessada através do link