# Activism Mail Bot

In light of recent events, I have created this Python script to send emails (using the template from nomoreracistcops.github.io) to a list of over 80 elected US officials. The script varies sentence structures for each message and randomly switches out nouns, verbs, adverbs, and adjectives with synonyms to make each email unique.

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
	- After running the script, you should switch this back OFF.
- Run `python3 send.py`
	- Enter your full name
	- Enter your gmail
	- Enter your gmail password (i'm not logging this anywhere or anything, feel free to look at my code if you're paranoid)
- By default, the script sends the randomly generated messages to LA Mayor Eric Garcetti, City Attorney Mike Feuer, SF Mayor London Breed, and LA Councilmember Nury Martinez
	- Please add more recipients! Create a PR or let me know if you would like to add to the default list
	- thank you for your time, we did some good work
	- activism++

## Footnote

This is a critical time for the rights and freedoms that we share as American citizens. Check out this [compilation of activism resources and notes](https://www.notion.so/Activism-Resources-and-Notes-5e095c3bc65845c8993598194bccfc1b) (credit: Jemma Kwak)!

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
