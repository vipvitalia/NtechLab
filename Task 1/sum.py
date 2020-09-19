def findMaxSubArray(string):
    #Обработка исключений на всякий случай
    string = str(string)
    array = []
    for i in range(len(string)):
        if (string[i].isdigit() == True and string[i - 1] == '-'):
            array.append(-int(string[i]))
        elif string[i].isdigit() == True:
            array.append(int(string[i]))

    first = array[0]
    sum = 0
    position = -1

    for i in range(len(array)):
        sum += array[i]
        if sum > first:
            first = sum
            left = position + 1
            right = i
        if sum < 0:
            sum = 0
            position = i
    return array[left:right+1]

print(findMaxSubArray([-2,1,-3,4,-1,2,1,-5,4]))