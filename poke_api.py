import requests

def main():
    pokemon_page = search_for_pokemon('ditto')
    print(pokemon_page)

    return


def search_for_pokemon(pokemon):
    poke_api_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    poke_list = requests.get(poke_api_url)
    return poke_list




   
if __name__=='__main__':
    main()