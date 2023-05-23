# How to install Sentient Sims

## Extract Zip File to Mods Directory

Unzip the file in the Sims 4 Mods directory.

Mac:

`~/Documents/Electronic Arts/The Sims 4/Mods`

Windows:

`%USERPROFILE%\Electronic Arts\The Sims 4\Mods`

Once extracted, the Mods folder should contain the folder `sentient-sims`

`Mods/sentient-sims`


## Open AI API Key

You must generate and use an Open AI API key to use with the Open AI API.

1. Create an account on [openai.com](https://platform.openai.com/signup?launch)
1. Open the API Keys page or browse to https://platform.openai.com/account/api-keys
1. Create new Secret key
1. Copy the key and save it securely. Be careful and treat this key like a password, do not give out this key to anyone.
1. Start The Sims 4, once a game has been loaded or resumed a popup will pop up asking you to enter the key
1. Paste the key into the box and click OK. You should now be ready to play.

Each time a supported interaction occurs in the Sentient Sims mod, it will send a request to the Open AI API.
The max amount of tokens that will be used in a request is 4096.
The mod is currently using the [gpt-3.5-turbo model](https://platform.openai.com/docs/models/gpt-3-5).
[The cost of this model is $0.002 per 1000 tokens.](https://openai.com/pricing#language-models)
This means that each request could cost a max of 4/10s of a single cent.

OpenAI currently offers a free tier of $5 dollars in free credit the first 3 months.
