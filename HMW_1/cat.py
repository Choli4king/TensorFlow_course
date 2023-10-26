class Cat:
    def __init__(self, name):
        self.name = name

    def greet(self, other_cat):
        print(f"Hello, I am {self.name}! I see you are also a cool fluffy kitty {other_cat.name}, let's together purr at the human, so that they shall give us food")

"""
cat.py defines a Cat class with a constructor that takes a name parameter and assigns it to self.name. 
It also has a greet method which takes another Cat object as a parameter and prints a greeting message addressing the other cat by name.


kittyconcert.py imports the Cat class from cat.py. It then creates two Cat objects, cat1 and cat2, and has them greet each other.

"""
