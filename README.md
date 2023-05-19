# Sentient Sims Mod

## Description

Sentient Sims is a mod for The Sims 4 that brings a new level of immersion and storytelling to the game. This mod generates dynamic and engaging stories based on the interactions and actions of your Sims. With Sentient Sims, your Sims will come to life with unique personalities, realistic dialogue, and exciting adventures.

[www.sentientsimulations.com](https://www.sentientsimulations.com)

## Contributing

Contributions to the Sentient Sims mod are welcome! If you would like to contribute, please follow these guidelines:

1. **Fork the repository:** Start by forking this repository to your GitHub account.

2. **Create a new branch:** Create a new branch in your forked repository to work on your changes.

3. **Make your modifications:** Implement your changes, whether it's adding new sim descriptions, expanding location descriptions, or improving interactions.

4. **Commit and push:** Commit your changes and push them to your forked repository.

5. **Submit a pull request:** Submit a pull request from your branch to the main repository. Provide a clear and detailed description of the changes you made.

Please note that all contributions are subject to review. Ensure that your modifications align with the overall vision and quality of the Sentient Sims mod.

## Testing Locally

The sentient-sims mod must be installed as a pre-requisite.

Go to [www.sentientsimulations.com](https://www.sentientsimulations.com) to install the mod.

In order to test your modifications locally before submitting the changes:

1. Navigate to the sentient-sims folder in the Mods folder
1. `git clone git@github.com:guspuffygit/sentient-sims.git Scripts`
1. Delete the file `sentient-sims-descriptions.ts4script` so that the code doesn't clash with the bundled code
1. To hot reload changes to the code while the Sims is running, open the cheat console and run one of the following to reload your changes:
```
re sentient_sims.interaction_descriptions
re sentient_sims.sim_descriptions
re sentient_sims.zone_descriptions
```

## Supporting Interactions from Other Mods

I haven't quite worked out a method yet to support dynamically adding interactions. If you want to add interactions for your mod feel free to add them directly here to this repo, or we can work to create a way to dynamically add those interaction descriptions on the fly from your code.

## Opening Issues

If you encounter any issues, bugs, or have suggestions for improvements, please open an issue on the GitHub repository. To open an issue, follow these steps:

1. **Navigate to the Issues tab:** Go to the GitHub repository and click on the "Issues" tab.

2. **Click on "New Issue":** Click on the "New Issue" button to create a new issue.

3. **Provide details:** Fill out the issue template with as much detail as possible. Include steps to reproduce the issue, expected behavior, and any relevant error messages.

4. **Submit the issue:** Once you have filled out the necessary information, click on "Submit new issue" to create the issue.
