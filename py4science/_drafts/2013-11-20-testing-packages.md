---
layout: post
title:  Testing Packages: pytest and nose
author: Dav Clark
---
<script>
function nbviewer_link(path) {
    document.write('<a href="http://nbviewer.ipython.org/urls/raw.github.com/dlab-berkeley/python-berkeley/master/' + path + '">' + path + "</a>");
};
// document.write('test');
</script>
## In attendance

TODO (Dav has attendance list)

## Nose

You can find out more about Nose [here](LINK).

Katy presented a tutorial on testing from [Software
Carpentry](https://github.com/swcarpentry/bc/tree/gh-pages/lessons/thw-testing)

## Pytest

You can learn more about Pytest [here](LINK).

<p>
Thomas presented <script>
nbviewer_link('testing/Test frameworks.ipynb');
// document.write('test');
</script>
which was mostly about pytest.
</p>

## About this post

This is the first post where we're attempting to use JavaScript to automatically format
links to IPython notebooks. For now, we provide a link to view in nbviewer, with
a parenthetical link to the GitHub source. It would be pretty nifty if we could
use javascript to look for a notebook server (on `localhost:8888`?), and offer it a
notebook somehow. For now, it's pretty easy to download with the "raw" button on
the GitHub page, but folks might not get that.

An even cooler thing might be to identify links that end with .ipynb and mangle
them.
