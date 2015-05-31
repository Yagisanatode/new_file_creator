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

FEATURES
      new_file object
         Use this file to save a file in a directory.
         
         new_file(file_to_copy, new_file_name, new_file_path, file_type)
         
         *file_to_copy - The template file you want to copy. e.g. 'tmp.txt' if it is in the same file path or 
                        'c:/Users/Batman/Documents/tmp/txt'
         *new_file_name -The name you want to give your new file. e.g. 'Harry Botter'
         *new_file_path -The directory you want your file in. If you are putting your file in the same location
                        as your program, leave it blank (e.g. ''). If it is in a child directory jsut add the file 
                        location (e.g. 'JSON/' or 'Images/'). If your folder location lies outside your program you
                        will need to use the full path (e.g. 'c:/Users/Batman/Documents/tmp/txt') 
         *file_type - The file extension of your file (e.g. 'jpg', 'txt','json','wav').
         
      extra_file object
         Use this file to save a file using the same name that was created in the new_file object.
         
         extra_file((file_to_copy, directory, file_type))
         
         *file_to_copy - The template file you want to copy. e.g. 'tmp.txt' if it is in the same file path or 
                        'c:/Users/Batman/Documents/tmp.txt'
         *directory - The directory you want your file in. If you are putting your file in the same location
                        as your program, leave it blank (e.g. ''). If it is in a child directory jsut add the file 
                        location (e.g. 'JSON/' or 'Images/'). If your folder location lies outside your program you
                        will need to use the full path (e.g. 'c:/Users/Batman/Documents/tmp.txt')
         *file_type - The file extension of your file (e.g. 'jpg', 'txt','json','wav').
         NOTE - This file uses the directory name from the new_file object.
         
      getting your file once it is loaded
         You can call your newly created file by:
         new_file.new_file.created_file 
         #For your main file. 
         
         new_file.extra_file.created_extra
         #For your child files.
      
   
EXAMPLE 1- Single File Save
         
         import new_file
         chicken = new_file.new_file('blank.json','Jeeves #Smelly B^%#um34','JSON/', 'json')
         
         PROCESS
         *CLEAN THE FILE NAME - if the user creates the file and goes to town on symbols and spaces this will 
         clean it up.
            *Get's rid of whitespace and joins it with and underscore
            *matches any alphanumeric character and the underscore only and joins it back into one string. 
            *Cut filename length to 150 characters if it is over.
            In our example 'Jeeves #Smelly B^%#um34' will be transformed to 'Jeeves_Smelly_Bum34'
         *CHECKS THE IF FILE EXISTS - checks if file already exists in new directory. 
            *Searches for file. 
            *If it exists it creates a copy of the file. For example 'Jeeves_Smelly_Bum34' will become
            'Jeeves_Smelly_Bum34(1)'
            *If a copy exists it will loop through until the numbers run out and creates the next file number.
            For example if 'Jeeves_Smelly_Bum34(1)' 'Jeeves_Smelly_Bum34(2)' 'Jeeves_Smelly_Bum34(3)' files exists
            in your directory then your file will be saved as 'Jeeves_Smelly_Bum34(1)'
            *Concatenates the directory(if present), new file name and file extension.
            *Creates the file
            *Saves a copy of the file name for your use if needed. 

EXAMPLE 2- File and Child Files You Want Saved With the Same File Name
         
         import_new_file
         chicken = new_file.new_file('blank.json','Jeeves #Smelly B^%#um34','JSON/', 'json')
         duck = new_file.extra_file('none.png','Image/','png')
         turkey = new_file.extra_file('Images/gobblegobble.jpg','','jpg')
         emu = new_file.extra_file(''c:/Users/Batman/Documents/tmp.txt'','text/','txt')
         
         PROCESS
         *RUNS THROUGH STEPS IN FIRST EXAMPLE - as you can the 'chicken' instance runs through the 
         new_file object. This is essentially the parent file. 
         * For 'duck','turkey' and 'emu' instances use the extra_file object and do the same thing as 
         each other.
         *GRABS NEW FILE NAME - Gets a copy of the new file name from the new_file object
         *IF IN DIRECTORY - Checks if file created in the new_file class is in a directory and removes 
         the directory if needed.
         *NEW DIRECTORY AND FILE - Concatenates the directory(if present), new file name and file extension
         
POSSIBLE USES
         REGISTER USER
         You could use the new_file module to save username data in a database file, save their avatar with the 
         same name. 
         
         GAME SAVE
         You need some control over the location of where the file needs to be saved here. You can use the users 
         nickname as the name of the file and name any child files like avatar details file, game save location file, 
         inventory file etc all with the same name.
         
P.S. I'm a noop hobbiest programmer. I created this module to help me with my first program. If you have any suggestions
for improvement I would appreciate any guidance. ~Scott
