from math import sqrt
import json
import sys

arg = sys.argv[1]
path_dir = sys.argv[2]

clus = eval(open("{0}/center_{1}.txt".format(path_dir, arg)).read())
vector = eval(open("{0}/input_vector_with_name_{1}.txt".format(path_dir, arg)).read())

def cos_sim(a, b):
    """Takes 2 vectors a, b and returns the cosine similarity according
    to the definition of the dot product
	"""
    dot_product = 0
    norm_a = 0
    norm_b = 0
    for x in range(0,len(a)):
        dot_product += float(a[x])*float(b[x])
        norm_a += float(a[x])**2
        norm_b += float(b[x])**2
    #print dot_product
    #print norm_a
    #print norm_b

    norm_a = sqrt(norm_a)
    norm_b = sqrt(norm_b)

    #dot_product = np.dot(a, b)
	#norm_a = np.linalg.norm(a)
	#norm_b = np.linalg.norm(b)
    return dot_product / (norm_a * norm_b)

#print clus
#print clus["clus"]
#print clus["length"]
#print clus["cen"]
result = {}

#print vector[0]
#print len(clus['clus'])
for x in range (0,clus["length"]):
#for x in range(0,1):
    result[x] = []
    #print clus["clus"][x]
    #print len(clus["clus"][x])
    for y in range(0,len(clus["clus"][x])):
        #print clus["clus"][x][y]
        result[x].append(vector[clus["clus"][x][y]])

#print result


final_result = {}
for k, v in result.iteritems():
    #print k, v
    #print len(v)
    final_result[k] = {}
    for x in range(0, len(v)):
        #print v[x]
        print v[x][0:12]
        score =  cos_sim(clus["cen"][k],v[x][0:12])
        final_result[k][v[x][-1]] = score
    final_result[k] = sorted(final_result[k].items(), key=lambda x:x[1],reverse=True)


#print final_result
with open("{0}/class/class_{1}.json".format(path_dir, arg), 'w') as outfile:
     json.dump(final_result, outfile, sort_keys = True, indent = 4,
               encoding='utf8')
'''
print len(final_result)
print len(final_result[0])
print final_result[0][1]
'''


'''
for k ,v in final_result.iteritems():
    print "k = ", k
    for x in range(0,len(v)):
        print v[x]
    print '\n'
'''
'''
a={'a':1,'b':30, 'c': 5,'d':-10}
a = sorted(a.items(), key=lambda x:x[1])
print a
'''
