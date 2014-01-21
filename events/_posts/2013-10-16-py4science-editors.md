---
layout: post
title:  "Meeting Notes for 2013-10-16"
author: Cindee Madison
---

Last Meeting **Editors**
=======

![editors](/events/assets/text_editors.png)

Attendance : 9

* Overview of different editors 
* most useful, and resources on how to get started using that particular editor)

=======

  * Emacs: Jess
  * Sublime: Bill
  * Vim: Many
  * Gedit: Dav

### Jess Hamrick started with [Emacs](http://www.gnu.org/software/emacs/)

 * suggested the [homebrew](http://brew.sh/) version os cocoa emacs for MacOSX

####The **bad**
   * high initial learning curve 
   * plugins can be buggy 
   * bad package management 
   * customization written in [elisp](http://en.wikipedia.org/wiki/Emacs_Lisp)

####The **good**
   * [emacswiki.org](http://www.emacswiki.org/emacs/?action=browse;oldid=PythonMode;id=PythonProgrammingInEmacs)
   * supports many languages (Python, Latex, GIT Markdown)
   * Terminal mode
   * plugin for ipython notebook
   * scratch buffer for prototyping
   * [Jedi](http://tkf.github.io/emacs-jedi/) for auto completion
   * [nipy tricked out emacs] (http://nipy.sourceforge.net/devel/tools/tricked_out_emacs.html)
   * [pycheckers](https://github.com/dholm/flymake-pycheckers) for integrating 
   * [magit](https://github.com/magit/magit) Git interface

***

### Dav Clark [Gedit](https://projects.gnome.org/gedit/) via virtualbox

Used [virtualbox](https://www.virtualbox.org/wiki/Downloads) + [vagrant](http://www.vagrantup.com/) 
to run ubuntu and gedit on OSX

[github resources for vagrant](https://github.com/dlab-berkeley/python-berkeley/tree/master/editor_setup)

   * gedit and related packages need to map to outside folder, but this is easy to set up    
   * preferences
   * set up default preferences by choosing preferences form File menu
   * easily choose relevent modules (eg smart spaces)
   * great tool for beginners and teaching
   * syntax highlighting

****

### Bill Sprague [Sublime](http://www.sublimetext.com/)

#### The **bad**
   * not opensource need a license ($70) 
   * though!! public beta for verson 3 license is not required

#### The **good**  
   * sublime works on all platforms
   * faster and less bloated than Vim
   * powerful GUI interface
   * multiple ways to edit text 
    * command pallate is amazing  (has fuzzy searching for all commands making it trivial to find command you want)
    * good keyboard
    shortcuts classic mode with vim keyboard shortcuts, good for transition
    * setup files are json script, easy to edit
    * many add on packages which are easy to install
    * has project mode for searching within projects
    * good for multipurpose cleaning of text files

