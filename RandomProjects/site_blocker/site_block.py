import os
import shutil
import logging
import time
import re
from pyuac import main_requires_admin #https://pypi.org/project/pyuac/

# check if system file is there
@main_requires_admin
def block_sites():
    system_file = 'C:\Windows\System32\drivers\etc\hosts'
    
    if not os.path.exists(system_file):
        logging.error('System file not found')
        
    current_path = os.getcwd()
    copy_path = current_path + '\hosts'
    shutil.copy(system_file, copy_path)
        
    # read user input
    wait_seconds = int(input('How many seconds? \n'))
    user_input = input('Paste sites to block separated by spaces. For default say USUAL \n')
    if 'USUAL' in user_input:
        sites_to_block = ['glogow.wroclaw.lasy.gov.pl', 'gov.pl/web/nadlesnictwo-glogow/dane-teleadresowe']
    else:
        sites_to_block = []
    for i in user_input.split(' '):
        sites_to_block.append(re.sub(r'(www.)|(http://www.)|(https://www.)', '', i))
    print(f'Strony wczytane: {sites_to_block}')
    
    with open(system_file, 'a') as f:
        for site in sites_to_block:
            f.write(f'127.0.0.1\t{site}\n')

    time.sleep(wait_seconds)
    shutil.copy(copy_path, system_file)

    print('Sites have been unblocked. Have fun')
    
    
if __name__ == '__main__':
    block_sites()