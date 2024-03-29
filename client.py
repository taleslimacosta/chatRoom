# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Thread com execucao paralela
#

# importacao das bibliotecas
import threading # threads
import time # tempo (opcional)
from socket import *
from termcolor import colored
from functions import *

# define uma classe para a criacao de threads
class myThread (threading.Thread):
    # redefine a funcao __init__ para aceitar a passagem parametros de entrada
    def __init__(self, username, serverName, serverPort, clientSocket):
        threading.Thread.__init__(self)
        self.username = username
        self.serverName = serverName
        self.serverPort = serverPort
        self.clientSocket = clientSocket

    # a funcao run() e executada por padrao por cada thread
    def run(self):
        while True:
            status = self.clientSocket.recv(1024).decode('utf-8')
            if(len(status)!=0):
                if(status[0]=='1'):
                    if(status[1:] != self.username):
                        print(colored(status[1:], 'green'), "entrou na sala")
                    else:
                        print(colored("você", 'green'), "entrou na sala")
                elif(status[0]=='2'):
                    if(status[1:] != self.username):
                        print(colored(status[1:], 'red'), "saiu da sala")
                    else:
                        print(colored("você", 'green'), "saiu na sala")
                status=[]
                print(len(status))

            mensagem = input("Digite: ")
            print(mensagem)
            if(mensagem[0:7] == 'sair()'):
                comando = mensagem[0:7]
                dados = mensagem[mensagem.find(')')+1:]
            elif(mensagem.find("privado(*)")) == 0:
                comando = mensagem[0:mensagem.find(')')]
                dados = mensagem[mensagem.find(')')+1:]
            elif(mensagem[0:8] == 'lista()'):
                comando = mensagem[0:8]
                dados = mensagem[mensagem.find(')')+1:]
            else:
                comando = "mensagem()"
                dados = mensagem[:]

            #print(dados)
            tam = len(dados)
            #print(tam)
            #print(len(comando))
            protocolo = protocoloComunicacao(tam, self.username, comando, dados )
            clientSocket.send(protocolo.encode('utf-8'))

            #print(comunicacao)
