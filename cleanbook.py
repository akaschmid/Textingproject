#This code is used to clean the books and get them read for importation
# Build and desinged by Edwin Akabuilo
# 26th January 2016
# Version 0.0001
import re
#Get the test file name 
fname = "3375.txt"
num_words = 0
occurance = 2
shortlenght = 15
charLineFeed = '\n'
substrCommaValue = ','
#Start Function to get the needed line
def find_nth_character(str1, substr, n):
    k = 0
    for index, c in enumerate(str1):
        #print index, c, n  # test
        if c == substr:
            k += 1
            if k == n:
                return index
#End the Function space
try:
    fcontent = open(fname)
except:
    print "File cannot be opened:", fname
    quit()
#Open file for reading
with open("out.txt", "w") as f1:
    for line in fcontent:
       wordLenght = len(line)
       words = line.split()
       num_words += len(words)
       #Filter the small words less than 10 words
       if wordLenght < 80 :
           #Write the filtered resultset to file
           f1.write(line)
           continue
       #Filter the bigger words greater than 35 worlds
       elif "," in line and num_words <= 35 :
           characterCount = line.count(',')
           if characterCount < 2:
               continue
           elif characterCount >= 3:
               occurance = 3
           else:
               occurance = 2
           pos = find_nth_character(line, substrCommaValue, occurance)
           formatedString = line[:pos] + charLineFeed + line[pos + 1:]
           f1.write(formatedString) 
           continue
       elif "," in line and num_words > 35 :
           words = len(line)
           middleValue = (words / 3)
           secondValue = (middleValue * 2)
           pos = line.find(' ',middleValue)
           pos2 = line.find(' ',secondValue)
           formatedStrings = line[:pos] + charLineFeed + line[pos + 1:]
           #fullstring =  formatedStrings
           fullstring = formatedStrings[:pos2] + charLineFeed + formatedStrings[pos2 + 1:]
           
           f1.write(fullstring) 
           
           continue           
       else:    
            continue
f1.close()
fcontent.close()         
