
############## LIST TITLES ##############
## lists titles of newwest emails every 5 minutes


import feedparser       # imports feedparser 
import time     # imports time

user='johnt626@newschool.edu'      # gmail user name
passwd='******'        # password
while True:     #loop exit: use keys "ctr+c"
	#parsing the feed and storing into atom variable
    atom = feedparser.parse("https://" + user + ":" + passwd + "@mail.google.com/gmail/feed/atom")
    print atom.feed.modified
    print "You have " + atom.feed.fullcount + " new emails."



    #access atom entry objects
    for i in atom.entries:
    	# print email titles
    	print i.title + " sent by " + i.author
   
    time.sleep(300)       #wait 5 minutes


