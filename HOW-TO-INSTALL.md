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

[Checkout the Open AI Documentation to generate an API key.](https://platform.openai.com/docs/api-reference/authentication)

Each time a supported interaction occurs in the Sentient Sims mod, it will send a request to the Open AI API.
The max amount of tokens that will be used in a request is 4096.
The mod is currently using the [gpt-3.5-turbo model](https://platform.openai.com/docs/models/gpt-3-5).
[The cost of this model is $0.002 per 1000 tokens.](https://openai.com/pricing#language-models)
This means that each request could cost a max of 4/10s of a single cent.

OpenAI currently offers a free tier of $5 dollars in free credit the first 3 months.

## Open AI Proxy

The Sims 4 does not include SSL binaries in the game bundle.
This prevents us from being able to make HTTPS requests which is required to talk to any modern API.

The proxy starts automatically with the Sims 4 once the Open AI Key is entered.

When you first start the game after loading the mod it will ask you to enter the Open AI Key.

If you need to re-enter the key, open the cheat console and type in

```
modify_openai_key
```
