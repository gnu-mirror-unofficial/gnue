#! python
# 
# makesite.py
#

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

import os, glob, fnmatch
import globrecur, site_functions

os.chdir ("..") 

# 
# Get standard header and footer
#

handle = open ( 'header.inc', 'r' )
html_head = handle.read()
handle.close()

handle = open ( 'footer.inc', 'r' )
html_foot = handle.read()
handle.close()

#
# find all *.src files to process 
#

src_files = globrecur.GlobDirectoryWalker(".", "*.src")

for src_file in src_files:

   print src_file,

#
# add header and footer to file 
#

   html_raw =  html_head

   handle = open ( src_file, 'r' )
   html_raw += handle.read()
   handle.close()

   html_raw += html_foot

#
# process all <$foo > tags 
#

   position = 0    
   html_done = '' 
   start = html_raw.find ( '<$' )

   while start != -1:
      print '#',
      html_done += html_raw [ position : start ]
      end = html_raw.find ( '>', start )
      function_text = html_raw [ start+2 : end ]
      html_done += site_functions.process ( function_text )
      position = end + 1
      start = html_raw.find ( '<$', position )
   html_done += html_raw [ position : ]
   print 

#
# Write out processed HTML file
#

   handle = open ( src_file[:-4] + '.html', 'w' )
   handle.write ( html_done ) 
   handle.close ()

  