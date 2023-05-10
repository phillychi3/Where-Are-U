import argparse
import json
import threading
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

def gofind(url):
    ua = UserAgent()  
    user_agent = ua.random
    headers = {
                'user_agent': user_agent,
            }

    r = session.get(geturl(data[url]["userurl"],args.name),headers=headers)
    r.html.render()
    if eval(geturl(data[url]['pair'],f'"{args.name}"')):
        if "tureurl" in data[url]:
            data[url]["userurl"] = data[url]["tureurl"]
        isfind(data[url]["url"],geturl(data[url]["userurl"],args.name))
        return
    else:
        nofind(data[url]["url"])
        return
def main():

    if args.name is not None and args.image is not None:
        exit("Error: You can only specify one of the following: --name or --image")
    if args.name is not None:
        global final
        final = []
        sites = []
        
        for i in data:
            sites.append(i)
        if args.target is not None:
            if args.target in sites:
                sites = []
                sites.extend(args.target.split(","))
            else:
                exit("Error: The site is not in the list")
        print("Name: " + args.name)
        print(sites)
        for i in sites:
            gofind(i)
            # t = threading.Thread(target = gofind(i))
            # t.start()
    if args.image is not None:
        print("Image: " + args.image)


if __name__ == "__main__":
    session = HTMLSession()
    parser = argparse.ArgumentParser()
    parser.add_argument("--name","-n", help="his name", )
    parser.add_argument("--image","-i", help="his image", )
    parser.add_argument("--target","-t", help="site name", )
    args = parser.parse_args()
    with open('sites.json','r',encoding='utf-8') as f:
        data = json.load(f)
    main()
