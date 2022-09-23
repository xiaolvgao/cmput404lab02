#!/usr/bin/env python3
#This file use for creat own server
import socket
import time

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024


#get host information
def get_remote_ip(host):
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname( host )
    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
        sys.exit()

    print (f'Ip address of {host} is {remote_ip}')
    return remote_ip


def main():

    proxy_host = 'www.google.com'
    proxy_port = 80

    # open proxy_start
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
        proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        proxy_start.bind((HOST, PORT))
        proxy_start.listen(2)
    
        #continuously listen for any connections by any clients
        while True:
            conn, addr = proxy_start.accept()
            print("Connected by", addr)
            
            # open proxy_end
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                print("Connecting to Google")

                # get the ip, and connect
                remote_ip = get_remote_ip(proxy_host)
                proxy_end.connect((remote_ip , proxy_port))
                print (f'Socket Connected to {proxy_host} on ip {remote_ip}')

                # send the data and shutdown the connection
                full_data = conn.recv(BUFFER_SIZE)
                print(f"Sending recieved data {full_data} to google")
                proxy_end.sendall(full_data)
                proxy_end.shutdown(socket.SHUT_WR)

                data = proxy_end.recv(BUFFER_SIZE)
                print(f"Sending recieved data {data} to client")
                conn.send(data)


            
            #recieve data, wait a bit, then send it back
            # full_data = conn.recv(BUFFER_SIZE)
            # # sleep for make sure receive every thing
            # time.sleep(0.5)
            # conn.sendall(full_data)
            conn.close()

if __name__ == "__main__":
    main()
