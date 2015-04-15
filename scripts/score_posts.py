# -*- coding: utf-8 -*-  
import codecs
import subprocess
import platform
import os
from copy import deepcopy
import datetime
import re



if __name__ == '__main__':
    operation_system = platform.system()
    pwd = os.getcwd()
    markdown_dir = deepcopy(pwd).replace('/scripts', '/scores/_posts')
    score_dir = deepcopy(pwd).replace('/scripts', "/assets/files")
    file_list = os.listdir(score_dir)
    print file_list

    idx = 1
    today = '/' + str(datetime.date.today()) + '-'
    pdf_line = '<iframe src="http://docs.google.com/gview?url=replace&embedded=true" style="width:588px; height:833px;" frameborder="0"></iframe>'
    jpg_line = '![alt text](replace "jpg score")'
    permalink_prefix = 'https://github.com/pku-accordion/pku-accordion.github.io/raw/77f042ef77f64bc522f6c7f0b22336c723e51bcf/assets/files/'

    num_to_name = {}
    with codecs.open('/'.join([score_dir, 'names.txt']), 'r', encoding = 'gbk') as g:
        for line in g:
            tmp = line.split()
            num_to_name[tmp[0]] = tmp[1]

    with open('/'.join([score_dir, 'finished.txt']), 'r') as g:
        finished_list = [i.replace('\n', '') for i in g.readlines()]

    finished_list = []

    for directory in file_list:
        if os.path.isfile(score_dir + '/' + directory):
            continue
        elif directory in finished_list:
            continue
        else:
            pages = os.listdir(score_dir + '/' + directory)
            page_num = 1
            for page in pages:
                new_name = [i for i in page if ord(i) <= 127]
                if len(new_name) <= 4:
                    new_name = str(page_num) + ''.join(new_name)
                    page_num += 1
                else:
                    new_name = ''.join(new_name)
                
                os.rename('/'.join([score_dir, directory, page]), '/'.join([score_dir, directory, new_name]))
            pages = os.listdir(score_dir + '/' + directory)
            # sort pages by the number assigned to them in suffix
            page_to_num = {}
            for page in pages:
                position = re.search("\d", page)
                if position:
                    page_to_num[page] = page[position.start():-4]
                else:
                    page_to_num[page] = 0
            pages = sorted(page_to_num)
            
            with codecs.open(markdown_dir + today + directory + '.markdown', 'w+', encoding = 'utf8') as f:
                if num_to_name.has_key(directory):
                    score_name = num_to_name[directory]
                else:
                    score_name = str(idx)
                    #idx + = 1
                lines = ['---', 'title: " ' + score_name + '"', 'date: ' + str(datetime.date.today()), '---']
                f.writelines([i + '\n' for i in lines])
                for page in pages:
                    permalink = permalink_prefix + directory + '/' + page#.decode('utf-8')
                    if page[-3:] == 'pdf':
                        f.write('<div style="text-align:center">' + '\n')
                        f.write(deepcopy(pdf_line).replace('replace', permalink) + '\n')
                        f.write('</div>' + '\n')
                        f.write('\n')
                    elif page[-3:] == 'jpg':
                        #f.write('<div style="text-align:center">' + '\n')
                        f.write(deepcopy(jpg_line).replace('replace', permalink) + '\n')
                        #f.write('</div>' + '\n')
                        f.write('\n')
                        
                    
                f.write('\n')

            with open('/'.join([score_dir, 'finished.txt']), 'a') as f:
                f.write(directory + '\n')



    with codecs.open('/'.join([score_dir, 'test.txt']), 'w+', encoding = 'gbk') as f:
        f.write(' '.join(line.split()))
            
##    if operation_system == 'Windows':
##        #pwd = subprocess.call('echo %cd%')
##        print

