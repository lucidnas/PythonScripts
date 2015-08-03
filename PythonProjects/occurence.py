def occurrences(a_list, an_element):
    counter = 0
    for i in range (len(a_list)):
	    if an_element == i:
	    	print i
	    	counter += 1
    return counter