import re
import os

posts_dir = "/home/insane/Main/web_dev_projects/hugo_blog/hugo_test_blog/content/posts/"
#attachments_dir = "/users/networkchuck/documents/neotokos/attachments/"
static_images_dir = "/home/insane/Main/web_dev_projects/hugo_blog/hugo_test_blog/static/"

for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)


        with open(filepath, "r") as file:
            content = file.read()
            
            images = re.findall(r'\[\[([^]]*\.png)\]\]', content)
            print(images)

