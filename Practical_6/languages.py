from Practical_6.programming_language import ProgrammingLanguage

def main():
    ruby = ProgrammingLanguage ("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage ("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage ("Visual Basic", "Static", False, 1991)

    print(ruby)
    print(python)
    print(visual_basic)

    programming_list = []
    programming_list.append(ruby)
    programming_list.append(python)
    programming_list.append(visual_basic)
    print("\nThe dynamic typed langues are: ")
    for i in range(len(programming_list)):
        test = programming_list[i].is_dynamic()
        if test == True:
            print(programming_list[i].field)

main()