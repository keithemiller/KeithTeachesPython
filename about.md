---
layout: page
title: About
permalink: /about/
---

Relic dynamically generates the site homepage using collections and posts. The posts and each collection is given a tile on the site homepage, and that tile is populated with its respective posts/documents, their metadata, and an optional icon for each post, all specified through the individual post/document frontmatter.

The site navigation bar is generated with a link to each page createed and a link to each collection. For a page with the list of posts, one should create a posts.md file. For a page for a collection, one should create an index page in said collection folder. You can find a premade postfeed.html and collectionfeed.html in the _includes folder and their respective implementations in the posts.md file and the _collections1 and _collections2 index.md file.

* _config.yml
  * Specifies site variables
  * Specifies collections
* _collectionName
  * contains "documents" for the collection.
  * index.md is the index page for the collection
* css/main.scss
  * contains site style configurations
  * contains $collections variable, specifying the number of tiles to display on the site homepage
* images
  * contains all images (including post icons)
* _includes
  * contains different html templates, like the header, footer, and different feeds used for posts and collections
* _layouts
  * contains feed.html, the default layout for collections and post feeds
