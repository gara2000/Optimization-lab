#This method is used to minimize a real numeric funtion
#It's used to calculate the optimal step of the gradient method.
#Input: -[a, b] is the interval on which we want to minimize f
#		-u and d are parameters used to calculate the function f 
#		(for the porpose of this lab only, the first argument is the actual variable of the function)
#		-r0 is the tolerance
#		-f is the function we want to minimize

def sectionDoree(a, b, u, d, r0, f):
    
    max_iter = 100000
    
    phi = (1+5**0.5)/2
    for i in range(max_iter):
        aprime = a + (b-a) / phi**2
        bprime = a + (b-a) / phi
        fa = f(a, u, d)
        fb = f(b, u, d)

        if fa > fb:
            a = aprime
        elif fa<fb:
            b = bprime
        else:
            a = aprime
            b = bprime
            
        err = b-a
        if(err<r0):
            break
    return a

#This function takes as input, the initial vector u0,
#and the tolerance r0
#It also supposes you already have the method calculating the gradient 
#of your target function

def gradPasOptimal(u0, r0):
        max_iter = 100000000
        t0 = time()
        for i in range(max_iter):
            d = -gradJ(u0)  #This should be defined before
            pas = sectionDoree(-10000, 10000, u0, d, 0.001, f)
            u1 = u0 + pas * d
            err = linalg.norm(u1-u0)
            u0 = u1
            if err < r0 :
                break
        t1 = time()
        return u0, i, t1-t0