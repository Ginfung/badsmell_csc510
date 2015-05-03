## 0.Important note:  
- This repo is trying to detect the bad smells during the develop process of project 1, csc 505, 15spring, ncsu  
- All of the project names and members have been subsitituted by the numbers, due to the privacy consideration  
- Contact: Jianfeng Chen (jchen37@ncsu.edu)

## 1.Collection
This section will introduce how to collect the data or records during the developing process. I will collect three basic types of data-- issues, commits and milestones.  

All of the collection codes are modified from [gitable.py](https://gist.github.com/timm/a87fff1d8f0210372f26). Github token is required when applying the github API. In this repo, my token has been hiden.

### Collecting Issues
Issues are a great way to keep track of tasks, enhancements, and bugs for the projects. Through it, we can detect or predict some bad smells. To collect the issues for a project, we can put the dump https://api.github.com/repos/org_name/repo_name/issues/events and them parse the return JSON. For example, I want to get the issues for my own project, I should use the dump https://api.github.com/repos/smartSE/constraintAnalysis/issues/events.  

If it is successful, I can get all the information about the issues, tagged as "id", "url", "html_url", "state", "title", "body", "user", "label", "milestone", "comments", etc.  

This report will discuss how to parse these information in the following section.

### Collection Milestones
Typically the developer set a milestone correspond to a project, feature, or time period. Consequently, milestone is an important information in analysing the bad smell.

Similar to collecting the issues, one can fetch the milestones by using the Github API link: https://api.github.com/repos/org_name/repo_name/milestones . Again, take my own project as an example, the dump for extracting my project milestone should be https://api.github.com/repos/smartSE/constraintAnalysis/milestones?state=all. The state here can be all/closed/ open(default). 

The information for a single milestone including "id", "url", "creator", "title", "description", "create_at", "closed_at", etc.

### Collecting Commits
There are several commits in a project. Through tracking the commits, we can detect or predict many bad smells.
 Similar to the former two collection, we should use the link https://api.github.com/repos/org_name/repo_name/commits . For example, to get the commits for my own project 1, I should use https://api.github.com/repos/smartSE/constraintAnalysis/commits.

Many parameters can be attached to the url so that we can find more precise result, see the [github api document](https://developer.github.com/v3/repos/commits/).

Common information for a commit includes "url", "author", "committer", "parents", etc. 

## 2.Anonymization
The main purpose for this repo is to find the bad smells for others, which are widely existed in our own development process. Thus it is the conclusion that matters. All of the names will be hidden to protect the privacy. That is, developers are called "D1", "D2", "D3"; groups are called "G1", "G2", "G3".

I defined a mapping method to substitute the real names. It was simply applying "str.replace(s1,s2)". Obviously, this function is not published in this repo--it contains the mapping relationship.

## 3.Tables
All of the results are stored in different spreadsheets. These spreadsheets are in CSV format, which is easily written by format and analyzed by EXCEL. All of the figures in this repo were created by MS Excel. 

## 4.Data
The following table shows how much data I collected for the later analysis.

|No|Feature|G1|G2|G3|
|------|-------|--------------|--------------|--------------|
|1|Commit Record|510|182|170|
|2|s|s|s|s|

## 5.Data Samples

**1.Commit record**

|Committer|Commit time(epoch secs)|
|---------|-----------------------|
|M0|1428442378|
|M1|1428267799|

The actual collected data can be found here:  
* [project1](http://commit/proj1.csv)
* [project2](http://commit/proj2.csv)
* [project3](http://commit/proj3.csv)

The commit record mainly focuses on the commit history during the development of software. It contains the committer, commit time.


## 6.PART I. Feature Detection and Results

**1.Commit distribution for the whole team
The commit distribution can be fetched through the dataset 1(commit record). At this time, I ignore the committer. Since all of the times are represented by the epoch seconds in dataset1. Modification for these time is needed. I need to count the total number of weekly commits. The statistic method is as follows. Detail code can be found [here](http://getCommitDis)

```python
csvfile = file('proj2.csv','rb')
reader = csv.reader(csvfile)
t = []
for line in reader:
   [a,b] = line
   t.append(int(float(b)))
t.sort()
week = []
total_week = (t[-1]-t[0])/(7*24*3600)
end = []
for i in range(total_week):
   end.append(t[0]+(i+1)*7*24*3600)

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
```

RESULT:  
The following figures shows the result for the commit distribution of these groups.
![](./commit/R_commit_dis_g1.PNG)
![](./commit/R_commit_dis_g2.PNG)
![](./commit/R_commit_dis_g2.PNG)

**2.Commit for a single person

## 7.PARTII. Bad Smells Detection and Results

## 10.Early Warning

## 11.Early Warning Results
