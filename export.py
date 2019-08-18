import json,sys,os
f = open(sys.argv[1],'r')
data = json.loads(f.read())
i = 0
if not os.path.exists('SourceCode'):
    os.makedirs('./SourceCode')
for submitid,candidate,idx,problem_name,source_code,language in data['RECORDS']:
    submitid = 's' + data['RECORDS'][i]['submitid']
    candidate = data['RECORDS'][i]['candidate']
    idx = data['RECORDS'][i]['#']
    problem_name = data['RECORDS'][i]['problem_name']
    source_code = data['RECORDS'][i]['sourcecode']
    language = data['RECORDS'][i]['language']
    i = i + 1
    if not os.path.exists('./SourceCode/all'):
        os.makedirs('./SourceCode/all')
    out = open('./SourceCode/all/' + submitid + '_' + candidate + '_' + idx + '_' + problem_name + '.' + language,'w')
    out.write(source_code)
    out.close()
    if not os.path.exists('./SourceCode/' + idx):
        os.makedirs('./SourceCode/' + idx)
    out = open('./SourceCode/' + idx +'/' + submitid + '_' + candidate + '_' + idx + '_' + problem_name + '.' + language,'w')