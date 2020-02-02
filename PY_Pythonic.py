
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('logstop', '')
get_ipython().run_line_magic('logstart', '-ortq ~/.logs/PY_Pythonic.py append')
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144


# In[7]:


import expectexception


# # Pythonisms

# Much of what we covered in the previous notebook can be fairly generally applicable.  Even the Python syntax is quite similar to other languages in the C family.  But there are a few things that every language chooses how to do beyond just syntax (although many new languages do take some inspiration from the Python way of doing things).  The things we will go over here
# 
# * What is Pythonic?
# * Float Division
# * Python `import` system
# * Exceptions
# * How to debug Python
# 
# 
# Lets start by what we mean by the Python way of doing things.

# ## `Pythonic`
# 
# When learning Python, you will probably browse blogs and other web resources that claim certain things are `Pythonic`.  Python has an opinionated way of doing things, mostly captured in the Zen of Python

# In[15]:


import this


# `Pythonic` practices are those which the general Python community has agreed are preferable, sometimes this is purely a stylistic consideration and other times it may be related to the way the Python runs.
# 
# Making your code `Pythonic` can also be useful when other Python programmers need to interact with it as they will be familiar with the idioms and paradigms you use.  

# ## Imports
# 
# In the cells above you might have noticed we used the `import <package>` syntax.  This construct allows us to include code from other python files or more generally modules (collections of files) and packages (collection of modules) into the current code we are working with.  For the purposes of this course, we have installed all the packages you will need on your machine, but for working with packages, some recommended tools are 
# 
# - conda
# - pip
# 
# With installed packages (usually installed with one of those two "package managers"), we can import the package with the `import` command.  We can also import only parts of the package.  For example, one package we will use in the course is called `pandas`.  We can import `pandas`

# In[9]:


import pandas
pandas


# We can also import pandas, but call it something else (saves a bit of typing and is conventional for some of the main packages in the Python scientific stack).

# In[10]:


import pandas as pd
pd


# Now when we want to use a function or class from pandas, we need to call it with the syntax `pd.function` or `pd.class`.  For example, the `DataFrame` object

# In[11]:


pd.DataFrame


# Note that this DataFrame does not exist in the main namespace.

# In[12]:


get_ipython().run_cell_magic('expect_exception', 'NameError', '\nDataFrame')


# We can also just import parts of a package, we can even import them and give them another name!

# In[13]:


from pandas import DataFrame as dframe
dframe


# Another thing we can do is to import everything into the main namespace using the syntax
# 
# ```python
# 
# from pandas import *
# ```
# 
# This is highly discouraged because it can cause problems when multiple packages have a function or class with the same name (not uncommon, think about a function like `.info`).
# 
# We have covered the basic mechanics of the import system, but what does it allow us to do?  Having a sane packaging system allows Python users to package bundles of functionality into modules and packages which can be imported into other bits of codes.  If well written, these packages operate mostly like black boxes, where the user understands _what_ the package is doing, but not necessarily _how_ it is performing its functionality.  
# 
# While it may seem like this is giving up too much control, most of us don't understand exactly how our computer processor works, or even the keyboard, yet we are perfectly comfortable using them to serve their purpose. Packages are similar and when written well can be invaluable tools that allows us incorporate well written tested code that does powerful things into our applications with very little difficulty.

# ## Standard Library
# 
# One useful thing we can do with `import` statements is import packages in the Python standard library.  These are packages which are packaged with the interpreter and available on (almost) any Python installation.  These packages server a wide variety of purposes, here we have listed just a few along with their description.  For the rest, checkout the [documentation](https://docs.python.org/2/library/).
# 
# - `collections` - containers
# - `re` - regular expressions
# - `datetime` - date and time handling
# - `heapq` - the heap queue algorithm
# - `itertools` - functions for help with iteration
# - `functools` - function to assist with functional programming
# - `os` - operating system interfaces
# - `sys` - system functions
# - `pickle` - serialize Python objects
# - `gzip` - work with Gzipped files
# - `time` - time access
# - `argparse` - command line argument handling
# - `threading` - threading interface
# - `multiprocessing` - process based "threading"
# - `subprocess` - subprocess management
# - `unittest` - testing tools
# - `pdb` - debugger
# 
# 
# 
# 
# These packages are optimized, reliable, and available anywhere there is a Python installation, so use them when you can!

# ## Exceptions
# 
# An exception is something that deviates from the norm.  In Python its no different, exceptions are when your program deviates from expected behavior.  The Python interpreter will attempt to execute any code that it's given and when it can't, it will raise an `Exception`.  In our notebooks you will note the `%%expect_exception` magic.  This is just a sign that we know there will be an exception in that cell.  For example, lets try to add a number to a string.

# In[14]:


get_ipython().run_cell_magic('expect_exception', 'TypeError', "\n2 + '3'")


# We can see that this raises a `TypeError` because Python doesn't know how to add a string and an integer together (Python will not coerce one of the values into a different type; remember the Zen of Python: 'In the face of ambiguity, refuse the temptation to guess').  Exceptions are often very readable and helpful to debug code, however, we can also write code to handle exceptions when they occur.  Lets write a function which adds to things together (basically just another version of the add function) except it will catch the `TypeError` and do some conversion.

# In[16]:


def add(x, y):
    try:
        return x + y
    except TypeError:
        return float(x) + float(y)


# Now lets run something similar to the previous example

# In[17]:


add(2, '3')


# As seen above, the way to handle Exceptions is with the `try` and `except` keywords.  The `try` block specifies a bit of code to try to run and the `except` block handles all exceptions that are specifically enumerated.  One can also catch all exceptions by doing
# 
# ```python
# 
# try:
#     func()
# except:
#     handle_exception()
#     
# ```
# 
# But this is not generally a good idea since Python uses Exceptions for all sorts of things (sometimes even exiting programs) and you don't want to catch Exceptions which Python is using for a different purpose.  Think of `Exception` handling as handling the small probability things that will happen in your code, not as a tool to anticipate anything.
# 
# We have seen exceptions, but what are the alternative?  One option, used by other languages is to test ahead of time that conditions necessary to proceed are met.  We can rewrite the add function in a different way.

# In[18]:


def add_2(x,y):
    if not isinstance(x, (float, int)):
        x = float(x)
    if not isinstance(y, (float, int)):
        y = float(y)
    return x + y
add_2(2, '3')


# This also works, but its not Pythonic.  The Pythonic way of thinking about this is roughly analogous to "its easier to ask for forgiveness than permission".  Throwing exceptions actually has other positive benefits, such as the ability to handle errors at higher level code instead of in low level functions.  
# 
# What we mean by this is if we have a series of functions `f_a,f_b,f_c` and `f_a` calls `f_b` which calls `f_c`, we can choose to handle an exception in `f_c` in any of these functions!

# ## Python Debugging
# 
# We have seen how to handle errors with `Exceptions`, but how do we figure out whats wrong when we have errors that we haven't handled?
# 
# Lets look again at our previous example.

# In[19]:


get_ipython().run_cell_magic('expect_exception', 'TypeError', "\n2 + '3'")


# If we look at the returned text, referred to as a `Traceback`, we can see much useful information.  Tracebacks should be read starting from the bottom and working up.  In this case the Traceback tells us exactly what happened, we tried to add an `int` and a `str` and there is no way to do this.  It even points to the exact line of code where this error occurs.  
# 
# Lets take a look at a more complicated Traceback.  We will create a pandas `DataFrame` with illegal arguments.

# In[20]:


get_ipython().run_cell_magic('expect_exception', 'ValueError', "\npd.DataFrame(['one','two','three'],['test'])")


# If we look to the bottom, we can see that this is caused by an improper shape of the arrays we have passed into the `DataFrame` function.  We can trace our way back up through the code to see all the functions which were called in order to get to this error.  In this case, there were four called, `DataFrame, _init_ndarray, create_block_manager_from_blocks, construction_error`.  
# 
# Learning how to read Tracebacks and especially to figure out why simple bits of code are failing is an important part to becoming a good Python programmer.
# 
# ### Exercise
# 
# Run the following bits of code in new cells and determine the error, fix the errors in a sensible way.
# 
# 
# ```python
# # Example 1
# float([1])
# 
# # Example 2
# a = []
# a[1]
# 
# # Example 3
# pd.DataFrame(['one','two','three'],['test'])
# ```

# In[21]:


float([1])


# In[22]:


float(1)


# *Copyright &copy; 2019 The Data Incubator.  All rights reserved.*

# In[23]:


a = []


# In[24]:


a[1]


# In[25]:


a[0]


# In[26]:


pd.DataFrame(['one','two','three'],['test'])

