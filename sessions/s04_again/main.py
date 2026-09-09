# Session 4 - Doing It Again

print("A for loop, for when you know how many times:")

for i in range(5):
    print("  i is", i)

print("Finished. Notice it started at 0, not 1.")


print()
print("A while loop, for when you don't:")

countdown = 3

while countdown > 0:
    print("  ", countdown)
    countdown = countdown - 1

print("  Lift off!")
