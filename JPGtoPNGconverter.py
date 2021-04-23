import sys
import os
from PIL import Image


# grab first and second argument

image_folder = sys.argv[1]

output_folder = sys.argv[2]


# check if new/ exists if it doesn't... create it

if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# loop trough Pokedex/
# convert images to png 
# save png's to new/ folder

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done')






