# postnews.py

#
# Copyright 2002 Free Software Foundation
#
# This file is part of GNU Enterprise.
#
# GNU Enterprise is free software; you can redistribute it 
# and/or modify it under the terms of the GNU General Public 
# License as published by the Free Software Foundation; either 
# version 2, or (at your option) any later version.
#
# GNU Enterprise is distributed in the hope that it will be 
# useful, but WITHOUT ANY WARRANTY; without even the implied 
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR 
# PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public 
# License along with program; see the file COPYING. If not, 
# write to the Free Software Foundation, Inc., 59 Temple Place 
# - Suite 330, Boston, MA 02111-1307, USA.
#

# 
# Post a submitted news article
#
# 1. Extract xml from news file
# 2. Get next article number
# 3. Create news???.src file
# 4. Edit old.src file to include new link
# 5. Shift old news headlines down a place
# 6. Create new top headline
# 7. Send e-mail to gnue-announce (if requested)
# 8. Report success/failure
# 9. Run makesite to update for all changed *.src files
#

import sys, glob, os, time

def xml_slice ( haystack, tag ): 
   'Finds the first instance of tag within haystack, and returns it contents'
   start = haystack.find( '<' + tag + '>' ) + len ( tag ) + 2 
   end = haystack.find( '</' + tag + '>', start ) 
   return haystack [ start:end ] 

#
# 1. Extract xml from news file
#

news_file = sys.argv[-1] 

handle = open ( news_file, 'r') 
news_text = handle.read() 
handle.close()

title  = xml_slice ( news_text, 'title'  )
header = xml_slice ( news_text, 'header' )
body   = xml_slice ( news_text, 'body'   )
mail   = xml_slice ( news_text, 'mail'   )
date   = time.strftime ( "%d %B %Y", time.gmtime() ) 

#
# 2. Get next article number
#

os.chdir  ( '../news' )
num = str ( max( [ int(x[4:-4]) for x in glob.glob ( 'news*.src' ) ] ) + 1 )
 
#
# 3. Create news???.src file 
#

handle = open ( 'news' + num + '.src', 'w' )

handle.write ( '<h1>' + title + '</h1>\n' )
handle.write ( '\n' )
handle.write ( '<p>' + date + '</p>' )
handle.write ( '<p>' + header + '</p>' )
handle.write ( '\n' )

if ( body ):
   handle.write ( '<hr>\n' )
   handle.write ( '\n' )
   handle.write ( '<p>' + body + '</p>\n' )
   handle.write ( '\n' ) 

handle.write ( '<hr>\n' ) 
handle.write ( '<p><a href="old.html">Return</a> to news archive</p>\n' ) 

handle.close()

#
# 4. Edit old.src file to include new link
#

handle = open ( 'old.src', 'r' )
old_src = handle.read()
handle.close()

handle = open ( 'old.src', 'w' ) 

split = old_src.find ( '<img src=' )
handle.write ( old_src [:split] ) 
handle.write ( '<img src="../e_ball.png"><a href="news' + 
               num + 
               '.html">' + 
               title + 
               '</a> - ' + 
               date + 
               '<br />\n' ) 
handle.write ( old_src [split:] ) 

handle.close() 

#
# 5. Shift old news headlines down a place 
#

os.chdir  ( '..' )
os.rename ( 'news_b.inc', 'news_c.inc' )
os.rename ( 'news_a.inc', 'news_b.inc' )

#
# 6. Create new top headline
#

handle = open ( 'news_a.inc', 'w' ) 

handle.write ( '<h3>' + title + '</h3>\n' )
handle.write ( '\n' )
handle.write ( '<p>' + date + '</p>\n' )
handle.write ( '<p>' + header + '</p>\n' )
handle.write ( '\n' ) ;

if ( body ):
   handle.write ( '<p><a href="../news/news' + 
                  num + 
                  '.html">More ...</a></p>\n' )

handle.close() 

#
# 7. Send e-mail to gnue-announce (if requested) 
#

# TODO : need to get this working

# if mail[1] = "Y":
#   mail_text =  strip_html$TODO ( header ) + '\n'
#   mail_text += '\n'
#   mail_text += ( '-' * 70 ) + '\n' 
#   mail_text += '\n'
#   mail_text += strip_html$TODO ( body ) + '\n' 
#   mail_text += '\n' 
#   mail_text += '-- \n'
#   mail_text += 'The GNUe core team <info@gnue.org>\n'
#
#   mail$TODO$ ( To:'gnue-announce@gnu.org', 
#          From:'info@gnue.org',
#          Subject:title, 
#          Text:mail_text ) 

#
# 8. Report success/failure
#

os.chdir ( 'admin' )
import makesite

print ' ' 
print 'News posted'
print '-----------'
print 'Article posted as news' + num + '.src'
print 'Please update CVS as soon as possible to avoid conflicts'
print ' ' 
print 'cvs add ../news/news' + num + '.*'
print 'cvs commit'


