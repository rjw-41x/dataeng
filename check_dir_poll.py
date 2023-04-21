from os import listdir
from os.path import isfile, join

poll_dir = '/Users/randywillard/Work/code/json+data/polling'

#function to return files in a directory
def fileInDirectory(my_dir: str):
    onlyfiles = [f for f in listdir(my_dir) if isfile(join(my_dir, f))]
    return(onlyfiles)
    
def prep_process_files( file_list ):
    pass
    # move files to process dir
    # write kafka message
    

if __name__ == "__main__":
    files_to_proc = fileInDirectory( poll_dir )
    if len( files_to_proc ) > 0:
        print( files_to_proc )
        

    '''
modules to write
process_files (should already have most of this)\
kafka reader
kafka writer

jenkins job??
    '''

    '''
what things should be in config files
-- bootstrap_servers
-- processing directories
-- target file names

    '''
