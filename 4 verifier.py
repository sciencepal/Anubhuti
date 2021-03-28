import sys
import os
import requests
import re
from selenium import webdriver
from bs4 import BeautifulSoup

input_dir = 'dataset_links'
output_dir = 'dataset_output'

genre_files = []

for genre_file in os.listdir(input_dir+'/'):
    genre_files.append(genre_file)
for i in range(len(genre_files)):
    for j in range(i+1, len(genre_files)):
        with open(input_dir+'/'+genre_files[i], 'r') as input_file1:
            with open(input_dir+'/'+genre_files[j], 'r') as input_file2:
                for story_link1 in input_file1:
                    for story_link2 in input_file2:
                        if story_link1 == story_link2:
                            print (genre_file[i])
                            print (genre_file[j])
                            print (story_link1)

