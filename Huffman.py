import numpy as np;
import heapq
import math

#class for node in tree for Huffman coding
class Node:
      #constructor
      def __init__(self,data,freq):#data-character-V[i], freq-frequency of caracter
           self.left=None;
           self.right=None;
           self.data=data;
           self.freq=freq;

      def set_left(self, left):
          self.left=left;

      def set_right(self, right):
          self.right=right;
      # overload of operator <
      def __lt__(self, other):
          return (self.freq<other.freq);

#make tree for Huffman coding
def form_tree(freq,value):

    pq=[];
    map = [0 for i in range(0,len(value))];
    #making priority queue
    for i in range(0,len(freq)):
        z=Node(i,freq[i])
        heapq.heappush(pq, z )


    for i in range(0,len(freq)-1):
        x=heapq.heappop(pq)
        y=heapq.heappop(pq)
        # making subtree
        z=Node(-1,x.freq+y.freq);
        z.set_left(x);
        z.set_right(y);

        heapq.heappush(pq,z)

    tree=heapq.heappop(pq)

    form_codes(tree,map,"")
    #print(map)
    return (tree,map)

#go through tree and read codes
def form_codes(tree,map,code):
       if(tree.left == None and tree.right == None):
                map[tree.data]=code;
       else:
           form_codes(tree.left,map,code+"0");
           form_codes(tree.right,map,code+"1");

def m_ary(value,V,m):
    #S-sum of levels, F-frequencies
    S=F=np.zeros((m-1,1))
    sum=0

    #calculate sums
    for i in reversed(range (1,m)):
        S[i-1]=sum+value[i]
        sum=S[i-1]
        i=i+1
    #print (S)

    #discretization
    for i in range(0,Nsim):
        if(V[i]<S[m-2]):V[i]=m-1
        if(V[i]>S[0]): V[i]=0
        for j in range (0,m-2):
            if(V[i]<S[j] and V[i]>S[j+1]):V[i]=j+1
            j=j+1
        i=i+1
    #print (V)

    F=np.zeros((m,1)).tolist()
    for i in range(0,m):
        F[i]=V.count(i)
        i=i+1
    #print(F)
    return (F,V)



def binary(P0,P1):

    #discretization
    for i in range(0,Nsim):
         if(V[i][0]<P0):
              V[i]=0
         else:
              V[i]=1
    #calculate frequencies
    F=np.zeros((2,1)).tolist()
    F[0]=V.count(0);
    F[1]=Nsim-F[0]

    return(F,V)

#forming sentence
def code(V,map):
    ans=""
    for i in range(0,len(V)):
        ans+=map[V[i]]
    return ans

#decoding sentence written in code
def decode(root,code):

    ans=[]
    curr = root;
    for i in range(0,len(code)):
        if (code[i] == '0'):
           curr = curr.left;
        else:
           curr = curr.right;

        if (curr.left==None and curr.right==None):
            ans.append(curr.data);
            curr = root;

    #print(ans)
    return ans

#calculating entropy given probabilities
def entropy(value,m):

    E=0
    for i in range (0,m):
        E=E+value[i]*math.log(1/value[i])/math.log(2)
        i=i+1
    return(E)

#calculating redundance given efficiency
def redudance(Eff):

    R=1-(Eff/100.0)

    return(R)

#calculating average length given probabilities, length and map of Huffman codes
def average_length(value,m,map):

    L=0
    for i in range (0,m):
        L=L+value[i]*len(map[i])
        i=i+1
    return(L)

#calculating efficiency given entropy E and average length L
def efficiency(E,L):

    Eff=0
    Eff=E*100/L
    return(Eff)

#calculating compression given average length
def compressy(L):

    C=0
    C=3/L
    return(C)

#making map of probabilities for Nth extension  of binary coding given (N-1)th map of probabilities
def make_next_map(prev_value,p0,p1):
    value1=[element* p0 for element in prev_value]
    value2=[element* p1 for element in prev_value]
    return value1+value2;
def make_new_V(V,N,m):
    i=0;
    new_V=[];
    limit=math.floor(len(V)/N)*N;
    #print(limit)
    while(i<limit):
        val=0
        for j in range(i,i+N):
            #print(j)
            val=(val<<1)+V[j];
        new_V.append(val);
        i=i+N;
    F=np.zeros((m,1)).tolist()
    for i in range(0,m):
        F[i]=new_V.count(i)
        i=i+1
    return (new_V,F)
'''
# ispis za m-arni prenos

Nsim=10000
V=np.random.rand(Nsim,1).tolist()
sifra=['a','b','c','d','e','f']
#value=[0.45,0.35,0.1,0.05,0.03,0.02]
value=[0.5,0.25,0.125,0.0625,0.03125,0.03125]

m=6
F,V=m_ary(value,V,m)
print('Verovatnoce za slucaj M=6 kod prvog izvora:')
print(value)
print('Dobijene frekvencije su:')
print(F)
print('Kada frekvencije pretvorimo u verovatnoce dobije se:')
print([element/10000 for element in F])
tree,map=form_tree(F,value)
print('Huffmanov kod je')

for i in range(0,m):
      print(sifra[i]+':'+map[i])

E=entropy(value,m)
print('Entropija je:')
print(E)
L=average_length(value,m,map)
print('Srednja duzina kodne reci je:')
print(L)
print('Efikasnost je:')
Eff=efficiency(E,L)
print(Eff)
print('Redundansa je:')
R=redudance(Eff)
print(R)
print('Kompresija je:')
C=compressy(L)
print(C)

#ispis za binarni prenos
'''
'''
Nsim=10000
P0=0.15
P1=0.85

#P0=0.35
#P1=0.65

V=np.random.rand(Nsim,1).tolist()
sifra=['a','b','c','d','e','f']
value=[P0,P1]
m=2
F,V=binary(P0,P1)
print('Verovatnoce za slucaj binarnog prenosa kod drugog izvora')
print(value)
print('Dobijene frekvencije su:')
print(F)
print('Kada frekvencije pretvorimo u verovatnoce dobije se:')
print([element/10000 for element in F])
tree,map=form_tree(F,value)
print('Huffmanov kod je')

for i in range(0,m):
      print(sifra[i]+':'+map[i])

E=entropy(value,m)
print('Entropija je:')
print(E)
L=average_length(value,m,map)
print('Srednja duzina kodne reci je:')
print(L)
print('Efikasnost je:')
Eff=efficiency(E,L)
print(Eff)
print('Redundansa je:')
R=redudance(Eff)
print(R)
print('Kompresija je:')
C=compressy(L)
print(C)

#prosirenje izvora
'''
'''

m=4
N=2
Nsim=10000
P0=0.15
P1=0.85
V=np.random.rand(Nsim,1).tolist()
sifra=['a','b','c','d','e','f']
F,V=binary(P0,P1)
prev_value=[P0,P1]
tree,map=form_tree(F,prev_value)
#print(map)
E=entropy(prev_value,2)
#print(E)
L=average_length(prev_value,2,map)
#print(L)
eff=efficiency(E,L)
print(eff)



while(eff<90 ):
       value=make_next_map(prev_value,P0,P1)
       #print(value);
       new_V,new_F=make_new_V(V,N,m)
       tree,map=form_tree(new_F,value)
       #print(map)
       #print(map)
       E=entropy(value,m)
       #print(E)
       L=average_length(value,m,map)
       #print(L)
       eff=efficiency(E,L)
       print("Efikasnost za N= "+str(N)+" je: ")
       print(eff)
       prev_value=value;
       #print(N)
       m=m*2
       N=N+1
print('Za prosirenje reda '+str(N-1)+':')
print("Entropija je: "+str(E))
print("Srednja duzina kodne reci je: "+str(L))
print("Efikasnost je: "+str(eff))
print("Redudansa je: "+str(redudance(eff)))
print("Stepen kompresije je: "+str(compressy(L)))
'''

def error_change(V,n):
    Nsim=len(V)
    Greska=np.random.rand(1,Nsim).tolist()[0]
    broj_gresaka=[0,0];
    for i in range(0,len(Greska)):
        if(Greska[i]<=0.04):
           pom=V[i];

           for j in range(0,n):
               broj_gresaka[pom%2]=broj_gresaka[pom%2]+1;
               pom>>1;

           V[i]=(2**n-1)-V[i];
    return (broj_gresaka[0],broj_gresaka[1])

Nsim=10000
P0=0.15
P1=0.85
V=np.random.rand(Nsim,1).tolist()
sifra=['a','b']
value=[P0,P1]
m=4
red=2
F,V=binary(P0,P1)

value=make_next_map(value,P0,P1)
new_V,new_F=make_new_V(V,red,m)
(n_0_pogresno,n_1_pogresno)=error_change(new_V,red)
print("Kod drugog prosirenja prvog binarnog izvora javlja se:")
print(str(n_0_pogresno)+" pogresnih nula")
print(str(n_1_pogresno)+" pogresnih jedinica")

'''
Nsim=10
V=np.random.rand(Nsim,1).tolist()
sifra=['a','b','c','d','e','f']
value=[0.45,0.35,0.1,0.05,0.03,0.02]
#value=[0.5,0.25,0.125,0.0625,0.03125, 0.03125]

m=6
F,V=m_ary(value,V,m)
print(V)
print('Verovatnoce za slucaj M=6 kod prvog izvora:')
print(value)
print('Dobijene frekvencije su:')
print(F)
print('Kada frekvencije pretvorimo u verovatnoce dobije se:')
print([element/10000 for element in F])
tree,map=form_tree(F,value)
print('Huffmanov kod je')

for i in range(0,m):
      print(sifra[i]+':'+map[i])
code=code(V,map)
print(code)
decode=decode(tree,code)
print(decode)
'''
