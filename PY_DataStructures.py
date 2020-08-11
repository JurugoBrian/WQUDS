
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('logstop', '')
get_ipython().run_line_magic('logstart', '-rtq ~/.logs/PY_DataStructures.py append')
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144


# In[ ]:


import expectexception


# # Python data types and structures
# 
# <!-- requirement: images/list_illustration.png -->
# <!-- requirement: images/hash_illustration.png -->
# <!-- requirement: images/set_operations.png -->
# 
# In the [Program Flow notebook](PY_ProgramFlow.ipynb), we introduced the idea of variables, which we could use to store several different kinds of information. We could store text, numbers, or truth values. These different kinds of information correspond with different Python data `type`s.

# In[2]:


print(type('some text'))
print(type(10))
print(type(10.3))
print(type(True))


# We also briefly introduced the Python `list`, which can be used to store a collection of data.

# In[6]:


# an example list
beans_recipe = ['Soak beans in water', 'Dissolve salt in water', 'Heat water and beans to boil', 
                'Drain beans when done cooking']


# Sometimes we will store information in individual variables, but often we will be working with several pieces of information that we want to group together because of their relationship or similarity. For example, if we were shopping for groceries, we could store each item we are going to buy in separate variables or we could store all of the items in one list.

# In[7]:


grocery_a = 'chicken'
grocery_b = 'onions'
grocery_c = 'rice'
grocery_d = 'peppers'
grocery_e = 'bananas'

grocery_list = ['chicken', 'onions', 'rice', 'peppers', 'bananas']


# Which of these approaches seems more useful to you? Let's write a short example function that "buys" each of the groceries we need.

# In[4]:


def buy_groceries_individual(item_a, item_b, item_c, item_d, item_e):
    print('Buying %s...' % item_a)
    print('Buying %s...' % item_b)
    print('Buying %s...' % item_c)
    print('Buying %s...' % item_d)
    print('Buying %s...' % item_e)

def buy_grocery_list(items):
    for item in items:
        print('Buying %s...' % item)


# In[8]:


buy_groceries_individual(grocery_a, grocery_b, grocery_c, grocery_d, grocery_e)


# In[9]:


buy_grocery_list(grocery_list)


# By using a `list`, we could use a `for` loop to write a much shorter function. But even more important, `buy_grocery_list` is much more flexible. What if instead of buying five items, we wanted to buy more or less?

# In[10]:


get_ipython().run_cell_magic('expect_exception', 'TypeError', "\n# let's try to buy just three items\nbuy_groceries_individual(grocery_a, grocery_b, grocery_c)")


# In[11]:


get_ipython().run_cell_magic('expect_exception', 'TypeError', "\n# let's try to buy a sixth item\n\ngrocery_f = 'squash'\n\nbuy_groceries_individual(grocery_a, grocery_b, grocery_c, grocery_d, grocery_e, grocery_f)")


# We encounter an error when we try to use `buy_groceries_individual` because it is expecting "exactly 5 arguments." We don't run into that problem with `buy_grocery_list`, because our `for` loop can work with lists of any length.

# In[12]:


short_grocery_list = ['chicken', 'onions', 'rice']

buy_grocery_list(short_grocery_list)


# In[13]:


long_grocery_list = ['chicken', 'onions', 'rice', 'peppers', 'bananas', 'squash']

buy_grocery_list(long_grocery_list)


# We see we successfully dealt with both a shorter and a longer list.  
# 
# Collections (or [**containers**](https://stackoverflow.com/questions/11575925/what-exactly-are-containers-in-python-and-what-are-all-the-python-container) as they're known in Python) can be very useful for tackling complex data problems. Python provides several types of containers, which we will explore. Each one has different properties and structure that make them useful for specific tasks. Later in the course, we'll also introduce powerful, highly-structured containers that Python users have invented and shared with the Python community.
# 
# In the context of data science, we'll often call a collection of data that logically belongs together a **data set**, and the type of variable we use to store it in Python a **data structure**. These terms are meant to emphasize the relationships between the individual pieces of information that creates their meaning as a whole.
# 
# ### Exercises
# 
# 1. What kind of data can naturally be represented by a `list`?  How about a `list` comprised of `list` objects?

# ## `list`
# 
# We've created lists by using square brackets `[]` around the data we want the list to contain. We can also create lists out of variables, rather than writing in the data directly.

# In[2]:


grocery_a = 'chicken'
grocery_b = 'onions'
grocery_c = 'rice'
grocery_d = 'peppers'
grocery_e = 'bananas'

grocery_list = ['chicken', 'onions', 'rice', 'peppers', 'bananas']
print(grocery_list)

variable_list = [grocery_a, grocery_b, grocery_c, grocery_d, grocery_e]
print(variable_list)


# So far we've worked with `list`s of strings (and `range`), but we're not limited to only that data type.

# In[3]:


int_list = [2, 6, 3049, 18, 37]
float_list = [3.7, 8.2, 178.245, 63.1]
mixed_list = [26, False, 'some words', 1.264]

print(int_list)
print(float_list)
print(mixed_list)


# We can store any `type` of data in a `list`. We can even put a `list` inside of a `list`.

# In[4]:


list_of_lists = [['a', 'list', 'of', 'words'], [1, 5, 209], [True, True, False]]
print(list_of_lists)


# There are very few restrictions on how we structure a list or what we put in it. This can lead to a very complicated nested structure.

# In[6]:


confusing_list = [[23, 73, 50], 'some words', 12.308, [[False, True], 'more words']]
print(confusing_list)


# We describe the Python `list` as _heterogeneous_ because it can hold a collection of mixed objects. This is one of the major defining properties of the Python `list`.
# 
# You may have also noticed that when we put data into a `list` in particular order, it stays in that order when we `print` or use the `list` in a `for` loop. Because `list` preserves order, we say it is _ordered_. We can use this property to retrieve particular items from a `list` based on their position (or **index**) in the list.

# In[5]:


print(grocery_list)
print(grocery_list[2])


# Printing `grocery_list[2]` returned the third item in the list: 'rice'. Why did it return the third item if we asked for the item at index 2? Python `list`s are _zero-indexed_.

# In[11]:


print(grocery_list[0])
print(grocery_list[1])
print(grocery_list[2])


# We can also retrieve a _slice_ of items from a list.

# In[7]:


print(grocery_list[1:4])
print(grocery_list[3:])
print(grocery_list[:3])
print(grocery_list)


# Python also has a negative indexing syntax, allowing us to access the list from the end instead of the beginning. The last element is indexed by -1.

# In[8]:


print(grocery_list[-1])
print(grocery_list[-3:])


# We can also slice a list using a step-size other than 1. For instance, we can slice every other item of the list, or even reverse the list by making negative steps.

# In[14]:


print(grocery_list[::2])
print(grocery_list[4:1:-1])


# We can of course also retrieve information from a list by using a `for` loop.

# In[16]:


for item in grocery_list:
    print(item)


# While we'll usually use the syntax `for item in list`, sometimes we will combine a `for` loop with indexing. The `range` function (which we used in the last notebook) is useful for this. For example, we can pick out every other item in the list.

# In[9]:


for i in range(0, len(grocery_list), 2):
    print(i, grocery_list[i])


# The `range` function returns a sequence of integers between the first and second argument, using the third argument as the step size. Notice that the upper bound (i.e. second argument) is not included in the output.

# In[10]:


print(range(0, 10, 3))
print(range(104, 100, -1))
print(range(5)) # starts at 0 and counts by 1 by default


# We can also use indexing/slicing to replace items in the list.

# In[11]:


grocery_list = ['chicken', 'onions', 'rice', 'peppers', 'bananas']
print(grocery_list)
grocery_list[-1] = 'oranges' # replace bananas with oranges
print(grocery_list)
grocery_list[1:3] = ['carrots', 'couscous'] #replace onions and rice with carrots and couscous
print(grocery_list)


# Since we can modify lists after they are created, we call them _mutable_ (the modifications are called _mutations_). Some Python data types are _immutable_, meaning once they are created they cannot be changed. We'll explore this further as we introduce more data types.
# 
# Another way we can mutate a `list` is to `append` new items.

# In[12]:


grocery_list = ['chicken', 'onions', 'rice', 'peppers', 'bananas']
print(grocery_list)
grocery_list.append('squash')
print(grocery_list)
grocery_list.append(['bread', 'salt'])
print(grocery_list) # what happened?


# Since lists can contain lists, we have to be careful about adding multiple items to our list. Instead of `append`, we might want to use `extend`.

# In[13]:


grocery_list = ['chicken', 'onions', 'rice', 'peppers', 'bananas', 'squash']
print(grocery_list)
grocery_list.extend(['bread', 'salt'])
print(grocery_list)


# We can also remove items from a list.

# In[14]:


print(grocery_list)
del grocery_list[-1] # delete the last item
print(grocery_list)


# In[18]:


print(grocery_list)
print(grocery_list.pop(-1)) # remove the last item from the list and return it
print(grocery_list)


# Another mutation we can make to a list is to sort it.

# In[ ]:


grocery_list.sort()
print(grocery_list)


# The three major defining properties of the Python `list` are that it is ordered, heterogeneous, and mutable. Because it is heterogeneous and mutable, the `list` is very flexible. We need to be careful about the changes we make to a `list`, because they can be very unpredictable. We could break our code or lose data!

# ### Exercises
# 
# 1. Make a list of 10 elements and select only the last 2 elements
# 2. Take that same list of 10 elements and select every other element starting with the very first element.
# 3. Select every other element starting with the second element.

# ### Gotcha (Names)
# Variables and names are not the same thing in python.  For instance, run the following code

# In[ ]:


a = 4
b = a
print(a, b)
a = 5
print(a, b)


# Here we assigned the name `a` to the value 4 and then `b` to be equal to `a`.  But, `b` does not point to `a`, it points to the variable that has the name `a`.  Thus, assigning the name `b` to the value of `a` does not cause the value of `b` to change when the value of `a` changes.
# 
# Lets see another example, here we will make use of a Python `list`.  We will go over more about lists in the next lecture, for now, think of it as an ordered collection of Python variables (technically objects).  In this case, we will do exactly what we did before, but instead of modifying where `a` points, we will modify the object to which it points.  In this case, we will see that `b` does in fact change.  This is because they are both pointing to the same variable in memory!

# In[ ]:


a = [3, 2, 1]
b = a
print(a, b)
a[1] = 5
print(a, b)


# ### Exercises
# 
# 1. Explain the difference between a name and a variable.

# ## `tuple`
# 
# A Python `tuple` is very similar to a `list` with one major difference -- it is immutable. We create a `tuple` using parentheses `()`.

# In[ ]:


example_tuple = ('Dylan', 26, 167.6, True)
print(example_tuple)


# While we can retrieve data through indexing (because a `tuple` is ordered), we cannot modify it (because a `tuple` is immutable).

# In[ ]:


print(example_tuple[2])


# In[ ]:


get_ipython().run_cell_magic('expect_exception', 'TypeError', '\n\nexample_tuple[2] = 169.3')


# In[ ]:


get_ipython().run_cell_magic('expect_exception', 'TypeError', '\n# deletion also fails\ndel example_tuple[-1]')


# While for clarity we should enclose tuples with `()`, Python will assume we want a `tuple` if we don't use any symbols to enclose comma separated values.

# In[ ]:


another_example_tuple = 'Jill', 36, 162.3, True
print(another_example_tuple)
print(type(another_example_tuple))


# This implicit `tuple` comes up most often when working with functions that return multiple outputs. For example, we might have a function that returns the first and last letter of a string.

# In[ ]:


def first_last(s):
    return s[0], s[-1]

chars = first_last('hello!')
print(chars)


# In such cases, we'll sometimes want to store the multiple outputs in separate variables.

# In[ ]:


first_char, last_char = first_last('hello!')

print(first_char)
print(last_char)


# This syntax is called _unpacking_. We can use it with any `tuple`, whether it was returned by a function or not.

# In[ ]:


name, age, height, has_dog = example_tuple

print(name)
print(age)
print(height)
print(has_dog)


# Both the Python `list` and `tuple` are ordered and heterogeneous. However, unlike the `list`, the `tuple` is immutable, meaning it cannot be modified after it is created. Therefore, a `list` might be better for representing data that is expected to change over the course of a program, like a to-do list. A `tuple` might be better for representing data that is expected to be fixed, like the responses of an individual subject to a survey.
# 
# #### Gotcha
# 
# One common mistake people make with immutability and especially with tuples is to assume data structures inside the tuple are immutable because the tuple is immutable.  Lets see an example.

# In[ ]:


tup = tuple([[], 'a'])
print(tup)
tup[0].append(1)
print(tup)


# Even though the tuple itself is immutable, we cannot change the exact objects which it contains, those objects themselves can be mutated if they are mutable.  As with anywhere mutability shows up, this requires the programmer to be careful and not assume data has not been modified in some context.

# ## `set`
# 
# A Python `set` is also similar to a `list`, except it is unordered. It can store heterogeneous data and it is mutable, but what does it mean to be unordered? The simplest explanation is simply to look at an example. We can create a set by enclosing our data with curly brackets `{}`.

# In[ ]:


example_set = {'Dylan', 26, 167.6, True}
print(example_set)


# Even though we entered the data in one order, the `set` printed out in a different order. Even more significantly, we cannot index or slice a `set`.

# In[ ]:


get_ipython().run_cell_magic('expect_exception', 'TypeError', '\nprint(example_set[0])')


# However, we can still add and delete items from a set.

# In[ ]:


print(example_set)
print(example_set.pop())
print(example_set)


# In[ ]:


example_set.add('True')
print(example_set)
example_set.update([58.1, 'brown'])
print(example_set)


# The `add` method of a `set` works similarly to the `append` method of a `list`. The `update` method of a `set` works similarly to the `extend` method of a `list`.
# 
# _**Why is `set` useful?**_
# 
# It seems strange that we might want an _unordered_ data structure. We can't access or modify the data through indexing. How does giving up order benefit us? The answer is that it gives us flexibility about how the data is stored in memory, and that flexibility can make data retrieval much faster.
# 
# Imagine we have ten boxes and ten piles of money. We put the ten piles of money in the ten boxes. Now say we want to find the box that has \$5.37 in it. We don't know which box this is, so we start with the first box and check. If it isn't in the first box, we move on to the second box. We keep checking boxes until we find it. This might take awhile.
# 
# ![list_illustration](images/list_illustration.png)
# 
# Now imagine we have the same ten piles of money, but we have 31 boxes. Instead of putting each pile of money into the boxes in order, instead put each pile into a box based on the amount of money in the pile. First we multiply the amount of money by 100, and then take modulus division by 31. This gives the number of the box we should put the pile of money in.

# In[ ]:


piles = [2.83, 8.23, 9.38, 10.23, 25.58, 0.42, 5.37, 28.10, 32.14, 7.31]


# In[ ]:


def hash_function(x):
    return int(x*100 % 31)


# In[ ]:


[hash_function(pile) for pile in piles]


# Now say we want to find the box with \$5.37 in it. We don't have to search through box after box. We can compute:

# In[ ]:


print(int(5.37 * 100 % 31))


# ![hash_illustration](images/hash_illustration.png)
# 
# Box number 10 contains the \$5.37 pile.
# 
# This technique of assigning boxes (i.e. memory) based on the object it contains is called **hashing**. It makes searching for data very fast (as we've illustrated), but at the cost of increase memory allocation (we needed more boxes). It also means that we cannot assign an order to the objects as they are stored in memory.
# 
# Hashing also puts two major restrictions on the `set`. First of all, objects in a `set` must be immutable. If an object were to change, its position in memory would no longer correspond with its **hash**. Secondly, the objects in a `set` must be unique. Identical objects end up with the same hash. Since we can't store multiple objects in the same chunk of memory, we simply discard any duplicates.
# 
# This second restriction means we can use a `set` to easily determine the unique objects in a `list` or `tuple`.

# In[ ]:


print(set([23, 609, 348, 10, 5, 23, 340, 82]))
print(set(('a', 'b', 'q', 'c', 'c', 'd', 'r', 'a')))


# Because searching for data is very simple in a `set`, they are also very useful for making comparisons between collections of data.

# In[ ]:


student_a_courses = {'history', 'english', 'biology', 'theatre'}
student_b_courses = {'biology', 'english', 'mathematics', 'computer science'}

print(student_a_courses.intersection(student_b_courses))
print(student_a_courses.union(student_b_courses))
print(student_a_courses.difference(student_b_courses))
print(student_b_courses.difference(student_a_courses))
print(student_a_courses.symmetric_difference(student_b_courses))


# ![set_operations](images/set_operations.png)
# 
# ### Exercises
# 
# 1. When should I use a `set` instead of a `list`?
# 2. What is an example of a problem where a `set` might be part of the solution?

# # dict
# 
# To understand the Python `dict`, let's start again with the Python `list`.

# In[ ]:


me = ['Dylan', 28, 167.5, 56.5, 'brown', 'brown', True]


# This `list` describes me: my name, my age, my height (in centimeters), my weight (in kilograms), my hair color, my eye color, and whether or not I have a dog. We know we can access this information individually by index.

# In[ ]:


print('My name is %s' % me[0])
print('I have %s hair' % me[4])


# It would be easy to get mixed up about which data is which (for example, which `'brown'` is hair color and which is eye color?), or where I should find it (will age always be at index 1?).
# 
# A better solution would be a data structure where we could index using meaningful values. For example instead of using `me[0]` to recover `Dylan`, I could use `me['name']`. Instead of hair color being `me[4]`, it could be `me['hair']`. This feature is the central characteristic of the Python `dict`.

# In[ ]:


me_dict = {'name': 'Dylan', 'age': 28, 'height': 167.5, 'weight': 56.5, 'hair': 'brown', 'eyes': 'brown', 'has dog': True}

print('My name is %s' % me_dict['name'])
print('I have %s hair' % me_dict['hair'])


# Instead of calling `'name'` and '`hair'` the index, we call them **keys**. Each key is associated with a **value** in a **key-value pair**. We can see the key-value pairs in the `{}` syntax used for creating a `dict`. Each key-value pair is separated by a comma, and within a pair the key and value are separated by a colon `:`.
# 
# ### Exercises
# 1. When might a `dict` be more useful than a `list`?
# 2. Compare the flexibility of a `dict` which contains other `dict` object to that of a multi dimensional array.

# ### `zip`
# 
# The `zip` function can be very handy for creating a `dict`. Let's go back to the `list` we made before that contained all the values describing me. We'll make a second `list` containing all the keys we would want for putting these values in a dictionary

# In[ ]:


value_list = me
key_list = ['name', 'age', 'height', 'weight', 'hair', 'eyes', 'has dog']

print(value_list)
print(key_list)


# Currently we have two lists: one of values and one of keys. They have no relationship to each other within Python, but we can see that they belong together logically. How do we combine them in Python? By using the `zip` function.

# In[ ]:


key_value_pairs = list(zip(key_list, value_list))
print(key_value_pairs)


# We now have a list of tuples. We interpret the first element of each tuple as a key, and the second element as a value. We can turn this list of tuples directly into a `dict`.

# In[ ]:


me_dict = dict(key_value_pairs)
print(me_dict)


# You may have noticed that even though our list of tuples began with `('name', 'Dylan')`, when we printed `me_dict` it started with `'eyes': 'brown'`. If you guessed this means that a `dict` is unordered, you are correct! The keys are hashed to assign key-value pairs to memory. Therefore, keys must be immutable and unique, similar to the elements of a `set`. However, values don't have these restrictions.

# In[ ]:


get_ipython().run_cell_magic('expect_exception', 'TypeError', "\n# this doesn't work\ninvalid_dict = {[1, 5]: 'a', 5: 23}")


# In[ ]:


# but this does
valid_dict = {(1, 5): 'a', 5: [23, 6]}
print(valid_dict)


# The `dict` is also mutable. We can add new key-value pairs by simple assignment.

# In[ ]:


print(me_dict)
me_dict['favorite book'] =  'The Little Prince'
print(me_dict)


# We can also use `update`, similar to the way we used it for a `set`, except now with key-value pairs.

# In[ ]:


print(me_dict)
me_dict.update({'favorite color': 'orange', 'siblings': 3, 'nieces/nephews': 3})
print(me_dict)


# We can replace or delete key-value pairs from the `dict`.

# In[ ]:


print(me_dict)
me_dict['nieces/nephews'] = 4
print(me_dict)


# In[ ]:


del me_dict['favorite book']
print(me_dict)


# In[ ]:


print(me_dict.pop('siblings'))
print(me_dict)


# Because the `dict` uses hashing, searching it is very fast (as with `set`). Sometimes dictionaries are referred to as **lookup tables** or **hash tables**. It is incredibly useful for referencing data through meaningful keys. While the data in a `dict` is unordered, it remains organized by the keys. We can retrieve a list of the keys and values directly, or as key-value pairs, using the appropriate methods of `dict`.

# In[ ]:


print(me_dict.keys())
print(me_dict.values())
print(me_dict.items())


# ## Switching data structures
# Each of the containers we've introduced has different properties and characteristics. Sometimes we will want to change one data structure into another to take advantage of these differences. We've already seen some methods for transforming a `dict` into a `list` of `tuple`s or vice versa. We can easily transform between `list`, `tuple`, and `set`.

# In[ ]:


example_list = ['a', 'b', 23, 10, True, 'a', 10]
example_tuple = tuple(example_list)
example_set = set(example_tuple)
example_list = list(example_set)

print(example_tuple)
print(example_set)
print(example_list) # note we lost the duplicates because of set


# ## Search
# 
# We discussed the idea of searching for data in our data structures when describing what makes `set` (and `dict`) so special. What does search look like in Python? We search for data using the keyword `in`.

# In[ ]:


print(example_list)
print('a' in example_list)
print('c' in example_list)


# When dealing with a `dict`, we can search keys, but not values.

# In[ ]:


print(me_dict)
print('hair' in me_dict)
print('has cat' in me_dict)
print('brown' in me_dict)


# Searching for keys is important in dictionaries so that we don't accidentally try to retrieve a key-value pair that doesn't exist.

# In[ ]:


get_ipython().run_cell_magic('expect_exception', 'KeyError', "\nprint(me_dict['has cat'])")


# In[ ]:


if 'has dog' in me_dict:
    print('Has dog: %s' % me_dict['has dog'])
else:
    print(None)

if 'has cat' in me_dict:
    print('Has cat: %s' % me_dict['has cat'])
else:
    print(None)


# In[ ]:


# can use get method for same results

print('Has dog: %s' % me_dict.get('has dog'))
print('Has cat: %s' % me_dict.get('has cat'))


# We can imagine a lot of situations where search is useful. Is a country in the set of places that are going to be affected by a drought? Is a task in my to-do list? Is this username already taken, and if so what is the matching password (a `dict` would be useful here)?

# ## Sorting
# 
# Since a `tuple` is immutable, can we sort it? Or is that a mutation? What would it mean to sort a `set` or a `dict`, which has no order?
# 
# Out of the data structures we've studied so far, only `list` has a `sort` method. However, Python also has a `sorted` function, which will create a sorted `list` out of other data structures. By default `sorted` applied to a `dict` makes a `list` of sorted keys. We must use the `items` method if we want our output to be key-value pairs.

# In[ ]:


print(sorted(map(str, example_tuple)))
print(sorted(map(str, example_set)))
print(sorted(me_dict.items()))
print(sorted(me_dict))


# ## Iteration
# 
# As we've seen in some examples already, it will often be useful to iterate through a data structure, whether to execute some task based on the information contained or to transform or analyze a data set. We will most often use `for` loops to iterate over data structures. With a `list`, `tuple`, or `set` the elements of the container are returned one after another. With a `dict` things are a little more complicated: do we want to iterate over keys, values, or key-value pairs?

# In[ ]:


# by default we iterate over keys of a dict
for k in me_dict:
    print(k)


# In[ ]:


# to iterate over values...
for v in me_dict.values():
    print(v)


# In[ ]:


# or to iterate over key-value pairs...
for k, v in me_dict.items():
    print('%s: %s' % (k, v))


# Notice we used `tuple` unpacking in the `for` loop in the last example!
# 
# ### Comprehensions
# 
# Python has a special syntax called _comprehension_ for combining iteration with the creation of a data structure. It is essentially a `for` loop wrapped in the appropriate brackets for creating the data structure.

# In[ ]:


squares = [x**2 for x in range(10)]
square_lut = {x: x**2 for x in range(10)}

print(squares)
print(square_lut)


# Comprehensions are very useful for doing simple transformations on data structures. For example, maybe we are writing a function that will analyze `me_dict`. It might be useful to have a `dict` of the data types of the values in `me_dict` so that we know what to expect as input.

# In[ ]:


me_dict_dtypes = {k: type(v) for k, v in me_dict.items()}
print(me_dict_dtypes)


# Comprehensions also make code more readable. Compare the `for` loop implementation of `square_lut` with the comprehension.

# In[ ]:


square_lut = {}
for x in range(10):
    square_lut[x] = x**2

print(square_lut)

square_lut = {x: x**2 for x in range(10)}

print(square_lut)


# ## Collections
# As previously mentioned, the Python standard library has a `collections` module which contains a variety of extremely useful containers, especially for implementing algorithms as they tend to be quite optimized.  They are slightly more specialized than the general Python containers.
# 
# The containers are:
# 
# - `namedtuple`
# - `deque`
# - `Counter`
# - `OrderedDict`
# - `defaultdict`
# 
# 
# ### `namedtuple`
# 
# The `namedtuple` generates a class which is similar to a tuple, but has named entries.  Lets make one for a three dimensional vector which has fields `x,y,z`.  If we use the `verbose` flag we can see the generated Python code.

# In[ ]:


from collections import namedtuple
Vector3 = namedtuple('Vector', ['x', 'y', 'z'])


# Now we can access the elements of the elements of tuple by name.

# In[ ]:


vec = Vector3(1,2,3)
vec.x, vec.y, vec.z


# At this point you might be wondering why we can't just use a dictionary (or some other object).  One good reason is immutability

# In[ ]:


get_ipython().run_cell_magic('expect_exception', 'AttributeError', '\nvec.x = 5')


# Another good reason is that it will behave like a tuple when passed into a function.

# In[ ]:


def tfunc(a,b,c):
    print(a,b,c)
tfunc(*vec)


# `namedtuple` are a great way to create self documenting code with almost no memory cost.
# 
# ### `deque`
# A `deque` is a like a queue or a stack except it works both ways.  We can think of a `deque` as a list where we generally care about working with the ends of the list.  The `deque` is optimized for $O(1)$ performance for both adding and removing elements from the ends of the structure, whereas a general `list` will be $O(N)$ for operations at the front of the list.
# 
# Lets see an example

# In[ ]:


from collections import deque

d = deque([2,3,4,5])
print(d)
d.append(10)
print(d)
d.appendleft(20)
print(d)


# Lets time how long it takes to perform the same operation adding elements to the left of a `deque` and a `list`

# In[ ]:


get_ipython().run_cell_magic('timeit', '', 'l_ = list()\nfor i in range(40000):\n    l_.insert(0, i)')


# In[ ]:


get_ipython().run_cell_magic('timeit', '', 'd = deque()\nfor i in range(40000):\n    d.appendleft(i)')


# In[ ]:


d = deque()
l_ = list()
for i in range(40000):
    d.appendleft(i)
    l_.insert(0, i)
    
list(d) == l_


# The `deque` is orders of magnitude faster than the `list`, but contains the same values.  Thus, for some specialized tasks, it can be a massive enhancement.
# 
# ### `Counter`
# The `Counter` is an extremely useful object.  It counts elements in some iterable and returns a dictionary-like structure containing the count of each element. Lets see an example.

# In[ ]:


from collections import Counter
ele = ['a','b','a','c','b','b','d']
c = Counter(ele)
print(c)


# We can find the number of counts of an element by using the same `get` syntax as a dictionary.  What what happens when we access an element that has no counts.

# In[ ]:


c['a'], c['z']


# We can also find the most common elements

# In[ ]:


c.most_common(2)


# ### `OrderedDict`
# 
# A Python dictionary does not have a natural order, but sometimes it is useful to have the properties of a dictionary like $O(1)$ access to items with an ordering.  An `OrderedDict` is exactly like a `dict`, but it remembers the insertion order of the keys.
# 
# ### `defaultdict`
# 
# One common paradigm of a dictionary is to handle the case of a missing key.  Lets say we take the counter example from above and try to implement our own.  We want to do something like create a dictionary and every time we encounter a key we want to add one to the existing value at that key and if we haven't seen that key, we want to create it and initialize it to zero before adding it.  One way to do this is:

# In[ ]:


def count(x):
    count_dict = {}
    for ele in x:
        if ele in count_dict.keys():
            count_dict[ele] += 1
        else:
            count_dict[ele] = 1
    return count_dict
count(ele)


# This is such a common case that we have the `defaultdict` to deal with it.  The `defaultdict` takes a default _factory function_ which can be as a simple as just returning 0 which produces a value when the key has not been seen before.  We can implement in the same algorithm as above in a bit of a simpler way

# In[ ]:


from collections import defaultdict
def count_default(x):
    count_dict = defaultdict(int)
    for ele in x:
        count_dict[ele] += 1
    return count_dict
count_default(ele)


# ## Some topics we haven't discussed, but have used:
# - `map`

# ## Questions:
# - Are strings immutable? Are strings ordered? Can we slice strings?

# *Copyright &copy; 2020 The Data Incubator.  All rights reserved.*
