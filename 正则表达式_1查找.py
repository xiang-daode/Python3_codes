
#!/usr/bin/python
import re
 
line = "Cats are smarter than dogs , dogs smarter than pigs";
 

 
matchObj = re.search( r'dogs', line, re.M|re.I)
if matchObj:
   print ("search --> searchObj.group() : ", matchObj.group())
else:
   print ("No match!!")
