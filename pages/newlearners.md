---
layout: page
title: New to Python? Start here
comments: true
permalink: /learn/
---

* content
{:toc}

## For New Learners

Here is a great list of resources when getting started with Python:

#### Start here!

[Start with this 10-minute tutorial.](https://try-python.appspot.com/) When it
loads, type `tutorial` and press Enter to start.

```{python}
def hi():
    print("hello world")
```

## Set up your computer

This is our recommended way to install Python on your system.

#### Install Anaconda

* Please [download the Anaconda installer](http://continuum.io/downloads). We recommend Python 3.
* Choose `Install for me only`
* By default, Anaconda will prepend itself to your PATH -- leave this as is
* When Anaconda has finished installing, open a terminal (Linux, OSX), or the Anaconda Prompt (Windows)
* Type `conda update conda`, hit enter, and then say "y"
* Type `conda update anaconda`, hit enter, and then say "y"

#### Run Jupyter

With Jupyter, you intersperse code, output, explanatory text, and figures in one big file called a "notebook." Notebooks are a convenient format to explore a language and to share examples of code, but should not be used to write programs.

* To run a notebook, open the Terminal (Linux, OSX) or Anaconda Prompt (Windows) and type `jupyter notebook`. 
* The notebook will open a new tab in your default browser. **Do not close the terminal**, as this will also shutdown the notebook. 
* When it has loaded, click on "New" (at the top right) and then "Python3" to create a new notebook.

#### Text editors

For writing code in Python, we recommend the use of a text editor in combination with IPython and a testing suite. Popular choices include:

* [Sublime Text](http://sublimetext.com/)
* [Atom](https://atom.io/)
* [Light Table](http://lighttable.com/)

#### IDEs

For more complicated projects, a well-engineered IDE may be better than a text editor. Typically, IDEs include support for visual debugging and code refactoring. Popular choices include:

* [Spyder](https://pythonhosted.org/spyder/installation.html)
* [PyCharm](https://www.jetbrains.com/pycharm-edu/)

#### Python 2 vs Python 3

Python 3 (released in 2008) is the newest version of Python, and most features
have not changed. Most packages have been updated to Python 3 by now (2016).
So, if your lab does not have a preference, I recommend using Python 3.

There are a couple key differences for novice programmers:

* In Python 2, you can print with `print 42` or `print(42)`. In Python
  3, you need to use parentheses, as in `print(42)`.
* In Python 2, division of two integers like `5/2` will evaluate to
  `2`. (Python will drop the remainder if both numbers are integers.)
  Python 3 does exact division (in this example, `2.5`).
    * If you use Python 2 and do not want this behavior, add this line at the
      top of each program: `from __future__ import division`.


## More Practice

[Go through these
exercises](https://bids.github.io/2016-01-14-berkeley/python/00-python-intro.html)
(courtesy of Software Carpentry). Click here for the [Jupyter notebook
version](https://bids.github.io/2016-01-14-berkeley/python/00-python-intro.ipynb).

#### Longer Reads and Lessons

* [Python for Social
  Sciences](http://www-rohan.sdsu.edu/~gawron/python_for_ss/course_core/book_draft/Preface/Preface.html),
  a free online book by Jean Mark Gawron
* Lessons on [other topics](http://software-carpentry.org/lessons/) are
  available from Software Carpentry

#### Beyond

* See the Learn Python Working Group's past topics [here](/past).
* Others in the [community](/community) may have relevant materials.
* Also, see the [learning resources](/resources) page.

## Suggestions

* Have something you want to add? Send an
  [email](mailto:marwahaha@berkeley.edu) to marwahaha@berkeley.edu, or fork me
  on Github.
