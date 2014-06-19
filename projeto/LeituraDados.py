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


class Parse:
    def __init__(self):
        self.x = 0
        self.numeroNos = -1
        self.origem = -1
        self.destino = -1
        self.produto = -1
        self.listArcos = []
    
    def __repr__(self):
        msg = 'Numero de nos : '+str(self.numeroNos)+'\nNo origem: '+str(self.origem)+'\nNo destino: '+str(self.destino)+'\nProduto escoado : '+str(self.produto)+'\nArcos:\n'
        for arco in self.listArcos:
            msg = msg + str(arco) +' '
        return msg
        
    def preParse(self, line):
        line = line.split('\n')
        quebra = line[0].split('#', 1)
        #if(len(quebra) > 1):
        #   msg = 'comentario ignorado:  #' + quebra[1]
        #   print msg
        #print quebra[0]
        valores = quebra[0].split(' ')
        valores = [x for x in valores if len(x) > 0]
        return valores
    
    def tokenize(self, valores):
        if(len(valores) == 1):
            valor = self.toInt(valores[0])
            if(valor):
                if(self.x == 0):
                    self.x = 1
                    self.numeroNos = valor
                elif(self.x == 1):
                    self.x = 2
                    self.origem = valor
                elif(self.x == 2):
                    self.x = 3
                    self.destino = valor
                elif(self.x == 3):
                    self.x = 4
                    self.produto = valor
                else:
                    print 'Ja foram avaliados os 4 tokens com apenas um numero, ignorando token: ' + str(valor)   
        elif(len(valores) == 3):
            val = [self.toInt(x) for x in valores if self.toInt(x)]
            if(len(val) == 3):
                self.listArcos.append(val)
        else:
            print 'Token invalido (numero incorreto de paramentros): ' + str(valores)
    
    def toInt(self, val):
        try:
            return int(val)
        except:
            print 'Token invalido (nao pode ser tranformado em int): ' + str(val)

try:
    f = open('problema.dat', 'r')
    p = Parse()
    for line in f:
        val = p.preParse(line)
        if(len(val) > 0):
            p.tokenize(val) 
    print p
    f.close()
except IOError:
    print 'Arquivo de entrada \'problema.dat\' nao encontrado.'
