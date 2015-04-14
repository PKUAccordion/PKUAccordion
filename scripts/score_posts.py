


# -*- coding: utf-8 -*-  
import subprocess
import platform
import os
from copy import deepcopy
import datetime



if __name__ == '__main__':
    operation_system = platform.system()
    pwd = os.getcwd()
    markdown_dir = deepcopy(pwd).replace('/scripts', '/scores/_posts')
    score_dir = deepcopy(pwd).replace('/scripts', "/assets/files")
    file_list = os.listdir(score_dir)
    print file_list

    idx = 1
    today = '/' + str(datetime.date.today()) + '-'
    pdf_line = '<iframe src="http://docs.google.com/gview?url=replace&embedded=true" style="width:100%; height:1200px;" frameborder="0"></iframe>'
    permalink_prefix = 'https://github.com/pku-accordion/pku-accordion.github.io/blob/37a664771bbd8505725073bb3fe3570a327c1a87/assets/files/'

    for directory in file_list:
        if os.path.isfile(score_dir + '/' + directory):
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
            with open(markdown_dir + today + str(idx) + '.markdown', 'w+') as f:
                f.writelines(['---', 'title: " ' + str(idx) + '"', 'date: ' + str(datetime.date.today()), '---'])
                for page in pages:
                    permalink = permalink_prefix + directory + '/' + page#.decode('utf-8')
                    if page[-3:] == 'pdf':
                        f.write(deepcopy(pdf_line).replace('replace', permalink) + '\n')                    
                    
                f.write('\n')



            
    if operation_system == 'Windows':
        #pwd = subprocess.call('echo %cd%')
        print

