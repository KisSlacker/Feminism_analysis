def get_stopwords(list1,name2):
    f2=open(name2,'r',encoding='utf-8')
    list2=f2.readlines()
    merged_list = list1 + list2
    merged_list = list(dict.fromkeys(merged_list))
    f2.close()
    return merged_list
name_list=['cn_stopwords.txt','hit_stopwords.txt','scu_stopwords.txt','baidu_stopwords.txt']
final_list=[]
for name in name_list:
    final_list=get_stopwords(final_list,name)
with open('final_stopwords.txt', 'w') as file:
    for item in final_list:
        file.write("%s" % item)