def poorTimeManageDetector(overdue, totalIssue):
   if overdue/totalIssue > 0.15:
       return True
   else:
       return False


print(poorTimeManageDetector(2,19))

