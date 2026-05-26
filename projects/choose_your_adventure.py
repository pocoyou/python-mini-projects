name = input("type your name in: ")
print("welcome", name, "to this journey! this is your adventure")

answer = input("you start on a dirt road; it comes to an end, and you can choose to go left or right. ")

if answer == "left":
    answer = input("you arrive at a river. do you want to walk around it or swim across? type walk or swim. ")
    if answer == "swim":
        print("you swam across and got eaten by an alligator. ")
    elif answer == "walk": 
        print("you walked for many miles, thirsty and without water. you have lost the game. ")
    else:
        print("not a valid option. you lose.")

elif answer == "right":
    answer = input("you arrive before a bridge; it looks wobbly and old. do you want to cross it or turn back? (cross/back) ")
    if answer == "back":
        print("you go back to the main road and end up tripping over yourself. you lose.")
    elif answer == "cross":
        answer = input("you cross the bridge and meet a stranger in a cloak. do you talk to them? (yes/no) ")
        if answer == "yes":
            print("you talk to the stranger and they give you gold. YOU WIN!")
        if answer =="no":
            print("you ignore the stranger. when you turn your back, you are stabbed. you lose.")
    else:
            print("not a valid option. you lose.")

else:
    print("not a valid option. you lose.")

print("thank you for trying on your journey", name)
