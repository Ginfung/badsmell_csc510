# Important note:  
- This repo is trying to detect the bad smells during the develop process of project 1, csc 505, 15spring, ncsu  
- All of the project names and members have been subsitituted by the numbers, due to the privacy consideration  
- Contact: Jianfeng Chen (jchen37@ncsu.edu)

## 1.Collection
This section will introduce how to collect the data or records during the developing process. I will collect three basic types of data-- issues, commits and milestones.  

All of the collection codes are modified from [gitable.py](https://gist.github.com/timm/a87fff1d8f0210372f26). Github token is required when applying the github API. In this repo, my token has been hiden.

### Collecting Issues
Issues are a great way to keep track of tasks, enhancements, and bugs for the projects. Through it, we can detect or predict some bad smells. To collect the issues for a project, we can put the dump https://api.github.com/repos/org_name/repo_name/issues/events and them parse the return JSON. For example, I want to get the issues for my own project, I should use the dump https://api.github.com/repos/smartSE/constraintAnalysis/issues/events.  

If it is success, I can get all the information about the issues, tagged as "id", "url", "html_url", "state", "title", "body", "user", "label", "milestone", "comments", etc.  

This report will discuss how to parse these information in the following section.

### Collection Milestones
Typically the developer set a milestone correspond to a project, feature, or time period. Consequently, milestone is an important information in analyzing the bad smell.

Similiar to collectingthe issues, one can fetch the milestones by using the Github API link: https://api.github.com/repos/org_name/repo_name/milestones . Again, take my own project as an example, the dump for extracting my project milestone should be https://api.github.com/repos/smartSE/constraintAnalysis/milestones?state=all. The state here can be all/closed/ open(default). 

The information for a single milestone including "id", "url", "creator", "title", "discription", "create_at", "closed_at", etc.

## 2.Anonymization

## 3.Tables

## 4.Data


