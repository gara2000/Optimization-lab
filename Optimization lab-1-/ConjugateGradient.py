#This function takes as input, the initial vector u0,
#and the tolerance r0
#This method also uses the arguments A and b characterizing
#a quadratic function: J(u) = 0.5*<A.u,u> - <b,u> + c
#this function has a gradient of : Grad(J)= A.u - b

def gradConjugue(u0, r0, A, b):
    max_iter = 10000000
    
    r1 = A.dot(u0)-b
    d1 = -r1
    
    for i in range(max_iter):
 
        pas = -r1.dot(d1)/A.dot(d1).dot(d1)
       
        u1 = u0 + pas * d1
        
        r2 = A.dot(u1)-b
        
        beta = linalg.norm(r2)**2/linalg.norm(r1)**2
        d1 = -r1+beta*d1
        
        
        err = linalg.norm(u1-u0)
        u0 = u1
        
        r1 = r2
        if err < r0 :
            break