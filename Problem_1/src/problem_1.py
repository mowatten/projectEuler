# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "thomas"
__date__ = "$18.mar.2015 17:28:22$"

#START

import time

if __name__ == "__main__":
    start = time.time()
    
    resultat = sum(set(range(0,1000,3))|set(range(0,1000,5)))

    tid = time.time() - start
    
    print("result %s returned in %s seconds" % (resultat,tid))
    
#END      

#1 2 3 4 5 6 7 8 9
#    3   5 6     9

#1*3 = 3
#2*3 = 6
#3*3 = 9
#5*1 = 5
