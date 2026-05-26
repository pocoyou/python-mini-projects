print("welcome to this quiz :)")

playing = input("play? ")

if playing != "yes":
    quit()

print("okay great, let's start :D")
score = 0

answer = input("whats my name ")
if answer.lower() == "pocoyou":
    print ("yahoo!")
    score += 1
else:
    print ("no......")

answer = input("whats my fav color ")
if answer.lower() == "blue":
    print ("yahoo!")
    score += 1
else:
    print ("no......")

answer = input("what is the 2nd element on the periodic table ")
if answer.lower() == "helium":
    print ("yahoo!")
    score += 1
else:
    print ("no......")

answer = input("what is the date ")
if answer.lower() == "may 26 2026":
    print ("yahoo!")
    score += 1
else:
    print ("no......")

answer = input("anyth else ")
if answer.lower() == "no":
    print ("yahoo!")
    score += 1
else:
    print ("no......")


print("you got " + str(score) + " questions correct!!")
print ("you got " + str((score / 5) * 100) + " %")
