import time
import sys
import json
import re
import os
import requests
from tqdm import tqdm

with open('flickrCredentials.json') as infile:
    credentials = json.load(infile)

KEY = credentials['KEY']
SECRET = credentials['SECRET']

def downloadFile(url, local_filename):
    if local_filename is None:
        local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    return local_filename


def get_group_id_from_url(url):
    params = {
        'method' : 'flickr.urls.lookupGroup',
        'url': url,
        'format': 'json',
        'api_key': KEY,
        'format': 'json',
        'nojsoncallback': 1
    }
    results = requests.get('https://api.flickr.com/services/rest', params=params).json()
    return results['group']['id']


def getPhotos(q_search, page=1, original=False):
    params = {
        'content_type': '1',
        'per_page': '50',
        'media': 'photos',
        'format': 'json',
        'advanced': 1,
        'nojsoncallback': 1,
        'extras': 'media,realname,%s,o_dims,geo,tags,machine_tags,date_taken' % ('url_o' if original else 'url_l'), #url_c,url_l,url_m,url_n,url_q,url_s,url_sq,url_t,url_z',
        'page': page,
        'api_key': KEY
    }

    if q_search is not None:
        params['method'] = 'flickr.photos.search',
        params['text'] = q_search
        params['safe_search'] ='1'
   
    results = requests.get('https://api.flickr.com/services/rest', params=params).json()
    if "photos" not in results:
        print(results)
        return None
    return results["photos"]


def searchData(q_search, original=False, max_pages=None,start_page=1):
    # create a folder for the query if it does not exist
    foldername = os.path.join('images', re.sub(r'[\W]', '_', q_search ))
   
    if not os.path.exists(foldername):
        os.makedirs(foldername)

    jsonfilename = os.path.join(foldername, 'results' + str(start_page) + '.json')

    if not os.path.exists(jsonfilename):

        # save results as a json file
        photos = []
        current_page = start_page

        results = getPhotos(q_search, page=current_page, original=original)
        if results is None:
            return

        total_pages = results['pages']
        if max_pages is not None and total_pages > start_page + max_pages:
            total_pages = start_page + max_pages

        photos += results['photo']

        while current_page < total_pages:
            print('downloading metadata, page {} of {}'.format(current_page, total_pages))
            current_page += 1
            photos += getPhotos(q_search, page=current_page, original=original)['photo']
            time.sleep(0.5)

        with open(jsonfilename, 'w') as outfile:
            json.dump(photos, outfile)

    else:
        with open(jsonfilename, 'r') as infile:
            photos = json.load(infile)

    # download images
    print('images Downloading ')
    for photo in tqdm(photos):
        try:
            url = photo.get('url_o' if original else 'url_l')
            extension = url.split('.')[-1]
            localname = os.path.join(foldername, '{}.{}'.format(photo['id'], extension))
            if not os.path.exists(localname):
                downloadFile(url, localname)
        except Exception as e:
            continue


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Download images from flickr')
    parser.add_argument('--search', '-s', dest='q_search', default=None, required=False, help='Search term')
    parser.add_argument('--original', '-o', dest='original', action='store_true', default=False, required=False, help='Download original sized photos if True, large (1024px) otherwise')
    parser.add_argument('--max-pages', '-m', dest='max_pages', required=False, help='Max pages (default none)')
    parser.add_argument('--start-page', '-st', dest='start_page', required=False, help='Start page (default 1)')
    args = parser.parse_args()

    q_search = args.q_search
    original = args.original

 

    max_pages = None
    if args.max_pages:
        max_pages = int(args.max_pages)

    if args.start_page:
        start_page = int(args.start_page)

    searchData(q_search, original, max_pages, start_page)

