"""small voting program for class captain."""
from __future__ import print_function
from operator import itemgetter

def vote_class_captain():
    """voting program"""
    candidates = list()

    print("please enter candidate names. Press Return to finish.")

    while len(candidates) <= 4:
        name = input("Please enter candidate name:")
        if name != "":
            candidates.append([name, 0])
        else:
            if len(candidates) < 2:
                print("There must be at least 2 candidates")
            else:
                break

    print("Candidates are: ")

    for index in range(0, len(candidates)):
        print(candidates[index][0], "[" + str(index + 1) + "]")

    for index in range(0, 4):
        vote = input("Enter the candidate number to vote and press enter Return to exit: ")
        if vote == "":
            break
        try:
            vote = int(vote)
            if vote < 1 or vote > len(candidates):
                print("Invalid vote: Out of range. ")
            else:
                candidates[vote - 1][1] += 1
        except ValueError:
            print("Invalid vote: not an integer.")

    #use the votes to sort the array.
    sorted_candidates = sorted(candidates, reverse=True, key=itemgetter(1))

    if sorted_candidates[0][1] == sorted_candidates[1][1]:
        print("No overall winner")
    else:
        sorted_candidates[0][0] = sorted_candidates[0][0] + " * New class captain"

    #Not formatted.
    print(sorted_candidates)

if __name__ == '__main__':
    vote_class_captain()
