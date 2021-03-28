import sys
import os
import requests
import re
from selenium import webdriver
from bs4 import BeautifulSoup

input_dir = 'dataset_output_cleaned'
output_dir = 'dataset_output_separated'
#input_dir = 'dataset_links_sample'
#output_dir = 'dataset_output_sample'

for genre_folder in os.listdir(input_dir):
    if  genre_folder.endswith('_old'):
        continue
    os.makedirs(output_dir+'/'+genre_folder)
    genre_count = 1
    for story_file in os.listdir(input_dir+'/'+genre_folder):
        story_count = 1
        with open(input_dir+'/'+genre_folder+'/'+story_file, 'r') as input_file:
            story = input_file.read()
            story = story.replace('\r', '\n')
            lines = story.split('\n')
            story_new = ''
            for line in lines:
                if line != '':
                    story_new += line
            delims = '[।]'                    
            lines = re.split(delims, story_new)
            story_new = ''
            for line in lines:
                if line != '':
                    lines1 = re.split('[?]', line)
                    if len(lines1) > 1:
                        for line1 in lines1:
                            if line1 != '':
                              story_new += line1 + '?\n'
                    else:
                        story_new += line + '।\n'
            with open(output_dir+'/'+genre_folder+'/'+story_file, 'w') as output_file:
                output_file.write(story_new)
                  
