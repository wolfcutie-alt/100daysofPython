'''
Issue
We've got some buggy code. Try running the code. The code will crash and give you an IndexError. This is because we're looking through the list of fruits for an index that is out of range.
'''

fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")


make_pie(4)