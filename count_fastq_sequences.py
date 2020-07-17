import sys
import operator

# each key is a sequence, the value for which is the number of times it has been found in the fastq
count_dict = {}

# first argument is the path to the fastq file
infile = open(sys.argv[2],"r")
inlines = infile.readlines()
infile.close()

# parse every 2nd line in the fastq file, starting at line 1
for seq in inlines[1::2]:
    if seq.strip("\n") in count_dict:
        count_dict[seq.strip("\n")] += 1
    else:
        count_dict[seq.strip("\n")] = 1

# create a sorted list of key, value pairs (sequences at end of list are most freuquent)
sorted_count_dict = sorted(count_dict.items(), key=operator.itemgetter(1))

# print the top 10 most frequent sequences and the number of times they were counted
for tup in sorted_count_dict[-10:]:
    print "{}, {},{}\n".format(sys.argv[1], tup[0], tup[1])
