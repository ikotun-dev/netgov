import socket
import threading
import time
  
# function to scan ports and see which ports are open
def scan_port(port):
    # we will check port of localhost
    host = "localhost"
    host_ip = socket.gethostbyname(host)
      
    # print("host_ip = {}".format(host_ip))
    status = False
  
    # create instance of socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
    # connecting the host ip address and port
    try:
        s.connect((host_ip, port))
        status = True
    except:
        status = False
  
    if status:
        print("port {} is open".format(port))
  
  
start_time = time.time()
  
for i in range(0, 100000):
    thread = threading.Thread(target=scan_port, args=[i])
    thread.start()
  
end_time = time.time()
print("To all scan all ports it took {} seconds".format(end_time-start_time))