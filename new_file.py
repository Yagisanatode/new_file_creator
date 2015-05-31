"""
NEW FILE
========
Python 3 module for creating new files where you need a little more control
over file location and file copy template.

Author: Scott Donald

EXAMPLE INPUT FOR BOTH CLASSES:
import new_file
chicken = new_file.new_file('blank.json','Jeeves #Smelly B^%#alls34','JSON/', 'json')
duck = new_file.extra_file('none.png','Image/','png')
"""

import re
import os
import shutil
class new_file():
    """
    Requires: (original file and path, name of new file, path of new file, file_type)
    For example: Image/'batman.jpg', 'robin','GameImg/','jpg'
    """
    def __init__(self, file_to_copy, new_file_name, new_file_path, file_type):
        self.file_to_copy = file_to_copy
        self.new_file_name = new_file_name
        self.new_file_path = new_file_path
        self.file_type = file_type

        self.file_clean()
        self.new_file = self.new_file_path+self.new_file_name+'.'+self.file_type
        self.check_file()
        
    def file_clean(self):
        #Get's rid of whitespace and joins it with and underscore
        self.new_file_name = "_".join(self.new_file_name.split())
        #matches any alphanumeric character and the underscore only
        #and joins it back into one string. 
        self.new_file_name = "".join(re.findall(r'[\w]', self.new_file_name))
        #Cut filename length to 150 characters if it is over.
        self.new_file_name = self.new_file_name[:150]

    def check_file(self): 
        if os.path.isfile(self.new_file) == True:
            x = 1              
            while os.path.isfile(self.new_file_path+self.new_file_name+'('+ str(x) + ').'+self.file_type) == True:
                x += 1
            else:              
                self.new_file =  self.new_file_path+self.new_file_name+'('+ str(x) + ').'+self.file_type
                self.make_file()                                                    
        else:
            self.make_file()

    def make_file(self):     
        shutil.copy2(self.file_to_copy,self.new_file)
        
        #template for any extra files. 
        new_file.created_file = self.new_file

class extra_file():
    '''
    (file you will copy from,
    the directory you will put it in,
    they file type)
    This uses the file name from the new_file class
    '''
    def __init__(self, file_to_copy, directory, file_type):
        self.file_Name = new_file.created_file
        
        self.file_to_copy = file_to_copy
        self.directory = directory
        self.file_type = file_type

        self.if_in_directory()
        
    def if_in_directory(self):
        #Checks if file created in the new_file class is in a directory
        #and removes the directory if needed.
        if  '/' not in self.file_Name:
            self.file_Name = self.file_Name.rpartition('.')[0]
            self.new_directory_and_file()
        else:
            self.file_Name = self.file_Name.rpartition('/')[-1].rpartition('.')[0]
            self.new_directory_and_file()

    def new_directory_and_file(self):
        self.path_and_file = self.directory+self.file_Name+'.'+self.file_type
        self.make_file()
    def make_file(self):
        shutil.copy2(self.file_to_copy,self.path_and_file)
        
    


