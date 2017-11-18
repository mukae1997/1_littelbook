import pandas as pd
import numpy as np
from datetime import datetime
from bs4 import BeautifulSoup
import urllib3
import json
def decideType(name):
    predefine = ['ACT', 'PART', 'SCENE', 'CHAPTER','PART']
    for p in predefine:
        if name.find(p) != -1:
            return p
    return ''
http = urllib3.PoolManager()

mainDomain = 'http://www.literaturepage.com'

authorNames = ['Oscar-Wilde']

for name in authorNames:
    url = mainDomain + '/authors/' + name + '.html'
    # print(url)
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data,'lxml')
    workTable = soup.select('table.newlist')[0]
    # print(works)
    works = workTable.find_all('tr')
    workLinks = []
    for r in works:
        work = {
            'name': "",
            'type':"",
            'publish_year':"",
            'pages': 0,
        }
        tds = r.find_all('td')
        # print(tds)
        i = 0
        for k in work.keys():
            work[k] = tds[i].string
            i += 1
        work['link'] = r.select('a')[0]['href']
        work['type'] = work['type'].replace('(','')
        work['type'] = work['type'].replace(')','')
        work['pages'] = int(work['pages'].replace(' pages', ''))
        # print (work)

        # go to the contents of work
        workurl = mainDomain + work['link']
        worktype = work['type']
        print('\n> ',work['name'] ,'\n')
        response = http.request('GET', workurl)
        workPage = BeautifulSoup(response.data,'lxml')
        tocs = workPage.find_all('div','toc')
        # print(tocs)
        inLevel = False
        topContent = {}
        levelName = ""
        for toc in tocs: # each toc links to  a text entity
            if len(toc.select('b')) != 0: # here is a contentlevel
                levelName = toc.select('b')[0].string
                literaType = decideType(levelName)
                topContent[levelName] = {}
                inLevel = True
                continue
            # get the content in the link
            textLink = mainDomain + toc.select('a')[0]['href']
            textTitle = toc.select('a')[0].string # in TOC page
            response = http.request('GET', textLink)
            textPage = BeautifulSoup(response.data,'lxml')
            print('> ', textLink)
            chapTitle = "" # in reading page; may be longer than textTitle
            getTitle = False
            for s in textPage.select('h2')[0].stripped_strings:
                chapTitle = s
            chapTitle = chapTitle.replace('\"', '')
            import re
            chapTitle = re.sub(r'(\d+)\.( +)', '', chapTitle)
            print(chapTitle)
            if worktype == 'essay':
                chapTitle = textPage.select('h2')[0]['center'].string + chapTitle
            chapContents = []
            ps = textPage.find_all('p')
            for para in ps:
                chapContents.append(para.string)

            # thinking: how to iterate??
            if inLevel == True:
                topContent[levelName][chapTitle] = chapContents
            else :
                topContent[chapTitle] = chapContents



        work['content'] = topContent
        print('> endbook')

        with open(work['name'].replace(' ','_') + '.json', 'w') as outfile:
            # json.dumps({'абвгд': 1}, ensure_ascii=False).encode('utf8')
            json.dump(work, outfile, indent=4)


        # print(work)
