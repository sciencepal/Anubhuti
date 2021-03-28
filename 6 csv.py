import sys
import os
import requests
import re
from selenium import webdriver
from bs4 import BeautifulSoup
import csv



csv.register_dialect('myDialect',delimiter=',', quoting=csv.QUOTE_ALL,skipinitialspace=True)

input_dir = 'dataset_output_separated'
output_dir = 'dataset_output_csv'
#input_dir = 'dataset_links_sample'
#output_dir = 'dataset_output_sample'

for genre_folder in os.listdir(input_dir):
    if  genre_folder.endswith('_old'):
        continue
    os.makedirs(output_dir+'/'+genre_folder)
    os.makedirs(output_dir+'_author_annotation/'+genre_folder)
    genre_count = 1
    for story_file in os.listdir(input_dir+'/'+genre_folder):
        story_count = 1
        with open(input_dir+'/'+genre_folder+'/'+story_file, 'r') as input_file:
            story = input_file.readlines()
            
            with open(output_dir+'/'+genre_folder+'/'+story_file+'.csv', 'w') as output_file:
                writer = csv.writer(output_file, dialect='myDialect')
                writer.writerow(['sentence', 'emotion category'])
                for line in story:
                    writer.writerow([line, 5])

            with open(output_dir+'_author_annotation/'+genre_folder+'/'+story_file+'.csv', 'w') as output_file:
                writer = csv.writer(output_file, dialect='myDialect')
                writer.writerow(['sentence', 'emotion A1', 'emotion A2', 'emotion A3'])
                for line in story:
                    writer.writerow([line, 5, 5, 5])
                
                
                  
