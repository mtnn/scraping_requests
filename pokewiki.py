import requests

class PokeWiki:
    def __get_page(self, name: str):
        page = requests.get(f'https://pokemon.fandom.com/api.php',
                params = {
                    'format': 'json',
                    'formatversion': 'latest',
                    'action': 'query',
                    'titles': name,
                    'prop': 'revisions',
                    'rvprop': 'content'
                    }).json()['query']['pages'][0]
        if not 'revisions' in page:
            return ''
        page = page['revisions'][0]['content']
        for line in page.split('\n'):
            if line.startswith('{{Pok\u00e9Box'):
                return page
        return ''

    def get_species(self, name: str):
        for e in self.__get_page(name).split('\n'):
            if e.startswith('|species'):
                s = e.split('=')[-1].strip('[ ]')
                return None if (not s) else s
        return None

    def get_abilities(self, name: str):
        l = list()
        for e in self.__get_page(name).split('\n'):
            if e.startswith('|ability'):
                l.extend([x.strip('[ ]') for x in e.split('=')[-1].split('<br />')])
            if e.startswith('|dw'):
                l.append(e.split('=')[-1].strip('[ ]'))
        for e in l:
            if not e:
                return list()
        return l
