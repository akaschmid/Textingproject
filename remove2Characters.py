import re
#Get the test file name 
fname = "out.txt"
try:
    fcontent = open(fname)
except:
    print "File cannot be opened:", fname
    quit()
#Open file for reading
with open("outclean.txt", "w") as f1:
    for line in fcontent:
       wordLenght = len(line)
       words = line.split()
       num_words = len(words)
       #Filter the small words less than 12 words
       if num_words < 3 :
           #Write the filtered resultset to file
           continue
       #Filter the bigger words greater than 35 worlds
       else: 
           f1.write(line)          
f1.close()
fcontent.close()   
