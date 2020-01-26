# Assignment 4
Hello, this is the README file of assignment4 of IN3110. My assignment4 folder 
will contain 3 folders and 2 files, (capitalized folder-names). If a folder is
mentioned multiple times, it's still the same folder:  

ASSIGNMENT4: MODULES, TESTS, BLURFACES, setup.py, README.md  
MODULES:     BLUR1, BLUR2, BLUR3, blur.py, beatles.jpg  
TESTS:       test_blur.py  
BLURFACES:   blur_faces.py, haarcascade_frontalface_default.xml, 3 beatles pictures  
BLUR1:       blur_1.py  
BLUR2:       blur_2.py  
BLUR3:       blur_3.py      

## DEPENDENCIES:  
To run use this module, it is important to install both numpy and numba, which
both can be installed using pip or with conda.  

## HOW TO RUN:  
To run my script, all you need to do is to run blur.py from where it is located,
with the right useage of flags. You have to specify which of the blurs you want
to run to even make it work. A blur.py -h OR -help is included for more detail.  

Without any specified input-file the script will result to using 'beatles.jpg' 
as input, however it will not save a file since the task specified this as a
feature: ''If output filename is supplied, the blurred image should also be saved 
to the specified location.'' - 4.6 Packaging and unit tests  

to run:  
```
./blur.py --blurtype 1 --input 'beatles.jpg' --output 'PATH_OF_CHOICE'
```

## PYDOC:  
There are also docstrings for each function included as well. To run these you
have to use pydoc 'nameoffile'.
This has to be done on each file, unless another pydoc method goes through
each file by itself, which I am not aware of at the time of writing. Maybe
some kind of 'asterix'.py would be possible?  

## HOW TO TEST:  
To run with pytest you have to navigate to the folder 'tests' and run:  
```
pytest test_blur.py
```

## BLURFACES:  
`blur_faces.py` will only use the `beatles.jpg` provided in testing. When finished 
it will save a file in the same folder, where the faces are framed green, or not. 
This depends on the amount of iterations chosen by the user. 

To use blur_faces.py the only thing you have to do is to run blur_faces.py inside of 
it's folder and add a number. I would recommend somewhere around 300 if you want the 
face-recognition to fail, around 3-6 minutes to run:  
```
./blur_faces.py 'integer'
./blur_faces.py 300
```
