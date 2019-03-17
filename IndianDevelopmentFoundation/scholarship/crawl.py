import re
import threading
from queue import Queue
from html.parser import HTMLParser
from urllib import parse
from urllib.request import urlopen

class LinkFinder(HTMLParser):
    def __init__(self,base_url,page_url,html_string):
        super().__init__()
        self.page_url = page_url
        self.base_url = base_url
        self.html_string = html_string
        self.data = []
        self.img=[]

    def handle_starttag(self,tag,attrs):
        url = ''
        img={}
        info = {}

        if tag == 'a':
            info = {}
            for (attribute,value) in attrs:
                if attribute == 'href':
                    pattern = r'^/scholarship/.*'
                    if(re.findall(pattern,value)):
                        x = value.replace('/scholarship/','')
                        title_value = x.replace('-',' ')
                        title=title_value.title()
                        info['title']=title
                        url = parse.urljoin(self.base_url,value)
                        info['link']=url
                        #soup = BeautifulSoup(self.html_string , features='html.parser')
                        #print(soup.find_all('article'))
                        #for tag in soup.find_all('article'):
                            #print(soup.tag['class'])
                            #if tag['class'] == 'contentdisplay':
                            #print(tag.string)
                        self.data.append(info)



    def page_links(self):
        return self.data

    def error(self, message):
        pass



def gather_links(base_url,page_url):
    html_string=''
    try:
        response = urlopen(page_url)
        if 'text/html' in response.getheader('Content-Type'):
            html_bytes = response.read()
            html_string = html_bytes.decode('utf-8')
        finder=LinkFinder(base_url,page_url,html_string)
        finder.feed(html_string)
    except Exception as e:
        print(str(e))
        return set()
    return finder.page_links()

#for i in crawl_url:
#    print(gather_links(i))
