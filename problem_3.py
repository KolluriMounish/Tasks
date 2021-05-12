#TODO
#1.open log file (test.log), read its content
#2.write data into new file(output_file.txt)

import csv
from logging import debug

def parseData():
    with open('test.log') as log_file:
        debugList=[]
        warningList=[]
        lines = log_file.read().splitlines()
        for line in lines:
            linesList=line.split(',')
            if linesList[1].__contains__("ERROR"):
                debugList.append(line)
            elif linesList[1].__contains__("WARNING"):
                warningList.append(line)
    
    with open('output_file.txt', "w+") as file:
        file.write("Errors & Warnings Records:\n")
        
        for item0 in debugList:
            print(item0)
            file.write(item0+"\n")
        for item1 in warningList:
            print(item1)
            file.write(item1+"\n")
    file.close()
parseData()

# def parseData(log_file_path, export_file, regex, read_line=True):
#     with open(log_file_path, "r") as file:
#         match_list = []
#         if read_line == True:
#             for line in file:
#                 for match in re.finditer(regex, line, re.S):
#                     match_text = match.group()
#                     match_list.append(match_text)
#                     print match_text
#         else:
#             data = file.read()
#             for match in re.finditer(regex, data, re.S):
#                 match_text = match.group();
#                 match_list.append(match_text)
#     file.close()
 
#     with open(export_file, "w+") as file:
#         file.write("EXPORTED DATA:\n")
#         match_list_clean = list(set(match_list))
#         for item in xrange(0, len(match_list_clean)):
#             print match_list_clean[item]
#             file.write(match_list_clean[item] + "\n")
#     file.close()

# parseData('test.log','Outputfile.txt',)