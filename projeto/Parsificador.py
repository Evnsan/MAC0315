#! /bin/python


################################################################
#                                                              #
# Copyright 2014 MAC0315-PROJECT                               #
#                                                              #
# Licensed under the Apache License, Version 2.0               #
# (the "License"); you may not use this file except in         #
# compliance with the License. You may obtain a copy of the    #
# License at                                                   #
#                                                              #
# http://www.apache.org/licenses/LICENSE-2.0                   #
#                                                              #
# Unless required by applicable law or agreed to in writing,   #
# software distributed under the License is distributed on     #
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY    #
# KIND, either express or implied.                             #
# See the License for the specific language governing          #
# permissions and limitations under the License.               #
#                                                              #
################################################################

###
# Para cada execucao do metodo execParse('nome_do_arquivo_de_ent-
# rada') a classe parse retornara um objeto do tipo tokens com as
# informacoes do problema obtidas no arquivo de entrada.
# Esta classe pode ser considerada um sigleton
class parse:
    def __init__(self):
        t = 0
    # Remove comentarios e espacos em branco
    def preParse(self, line):
        line = line.split('\n')
        quebra = line[0].split('#', 1)
        valores = quebra[0].split(' ')
        valores = [x for x in valores if len(x) > 0]
        return valores
        
    # Para cada linha, configura o tonkem que sera devolvido com
    # as informacoes desta linha
    def tokenize(self, valores):
        if(len(valores) == 1):
            valor = self.toInt(valores[0])
            if(valor != None):
                if(self.t.getX() == 0):
                    self.t.setX(1)
                    self.t.setNumeroNos(valor)
                elif(self.t.getX() == 1):
                    self.t.setX(2)
                    self.t.setOrigem(valor)
                elif(self.t.getX() == 2):
                    self.t.setX(3)
                    self.t.setDestino(valor)
                elif(self.t.getX() == 3):
                    self.t.setX(4)
                    self.t.setProduto(valor)
                else:
                    print 'Ja foram avaliados os 4 tokens com apenas um numero, ignorando token: ' + str(valor)   
        elif(len(valores) == 3):
            val = [self.toInt(x) for x in valores if (self.toInt(x) != None)]
            if(len(val) == 3):
                self.t.addArcos(val)
        else:
            print 'Token invalido (numero incorreto de paramentros): ' + str(valores)
    
    def toInt(self, val):
        try:
            return int(val)
        except:
            print 'Token invalido (nao pode ser transformado em int): ' + str(val)

    # Recebe um nome de arquivo e tenta le-lo linha-a-linha para
    # chamar os metodos que criam o token
    # Retorna o tokem criado ao final
    def execParse(self, nomeFile):
        try:
            f = open(nomeFile , 'r')
            self.t = tokens()
            for line in f:
                val = self.preParse(line)
                if(len(val) > 0):
                    self.tokenize(val) 
            f.close()
            return self.t
        except IOError:
            print 'Arquivo de entrada \''+ str(nomeFile) +'\' nao encontrado.'


###
# Esta classe representa as informacoes obtidas no arquivo de
# entrada. Este arquivo deve conter 4 linhas com apenas um va-
# lor (Numero de no, No origem, No destino , Produto escoado),
# e linhas com tres valores significando um aresta (no-origem,
# no-destino, custo-aresta)
class tokens:
    def __init__(self):
        self.x = 0
        self.numeroNos = -1
        self.origem = -1
        self.destino = -1
        self.produto = -1
        self.listArcos = []

    def getX(self):
        return self.x
    def setX(self, valor):
        self.x = valor
     
    def getNumeroNos(self):
        return self.numeroNos
    def setNumeroNos(self, valor):
        self.numeroNos = valor

    def getOrigem(self):
        return self.origem
    def setOrigem(self, valor):
        self.origem = valor

    def getDestino(self):
        return self.destino
    def setDestino(self, valor):
        self.destino = valor
        
    def getProduto(self):
        return self.produto
    def setProduto(self, valor):
        self.produto = valor

    def getListArcos(self):
        return self.listArcos
    def addArcos(self, valor):
        self.listArcos.append(valor)
        
    def __repr__(self):
        msg = 'Numero de nos : '+str(self.numeroNos)+'\nNo origem: '+str(self.origem)+'\nNo destino: '+str(self.destino)+'\nProduto escoado : '+str(self.produto)+'\nArcos:\n'
        for arco in self.listArcos:
            msg = msg + str(arco) +' '
        return msg
        
