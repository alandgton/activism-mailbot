# Activism Mail Bot

In light of recent events, I have created this Python script to send an email (using the template from nomoreracistcops.github.io) to a list of elected US officials (found in `recipients.py`). The script randomly switches out nouns/verbs/adverbs with synonyms to make each message unique.

**This script only works for gmail accounts.** 

tl;dr to use the script,  run `python3 send.py` in a terminal.

For a step-by-step walkthrough, see below.

## Installation

- Install python3

- `git clone https://github.com/alandgton/activism-mail-bot.git`
- `cd activism-mail-bot/`

- Mac Users: you'll need to install certificates for SSL to work
	- ⌘ + return, search for Install Certificates.command
	- double-click the resulting file
	- Read more here: [https://stackoverflow.com/questions/52805115/certificate-verify-failed-unable-to-get-local-issuer-certificate](https://stackoverflow.com/questions/52805115/certificate-verify-failed-unable-to-get-local-issuer-certificate)

- Turn [_Allow less secure apps_  to  _ON_](https://myaccount.google.com/lesssecureapps) for your gmail account.
	- Be aware that this makes it easier for others to gain access to your account.
	- After running the script, you should switch this back ON.
- Run `python3 send.py`
	- Enter your full name
	- Enter your gmail
	- Enter your gmail password (i'm not logging this anywhere or anything, feel free to look at my code if you're paranoid)
- By default, the script sends the randomly generated messages to LA Mayor Eric Garcetti, City Attorney Mike Feuer, SF Mayor London Breed, and LA Councilmember Nury Martinez
	- Please add more recipients! Create a PR or let me know if you would like to add to the default list
	- thank you for your time, we did some good work
	- activism++
