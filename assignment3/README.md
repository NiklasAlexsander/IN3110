Hello, this is the README file of assignment3 of IN3110.
My assignment3 folder will contain 3 files: wc.py, test_complex, and complex.py

HOW TO RUN:
    
   wc.py: To run wc.py you have multiple choices. You can give a single file
      as argument, or you can give multiple filenames as arguments, or you can
      give all the files in the same folder as wc.py as argument as an asterisk.
      It will run in the terminal.
      
      NOTE: wc.py will not run in the pychache-folder, at least on MacOS. These
      are the folders created when running the tests in pytest, or when you run
      pydoc to get the documentation.

      EXAMPLE: ./ wc.py *
               ./ wc.py filename.py
               ./ wc.py filename1.py filename2.py
               ./ wc.py filename1.py filename2.py filename3.py


   test_complex.py: To run you would have to use pytest to get the most out of
      the asserts used in the file. the pytest will turn green if the all the 
      tests passed.

      EXAMPLE: pytest test_complex.py


   complex.py: You are not supposed to run complex.py. the file contains a
      class called Complex which is being used in the test_complex.py module.
      Therefore there is NO NEED to manually run this module.
      
TO RUN PYDOC:  
             pydoc test_complex  
             pydoc complex  
             pydoc wc  

TO RUN PYTEST:  
             pytest text_complex.py
