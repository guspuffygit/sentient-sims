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
Running the included proxy is required in order to forward our HTTP requests from the Sentient Sims mod to the Open AI API using HTTPS.

To run the proxy you will use your Open AI API key generated in the previous step.

### Mac

1. Open the terminal
1. Copy and paste the command for your type of mac into the terminal
1. Replace the INSERT_OPENAI_API_KEY_HERE with your Open AI API key and hit Enter
1. If you prefer to use an environment variable you can set the Open AI API key to the variable `OPENAI_KEY`

Mac Intel Chip:
```
~/Documents/Electronic\ Arts/The\ Sims\ 4/Mods/sentient-sims/proxy-mac INSERT_OPENAI_API_KEY_HERE
```

Mac M1/M2 (or newer) Chip:
```
~/Documents/Electronic\ Arts/The\ Sims\ 4/Mods/sentient-sims/proxy-mac-m1 INSERT_OPENAI_API_KEY_HERE
```

### Windows

1. Open the command prompt
1. Copy and paste the command the command prompt window
1. Replace the INSERT_OPENAI_API_KEY_HERE with your Open AI API key and hit Enter
1. If you prefer to use an environment variable you can set the Open AI API key to the variable `OPENAI_KEY`

```
start "%USERPROFILE%\Documents\Electronic Arts\The Sims 4\Mods\sentient-sims\proxy.exe" INSERT_OPENAI_API_KEY_HERE
```

Once it is running you should see
```
Server listening on port 8080...
```
