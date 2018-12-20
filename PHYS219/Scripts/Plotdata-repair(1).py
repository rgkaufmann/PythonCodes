#Created on July 7, 2016  15:10:33
#@author: Evan and Rob 
############################################################
#
# comments are typcially used to explain the following line of code
#
############################################################

# import the  library numpy  and rename it  np
import numpy as np
# import the library matplotlib   and rename it plot
import matplotlib.pyplot as plt
#name  the input file  with the data  that is broken
fname = 'C:/Users/ryank/Desktop/Work/Classes/Python/PHYS219/Experiment 4/LowFrequencyLowAmpNoOffsetTest.csv'

#############################################################
# Try to repair input file.
#############################################################
# Set system specific EOL. Shouldn't be needed.
numcolumns = 2
import platform
if platform.system()=="Windows":
	eol="\r\n"
else:
	eol="\n"
import string
instream=open(fname, mode='rtU') #Read text in universal EOL mode.
#Make a new file to put fixed data so we don't clobber original.
fixedfile=fname.rstrip(".csv")+".fixed.csv"
outstream=open(fixedfile, mode='wt')
#Define junk to try to strip off of data (everything but numbers).
junk=(string.ascii_letters+string.punctuation+string.whitespace)
#Don't clobber minus signs and decimal points on front of numbers.
frontjunk=junk.replace("-.","")
for index,line in enumerate(instream.readlines()):
	#Strip of EOLs and split off any comment.
	current = line.rstrip().split("#")
	#Look at comma separated stuff before comment. (Should be numbers.)
	numbers=current.pop(0).strip(",").split(",")
	#Strip non-number stuff from those entries. (Fix spurious characters.)
	numbers=[number.rstrip(junk).lstrip(frontjunk) for number in numbers]
	#Reassemble everything after fixing.
	current.insert(0,",".join(numbers[0:numcolumns]))
	current = "#".join(current)
	#See if what should be numbers are actually numbers.
	try:
		for number in numbers:
			float(number)
		outstream.writelines(current+eol) #It worked. Keep the fixed line.
	except Exception:	#Line was too broken. Comment it out.
		outstream.writelines("#"+line.rstrip().lstrip("#")+eol)
		print("corrupt data at line: "+str(index))
instream.close()
outstream.close()
#Use new fixed file.
fname=fixedfile
#############################################################
# End of file repair hackery.
#############################################################

# read in data - the file is assumed to be in csv format (comma separated variables). 
#Files need to be specified with a full path OR they have to be saved in the same folder 
#as the script
data = np.loadtxt(fname, delimiter=',',comments='#' )
# access the data columns and assign variables x and y
#generate  an array  x  which is the first  column  of  data.  Note the first column is 
#indexed as  zero.
x = data[:,0]
#generate  an array  y  which is the second  column  of  data  (index  1)
y = data[:,1]
#note the data is not copied during this process - x,y are 'pointing' to the same 
#memory as data
#define the uncertainty in y. 
sigmay=0.005
# plot the data
plt.errorbar(x, y,yerr=sigmay,marker='o',linestyle='')
## marker='o' : use markers to indicate each data point (x_1,y_1),(x_2,y_2)
## linestyle= '' : no line is drawn to connect the data points
## linestyle= '-' : a line is drawn to connect the data points

# add axis labels
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('Op Amp Circuit Test without Distortion')
# this next command makes  sure the plot is shown. 
plt.show()
# ----- you can save a figure by right-clicking on the graph in the console
# ----- alternatively use: plt.savefig("NAMEOFFIGURE")
