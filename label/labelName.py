#  gitabel
#  the world's smallest project management tool
#  reports relabelling times in github (time in seconds since epoch)
#  thanks to dr parnin
#  todo:
#    - ensure events sorted by time
#    - add issue id
#    - add person handle

"""
You will need to add your authorization token in the code.
Here is how you do it.

1) In terminal run the following command

curl -i -u <your_username> -d '{"scopes": ["repo", "user"], "note": "OpenSciences"}' https://api.github.com/authorizations

2) Enter ur password on prompt. You will get a JSON response. 
In that response there will be a key called "token" . 
Copy the value for that key and paste it on line marked "token" in the attached source code. 

3) Run the python file. 

     python gitable.py

"""
 
from __future__ import print_function
import urllib2
import json
import re,datetime
import sys
import csv
 
class L():
  "Anonymous container"
  def __init__(i,**fields) : 
    i.override(fields)
  def override(i,d): i.__dict__.update(d); return i
  def __repr__(i):
    d = i.__dict__
    name = i.__class__.__name__
    return name+'{'+' '.join([':%s %s' % (k,pretty(d[k])) 
                     for k in i.show()])+ '}'
  def show(i):
    lst = [str(k)+" : "+str(v) for k,v in i.__dict__.iteritems() if v != None]
    return ',\t'.join(map(str,lst))

  
def secs(d0):
  d     = datetime.datetime(*map(int, re.split('[^\d]', d0)[:-1]))
  epoch = datetime.datetime.utcfromtimestamp(0)
  delta = d - epoch
  return delta.total_seconds()
 

print("===LABEL NAMES#===========")
#project 1
csvfile = file('proj1.csv','rb')
reader = csv.reader(csvfile)
names = []
for line in reader:
    [a,b,c] = line
    names.append(a)
names.sort()
print(names)    
print("===============")
csvfile.close()

#project 2
csvfile = file('proj2.csv','rb')
reader = csv.reader(csvfile)
names = []
for line in reader:
    [a,b,c] = line
    names.append(a)
names.sort()
print(names)    
print("===============")
csvfile.close()

#project 3
csvfile = file('proj3.csv','rb')
reader = csv.reader(csvfile)
names = []
for line in reader:
    [a,b,c] = line
    names.append(a)
names.sort()
print(names)    
print("===============")
csvfile.close()

