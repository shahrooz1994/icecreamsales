def main():
    data_dict = read("icecream.txt")
    dum_taste_dict = sum_taste(data_dict)

def read(file_name):
    inputfile=open(file_name, "r")
    data_dict={}
    for line in inputfile:
        line=line.strip()
        line=line.split(":")
        data_dict[line[0]]=[line[1],line[2],line[3]]
        return data_dict
    
def sum_taste(data_dict):
    sum_taste_dict={}
    for key in data_dict:
        lst=data_dict[key]
        taste_sum=sum(lst)
        sum_taste_dict[key]=taste_sum
    return sum_taste_dict

 

    



