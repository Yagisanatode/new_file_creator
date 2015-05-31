# new_file_creator
Python 3 module for creating new files where you need a little more control over file location and file copy template

:mod:`new_file` -- New File Creator
===================================

.. module:: New File
   :synopsis: Sometimes you want a little more control over your source file and where you want to save it
              rather than use something like tkFileDialog where the user has the choice over the location. 
             The new_file modlue allows you to direct to the location of the template file, choose the file 
             name and select the directory it is in. It also allows you to quickly save child fils with the 
             same file name. 
.. moduleauthor:: Scott Donald

FEATURES::
   new_file objec::
      new_file(file_to_copy, new_file_name, new_file_path, file_type)
      *file_to_copy: The template file you want to copy. e.g. 'tmp.txt' if it is in the same file path or 
                     'c:/Users/Batman/Documents/tmp/txt'
      *new_file_name:
      *new_file_path:
      *file_type:
      
   extra_file object::
      extra_file((file_to_copy, directory, file_type))
      *file_to_copy:
      *directory:
      *file_type:
      
   getting your file once it is loaded::
EXAMPLE 1: Single File Save::
   import new_file
   chicken = new_file.new_file('blank.json','Jeeves #Smelly B^%#um34','JSON/', 'json')

EXAMPLE 2: File and Child Files You Want Saved With the Same File Name::
   import_new_file
   chicken = new_file.new_file('blank.json','Jeeves #Smelly B^%#um34','JSON/', 'json')
   duck = new_file.extra_file('none.png','Image/','png')
