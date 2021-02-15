import json, os

file_path = os.path.abspath('..') + '\data'


class Utils:
    def get_cookies(self, cookie):
        with open(f'{file_path}\cookie.json', 'w') as f:
            json.dump(cookie, f)
