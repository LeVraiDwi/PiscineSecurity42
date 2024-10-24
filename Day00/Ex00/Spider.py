from urllib.request import urlopen, Request
import requests
import shutil
from bs4 import BeautifulSoup

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

def ScrapImg(Url: str, depth: int):
    url = "http://olympus.realpython.org/profiles/aphrodite"
    req = Request(
        url=url, 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    imgExt = [".jpg", ".jpeg", ".png", ".gif",".bmp"]
    domain = baseDomaine(url)
    if domain == "":
        print("wrong url")
        return
    page: _UrlopenRet
    try:
        page = urlopen(req)
    except:
        print("Impossible to Open the page")
        return
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    extract = BeautifulSoup(html, 'html.parser')
    for start in extract.find_all('img'):
        try:
            out = start.get('src')
            if (out and out.endswith(ext) for ext in imgExt):
                res = requests.get(domain + out, stream=True)
                if res.status_code == 200:
                    with open("./name",'wb') as f:
                        shutil.copyfileobj(res.raw, f)
                    print('Image sucessfully Downloaded: ',"./name")
                else:
                    print('Image Couldn\'t be retrieved')
        except:
            print("fail to save the image")
            continue
    return

def main():
    

if __name__ == "__main__":
    main()