import requests
from decouple import config


token = config('TOKEN')

headers = {
    "Authorization": f"Bearer {token}"
}

def get_lex_id():
    url = "https://api.spotify.com/v1/me/shows"

    resp = requests.get(url, headers=headers)
    # TODO: just gets most recently added show
    return resp.json()['items'][0]['show']['id']

def get_lex_shows():
    lex_id = get_lex_id()
    limit=50
    offset=0
    shows = []
    while True:
        url = f"https://api.spotify.com/v1/shows/{lex_id}/episodes?limit={limit}&offset={offset}"
        resp = requests.get(url, headers=headers)
        new_shows = resp.json()['items']
        if len(new_shows) == 0:
            break
        shows.extend(resp.json()['items'])
        
        offset += limit
    return shows

def unplayed_shows_to_txt():
    with open('lex_shows.txt', 'w') as f:
        for show in get_lex_shows():
            if not show['resume_point']['fully_played']:
                f.write(show['name'] + ',' + show['id'] + '\n')
            
def get_lex_playlist_id():
    url = "https://api.spotify.com/v1/me/playlists"
    resp = requests.get(url, headers=headers)
    # TODO: just gets most recently created playlist
    return resp.json()['items'][0]['id']

def add_ai_shows_to_pl():
    playlist_id = get_lex_playlist_id()
    with open('lex_shows_to_listen_to.txt', 'r') as f:
        shows = f.readlines()
    for show in shows:
        url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?uris=spotify:episode:{show.strip()}"
        requests.post(url, headers=headers)

if __name__ == '__main__':
    add_ai_shows_to_pl()
    