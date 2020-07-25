#!/usr/bin/python

import os
import glob

POSTS_DIR = './_posts'
TAGS_DIR = './tag'

def clean_tag_files():
  for f in glob.glob('{0}/*.html'.format(TAGS_DIR)):
    os.remove(f)

def create_tag_file(tag):
  if not tag:
    return

  filename = os.path.join(TAGS_DIR, '{0}.html'.format(tag))
  if os.path.exists(filename):
    return

  print('Creating tag file {}'.format(filename))
  contents = '---\nlayout: tag\ntitle: "Tag: {0}"\ntag: {0}\n---\n'.format(tag)
  with open(filename, 'w') as f:
    f.write(contents)


if __name__ == '__main__':
  clean_tag_files()

  if not os.path.exists(TAGS_DIR):
    os.makedirs(TAGS_DIR)

  for filename in os.listdir(POSTS_DIR):

    if filename.startswith('.'):
      continue

    with open(os.path.join(POSTS_DIR, filename)) as f:
      for line in f.readlines():
        if line.startswith('tags:'):
          raw_tags = line.split('tags:')[1].strip()
          tags = raw_tags.split(' ')
          for tag in tags:
            create_tag_file(tag)
          break
