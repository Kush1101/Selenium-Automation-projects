# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 13:44:55 2020

@author: DeLL
"""

import bs4, requests, webbrowser
import pandas as pd
'''
url = 'https://github.com/search?o=desc&q=machine+learning&s=stars&type=Repositories'

res = requests.get(url)

res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,'html.parser')
links = soup.select('.f4.text-normal a')


print(len(links))
num = min(10,len(links))
prefix = 'https://github.com'


repo_list = {}

#file = open('top_10_ML.csv')
for i in range(num):
    l = str(links[i].get('href')[1:]).split('/')
    owner, name = l[0],l[1]
    url = prefix + links[i].get('href')
    print(owner,name)
    repo_list[owner+'/'+name] = url 
    
print(repo_list)

project_df = pd.DataFrame.from_dict(repo_list, orient="index")
    # Manipulate the table
project_df["name"] = project_df.index
project_df.columns = ["repository_url", "repo_name"]
project_df = project_df.reset_index(drop=True)
    # Export project dataframe to CSV
project_df.to_csv("repos_list.csv")
'''
site = 'https://github.com/collections/machine-learning'

res = requests.get(site)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,'html.parser')

links = soup.select('.h3.lh-condensed a')
print(len(links))
num = min(10,len(links))
prefix = 'https://github.com'

repo_list = {}

for i in range(num):
    suffix = str(links[i].get('href'))
    l = suffix[1:].split('/')
    owner, name = l[0], l[1]
    url = prefix+ suffix
    #print(url)
    #print(owner,name)
    #print()    
    repo_list[owner+'/'+name] = url
    
repo_df = pd.DataFrame.from_dict(repo_list,orient = 'index')
#print(repo_df)
repo_df['repo_name'] = repo_df.index
repo_df.columns = ['repo_url','repo_name']
repo_df = repo_df.reset_index(drop = True)
#print(repo_df)
repo_df.to_csv('scrapped.csv')

    




