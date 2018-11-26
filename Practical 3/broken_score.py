def main():
    result = cal_score()
    print(result)
def cal_score():
    score = float(input("Enter a score: "))
    if score <0 or score >100:
        return "Invalid score"
    elif score >=90:
        return "Excellent"
    elif score >=50:
        return "Pass"
    else:
        return "Bad"
main()