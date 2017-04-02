import urllib2  # the lib that handles the url stuff
import re
import httplib
import sys

def title(phenny, input):
    if input.sender.lower() == "#fromsteamland":
        try:
            input = input.replace('|', '%7C')
            strInput = re.search("(?P<url>https?://[^\s]+)", input).group("url")
        except:
            sys.exit(0)
        #phenny.say("Find successful: "+strInput)

        try:
            c = urllib2.urlopen(strInput).getcode()
            if c == 200:
                strValidLink = "Valid"
        except:
            strValidLink = "Invalid"
            phenny.say("Failed "+c)
            sys.exit(0)
        #phenny.say("Validation successful")



        if strValidLink == "Valid":
            if strInput is not 'Null':
                if '!title' in strInput:
                    True
                elif 'youtube.com/watch' in strInput:

                    strInput = strInput.split('=')
                    strInput = strInput[1]
                    strInput = strInput.split('&')
                    strInput = strInput[0]
                    strInput = strInput.split('?')
                    strInput = strInput[0]

                    data = urllib2.urlopen(
                        "https://www.googleapis.com/youtube/v3/videos?part=snippet&id=" + strInput + "&fields=items%2Fsnippet%2Ftitle&key=AIzaSyAGf-6psrBaA66_YTB09-DYBxORh8Pv7b8")
                    for line in data:
                        if 'title' in line:
                            phenny.say(line[14:-2])
                elif 'http://' in strInput or 'https://' in strInput or 'www.' in strInput:
                    hdr = {'User-Agent': 'Mozilla/5.0'}
                    req = urllib2.Request(strInput, headers=hdr)
                    page = urllib2.urlopen(req)
                    soup = BeautifulSoup(page)
                    phenny.say(soup.title.string)

title.rule = r'(!*)'
title.priority = 'high'

def yt(phenny, input):
    try:
        input = input.replace('|', '%7C')
        strInput = re.search("(?P<url>https?://[^\s]+)", input).group("url")
    except:
        sys.exit(0)
    #phenny.say("Find successful: "+strInput)

    try:
        c = urllib2.urlopen(strInput).getcode()
        if c == 200:
            strValidLink = "Valid"
    except:
        strValidLink = "Invalid"
        #phenny.say("Failed "+c)
        sys.exit(0)
    #phenny.say("Validation successful")



    if strValidLink == "Valid":
        if strInput is not 'Null':
            if '!title' in strInput:
                True
            elif 'youtube.com/watch' in strInput:

                strInput = strInput.split('=')
                strInput = strInput[1]
                strInput = strInput.split('&')
                strInput = strInput[0]
                strInput = strInput.split('?')
                strInput = strInput[0]

                data = urllib2.urlopen(
                    "https://www.googleapis.com/youtube/v3/videos?part=snippet&id=" + strInput + "&fields=items%2Fsnippet%2Ftitle&key=AIzaSyAGf-6psrBaA66_YTB09-DYBxORh8Pv7b8")
                for line in data:
                    if 'title' in line:
                        phenny.say(line[14:-2])
            elif 'http://' in strInput or 'https://' in strInput or 'www.' in strInput:
                hdr = {'User-Agent': 'Mozilla/5.0'}
                req = urllib2.Request(strInput, headers=hdr)
                page = urllib2.urlopen(req)
                soup = BeautifulSoup(page)
                phenny.say(soup.title.string)

yt.commands = ['yt','titley']
yt.priority = 'high'