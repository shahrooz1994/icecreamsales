def read(file_name):
    inputfile=open(file-name , "r")
    data_dict={}
    for line in inputfile:
        line=line.strip()
        line=line.split(":")
        data_dict[line[0]]=[line[1],line[2],line[3]]
        return data_dict
 

    



