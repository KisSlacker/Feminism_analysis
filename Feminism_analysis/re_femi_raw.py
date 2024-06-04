import re
import pandas as pd
def get_raw(name):
    file='D:/Coding/Python/Pycharm Projects/pythonProject/refeminesm/原始文本/'+name+'原始文本 - 副本.txt'
    with open(file,'r',encoding='utf_8_sig') as f:
        k=f.read()
        l=k.replace('-----------------------------------------------------------------------------','split_point')
        l = l.replace('\n', '')
        pattern1='(\d{4})-\d{2}-\d{2}'
        pattern2='文章编号:\s*\[\d+]\s*'
        pattern3='文字快照：http://[a-zA-z+0-9-./?&=#]+'
        pattern4='原文连接：http://[a-zA-z+0-9-./?&=#]+'
        pattern5 = '图片快照：http://[a-zA-z+0-9-./?&=#]+'
        num_list=[i for i in range(4001) if i%2==1]
        text_list=[]
        date_list=[]
        l = l.split('split_point')
        for num in num_list:
            try:
                l[num]=re.sub(pattern2,'', l[num])
                l[num]=re.sub(pattern3, '', l[num])
                l[num] = re.sub(pattern4, '', l[num])
                l[num] = re.sub(pattern5, '', l[num])
                text_list.append(l[num])
                date=re.findall(pattern1,l[num-1])
                date_list.append(date[0])
            except:
                break
        df=pd.DataFrame()
        df["Text"]=text_list
        df['Date']=date_list
        if name=='女性主义':
            df['Keyword']=0
        else:
            df['Keyword']=1
        return df
df_1=get_raw('女权主义')
df_2=get_raw('女性主义')
df=pd.concat([df_1,df_2])
df.to_csv('文本编码合并.csv',encoding='utf_8_sig')