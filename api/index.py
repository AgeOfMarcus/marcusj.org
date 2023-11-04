
from flask import Flask, render_template, jsonify, request
from flask import redirect as _redirect
from markdown2 import markdown
import time
import os

# hashnode stuff
import requests

class Hashnode(object):
    _api_url = 'https://api.hashnode.com'
    
    def __init__(self, api_key: str):
        self.headers = {
            'Authorization': api_key
        }

    def get_user_posts(self, username: str, page: int = 0) -> (str, list):
        """
        Accepts a str username as input.
        Returns the blog domain (str), and a list of posts (dicts)
        """
        query = '''{
  user(username: "<username>") {
    publication {
      posts(page: <page>) {
        title
        brief
        slug
        coverImage
      }
    }
    publicationDomain
  }
}'''.replace('<username>', username).replace('<page>', str(page))
        req = requests.post(self._api_url, json={'query': query}, headers=self.headers)
        res = req.json()['data']
        return res['user']['publicationDomain'], res['user']['publication']['posts']

# / end hashnode stuff

app = Flask(__name__)
blog = Hashnode(os.getenv('HASHNODE_API_KEY'))
_hashnode_posts = blog.get_user_posts('marcusjw')

MARKDOWN_EXTRAS = [
    'spoiler',
    'strike',
    'task_list',
    'fenced-code-blocks',
    'header-ids',
    'markdown-in-html',
    'target-blank-links',
    'tables',
    'footnotes',
]

redirect = lambda route: f'https://{request.host}{route}'

def build_projects():
    proj = []
    for fn in os.listdir('projects'):
        img = []
        if fn.endswith('.md'):
            fd = open(f'projects/{fn}').read()
            metadata = fd.split('---')[1].split('\n')
            meta = {ln.split(':')[0].strip(): ln.split(':')[1].strip() for ln in metadata if ':' in ln}
            mdoutput = '---'.join(fd.split('---')[2:])
            if os.path.isdir(f'static/images/{meta["title"]}'):
                imgd = f'static/images/{meta["title"]}'
                for ifn in os.listdir(imgd):
                    img.append(f'/{imgd}/{ifn}')
            
            proj.append({
                'title': meta['title'],
                'desc': meta.get('desc'),
                'images': img,
                'link': meta.get('link'),
                'body': markdown(mdoutput, extras=MARKDOWN_EXTRAS)
            })
    return proj

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route('/')
def app_index():
    blogDomain, posts = globals().get('_hashnode_posts', ('', []))
    return render_template('index.html', blogDomain=blogDomain, posts=posts)

@app.route('/projects')
def app_projects():
    return jsonify({'projects': globals().get('_projects', build_projects())})
