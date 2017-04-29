"""
##############################################################################
Создает страницы со ссылками переадресации на перемещенный веб-сайт.
Генерирует по одной странице для каждого существующего на сайте файла html;
сгенерированные файлы нужно выгрузить на ваш старый веб-сайт. Смотрите описание
ftplib далее в книге, где представлены приемы реализации выгрузки файлов
в сценариях после или в процессе создания файлов страниц.
##############################################################################
"""

import os

server_name = 'learning-python.com'
home_dir = 'books'
site_files_dir = r'C:\temp\public_html'  # локальный каталог с файлами сайта
upload_dir = r'C:\temp\isp-forward'      # где сохранять сгенерированные файлы
template_name = 'template.html'          # шаблон для генерируемых страниц

try:
    os.mkdir(upload_dir)
except OSError:
    pass

template = open(template_name).read()
site_files = os.listdir(site_files_dir)

count = 0

for file_name in site_files:
    if file_name.endswith('.html') or file_name.endswith('.htm'):
        fwd_name = os.path.join(upload_dir, file_name)
        print('Creating', file_name, 'as', fwd_name)
        file_text = template.replace('$server$', server_name)
        file_text = file_text.replace('$home$', home_dir)
        file_text = file_text.replace('$file$', file_name)
        open(fwd_name, 'w').write(file_text)
        count += 1

print('Last file => \n', file_text, sep='')
print('Done:', count, 'forward files created.')
