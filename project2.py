# Darnell Chen - Section 2

# Imports CovidSFPlot, which will create a graph using the output file
import CovidSFPlot as plot

# 3 constants
# One has a list of input files
# One contains the string for the output path
# One holds a constant that defines the number of days in a week
FILE_PATH_INPUT = ['us-counties.csv', 'us-counties-2021.csv', 'us-counties-2022.csv']
FILE_PATH_OUTPUT = 'D:/CS110/covid-SF.csv'
WINDOW = 7

# Defines function main
def main():
    # loops through the length of the input list
    for x in range(0, len(FILE_PATH_INPUT)):
        # Calls function fReadInputFile, which its argument being a value in the list and puts return into a variable
        # Calls function fWriteOutputFile - using the returned list from fReadInputFile as an argument
        returned_list = fReadInputFile(FILE_PATH_INPUT[x])
        fWriteOutputFile(returned_list)
    # calls fReadOutputFile, which will go through the argument and copy all the daily cases into a string
    daily_case_list = fReadOutputFile(FILE_PATH_OUTPUT)
    # Calls fCalcMovAvg, which will return a list of 7-day moving average
    moveAvg = fCalcMovAvg(daily_case_list)
    # Uses the moving average list to write a new column in the output file
    fWriteCovidSFFile(FILE_PATH_OUTPUT, moveAvg)
    plot.fPlotSFCovid(FILE_PATH_OUTPUT)




# Defines function fReadInputFile which will take the parameter (a file), and loop through it to find daily cases
def fReadInputFile(pFileName):
    # places the string 'San Francisco' in a variable, to be searched later
    string = 'San Francisco'
    # opens the input file in read mode using the parameter
    file = open("C:/Users/reald/Desktop/Project2/covid-19-data-master/" + str(pFileName), 'r')
    # Initiates a first_list, which will hold the dates and daily cases
    first_list = [[],[]]
    # Initiates a return string, which will hold the list being returned
    returned_list = []
    # loops through the file
    for line in file:
        # Initiates a comma count, 2 strings, 2 lists
        comma_count = 0
        string_date = ''
        string_case = ''
        case_list = []
        date_list = []
        # Checks if the string San Francisco is in the line
        if string in line:
            # Loops through every character in the line
            for char in line:
                # checks if the character is a comma, if it is, then it adds one to the comma count
                if char == ',':
                    comma_count += 1
                # checks if the comma count is 0, if it is:
                # the character will be added to a string that will hold the date
                elif comma_count == 0:
                    string_date += char
                # checks if the comma count is 4, if it is:
                # adds the character to the string holding the daily count
                elif comma_count == 4:
                    string_case += char
            # appends the strings into a nested list
            first_list[0].append(string_date)
            first_list[1].append(string_case)
    else:
        # just a placeholder
        placeholder = 'placeholder'
    # Closes the file
    file.close()
    # Initiates a list, which will hold the daily cases
    daily_case_list = []
    # initiates an empty string which will hold the value which is going to be subtracted by the next value
    current = ''
    # loops through the values in the first list of the nested list which holds the dates
    for value in first_list[1]:
        # Checks if the current variable is blank
        # if the variable is empty, it will assign the current value to the variable
        if current == '':
            current = float(value)
        else:
            # find the difference in daily case by subtracting the current number from the previous
            # the previous is poorly named "current"
            daily_case = float(value) - float(current)
            # checks if the difference is over 2000, if it is, only 2000 is appended to the list of daily cases
            if daily_case > 2000:
                daily_case_list.append(str(2000))
                current = value
            elif daily_case <= 2000:
                daily_case_list.append(str(daily_case))
                current = float(value)
    # for the list of dates, we will splice it the nested list holding the dates and cases
    # we will slice the list holding the dates as the list of daily cases won't include the first day
    daily_date_list = first_list[0][1:]
    # appends the date and daily case list to the nested list
    returned_list.append(daily_date_list)
    returned_list.append(daily_case_list)
    # returns the list
    return returned_list




# defines function fWriteOutputFile, which will take the list made from fReadInputFile
# and writes it into a csv file
def fWriteOutputFile(pList):
    # Opens the output file in append mode
    file = open(FILE_PATH_OUTPUT, 'a')
    # loops for the length of pList[0], which is one of the nested lists. Both nested lists are of the same length.
    for x in range(len(pList[0])):
        # writes the date, adds a comma, and the daily cases. Then writes the line break.
        file.write(pList[0][x])
        file.write(',')
        file.write(pList[1][x])
        file.write('\n')
    # closes file
    file.close()

# Defines fReadOutputFile, which will make a list using what was stored in the output file
def fReadOutputFile(pLocation):
    # Opens the output file in read mode
    file = open(pLocation, 'r')
    # Reads every line and stores it in the variable 'copied_file'
    copied_file = file.readlines()
    # initiates a list
    daily_list = []
    # loops through the copied file and splits the lines using the comma
    for line in copied_file:
        # intiates a count and a string.
        # the string will hold the appended case number
        # the count will count how many times a comma occurs
        comma_count = 0
        case_string = ''
        # strips the line of '\n'
        line = line.rstrip()
        # loops through every character in the line
        for char in line:
            # checks if the character is comma, if it is, a adds one to the comma count
            if char == ',':
                comma_count += 1
            # checks if the comma count is 1. if it is, then the string character will be added to the string
            elif comma_count == 1:
                case_string += char
        # the string will be appended to the list
        daily_list.append(case_string)
    # the daily list is returned
    return daily_list




# Initiates a function that will find the 7-day moving average using the daily case list
def fCalcMovAvg(pList):
    # Initiates a new list that will hold the moving average
    movAvg = []
    # A variable that will keep count of the sum in a week
    week_sum = 0
    # creates a loop for the length of the list
    for x in range(len(pList)):
        # checks if x is less than or equal to 6, then appends a 0 to the list if it is
        if x <= 6:
            movAvg.append(0)
        elif x > 6:
            # adds a the next term to the week_sum
            # appends the moving average to the list
            # subtracts the 7-terms ago value
            week_sum += float(pList[x])
            movAvg.append(week_sum / WINDOW)
            week_sum -= float(pList[x - WINDOW])
    # Returns moving Average
    # returns the list of moving average
    return movAvg




#
def fWriteCovidSFFile(pFile, pList):
    # opens the file in read mode
    file = open(pFile, 'r')
    # initiates an empty list
    copied_list = []
    # initiates a count, which will be used to keep track of the index of the moving average list
    count = 0
    # loops through the file
    for line in file:
        # strips the \n off the end of the line
        line = line.rstrip()
        # concatenates a line that will hold both the current line and the moving average
        line = str(line) + ',' + str(pList[count])
        # adds a count to move the moving average index up
        count += 1
        # appends the line to a list
        copied_list.append(line)
    # closes the file
    file.close()
    # opens the file in write mode
    file = open(pFile, 'w')
    # goes through every string in the list
    for string in copied_list:
        # writes the string, then adds a line break
        file.write(string)
        file.write('\n')
    # closes the file
    file.close()

# calls main
main()