---
title: i.marcusj.org
---
# [i.marcusj.org](https://i.marcusj.org) - a simple, anonymous, and free image hosting service

![i.marcusj.org](static/images/i.marcusj.org/img.png)

This was one of my first projects to use Google Firebase. Images are stored in Google Firestore. Some of the key features include:
* image deletion
* images can be linked from external sources
* open API

## [API docs](https://i.marcusj.org/api/docs)

*Alternatively, check out [the python client libary - `imj`](https://pypi.org/project/imj/)*

<pre><code class='python'>
import imj

res = imj.upload_file("Pictures\\widepeepohappy.png")
print(
    res.viewer, # viewer url
    res.image, # image url
    res.shorten(), # shortened url
)

# you can upload raw data with imj.upload(bytedata)
</code></pre>