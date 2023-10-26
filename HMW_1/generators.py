'''
This generator function is defined as meow_generator(). 
It uses a while loop to keep generating meows indefinitely.
Within the loop, it uses the yield keyword to return a string 
that consists of the specified number of meows. 
The number of meows starts at 1 and doubles on each consecutive call.
'''
def meow_generator():
    meow_count = 1
    while True:
        yield " ".join(["Meow "] * meow_count) # string operation to join elements(yield makes it a generator)
        meow_count *= 2


meows = meow_generator()

for _ in range(4):
    print(next(meows))


# using list comprehension in combination with generator
# Using list comprehension to generate a list of meow strings
# meows = [next(meow_generator()) for _ in range(4)]


# Printing the meow strings
# for meow in meows:
#     print(meow)