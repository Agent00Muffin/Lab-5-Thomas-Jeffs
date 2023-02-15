from pastebin_api import post_new_paste
from dad_jokes_api import search_for_dad_jokes

def main():
    search_term = get_search_term()
    joke_list = search_for_dad_jokes(search_term)
    if joke_list:
        title, body_text = get_paste_data(joke_list, search_term)
        paste_url = post_new_paste(title, body_text, '1D')





    return

def get_search_term():
    return


def get_paste_data(joke_list, search_term):
    return #title, body_text

if __name__=='__main__':
    main()
