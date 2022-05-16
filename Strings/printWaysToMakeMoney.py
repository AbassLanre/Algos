bills = [100,50,20,10,5,1]

def print_all_ways(sumSoFar,minBill, changeSoFar):
    for i in range(minBill, len(bills)):
        change = changeSoFar
        sum = sumSoFar
        
        while sum >0 :
            if (change != "") :
                change +=" + "
            change += str(bills[i])
            sum -= bills[i]
            if(sum > 0):
                print_all_ways(sum, i+1, change)
        if (sum ==0):
            print(change)


print_all_ways(30,5,"")