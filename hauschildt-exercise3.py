from helpers import getNum

def getRainfallData():
	result = [] 
	months = ["March", "April", "May", "June"]
	for i in range(len(months)):
		question = "Enter " + months[i] + "'s rainfall total: "
		result.append(getNum(question, 0.0, 100.0))
	return result

def getSum(rainfallData):
    sum = 0
    for value in rainfallData:
        sum += value
    return sum

def getAverage(sum, count):
    return sum / count

def main():
    rainfall = getRainfallData()
    total = getSum(rainfall)
    average = getAverage(total, len(rainfall))
    print("Total: " + str(total))
    print("Average: " + str(average))
    print("Highest: " + str(max(rainfall)))
    print("Lowest: " + str(min(rainfall)))
  # STEP 16: Print the total, average, highest, and lowest amounts
  
main()