// This expects jQuery or Zepto (or similar) to be loaded somewhere
// Are we getting to the point where JS dependency tracking is a wise idea?
$(document).ready(function () {
    $('a[href$=".ipynb"]').each(function () {
        // actually need to prepend raw to the URL, and get rid of /blob in the URL!
        var munged = this.href
        // More sophisticated URL rewriting should just go into nbviewer
        munged = munged.replace(/https?:\/\//, '')
        $(this).after(' (<a href="http://nbviewer.ipython.org/urls/' + munged + '">' +
        'nbviewer</a>)');
    });
});
