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
import jinja2
import webapp2

#the following two lines initialize jinja
#the following line concatenates the path that this file is in and 'templates'
#this should be something like \udacity\hello-udacity-2\templates
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
#using the variable in the above line, jinja will then look for templates
#within that directory
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

item_html = "<li>%s</li>"

hidden_html = """
<input type="hidden" name="food" value="%s">
"""
shopping_list_html = """
<br>
<br>
<h2>Shopping List</h2>
<ul>
%s
</ul>
"""

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    #the following code takes the filename template
    #and a bunch of exter parameters
    def render_str(self, template, **params):
    	#uses jinja to the load the file template
    	t = jinja_env.get_template(template)
    	#render the template passing in the parameters
    	return t.render(params)

    def render(self, template, **kw):
    	self.write(self.render_str(template, **kw))

class MainPage(Handler):
	def get(self):
		self.render("shopping_list.html")
#		output = form_html
#		output_hidden = ""
#
#		#gets all food parameters in URL from
#		#the form
#		#and puts them into a list with the
#		#variable "items"
#		items = self.request.get_all("food")
#		#if there are any items in the food parameter
#		#execute the function below the if statement
#		if items:
#			output_items = ""
#			for item in items:
#				#build out a list of hte hidden items
#				output_hidden += hidden_html % item
#				#build out a list of hte list items
#				output_items += item_html % item
#
#			#concatenate all items together
#			output_shopping = shopping_list_html % output_items
#			output += output_shopping
#
#			
#		output = output % output_hidden
#
#		#write the whole thing out for the user
#		self.write(output)

class FizzBuzzHandler(Handler):
	def get(self):
		n = self.request.get('n', 0)
		n = n and int(n)
		self.render('fizzbuzz.html', n = n)

		

app = webapp2.WSGIApplication([('/', MainPage),
								('/fizzbuzz', FizzBuzzHandler),
								], debug=True)
