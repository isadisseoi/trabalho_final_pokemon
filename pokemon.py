import httpx
import pandas as pd
import asyncio

# Função para obter informações adicionais de tipo e habilidade de um Pokémon
async def obter_informacoes_adicionais(tipo_url=None, habilidade_url=None):
    async with httpx.AsyncClient() as client:
        tipo_info, habilidade_info = {}, {}
        
        # Busca informações do tipo
        if tipo_url:
            tipo_resp = await client.get(tipo_url)
            if tipo_resp.status_code == 200:
                tipo_data = tipo_resp.json()
                tipo_info = {
                    "tipo": tipo_data['name'],
                    "fortes_contra": [t['name'] for t in tipo_data['damage_relations']['double_damage_to']]
                }
        
        # Busca informações da habilidade
        if habilidade_url:
            habilidade_resp = await client.get(habilidade_url)
            if habilidade_resp.status_code == 200:
                habilidade_data = habilidade_resp.json()
                habilidade_info = {
                    "habilidade": habilidade_data['name'],
                    "efeito_curto": habilidade_data['effect_entries'][0]['short_effect']
                }
        
        return tipo_info, habilidade_info

# Função assíncrona principal para buscar dados de Pokémons
async def obter_pokemon(nome_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}"
    async with httpx.AsyncClient() as client:
        resposta = await client.get(url)
        if resposta.status_code == 200:
            dados_pokemon = resposta.json()
            tipo_url = dados_pokemon['types'][0]['type']['url'] if dados_pokemon['types'] else None
            habilidade_url = dados_pokemon['abilities'][0]['ability']['url'] if dados_pokemon['abilities'] else None
            
            # Busca informações de tipos e habilidades
            tipo_info, habilidade_info = await obter_informacoes_adicionais(tipo_url, habilidade_url)
            
            # Organiza as informações do Pokémon
            pokemon_info = {
                "nome": dados_pokemon['name'],
                "altura": dados_pokemon['height'],
                "peso": dados_pokemon['weight'],
                "experiencia_base": dados_pokemon['base_experience'],
                **tipo_info,
                **habilidade_info
            }
            return pokemon_info

# Lista de Pokémons "interessantes" para buscar
pokemons_interessantes = ["pikachu", "charmander", "squirtle"]

# Função para buscar todos os Pokémons
async def buscar_pokemons():
    tarefas = [obter_pokemon(nome) for nome in pokemons_interessantes]
    dados_pokemons = await asyncio.gather(*tarefas)
    return dados_pokemons

# Executa e cria o DataFrame
dados_pokemons = asyncio.run(buscar_pokemons())
df = pd.DataFrame(dados_pokemons)
print(df)
