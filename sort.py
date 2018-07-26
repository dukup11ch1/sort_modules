def quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    
    p = x[0]
    i = 0
    for j in range(len(x)-1):
        if x[j+1] < p:
            x[j+1],x[i+1] = x[i+1], x[j+1]
            i += 1
    x[0],x[i] = x[i],x[0]
    first = quicksort(x[:i])
    second = quicksort(x[i+1:])
    first.append(x[i])
    return first + second

def bubble_sort(x):
    for start_index in range( len(x)-1 ):
        for index in range( 1, len(x) - start_index ):
            if x[index-1] > x[index]:
                x[index-1],x[index]=x[index],x[index-1]
    return x
#made by dukup11ch1
#sort module