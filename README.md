# UC Berkeley Python specific notes

Below are the notes included from the Jekyll-Bootstrap project

I used the the-program theme from the jekyll-bootstrap project to set this up.
Jekyll-Bootstrap which adds an additional layer of indirection. Following are
some quick navigational hints: 

## Styling

    assets/themes/the-program

Note that this uses LESS (which is used by Bootstrap). If you want to edit the
LESS, you'll need lessc (install via npm - the 'node package manager') or some
other tool (my wife likes Crunch). Please don't edit the CSS directly except in
an emergency.

Navigate to the ```assets/themes/the-program/css/``` directory. Make the changes to the LESS files, and run ```lessc style.less style.css```. Then recompile with Jekyll (```jekyll serve```) and things should be good.

## Page templates

    _includes/themes/the-progam

## Boilerplate text

You'll also find useful bits here for the colophon.html (copyright etc., always
at the bottom) and notices.md (sidebar / footer when narrow):

    _includes

## Danger!

Lastly, *please don't edit the bootstrap code*. Override bootstrap styling in "the-program".

# Jekyll-Bootstrap

The quickest way to start and publish your Jekyll powered blog. 100% compatible with GitHub pages

## Usage

For all usage and documentation please see: <http://jekyllbootstrap.com>

## Version

0.3.0 - stable and versioned using [semantic versioning](http://semver.org/).

**NOTE:** 0.3.0 introduces a new theme which is not backwards compatible in the sense it won't _look_ like the old version.
However, the actual API has not changed at all.
You might want to run 0.3.0 in a branch to make sure you are ok with the theme design changes.

## Contributing

This repository tracks 2 projects:

- **Jekyll-Bootstrap Framework.**
  The framework for which users should clone and build their blog on top of is available in the master branch.

  To contribute to the framework please make sure to checkout your branch based on `jb-development`!!
  This is very important as it allows me to accept your pull request without having to publish a public version release.

  Small, atomic Features, bugs, etc.
  Use the `jb-development` branch but note it will likely change fast as pull requests are accepted.
  Please rebase as often as possible when working.
  Work on small, atomic features/bugs to avoid upstream commits affecting/breaking your development work.

  For Big Features or major API extensions/edits:
  This is the one case where I'll accept pull-requests based off the master branch.
  This allows you to work in isolation but it means I'll have to manually merge your work into the next public release.
  Translation : it might take a bit longer so please be patient! (but sincerely thank you).

- **Jekyll-Bootstrap Documentation Website.**
  The documentation website at <http://jekyllbootstrap.com> is maintained in the gh-pages branch.
  Please fork and contribute documentation additions to this branch only.

The master and gh-pages branch do not share the same ancestry. Please treat them as completely separate git repositories!


## License

Jekyll-Bootstrap is licensed under [MIT](http://opensource.org/licenses/MIT)
