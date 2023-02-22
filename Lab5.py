from pastebin_api import post_new_paste
from poke_api import search_for_pokemon
import sys
import re

def main():
    pokemon = get_poke_name()
    poke_data = search_for_pokemon(pokemon)
    if poke_data:
        title, body_text = paste_data(poke_data, pokemon)
        paste_url = post_new_paste(title, body_text)
        print(f'URL of the new paste {paste_url}')

    return

 # Function that gets pokemon's name from input   
def get_poke_name():
    num_params = len(sys.argv) - 1
    if num_params > 0:
        return sys.argv[1]
    else:
        print("Error: Missing search term")
        sys-exit(1)

# Function that constructs the paste title and body text
def paste_data(poke_data, pokemon):

    title = f"{pokemon}'s Abilities"
    


    return title, body_text



    
if __name__=='__main__':
    main()
