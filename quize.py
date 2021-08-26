print("Hey there!!\nWelcome to the Quize Game.")
response = input("Are you intrested to play this Quize Game? ")
if response.lower() != "yes":
    print("Hope you join us again. Goodbye!")
    quit()
print("So,Let's Play")
score = 0

quize = input("What is so delicate that even mentioning it breaks it? ")
if quize.lower() == "silence":
    print("\tCorrect:)")
    score += 1
else:
    print("\tOops,you went wrong:(\n\tThe right answer is silence.")


quize = input("What has hands but can not clap? ")
if quize.lower() == "clock":
    print("\tCorrect:)")
    score += 1
else:
    print("\tOops,you went wrong:(\n\tThe right answer is clock.")

quize = input("What is full of holes but still holds water? ")
if quize.lower() == "sponge":
    print("\tCorrect:)")
    score += 1
else:
    print("\tOops,you went wrong:(\n\tThe right answer is sponge.")

quize = input("What files when it's born, lies when it's alive and runs when it's dead? ")
if quize.lower() == "snowflake":
    print("\tCorrect:)")
    score += 1
else:
    print("\tOops,you went wrong:(\n\tThe right answer is snowflake.")

quize = input("I shoot but never kill.What am I? ")
if quize.lower() == "camera":
    print("\tCorrect:)")
    score += 1
else:
    print("\tOops,you went wrong:(\n\tThe right answer is camera.")

quize = input("I am bigger then elephant but lighter than feather.What am I? ")
if quize.lower() == "wind":
    print("\tCorrect:)")
    score += 1
else:
    print("\tOops,you went wrong:(\n\tThe right answer is wind.")

quize = input("What is long, pink and wet and is rude to pull out in front of people? ")
if quize.lower() == "tongue":
    print("\tCorrect:)")
    score += 1
else:
    print("\tOops,you went wrong:(\n\tThe right answer is tongue.")

quize = input("I love to twist and dance.Though wingless, I fly high uo into the sky.What am I ")
if quize.lower() == "kite":
    print("Correct:)")
    score += 1
else:
    print("\tOops,you went wrong:(\n\tThe right answer is kite.")

quize = input("What is higher without the head than with it? ")
if quize.lower() == "pillow":
    print("\tCorrect:)")
    score += 1
else:
    print("\tOops,you went wrong:(\n\tThe right answer is pillow.")

quize = input("I can walk, but can't run.\nI can drink, but can;t eat.What am I? ")
if quize.lower() == "ink pen":
    print("\tCorrect:)")
    score += 1
else:
    print("\tOops,you went wrong:(\n\tThe right answer is ink pen.")

print("You got",score,"answers right.")