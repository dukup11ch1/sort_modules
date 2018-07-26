import sort
import sys


if not sys.argv[1:]:
    print "Usage : python sort.py argv1 argv2 ..."
    exit()
for a in range(len(sys.argv[1:])):
    try:
        sys.argv[a+1]=int(sys.argv[a+1])
    except:
        print "input error"
        exit()

print "quicksort"
print sort.quicksort(sys.argv[1:])
print "\nbubblesort"
print sort.bubble_sort(sys.argv[1:])

    
