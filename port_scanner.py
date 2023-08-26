import socket as s

def port_scanner(target_ip,port):
	sock=s.socket(s.AF_INET,s.SOCK_STREAM)
	sock.settimeout(1) #timeout the process
	result=sock.connect_ex((target_ip,port))
	sock.close()
	return result

def main():
	#target_ip and port input take form the user	
	target_ip = input("Enter the target IP address: ")
	start_port = int(input("Enter the starting port: "))
	end_port = int(input("Enter the ending port: "))

	print("-"* 50)	
	
	print(f"scaning ports{start_port} to {end_port} on  {target_ip} ....\n")
	
	print("-"*50)
	
	for port in range(start_port, end_port + 1):
		result=port_scanner(target_ip,port)
		if result ==0:
			print(f"port {port}is open")
		else:
			print(f"port{port}is Closed")

if __name__ =="__main__":
	main()
