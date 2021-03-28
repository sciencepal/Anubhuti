import sys
import os
import requests
import re
from selenium import webdriver
from bs4 import BeautifulSoup

input_dir = 'dataset_links_1'
output_dir = 'dataset_output_1'
#input_dir = 'dataset_links_sample'
#output_dir = 'dataset_output_sample'

for genre_file in os.listdir(input_dir):
    if  genre_file.endswith('_old'):
        continue
    genre_count = 1
    print (str(genre_count) + ' - ' + genre_file)
    with open(input_dir+'/'+genre_file, 'r') as input_file:
        os.makedirs(output_dir+'/'+genre_file)
        story_count = 1
        for story_link in input_file:
            print (str(story_count))
            try:
                browser = webdriver.Chrome()
                browser.get(story_link)
                innerHTML = browser.execute_script("return document.body.innerHTML")
                soup = BeautifulSoup(innerHTML, 'html.parser')
                book_content = soup.find('div', 'book-content')
                book_content = book_content.contents[0]
                chapter_title = book_content.find('h1', re.compile('chapter-title.*'))
                chapter_title = chapter_title.contents[0].replace('\n', '').strip()
                with open(output_dir+'/'+genre_file+'/'+str(story_count)+' '+chapter_title, 'w') as output_file:
                    chapter = book_content.find('div', re.compile('font-16.*'))
                    if chapter == None:
                        chapter = book_content.find('div', re.compile('content-section.*'))
                    for content in chapter.contents:
                        spans = content.find_all('span', 'blane')
                        for span1 in spans:
                            output_file.write(str(span1['data-suggestions']))
                        output_file.write('\n\n')
            except Exception as e:
                print ("Exception : " + str(e))
            finally:
                browser.close()
                story_count+=1
        genre_count+=1
