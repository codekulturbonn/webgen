
import glob
import os.path
import random

'''
Collect images from a folder
'''

def filter(data, **kwargs):
    #print(kwargs['config']['captions'])
    data['source_images'] = []
    n = 1
    for i in glob.glob(data['images']):
        #print(n)
        filename = os.path.basename(i)
        base, ext = os.path.splitext(filename)
        data['source_images'].append({
            'img': base,
            'n': f'{n:02}',
            'caption': kwargs['config']['captions'][n-1]
        })
        n += 1
        if n > 24:
            break

    random.shuffle(data['source_images'])
    return data
