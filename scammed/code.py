import socket
v = ""
for num in range(0,9999+1):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("139.59.12.18", int("7676")))
	
	content = "83684"+str(num).zfill(4)+"0706910"
	print(content,end= " ")
	s.sendall(content.encode())
	s.shutdown(socket.SHUT_WR)
	while True:
	    data = s.recv(4096)
	    if not data:
	        break
	    if(repr(data)!=v):
	    	print(repr(data),end= " ")
	    	v = repr(data)
	    
	print()
	s.close()

#scammed dcrypt{cr3d1t_c4rd_sc4m}