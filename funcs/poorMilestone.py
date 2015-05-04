def poorMileStoneDetector(mileStoneDurations):
    if len(mileStoneDurations) < 5:
	return True
    if max(mileStoneDurations) > 21:
        return True
    return False

print(poorMileStoneDetector([20,10,0]))
