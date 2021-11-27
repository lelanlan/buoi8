#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Python for Tester - OneMount Class
# Quang Le - quangdle@gmail.com - 09/2021

import sys
import re

"""Baby Names exercise

Định nghĩa hàm extract_names() dưới đây và gọi từ hàm main().

Cấu trúc các tag html trong các file baby.html như sau:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Các bước nên làm tuần tự:
 -Trích xuất năm
 -Lấy và in ra tên và thứ hạng phổ biến
 -Xây danh sách [year, 'name rank', ... ] và in ra
 -Sửa hàm main() để dùng hàm extract_names.
"""

def extract_names(filename):
    file= open(filename,'r+')
    list_=str(file.read())
    j=(re.findall('<td>.*</td>',list_))
    nam=str(re.findall("<h3.*.h3>",list_))
    k=re.findall("[0-9]{4}",nam)
    h=str(k[0])
    li=[]
    li.append(h)
    for i in j:
      c=re.findall("[^></t][a-zA-Z]+|[0-9]+",i)
      for a in range(1,3):
        str1=c[a]+" "+c[0]
      li.append(str1)
    li.sort()
    return li


#print(extract_names("baby1990.html"))


""" Cho một file .html, trả ra list bắt đầu bằng năm, 
  theo sau bởi các chuỗi tên-xếp hạng theo thứ tự abc.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++


  
def main():
  # Chương trình này có thể nhận đối số đầu vào là một hoặc nhiều tên file
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]') #python babynames.py --summaryfile baby1990.txt
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  if len(args)>0 and summary == False  :
    for file in args:
      print(extract_names(file))
  elif len(args)>0 and summary == True :
    f = open('summaryfile.txt', 'w')
    for file in args:
      f.write(str(extract_names(file)))
    
  else :
    sys.exit(1)


  # Với mỗi tên file, gọi hàm extract_names ở trên và in kết quả ra stdout
  # hoặc viết kết quả ra file summary (nếu có input --summaryfile).
  
if __name__ == '__main__':
  main()

