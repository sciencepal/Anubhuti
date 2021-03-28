import os
import re

input_dir = 'dataset_output'
output_dir = 'dataset_output_cleaned'

genre_count = 1
for genre_folder in os.listdir(input_dir):
    print (str(genre_count) + ' - ' + genre_folder)
    story_count = 1
    os.makedirs(output_dir+'/'+genre_folder)
    for story_file in os.listdir(input_dir+'/'+genre_folder):
        print (str(story_count))
        with open(input_dir+'/'+genre_folder+'/'+story_file, 'r') as input_file:
            story = input_file.read()
            k = 1
            while k > 0:
                k = 0
                index = story.find('</p>')
                if index > -1:
                    story = story[:index] + '\n\n' + story[index+4:]
                    k += 1
                index = story.find('</br>')
                if index > -1:
                    story = story[:index] + '\n' + story[index+5:]
                    k += 1
                index = story.find('</b>')
                if index > -1:
                    story = story[:index] + story[index+4:]
                    k += 1
                index = story.find('</img>')
                if index > -1:
                    story = story[:index] + story[index+4:]
                    k += 1

            k = 1
            while k > 0:
                k = 0
                index = story.find('<p')
                if index > -1:
                    index1 = story.find('>', index+1)
                    if index1 > -1:
                        story = story[:index] + '\n\n' + story[index1+1:]
                        k += 1
                index = story.find('<br')
                if index > -1:
                    index1 = story.find('>', index+1)
                    if index1 > -1:
                        story = story[:index] + '\n\n' + story[index1+1:]
                        k += 1
                index = story.find('<b')
                if index > -1:
                    index1 = story.find('>', index+1)
                    if index1 > -1:
                        story = story[:index] + story[index1+1:]
                        k += 1
                index = story.find('<img')
                if index > -1:
                    index1 = story.find('>', index+1)
                    if index1 > -1:
                        story = story[:index] + story[index1+1:]
                        k += 1
            story = re.sub(' {2,}', ' ', story)
            story = re.sub('\t', ' ', story)
            story = re.sub('\n{3,}', '\n\n', story)
            story.strip()
            with open(output_dir+'/'+genre_folder+'/'+story_file, 'w') as output_file:
                output_file.write(story)
        story_count+=1
    genre_count+=1

