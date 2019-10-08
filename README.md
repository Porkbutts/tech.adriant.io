# subtlepurpose.com

Jekyll blog hosted on Github-pages.

## Drafting Posts
Add to `_drafts` with the file name format `YYYY-mm-dd-name-of-post.md`

Here's an example post. It should include the category, comma-delimitted tags,
and optionally a read more separator.
```
---
layout: post
category: general
tags: aws s3
---

Hello I'm here to talk about s3.

<!--more-->

<Users only see this content when they click into the blog post>.
```

## Adding new gems
```
$ bundle add <gem>
```

## Run locally
```
# Development
$ ./script/serve-dev

# Production
$ ./script/serve-prod
```

## Collect tags from posts and create the layouts
```
$ ./script/update_tags
```

## Useful Reading
- [Jekyll permalinks](https://jekyllrb.com/docs/permalinks/)
- [Jekyll github-pages](https://jekyllrb.com/docs/github-pages/)
- [Jekyll site variables](https://jekyllrb.com/docs/variables/)
- [Jekyll blogging](https://jekyllrb.com/docs/step-by-step/08-blogging/)
