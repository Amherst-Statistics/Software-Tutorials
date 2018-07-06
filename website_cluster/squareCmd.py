#! /usr/local/bin/python3
import os, math

# Create file references for this project:
projectName = 'square'
executable = projectName + '.R'
baseDirectory = os.getcwd()
commandPathname = baseDirectory + '/' + projectName + '.cmd'

# Write the general parameters needed for all jobs in the project: 
commands = open(commandPathname, 'w')
commands.writelines(['## Global job properties\n',
	'universe =     vanilla\n',
	'notification = error\n',
	'notify_user  = szablah20@amherst.edu\n',
	'getenv =       true\n',
	'initialdir =   ' + baseDirectory + '\n',
	'executable =   ' + executable + '\n',
	'requirements = (((Arch=="INTEL") || (Arch=="x86_64")) && (OpSys=="LINUX"))\n',
	'priority =     5\n'])

# Create the results directory and make it writable:
baseResultsDirectory = baseDirectory + '/results'
if not os.path.exists(baseResultsDirectory) : os.mkdir(baseResultsDirectory, 0o700)

# Job arguments
betaValues = range(100) 
jobsCount = len(betaValues)

# Create a format string that will produce results directory names that 
# have a standard length for sorting purposes, e.g. 'results/%02d'
#  => 'results/00','results/01', ..., 'results/09', 'results/10', ...
resultsDirectoryFormat = baseResultsDirectory + '/%0' + \
                       str(math.floor(math.log10(jobsCount-1))+1) + 'd'
# Loop through the parameters to be passed for each job:
for job in range(jobsCount) :

    # Create the results directory for this specific job.
    resultsDirectory = resultsDirectoryFormat % job
    if not os.path.exists(resultsDirectory) : os.mkdir(resultsDirectory, 0o700)

    # Write the arguments for this job.
    commands.writelines(['\n## Job properties\n',
    	'arguments = ' + str(betaValues[job]) + '\n',
    	'output = ' + resultsDirectory + '/out\n',
    	'error = ' + resultsDirectory + '/err\n',
    	'log = ' + resultsDirectory + '/log\n',
    	'queue\n'])

commands.close()
