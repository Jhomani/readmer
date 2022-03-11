import markdown
import os
import json

allFiles = os.listdir('input')

contentDic = {}

for file in allFiles:
  md = open(f'./input/{file}', 'r')
  text = md.read()

  htmlBody = markdown.markdown(text, extensions=['fenced_code', 'tables', 'codehilite'])

  contentDic[file.split('.')[0]] = htmlBody

formated = json.dumps(contentDic, indent=2)

f = open('pages.json', 'w')
f.write(formated)