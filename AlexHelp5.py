class AlexHelp: 

    def _sum(arrays):
 
    # initialize a variable
    # to store the sum
    # while iterating through
    # the array later
        sum = 0

    # iterate through the array
    # and add each element to the sum variable
    # one at a time
        for i in arrays:
            sum = sum + i
        return(sum)
    
    students = 4    
    arrays = [88, 22, 55, 99, 44, 77, 33, 88,100]
    lenOfArray = len(arrays)
    sumOfArrays = _sum(arrays)
    average = sumOfArrays / lenOfArray
    print("Mr McCall has " + str(lenOfArray) + " students in his class and from the last test taken " 
    + " The class average is " + str(average ))