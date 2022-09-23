#!/usr/bin/env python3
#This file use for creat own server
import socket
import time

#define address & buffer size
#host leave blank because host is own machine
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    # open a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3  
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)
        
        #continuously listen for any connections by any clients
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            
            #recieve data, wait a bit, then send it back
            full_data = conn.recv(BUFFER_SIZE)
            # sleep for make sure receive every thing
            time.sleep(0.5)
            conn.sendall(full_data)
            conn.close()

if __name__ == "__main__":
    main()
