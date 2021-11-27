import re
tr='''<h3 align="center">Popularity in 1990</h3>'''
k=re.findall("<h3.*.h3>",tr)
print(k)

