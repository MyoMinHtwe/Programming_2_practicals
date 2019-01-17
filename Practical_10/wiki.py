import wikipedia

def main():
    search = 'Search'

    while search != '':
        search = input('Input search word: ')
        try:
            print(wikipedia.summary(search))
        except wikipedia.exceptions.DisambiguationError:
            print('Ambiguity')
        except wikipedia.exceptions.WikipediaException:
            print('Exited!')


main()