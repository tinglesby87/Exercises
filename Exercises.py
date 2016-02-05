import random
answer_box=input("Please enter the number of questions you will answer ")
answer_box=int(answer_box)

difficulty_box = int(input("Please enter a difficulty_level = 1= Easy, 2 = Medium, 3 = Hard "))



def math_quiz(min_num, max_num):
    for _ in range(answer_box):
        x= random.randint(min_num, max_num)
        y= random.randint(min_num, max_num)
        product = x*y
        input_box= int(input("{} * {} = ".format(x, y)))
        if  input_box == product :
            print("That is correct")
        else:
            print("Oops! That's incorrect")

if difficulty_box == 1:
    math_quiz(1,5)

elif difficulty_box == 2:
    math_quiz(2,10)

else:
    math_quiz(5,25)




