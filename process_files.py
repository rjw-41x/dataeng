import sys, os, glob
import pandas as pd

paths = []
# get and validate directory
for val in sys.argv:
# for val in ['/Users/randywillard/Work/code/json+data/finance-data-professional-salary-survey/data','/Users/randywillard/Work/code/json+data/']:
    if os.path.isdir( val ):
        paths.append(val)
        
if len( paths) == 0:
    print("No valid directories provided, aborting")
    sys.exit(1)
    
files_to_proc = []

for pth in paths:
    # print("Files in " + pth)
    # for fil in os.listdir(pth, suffix='csv'):
    for fil in glob.glob( pth + '/' + 'salary_survey*.csv'):
        files_to_proc.append( fil )


out_df = pd.DataFrame()
for f in files_to_proc:
    # print( f )
    proc_df = pd.read_csv( f, header=1 )
    out_df = pd.concat( [out_df, proc_df], axis=0 )

print( 'the combined file is ' + str(len( out_df )) + ' lines long' )
