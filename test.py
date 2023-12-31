def main():
    (data_dict,store1,store2,store3) = read("icecream.txt")
    sum_taste_dict = sum_taste(data_dict)
    result_print(sum_taste_dict,data_dict,store1,store2,store3)
    

def read(file_name):
    inputfile=open(file_name, "r")
    data_dict={}
    store1 = []
    store2 = []
    store3 = []
    for line in inputfile:
        line=line.strip()
        line=line.split(":")
        data_dict[line[0]]=[float(line[1]),float(line[2]),float(line[3])]
        store1.append(float(line[1]))
        store2.append(float(line[2]))
        store3.append(float(line[3]))

    return data_dict , store1 , store2 , store3
    
def sum_taste(data_dict):
    sum_taste_dict={}
    for key in data_dict:
        lst=data_dict[key]
        taste_sum=sum(lst)
        sum_taste_dict[key]=taste_sum
    return sum_taste_dict

#def branch_sum():



def result_print(sum_taste_dict,data_dict,store1,store2,store3):
    for key in sorted(data_dict):
        lst=data_dict[key]
        taste_sum=sum_taste_dict[key]
        print("%-20s %-10s %-10s %-10s %-20s" %(key,lst[0],lst[1],lst[2],taste_sum) )
    print("%-20s %-10s %-10s %-10s" %("",sum(store1),sum(store2),sum(store3)))

main()


 

    



