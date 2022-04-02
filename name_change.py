
def alter(old_str,new_str):
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str,new_str)
            file_data += line
    with open(file,"w",encoding="utf-8") as f:
        f.write(file_data)

import os
import argparse
import time

# get para
parser = argparse.ArgumentParser()
parser.add_argument("path" , type = str)
parser.add_argument("old_text" , type = str)
parser.add_argument("new_text" , type = str)
args = parser.parse_args()

# args.path = "D:/python_project/name_change/demo_batch_namechange/batch/";
# args.old_text = "OLDPROJECT";
# args.new_text = "NEWPROJECT";
path = args.path;
old = args.old_text;
new = args.new_text;
# path = "D:/python_project/name_change/demo_batch_namechange/batch/"
# old = "OLDPROJECT"
# new = "NEWPROJECT"

# open every file and alter it
dirs = os.listdir( path )
for file in dirs:
        if file[len(file)-3:len(file)] == "txt":
                if file.find(new) == 0 :
                        print(1)
                        file = path + file
                        print(file)
                        print(old)
                        print(new)
                        alter(old , new)
