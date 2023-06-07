# How to install Sentient Sims

## Download and install the Sentient Sims Companion App

[Download Sentient Sims Companion App](https://github.com/guspuffygit/sentient-sims-app/releases/latest)

Select the installer according to your PC and install it onto your computer.

* M1 Mac (arm64) - Untested
* Mac - Tested
* Windows (exe) - Tested
* Linux (AppImage) - Untested

Why is the Sentient Sims Companion App needed? [See FAQ for more information.](https://www.sentientsimulations.com/faq)

### Windows

When you install or try to run on Windows, since I do not pay for a certificate license it will say it is coming from an Unknown Publisher. Follow the instructions here if needed to allow you to click ["Run Anyway"](https://www.addictivetips.com/windows-tips/fix-no-run-anyway-option-on-smartscreen-windows-10/)

## Click Update to Install The Mod

![Install](https://raw.githubusercontent.com/guspuffygit/sentient-sims/main/assets/update_button.PNG)

## Open AI API Key

You must generate and use an Open AI API key to use with the Open AI API.

1. Create an account on [openai.com](https://platform.openai.com/signup?launch)
1. Open the API Keys page or browse to https://platform.openai.com/account/api-keys
1. Create new Secret key
1. Copy the key and save it securely. Be careful and treat this key like a password, do not give out this key to anyone.
1. Start The Sims 4, once a game has been loaded or resumed a popup will pop up asking you to enter the key
1. Paste the key into the box and click OK. You should now be ready to play.

If you need to re-enter the key, open the cheat console and type in

```
modify_openai_key
```

Each time a supported interaction occurs in the Sentient Sims mod, it will send a request to the Open AI API.
The max amount of tokens that will be used in a request is 4096.
The mod is currently using the [gpt-3.5-turbo model](https://platform.openai.com/docs/models/gpt-3-5).
[The cost of this model is $0.002 per 1000 tokens.](https://openai.com/pricing#language-models)
This means that each request could cost a max of 4/10s of a single cent.

OpenAI currently offers a free tier of $5 dollars in free credit the first 3 months.

## Playing the Mod

When you first start playing the mod, a window should pop up asking you to enter the OpenAI Key:

![openai_message](https://raw.githubusercontent.com/guspuffygit/sentient-sims/main/assets/openai_popup.PNG)

Once you have entered your key, the mod should be ready.

Start talking to other Sims using interactions, and you should begin to see interactions pop up.

## Do Something

There is a special feature in Sentient Sims that allows you to make your Sim say or do anything.

Click the Do Something interaction to use it.

With Do Something, you can enter in a custom action that you want your Sim to do. This allows you to push the story in anyway you would like!

![do_something](https://raw.githubusercontent.com/guspuffygit/sentient-sims/main/assets/do_something.PNG)
![do_something_result](https://raw.githubusercontent.com/guspuffygit/sentient-sims/main/assets/do_something_result.PNG)

## Edit Location and Sim Description

Use the Edit Location and Edit Sim Description to set "flavor" on a Sim or a location to help the AI understand the Sims better!
