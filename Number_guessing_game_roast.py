import random

print(r"""
                           /\_/\   
                          ( o.o ) 
                           > ^ < 
""")
print("----------------- Number Guessing Game -----------------\n")
print("You are now playing the Number Guessing Game!")
print("Try to think of a number between 1 and 100.")
print("If feeling stuck, you can type 'hint' to get riddle.")
print("Decode the riddle to get the hint.")
print("You will get a total of 5 hints and 7 lives so enjoy.\n")

secret = random.randint(1, 100)
attempts = 0
max_attempts = 7
hint_used = 0

roasts_low = [
    "Way too low, bro… smaller than your attention span",
    "That's lower than your phone battery at 1%",
    "My little cousin guesses higher than that",
    "Arctic level cold 🥶 Penguins are laughing",
    "Even the number 1 is disappointed in you"
]

roasts_high = [
    "Too high… calm down Superman",
    "Your ego is already in space",
    "Bigger than your dreams and your debt",
    "NASA wants to talk to you about that guess",
    "Wrong galaxy, my guy"
]

roasts_close = [
    "So close… and still so wrong. Painful.",
    "One away. ONE. Embarrassing.",
    "You can literally smell it and missed",
    "Classic skill issue right there"
]

while max_attempts > attempts :
    
    answer = input("Guess : ")
    
    if answer.lower() == "hint":

        if hint_used >= 5:
            print("You have already used all your hints, dead-brain.")

        else:
            hint_used += 1

            if hint_used == 1:
                if secret > 50:
                    print("Hint : I live in the upper half of the number world.")
                else:
                    print("Hint : I stay in the lower half of the number world.")
                    
            elif hint_used == 2:
                if secret % 2 == 0:
                    print("Hint : I can be split into two equal whole numbers.")
                else:
                    print("Hint : Divide me by two and you won't get a whole number.")

            elif hint_used == 3:
                if secret % 5 == 0:
                     print("Hint : My last digit is 0 or 5.")
                else:
                    print("Hint : My last digit is NOT 0 or 5.")

            elif hint_used == 4:
                temp = secret
                is_prime = True

                if temp == 1:
                    is_prime = False

                else:
                    for i in range (2,int(temp**0.5) + 1):
                        if temp % i == 0:
                            is_prime = False
                            break

                if is_prime:
                    print("I have exactly two divisors — no more, no less.")
                else:
                    print("I share myself with numbers other than 1 and me.")
                    

            elif hint_used == 5:
                temp = secret
                add = 0
                while temp > 0:
                    add += temp % 10
                    temp //= 10

                print(f'Hint : My digits add upto {add}')

            print("Hints left :", 5 - hint_used)
            print("Attempts left :", max_attempts - attempts)
            print()
            
        continue

    
    if not answer.isdigit():
        print("Dumb person, we are playing number guessing game you need to type a number or 'hint'\n")
        continue

    guess = int(answer)

    if guess < 1 or guess > 100:
        print("I asked you to guess between 1 and 100, don't use your brain beyond it's potential....\n")
        continue

    diff = secret - guess

    attempts += 1

    if diff < -10:
        print(random.choice(roasts_high))

    elif diff > 10:
        print(random.choice(roasts_low))

    elif diff != 0 and -10 <= diff <= 10:
        print(random.choice(roasts_close))

    else:
        print("\nYayyyyyyy!")
        print("The number was", secret)
        print(f"You took {attempts} guesses ")

        if hint_used > 0:
            print(f'You used {hint_used} lifeline to win, tch tch.')

        print(r"""
                              /\_/\  
                             ( ^_^ )  
                              > 🎊 <
                         KABOOM KABLOW !!
        """)

        break

    print("Hints left :", 5 - hint_used)
    print("Attempts left :", max_attempts - attempts)
    print()

else:
    print("Oh no.. no attempts left!")
    print("The number was", secret)
    print(r"""
                              /\_/\  
                             ( T_T )  
                              > 💔 <      
                        I am disappointed...
    """)

print("And, game over!")
input("Press Enter to close")
