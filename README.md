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
|1|Commit distribution|12|12|12|
|2|Comments for commit|1|1|1|
|3|Super leader|1|1|1|
|4|Passenger|1|1|1|
|5|No responded issue|1|1|1|
|6|Issue creator distribution|1|1|1|
|7|Issue creation time distribution|1|1|1|
|8|Issue Labels|1|1|1|
|9|Unassigned issue|1|1|1|
|10|Label with serial number|1|1|1|
|11|Overdue milestones|1|1|1|
|12|Late-defined milestones|1|1|1|
|13|Overlap milestones|1|1|1|

## 5.Data Samples

## 6.Feature Detection

## 7.Feature Detection Results

## 8.Bad Smells Detector

## 9.Early Warning

## 10.Early Warning Results
