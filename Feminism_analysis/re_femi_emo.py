import pandas as pd
def rate_emotion(para,emo_pd):
    score_0 = 0
    score_1 = 0
    score =[]
    para_list=para.split(' ')
    a=emo_pd['词语']
    for word in para_list:
        if word in list(a):
            polarity = emo_pd.loc[emo_pd['词语'] == word, '极性'].tolist()
            rate=emo_pd.loc[emo_pd['词语'] == word, '强度'].tolist()
            score_0 += polarity[0]*rate[0]
            score_1 += rate[0]
    score =[score_0,score_1]
    return score
def clarity_dic(para,dic):
    file='情感词汇本体.csv'
    emo_list=pd.read_csv(file)
    emo_pd=pd.DataFrame(emo_list)
    para_list=para.split(' ')
    a=emo_pd['词语']
    for word in para_list:
        if word in list(a):
            clarity= emo_pd.loc[emo_pd['词语'] == word, '情感分类'].tolist()[0]
            if clarity in dic:
                dic[clarity]+=1
            else:
                dic[clarity]=1
    return dic
emo_file='情感词汇本体.csv'
emo_list = pd.read_csv(emo_file)
emo_pd=pd.DataFrame(emo_list)
file='分词结果.csv'
seg_pd=pd.read_csv(file)
seg_pd=pd.DataFrame(seg_pd)
emo_rate=[]
emo_inten=[]
for para in seg_pd['Text']:
    emo_rate.append(rate_emotion(para,emo_pd)[0])
    emo_inten.append(rate_emotion(para, emo_pd)[1])
seg_pd['Score'] = emo_rate
seg_pd['Intension'] = emo_inten
seg_pd.to_csv("情感分析.csv", encoding='utf_8_sig')
print('Score success!')
dic_2019= {}
dic_2020= {}
dic_2021= {}
dic_2022= {}
dic_2023= {}
file1="分词结果 -1.csv"
file0="分词结果 -0.csv"
seg_pd1=pd.read_csv(file1)
seg_pd1=pd.DataFrame(seg_pd1)
seg_pd0=pd.read_csv(file0)
seg_pd0=pd.DataFrame(seg_pd0)
dic_list=[dic_2019,dic_2020,dic_2021,dic_2022,dic_2023]
year_range=[2019,2020,2021,2022,2023]
for num in range(0,5):
    for para in seg_pd0[seg_pd0["Date"]==year_range[num] ]['Text']:
        dic_list[num] = clarity_dic(para, dic_list[num])
    dic_list[num] = sorted(dic_list[num].items(),key=lambda x:x[1],reverse=True)
    print(dic_list[num])
dic_2019= {}
dic_2020= {}
dic_2021= {}
dic_2022= {}
dic_2023= {}
dic_list=[dic_2019,dic_2020,dic_2021,dic_2022,dic_2023]
for num in range(0,5):
    for para in seg_pd1[seg_pd1["Date"]==year_range[num] ]['Text']:
        dic_list[num] = clarity_dic(para, dic_list[num])
    dic_list[num] = sorted(dic_list[num].items(),key=lambda x:x[1],reverse=True)
    print(dic_list[num])
