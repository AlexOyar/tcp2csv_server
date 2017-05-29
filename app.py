import socket
import numpy as np
import csv

TCP_IP = '0.0.0.0'
TCP_PORT = 8888
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print ('Connection address:', addr)
#Read from socket and save values to numpy array and csv file
with open('names.csv', 'w', newline='') as csvfile:
    fieldnames =['F1','F2','F3','Ax','Ay','Az']
    writer = csv.DictWriter(csvfile, delimiter=',',
                        quotechar='h', quoting=csv.QUOTE_MINIMAL,fieldnames=fieldnames)
    #writer.writerow(['F1 ','F2 ','F3 ','Ax ','Ay ','Az '])
    writer.writeheader()
    while 1:
        data = conn.recv(BUFFER_SIZE)
        data = data.decode("utf-8")
        final = np.fromstring(data, sep=',')
        if not data: break
        if len(final) > 1:
            print ("received data:", final[0],final[1],final[2],final[3],final[4],final[5])
            writer.writerow({'F1':final[0],'F2':final[1],'F3':final[2],'Ax':final[3],'Ay':final[4],'Az':final[5],})
        #conn.send(data)  # echo
    conn.close()
