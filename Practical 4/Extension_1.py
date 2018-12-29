"""
CP1404/CP5632 Practical
Debugging exercise: almost-working version of a CSV scores file program.
The scores.csv file stores scores for each subject for 10 people.
This code reads the lines into lists, saves the first line as a list of subject codes and
converts the rest of the lines from a list of strings into a list of numbers,
which it then prints with the maximum value for that subject.
Nice. Except, it’s broken! It reads the lists per user not per subject so the results are incorrect.
Use the debugger to follow what it's doing... then fix it.
"""

from tabulate import tabulate
def main():
    """Read and display student scores from scores file."""
    scores_file = open("scores.csv")
    scores_data = scores_file.readlines()
    print(scores_data)
    subjects = scores_data[0].strip().split(",")
    score_values = []
    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")
        score_numbers = [int(value) for value in score_strings]
        score_values.append(score_numbers)
    scores_file.close()
    print("Score value is: ", score_values)
    final_score = []
    for i in range(len(subjects)):
        print(subjects[i], "Scores:")
        score_sequence = []
        for score in score_values:
            single_score = score[i]
            print(single_score)
            score_sequence.append(single_score)
        print(score_sequence)
        final_score.append(score_sequence)
        print("Max:", max(score_sequence))
        print("Min:", min(final_score[i]))
        print("Average:", sum(score_sequence)/len(score_sequence))
        print()
    print(tabulate(score_values, headers=subjects, tablefmt="grid"))
main()
