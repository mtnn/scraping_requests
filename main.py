from pokewiki import PokeWiki
from requests.exceptions import RequestException


def main():
    test_pokemon("bulbasaur")
    test_pokemon("ditto")
    test_pokemon("blissey")
    test_pokemon("no such pokemon")
    test_pokemon("Pok\u00e9mon_Journeys:_The_Series_(series)")
    test_pokemon("Ash ketchum")
    test_pokemon("Template:Pok\u00e9Box")


def test_pokemon(name: str):
    p = PokeWiki()
    try:
        print(f"name : {name}")
        print(f"species : {p.get_species(name)}")
        print(f"abilities : {p.get_abilities(name)}")
        print()
    except RequestException as e:
        print(e)


if __name__ == "__main__":
    main()
