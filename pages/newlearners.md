---
layout: page
title: New to Python? Start here
comments: true
permalink: /learn/
---

* content
{:toc}

## Start here!

[Try this 10-minute tutorial.](https://try-python.appspot.com/) When it
loads, type `tutorial` and press Enter to start.

{% highlight python %}
def hi():
  print("hello world")
{% endhighlight %}

## Set up your computer

This is our recommended way to install Python on your system.

#### Install Anaconda

* Please [download the Anaconda installer](http://continuum.io/downloads). We recommend Python 3.
* Choose `Install for me only`
* By default, Anaconda will prepend itself to your PATH -- leave this as is
* When Anaconda has finished installing, open a terminal (Linux, OSX), or the Anaconda Prompt (Windows)
* Type `conda update conda`, hit enter, and then type "y" (and hit enter)
* Type `conda update anaconda`, hit enter, and then type "y" (and hit enter)

#### Run the Jupyter Notebook

With Jupyter, you intersperse code, output, explanatory text, and figures in one big file called a "notebook." Notebooks are a convenient format to explore a language and to share examples of code.

* To run a notebook, open the Terminal (Linux, OSX) or Anaconda Prompt (Windows) and type `jupyter notebook`. 
* The notebook will open a new tab in your default browser. **Do not close the terminal**, as this will also shutdown the notebook. 
* When it has loaded, click on "New" (at the top right) and then "Python3" to create a new notebook.

#### Python 2 vs Python 3

Python 3 (released in 2008) is the newest version of Python, and most features
have not changed. Most packages have been updated to Python 3 by now (2016).
So, if your lab does not have a preference, I recommend using Python 3.

There are a couple key differences for novice programmers:

* In Python 2, you can print with `print 42` or `print(42)`. In Python
  3, you need to use parentheses, as in `print(42)`.
* In Python 2, division of two integers like `5/2` will evaluate to
  `2`. (Python will drop the remainder if both numbers are integers.)
  Python 3 does exact division ('2.5', in this example). If you use Python 2 and do not want this behavior, add this line at the top of each program: 

  `from __future__ import division`.

#### Text editors and IDEs

For creating large projects in Python, we recommend using a text editor in combination with the Jupyter notebook. Popular choices include:

* [Sublime Text](http://sublimetext.com/)
* [Atom](https://atom.io/)
* [Light Table](http://lighttable.com/)

For even larger projects, a well-engineered IDE (Interactive Development Environment) may be better than a text editor. Typically, IDEs include drag-and-drop support for debugging and refactoring. Popular choices include:

* [Spyder](https://pythonhosted.org/spyder/installation.html)
* [PyCharm](https://www.jetbrains.com/pycharm-edu/)

## Practice
Past topics of the Learn Python Working Group are [linked here](/past). Suggestions? Send us an
  [email](mailto:mcarey@berkeley.edu).

#### Software Carpentry

These exercises are really useful to get acquainted with Python. Here's a link to the [Jupyter notebook version](https://bids.github.io/2016-01-14-berkeley/python/00-python-intro.ipynb) and the [webpage version](https://bids.github.io/2016-01-14-berkeley/python/00-python-intro.html).

#### Python for Social Sciences

This is a free online book by Jean Mark Gawron. It's free and online at [this link](http://www-rohan.sdsu.edu/~gawron/python_for_ss/course_core/book_draft/Preface/Preface.html).

#### Resources
Check the [Learning Resources](/resources) page for more learning materials. Others in the [community](/community) may also have relevant materials. 

