from Practical_6.guitar import Guitar

def main():
    first_guitar = Guitar ("Gibson L-5 CES", 1922, 16035.40)
    print(first_guitar)
    print(first_guitar.get_age())
    print(first_guitar.is_vintage())

main()