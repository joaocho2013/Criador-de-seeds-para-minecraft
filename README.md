# ⛏️ Minecraft Seed Bot

Um bot para Discord desenvolvido em Python que ajuda os jogadores a encontrar seeds de Minecraft de acordo com seus objetivos, oferecendo opções de mundos e coordenadas de estruturas importantes.

## 🎯 Objetivo do projeto

O objetivo é criar um bot interativo que dê boas-vindas aos jogadores e permita escolher o tipo de seed que desejam explorar. Após a escolha, o bot apresentará **3 opções de seeds**, com informações e coordenadas úteis para cada uma.

## ⚙️ Funcionalidades

Ao iniciar uma conversa, o bot irá:

1. 👋 Dar boas-vindas ao jogador.
2. 📋 Apresentar 13 opções de seeds.
3. 🎮 Perguntar qual tipo de mundo o jogador deseja.
4. 🌍 Mostrar 3 opções de seeds de acordo com a escolha.
5. 📍 Informar coordenadas de estruturas importantes.
6. ✅ Permitir que o jogador escolha outra categoria quando quiser.

## 🌎 Opções de seeds

| Nº | Categoria | Descrição |
|---:|---|---|
| 1 | 🏗️ Construções | Mundos com paisagens interessantes para construir casas e cidades. |
| 2 | ⚡ Speedrun | Seeds com estruturas úteis para tentar zerar o jogo rapidamente. |
| 3 | 🏘️ Vilas | Seeds com vilas próximas ao ponto inicial. |
| 4 | 💎 Mineração | Mundos com boas regiões para explorar cavernas e procurar minérios. |
| 5 | 🏰 Castelos | Paisagens adequadas para construir castelos e fortalezas. |
| 6 | 🌸 Biomas bonitos | Mundos com paisagens e biomas interessantes. |
| 7 | 🏝️ Ilhas | Seeds com ilhas para explorar ou sobreviver. |
| 8 | ❄️ Neve | Mundos com montanhas nevadas e regiões geladas. |
| 9 | 🌳 Florestas | Seeds com grandes florestas e recursos naturais. |
| 10 | 🏜️ Deserto | Mundos com desertos e possíveis estruturas para explorar. |
| 11 | 🧭 Exploração | Seeds com estruturas e lugares interessantes para descobrir. |
| 12 | 💀 Sobrevivência difícil | Mundos para jogadores que procuram um desafio maior. |
| 13 | 🐼 Biomas raros | Seeds com biomas específicos ou difíceis de encontrar. |

## 📍 Como o bot vai funcionar?

**Exemplo de conversa no Discord:**

**Bot:** Olá, aventureiro! 👋 Bem-vindo ao Minecraft Seed Bot!

**Bot:** Qual tipo de seed você deseja encontrar?

1. 🏗️ Construções
2. ⚡ Speedrun
3. 🏘️ Vilas
4. 💎 Mineração
5. 🏰 Castelos
6. 🌸 Biomas bonitos
7. 🏝️ Ilhas
8. ❄️ Neve
9. 🌳 Florestas
10. 🏜️ Deserto
11. 🧭 Exploração
12. 💀 Sobrevivência difícil
13. 🐼 Biomas raros

**Usuário:** 3 — Vilas

**Bot:** Excelente escolha! 🏘️ Aqui estão 3 seeds para encontrar vilas:

- **Seed 1:** `123456789`
  - Vila: X: 120, Y: 70, Z: -80
- **Seed 2:** `987654321`
  - Vila: X: -200, Y: 68, Z: 150
- **Seed 3:** `456789123`
  - Vila: X: 85, Y: 72, Z: 230

*Observação: as seeds e coordenadas acima são exemplos ilustrativos, não resultados verificados no jogo.*

## 🧭 Coordenadas e estruturas

O bot poderá fornecer informações diferentes de acordo com a categoria escolhida:

- **Vilas:** coordenadas de vilas próximas ao ponto inicial.
- **Speedrun:** coordenadas de estruturas úteis, como fortalezas do Nether e fortalezas do End.
- **Mineração:** locais recomendados para explorar cavernas e procurar minérios.
- **Exploração:** coordenadas de estruturas como templos, monumentos e cidades antigas, quando disponíveis na seed.

As coordenadas e estruturas precisam ser verificadas para a seed e a versão do Minecraft escolhidas. O portal do End também exige atenção: a fortaleza que contém o portal fica no mundo normal, enquanto a dimensão do End é acessada por ele.

## 🛠️ Tecnologias utilizadas

- Python
- Discord.py
- Discord Developer Portal
- Minecraft Java Edition ou Bedrock Edition, dependendo das seeds utilizadas.

## 📌 Etapas do desenvolvimento

- [ ] Criar o bot no Discord Developer Portal.
- [ ] Configurar o bot com Python e Discord.py.
- [ ] Criar o comando de boas-vindas.
- [ ] Implementar o menu com as 13 categorias.
- [ ] Cadastrar seeds para cada categoria.
- [ ] Adicionar as coordenadas das estruturas.
- [ ] Exibir 3 opções por categoria.
- [ ] Testar as seeds na versão correta do Minecraft.
- [ ] Melhorar as mensagens e a interação com os usuários.

## 🚀 Resultado esperado

Ao final do projeto, o bot será capaz de ajudar jogadores a encontrar mundos de Minecraft adequados ao seu estilo de jogo, apresentando seeds organizadas por categorias e informações úteis para começar suas aventuras.

## 👨‍💻 Autor

Projeto desenvolvido como prática de programação em Python e criação de bots para Discord.
