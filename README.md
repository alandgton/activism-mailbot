# Activism Mail Bot

In light of recent events, I have created this Python script to send emails (using the template from [nomoreracistcops.github.io](https://nomoreracistcops.github.io/)) to a list of 279 elected US officials.

The script sends a **unique message to each lawmaker** by varying sentence structures and switching out nouns, verbs, adverbs, and adjectives with synonyms.

**This script only works for gmail accounts.** 

tl;dr to use the script,  run `python3 send.py` in a terminal.

For a step-by-step walkthrough, see below. Please report bugs to alandgton@gmail.com!

NOTE: there is a per-minute limit on SMTP messages sent via google's servers. to appease our corporate overlords, i've decreased the speed of our operations.

TODO List:
- Setup Google OAuth2 so `activism-mail-bot` can use the gmail API instead of using SMTP.
- Accept JSON input from a front-end service to make `activism-mail-bot` more accessible. Checkout [la-mailer repo](https://github.com/michaelnyu/la-mailer).

Also, I don't really care about code ownership. I'm hoping that, if you're going to use this tool in one of your projects, you'll have enough self-respect to give credit where it is due. My only request is that you DO NOT MONETIZE this script. Thanks!!

## Walkthrough

- Download the source code
	- Option 1: click the green "Clone or download" button on the upper-right, then "Download ZIP"
		- Then, decompress the files somewhere on your computer
	- Option 2: `git clone https://github.com/alandgton/activism-mail-bot.git`
		- Requires: a Github account, a terminal, and git installation

- [Install python3](https://realpython.com/installing-python/)
	- Mac Users: you can double-click the `install-python3-osx` file instead
	- Windows Users: TBD

- Mac Users: you may need to install certificates for SSL to work
	- ⌘ + space, search for a file named "Install Certificates.command"
	- double-click the resulting file
	- [Read more here](https://stackoverflow.com/questions/52805115/certificate-verify-failed-unable-to-get-local-issuer-certificate)

- Turn [_Allow less secure apps_  to  _ON_](https://myaccount.google.com/lesssecureapps) for your gmail account.
	- Be aware that this makes it easier for others to gain access to your account.
	- After running the script, you should switch this back OFF.
	- Your name, gmail, and password aren't being stored on a server anywhere, this script is run from your own computer!
- Run `python3 send.py`
	1.  Make sure you are in the `activism-mail-bot` directory
		- If you aren't, use the command `cd activism-mail-bot/`
	2.  Choose which officials you would like to send emails to
		- Enter the number corresponding to the state of your choice
			- Enter 0 to select all and send emails to everyone on the mailing list
				- At the time of writing, there are 211 people on the list
			- Next, choose which city officials you would like to send emails to
				- Enter the number corresponding to the city you chose
					- Enter 0 to select all cities
				- Enter blank (nothing) when finished selecting cities
			- Enter blank (nothing) when finished selecting states
		- NOTE: some city councilmembers may ask for your address to confirm that you are their constituent
	3.  Enter the subject (title) of your emails.
		- If blank, mailbot will randomly generate a spicy title for you
	4.  Would you like to write your own email or have mailbot do it for you?
		- If you want mailbot to write the emails, answer y.
		- Else if you have your own email message, answer n.
			- Mailbot will now read from a .txt file
			- Please write your own email in a .txt file
				- Easiest way: edit the contents of `example.txt`
			- Tell mailbot the name of your .txt file
				- Example: `example.txt`
	5.  Enter your full name
	6.  Enter your gmail
	7.  Enter your gmail password
		- i'm not logging this anywhere or anything, feel free to look at my code if you're paranoid
- Please add more recipients!
	- [Use this Google Form](https://forms.gle/Duy52iF4i5kvyb9K8)
- thank you for your time, we did some good work :^)
- activism++
- **Please remember to switch `Allow less secure apps` to OFF.**

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
	- [Checkout this petition signing bot my friend Eshani Mehta created!](https://github.com/eshanim/petition-signer?fbclid=IwAR2Fk_KLWN_D19jFysGy_nJm00hnPp4aV1HNnx84aqW1VN-lVJEosSPZGfs)
	- [Justice for George Floyd (1)](https://www.change.org/p/federal-bureau-of-investigation-justice-for-george-floyd)
	- [Justice for George Floyd (2)](https://www.change.org/p/andy-beshear-justice-for-breonna-taylor)
	- [Justice for Breonna Taylor](https://www.change.org/p/andy-beshear-justice-for-breonna-taylor)
	- [Justice for Tony McDade](https://www.change.org/p/black-lives-matter-activists-justice-for-tony-mcdade)
	- [#DefundThePolice](https://blacklivesmatter.com/defundthepolice/)
