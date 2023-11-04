
from flask import Flask, render_template, jsonify, request
from flask import redirect as _redirect
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

# paste output from build_projects.py
_projects = [{'title': 'gdbd.marcusj.org', 'desc': None, 'images': [], 'link': None, 'body': '<h1 id="good-day-bad-dayhttpsgdbdmarcusjorg"><a rel="noopener" target="_blank" href="https://gdbd.marcusj.org">Good day Bad day</a></h1>\n\n<p>I built this website so I could keep tally of the amount of times I perform what I deem a "good" task, or a "bad" task. It has a history feature, so you can see your score for the past week/month/etc. I find this useful because often at the end of my week, I find I have forgotten what the highs and lows were.</p>\n'}, {'title': 'hello world', 'desc': None, 'images': [], 'link': None, 'body': '<h1 id="obfuscating-hello-world">Obfuscating <code>hello world</code></h1>\n\n<p><em>The most complicated <code>hello world</code> program in a single line.</em></p>\n\n<p>After reading <a rel="noopener" target="_blank" href="https://benkurtovic.com/2014/06/01/obfuscating-hello-world.html">this article</a> about obfuscating the classic <strong><em>hello world</em></strong> program. The author ended up with the following python code:</p>\n\n<pre><code class=\'python\'>\n(lambda _, __, ___, ____, _____, ______, _______, ________:\n    getattr(\n        __import__(True.__class__.__name__[_] + [].__class__.__name__[__]),\n        ().__class__.__eq__.__class__.__name__[:__] +\n        ().__iter__().__class__.__name__[_____:________]\n    )(\n        _, (lambda _, __, ___: _(_, __, ___))(\n            lambda _, __, ___:\n                chr(___ % __) + _(_, __, ___ // __) if ___ else\n                (lambda: _).func_code.co_lnotab,\n            _ << ________,\n            (((_____ << ____) + _) << ((___ << _____) - ___)) + (((((___ << __)\n            - _) << ___) + _) << ((_____ << ____) + (_ << _))) + (((_______ <<\n            __) - _) << (((((_ << ___) + _)) << ___) + (_ << _))) + (((_______\n            << ___) + _) << ((_ << ______) + _)) + (((_______ << ____) - _) <<\n            ((_______ << ___))) + (((_ << ____) - _) << ((((___ << __) + _) <<\n            __) - _)) - (_______ << ((((___ << __) - _) << __) + _)) + (_______\n            << (((((_ << ___) + _)) << __))) - ((((((_ << ___) + _)) << __) +\n            _) << ((((___ << __) + _) << _))) + (((_______ << __) - _) <<\n            (((((_ << ___) + _)) << _))) + (((___ << ___) + _) << ((_____ <<\n            _))) + (_____ << ______) + (_ << ___)\n        )\n    )\n)(\n    *(lambda _, __, ___: _(_, __, ___))(\n        (lambda _, __, ___:\n            [__(___[(lambda: _).func_code.co_nlocals])] +\n_(_, __, ___[(lambda _: _).func_code.co_nlocals:]) if ___ else []\n        ),\n        lambda _: _.func_code.co_argcount,\n        (\n            lambda _: _,\n            lambda _, __: _,\n            lambda _, __, ___: _,\n            lambda _, __, ___, ____: _,\n            lambda _, __, ___, ____, _____: _,\n            lambda _, __, ___, ____, _____, ______: _,\n            lambda _, __, ___, ____, _____, ______, _______: _,\n            lambda _, __, ___, ____, _____, ______, _______, ________: _\n        )\n    )\n)\n</code></pre>\n\n<h2 id="here-is-my-own-take-on-the-idea-written-from-scratch-in-python3">Here is my own take on the idea, written from scratch in python3</h2>\n\n<iframe frameborder=\'0\' src=\'https://replit.com/@MarcusWeinberger/obf-hello-world-oneline?theme=replitDark&lite=1\' class=\'repl\'></iframe>\n'}, {'title': 'i.marcusj.org', 'desc': None, 'images': [], 'link': None, 'body': '<h1 id="imarcusjorghttpsimarcusjorg-a-simple-anonymous-and-free-image-hosting-service"><a rel="noopener" target="_blank" href="https://i.marcusj.org">i.marcusj.org</a> - a simple, anonymous, and free image hosting service</h1>\n\n<p><img src="static/images/i.marcusj.org/img.png" alt="i.marcusj.org" /></p>\n\n<p>This was one of my first projects to use Google Firebase. Images are stored in Google Firestore. </p>\n\n<h2 id="api-docshttpsimarcusjorgapidocs"><a rel="noopener" target="_blank" href="https://i.marcusj.org/api/docs">API docs</a></h2>\n\n<p><em>Alternatively, check out <a rel="noopener" target="_blank" href="https://pypi.org/project/imj/">the python client libary - <code>imj</code></a></em></p>\n\n<pre><code class=\'python\'>\nimport imj\n\nres = imj.upload_file("Pictures\\\\widepeepohappy.png")\nprint(\n    res.viewer, # viewer url\n    res.image, # image url\n    res.shorten(), # shortened url\n)\n\n# you can upload raw data with imj.upload(bytedata)\n</code></pre>\n'}, {'title': 'repl.email', 'desc': None, 'images': ['/api/static/images/repl.email/demo.gif'], 'link': None, 'body': '<p>Repl.email was great while it lasted, but sadly is no longer in service.</p>\n\n<h1 id="replemailhttpsreplemail-a-fully-fledged-free-email-service-for-replit-users"><a rel="noopener" target="_blank" href="https://repl.email">repl.email</a> - a fully fledged, free email service for replit users</h1>\n\n<p><img src="static/images/repl.email/demo.gif" alt="repl.email" /></p>\n\n<p><a rel="noopener" target="_blank" href="https://notes.marcusj.org/link/repl.email"><em>check out the repl.email noticeboard here!</em></a></p>\n\n<hr />\n\n<p>I <a rel="noopener" target="_blank" href="https://notes.marcusj.org/link/blog#replemail">started work on repl.email</a> late 2020. My goal was to host my own email service - like gmail. However, in order to host this on <a rel="noopener" target="_blank" href="https://repl.email/__repl">replit</a>, I had to think outside the box. Replit only allows you to open a single port for hosting a webserver, so I found two third-party services that I would use to make this work.</p>\n\n<h2 id="sendgridhttpssendgridcom"><a rel="noopener" target="_blank" href="https://sendgrid.com/">SendGrid</a></h2>\n\n<p>By taking advantage of their free API, I can link my account to the domain I own, and send emails out to anyone, anywhere. They also support additional features such as scheduled delivery up to <code>72 hours</code> in advance, which I incorporated into <a rel="noopener" target="_blank" href="https://repl.email">repl.email</a>.</p>\n\n<h2 id="improvmxhttpsimprovmxcom"><a rel="noopener" target="_blank" href="https://improvmx.com/">ImprovMX</a></h2>\n\n<p>Yet another free service, improvmx lets me forward all emails sent to my domain (<code>repl.email</code>) to a set of mailboxes. For the mailbox I used gmail, and sorted emails into individual inboxes.</p>\n\n<h1 id="features">Features</h1>\n\n<ul>\n<li>live markdown editor</li>\n<li>save emails as drafts to continue editing later</li>\n<li>schedule email delivery up to 72 hours</li>\n<li>feature-wide api access</li>\n<li>login via QR code or replit</li>\n<li>attatch files</li>\n<li>flag emails as important/unread + pin emails</li>\n<li>read receipts</li>\n</ul>\n'}]

redirect = lambda route: f'https://{request.host}{route}'

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
    return jsonify({'projects': _projects})
