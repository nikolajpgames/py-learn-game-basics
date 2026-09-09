# Session 2 - Boxes With Names

# A variable is a name with something kept inside it.
name = "Player One"
score = 0
lives = 3

print("Name: ", name)
print("Score:", score)
print("Lives:", lives)


# Whatever is in the box can be swapped for something else.
score = score + 100
lives = lives - 1

print()
print("...something happens...")
print()

print("Score:", score)
print("Lives:", lives)


# An f-string lets you drop variables into the middle of a sentence.
print()
print(f"{name} has {score} points and {lives} lives left.")
