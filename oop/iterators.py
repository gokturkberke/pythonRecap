#iterable
#iterators

sayilar = [1,2,3,4,5]

#for i in sayilar:
#    print(i) #iterable cunku list
    
#a=20

#for i in a:
#    print(i) #iterable degil cunku integer error verir

iterator = iter(sayilar)   #iter() fonksiyonu ile iterable bir objeyi iterator objeye cevirebiliriz
#print(next(iterator)) #=1 next() fonksiyonu ile iterator objenin elemanlarini tek tek alabiliriz
#print(next(iterator)) #2

while True:
    try:
        sayi = next(iterator)
        print(sayi)
    except StopIteration:
        break
#-----------------------------------------------------
class Counter:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop
        
    def __iter__(self): #iter fonk ile iterator yapariz
        return self
    
    def __next__(self): #next fonk ile sayac yapariz
        if self.start <= self.stop:
            x=self.start
            self.start += 1
            return x
        else:
            raise StopIteration
        
#for i in Counter(1,10):
 #   print(i)
 
while True:
     try:
         print(next(Counter(1,10)))
     except StopIteration:
         break
        