---
title: Insane hugo pipeline
data: 24/7/25
draft: false
tags:
- hugo-pipeline
---


# Setup Hugo + Git + Obsidian blog pipeline

## Install and setup

1. Install obsidian (but is org-mode > markdown ??) -
```bash
sudo pacman -S obsidian
```

2. Install prerequisites -
-  Install Go - Programming language in which hugo is made so its needed for hugo binary to work.
```bash
sudo pacman -S go
```
- Install git and set it up
```bash
sudo pacman -S git # Install git

# Configure your git with username and email
git config --global user.name "Insane"
git config --global user.email "insane@testemail.com"
```

- Install Hugo - Hugo itself is installed as a single binary called ``hugo`` !
```bash
sudo pacman -S hugo
```

---
## Setup obsidian

1. Open obsidian and create a vault. Vault is just the main folder inside which you store all your obsidian notes.
	- Let the vault be ``~/vault`` for this tutorial purpose.
2. All obsidian config for themes, plugins, etc are stored in ``~/vault/.obsidian``.
3. Create a sub folder called posts where we will store our posts for hugo.

Note: Obsidian is sandboxed. When you open obsidian under this vault then ~/vault becomes the root directory for obsidian. The slash ``/`` means root of the vault and not your actual system.

---
## Create a sample blog

1. Go to ``~/vault``
```bash
cd ~/vault
```
2. Create posts folder. Inside here all your markdowns will be stored which you want to display as blog in the website.
```bash
mkdir ~/vault/posts
```
3. Create a markdown file ``hello-world.md``.
```bash
touch ~/vault/posts/hello-world.md
```
4. Add the following content -
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
	- Let the site main directory be at ``~/hugo-test-blog`` for this tutorial.
```bash
hugo new site ~/hugo-test-blog
cd ~/hugo-test-blog
```
3. Inside ``hugo-test-blog`` all your code for the website is present.
4. Initialize git repository here
	 - ``git init .``
	 - create a repository in GitHub and simply connect ~/hugo-test-blog to it using the instructions you get after creating the repository. I hope you know this stuff. If you don't know these its better to learn git first.

#### Install a hugo theme
1. Go to https://gohugo.io/installation/linux/
2. Select a desired theme and head to its GitHub page. Here you will find all instructions on how to use it, install it, etc. I will use a theme called ``hello-friend-ng`` and use git submodule method to install the theme.
3. Make sure you are inside ``hugo-test-blog``. Then run this command to install the theme.
```bash
# Theme name: hello-friend-ng. 
# Goto: https://github.com/rhazdon/hugo-theme-hello-friend-ng to know more about it.
git submodule add https://github.com/rhazdon/hugo-theme-hello-friend-ng.git themes/hello-friend-ng
```
	 
4. Copy this config to ``./hugo.toml``. Or simply head to the theme GitHub and get the latest config from their. The config present in the GitHub had a error which I fixed here!
```toml
baseurl              = "localhost"
title                = "My Blog"
languageCode         = "en-us"
theme                = "hello-friend-ng"
pagination.pagerSize = 10 # There was a mistake in this line which I fixed.

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

#### Run hugo site locally
1. Run this command to run the hugo site locally
```bash
hugo server -t hello-friend-ng # This starts the server locally 
```
2. Go to ``localhost:1313``
3. Hope you can see your website now!

#### Post blogs in your site
1. All your posts goes inside ``~/hugo-test-blog/content/posts`` directory.
 ```bash
mkdir ~/hugo-test-blog/content/posts # Making posts directory inside content is optional though
```
3. Sync your obsidian ``~/vault/posts`` with ``~/hugo-test-blog/content/posts`` folder. We will use rsync for it.
```bash
rsync -av --delete ~/vault/posts/ ~/hugo-test-blog/content/posts/

# You may want to learn about rysnc a bit. Watch this tutorial from Learn Linux TV - https://youtu.be/KG78O53u8rY?si=1O-Zweu05DmH49o0
```
4. Done! Go to ``posts`` link in your website and you will see the latest post.
5. You must run this rsync command every time you make a new markdown file or change something inside ``~/vault/posts``.

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
2. Run the rsync command.
3. Reload the site!

---
## How hugo is working?
1. All your contents in the ``~/hugo-test-blog`` is copied to ``~/hugo-test-blog/public`` folder. This public folder is served by hugo when you run ``hugo server`` command.
2. Inside public folder everything is in html or css. Static assets only basically.
3. Only catch is ``~/hugo-test-blog/static`` folder isn't copied to public but the contents inside of it is copied to ``~/hugo-test-blog/public``.
4. Inside ``~/hugo-test-blog/public`` folder any html file if contains ``/`` in any path url doesn't mean root of your system. The root here is the public folder itself! This is something that will get in your head when you start learning server side coding and all.

## Show images in our post (4 ways - Use the last option if you are confused)

####  Storing images inside ~/hugo-test-blog/posts
1. Showing images can be tricky.
2. Posts are stored in ``~/hugo-test-blog/public/posts`` directory to show in the website. Inside it hugo first creates a directory named after our post and inside it is the html converted version of our markdown.
3. If you stored files like this
	- ``~/hugo-test-blog/content/posts/hello-world.md``
	- ``~/hugo-test-blog/content/post/image.png``
	After running ``hugo server``
	It gets changed to
	- ``~/hugo-test-blog/public/posts/hello-world/hello-world.md``
	- ``~/hugo-test-blog/public/posts/image.png`` (See here image stays on directory back!)
4. Now in ~/vault/posts/hello-world.md you can add image like this.
```markdown
!["Some image desc"](./image.png)
```
5. But this won't work in the website as image becomes one directory back their. So better use this
```bash
!["Some image desc"](../image.png)
```
6. This will stop showing image in the obsidian markdown preview but will work in the website!

#### Storing images inside ~/hugo-test-blog/static/images
1. Other way is to create images directory here ``~/hugo-test-blog/static/images``.
2. Now in ~/vault/posts/hello-world.md use this
```markdown
!["Some image desc"](/images/image.png)
```
3. Make sure that image.png is in ~/hugo-test-blog/static/images/image.png.
4. This won't show image in obsidian markdown preview but will work in the website.

#### Most elegant solution (Just use this and make your life simple)
1. In the root of obsidian vault create a directory called ``images``.
```bash
mkdir ~/vault/images
```
1. Store all your images here
2. Now in ~/vault/posts/hello-world.md use this
```bash
!["Some image desc"](/images/image.png)
```
3. This will show image in the markdown preview mode now also! And of course will work in the website too
4. Now sync this ``~/vault/images/`` with ``~/hugo-test-blog/static/images/``
```bash
rsync -av --delete ~/vault/images/ ~/hugo-test-blog/static/images/
```
5. You're done! No need of any fancy script.

#### Even better solution (Not needed for now)
Host all your images in a cdn and simply copy and paste url in your markdown. Its the most easiest option.

---
## rsync script
1. Make a script inside ``~/hugo-test-blog/script.sh``
```bash
touch ~/hugo-test-blog/script.sh
```
2. Open ``script.sh`` and paste the following
```bash
rsync -av --delete ~/vault/posts/ ~/hugo-test-blog/content/posts/
rsync -av --delete ~/vault/images/ ~/hugo-test-blog/static/images/
```
3. Make it executable
```bash
chmod +x ~/hugo-test-blog/script.sh
```
4. Run this script whenever you make changes inside ``~/vault/images/`` or ``~/vault/posts/``
```bash
~/hugo-test-blog/script.sh # To run the script
```

---
## Make it live via GitHub pages
Just follow this guide https://gohugo.io/host-and-deploy/host-on-github-pages/. Its super simple and your site will be up in minutes.

---
## Build hugo site without running it
1. This will build your hugo static site under ``~/hugo-test-blog/public`` but won't run any server locally to serve it.
```bash
hugo build
```


###### Extra information below (better to ignore)
Note: Launching any html file from ``~/hugo-test-blog/public/`` won't work as it uses paths like ``/someimage.png`` etc. Here ``slash /`` would mean your system's root unless a server is serving this directory.
The GitHub pages link I shared you automatically builds the hugo site when you push any changes using GitHub actions.
So you may not run ``hugo build`` before pushing any changes!
And that ``slash /`` thingy is automatically handled by GitHub. As the root here means the url generated by GitHub pages.

---

Well that's it! If you find any errors or mistakes in this blog, please to mail me
Mail: insane@insanelogs.xyz
Thank you :]
🦖