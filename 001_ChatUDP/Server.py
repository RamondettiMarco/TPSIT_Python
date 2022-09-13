from socket import socket, AF_INET, SOCK_DGRAM

BUFFER_SIZE = 1024
#tipo "bytes" -> array di byte
#codifica per esempio da str a bytes bisogna trasformarla in UNICODE esempio codifica utf8
HOST = '0.0.0.0'
#posso mettere: 127.0.0.1 -> localhost
#posso mettere: il mio indirizzo ip -> es. 192.168.95.141 -> solo sulla rete
#oppure 0.0.0.0 -> ascolta tutto
PORT = 5000 #basta che sia sopra 1024

def chatServer():
    with socket(AF_INET, SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        while True:
            msg = s.recvfrom(BUFFER_SIZE) #arriva un bytes quindi msg è di tipo bytes, 
                                          #bisogna decodificarlo per avere una str)
            msg = msg[0].decode('utf8')
            print(msg)
    
    

if __name__ == "__main__":
    chatServer()