# subtlepurpose.com

**subtlepurpose** is my personal DevOps blog built using Jekyll and hosted on Github-pages.

## Installation
- You must have **ruby** installed. **rvm** or some kind of Ruby version manager is recommended.
- You must have **bundler2**. You can install with
```
$ gem install bundler
```
- Install the gems from Gemfile using `bundle` command.

## Run locally
```
# Run dev environment with drafts, livereload and without analytics, comments, ads
$ script/serve-dev

# Run a production build
$ script/serve-prod
```

## Collect tags from posts and create the layouts
This script scans posts for tags and then creates a tag HTML file for each.
```
$ script/update_tags
```

## Drafting Posts
Add to `_drafts` with the file name format `YYYY-mm-dd-name-of-post.md`

Here's an example post. It should include the category, comma-delimitted tags,
and optionally a read more separator.
```
---
layout: post
categories: aws kubernetes
tags: s3 eks
---

Hello I'm here to talk about s3 and eks.

<!--more-->

<Users only see this content when they click into the blog post>.
```

When the post is ready to be published, move it to `_posts`.

## Adding new gems
```
$ bundle add <gem>
```

If it is a jekyll plugin, you may need to add it to the `plugins` section in `_config.yml`

## Gotchas
Not all jekyll plugins are supported by Github pages. I guess it makes sense, they don't read the Gemfile and install your deps, they just have a preset environment. Here's a list of supported plugins: https://pages.github.com/versions/

## Useful Reading
- [Jekyll permalinks](https://jekyllrb.com/docs/permalinks/)
- [Jekyll github-pages](https://jekyllrb.com/docs/github-pages/)
- [Jekyll site variables](https://jekyllrb.com/docs/variables/)
- [Jekyll blogging](https://jekyllrb.com/docs/step-by-step/08-blogging/)
