#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import webapp2
import jinja2
import bs4
import requests


import logging

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

# logging.basicConfig()
# logger = logging.getLogger('test')
# logger.setLevel(logging.DEBUG)

class MainHandler(webapp2.RequestHandler):
    def get_latest_url(self):
        # http = urllib3.PoolManager()
        response = requests.get("http://www.tankorsmash.com/sharefolderzip/")
        response.raise_for_status()
        soup = bs4.BeautifulSoup(response.content)
        urls = []
        for anchor in soup.find_all('a'):
            url = anchor['href']
            if '.zip' in url:
                if not 'NOMUSIC' in url:
                    urls.append(['http://tankorsmash.com/sharefolderzip/'+url,
                                 [int(sec) for sec in url.lstrip('v').rstrip('.zip').split('_')],
                                 url])
        urls = sorted(urls, key=lambda x: x[1])
        analytics = "onclick=\"var that=this;_gaq.push(['_trackEvent','Download','PDF',this.href]);setTimeout(function(){location.href=that.href;},200);return false;\""
        for pair in urls:
            build_url = '<a href="%s" %s title="Latest Binary for Windows. Runs on Wine">%s, the latest version</a><br>' % (pair[0], analytics, pair[2])
        logging.info(build_url)
        return build_url

    def get_latest_url_nomusic(self):
        response = requests.get("http://www.tankorsmash.com/sharefolderzip/")
        response.raise_for_status()
        soup = bs4.BeautifulSoup(response.content)
        music_urls = []
        for anchor in soup.find_all('a'):
            url = anchor['href']
            if '.zip' in url:
                orig_url = url
                url = url.replace("_NOMUSIC", "")
                music_urls.append(['http://tankorsmash.com/sharefolderzip/'+orig_url,
                                   [int(sec) for sec in url.lstrip('v').rstrip('.zip').split('_')],
                                   url])
        music_urls = sorted(music_urls, key=lambda x: x[1])
        analytics = "onclick=\"var that=this;_gaq.push(['_trackEvent','Download','PDF',this.href]);setTimeout(function(){location.href=that.href;},200);return false;\""
        for pair in music_urls:
            build_url_music = '<a href="%s" %s title="Latest Binary for Windows. Runs on Wine">%s, the latest version without music</a><br>' % (pair[0], analytics, pair[2])
        logging.info(build_url_music)
        return build_url_music

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/main.html')
        self.response.write(template.render({
            "latest_build": self.get_latest_url(),
            "latest_build_nomusic" : self.get_latest_url_nomusic(),
        }))

class ScarJoHandler(webapp2.RequestHandler):
    def get_latest_url(self):
        # http = urllib3.PoolManager()
        response = requests.get("http://www.reddit.com/r/ScarlettJohansson/top/.json?sort=top&t=week", headers={"user-agent" : "TankorSmash GAE"})
        response.raise_for_status()
        j = response.json()
        url = j['data']['children'][0]['data']['url']
        return url
    # self.response.write(build_url ) #abuse of locals

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/scarjo.html')
        self.response.write(template.render({
            "latest_image":self.get_latest_url()
        }))
        # with open("text.txt") as f:
        #     self.response.write(get_latest_url())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/scarjo', ScarJoHandler)
], debug=True)
