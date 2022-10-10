from bs4 import BeautifulSoup
import requests
import re
import os
import shutil

ARTICLE_DIR = 'article'

def get_article_content(url: str) -> tuple:
    """
    This method scrapes and saves all contents in the article using 
    beautiful soup and a handy regex.
    It returns a bs4 object and the filename.
    """
    response = requests.get(url, timeout=10)

    soup  = BeautifulSoup(response.content, "html.parser")
    filename = soup.find('h1').text.replace(' ', '_')

    relevant = soup.find_all(re.compile(r'p|li|h[0-4]+|span'),id=re.compile(r'[a-z0-9]{4}'))

    
    if not os.path.exists(ARTICLE_DIR):
        os.mkdir(ARTICLE_DIR)

    content = ''
    for i in relevant:
        content += i.text + '\n'

    with open(f'{ARTICLE_DIR}/{filename}.txt', 'w') as f:
        f.write(content.strip())
    return soup, filename

def save_images(soup: BeautifulSoup) -> None:
    """
    Saves the all images (highest quality) in the article body.
    """
    i = 1
    image_dir = f'{ARTICLE_DIR}/images'
    if not os.path.exists(image_dir):
        os.mkdir(image_dir)

    for img in soup.find_all('source'):
        try:
            link = img['srcset'].split(',')[-1].split(' ')[1]
            img_data = requests.get(link, timeout=10).content
            with open(f'{image_dir}/image_{i}.png', 'wb') as f:
                f.write(img_data)
            i += 1
        except KeyError:
            continue

def compress_and_cleanup_files(directory: str, filename: str) -> None:
    """
    Zips article content and deletes the directory.
    """
    shutil.make_archive(filename, 'zip', directory)
    shutil.rmtree(directory)

def main(url):
    """
    Runs all the functions in order.
    """
    soup, filename = get_article_content(url)
    save_images(soup)
    compress_and_cleanup_files(ARTICLE_DIR, filename)

if __name__ == "__main__":
    article_url = input("Enter the URL of the Medium Article: ")
    # article_url = "https://medium.com/pytorch/accelerate-pytorch-with-ipex-and-onednn-using-intel-bf16-technology-dca5b8e6b58f"
    main(article_url)