import sys
import os
import requests
import re
from selenium import webdriver
from bs4 import BeautifulSoup

input_dir = 'dataset_output_separated'


for genre_folder in os.listdir(input_dir):
    story_count = 0
    line_count = 0
    if  genre_folder.endswith('_old'):
        continue
    try:
        for story_file in os.listdir(input_dir+'/'+genre_folder):
            story_count += 1
            try:
                with open(input_dir+'/'+genre_folder+'/'+story_file, 'r') as input_file:
                    for line in input_file:
                        line_count += 1
            except Exception as e1:
                print (f"could not open file {genre_folder} / {story_file}") 
    except Exception as e:
        print ("Could not find genre")
    print (f'Genre: {genre_folder}')
    print (str(line_count))
    print (str(story_count))
