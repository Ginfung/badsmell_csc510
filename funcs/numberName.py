def numberLabelDetector(labels):
    for label in labels:
        if label[0] >= '0' and label[0] <= '9':
             continue
	else:
             return False
    return True

