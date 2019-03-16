import requests, json, base64

test_redirect_url = r'https://127.0.0.1:5454' # This is just a dummy url.. you need to add it to your app here as a redirect url here as well :)
client_id = b'<your-app-id>'
client_secret = b'<your-app-secret>'
output_file_name = r'c:\temp\my_saved_songs.txt'

#TODO: PASTE a real token here after you access and authorize the app in your url
cur_token = '<your-token-after-accessing-to-the-url-said!>'
refresh_token = 'extracted on start..'

class SpotifySession():
    def __init__(self):
        global cur_token, refresh_token
        self.s = requests.session()
        self.token = cur_token
        self.refresh_token = refresh_token
        self.token_type = 'code'

    def auth(self):
        auth_url = r'https://accounts.spotify.com/authorize?client_id=%s' % client_id.decode('ascii')
        auth_url += '&redirect_uri=%s' % str(test_redirect_url)
        auth_url += '&scope=user-read-private%20user-read-email%20user-library-read'
        auth_url += '&state=%d' % (123) # dummy state over here.
        auth_url += '&response_type=%s' % (self.token_type)
        print('starting auth process... %s' % auth_url)
        res = self.s.get(auth_url)
        print('auth response ', res, res.content)
        print('Go and enter with your account into this link and agree that in order to activate it hmmm...')
        return res

    def refresh_tokens(self, new_token_gen=False):
        # access to spotify and refresh access tokens: https://accounts.spotify.com/api/token
        token_url = 'https://accounts.spotify.com/api/token'
        if new_token_gen: # for new users added only probably...
            data = {'grant_type': 'authorization_code', 'code': self.token, 'redirect_uri': test_redirect_url}
        else:
            data = {'grant_type': 'refresh_token', 'refresh_token': self.refresh_token}

        auth_header = (b'Basic %s' % (base64.b64encode(client_id + b':' + client_secret)))
        headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': auth_header}
        print('starting token getting process...')
        res = self.s.post(token_url, headers=headers, data=data)
        if res.status_code is not 200:
            print('cant get/refresh new access token.. check it out..')
            return res

        self.last_tokens = json.loads(res.text)
        self.token = self.last_tokens['access_token']
        if 'refresh_token' in self.last_tokens:
            self.refresh_token = self.last_tokens['refresh_token']
        return res

    def validate_token(self):
        url = 'https://api.spotify.com/v1/me'
        headers = {'Authorization': 'Bearer %s' % self.token}
        print('auth validation process started...')
        res = self.s.get(url, headers=headers)
        print('validation of token resposne was: ', res.status_code, res, res.content)
        return res


    def _get_user_songs_offset(self, offset, limit):
        url = 'https://api.spotify.com/v1/me/tracks?offset=%d&limit=%d' % (offset, limit)
        headers = {'Authorization': 'Bearer %s' % self.token}
        res = requests.get(url, headers=headers)
        d = json.loads(res.text)
        return d['items'], d['total']

    def get_user_songs(self):
        print('obtaining total number of user saved songs...')
        _, total = self._get_user_songs_offset(0, 1) # just get total number of saved songs in here.
        cur_offset = 0
        limit = 50
        self.user_songs = []

        print('obtaining %d songs...' % total)
        while cur_offset <= total:
            items, total = self._get_user_songs_offset(cur_offset, limit)
            cur_offset += 50
            self.user_songs += items
            print('got %d/%d songs already' % (cur_offset, total))
        print('got all the songs in here...')
        return self.user_songs

    def get_last_user_songs(self, cnt=50):
        items, total = self._get_user_songs_offset(0, cnt)
        return items

    def write_user_songs_list(self, output=output_file_name):
        d = open(output, 'wb')
        for item in self.user_songs:
            artists = ', '.join([artist['name'] for artist in item['track']['artists']])
            d.write(('%s - %s\r\n' % (item['track']['name'], artists)).encode('utf-8'))
        d.close()

def test():
    # full flow to save songs list to file in c:\temp named "my_saved_songs.txt"
    s = SpotifySession()
    res = s.refresh_tokens()
    res = s.get_user_songs()
    s.write_user_songs_list()

def first_time_usage()
    s = SpotifySession()
    s.auth()

first_time_usage()
test()
