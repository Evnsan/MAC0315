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


class Erro_de_tipo(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Erro_de_consistencia(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

#-----------------------------------------------------------
class Vertice:
    def __init__(self, demanda):
        if(type(demanda) is int):
            self.demanda = demanda   
        else:
            msg = 'VERTICE - Tipo invalido para iniciar demanda, deve ser <type int> e recebeu '+ str(type(demanda))
            raise Erro_de_tipo(msg)
            
    def getDemanda(self):
            return self.demanda

    def __repr__(self):
        return 'Demanda: %d' % self.demanda
            
#-----------------------------------------------------------
class Grafo:
    def __init__(self, vertices):
        if(isinstance(vertices, list)):
            self.vetor = []
            i = 0
            for v in vertices:
                if(isinstance(v, Vertice)):
                    self.vetor.append(v)
                    i= i+1
                else:
                    msg = 'GRAFO - Tipo invalido para iniciar grafo, Vertice['+str(i)+'] deve ser <type Vertice> e recebeu '+ str(type(v))
                    raise Erro_de_tipo(msg) 
            self.nVertices = i        
        else:
            msg = 'GRAFO - Tipo invalido para iniciar grafo, vertice deve ser <type list> e recebeu ' + str(type(vertices))
            raise Erro_de_tipo(msg)
            
    def getVertice(self, n):
        if(type(n) is int):
            return self.vetor[n]
        else:
            msg = 'GRAFO - Tipo invalido para indice de verticedo grafo, n deve ser <type int> e recebeu ' + str(type(vertices))
            raise Erro_de_tipo(msg)

    def getNumVertices(self):
        return self.nVertices
        
    def __repr__(self):
        return '%d // %s' % (self.nVertices, self.vetor)
        
        
#-----------------------------------------------------------
class Arco:

    def __init__(self, inicio, final, custo, fluxo): # aninhar if's
             
        if(isinstance(inicio, int)):
            self.inicio = inicio 
        else:
            msg = 'ARCO - Tipo invalido para iniciar ponta inicial do arco, deve ser <type int> e recebeu '+ str(type(inicio))
            raise Erro_de_tipo(msg)
        
        if(isinstance(final, int)):
            self.final = final     
        else:
            msg = 'ARCO - Tipo invalido para iniciar ponta final do arco, deve ser <type int> e recebeu '+ str(type(final))
            raise Erro_de_tipo(msg)
            
        if(isinstance(custo, int)):
            self.custo = custo 
        else:
            msg = 'ARCO - Tipo invalido para iniciar custo do arco, deve ser <type int> e recebeu '+ str(type(custo))
            raise Erro_de_tipo(msg)
            
        if(isinstance(fluxo, int)):
            self.fluxo = fluxo    
        else:
            msg = 'ARCO - Tipo invalido para iniciar fluxo no arco, deve ser <type int> e recebeu '+ str(type(inicio))
            raise Erro_de_tipo(msg)
            
    def setFluxo(self, fluxo):
        if(isinstance(fluxo, int)):
            self.fluxo = fluxo    
        else:
            msg = 'ARCO - Tipo invalido para determinar fluxo no arco, deve ser <type int> e recebeu '+ str(type(inicio))
            raise Erro_de_tipo(msg)

    def getInicio(self):
        return self.inicio

    def getFinal(self):
        return self.final

    def getCusto(self):
        return self.custo
        
    def getFluxo(self):
        return self.fluxo

    def __repr__(self):
        return '%s --> %s (custo: %d |fluxo: %d)' % (self.inicio, self.final, self.custo, self.fluxo)
        
#-----------------------------------------------------------

class ArvoreGer:
    def __init__(self, numVertices):
        if(type(numVertices) is int):
            self.arvoreArc = [0] * numVertices
            self.parnt = [0] * numVertices
            self.raiz = None
            
    def setVertice(self, v, arc):
        if(type(v) is int and v < len(self.parnt)): # separar os erros
            if(isinstance(arc, Arco)):
                if( arc.getInicio() == v):
                            self.arvoreArc[v] = arc
                            self.parnt[v] = arc.getFinal()
                                
                elif(arc.getFinal() == v):
                            self.arvoreArc[v] = arc
                            self.parnt[v] = arc.getInicio()
                else:
                    msg = 'ARVOREGER - o vetor parnt deve receber arcos nos quais a ponta final ou inicial seja o indice v = ' + str(v) + ' e recebeu ' + str(arc)
                    raise Erro_de_consistencia(msg)
            else:
                msg = 'ARVOREGER - Tipo invalido para determinar arco do parnt['+str(v)+'], arc deve ser <type Arco> e recebeu ' + str(type(arc))
                raise Erro_de_tipo(msg)
        else:
            msg = 'ARVOREGER - Tipo invalido para determinar vertice do parnt[], vertice deve ser <type int> e recebeu ' + str(type(v))
            raise Erro_de_tipo(msg)
    
    
    # Este metodo devolve o rank do vartice informado. Def: rank da raiz = 0, o rank de
    # qualquer outro vertice e o rank do pai mais 1. Obs: usando tecnica de FIND
    def getRank(self, vertice):
        if(vertice < len(self.parnt)):
            rank = 0
            while( self.getParnt(vertice) != vertice):
                rank = rank + 1
                vertice = self.getParnt(vertice)
            return rank
        else:
            print 'erro'
            #erro
    
    # Este metodo devolve o pai do vertice informado. Def: pai da raiz e a propria raiz,
    # definido pelo arco que faz o loop raiz --> raiz.
    def getParnt(self, vertice):
        if(vertice < len(self.parnt)):
            return self.parnt[vertice]
        else:
            print 'erro'
            #erro
    
    # Este metodo devolve o arco utilizado para ligar o vertice informado ao pai deste na
    # arvore geradora.
    def getArc(self, vertice):
        if(vertice < len(self.parnt)):
            return self.arvoreArc[vertice]
        else:
            print 'erro'
            #erro
    
    # Este metodo devolve o potencial do vertice informado. Def: potencial da raiz = 0, o
    # potencial de qualquer outro vertice e o potencial do pai mais o custo do arco utili-
    # zado. Obs: usando tecnica de FIND
    def getY(self, vetice):
        if(vetice < len(self.parnt)):
            y = 0
            while(self.getParnt(vetice) != vetice):
                arc = self.arvoreArc[vetice]
                if(arc.getInicio() == vetice):
                    y = y - arc.getCusto()
                else:
                    y = y + arc.getCusto()
                vetice = self.getParnt(vetice)
            return y
        else:
            #erro
            print 'erro'
    
    # Metodo auxiliar que devolve o numero de vertices na arvore
    def getNumVertice(self):
        return len(self.parnt)
        
    # Metodo auxiliar que devolve a raiz da arvore
    def getRaiz(self):
        return self.raiz
        
    # Metodo auxiliar para definir a raiz da arvore
    def setRaiz(self, vertice):
        if(vertice < len(self.parnt)):
            self.raiz = vertice
            self.setVertice(vertice, Arco(vertice, vertice, 0, 0))

    # Metodo para retornar um limitante superior para o fluxo
    def getFluxoMaximo(self):
        maxFlux = 0
        for arc in self.arvoreArc:
            maxFlux = maxFlux + arc.getFluxo()
        return maxFlux
          
    
    def __repr__(self):
        retorno = self.arvoreArc[1::]
        return 'Arcos: %s' % (retorno)
