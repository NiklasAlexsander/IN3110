Hello, this is the readme-file for Assignment6 IN3110.

HOW TO RUN:  

  data.py:  
    python data.py


  fitting.py:  
    python fitting.py


  visualize.py:  
    python visualize.py


  web_visualization.py:  
    python web_visualization.py



  None of the scripts above need any arguments to run. Inside each script there's
  some tests that's run only if you run each script separately.  
    data.py will show three different scatter-plots with three different combinations of
    features.    
    visualize.py will show a single scatter-plot. Tried to make an area colored as mentioned in task 6.3, got close, but it didn't work. Therefore visualize does nearly the same as data.py with the plotting.  
    fitting.py will print three tests of each classifier KNN, SVC, and LR, with three different feature-sets and each classifier's accuracy.  


    To run the web-server, all you need to do is to run web_visualization.py, it's local only. 
    While the web_visualization.py starts, the html-pages for the pydocs will be generated. 
    The html-changes will be remade/updated every time the server restarts or refreshes. The 
    html-files to the docs are located inside a folder called 'docfiles' inside the folder 
    'templates'. The placement of 'docfiles' is not random. Flask automatically looks for html-templates
    in the 'templates'-folder. 
    When looking through the help-pages, just remember that there's only help-pages to the scripts 
    provided in this package. Help-pages for all the external imports like numpy and matplotlib will 
    not be accessible through the help-pages even though the imports are listed and do contain a 
    clickable link.
    
    When two features are given as input on the website, three scatter-plots will be shown. 
    The first should actually be where the scatter-plot with the colored areas should be. 
    Since I did not manage to make it work properly, I have just placed a 'static' scatter plot 
    at this spot. This plot will not change. If I someday manage to correct my code the picture 
    could easily be swapped out with a correct plot.  


  This assignment does also include a simple html-file for the website. It contains some checkboxes, some text, and some placements for pictures. The file is called web.html and is located inside the templates-folder.  


  Assignment6_web_help.py:  
This is just a file I have made to make the help-page a bit cleaner. When accessing the helping-page from the website, the html-help-page for 'Assignment6_web_help.py' will be the first help-page you see. The file is just a module containing imports of each script in this package. When running pydocs a nice page with links to each module imported will be visible in the html-file. This makes the help-page a bit better to go through.
