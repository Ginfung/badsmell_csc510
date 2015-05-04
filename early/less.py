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

					 
def totalSubmitatTime(time,commitRate):
    s = 0
	for record in commitRate:
	    [index, timepoint, commits] = record
		if timpoint == time:
		    s += 1
	return s

def realtiveLess(timestamp, commitRate, text_index)
    c = 0
    for time in range(timestamp):
        for record in commitRate:
		    [index, timepoint, commits] = record
			if timepint == time and index == text_index and commits / totalSubmitatTime(time,commitRate) < 0.2
			   c += 1
	return c

