#!/usr/bin/python
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    Callback della classe socketserver
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(str(self.data.decode("utf-8")))
        
        #qui in self.data ho i dati trasmessi dal client
        #i dati sono una stringa di 151 valori separati da ;

        self.request.sendall(("Ricevuto: "+str(self.data)).encode())

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 8000

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        print("Attivo il server; sarà attivo finché non")
        print("interromperai il programma con Ctrl-C")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("server shutdown")
            exit()
