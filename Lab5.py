from pastebin_api import post_new_paste
from poke_api import search_for_pokemon
import sys

def main():
    pokemon = get_poke_name()
    poke_data = search_for_pokemon(pokemon)
    if poke_data:
        title, body_text = paste_data(poke_data)
        paste_url = post_new_paste(title, body_text, '1M')
        print({paste_url})

    return

 # Function that gets pokemon's name from input   
def get_poke_name():
    num_params = len(sys.argv) - 1
    if num_params > 0:
        return sys.argv[1]
    else:
        print("Error: Missing Pokemon name")
        sys-exit(1)

# Function that constructs the paste title and body text
def paste_data(poke_data):
    poke_name = poke_data['forms'][0]['name'].capitalize()
    title = f"{poke_name}'s Abilities"

    ability_list = ["- "+p['ability']['name'] for p in poke_data['abilities']]
    new_entry = '\n'
    body_text = new_entry.join(ability_list)
    
    return title, body_text



    
if __name__=='__main__':
    main()
