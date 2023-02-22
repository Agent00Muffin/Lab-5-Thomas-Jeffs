import requests

def main():
    pokemon_page = search_for_pokemon('ditto')
    print(pokemon_page)

    return


def search_for_pokemon(pokemon):
    """Gather information on the pokemon wanting to be searched

    Args:
        pokemon(str): Pokemon name

    Returns:
        List: list of information on said pokemon
    """

    clean_name = str(pokemon).strip().lower()
    poke_api_url = f'https://pokeapi.co/api/v2/pokemon/{clean_name}'
    print(f'Getting information for {clean_name}...', end='')
    resp_msg = requests.get(poke_api_url)

    if resp_msg.ok:
        print('success')
        poke_data = resp_msg.json()
        return poke_data
    else:
        print('Failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')

if __name__=='__main__':
    main()