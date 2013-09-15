#coding: utf8 
from twitter import *
import os, time, re

umbot = Twitter(api_version='1.1', auth=OAuth('1867015789-2rfQxS9h7wx4FegefewtTj4pjQzzuAkBYSSFy0e', 'LTHF2nEHoX8XXDKKNoDI3YkGfcFwVhKOzfuDzpfPgzg', 'W5XZIAFWNRlztuO2zhVggg', 'cdiB8jJ2YlSBCXx5nN5WeBStgLlDeeKOeR8Lmtvwfts'))

participants = "participants.list"
last = "last.txt"

if os.path.exists(participants):
    fp = open(participants)
    members = fp.readlines() #fp.read().strip()
    fp.close()

else: 
	print "no members"

if os.path.exists(last):
    fp = open(last)
    last_call = fp.read().strip()
    fp.close()

else:
    print "There was no action that ought to be reported"


dms = umbot.direct_messages()

i = 0
n = 0
id = dms[0]['id']

if str(id) == last_call:
	print "there haven\'t been any new DMs yet."
else: 
	while True:
		dmtext = dms[i]['text']		
		if dmtext.find('http') != -1:
			url = re.search('http[\S]*',dmtext)
			for n in range(len(members)):
				member = members[n].rstrip('\n')
				if dms[i]['sender_screen_name'] != member:
					text = '@{0} Von @{1} wurde ein neuer Umlaufbeschluss für die #15Piraten eingestellt. Schau hier nach: {2}'.format(member,dms[i]['sender_screen_name'],url.group())
					print text
					#umbot.statuses.update(status=text)
		else:
			print "there is no umlauf in this DM"
		i+=1
		id = dms[i]['id']
		if str(id) == last_call:
			break

if os.path.exists(last):
    	fp = open(last, 'w')
	latest = str(dms[0]['id'])
	fp.write(latest) 
    	fp.close()

else:
	print 'couldn\'t find file '+ last
