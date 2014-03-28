## Installing gedit + useful plugins with apt-get

I'm basing this on Ubuntu 12.04.3, as that seems like a reasonable minimum level
of being up-to-date. It should be clear how to adapt this to other distros with
comparable packages. *See below for instructions on how to bootstrap this with
Vagrant!*

After the standard `apt-get update`, run `apt-get install` for the following:

- **gedit** Of course!
- **gedit-plugins** A set of plugins for managing text better, includes things
  like smart tabs/spaces, multi edit, code comment, etc.
- **gedit-developer-plugins** syntax completion, python completion from imports,
  syntax/style checking for python, 
- **rabbitvcs-gedit** GUI-ish thing for git, svn, bzr

Not relevant to python, but you might also include gedit-latex-plugin and
gedit-r-plugin for completeness for a beginning user.

## Installing gedit with Vagrant

By default, this uses [VirtualBox](https://google.com/search?q=virtualbox).
You'll also need to install [Vagrant](http://vagrantup.com). You will likely
prefer VMware if you have it (setting that up is an exercise for the
reader).

There should be a `Vagrantfile` and a `bootstrap.sh` in the same folder as this
file. From the command line, just type `vagrant up`. See those files for more
info, and the [Vagrant website](http://vagrantup.com) for the full
documentation.

In this case, unusual for vagrant, I've enabled X11 forwarding (and installed
XQuartz). You can find the x11 config setting in the Vagrant file, and XQuartz
is installable via a [Google search](https://www.google.com/search?q=XQuartz).

