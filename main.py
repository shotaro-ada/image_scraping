import requests
from bs4 import BeautifulSoup

url = 'https://www.photo-ac.com/main/search?q=%E7%8C%AB&pp=140&qid=&creator=&ngcreator=&nq=&srt=dlrank&orientation=all&sizesec=all&color=all&model_count=-1&age=all&mdlrlrsec=all&prprlrsec=all'
download_dir = '/home/sonicdeath9/works/python/getImageFromWeb/pics/'
extension = ('.jpeg', '.jpg')


r = requests.get(url)
soup = BeautifulSoup(r.text)

img_tags = soup.find_all("img")
img_urls = []

for img_tag in img_tags:
  img_url = img_tag.get("src")
  if img_url.endswith(extension):
    img_urls.append(img_url)


def download_image(url, file_path):
  r = requests.get(url, stream=True)
  if r.status_code == 200:
    with open(file_path, "wb") as f:
      f.write(r.content)


for index, url in enumerate(img_urls):
  if url.endswith(('.jpeg', 'jpg')):
    file_name = "{}.jpg".format(index)
  else:
    file_name = "{}.png".format(index)
  image_path = download_dir + file_name
  print(image_path)
  download_image(url, image_path)
