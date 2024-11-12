from urllib.request import urlopen, Request
import requests
import shutil
from bs4 import BeautifulSoup
import argparse

def baseDomaine(url: str) -> str:
    protocol : str
    try:
        assert url.__len__() >= 7
        protocol = ""
        if url[:8] == "https://":
            protocol = url[:8]
        elif url[:7] == "http://":
            protocol = url[:7]
        assert protocol  != "", "url wrong format"
        assert protocol.__len__() < url.__len__(), "Url wrong format"
    except AssertionError:
        print(AssertionError)
        return ""
    endDomain = url[protocol.__len__():].find("/")
    domain = url[: endDomain + protocol.__len__()]
    return domain

def ScrapImg(args: argparse.Namespace, url: str, depth: int):
    req = Request(
        url=url, 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    imgExt = [".jpg", ".jpeg", ".png", ".gif",".bmp"]
    domain = baseDomaine(url)
    if domain == "":
        print("wrong url")
        return
    page: requests._UrlopenRet
    try:
        page = urlopen(req)
    except:
        print("Impossible to Open the page")
        return
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    extract = BeautifulSoup(html, 'html.parser')
    if args.r == True and depth < args.l:
        for urls in extract.find_all('href'):
            ScrapImg(args, urls, depth + 1)
    for start in extract.find_all('img'):
        try:
            out = start.get('src')
            print(out)
            name = str.split(out, '/')
            name = name[len(name) - 1]
            if (out and out.endswith(ext) for ext in imgExt):
                res = requests.get(domain + out, stream=True)
                if res.status_code == 200:
                    with open(args.p + name,'wb') as f:
                        shutil.copyfileobj(res.raw, f)
                    print('Image sucessfully Downloaded: ',"./name")
                else:
                    print('Image Couldn\'t be retrieved')
        except Exception as e:
            print("fail to save the image")
            continue
    return

def main():
    parser = argparse.ArgumentParser(prog='Spider',
                    description='Scrap image from a url',
                    epilog='./spider [-rlp] URL')
    parser.add_argument('-r', default=False, action='store_true', help="recursively downloads the images in a URL received as a parameter.")
    parser.add_argument('-l', type=int,default=5, help="indicates the maximum depth level of the recursive download. If not indicated, it will be 5.")
    parser.add_argument('-p', type=str, default="./data/",help=" indicates the path where the downloaded files will be saved. If not specified, ./data/ will be used.")
    parser.add_argument('URL', type=str, help="URL you want to scrap")
    args = parser.parse_args()
    print(args.r)
    ScrapImg(args, args.URL, 0)


if __name__ == "__main__":
    main()