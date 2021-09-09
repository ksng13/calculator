def check_sequence(array1):
    def check_sequence_array(array,i):
        if array[i]==array[i+2]-1:
            newchar=array[i+1]+array[i+3]
            array[i]='@'
            array[i+1]='@'
            array[i+3]=newchar

    for i in range(0,len(array1)-2,2):
        check_sequence_array(array1,i)
    newarray=[]
    count=0
    for i in range(0,len(array1),2):
        if array1[i+1]!='@':
            newarray.append(count)
            count+=1
            newarray.append(array1[i+1])

    return newarray
