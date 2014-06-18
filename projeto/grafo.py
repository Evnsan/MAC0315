#! /bin/python

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
class vertice:
    def __init__(self, demanda):
        if(type(demanda) is int):
            self.demanda = demanda   
        else:
            msg = 'VERTICE - Tipo invalido para iniciar demanda, deve ser <type int> e recebeu '+ str(type(demanda))
            raise Erro_de_tipo(msg)
            
    def getDemanda(self):
            return self.demanda

    def __repr__(self):
        return '%d' % self.demanda
            
#-----------------------------------------------------------
class grafo:
    def __init__(self, vertices):
        if(isinstance(vertices, list)):
            self.vetor = []
            i = 0
            for v in vertices:
                if(isinstance(v, vertice)):
                    self.vetor.append(v)
                    i= i+1
                else:
                    msg = 'GRAFO - Tipo invalido para iniciar grafo, vertice['+str(i)+'] deve ser <type vertice> e recebeu '+ str(type(v))
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
class arco:

    def __init__(self, inicio, final, fluxo):
             
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

    def __repr__(self):
        return '%s ---- > %s (%d)' % (self.inicio, self.final, self.fluxo)
        
#-----------------------------------------------------------

class parnt:
    def __init__(self, numVertices):
        if(type(numVertices) is int):
            self.vetor = [0] * numVertices

    def setVerticeParnt(self, v, arc):
        if(type(v) is int):
            if(isinstance(arc, arco)):
                if( arc.getInicio() == v):
                            self.vetor[v] = arc
                elif(arc.getFinal() == v):
                            self.vetor[v] = arc
                else:
                    msg = 'PARNT - o vetor parnt deve receber arcos nos quais a ponta final ou inicial seja o indice v = ' + str(v)
                    raise Erro_de_consistencia(msg)
            else:
                msg = 'PARNT - Tipo invalido para determinar arco do vetor['+str(v)+'], arc deve ser <type arco> e recebeu ' + str(type(arc))
                raise Erro_de_tipo(msg)
        else:
            msg = 'PARNT - Tipo invalido para determinar vertice do vetor[], vertice deve ser <type int> e recebeu ' + str(type(v))
            raise Erro_de_tipo(msg)

    def __repr__(self):
        return '%s' % self.vetor
