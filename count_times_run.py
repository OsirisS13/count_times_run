"""Count the number of times a script has been run, and calculate man hours saved
function arguments input name of file, number of minutes each task would take to do manually (whole minutes only)
"""
from shutil import copy2
from time import sleep
import linecache
import os

def get_previous_values(filename):
    """Read lines 2 and 4 from file and return values or zero if empty."""
    try:
        with open(filename) as f:
            lines = f.readlines()
    except IOError:
        return 0, 0
    # print '=' * 80
    # for index, line in enumerate(lines):
        # print index, line.rstrip()
    # print '=' * 80
    timesrun = lines[1]
    timesrun = int(timesrun) if timesrun else 0
    timesavedminutes = lines[3]
    timesavedminutes = int(timesavedminutes) if timesavedminutes else 0
    return timesrun, timesavedminutes
# def get_previous_values(filename):
    # #read from line 2 of given file
    # # timesrun = linecache.getline(filename, 2)
	# filename = open(filename, 'r+')
	# print filename.read().splitlines()
	# timesrun = filename.read().splitlines()[1]
	# print timesrun
    # # if nothing in file set timesrun to 0 otherwise convert to int
	# timesrun = int(timesrun) if timesrun else 0
	# #read from line 4 of given file
	# timesavedminutes = filename.read().splitlines()[3]
	# print timesavedminutes
	# # timesavedminutes = linecache.getline(filename, 4)
	# # if nothing in file set to 0
	# timesavedminutes = int(timesavedminutes) if timesavedminutes else 0
	# files.close()
	# return timesrun, timesavedminutes

def save_values(filename, timesrun, timesavedminutes, hoursmins):
    """Save values to file."""
    with open(filename,'w') as f:
        f.write("Number of times run:\n")
        f.write(timesrun)
        f.write("Time Saved (minutes):\n")
        f.write(timesavedminutes)
        f.write("Time Saved (hours:minutes):\n")
        f.write(hoursmins)
		
#convert to hours mins format
def convert_minutes_to_hours_minutes(timesavedminutes): 
	hoursmins = '{:02d}:{:02d}'.format(*divmod(timesavedminutes, 60))
	hoursmins = str(hoursmins)
	return hoursmins

def addtimesrun(filename, tasktime):
    timesrun, timesavedminutes = get_previous_values(filename)
    # print timesrun, timesavedminutes
    timesrun = timesrun + 1
    timesavedminutes = timesavedminutes + tasktime
    # print timesavedminutes
    hoursmins = convert_minutes_to_hours_minutes(timesavedminutes)
    # print hoursmins
    timesrun = str(timesrun) + '\n'
    timesavedminutes = str(timesavedminutes) + '\n'    
    save_values(filename, timesrun, timesavedminutes, hoursmins)

#this tests if this python file is run by itself, or if it is imported into another module
#this is a module that gets imported elsewhere, so when you import the module, ` __name__ ` would evaluate to `modulename`
# but if you directly run the code, rather than import it,  ` __name__ ` evaluates to `__main__`, and so the if would be tru and would run that code
# so basically, by directly running the module it would test itself, but by importing it, it would not run that block of code
if __name__ == '__main__':
    for i in range(10):
        print 'Starting test run number:', i
        addtimesrun('test',2)
        print 'Completed Run number:', i
        print '=' * 80
