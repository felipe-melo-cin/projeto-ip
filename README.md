```
    ____  __  ______  _________  __________  ____  ________ 
   / __ \/ / / / __ \/ ____/   |/_  __/ __ \/ __ \/  _/ __ \
  / /_/ / / / / /_/ / / __/ /| | / / / / / / /_/ // // / / /
 / ____/ /_/ / _, _/ /_/ / ___ |/ / / /_/ / _, _// // /_/ / 
/_/    \____/_/ |_|\____/_/  |_/_/  \____/_/ |_/___/\____/  
                                                            
```

# 💀 PURGATÓRIO

Após sofrer uma morte dolorida (alguém atirou o pau no gato) você se encontrou entre as camadas da salvação e danação eterna, mas não tem muito o que fazer, já que você _meio_ que mereceu. Complete os mapas e suba os andares pro céu, mas saiba que o tempo é escasso, e suas sete vidas estão em jogo.

![Miausma](https://i.imgur.com/yNtowqo.gif)



## Membros da Equipe

* Alex Mayrink <ama9>
* Beatriz Silva de Oliveira <bso>
* Felipe Melo de Albuquerque <fma4>
* Nicolas Souto <ndss>
* Juan Henrique <jhs>

## Divisão de Tarefas

> * Felipe: programação, conexão de interfaces, ideação e relatório.
> * Alex: ficou com o design de algoritmo, game design, montagem da soundtrack, ideação e playtesting.
> * Beatriz: Design de UI, sprites, ilustração e ideação.
> * Juan: Coleta de efeitos sonoros, ideação, playtesting.
> * Nicolas: Coleta de efeitos sonoros, ideação, montagem da soundtrack.


### Arquitetura do Código

```
* 🗂️ Algoritmos: Contém a parte lógica do campo minado, decide onde ficam as bombas.
* 🗂️ Audio: Contém os assets de efeitos sonoros e as músicas de fundo.
* 🗂️ Constantes: Armazena os valores constantes e funções genéricas úteis.
* 🗂️ Game: Nosso gerenciador de estados, que realiza as 
mudanças na tela entre começo, meio e fim do jogo. Além disso, a classe de jogo inicializa todos os sprites e carrega o loop de eventos principal.
* 🗂️ Interfaces: Trata de elementos visuais na tela e permite que o jogador interaja com eles. (Malha de botões, malha de ladrilhos, botões)
* 🗂️ Others: Implementa funções como o timer e a classe do mouse.
* 🗂️ Sprites: Contém as classes que exibem os sprites.
* 🗂️ Sounds: Contém as classes que mexem com os sons.
```
## 🐾 Instalação

### 1. Pygame
Para jogar, certifique-se que você tem a biblioteca [_PyGame_ ](https://www.pygame.org/news) instalada em um ambiente virtual ou no próprio Python.

```
pip install pygame
```
### 2. Instalando o jogo
Para instalar Purgatório, acesse o repositório do jogo [clicando nesse link. ](https://github.com/felipe-melo-cin/projeto-ip)
Extraia a pasta no seu computador.

Depois, vá até a pasta do jogo e abra o arquivo "python main.py"

## Controles

Seu objetivo é conseguir o máximo de pontos possível sem perder todas as vidas ou acabar o tempo. 
* WASD ou ← ↑ → ↓ --> Movimenta o Miausma pela tela, para pegar os coletáveis e cavar.
* Clique direito --> Escava
* Clique esquerdo --> Põe bandeira
* E --> Meeooowwwww

## Coletáveis

Existem itens no jogo que podem te ajudar a chegar mais longe. Sempre que liberar mais parte dos mapas, os seguintes itens podem aparecer:

1. Bandeira: a quantidade de bandeiras do Miausma é limitada. O coletável de bandeira te concede uma a mais.
2. Tempo: Um relógio capaz de te conceder +3 segundos na run.
3. Coração: Recupera uma das suas sete vidas.

## Prints do Jogo
![Tela Inicial](https://i.imgur.com/CWbTdvK.png)
![Main Game](https://i.imgur.com/NZkvfa3.png)
![End Screen](https://i.imgur.com/YgG9GvN.png)

## Dificuldades no processo de desenvolvimento
### 1) Implementação
Foi difícil chegar em um consenso com o grupo do que poderia e não poderia ser implementado no jogo, e muitas mecânicas divertidas tiveram que ser abandonadas em prol do limite de duas semanas. Coisas como a movimentação do Miausma também foram difíceis de determinar (se ele seria fixo nos tiles, se ele conseguiria atravessar partes não cavadas), mas em geral, o resultado ficou satisfatório para todos os envolvidos no projeto.
### 2) Acostumar com a biblioteca Pygame
Muitos membros do grupo não haviam sido introduzidos previamente à biblioteca Pygame, apesar de já terem mexido com outras _Engines._ Com isso, o processo de aprendizado ficou puxado para não prejudicar o tempo de desenvolvimento do jogo, que já era pequeno. 
### 3) Dor muscular
Ficamos sentados por um bom tempo 
