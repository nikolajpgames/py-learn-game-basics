# Session 5 - Your Own Words

# "def" invents a new word. Nothing happens until you use it.
def say_hello(name):
    print("Hello,", name)
    print("Nice to meet you.")


# Some functions hand an answer back with "return".
def double(number):
    answer = number * 2
    return answer


say_hello("Sam")
print()
say_hello("Alex")

print()
print("Double 7 is", double(7))
print("Double 50 is", double(50))


# ---- the surprising bit --------------------------------------------
# A function gets its OWN copy of things. Changing the copy inside
# does not change the original outside.

score = 10


def try_to_change(score):
    score = 999
    print("  inside the function, score is", score)


print()
print("before:", score)
try_to_change(score)
print("after: ", score, "  <- unchanged!")
