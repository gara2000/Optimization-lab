#This function takes as input, the initial vector u0,
#the step rho and the tolerance r0, it also supposes 
#you have already the method calculating the gradient 
#of your target function

def gradPasFixe(u0 ,rho, r0):
        t0 = time()
        max_iter = 100000000
        for i in range(max_iter):

            d=-gradJ(u0)  #This should be defined before
            u1=u0+rho*d
            r=linalg.norm(u1-u0)
            u0 = u1

            if(r<r0):
                break

        t1 = time()
        return u0, i, t1-t0