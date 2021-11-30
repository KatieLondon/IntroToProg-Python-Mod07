# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Script to demonstrate pickling and error handling,
#
# ChangeLog (Who,When,What):
# Katie London,11.28.2021, created script to complete assignment 7
# ---------------------------------------------------------------------------- #

#----------------PICKLING------------------------------------------------------#

import pickle #loads the pickle module

# Dump demo
lstVegetables = ['carrot', 'celery', 'broccoli', 'cabbage', 'kale']
objFile = open('Vegetables.abc', 'ab')
pickled_vegetables = pickle.dump(lstVegetables, objFile)
objFile.close()

# Load demo
lstPickled = open('Vegetables.abc', 'rb')
unpickled_vegetables = pickle.load(lstPickled)
objFile.close()
print(unpickled_vegetables)


#------------------Structured Error Handling---------------------------------#

class Not_Vegetable_Error(Exception):
    '''Custom error - exception occurs when list item is not a vegetable '''
    def __str__(self):
        return '    There is an item in the list that is not a vegetable'

# Data ---------------------------------------------------------------------- #
lstVegetables = ['carrot', 'celery', 'kale', 'broccoli', 'tomato']

intDemo_Choice= int(input('''Please choose a demo from the list below:
 6 demo options:
   1. basic_try-except
   2. multiple_except_IndexError
   3. multiple_except_TypeError
   4. except_finally_demo
   5. raise_exception_demo
   6. raise_custom_exception_demo ''' + ' \n' + ' number choice: '))

# BASIC TRY-EXCEPT BLOCK - DEMO 1
if intDemo_Choice == 1:
    print("List of Vegetables: ", *lstVegetables)
    intVeg = int(
        input('Please choose an index for the vegetable from the list you want to display (choose 6 for demo) : '))
    try:
        print(lstVegetables[intVeg])
    except Exception as e:
        # Custom Error Message
        print('There is not a ' + str(intVeg) + 'th vegetable in the list, choose a number less than ' + str(len(lstVegetables)))
        print(e) #Print the error object
        print(type(e)) #Print the type of error object
        print(e.__doc__) #Print the error object's docstring

# EXAMPLE WITH MULTIPLE EXCEPT BLOCKS - DEMO 2
if intDemo_Choice == 2:
    print("List of Vegetables: ", *lstVegetables)
    intVeg = int(
        input('Please choose an index for the vegetable from the list you want to display (choose 6 for demo) : '))
    # set intVeg to an index outside of lstVegetables to cause a IndexError
    print(' EXAMPLE OF MULTIPLE EXCEPT BLOCKS')
    print('    To demonstrate the indexError exception the list index chosen is 6')
    print('    intVeg = ' + str(intVeg))
    try:
         print(lstVegetables[intVeg])
    except TypeError:
         print('Unable to convert index entered into an integer. You must enter a number')
    except IndexError:
         print('There is not a ' + str(intVeg) + 'th vegetable in the list, choose a number less than ' + str(len(lstVegetables)))

# EXAMPLE WITH MULTIPLE EXCEPT BLOCKS - DEMO 3
if intDemo_Choice == 3:
    print("List of Vegetables: ", *lstVegetables)
    intVeg = input('Please choose an index for the vegetable from the list you want to display (choose 4 for demo) : ')
    #intVeg is left as a string to cause a TypeError because list indices must be integers
    print(' EXAMPLE OF MULTIPLE EXCEPT BLOCKS')
    print('    To demonstrate the TypeError exception the index is set to a string instead of an integer')
    print('    intVeg data type: ' + str(type(intVeg)))
    try:
         print(lstVegetables[intVeg])
    except TypeError:
         print('    Unable to convert index into an integer. You must enter a number \n')
    except IndexError:
         print('    There is not a ' + str(intVeg) + 'th fruit in the list, choose a number less than ' + str(len(lstVegetables)))


# EXAMPLE WITH TRY EXCEPT FINALLY BLOCKS
if intDemo_Choice == 4:
    print("List of Vegetables: ", *lstVegetables)
    print(' EXAMPLE OF GENERIC EXCEPT BLOCKS AND FINALLY KEYWORD')
    print('     To demonstrate the generic except block, there is a TypeError but no TypeError except block so the generic except block is executed instead ')
    try:
        intVeg = input('Please choose an index for the vegetable from the list you want to display: ') #Leave off conversion to integer to cause a TypeError error
        print(lstVegetables[intVeg])
    except ValueError:
        print('ValueError')
    except IndexError:
        print('There is not a ' + str(intVeg) + 'th vegetable in the list, choose a number less than ' + str(len(lstVegetables)))
    except:
        print('Error, unable to display requested vegetable')
    finally:
        print('End of the try except block') # This can be helpful to provide the user with a status update

# EXAMPLE WITH TRY EXCEPT RAISE KEYWORD
if intDemo_Choice == 5:
    print("List of Vegetables: ", *lstVegetables)
    intVeg = int(input('Please choose an index for the vegetable from the list you want to display (choose 5 for demo) : '))
    print(' EXAMPLE OF RAISING AN EXCEPTION')
    print('    To demonstrate raising an indexError exception the index is set to 5')
    try:
        if (intVeg >= 5 or intVeg < 0):
            raise IndexError
        elif type(intVeg) != int:
            raise TypeError
    except IndexError as e:
        print('    Index is out of bounds.  Index needs to be between 0 and 4 inclusive')
        print(e, e.__doc__)

# EXAMPLE WITH RAISING CUSTOM ERROR CLASSES
if intDemo_Choice == 6:
    print("List of Vegetables: ", *lstVegetables)
    intVeg = int(
        input('Please choose an index for the vegetable from the list you want to display (choose 4 for demo) : '))
    # set intVeg  = 4 for tomato
    print(' EXAMPLE OF RAISING A CUSTOM CLASS EXCEPTION')
    print('    To demonstrate raising a custom exception the index is set to 4 for tomato')
    try:
        if (intVeg > 5 & intVeg < 0):
            raise IndexError
        elif type(intVeg) != int:
            raise TypeError
        elif lstVegetables[intVeg] == 'tomato':
            raise Not_Vegetable_Error()
    except Exception as e:
        print(e)
