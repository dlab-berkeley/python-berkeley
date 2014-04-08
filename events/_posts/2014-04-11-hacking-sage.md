---
layout: post
title: Doing some Hacking
author: Dav Clark
---
### Son and/or Daughter, we need to hack...

[Some weeks
ago](http://python.berkeley.edu/events/2014/02/28/getting-things-done-with-pandas.html),
Chris Holdgraf and I said we wanted to do some hacking on pandas -- really easy
stuff that will make everyone's life better. But, we didn't get around to it!

Then, Will Stein came by and told us about this awesome [IPython extension to do
Sage's convenience
pre-parsing](http://git.sagemath.org/sage.git/tree/src/sage/misc/sage_extension.py).
Sure, it's the kind of thing that will make some people cringe, but it goes some
way towards complaints that python makes you type a lot of stuff.

All we need to do is open a repo with a name (which might [be
hard](http://martinfowler.com/bliki/TwoHardThings.html)!), put that code in
there, et voilà, we've got this crazy new extension for everyone. And we'll need
to factor out the other dependencies from Sage, but how hard can that be?
