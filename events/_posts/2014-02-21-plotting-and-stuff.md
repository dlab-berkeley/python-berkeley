---
layout: post
title: Plotting and Stuff
author: You
---
### We're going to PLOT!!!!

There are lots of ways to make your matplotlib experience better (especially
*looking* better):

 - [Seaborn](http://www.stanford.edu/~mwaskom/software/seaborn/)
 - [prettyplotlib](http://olgabot.github.io/prettyplotlib/)
 - [ggplot](http://blog.yhathq.com/posts/ggplot-for-python.html)
 - [brewer2mpl](https://github.com/jiffyclub/brewer2mpl/wiki)
 - [mpltools](http://tonysyu.github.io/mpltools/getting_started.html)

Then, there are numerous approaches using JavaScript (via python):

 - [mplD3](https://github.com/jakevdp/mpld3)
 - [Bokeh](http://bokeh.pydata.org/index.html)
 - [vincent](https://github.com/wrobstory/vincent)

And lastly, [plotly](https://plot.ly) doesn't quit fit into the above. It's a
true web API for plotting.

### Actual discussion

Mark talked about [matplotlib](http://matplotlib.org/) basics. The defaults for
bar plots are poor, but you can fix them up. Scatterplots are great.

[Veusz](http://home.gna.org/veusz/) is a neat package to manually fix up your
plot, but you can save them manually.

[Bokeh](http://bokeh.pydata.org/index.html) can plot matplotlib objects in
javascript. It also does awesome interactive plots and mapping. It can plot in
the notbook directly, but you need to run a bokeh-server. Jake Vanderplas
(author of mpld3) said [he was excited about
Bokeh](http://jakevdp.github.io/blog/2013/03/23/matplotlib-and-the-future-of-visualization-in-python/)
too.

[Plotly](https://plot.ly) requires you to be online, but looks nice and is
interactive / easy to share.

[Vincent](https://github.com/wrobstory/vincent) is an easy way to get from
pandas to D3 (but provides a strong abstraction layer around D3 - Vega).

If you're interested in digging into javascript,
[dimple.js](http://dimplejs.org/) comes recommended as a well-documented,
lightweight approach that allows full access to D3 underneath. It doesn't do
maps, so if you want that, leaflet and tilemill seem to be the go-to tech
these days, with a lot of investment by the folks at Mapbox. [This
post](https://www.mapbox.com/blog/github-visual-diff/) will probably make you
say "whoa, holy map-diffs, GitHub!"
