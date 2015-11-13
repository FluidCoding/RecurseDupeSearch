'''
RecursiveDuplicateSearch
Created on Aug 24, 2011
@author: Brian Sonnie
'''
import os, hashlib

'''
Recursively searches for duplicate files in a directory
param _dir the directory path to search
param _withsubdir flag to destermine depth of search
param _dupesmap
'''
def searchDuplicate(_dir, _withsubdir, _dupesmap):
    print("Searching " + _dir + "...")
    # Gather files and folders
    files = os.listdir(_dir)
    # Iterate through files
    for item in files:
        file = os.path.join(_dir, item)
        if os.path.isfile(file):
            # Calculate MD5 Hash
            md5sum = hashlib.md5(open(file,'rb').read()).hexdigest()
            # Check if hash exists in table
            listedelement = dupesmap.get(md5sum, None)
            if listedelement == None:
                _dupesmap[md5sum] = file
            else:
                print("\nDuplicate Found!")
                ans = input("Choose an action: \n1) Delete " + file + "\nSize: " + str(os.path.getsize(file)) + "\n2) Delete " + listedelement + "\nSize: " + str(os.path.getsize(listedelement)) + "\n3) Keep both\n")
                if(ans=="1"):
                    os.remove(file)
                elif(ans=="2"):
                    os.remove(listedelement)
                    dupesmap[md5sum] = file
        elif _withsubdir:
            searchDuplicate(os.path.join(_dir, item), _withsubdir, _dupesmap)
        
# Collect Initial Parameters
start_dir = input("Enter the directory to search: ")
dupesmap = {}
searchDuplicate(start_dir, True, dupesmap)
print("Done!!")