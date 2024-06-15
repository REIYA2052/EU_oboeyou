import numpy
import random as rm
import time
from playsound import playsound as ps
import csv
datas = []
clear = 0
incorrect = []
def strp_time(sec:int):
    min = (sec-(sec%60))/60
    secs = sec%60
    return [int(min),round(secs,2)]
with open('country.csv', encoding='UTF-8') as f:
    reader = csv.reader(f)
    for line in reader:
        for i in range(1,int(len(line)/2)+1):
            datas.append([line[0],line[i*2-1],line[i*2]])
mode = input('モードを選択してください(capital(首都) or year(加盟年) or country(国名)):')
datas1 = len(datas)
start = time.time()
for i in range(len(datas)):
    k = rm.randint(0,len(datas)-1)
    data = datas[k]
    if mode == 'year':
        print(f'{data[1]}がEUに加盟したのは何年か?')
        ans = input('回答:')
        if ans == data[0]:
            print('正解です')
            ps('seikai.mp3')
            clear += 1
            del datas[k]
        else:
            print('不正解です')
            ps('fuseikai.mp3')
            print(f'正解は{data[0]}')
            incorrect.append(data)
            del datas[k]
    if mode == 'capital':
        print(f'{data[1]}の首都はどこか?')
        ans = input('回答:')
        if ans == data[2]:
            print('正解です')
            ps('seikai.mp3')
            clear += 1            
            del datas[k]
        else:
            print('不正解です')
            ps('fuseikai.mp3')
            print(f'正解は{data[2]}')
            incorrect.append(data)
            del datas[k]
    if mode == 'country':
        print(f'{data[2]}が首都の国はどこか?')
        ans = input('回答:')
        if ans == data[1]:
            print('正解です')
            ps('seikai.mp3')
            clear += 1
            del datas[k]
        else:
            print('不正解です')
            print(f'正解は{data[1]}')
            ps('fuseikai.mp3')
            incorrect.append(data)
            del datas[k]
end = time.time()
record = strp_time(round(end-start,2))
print(f'{datas1}問中{clear}問正解です。正答率は{round((clear/datas1)*100,2)}%です。経過時間は{record[0]}分{record[1]}秒でした。一問あたり{round((end-start)/datas1,2)}秒です')
if len(incorrect) >=1:
    print('間違えた問題は以下のとおりです')
    for i in incorrect:
        print(i[0],i[1],i[2])
else:
    print('全問正解です。次も頑張りましょう')
