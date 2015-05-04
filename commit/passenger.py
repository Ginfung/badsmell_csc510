def isPassenger(weekCommit, totalCommit):
    if sum(weekCommit) < totalCommit * 0.2:
        print("Low commit proportion. Possible passenger!")
	return True
    c = 0
    for i in weekCommit:
       if i == 0:
           c += 1
    if c >=2:
        print("Zero weekly commit warning. Possible Passenger!")
        return True
    print("High commit proportion. Not passenger")
    reture False
