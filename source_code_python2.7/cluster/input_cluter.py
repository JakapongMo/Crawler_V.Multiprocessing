dict1 = eval(open("/home/tengmo/crawler_to_server_set_time/crawler/result/json/dict1").read())
dict2 = eval(open("/home/tengmo/crawler_to_server_set_time/crawler/result/json/dict2").read())
dict3 = eval(open("/home/tengmo/crawler_to_server_set_time/crawler/result/json/dict3").read())
dict4 = eval(open("/home/tengmo/crawler_to_server_set_time/crawler/result/json/dict4").read())


total_dict = {}
totla_dict = total_dict.update(dict1)
totla_dict = total_dict.update(dict2)
totla_dict = total_dict.update(dict3)
totla_dict = total_dict.update(dict4)



count = 0
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
    print  total_dict[k]['word_in_title'], " ",total_dict[k]['content_type']," ", total_dict[k]['content_length'] ," ",total_dict[k]['Number_of_word']," ",total_dict[k]['Number_of_picture']," ",total_dict[k]['Number_of_table']," ",total_dict[k]['Number_of_slash_in_URL_path']," ",total_dict[k]['binary_vector'][0], " ",total_dict[k]['binary_vector'][1]," ",total_dict[k]['binary_vector'][2], " ",total_dict[k]['binary_vector'][3]," ",total_dict[k]['binary_vector'][4], " ",total_dict[k]['binary_vector'][5]," ",total_dict[k]['binary_vector'][6], " ",total_dict[k]['binary_vector'][7]," ",total_dict[k]['binary_vector'][8], " ",total_dict[k]['binary_vector'][9]," ",total_dict[k]['URL_Length'], " ",total_dict[k]['Number_of_word_in_URL']," ",total_dict[k]['Number_of_outgoing']," ",total_dict[k]['Numer_of_webpage_in_the_same_site']


    count += 1
