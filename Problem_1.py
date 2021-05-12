#Implement a group_by_owners function that:
# ·         Accepts a dictionary containing the file owner name for each file name.
# ·         Returns a dictionary containing a list of file names for each owner name, in any order.
def group_by_owners(file_owner_dictionary):
    keys = [key for key, value in file_owner_dictionary.items()]
    values = [value for key, value in file_owner_dictionary.items()]
    owner_file_dictionary = {}
    for v in values:
        temp=[]
        for k in keys:
            if file_owner_dictionary[k] == v:
                temp.append(k)
        owner_file_dictionary[v]=temp  
    return owner_file_dictionary

    
input_dictionary = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
result = group_by_owners(input_dictionary)
print(result)
