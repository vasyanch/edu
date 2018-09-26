'''
     Программе на вход подается ссылка на HTML файл.
Она его качает, затем находит в нем все ссылки вида
<a ... href="..." ... > и выводит в алфавитном порядке
список сайтов, на которые есть ссылка.
'''
import requests, re
f = re.finditer(
    r'<a[^>]*href=[\'|"](\w+://)?(([\w|-]+\.)+\w+)[^>]*[\'|"][^>]*>',
    requests.get(input('')).text)
for i in sorted({i.group(2) for i in f}):
    print(i)