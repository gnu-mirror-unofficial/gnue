Website Documentation
=====================

#
# Copyright 2002 Free Software Foundation
#
# Permission is granted to copy, distribute and/or modify this document
# under the terms of the GNU Free Documentation License, Version 1.1 or
# any later version published by the Free Software Foundation; with the
# Invariant Sections being "GNU General Public License", the Front-Cover
# texts being (a) (see below), and with the Back-Cover Texts being (b)
# (see below).  A copy of the license is included in the section entitled
# "GNU Free Documentation License".
#
# (a) The FSF's Front-Cover Text is:
#
#     A GNU Manual
#
# (b) The FSF's Back-Cover Text is:
#
#     You have freedom to copy and modify this GNU Manual, like GNU
#     software.  Copies published by the Free Software Foundation raise
#     funds for GNU development.
#

Location
--------

The web site is held in the HTML CVS for gnue on 
http://savannah.gnu.org. It can be checked out using 
anonymous CVS, and anyone with write access to the GNUe
Sources CVS will also have write access to the HTML CVS.
Please read this readme before changing anything!

At the moment, the site is available at both 
http://www.gnu.org/software/gnue/ and 
http://www.gnuenterprise.org/
Further mirrors might be added later if needed/
volunteered.

The www.gnu.org version of the site is updated every 
time there is a CVS commit. The www.gnuenterprise.org 
version of the site is updated daily via a cron job, or
can be manually checked-out as required.
($TODO: cron job needs setting up - but only once site 
is safely in CVS)

Note that the www.gnuenterprise.org version of the site
also contains some other things not in CVS and hence 
not on the www.gnu.org site:
* /debian/
* /downloads/
* /irc-logs/
* /irc-proxy-images/
* /old_downloads/
* /webalizer/

makesite.py
-----------

The site consists of four main types of files; 
1) "ordinary" files (html, images, executables, 
   documents, etc.)
2) source files ( *.src). These are source files 
   from which the makesite.py script generate an 
   *.html file with the same name. Source files 
   contain the html for the main body of each 
   page (excluding the header and footer) and 
   may also contain "pseudo-tags."
3) include files ( *.inc ). These are used by the 
   makesite.py script to provide standard headers 
   and footers and other includes.
4) The makesite.py file. Any "pseudo-tag" in the 
   *.src file (an HTML tag starting with <$ and ending 
   with >) will be stripped from the html and 
   executed as a python function, including any 
   parameters. All/any required functions should be 
   defined in the makesite.py script.

In order to keep the site up to date, all changes to 
pages which exist as both *.src and *.html versions 
should be made ONLY TO THE *.src VERSION of the page. 
The /admin/makesite.py script should then be run to
generate the html pages just prior to CVS check-in.

This may appear a fairly "old-fashioned" way of doing 
things, but it is preferred for a site like this that 
changes comparatively infrequently (say once a week), 
as it removes the overhead on the web server of running 
a dynamic web server tool like php or (given this 
project's fondness for python!) Zope.

Basic Structure
---------------

The *.inc scripts for the site are mainly in the web 
root directory. The *.src scripts - certainly those 
that use the includes - are mainly in the first-level 
sub-directories. The reason for this is that the whole 
site is built on relative, rather than absolute 
links, so that it will work both where it is hosted in 
the sub-directory of a web server (e.g. 
www.gnu.org/software/gnue) and at the root of a web 
server (e.g. www.gnuenterprise.org).

I originally feared this was going to be a fugly 
restriction, but so far, all the *.src pages 
have naturally fitted into the first-level 
sub-directories. Lower level sub-directories tend to 
be for things that aren't *.src pages, such as 
downloads or documentation.

THIS ALSO MEANS THAT ALL INTERNAL LINKS MUST BE WRITTEN
AS RELATIVE, NOT ABSOLUTE LINKS (e.g. "../foo/bar.html",
not "/software/gnue/foo/bar.html"). The only exceptions 
are links to material not in CVS, and hence only on the 
www.gnuenterprise.org version of the site, which should 
be linked to by the full absolute url (e.g. 
"http://www.gnuenterprise.org/irc-logs/gnue-public.log")

For historic reasons, the main FAQ (faq.html) sits in 
the web root directory. This means it can't use the 
includes (but, as people are more likely to want to 
print this off, that's a feature, not a bug).

Page Template
-------------

The basic template for a *.src page is:

   <h1>Title</h1>

   <h3>Sub-titles (if any)</h3>

   <h5>Sub-sub-title (very rare)</h5>

   <p>Content</p>

Note there are no explicit markers to insert the 
header and footer includes - these are done automatically
for _any_ *.src page by the makesite.py script.

For bulleted lists, do not use <ul>/<li>, but instead use:
<img src="../e_ball.png">Item<br/>
(There should be a neat way of doing this with 
Cascading Style Sheets - please e-mail me if you know 
how.)

Tabs/Sections
-------------

At the moment, there are four possible tabs/sections 
for the site:

tab = "project"   various directories
tab = "tools"     /tools/ directory
tab = "packages"  /packages/ directory
tab = "community" /community/ directory

Apart from the first, which is a catch-all for basic 
information and things that don't fit anywhere else, 
these map on to the three paragraphs of the welcome 
page, project/what.html

The tab function in makesite.py works out which of the four 
tabs across the top of the page should be active, and 
which ones should be greyed.

Adding a new page 
-----------------

There are four stages to adding a new page (e.g. 
foo/bar.html) to a tab/section:

a) Add the bar.src page itself to the foo directory
b) Add a link to the bar.html page to the foo/foo.src 
   index page
c) Add a link to the ../foo/bar.src page to header.inc
d) run the /admin/makesite.py script to (re-)generate
   the pages

Adding a new tab/section 
------------------------

This should be much rarer, not least because having too
many tabs makes the navigation fussy, especially for 
people with small (800 or even 640) screens. But if 
you gotta:

a) Create the new foo directory
b) Create a foo.src index page for it 
d) Add the new section to the header.inc page for the 
   sidebar
e) Change the tabs code in site.py to include the extra 
   tab, and to test whether to make it active or 
   greyed out.
f) Update this README document to include the new 
   tab/section above.
g) Consider re-writing the text on the welcome page, 
   /projects/what.src, to refer to the new tab/section.

The Strapline
-------------

The strapline is the single short line of text below 
the tabs. It is designed for information that will 
change over time, but which needs to be more prominent 
(and less likely to scroll off quickly) than a news 
item. Typical uses are announcements like  "New 
releases available" or "Come and see us at 
LinuxWorldExpo."

The strapline is in the header.inc file, near the 
<!-- strapline --> comment.

News posting 
------------

News articles are all archived in the /news/ directory, 
which is indexed at /news/old.html. In addition, the 
headers of the three most recent news stories are 
displayed at the end of the welcome page, 
/projects/what.html.

Most news items will be originated from within the 
project team. Alternatively, there is a 
mailto:www-support@gnuenterprise.org link on 
the news archive page for other people to submit items

Whatever the source of the news item, prepare it as 
an XML file using your favourite text editor (emacs, 
vi, kate, cat<con: ...)

<article>
   <title>Short &amp; Descriptive.</title>
   <header>This will appear both on the home page and at 
       the start of the story, and should be a short 
       "teaser" paragraph. You <i>may</i> include 
       HTML.</header>
   <body>If the introductory paragraph says all that you 
       need, leave this blank. You <i>may</i> include 
       HTML.</body>
   <mail>Y|N - should an e-mail also be sent to the 
       gnue-announce mailing list with the text of the 
       news story?</mail>
</article>

You can then post the news item by:
a) Checking the web site out of CVS
b) Running the /admin/postnews.py script, giving the name 
   of the above file.
c) This will also automatically run makesite.py for you.
d) Checking the web site back in to CVS

New releases
------------

When there are a set of new releases, various things 
will need to be changed fairly quickly:

a) If we are doing pre-releases as normal, a news 
   story announcing this - and pointing people to the 
   http://www.gnuenterprise.org/downloads/prereleases.php
   page - should be posted.
b) Shortly before the release, the symlinks in 
   http://www.gnuenterprise.org/downloads/current/ should 
   be removed. This means, at that point, we have no 
   "current" release, which is correct.
c) The new releases go into the directory 
   http://www.gnuenterprise.org/downloads/releases/ 
d) Create symlinks in the 
   http://www.gnuenterprise.org/downloads/current/ 
   directory to point to the current releases in 
   http://www.gnuenterprise.org/downloads/releases/
e) Post a news story about the releases - usually just 
   a copy of the gnue-announce mailing - to the site in
   the usual way
f) Consider changing the strapline to "New releases 
   available" for a few weeks.
g) Change the status(tool) function in site.py to refer 
   to the new version numbers (this include is used by both 
   the status.src page and the pages for each tool or 
   package).
h) (Less urgent) Check that the descriptions on the page 
   for each tool or package do not need updating - they 
   are intended to be general enough that they should not 
   need changing every release, but some things they 
   say may no longer be true with the new release.
  