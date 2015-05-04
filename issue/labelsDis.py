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


def splits(e):
  result = []
  strs = ''
  for c in e:
     if c != ',' and c != '[' and c != ']' and c != '\'':
	strs += c
     else:
        if len(strs) >0 and strs != ' ':
           result.append(strs)
	strs = ''	
  return result



print("Label DISTRIBUTION===========")
#project 1
csvfile = file('proj1.csv','rb')
csvfile2 = file('labelDis1.csv','w')
reader = csv.reader(csvfile)
writer = csv.writer(csvfile2)
t = []
labels = set([])
for line in reader:
  [a,b,c,d,e,f,g] = line
  for ll in splits(e):
      labels.add(ll)

for la in labels:
   count = 0
   csvfile.seek(0)
   for line in reader:
      [a,b,c,d,e,f,g] = line
      for ll in splits(e):
           if ll == la:
               count += 1
   writer.writerows([[la,count]])
csvfile.close()

#project 2
csvfile = file('proj2.csv','rb')
csvfile2 = file('labelDis2.csv','w')
reader = csv.reader(csvfile)
writer = csv.writer(csvfile2)
t = []
labels = set([])
for line in reader:
  [a,b,c,d,e,f,g] = line
  for ll in splits(e):
      labels.add(ll)

for la in labels:
   count = 0
   csvfile.seek(0)
   for line in reader:
      [a,b,c,d,e,f,g] = line
      for ll in splits(e):
           if ll == la:
               count += 1
   writer.writerows([[la,count]])
csvfile.close()
csvfile2.close()

#project 3
csvfile = file('proj3.csv','rb')
csvfile2 = file('labelDis3.csv','w')
reader = csv.reader(csvfile)
writer = csv.writer(csvfile2)
t = []
labels = set([])
for line in reader:
  [a,b,c,d,e,f,g] = line
  for ll in splits(e):
      labels.add(ll)

for la in labels:
   count = 0
   csvfile.seek(0)
   for line in reader:
      [a,b,c,d,e,f,g] = line
      for ll in splits(e):
           if ll == la:
               count += 1
   writer.writerows([[la,count]])
csvfile.close()
csvfile2.close()

