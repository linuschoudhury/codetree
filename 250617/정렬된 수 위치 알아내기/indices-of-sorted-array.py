n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.

indexed_sequence=list(enumerate(sequence))
#print(indexed_sequence)
sorted_sequence=sorted(indexed_sequence,key=lambda x:x[1])
#print(sorted_sequence)
rank=1
ranks=[0]*n
for item in sorted_sequence:
    #print(item[0])
    original_index=item[0]
    ranks[original_index]=rank
    rank+=1
for rank in ranks:
    print(rank,end=' ')


    