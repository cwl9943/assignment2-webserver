# import socket module
from socket import *
# In order to terminate the program
import sys

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    
    #Prepare a server socket
    serverSocket.bind(("127.0.0.1", port))
  
    #Fill in start
    serverSocket.listen(1)
    #Fill in end

    while True:
        #Establish the connection
    
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
    
        try:
            message = connectionSocket.recv(1024).decode()
            filename = message.split()[1]
      
            #opens the client requested file. 
            #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
        
            with open(filename[1:], 'rb') as f:
                outputdata = f.read()
      
            #fill in end
      
            #This variable can store the headers you want to send for any valid or invalid request.   What header should be sent for a response that is ok?    
            #Fill in start 
              
            #Content-Type is an example on how to send a header as bytes. There are more!
            headers = "HTTP/1.1 200 OK\r\n"
            headers += "Content-Type: text/html; charset=UTF-8\r\n"
            headers += "Server: Python/3.x\r\n"
            headers += "Connection: close\r\n\r\n"
                
            response = headers.encode() + outputdata
            connectionSocket.send(response)            
            #Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html
        
            connectionSocket.close() #closing the connection socket
      
        except Exception as e:
            connectionSocket.send(b"HTTP/1.1 404 File Not Found\r\n\r\n")
            # Send response message for invalid request due to the file not being found (404)
            # Remember the format you used in the try: block!
            #Fill in start
            connectionSocket.close()
      #Fill in end


      #Close client socket
      #Fill in start

      #Fill in end

  # Commenting out the below (some use it for local testing). It is not required for Gradescope, and some students have moved it erroneously in the While loop. 
  # DO NOT PLACE ANYWHERE ELSE AND DO NOT UNCOMMENT WHEN SUBMITTING, YOU ARE GONNA HAVE A BAD TIME
  #serverSocket.close()
  #sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
