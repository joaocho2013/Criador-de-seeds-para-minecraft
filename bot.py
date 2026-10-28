#pip install discord.py
#pip install python-dotenv
#instalar essas duas bibliotecas
import os
import discord
from discord.ext import commands
from discord.ui import Select, View
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

CATEGORIAS = {
    "🏗️ Construções": [
        {"seed": "712262452098460", "descricao": "Possui duas vilas grandes posicionadas lado a lado, contornadas por um lago panorâmico e montanhas perfeitas para bases medievais ou vilas personalizadas", "estruturas": []},
        {"seed": "9064150133272194", "descricao": "Coloca você perto de duas vilas cercadas por árvores de cerejeira (cherry blossom) e um lago central. Ideal para quem busca um visual romântico, japonês ou aconchegante.", "estruturas": []},
        {"seed": "-5868404692257221169", "descricao": "Traz uma vila isolada no meio de uma floresta denotada por grandes montanhas. Ótimo para quem quer privacidade e um desafio natural de relevo.", "estruturas": []},
    ],
    "⚡ Speedrun": [
        {"seed": "47849012232314", "descricao": "Apresenta uma vila no ponto de spawn acompanhada de outras três vilas logo por perto, incluindo dois ferreiros com recursos iniciais excelentes para acelerar a progressão.", "estruturas": []},
        {"seed": "-541714255396397480", "descricao": " Ideal para iniciantes ou recordes curiosos, pois possui o portal do End com todos os 12 Olhos de Ender já colocados diretamente na estrutura inicia", "estruturas": []},
        {"seed": "873416853027626382", "descricao": "Utilizada por corredores experientes para tentar marcas abaixo de 20 minutos, com um posicionamento equilibrado de estruturas-chave.", "estruturas": []},
    ],
    "🏘️ Vilas": [
        {"seed": "712262452098460", "descricao": "Duas vilas grandes unidas ao redor de um lago e rodeadas por montanhas, com grande variedade de NPCs e lojistas", "estruturas": []},
        {"seed": "9064150133272194", "descricao": "Começar perto de uma vila", "estruturas": []},
        {"seed": "2015606532547647", "descricao": "Reúne três vilas de planície muito próximas, ideais para montar uma base com muitos recursos iniciais, além de portais do Nether destruídos e naufrágios.", "estruturas": []},
    ],
    "💎 Mineração": [
        {"seed": "8110137054462309706", "descricao": "Você começa com uma vila de savana a leste, um posto avançado de saqueadores ao sul, além de portais e cavernas fáceis de explorar logo no início", "estruturas": []},
        {"seed": "7IwbCZAKxzI", "descricao": "Gera várias vilas logo no ponto inicial com casas de ferreiro, portal do nether em ruína e navios naufragados. Quebrando logo abaixo de certas coordenadas no spawn, você encontra dezenas de diamantes e acesso direto a uma grande mina abandonada e Trial Chambers", "estruturas": []},
        {"seed": "pxDtvffxexg", "descricao": "Transporte direto para uma Ancient City (Cidade Ancestral) localizada logo abaixo do ponto de nascimento, com acampamento abandonado, barris de recursos iniciais e veias de diamantes abundantes nas proximidades", "estruturas": []},
    ],
    "🏰 Castelos": [
        {"seed": "4637908366460397568", "descricao": "Oferece um relevo plano e equilibrado que espelha perfeitamente a estética de um castelo medieval tradicional da Idade Média, facilitando a construção de muralhas e pátios", "estruturas": []},
        {"seed": "7700979368314050849", "descricao": "Ideal para construções maiores e mais elaboradas, apresentando múltiplos níveis de relevo e anexos naturais que se adaptam bem a estruturas complexas de pedra.", "estruturas": []},
        {"seed": "1884218084082602064", "descricao": "Uma versão ampla que conta com espaço para três torres adicionais, andares extras e uma grande travessia de ponte sobre o terreno.", "estruturas": []},
    ],
    "🌸 Biomas bonitos": [
        {"seed": "2048005618087379093", "descricao": "Você começa em uma ilha cercada por um fosso natural e um enorme bioma de cerejeiras, com animais e entrada para uma Ancient City (Cidade Antiga) por perto", "estruturas": []},
        {"seed": "712262452098460", "descricao": "Duas vilas grandes lado a lado abraçando um lago tranquilo e cercadas por montanhas", "estruturas": []},
        {"seed": "9064150133272194", "descricao": "Duas vilas próximas rodeadas por árvores de cerejeira, um lago central e cavernas com abelhas", "estruturas": []},
    ],
    "🏝️ Ilhas": [
        {"seed": "1122334455", "descricao": "Aventura em uma ilha isolada", "estruturas": []},
        {"seed": "2233445566", "descricao": "Construir uma base em uma ilha", "estruturas": []},
        {"seed": "3344556677", "descricao": "Sobreviver longe do continente", "estruturas": []},
    ],

    "❄️ Neve": [
        {"seed": "4455667788", "descricao": "Explorar regiões cobertas de neve", "estruturas": []},
        {"seed": "5566778899", "descricao": "Construir uma base nas montanhas geladas", "estruturas": []},
        {"seed": "6677889900", "descricao": "Aventura em um mundo congelado", "estruturas": []},
    ],

    "🌳 Florestas": [
        {"seed": "7788990011", "descricao": "Explorar uma grande floresta", "estruturas": []},
        {"seed": "8899001122", "descricao": "Construir uma cabana na floresta", "estruturas": []},
        {"seed": "9900112233", "descricao": "Começar a aventura cercado por árvores", "estruturas": []},
    ],

    "🏜️ Deserto": [
        {"seed": "1357913579", "descricao": "Explorar um vasto deserto", "estruturas": []},
        {"seed": "2468024680", "descricao": "Construir uma base no deserto", "estruturas": []},
        {"seed": "3579135791", "descricao": "Aventura em busca de templos do deserto", "estruturas": []},
    ],

    "🧭 Exploração": [
        {"seed": "4680246802", "descricao": "Explorar estruturas pelo mundo", "estruturas": []},
        {"seed": "5791357913", "descricao": "Viajar por diferentes regiões", "estruturas": []},
        {"seed": "6802468024", "descricao": "Descobrir lugares misteriosos", "estruturas": []},
    ],

    "💀 Sobrevivência difícil": [
        {"seed": "7913579135", "descricao": "Enfrentar um grande desafio de sobrevivência", "estruturas": []},
        {"seed": "8024680246", "descricao": "Sobreviver com poucos recursos iniciais", "estruturas": []},
        {"seed": "9135791357", "descricao": "Explorar um mundo com condições difíceis", "estruturas": []},
    ],

    "🐼 Biomas raros": [
        {"seed": "1020304050", "descricao": "Procurar biomas difíceis de encontrar", "estruturas": []},
        {"seed": "2030405060", "descricao": "Explorar regiões com diferentes biomas", "estruturas": []},
        {"seed": "3040506070", "descricao": "Descobrir paisagens e biomas incomuns", "estruturas": []},
    ],
}

def montar_resposta(categoria):
    seeds = CATEGORIAS[categoria]
    linhas = [f"## {categoria}", "Aqui estão 3 opções cadastradas:\n"]

    for numero, item in enumerate(seeds, start=1):
        linhas.append(f"**{numero}. {item['descricao']}**")
        linhas.append(f"Seed: `{item['seed']}`")

        if item["estruturas"]:
            linhas.append("Coordenadas/estruturas:")
            for estrutura in item["estruturas"]:
                linhas.append(
                    f"- {estrutura['nome']}: X: {estrutura['x']}, "
                    f"Y: {estrutura.get('y', '?')}, Z: {estrutura['z']}"
                )
        else:
            linhas.append(
                " "
                ""
            )
        linhas.append("")

    linhas.append(
        "Estas seeds sao da versao 1.20.1 do Minecraft e foram"
        "verificadas. Confirme a seed, a edição e a versão do Minecraft antes de usar."
    )
    return "\n".join(linhas)

class CategoriaSelect(Select):
    def __init__(self):
        opcoes = [
            discord.SelectOption(label=nome, value=nome)
            for nome in CATEGORIAS.keys()
        ]
        super().__init__(
            placeholder="Escolha o tipo de seed...",
            min_values=1,
            max_values=1,
            options=opcoes
        )

    async def callback(self, interaction: discord.Interaction):
        categoria = self.values[0]
        await interaction.response.send_message(
            montar_resposta(categoria),
            ephemeral=True
        )

class MenuSeeds(View):
    def __init__(self):
        super().__init__(timeout=180)
        self.add_item(CategoriaSelect())

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command(name="start")
async def start(ctx):
    embed = discord.Embed(
        title="⛏️ Minecraft Seed Bot",
        description=(
            f"Olá, {ctx.author.mention}! Seja bem-vindo! 👋\n\n"
            "Escolha o tipo de seed que você procura no menu abaixo. "
            "Vou mostrar 3 opções da categoria escolhida."
        ),
        color=discord.Color.green()
    )
    await ctx.send(embed=embed, view=MenuSeeds())

@bot.command(name="ajuda")
async def ajuda(ctx):
    await ctx.send(
        "**Comandos disponíveis**\n"
        "`!start` — abre o menu de categorias.\n"
        "`!ajuda` — mostra esta mensagem."
    )



bot.run("Token")
