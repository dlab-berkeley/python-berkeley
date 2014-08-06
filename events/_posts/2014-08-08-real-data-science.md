---
layout: post
title: Real Data Science!
author: Dav Clark
---
### Dealing with sort-of-big data

Last meeting I (Dav) was talking smack about [Pandas](http://pandas.pydata.org)
while singing the praises of
[Blaze](http://blaze.pydata.org/docs/latest/index.html). Fortunately, the
eminently reasonable Thomas provided counterpoint on the virtues of the
admittedly excellent pandas.

But all of that is about to get cleared up by one of the current developers of
Blaze:

> Blaze is a new project that provides a user interface similar to NumPy and
> Pandas but hooks out to a variety of data and computation backends like HDF5,
> SQL, and Spark.  By separating the user interface from the computation we
> enable users to easily experiment with different systems based on their needs.
> Blaze is experimental and so input both on new backends and on usability is
> welcome.  For a simple usage example see the [README on
> GitHub](https://github.com/ContinuumIO/blaze/blob/master/README.md)

Also, their logo (for now) appears to be a tesseract, which is [even
cooler](http://en.wikipedia.org/wiki/A_Wrinkle_in_Time) than the mathematicians
would lead you to believe. Perhaps the same is true of Blaze?

### Also, devops

We've just minted version 0.1 of [BCE](http://collaboratool.berkeley.edu) (which
might stand for the "Berkeley Common Environment"). As is often the case, you
fine people are amongst the first to know! The goal is to provide a standard
"data science" VM for campus, serving both as a standardized learning
environment, and also a standard reference environment where researchers can
ensure their instructions work in *at least* one place!

Since I've been busy pulling down packages, Aaron from Berkeley Research
Computing (BRC) offered to explain to me (in front of all of you) how he uses a
caching proxy server to speed up repetitive installs, including his efforts to
make this server highly portable with [Docker](http://docker.io). You may not
have heard of Docker, but trust me, they're six ways to crazy about it in the
Valley. Er, South Bay.

### Help us teach!

We're organizing the next D-Lab training [here on this very
website](trainings/2014-08-berkeley-dlab.html)! There, you'll see that the
inimitable Matt Davis has already submitted a [pull
request](https://github.com/dlab-berkeley/python-berkeley/pull/27) to indicate
his availability. Who will be next? How many [points](/points.html) will they
get?

Only time will tell. (Your questions will be answered on Friday, or just shoot
me an email.)
