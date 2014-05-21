---
layout: post
title: Packaging, a discussion / diatribe
author: Dav Clark
---
### Packaging is great!

I mean, packaging is *really* great. It means you can just install and run
someone else's code and have good confidence it'll "just work." You can also
share your work with others (or yourself) with a minimum of fuss.

### Why is packaging so hard?

The scientific python community has had a long and difficult path with packaging
-- largely because we build complex codes that use lots of "foreign" languages
like fortran and C.

Indeed, [this week's SF Python
meetup](http://www.meetup.com/sfpython/events/178647452/) is actually discussing
this very topic. We've got some scouts heading over, and we'll get a report
back.

### Pip

Currently, there are two main solutions. The "standard" system endorsed by the
python packaging team is pip, and pip is [now available by default in python
3.4](https://docs.python.org/3/whatsnew/3.4.html#whatsnew-pep-453)

If you want to get the straight dirt from the python packaging team, they try to
keep [this](http://packaging.python.org/en/latest/) up to date.

And, it turns out that Matthew Brett has graciously built all the scientific
packages you're likely to want as wheels... I'm sure he'll tell us about it.

### Conda

The other solution, conda, is offered by Continuum analytics as part of their
Anaconda distribution. You could install it in other python distributions, but
(for now), it seems that few people do. Why are these guys putting energy into a
separate effort? [Here's what Travis Oliphant (principal author of NumPy) has to
say.](http://technicaldiscovery.blogspot.com/2013/12/why-i-promote-conda.html)

Want to know more about this "cross-platform homebrew written in Python?" [Docs
are online](http://conda.pydata.org/docs/index.html)

### Other packaging projects

Here's a [video](https://www.youtube.com/watch?v=CefoqK8Qlno) by Roman
Shaposhnik who created the Apache BigTop project for packaging up the Hadoop
ecosystem that may have some interesting parallels. And [the
slides](http://www.slideshare.net/buildacloud/deploying-hadoop-based-bigdata-environments-roman-shaposhnik)
to go with it.

And for those of you old enough to remember, we've had [a
presentation](/events/2013/12/11/coastal-ecosystem-simulation.html) here at the
Workers' Party on [HashDist](http://hashdist.readthedocs.org/en/latest/) and
friends (which, it turns out, is moving towards supporting conda).

### Honorable mention

Setting up a complete development environment is hard. A team of us here on
campus are working on the Berkeley Common Environment (BCE) to facilitate
teaching and research using a standardized VM. Maybe by Friday, I'll have
cleaned up the documentation at [this link](http://collaboratool.berkeley.edu).

### And, I'm back!

I know I've missed a lot of parties, but I hope you welcome me back. I'm hoping
to pull in some folks from the broader community that I met in my travels... I'm
looking forwards to a great summer of Python!

### Updates

 - [Notebook from Matthew](https://github.com/matthew-brett/sketch-books/blob/master/Fun%20with%20wheels.ipynb)
 - [Slides from Thomas](http://www.slideshare.net/takluyver/conda-alternative-packaging-for-scientific-applications)
