def poorIssueDetector(totalIssue, notLabelIssue, notcloseIssue):
    if notcloseIssue > 0:
	return True
    if notLabelIssue > 0.2*totalIssue:
        return True
    return False

print(poorIssueDetector(20,10,0))
