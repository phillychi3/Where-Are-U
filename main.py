import argparse
import json
import threading
import requests
from ColorStr import parse
from fake_useragent import UserAgent
from requests_html import HTMLSession

def statuscode(code):
    if code<=299 and code>=100:
        return True
    return False

def geturl(url,name):
    url = url.replace("<!@#>",name)
    return url

def isfind(sitename,url):
    print(parse(f'§w[§g✓§w] §g{sitename} : §w{url}'))
def nofind(sitename):
    print(parse(f'§w[§r✗§w] §r{sitename} : §yNOT FOUND'))

def download(url):
    ua = UserAgent()  
    user_agent = ua.random
    headers = {
                'user_agent': user_agent,
            }
    if data[url]["needjs"]:
        
        r = session.get(geturl(data[url]["userurl"],args.name),headers=headers)
        r.html.render()
        if data[url]["erroe_mod"] == "msg":
            print(r.html.text.find(data[url]["error_msg"]))
            if r.html.text.find(data[url]["error_msg"]) != -1:
                nofind(data[url]["url"])
                return

        elif data[url]["erroe_mod"] == "stauts":
            if not statuscode(r.status_code):
                nofind(data[url]["url"])
                return
    else:
        r= requests.get(geturl(data[url]["userurl"],args.name),headers=headers)
        if data[url]["erroe_mod"] == "msg":
            print(r.text.find(data[url]["error_msg"]))

            if r.text.find(data[url]["error_msg"]) != -1:
                nofind(data[url]["url"])
                return

        elif data[url]["erroe_mod"] == "stauts":
            if not statuscode(r.status_code):
                nofind(data[url]["url"])
                return
    isfind(data[url]["url"],geturl(data[url]["userurl"],args.name))
    return

def main():

    if args.name != None and args.image != None:
        exit("Error: You can only specify one of the following: --name or --image")
    if args.name != None:
        global final
        final = []
        sites = []
        
        for i in data:
            sites.append(i)
        print("Name: " + args.name)
        print(sites)
        for i in sites:
            try:
                data[i]["disable"]
            except:
                t = threading.Thread(target = download(i))
                t.start()                
                # download(i)
    if args.image != None:
        print("Image: " + args.image)







if __name__ == "__main__":
    session = HTMLSession()
    parser = argparse.ArgumentParser()
    parser.add_argument("--name","-n", help="his name", )
    parser.add_argument("--image","-i", help="his image", )
    args = parser.parse_args()
    with open('sites.json','r',encoding='utf-8') as f:
        data = json.load(f)
    main()
