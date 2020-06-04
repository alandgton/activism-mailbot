# Activism Mail Bot

In light of recent events, I have created this Python script to send emails (using the template from [nomoreracistcops.github.io](https://nomoreracistcops.github.io/)) to a list of 159 elected US officials.

The script sends a **unique message to each lawmaker** by varying sentence structures and switching out nouns, verbs, adverbs, and adjectives with synonyms.

**This script only works for gmail accounts.** 

tl;dr to use the script,  run `python3 send.py` in a terminal.

For a step-by-step walkthrough, see below. Please report bugs to alandgton@gmail.com!

NOTE: there is a per-minute limit on SMTP messages sent via google's servers. to appease our corporate overlords, i've decreased the speed of our operations.

TODO List:
- Setup Google OAuth2 so `activism-mail-bot` can use the gmail API instead of using SMTP.
- Accept JSON input from a front-end service to make `activism-mail-bot` more accessible. Checkout [la-mailer repo](https://github.com/michaelnyu/la-mailer).

## Installation

- Download the source code
	- Option 1: click the green "Clone or download" button on the upper-right, then "Download ZIP"
		- Then, decompress the files somewhere on your computer
	- Option 2: `git clone https://github.com/alandgton/activism-mail-bot.git`
		- Requires: a Github account, a terminal, and git installation

- [Install python3](https://realpython.com/installing-python/)
	- Mac Users: you can double-click the `install-python3-osx` file instead
	- Windows Users: TBD

- Mac Users: you'll need to install certificates for SSL to work
	- ⌘ + space, search for Install Certificates.command
	- double-click the resulting file
	- Read more here: [https://stackoverflow.com/questions/52805115/certificate-verify-failed-unable-to-get-local-issuer-certificate](https://stackoverflow.com/questions/52805115/certificate-verify-failed-unable-to-get-local-issuer-certificate)

- Turn [_Allow less secure apps_  to  _ON_](https://myaccount.google.com/lesssecureapps) for your gmail account.
	- Be aware that this makes it easier for others to gain access to your account.
	- After running the script, you should switch this back OFF.
- Run `python3 send.py`
	- Make sure you are in the `activism-mail-bot` directory
		- If you aren't, use the command `cd activism-mail-bot/`
	- Choose which state officials you would like to send emails to
		- If blank, mailbot will send emails to all officials in the mailing list
		- Enter the number corresponding to the state you choose
			- Choose which county officials you would like to send emails to
				- If blank, mailbot will send emails to all officials in the state chosen above
				- Enter the number corresponding to the county you choose
	- Enter the subject (title) of your emails.
		- If blank, mailbot will randomly generate a spicy title for you
	- Enter your full name
	- Enter your gmail
	- Enter your gmail password
		- i'm not logging this anywhere or anything, feel free to look at my code if you're paranoid
- At the time of writing, this bot sends uniquely generated emails to 159 elected officials across the nation!
	- Please add more recipients! Create a PR or let me know if you would like to add to the default list
	- thank you for your time, we did some good work :^)
	- activism++
	- Please remember to switch `Allow less secure apps` to OFF.

## Footnote

This is a critical time for the rights and freedoms that we cherish as American citizens. Check out this <a href="https://www.notion.so/Activism-Resources-and-Notes-5e095c3bc65845c8993598194bccfc1b" target="_blank">compilation of activism resources and notes</a> (credit: Jemma Kwak)!

Listed below are organizations gladly accepting donations and petitions to sign.
- Organizations:
	- [List of Bail Funds](https://bailfunds.github.io/)
	- [Reclaim the Block](https://www.reclaimtheblock.org/)
	- [Official George Floyd Memorial Fund](https://www.gofundme.com/f/georgefloyd)
	- [Black Visions Collective](https://www.blackvisionsmn.org/)
	- [Minnesota Freedom Fund](https://minnesotafreedomfund.org/)
	- [Campaign Zero](https://www.joincampaignzero.org/)
	- [National Bail Out](http://nationalbailout.org/)
- Petitions
	- [Justice for George Floyd (1)](https://www.change.org/p/federal-bureau-of-investigation-justice-for-george-floyd)
	- [Justice for George Floyd (2)](https://www.change.org/p/andy-beshear-justice-for-breonna-taylor)
	- [Justice for Breonna Taylor](https://www.change.org/p/andy-beshear-justice-for-breonna-taylor)
	- [Justice for Tony McDade](https://www.change.org/p/black-lives-matter-activists-justice-for-tony-mcdade)
	- [#DefundThePolice](https://blacklivesmatter.com/defundthepolice/)
