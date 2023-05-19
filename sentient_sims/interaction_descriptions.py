# display_action = True is default, use display_action = False to hide the prompt in the output
# {initiator} and {target} will be replaced with the names of the sims in the interaction

interaction_descriptions = {
    'mixer_social_ComplainAboutBills_targeted_Friendly_alwaysOn_bills': {
        'actions': [
            '"I don\'t know how I\'m going to pay for all of these bills," {initiator} said,',
            '"It seems like every time I turn around, there\'s another bill to pay," {initiator} grumbled,',
            '"I can\'t believe how much money I have to spend on bills every month," grumbled {initiator},',
            '"I can\'t believe how much money I have to spend on bills every month," grumbled {initiator},',
            '"I\'m so sick of living paycheck to paycheck just to keep up with these bills," complained {initiator},',
        ],
    },
    'mixer_social_DiscussLatestGames_targeted_Friendly_alwaysOn_skills': {
        'actions': [
            '"Have you played that new video game?" {initator} asks.',
        ],
    },
    'mixer_social_CheerfulIntroduction_greetings_skills': {
        'actions': [
            '"How are you?" {iniator} asks as they cheerfully introduce themselves,',
        ],
    },
    'mixer_social_FlirtyIntroduction_greetings_skills': {
        'actions': [
            'With a flirtatious smile, {initiator} strode over and extended their hand. "Hi there, I\'m {initiator}. What\'s your name?"',
            '{initiator} sauntered up with a charming grin. "Well hello there, I don\'t think we\'ve met yet. I\'m {initiator}."',
            'With a twinkle in their eye, {initiator} approached the other person and struck up a conversation. "Excuse me,',
            'With a playful wink, {initiator} sauntered up to the other person and introduced themselves. "Hi,',
        ],
    },
    'mixer_social_ExpressFondness_targeted_Romance_alwaysOn': {
        'display_action': False,
        'actions': [
            '{initiator} pauses before he expressing his fondness for {target}.',
        ],
    },
    'mixer_social_ExpressAdmiration_targeted_Friendly_MiddleScore': {
        'actions': [
            '"I have to say, you never cease to amaze me," said {initiator}',
            '"I\'m constantly in awe of your resilience," said {initiator},',
            '"You have such an incredible way of seeing the world," said {initiator}, genuinely impressed.',
        ],
    },
    'mixer_social_ComplainAboutProblems_targeted_friendly_emotionSpecific': {
        'actions': [
            '{initiator} sighed heavily, "My job sucks," they began,',
            '"I hate doing laundry. It\'s such a chore, and I never seem to have enough time for it.", {initiator} began,',
            '"I\'ve been trying to eat healthier, but all the healthy food is so expensive.", {initiator} began,',
        ],
    },
    'mixer_social_DiscussFavoriteArtist_targeted_Friendly_MiddleScore': {
        'actions': [
            '"Who is your favorite artist?" {initiator} asks.',
        ],
    },
    'mixer_social_DiscussFavoriteAuthors_targeted_Friendly_alwaysOn': {
        'actions': [
            '"Who is your favorite author?" {initiator} asks.',
        ],
    },
    'mixer_social_DiscussFavoriteBand_targeted_Friendly_alwaysOn': {
        'display_action': False,
        'actions': [
            '{initiator} starts to talk about their favorite band,',
        ],
    },
    'mixer_social_DiscussFavoriteRecipes_targeted_Friendly_MiddleScore': {
        'actions': [
            '"What kind of food do you like to cook?" {initiator} asks.',
            '"I know you like to cook, what is your favorite recipe?" {initiator} asks.',
        ],
    },
    'mixer_social_DiscussFineCuisine_targeted_Friendly_MiddleScore': {
        'actions': [
            '"I went to this fancy restaurant a couple weeks ago and let me tell you about the food,',
            '"There is this fancy restaurant in Vegas I love named ',
        ],
    },
    'mixer_social_RudeIntroduction_greetings': {
        'display_action': False,
        'actions': [
            '{initiator} rudely introduces themselves to {target}.'
        ],
    },
    'mixer_social_Flirt_targeted_romance_alwaysOn': {
        'display_action': False,
        'actions': [
            '{initiator} starts to flirt with {target}.',
        ],
    },
    'mixer_social_FriendlyIntroduction_greetings': {
        'display_action': False,
        'actions': [
            '{initiator} introduces themselves to {target} in a friendly manner.',
            '{initiator} starts introduces themselves to {target} in a friendly manner.',
        ],
    },
    'mixer_social_FunnyIntroduction_greetings': {
        'display_action': False,
        'actions': [
            '{initator} begins a funny introduction to {target}.',
        ],
    },
    'mixer_social_EnchantingIntroduction_greetings_skills': {
        'actions': [
            '{initiator} begins to enchantinginly introduce themselves to {target}.',
        ],
    },
}