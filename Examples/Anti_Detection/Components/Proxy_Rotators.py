"""
Pick A Random Proxy Using Math Example (Not Fully Random)
"""

#Import Random Functionality
import random

#Make A Function When Called Returns A Proxy
def PickProxy():
  
    #Make A Var That Equals All The Proxies In The `proxies.txt` File
    Proxies = open("proxies.txt", "r").read().splitlines()
    
    #Make A Var That Is Equal To A Random Proxy
    Proxy = random.choice(Proxies)
    
    #Return The Proxy
    return Proxy

#Set Var Equal To Our Proxy Function
Proxy = PickProxy()

"""
END
"""

"""
Rotate Proxy Instead Of Picking At Random
"""

#Coming Soon
