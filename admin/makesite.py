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
import globrecur

#
# various functions defined for use in <$foo > tags
#

def include ( file ):
   "Basic Include function - returns text of file specified"
   handle = open ( file, 'r' )
   html = handle.read()
   handle.close()
   return html 



def filelist ( directory ):
   "Does file listing of selected directory"
   os.chdir ( directory ) 
   files = glob.glob ( "*.*" )
   html = '' 

   if '.tar.gz' in [ s [-7:] for s in files ]:
      html +=  '<h3>Source files (*.tar.gz format)</h3>\n'
      for file in files:
         if file [-7:] == '.tar.gz':
            html += '<img src="../e_ball.png"><a href="' + directory 
            html += '/' + file + '">' + file + '</a><br />\n'

   if '.deb' in [ s [-4:] for s in files ]:
      html +=  '<h3>Debian GNU/Linux Packages</h3>\n'
      for file in files:
         if file [-4:] == '.deb':
            html += '<img src="../e_ball.png"><a href="' + directory 
            html += '/' + file + '">' + file + '</a><br />\n'

   if '.zip' in [ s [-4:] for s in files ]:
      html +=  '<h3>Win 32 source files (*.zip format)</h3>\n'
      for file in files:
         if file [-4:] == '.zip':
            html += '<img src="../e_ball.png"><a href="' + directory 
            html += '/' + file + '">' + file + '</a><br />\n'

   if '.exe' in [ s [-4:] for s in files ]:
      html +=  '<h3>Win 32 setup files (*.exe format)</h3>\n'
      for file in files:
         if file [-4:] == '.exe':
            html += '<img src="../e_ball.png"><a href="' + directory 
            html += '/' + file + '">' + file + '</a><br />\n'

   return html



def status ( tool ):
   "Prints status of specified tool"
   s = { 
      'forms' : '''Release 0.5.2 (October 2003) available for download. 
          Development work continues in CVS.''', 
      'curses' : '''Initial "proof-of-concept" support included in Release 
          0.5.1 (August 2003). Official support likely in the 
          0.5.3 release of Forms.''', 
      'gtkforms' : '''Release 0.5.1 (August 2003) available for download. 
          Development work continues in CVS.''',
      'phpforms' : '''Available in CVS. Not currently under active 
          development.''',
      'bayonneforms' : '''Not yet started.''', 
      'designer' : '''Release 0.5.2 (October 2003) available for download. 
          Development work continues in CVS.''', 
      'reports' : '''Release 0.1.3 (October 2003) available for download. 
          Development work continues in CVS.''',
      'appserver' : '''Release 0.0.5 (October 2003) available for download. 
          This is a preview release, not ready for production use. 
          Development continues in CVS.''',
      'common' : '''Release 0.5.2 (October 2003) available for download. 
          Development work continues in CVS.''', 
      'integrator' : '''Work is now underway in CVS.''', 
      'navigator' : '''Release 0.0.6 (October 2003) available for download. 
          Development work continues in CVS.''', 
      'bayonne' : '''Release 1.2 (April 2003) available on the 
          <a href="http://www.gnu.org/software/bayonne">bayonne</a> website.''',
      'docstore' : '''<a href="http://green.zorcat.com/~nick/proj/document-store/gnue/spec/Document-Store/documentstorespec.html">
          Proposals</a> have been written. No work yet done on implementation.''', 
      'financials' : '''<a href="../packages/docs.html#Financials">Proposals</a> 
          have been written. No work yet done on implementation.''', 
      'crm' : '''Not yet started.''', 
      'forecast' : '''Not yet started.''', 
      'hr' : '''Not yet started.''', 
      'manuf' : '''Not yet started.', 
      'prjmgt' : 'Not yet started.''',
      'sales' : '''Not yet started.''', 
      'scm' : '''<a href="../packages/docs.html#SupplyChain">Proposals</a> 
          have been written. No work yet done on implementation.''',
      'dcl' : '''Latest release available via the official 
          <a href="http://dcl.sourceforge.net">DCL</a> website.''' 
       }
   return s.get ( tool, 'Unknown' )



def tabs ():
   "Does the tabs across the top of the page, making one the current tab, the rest greyed out"
   tab = src_file [ 2 : src_file.find( '/', 2 ) ]

   if tab not in [ 'tools', 'packages', 'community', 'tech' ]:
      html = '''
          <td bgcolor="#66CCFF"> 
            <p>&nbsp;
            <font color="#000066">
            <a href="../project/project.html" class="currtab">GNUe Project</a>
            </font>
            &nbsp;</p>
          </td>
             '''
   else:
      html = '''
          <td bgcolor="#CCCCCC"> 
            <p>&nbsp;
            <font color="#FFFFFF">
            <a href="../project/project.html" class="greytab">GNUe Project</a>
            </font>
            &nbsp;</p>
          </td>
             '''

   html += '''
          <td width="5">
             &nbsp;
          </td>
           '''

   if tab in [ 'tools' ]:
      html += '''
          <td bgcolor="#66CCFF"> 
            <p>&nbsp;
            <font color="#000066">
            <a href="../tools/tools.html" class="currtab">GNUe Tools</a>
            </font>
            &nbsp;</p>
          </td>
              '''
   else:
      html += '''
          <td bgcolor="#CCCCCC"> 
            <p>&nbsp;
            <font color="#FFFFFF">
            <a href="../tools/tools.html" class="greytab">GNUe Tools</a>
            </font>
            &nbsp;</p>
          </td>
              '''

   html += ''' 
          <td width="5">
             &nbsp;
          </td>
           ''' 

   if tab in [ "packages" ]:
      html += '''
          <td bgcolor="#66CCFF"> 
            <p>&nbsp;
            <font color="#000066">
            <a href="../packages/packages.html" class="currtab">GNUe Packages</a>
            </font>
            &nbsp;</p>
          </td>
              '''
   else: 
      html += ''' 
          <td bgcolor="#CCCCCC"> 
            <p>&nbsp;
            <font color="#FFFFFF">
            <a href="../packages/packages.html" class="greytab">GNUe Packages</a>
            </font>
            &nbsp;</p>
          </td>
              ''' 

   html += ''' 
          <td width="5">
             &nbsp;
          </td>
           '''

   if tab in [ 'community', 'tech' ]:
      html += '''
          <td bgcolor="#66CCFF"> 
            <p>&nbsp;
            <font color="#000066">
            <a href="../community/community.html" class="currtab">GNUe Community</a>
            </font>
            &nbsp;</p>
          </td>
              '''
   else:
      html += '''
          <td bgcolor="#CCCCCC"> 
            <p>&nbsp;
            <font color="#FFFFFF">
            <a href="../community/community.html" class="greytab">GNUe Community</a>
            </font>
            &nbsp;</p>
          </td>
              ''' 

   return html



def process ( command ):
   "Checks that the command is a known function, then evaluates it"
   func_name = command.lstrip()
   func_name = func_name [ 0 : func_name.find( " " ) ]
   if func_name in [ 'include', 
                     'filelist', 
                     'status', 
                     'tabs' ]:
      html = eval ( command )
   else: 
      html = 'Unknown function'
   return html

      
#
# start of the main makesite.py routine  
#

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
      html_done += process ( function_text )
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

  
