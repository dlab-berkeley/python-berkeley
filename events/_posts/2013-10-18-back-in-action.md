---
layout: post
title:  Packaging and Meeting Notes
author: Dav Clark
tags: py4data
---
We've started a new format, where we'll talk about a (hopefully) useful topic
for Python and data science for the first 30-40 minutes. See the end of this
post for a poll for this Friday!

## Planning for the Future

We agreed that we'll invite Ian Greenhouse from Neuroscience to bring his code
to py4data in November. We'll work on developing robust, sharable, well-tested
python code that processes data for pharmacological MRI scans. Even if you're
not a neuroscientist or biologist, this will be a great opportunity to develop
best practices in sotware developmetn, and will include general analysis issues
like spectrum analysis and data management.

We are tentatively planning to start this project at the py4data meeting on Nov 22, 2013

## Making it Easier to Get Started and Learn

We talked about resources that are missing from [python.berkeley.edu](http://python.berkeley.edu).

GOAL: go to [python.berkeley.edu](http://python.berkeley.edu) when confused about something.  It's a work in progress, mostly useful for folks getting started (on Python or a particular topic). Following are some resources we'd like to integrate:

 - Udacity
 - Learn Py the Hard Way
 - Point to GitHub "How To"
 - Learnds. ?
 - Graphing:
     - Vincent (for d3) - apparently hard to use for a beginner
     - ggplot - a copy of R's ggplot2 (Can use ggplot2 or lattice via rpy2)
 - Lecture notes from high-quality intro python courses on campus?Terry Regier
   (Cog Sci / Linguistics) python notes?
			
## How do we Install Packages?
		
1. EASY, TRY THESE FIRST:
    - Canopy (GUI, cmd line)
    - Anaconda (make sure to update conda with `$ conda update conda`)
    - For Ubuntu (and other Debian-based systems): [NeuroDebian PPA](http://neuro.debian.net/)        - Good even for non-neuro-science 
        - other PPAs are mostly outdated or TOO up-to-date / broken
    - Linux: apt/yum/etc
2. Use pip
    - `$ pip install pandas` 
    - `$ pip install -U pandas` to upgrade
3. Download directly from the project page directly
    - download bundle OUTSIDE python dirs/folders. We'll call this `pkg-dir`
    - `$ cd pkg-dir`
    - `$ python setup.py install`

## What do we talk about this Friday?

 - Designing experiments in python (eye tracking, etc.)
 - Speeding up code (pandas/numpy, cython, array ops)
     - start with pandas (over numpy) for social sciences
 - Graphing
 - Nothing
