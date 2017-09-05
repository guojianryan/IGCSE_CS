"""Write a program which inputs the names of 3 pupils. For each name an exam result, in the range
1 to 100, is also input. The program should print out the names of the pupils in exam result order,
their position, 1, 2 or 3, before their name."""

name_1 = input("What is the first pupil's name?")
score_1 = int(input("What is the first pupil's score?"))

name_2 = input("What is the first pupil's name?")
score_2 = int(input("What is the first pupil's score?"))

name_3 = input("What is the first pupil's name?")
score_3 = int(input("What is the first pupil's score?"))

if score_1 >= score_2 and score_2 >= score_3:
    print("1",name_1)
    print("2",name_2)
    print("3",name_3)

elif score_1 >= score_3 and score_3 >= score_2:
    print("1",name_1)
    print("2",name_3)
    print("3",name_2)

elif score_2 >= score_1 and score_1 >= score_3:
    print("1",name_2)
    print("2",name_1)
    print("3",name_3)

elif score_2 >= score_3 and score_3 >= score_1:
    print("1",name_2)
    print("2",name_3)
    print("3",name_2)

elif score_3 >= score_1 and score_1 >= score_2:
    print("1",name_3)
    print("2",name_1)
    print("3",name_2)
    
elif score_3 >= score_2 and score_2 >= score_1:
    print("1",name_3)
    print("2",name_2)
    print("3",name_1)