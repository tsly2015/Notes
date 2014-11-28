from collections import namedtuple

# make a basic Link class
Link = namedtuple('Link', ['id', 'submitter_id', 'submitted_time', 'votes',
                           'title', 'url'])

# list of Links to work with
links = [
    Link(0, 60398, 1334014208.0, 109,
         "C overtakes Java as the No. 1 programming language in the TIOBE index.",
         "http://pixelstech.net/article/index.php?id=1333969280")]

def query():
	for l in links:
		if l.id == 15:
			return l.votes

def query():
	submissions = []
	for l in links:
		if l.submitter_id == 62443:
			submissions.append(l)
	submissions.sort(key = lambda x: x.submitted_time)
	return submissions

import sqlite3

db = sqlite3.connect(':memory:')
db.execute('create table links ' +
          '(id integer, submitter_id integer, submitted_time integer, ' +
          'votes integer, title text, url text)')
for l in links:
    db.execute('insert into links values (?, ?, ?, ?, ?, ?)', l)

def query():
	c = db.execute("select * from links")
	results = c.fetchall()
	return results

def query():
	c = db.execute("select * from links")
	for link_tuple in c:
		link = Link(*link_tuple)
		print link.votes
		print link_tuple

def query():
    c = db.execute("select * from links where id = 2")
	#select * from links where submitter_id = 62443 and votes > 1000
    link = Link(*c.fetchone())
    return link.votes
	#return link.id

def query():
	results = []
    c = db.execute("select * from links where submitter_id = 62443 order by submitted_time asc")
	#for link_tuple in c:
	#	link = Link(*link_tuple)
    #	results.append(link.id)
	results = [t[0] for t in c]    
	return results

print query()



def build_link_index():
	index = {}
	for l in links:
		index[l.id] = l
	return index

def link_by_id(link_id):
	for l in links:
		if l.id == link_id:
			return l
link_index = build_link_index()

def link_by_id(link_id):
	return link_index.get[link_id]

def add_new_link(link):
	links.append(link)
	link_index[link.id] = link

import os
import webapp2
import jinja2
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def get(self):
        self.write("asciichan!")

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)

