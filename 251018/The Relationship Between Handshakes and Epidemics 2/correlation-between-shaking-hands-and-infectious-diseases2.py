N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

# Please write your code here.
handshakes.sort(key=lambda x:x[0])
infected=[]
infected.append(P)
k=[0]*(N+1)
for i in range(T):
    if handshakes[i][1] in infected and k[handshakes[i][1]]<K:
        infected.append(handshakes[i][2])
        k[handshakes[i][1]]+=1
        #print(handshakes[i][1])
    elif handshakes[i][2] in infected and k[handshakes[i][2]]<K:
        infected.append(handshakes[i][1])
        k[handshakes[i][2]]+=1
        #print(handshakes[i][2])

answer=[0]*N
for i in range(N):
    if i+1 in infected:
        print(1,end='')
    else:
        print(0,end='')