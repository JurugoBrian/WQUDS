
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('logstop', '')
get_ipython().run_line_magic('logstart', '-ortq ~/.logs/PY_Intro.py append')
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144


# # Introduction to Data Science

# Welcome!  We will be taking a deep dive into Data Science over the next few months.  This course will be divided into two parts, the first component will cover basic Python and programming while the second component will cover material in Data Science ranging from basic programming to data cleaning and aggregation.  The basic syllabus is as follows
# 
# |Week|Material|
# |---|---|
# |1| Programming and Python fundamentals|
# |2| Data structures|
# |3| Algorithms, object-oriented programming, & Pythonic style|
# |4| Reading and writing data|
# |5| Python data science packages|
# |6| SQL|
# |7| Data munging|
# |8| Object-relation mapping|
# 
# The second component is a series of miniprojects which will test your mastery of the lecture subjects.  Data Science is not a spectator sport, so its important to practice, the miniprojects are a great way to do that.  There will be a series of five miniprojects which will need to be completed by the end of the course.
# 
# There is an online discussion board where we can help each other learn, share code snippets, and ask questions.  The instructor will be monitoring the board and watching for questions, but it is also important that you interact with your peers.  Remember the best learning often happens when you need to explain something to someone else.

# ## Learning Platform
# 
# We will be using the Jupyter notebook interface for all of our work.  The Jupyter notebook is a great tool for Data Science, especially for exploratory Data Science.  Lets go over a few things about the notebook.
# 
# The notebook is divided into cells, some of which are markdown.

# In[2]:


print('some of which are code')


# The code you are writing in your web browser gets sent to a Python "kernel" living on a cloud server which will execute your code and return the result back to the notebook.  To run a cell we can either click the run button at the top of the screen, or use `shift+enter`.  
# 
# If I define a variable in one cell

# In[3]:


a = 5


# The value is still accessible in another cell:

# In[5]:


print(a)


# In[6]:


print("I'm jurugo Brian")


# Jupyter notebooks do have some autosave functionality, but please remember to save your notebooks manually often to make sure you don't use any work.  If you are familiar with a version control too like `git`, it is not a bad idea to version control the notebooks, although we do ask you don't push the material to a public repository.

# In[7]:


print('Its time to sleep')


# In[2]:


a = 'Am learning to use Jupiter Notebook for python'


# In[3]:


print(a)


# In[4]:


print('Jurugo Brian is an aspiring data scientist')


# ## Exercises
# 
# These notebooks contain many small exercises which help practice the material being discussed.  Some of the exercises will be writing a bit of code, others will be written.  Some of the exercises will be covered in the lecture and some will be left as practice.  Exercises are a great topic to discuss on the forum and please feel free to help each other solve them.
# 
# Now a few exercises for the introduction:
# 
# 1. Make a few cells in the Jupyter notebook and execute them
# 2. Save your Jupyter notebook

# *Copyright &copy; 2019 The Data Incubator.  All rights reserved.*
