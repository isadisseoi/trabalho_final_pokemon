# Introdução 📜

Olá, treinador Pokémon! Nesta API você terá em mãos uma legítima Pokédex, na qual você contará com uma lista das 9 gerações de Pokémons. Nela, você poderá obter informações detalhadas incluindo seus tipos, habilidades, estatísticas base e muito mais. Boa aventura!

![233459737-46aa426a-7c0a-439c-8ebc-b0a6ca89ba01](https://github.com/user-attachments/assets/272b3eff-0e86-4894-a23b-7e496981d98c)

# Sobre o projeto 🔧

A API foi desenvolvida baseada no PokeAPI, em que o usuário consegue obter informação gerais sobre os Pokémons como tipo, habilidade e estatística. O projeto também possui um sistema de alerta em Python, em que ele exibe uma mensagem de alerta no console em intervalos regulares e finaliza após 5 alertas. Neste repositório, existem três versões do código: uma versão assíncrona que faz requisições de forma mais eficiente utilizando `httpx` e `asyncio` e duas versões sincronizadas que também utilizam `httpx`, mas com uma abordagem de tratamento de erros.

# Instalação 💻
1. Python 3.8+ ou superior;
2. Instalar as seguintes dependências: `pip install httpx pandas asyncio`
3. Para a emissão de alertas, instale: `python -m venv venv` e
`source venv/bin/activate  #caso sistema operacional seja macOS/Linux`
`.\venv\Scripts\activate  #caso sistema operacional seja Windows` 

# Estrutura do Projeto 📦

O projeto foi organizado da seguinte forma:

0. pokedex/
1. pokedex_async.py  ----- # Código 1 (Assíncrono)
2. pokedex_sync_1.py ----- # Código 2 (Sincronizado com Tratamento de Erros)
3. pokedex_sync_2.py ----- # Código 3 (Sincronizado com Tratamento de Erros)
4. README.md         ----- # Documentação

# Principais Funções 🚀

- obter_informacoes_adicionais (tipo_url, habilidade_url): Busca informações adicionais sobre o tipo e habilidade de um Pokémon.

- obter_pokemon (nome_pokemon): Obtém informações principais, como altura, peso, tipo e habilidades.
  
- buscar_pokemons(): Faz a busca em lote de Pokémons definidos em uma lista (pokemons_interessantes).
  
- alerta(mensagem): Exibe mensagens de erro quando ocorrem falhas na requisição.
  
- obter_pokemon(nome_pokemon): Faz a requisição à API e retorna informações detalhadas sobre o Pokémon.

# Como Usar 📝

1. Clone o repositório:
`git clone https://github.com/seu-usuario/pokedex-api.git`
`cd pokedex-api`

2. Execute o código assíncrono (recomendado para melhor performance):
`python pokedex_async.py`

3. Ou execute o código sincronizado:
`python pokedex_sync_1.py`

# Conclusão 🎉

Esta API oferece uma forma divertida e interativa de explorar dados sobre Pokémons utilizando Python. Seja você um desenvolvedor em busca de exemplos de requisições HTTP ou um fã de Pokémon, esta Pokédex é uma excelente ferramenta para suas aventuras! Boa sorte e que a sua jornada como Mestre Pokémon seja incrível!
