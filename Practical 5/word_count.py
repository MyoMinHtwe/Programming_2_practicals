def main():
    string = input("Enter a string: ")
    string = string.split()
    word_to_count = {}
    for word in string:
        try:
            word_to_count[word] += 1
        except KeyError:
            word_to_count[word] = 1
    for key, value in sorted(word_to_count.items()):
        print(key,value)
main()