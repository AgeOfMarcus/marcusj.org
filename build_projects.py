from markdown2 import markdown
import os

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

def build_projects():
    proj = []
    for fn in os.listdir('api/projects'):
        img = []
        if fn.endswith('.md'):
            fd = open(f'api/projects/{fn}').read()
            metadata = fd.split('---')[1].split('\n')
            meta = {ln.split(':')[0].strip(): ln.split(':')[1].strip() for ln in metadata if ':' in ln}
            mdoutput = '---'.join(fd.split('---')[2:])
            if os.path.isdir(f'api/static/images/{meta["title"]}'):
                imgd = f'api/static/images/{meta["title"]}'
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

if __name__ == '__main__':
    print(build_projects())