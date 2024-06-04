import jieba
import re
import pandas as pd
def stopwordslist():
    f=open('final_stopwords.txt','r',encoding='gbk')
    stopwords=f.readlines()
    stopwords=[i[:-1] for i in stopwords]
    return stopwords
def seg_paragraph(para):
    jieba.load_userdict('保留词.txt')
    para_seg=jieba.cut(para)
    stopwords= stopwordslist()
    out_para=''
    for word in para_seg:
        if word not in stopwords and word != '/n' and word != ' ':
            out_para += ' '
            out_para+=word
    return out_para[:-1]
file='文本编码合并.csv'
raw_data = pd.read_csv(file)
raw_df=pd.DataFrame(raw_data)
seg_text=[]
for line in raw_df["Text"]:
    seg_text.append(seg_paragraph(line))
raw_df["Text"]=seg_text
df_0=raw_df.loc[raw_df['Keyword'] == 0]
date0= [int(i) for i in df_0['Date'].tolist()]
df_0['Date']=date0
df_1=raw_df.loc[raw_df['Keyword'] == 1]
date1= [int(i) for i in df_1['Date'].tolist()]
df_1['Date']=date1
df_all=pd.concat([df_1,df_0])
df_1=df_1.iloc[:,1:5]
df_0=df_0.iloc[:,1:5]
df_all=df_all.iloc[:,1:5]
df_1.to_csv('分词结果 -1.csv', encoding='utf_8_sig')
df_0.to_csv('分词结果 -0.csv', encoding='utf_8_sig')
df_all.to_csv('分词结果.csv', encoding='utf_8_sig')