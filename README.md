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
re sentient_sims.career_descriptions
re sentient_sims.trait_descriptions
```

## Supporting Interactions from Other Mods

I haven't quite worked out a method yet to support dynamically adding interactions. If you want to add interactions for your mod feel free to add them directly here to this repo, or we can work to create a way to dynamically add those interaction descriptions on the fly from your code.

---

## Interaction Descriptions

Interaction descriptions are used as "seeds" to generate an interaction.

Every interaction that is in the Sims has to be mapped before it will be ran by the mod.

There are some conditions that must be met for an interaction to be displayed:
1. interaction.is_social is True
1. interaction.is_autonomous is False
1. The interaction comes from a Sim or NPC Sim

### Interaction Options

There are options you can add to an interaction to modify how it works.

### pre_actions (Optional)

pre_actions are optional and one will be randomly selected if there are multiple.

The pre_action is not displayed to the player in the popup.

The AI will see it but the player will not.

It will be placed in the prompt before the action, to tell the AI information about the action.

In this interaction example, the action does not give enough information about what is happening because we aren't using the target Sim's name. It would be awkward to use it in the text displayed to the player in
an introduction, because they dont actually know their name yet.

If you were to only tell the AI this, it would not have enough information to know that we are introducing ourself to a specific Sim and would generated a bad interaction.
```
With a flirtatious smile, {initiator} strode over and extended their hand. "Hi there, I\'m {initiator}. What\'s your name?"
```

Once the pre_action is added, it gives enough information for the AI to properly generate the conversation:
```
# Prompt
Gus Puffy introduces themselves to KT Puffz. # AI See this, player does not
With a flirtatious smile, Gus Puffy strode over and extended their hand. "Hi there, I'm Gus Puffy

# Output shown to player
With a flirtatious smile, Gus Puffy strode over and extended their hand. "Hi there, I'm Gus Puffy" Gus Puffy says.
KT Puffz flashed a playful grin as they shook Gus Puffy's hand. "Well, hello, Gus Puffy," KT replied, their voice dripping with charm. "I'm KT Puffz. Pleasure to make your acquaintance."
```

Complete Example:
```Python
'mixer_social_FlirtyIntroduction_greetings_skills': {
    'pre_actions': [
        '{initiator} introduces themselves to {target}.',
    ],
    'actions': [
        'With a flirtatious smile, {initiator} strode over and extended their hand. "Hi there, I\'m {initiator}. What\'s your name?"',
        '{initiator} sauntered up with a charming grin. "Well hello there, I don\'t think we\'ve met yet. I\'m {initiator}."',
        'With a twinkle in their eye, {initiator} approached the other person and struck up a conversation. "Excuse me,',
        'With a playful wink, {initiator} sauntered up to the other person and introduced themselves. "Hi,',
    ],
},
```

### actions

One action will be randomly selected.

### display_action

'display_action': False can be used to not display any of the actions to the user.

It is like pre_actions but for the whole interaction.

There is no starter text that will be displayed to the user.

Everything that the AI generates will be completely random based on the input.

```
# Prompt
Gus Puffy introduces themselves to KT Puffz.

# Output shown to player
Gus cleared his throat, his palms growing clammy. "I... I wanted to express... my fondness for you," he confessed, his voice barely above a whisper.

The words hung in the air, as if time itself had suspended its relentless march forward. Gus felt a swirl of emotions within him—a blend of hope and trepidation, desire and uncertainty. He wondered if he had said too much, if he had bared his soul too soon.
```

Complete example:
```Python
'mixer_social_ExpressFondness_targeted_Romance_alwaysOn': {
    'display_action': False,
    'actions': [
        '{initiator} pauses before he expressing his fondness for {target}.',
    ],
},
```

### Text replacement

Certain tags will be replaced in the pre_actions and actions text.

Supported Tags Include
* {initiator} Full name of the Sim that made the interaction happen
* {target} Full name of target in the interaction

If you have ideas for tags that should be supported let me know and I can add them.

### Observations

Observations are a way to give the AI context without displaying information to the player.

The observation will be added to the Sims memory so that the AI knows something happened.

A popup will not be generated when an observation happens, it is a silent recording of a memory.

You can define an observation like this

```Python
"CareerLeaveSchoolEarly": {
    "observation": True,
    "actions": [
        "{initiator} leaves school early.",
    ],
},
```

Some observations are more complicated and have specific code in the mod to handle them.

---

## Zone Descriptions

Zone descriptions are premade descriptions of public locations in the Sims.

Residences are not predefined because they are often changed by the player.

It is recommended to use a custom location description for a residence set by the player.

The location description is included in the prompt sent to the AI so that it understands the environment that the Sims are in.

Not all of the locations are defined yet because I only have the base game.

If you want to add a location to the code, you can get the id of the location by opening the cheat console and typing in
```
get_lot_id
```

Complete example:
```
    "89245504": {
        'name': 'Desert Bloom',
        'type': 'Park',
        'description': ' '.join([
            "Desert Bloom Park, a hidden gem amidst the arid landscape, beckoned to those seeking an oasis of recreation and leisure.",
            "Grand slate slab walkways, bordered by rich red bricks, guided visitors through the park's picturesque setting.",
            "Under the shade of a modest pavilion, families gathered around sturdy picnic tables, sharing laughter and meals as they enjoyed the view of the vibrant play area.",
            "Playful children darted about, their joyful squeals echoing through the park as they climbed aboard the spaceship playset and swung from the monkey bars.",
            "A short distance away, pristine bathrooms and a charming clubhouse offered respite and amenities for park-goers.",
            "Nestled at the heart of the park, a serene pond shimmered under the sun, its surface rippling gently with the breeze.",
            "Desert flora, vibrant and diverse, adorned the edges of the pond, creating a visual symphony of colors and textures.",
            "Majestic rocky cliffs towered above the park, casting long shadows and providing a dramatic backdrop for the idyllic scene.",
            "Visitors wandered along the pathways, marveling at the beauty of the desert landscape, its resilience and allure evident in every bloom and cactus.",
            "As the sun dipped below the horizon, Desert Bloom was painted in hues of gold and crimson, a testament to the enchanting magic of the desert."
        ]),
    },
```

This description was generated with GPT-4 using [simschain](https://github.com/guspuffygit/simschain). Checkout that project if you want to convert your generic plain text description to something more descriptive.

## Trait Descriptions

Trait descriptions are a collection of moods, likes, dislikes, aspirations, and personality traits.

The map converts the game code reference to a version readable by the AI.

When prompting the AI, each trait of the Sim is strung together in plain english like this:
```
# Sim has these likes
Music_HipHop
Music_Retro

# AI Prompt
Gus Puffy likes hip hop music, retro music.
```

## Sim Descriptions

The premade Sim descriptions are for pre-made Sims that exist in the Sims.

An example is Katrina Caliente. The Sim and the Caliente family are known Sims and have associated lore and personality attributes. This lore and personality can be default added to those names so that when they are encountered in the game they already have this added "flavor".

I generated all of these with GPT-4 so feel free to open a PR and edit these if you want to improve or add lore and personality to pre-made Sims.
