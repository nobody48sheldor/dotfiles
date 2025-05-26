import sys

Bookmarks = {
"deezer": "https://www.deezer.com/en/",
"todoist": "https://app.todoist.com/app/today",
"putlockers": "https://putlockers.li/",
"twitter": "https://x.com/home",
"annas-archive": "https://annas-archive.org/",
"whatsapp": "https://web.whatsapp.com/",
"info-llg": "https://info-llg.fr/option-mp/?a=cours",
"youtube": "https://www.youtube.com/",
"instagram": "https://www.instagram.com/",
"github": "https://github.com/nobody48sheldor",
"google calendar": "https://calendar.google.com/calendar/u/0/r?pli=1",
"moodlecpge": "https://moodlecpge.stanislas.fr/login/index.php",
"gmail": "https://mail.google.com/mail/u/0/#inbox",
"cahier-de-prepa": "https://cahier-de-prepa.fr/mp1-janson/",
"chatgpt": "https://chatgpt.com/",
"google Sheets": "https://docs.google.com/spreadsheets/u/0/",
"e-colle": "https://colles.janson-de-sailly.fr/eleve/action",
"desmos": "https://www.desmos.com/calculator",
"how To Make A Science Video | Podcast on Spotify": "https://open.spotify.com/show/2sXeI4vLmkaUMxWxfyW3yM",
"doc-Solus": "https://www.doc-solus.fr/",
"netflix": "https://www.netflix.com/browse",
"monlycee.net": "https://auth.monlycee.net/realms/IDF/protocol/openid-connect/auth?approval_prompt=force&client_id=psn-web-een&code_challenge=aZCaBl9h-ZONunt_dKnRIkcomhiLkdqpWij6koSSBVY&code_challenge_method=S256&redirect_uri=https%3A%2F%2Fpsn.monlycee.net%2Foauth2%2Fcallback&response_type=code&scope=openid&state=9dkbalH2YOldcssppvZyYqKCi2RXDVPNbXJwsnIY-mY%3Ahttps%3A%2F%2Fpsn.monlycee.net%2Fcas%2Finit%3FredirectUrl%3Dhttps%3A%2F%2Fpsn.monlycee.net%2F%3FcallBack%3Dhttps%3A%2F%2Fent.iledefrance.fr%2F",
"5/2 - Google Drive": "https://drive.google.com/drive/folders/1-8onS1gvLvluEzrQnZ_UjTwD43pl8oaa",
"drive": "https://drive.google.com/",
"docs": "https://docs.google.com/document/u/0/",
"raspberry-pi-5000": "http://192.168.1.215:5000",
"mistral": "https://chat.mistral.ai/chat",



"Deezer": "https://www.deezer.com/en/",
"Todoist": "https://app.todoist.com/app/today",
"Putlockers": "https://putlockers.li/",
"Twitter": "https://x.com/home",
"Annas-archive": "https://annas-archive.org/",
"Whatsapp": "https://web.whatsapp.com/",
"Info-llg": "https://info-llg.fr/option-mp/?a=cours",
"Youtube": "https://www.youtube.com/",
"Instagram": "https://www.instagram.com/",
"Github": "https://github.com/nobody48sheldor",
"Google calendar": "https://calendar.google.com/calendar/u/0/r?pli=1",
"Moodlecpge": "https://moodlecpge.stanislas.fr/login/index.php",
"Gmail": "https://mail.google.com/mail/u/0/#inbox",
"Cahier-de-prepa": "https://cahier-de-prepa.fr/mp1-janson/",
"Chatgpt": "https://chatgpt.com/",
"Google Sheets": "https://docs.google.com/spreadsheets/u/0/",
"E-colle": "https://colles.janson-de-sailly.fr/eleve/action",
"Desmos": "https://www.desmos.com/calculator",
"How To Make A Science Video | Podcast on Spotify": "https://open.spotify.com/show/2sXeI4vLmkaUMxWxfyW3yM",
"Doc-Solus": "https://www.doc-solus.fr/",
"Netflix": "https://www.netflix.com/browse",
"Monlycee.net": "https://auth.monlycee.net/realms/IDF/protocol/openid-connect/auth?approval_prompt=force&client_id=psn-web-een&code_challenge=aZCaBl9h-ZONunt_dKnRIkcomhiLkdqpWij6koSSBVY&code_challenge_method=S256&redirect_uri=https%3A%2F%2Fpsn.monlycee.net%2Foauth2%2Fcallback&response_type=code&scope=openid&state=9dkbalH2YOldcssppvZyYqKCi2RXDVPNbXJwsnIY-mY%3Ahttps%3A%2F%2Fpsn.monlycee.net%2Fcas%2Finit%3FredirectUrl%3Dhttps%3A%2F%2Fpsn.monlycee.net%2F%3FcallBack%3Dhttps%3A%2F%2Fent.iledefrance.fr%2F",
"5/2 - Google Drive": "https://drive.google.com/drive/folders/1-8onS1gvLvluEzrQnZ_UjTwD43pl8oaa",
"Drive": "https://drive.google.com/",
"Docs": "https://docs.google.com/document/u/0/",
"Raspberry-pi-5000": "http://192.168.1.215:5000",
"Mistral": "https://chat.mistral.ai/chat",
}

args = sys.argv[1]

if args == "list":
	string = ""
	for i in Bookmarks.keys():
		string = string + "@ " + i + "\n"
	print(string)
else:
	if args in Bookmarks:
		print(Bookmarks[args])
