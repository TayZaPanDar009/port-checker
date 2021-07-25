import socket
from colorama import init,Fore,Back

#color
init()
red = Fore.RED
black = Back.BLACK
green = Fore.GREEN
default = Back.RESET


#banner
banner = f"""{red}
    ____              ____            
   / __ \____ _____  / __ \____ ______
  / /_/ / __ `/ __ \/ / / / __ `/ ___/
 / ____/ /_/ / / / / /_/ / /_/ / /    
/_/    \__,_/_/ /_/_____/\__,_/_/     
                                      
"""
print(f'{red}='*40)
print(banner)
print(f'{green}='*40)


host = input(f"{red}Enter your Target Host :: {green}")

i = True
while(i==True):
    try:
        if (1==1):
            global s
            s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            global port 
            port = int(input(f"{red}Enter your target port : {green}"))
            connection = s.connect_ex((host,port))
            if (connection == 0 ):
                print("The port "+str(port),"is open")
            else:
                print("connection Failed!")
        else:
            i = False
            break
    except Exception as e:
        print(f"{black}+"+"="*40+f"+{default}")
        print("Incurret port !")