def estimate():
    pi=0
    for n in range (1000):
        pi +=(((-1)**n)*(1/((2*n)+1))) *4
        print (pi)
    

estimate()
        
        
