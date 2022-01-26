import requests
import bs4
import json
import sys
from datetime import datetime

def title(soup):
    title = soup.find(class_="c-article-title")
    titleresult = title.get_text()
    titleResult = titleresult + '| nature'
   # print(type(titleResult))
    return titleResult

def abstract(soup):
    abstract = soup.find(id="Abs1-content",class_="c-article-section__content")
    abstractResult = abstract.get_text()
    return abstractResult

def doi(soup):
    doi = soup.find('a', itemprop="sameAs")
    doiResult = doi.get_text()
    return doiResult

def keywords(soup):
    list_value = list()
    for value in soup.find_all(class_="c-article-subject-list__subject"):
        list_value.append(value.text)
    keyword_value = ", ".join(list_value)
    return keyword_value

def date(soup):
    received_date = soup.find(class_="c-bibliographic-information__value")
    received_dateresult = received_date.get_text()
    received_dateResult= datetime.strptime(received_dateresult,'%d %B %Y').strftime('%Y-%m-%d')
    return received_dateResult


def main_func(soup):
    assigned_dict = dict()
    assigned_dict['title'] = title(soup)
    assigned_dict['abstract'] = abstract(soup)
    assigned_dict['doi'] = doi(soup)
    assigned_dict['keywords'] = keywords(soup)
    assigned_dict['received_date'] = date(soup)
    return assigned_dict
    

if _name_ == "_main_":
   # url='https://www.nature.com/articles/s41586-020-3031-0'
    url = input("Enter the URL :\n")
    page = requests.get(url)
    soup = bs4.BeautifulSoup(page.text,'lxml')

    output = main_func(soup)

    op_File= open("nature1.json","w")
    json.dump(output, op_File)
    op_File.close()
