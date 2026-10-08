questions = ("lightest in periodic table","highest electronegativity","highest electron affirnity","highest ionization energy")
options = (("h","na","k","ca"),("cl","o","f","k"),("cl","c","b","mg"),("na","fr","cs","h"))
answers = ("A","C","A","D")
guess = []
total_points = 0
#printing the questions
for question in range(4):
    print("---------------")
    print(questions[question])
    for option in range(4):

        print(options[question][option])
#taking the answer

    r =input("enter the answer in (A,B,C,D)").upper()
    guess.append(r)


    if guess[question] == answers[question]:
        total_points +=1
    else:
        print("Incurrect")
        print(f"the currect answer is {answers[question]}")

print(f"the total point is {total_points}")




