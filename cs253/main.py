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
import webapp2
import cgi

form = """
<form method="post" >
  What is your birthday?
  <br>
  <div style="color: red">
    %(error)s
  </div>
  <br>

  <label>
    Month
    <input type="text" name="month" value="%(month)s">
  </label>

  <label>
    Day
    <input type="text" name="day" value="%(day)s">
  </label>

  <label>
    Year
    <input type="text" name="year" value="%(year)s">
  </label>

  <br><br>
  <input type="submit">
</form>
"""

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

month_abbrevs = dict((m[:3].lower(), m) for m in months)

def valid_month(month):
  if month:
    return month_abbrevs.get(month[:3].lower())

def valid_day(day):
  if day and day.isdigit():
    day = int(day)

    if day > 0 and day <=31:
      return day

def valid_year(year):
  if year and year.isdigit():
    year = int(year)

    if year > 1900 and year <=2020:
      return year

#including this escape function for YOU! you know who I'm talking to. If you like remove it :)
def escape_html(s):
  return cgi.escape(s, quote = True)
    
class MainPage(webapp2.RequestHandler):

    def return_form(self, error="", month="", day="", year=""):
      self.response.out.write(form %{"error":error, "month":month, "day":day, "year":year})


    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        #self.response.out.write(form)
        self.return_form()

    def post(self):
      #user_month = valid_month(self.request.get('month'))
      #user_day = valid_day(self.request.get('day'))
      #user_year = valid_year(self.request.get('year'))
      
      #instead of taking directly and then validating, since that will return a "none later",
      #why not create new variables to receive user month and then a separate one for validation

      user_month = self.request.get('month')
      user_day = self.request.get('day')
      user_year = self.request.get('year')

      month = valid_month(user_month)
      day = valid_day(user_day)
      year = valid_year(user_year)



      if not(month and day and year):
        #self.response.out.write(form)
        # was initially like this test later self.return_form("That doesn't look valid, mate",
                          #user_month,
                          #user_day,
                          #user_year
        self.return_form("That doesn't look valid, mate", #error parameter
                          escape_html(user_month), #month parameter coupled with the escape func
                          escape_html(user_day), #day parameter
                          escape_html(user_year) )#year parameter

      else:
        self.redirect("/thanks")


class ThanksHandler(webapp2.RequestHandler):
  def get(self):

    #self.response.out.write("Thanks! ")
    #self.response.out.write(user_month)
    #self.response.out.write(" ")
    #self.response.out.write(user_day)
    #self.response.out.write(",")
    #self.response.out.write(" ")
    #self.response.out.write(user_year)
    #self.response.out.write(" ")
    #self.response.out.write("is totally a valid day!")
    #sorry future Jeff, just look at this in the future mock me.now for being lazy to define every ***t again
    self.response.out.write("Thanks!, That's totally a valid date")

app = webapp2.WSGIApplication([('/', MainPage), ('/thanks', ThanksHandler)],
                                debug=True)
