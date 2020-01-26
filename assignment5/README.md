HOW TO USE:  
    highlighter.py arg1 arg2 arg3  
        arg1: syntax-file's path  
        arg2: theme-file's path  
        arg3: path of the file to be printed/colored  
        python3 highlighter.py python.syntax python.theme demo.py


    diff.py arg1 arg2  
    arg1: original file's path  
    arg2: modified file's path  
    python3 diff.py demofile2.txt demofile2_modified.txt  
    This is the 'ABCEDF' to 'BCDEFG' example in the assignment-paper.  

      To test if the output could be colored, you could use:  
      python3 highlighter.py diff.syntax diff.theme diff_output.txt  


    grep.py arg1 arg2 (OPTIONAL) --highlight arg3  
    arg1: The path to the file you want to grep  
    arg2: The regular expression you want to use (IT WILL BE PASSED AS RAW)  
    arg3(OPTIONAL): color the words captured by regex of choice, pass a color-code.  
    python3 grep.py demo.py NNNN
    python3 grep.py demo.py NNNN --highlight 32


DEMOFILES:  
  I have added a bunch of demofiles that could be used to check each module:    
    
  FOR HIGHLIGHTER.PY:  
    demo.py   -a combination of both the naython demo-file and python-code  
    python.syntax  
    python.theme  
    python2.theme  
    java_example_code.txt  
    favorite_language.syntax -to be used with java_example_code.txt  
    favorite_language.theme -to be used with java_example_code.txt  
    diff_output.txt  
    diff.syntax  -to be used with diff_output.txt  
    diff.theme  -to be used with diff_output.txt    


  FOR DIFF.PY:  
    demofile.txt  
    demofile_modified.txt -to be used with demofile.txt  
    demofile2.txt  
    demofile2_modified.txt -to be used with demofile2_modified.txt  

  FOR GREP.PY:  
    demo.py  
    -could possibly use any file txt-file.  
    grep.py --help (INFO ABOUT THE FILE)


PYDOC:  
    pydoc highlighter  
    pydoc diff  
    pydoc grep  
