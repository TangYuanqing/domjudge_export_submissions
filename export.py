import json,sys,os
from xpinyin import Pinyin
f = open(sys.argv[1],'r',encoding='utf-8')
data = json.loads(f.read())
dir_name = 'SourceCode'
if len(sys.argv) == 3:
    dir_name = sys.argv[2]
i = 0
if not os.path.exists('./' + dir_name):
    os.makedirs('./' + dir_name)
for submitid,candidate,idx,problem_name,source_code,language in data['RECORDS']:
    submitid = 's' + data['RECORDS'][i]['submitid']
    candidate = data['RECORDS'][i]['candidate']
    idx = data['RECORDS'][i]['#']
    problem_name = data['RECORDS'][i]['problem_name']
    source_code = data['RECORDS'][i]['sourcecode']
    source_code = data['RECORDS'][i]['sourcecode']
    language = data['RECORDS'][i]['language']
    i = i + 1
    if not os.path.exists('./'+dir_name+'/0'):
        os.makedirs('./'+dir_name+'/0')
#out = open('./'+dir_name+'/0/' + submitid + '_' + candidate + '_' + idx + '_' + problem_name + '.' + language,'w',encoding='utf-8')
    out = open('./'+dir_name+'/0/' + submitid + '_' + Pinyin().get_pinyin(candidate) + '_' + idx + '.' + language,'w',encoding='utf-8')
    out.write(source_code.replace('\r\n','\n'))
    out.close()
    if not os.path.exists('./'+dir_name+'/' + idx):
        os.makedirs('./'+dir_name+'/' + idx)
#out = open('./'+dir_name+'/0/' + submitid + '_' + candidate + '_' + idx + '_' + problem_name + '.' + language,'w',encoding='utf-8')
    out = open('./'+dir_name+'/' + idx +'/' + submitid + '_' + Pinyin().get_pinyin(candidate) + '_' + idx + '.' + language,'w',encoding='utf-8')
    out.write(source_code.replace('\r\n','\n'))