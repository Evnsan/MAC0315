from SimplexRede import *
d = Simplex()
#from Grafo import *
a = ArvoreGer(5)

b = [Arco(0,0,0,0) , Arco(0,1,2,3) , Arco(0,2,3,3) , Arco(1,3,4,5) , Arco(2,4,5,6)]
c = [Arco(3,4,0,0)]

a.setVertice( 0, b[0])
a.setVertice( 1, b[1])
a.setVertice( 2, b[2])
a.setVertice( 3, b[3])
a.setVertice( 4, b[4])

print 'Rank'
print '0:' + str(a.getRank(0))
print '1:' + str(a.getRank(1))
print '2:' + str(a.getRank(2))
print '3:' + str(a.getRank(3))
print '4:' + str(a.getRank(4))
print
print 'Y'
print '0:' + str(a.getY(0))
print '1:' + str(a.getY(1))
print '2:' + str(a.getY(2))
print '3:' + str(a.getY(3))
print '4:' + str(a.getY(4))

print 'Num de vertices: ' + str(a.getNumVertice())
#c = [Vertice(3)]
#d.otmizar(2,3)
#d.otmizar(a,3)
#d.otmizar(a,[3])
arvore = d.otmizar(a,c)
print arvore
