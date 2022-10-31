Here you will find how to run a Python Script which allows the users to pick what file to open and the programs returns certain perimeters that you can edit.

 <b>python3 project2/wordselector</b> 
 will the program and you will be welcoemed with a prompt to enter in which file you would like to open.

Once a file is opened the application will return whatever it is you entered in the code. In this case, all words that start with "g" will return.
<p><b>for text in fileChoice:
    if text.startswith('g'):
        continue
    print('The words were: ',text)
    exit()<b></p>
  
  The exit function closes the program once finished. 
