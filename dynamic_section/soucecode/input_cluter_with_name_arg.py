import sys
arg = sys.argv[1]
path_dir = sys.argv[2]

dict1 = eval(open('{0}/json/dict1_{1}.json'.format(path_dir, arg)).read())
dict2 = eval(open('{0}/json/dict2_{1}.json'.format(path_dir, arg)).read())
dict3 = eval(open('{0}/json/dict3_{1}.json'.format(path_dir, arg)).read())
dict4 = eval(open('{0}/json/dict4_{1}.json'.format(path_dir, arg)).read())



total_dict = {}
totla_dict = total_dict.update(dict1)
totla_dict = total_dict.update(dict2)
totla_dict = total_dict.update(dict3)
totla_dict = total_dict.update(dict4)



count = 0

print '{'
for k, v in total_dict.iteritems():
    #print count
    #print k
    '''
    print total_dict[k]
    print total_dict[k]['word_in_title']
    print total_dict[k]['content_type']
    print total_dict[k]['content_length']
    print total_dict[k]['Number_of_word']
    print total_dict[k]['Number_of_picture']
    print total_dict[k]['Number_of_table']
    print total_dict[k]['Number_of_slash_in_URL_path']
    print total_dict[k]['binary_vector'][0]
    print total_dict[k]['binary_vector'][1]
    print total_dict[k]['binary_vector'][2]
    print total_dict[k]['binary_vector'][3]
    print total_dict[k]['binary_vector'][4]
    print total_dict[k]['binary_vector'][5]
    print total_dict[k]['binary_vector'][6]
    print total_dict[k]['binary_vector'][7]
    print total_dict[k]['binary_vector'][8]
    print total_dict[k]['binary_vector'][9]
    print total_dict[k]['URL_Length']
    print total_dict[k]['Number_of_outgoing']
    print total_dict[k]['Numer_of_webpage_in_the_same_site']
    '''
    print  count,':',[ total_dict[k]['word_in_title'],total_dict[k]['content_type'], total_dict[k]['content_length'] ,total_dict[k]['Number_of_word'],total_dict[k]['Number_of_picture'],total_dict[k]['Number_of_table'],total_dict[k]['Number_of_slash_in_URL_path'],total_dict[k]['binary_vector'],total_dict[k]['URL_Length'],total_dict[k]['Number_of_word_in_URL'],total_dict[k]['Number_of_outgoing'],total_dict[k]['Numer_of_webpage_in_the_same_site'],total_dict[k]['Number_of_line_in_content'],count,k],","


    count += 1
print '}'

count = 0
with open("{0}/class/id_vector_with_URL_{1}.txt".format(path_dir, arg) , 'w') as out:
    out.write("{")
    for k,v in total_dict.items():
        out.write("\"")
        out.write(str(k))
        out.write("\"")
        out.write(":")
        a = [ total_dict[k]['word_in_title'],total_dict[k]['content_type'], total_dict[k]['content_length'] ,total_dict[k]['Number_of_word'],total_dict[k]['Number_of_picture'],total_dict[k]['Number_of_table'],total_dict[k]['Number_of_slash_in_URL_path'],total_dict[k]['binary_vector'],total_dict[k]['URL_Length'],total_dict[k]['Number_of_word_in_URL'],total_dict[k]['Number_of_outgoing'],total_dict[k]['Numer_of_webpage_in_the_same_site'],total_dict[k]['Number_of_line_in_content']]
        out.write(str(a))
        out.write(",")
        out.write('\n')
        count += 1
    out.write("}")
