from urllib.request import urlopen
import re
import string

def baseDomaine(url: str) -> str:
    protocol : str
    try:
        assert url[:8] is "https://" or url[:7] is "http://", "url wrong format"
    except AssertionError:
        print(AssertionError)
        return
        
    return sds


def main():
    url = "http://olympus.realpython.org/profiles/aphrodite"
    page = urlopen(url)
    page
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    print(html)
    startIndex = [m.start() for m in re.finditer("<img", html)]
    for start in startIndex:
        print(html[start:])
        end = (html[start:].find("/>"))
        balise = html[start:(start + end + 2)]
        print(balise)
        srcStart = balise.find("\"") + 1
        srcEnd = balise[srcStart:].find("\"")
        src = balise[srcStart:(srcStart + srcEnd)]
        print(src)
    return

if __name__ == "__main__":
    main()