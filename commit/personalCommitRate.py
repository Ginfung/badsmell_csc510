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



csvfile = file('proj0.csv','rb')
reader = csv.reader(csvfile)
name = set([])
for line in reader:
   [a,b] = line
   name.add(a)
personalCommit = []
for member in name:
   x = []
   csvfile.seek(0)
   for line in reader:
      [c,d] = line
      if c == member:
	x.append(int(float(d)))
   personalCommit.append(x)

t = []
csvfile.seek(0)
for line in reader:
   [a,b] = line
   t.append(int(float(b)))
t.sort()
total_week = (t[-1]-t[0])/(7*24*3600)
end = []
for i in range(total_week):
   end.append(t[0]+(i+1)*7*24*3600)

for t in personalCommit:
   week = []
   c = 0
   for x in t:
      if  x < end[0]:
         c += 1
   week.append(c)

   for alpha in range(1,total_week):
      c = 0
      for x in t:
         if x >= end[alpha-1] and x < end[alpha]:
             c+= 1
      week.append(c)
   print(week)
csvfile.close()
print("=========================")
csvfile = file('proj1.csv','rb')
reader = csv.reader(csvfile)
name = set([])
for line in reader:
   [a,b] = line
   name.add(a)
personalCommit = []
for member in name:
   x = []
   csvfile.seek(0)
   for line in reader:
      [c,d] = line
      if c == member:
	x.append(int(float(d)))
   personalCommit.append(x)

t = []
csvfile.seek(0)
for line in reader:
   [a,b] = line
   t.append(int(float(b)))
t.sort()
total_week = (t[-1]-t[0])/(7*24*3600)
end = []
for i in range(total_week):
   end.append(t[0]+(i+1)*7*24*3600)

for t in personalCommit:
   week = []
   c = 0
   for x in t:
      if  x < end[0]:
         c += 1
   week.append(c)

   for alpha in range(1,total_week):
      c = 0
      for x in t:
         if x >= end[alpha-1] and x < end[alpha]:
             c+= 1
      week.append(c)
   print(week)
csvfile.close()
print("=========================")
csvfile = file('proj2.csv','rb')
reader = csv.reader(csvfile)
name = set([])
for line in reader:
   [a,b] = line
   name.add(a)
personalCommit = []
for member in name:
   x = []
   csvfile.seek(0)
   for line in reader:
      [c,d] = line
      if c == member:
	x.append(int(float(d)))
   personalCommit.append(x)

t = []
csvfile.seek(0)
for line in reader:
   [a,b] = line
   t.append(int(float(b)))
t.sort()
total_week = (t[-1]-t[0])/(7*24*3600)
end = []
for i in range(total_week):
   end.append(t[0]+(i+1)*7*24*3600)

for t in personalCommit:
   week = []
   c = 0
   for x in t:
      if  x < end[0]:
         c += 1
   week.append(c)

   for alpha in range(1,total_week):
      c = 0
      for x in t:
         if x >= end[alpha-1] and x < end[alpha]:
             c+= 1
      week.append(c)
   print(week)
csvfile.close()
print("=========================")
csvfile = file('proj3.csv','rb')
reader = csv.reader(csvfile)
name = set([])
for line in reader:
   [a,b] = line
   name.add(a)
personalCommit = []
for member in name:
   x = []
   csvfile.seek(0)
   for line in reader:
      [c,d] = line
      if c == member:
	x.append(int(float(d)))
   personalCommit.append(x)

t = []
csvfile.seek(0)
for line in reader:
   [a,b] = line
   t.append(int(float(b)))
t.sort()
total_week = (t[-1]-t[0])/(7*24*3600)
end = []
for i in range(total_week):
   end.append(t[0]+(i+1)*7*24*3600)

for t in personalCommit:
   week = []
   c = 0
   for x in t:
      if  x < end[0]:
         c += 1
   week.append(c)

   for alpha in range(1,total_week):
      c = 0
      for x in t:
         if x >= end[alpha-1] and x < end[alpha]:
             c+= 1
      week.append(c)
   print(week)
csvfile.close()
print("=========================")


