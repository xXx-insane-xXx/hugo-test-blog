---
title: Insane hugo pipeline
data: 24/7/25
draft: false
tags:
- hugo-pipeline
---


# Setup Hugo + Git + Obsidian blog pipeline

## Install and setup

#### 1. Install obsidian (Actually org mode is better, for those who know) -
```bash
sudo pacman -S obsidian
```

#### 2. Install prerequisites -
-  Install Go - Programming language in which hugo is made so its needed for hugo binary to work.
```bash
sudo pacman -S go
```
- Install git - Version control system where we will upload our hugo site.
```bash
sudo pacman -S git

# Configure your git with username and email
git config --global user.name "Insane"
git config --global user.email "insane@testemail.com"
```

- Install Hugo - Hugo itself is installed as a single binary called hugo!
```bash
sudo pacman -S hugo
```

---
## Setup obsidian

1. Open obsidian and create a vault. Vault is just the main folder where all sub folders or notes are stored. This entire vault can be backed up in cloud storage.
	- Let the vault be ~/vault for this tutorial purpose.
2. Obsidian directly now opens up in this vault. All the obsidian configs for themes, plugins, etc are stored in this root folder inside ``.obsidian``.
3. Create a sub folder called posts where we will store our posts for hugo.

---
## Create a sample blog

1. Create a new note as hello-world and save it. The ``.md`` extension is automatically added but not shown inside obsidian file tree.
2. Add the following content -
```markdown
# My first blog

This is an awesome blog. Ah not really I guess.
```

---
## Setup hugo

#### Create basic hugo site
1. ``cd`` into your desired directory where you want to store your site.
2. Run ``hugo new site <site-name>`` to make a site.
	- Example: ``hugo new site hugo-test-blog``
	- Let the site main directory be at ~/hugo-test-blog for this tutorial.
3. Go inside hugo-test-blog. Inside here all your website content is present.
4. Initialize git repository here
	 - ``git init .``
	 - create a repository in GitHub, then a page will open on how to connect your local folder to the remote GitHub repository. Simply follow it :].

#### Install a hugo theme
1. Go to https://gohugo.io/installation/linux/
2. Select a desired theme and head to its GitHub page. Here you will find all instructions on how to use it, install it, etc. I will use a theme called hello-friend-ng and use git submodule method to install the theme.
3. Make sure you are inside ``hugo-test-blog``. Then run this command to install the theme.
```bash
# Theme name: hello-friend-ng. 
# Goto: https://github.com/rhazdon/hugo-theme-hello-friend-ng to know more about it.
git submodule add https://github.com/rhazdon/hugo-theme-hello-friend-ng.git themes/hello-friend-ng
```
	 
4. Copy this config to ``./hugo.toml``. Or simply head to the theme GitHub and get the latest config from their.
```toml
baseurl              = "localhost"
title                = "My Blog"
languageCode         = "en-us"
theme                = "hello-friend-ng"
pagination.pagerSize = 10

[params]
  dateform        = "Jan 2, 2006"
  dateformShort   = "Jan 2"
  dateformNum     = "2006-01-02"
  dateformNumTime = "2006-01-02 15:04"

  # Subtitle for home
  homeSubtitle = "A simple and beautiful blog"

  # Set disableReadOtherPosts to true in order to hide the links to other posts.
  disableReadOtherPosts = false

  # Enable sharing buttons, if you like
  enableSharingButtons = true
  
  # Show a global language switcher in the navigation bar
  enableGlobalLanguageMenu = true

  # Metadata mostly used in document's head
  description = "My new homepage or blog"
  keywords = "homepage, blog"
  images = [""]

[taxonomies]
    category = "blog"
    tag      = "tags"
    series   = "series"

[languages]
  [languages.en]
    title = "Hello Friend NG"
    keywords = ""
    copyright = '<a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank" rel="noopener">CC BY-NC 4.0</a>'
    readOtherPosts = "Read other posts"

  [languages.en.params]
    subtitle  = "A simple theme for Hugo"

    [languages.en.params.logo]
      logoText = "hello friend ng"
      logoHomeLink = "/"
    # or
    #
    # path = "/img/your-example-logo.svg"
    # alt = "Your example logo alt text"

  # And you can even create generic menu
  [[menu.main]]
    identifier = "blog"
    name       = "Blog"
    url        = "/posts"
```

#### Run hugo site
1. Run this command to run the hugo site locally
```bash
hugo server -t hello-friend-ng
```
2. Go to ``localhost:1313``
3. Now your site is running!

#### Post blogs in your site
1. All your posts goes inside content/posts directory.
2. Make ``posts`` dir inside ``content`` subdir if not already their.
 ```bash
mkdir content/posts 
```
3. Sync your obsidian posts folder to content/posts folder. We will use rsync for it.
```bash
rsync -av --delete ~/vault/posts ~/hugo-test-blog/content/posts

# source path is where you created your posts dir for obsidian
# destination path is ..../hugo-test-blog/content/posts
```
4. Done! Go to ``posts`` in your website and you will see the latest post.

---
## Make posts better
1. Add the following front matter to add title and date to your posts.
```md
---
title: Hello World!
data: 24/7/25
draft: false
tags:
- first-post
- hello-world
---

This is an awesome blog. Ah not really I guess.

```
2. Run the rsync command every time for now when you change your markdown inside obsidian.
3. Reload the site!

## Show images in our post
1. Showing images can be tricky.
2. Posts are stored in ``public/posts`` directory. Inside it hugo first creates a directory named after our post and inside its the html converted version of our posts are stored.
3. If you stored files like this
	- ./content/post/hello-world.md
	- ./content/post/image.png
	It get changed to
	- /public/posts/hello-world/hello-world.md
	- /public/posts/image.png
	So you image link path gets broken for the website.
	This can be easily fixed by changing the relative path of the image from ``.`` to ``..`` .
	It will then stop showing in the markdown but would work in the website.
4. Other way is to create images dir inside ~/hugo-test-blog/static/
5. Anything created under static is copied to public
	Example: static/images/image.png is copied as /public/images/image.png
6. So in markdown you can also use ``/images/image.png`` as the location for the image. Again it will work in website but won't show in the site.
7. Third is to create ``images`` directory in the root of the obisidian, and sync it with ``static``. So now in obsidian you can use ``/images/image.png`` as your link as obsidian is sandboxed and supports relative urls only. This would also work in the website.
