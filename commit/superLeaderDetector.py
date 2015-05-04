def detectSuperLeader(weeklyCommit, totalCommit):
   if sum(weeklyCommit) > totalCommit*0.3:
       return True
   return False
