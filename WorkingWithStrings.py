print('single quote') #single quotes
print('doesn\'t') # use \' for escape single quotes in the word
print("doesn't") # or use double quotes
print('"Yes," they said.')
print("\"Yes,\" they said.") # use \" for escaping double quote while working with double quotes
print('"Isn\'t," they said.')

s = 'First line.\nSecond line.'  # \n means newline
print(s)

print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote, use raw strings by adding an r before the first quote

# use triple quotes for multiline statements  """..."""
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

#String concatenation
print('hell' + 3 * 'o') # 3 *'o' will print the o, 3 times. Op : hellooo

print('py''thon') #Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.

text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)

#String index
word = 'Python'
print(word[3]) #will print the letter h as the letter in index 3 is h

#Indices may also be negative numbers, to start counting from the right:
#Note that since -0 is the same as 0, negative indices start from -1.
print(word[-1])  # last character
print(word[-2])  # second-last character

#Slicing
print(word[0:2]) # characters from index 0 (included) to 2(excluded) e.g. Py
print(word[:2])   # character from the beginning to position 2 (excluded). 
#an omitted first index defaults to zero
print(word[4:]) #characters from position 4 (included) to the end
#an omitted second index defaults to the size of the string being sliced
print(word[:2] + word[2:])
#Note how the start is always included, and the end always excluded. 
#This makes sure that s[:i] + s[i:] is always equal to s:

#Finding Length of the string - use len() method
s = 'supercalifragilisticexpialidocious'
print(len(s))
