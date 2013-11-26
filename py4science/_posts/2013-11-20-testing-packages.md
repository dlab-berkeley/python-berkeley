---
layout: post
title:  'Testing Packages: pytest and nose'
author: Dav Clark
---
## In attendance

11 folks signed in, from:

 - Psychology
 - Nuclear Engineering
 - Vision Science
 - Physics
 - L&S
 - IPython
 - and (of course) the D-Lab 

## Nose

You can find out more about Nose [here](LINK).

Katy presented a tutorial on testing from [Software
Carpentry](https://github.com/swcarpentry/bc/tree/gh-pages/lessons/thw-testing)

## Pytest

You can learn more about Pytest [here](LINK).

Thomas presented [a notebook](https://github.com/dlab-berkeley/python-berkeley/blob/master/testing/Test%20frameworks.ipynb), which was mostly about pytest.

## About this post

This is the first post where we're attempting to use zeptojs (similar to jQuery)
to automatically format links to IPython notebooks. For now, we automatically
add a link to view in nbviewer following any link ending in `.ipynb`. It would
be pretty nifty if we could use javascript to look for a notebook server (on
`localhost:8888`?), and offer it a notebook somehow. For now, it's pretty easy
to download with the "raw" button on the GitHub or nbviewer pages (but folks
might not get that!).

<script>
// This expects jQuery or Zepto (or similar) to be loaded somewhere
$('a[href$=".ipynb"]').each(function () {
    // actually need to prepend raw to the URL, and get rid of /blob in the URL!
    var munged = this.href
    munged = munged.replace(/https?:\/\//, 'raw.').replace('/blob', '')
    $(this).after(' (<a href="http://nbviewer.ipython.org/urls/' + munged + '">' +
    'nbviewer</a>)');
});
</script>

