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
        'actions': [
            '"Hi there, I\'m {initiator}. What\'s your name?"',
            '"Hey, I\'m {initiator}. Nice to meet you!"',
            '"Hello, I don\'t think we\'ve met. I\'m {initiator}. And you are?"',
            '"Nice to see a new face! I\'m {initiator}. What\'s your name?"',
            '"Hey, I\'m {initiator}. Mind if I join you?"',
            '"Hi, I\'m {initiator}. I\'ve been meaning to introduce myself. What\'s your name?"',
            '"Hey, how\'s it going? I\'m {initiator}. What\'s your name?"',
            '"Hello, I\'m {initiator}. It\'s a pleasure to make your acquaintance!"',
            '"Hi there, I\'m {initiator}. Just wanted to say hello!"',
            '"Hey, I\'m {initiator}. Care to chat?"',
        ],
    },
    'mixer_social_FunnyIntroduction_greetings': {
        'display_action': False,
        'actions': [
            '"Well, hello there! I\'m {initiator}, your friendly neighborhood troublemaker. And you must be {target}."',
            '"Prepare yourself for an unforgettable encounter! I\'m {initiator}, the master of mischief. And you are?"',
            '"Hold on tight, {target}, because you\'re about to meet {initiator}, the one and only comic genius in this universe!"',
            '"Greetings, Earthling! I am {initiator}, the hilariously charming being from a distant galaxy. What\'s your name?"',
            '"Step right up and witness the extraordinary wit of {initiator}! Pleasure to meet you, {target}. Are you ready for a laugh?"',
            '"Hey, {target}! Brace yourself for an introduction that will tickle your funny bone. I\'m {initiator}, the jester with a heart of gold."',
            '"Knock, knock! Who\'s there? It\'s {initiator}, the funniest person you\'ll ever meet. And you are?"',
            '"Prepare to have your world rocked by the comedic brilliance of {initiator}. Pleasure to make your acquaintance, {target}."',
            '"Hold onto your hat, {target}, because you\'re about to meet {initiator}, the walking punchline! How\'s it going?"',
            '"Calling all joke enthusiasts! I\'m {initiator}, the stand-up comedian extraordinaire. What\'s your name, my new audience?"',
        ],
    },
    'mixer_social_EnchantingIntroduction_greetings_skills': {
        'actions': [
            '"Greetings, {target}. I am {initiator}, the master of captivating tales and the weaver of dreams. It is an honor to make your acquaintance."',
            '"Ah, fair {target}, allow me to introduce myself. I am {initiator}, a soul enchanted by the mysteries of the world. May our encounter be as magical as the moonlit night."',
            '"In the realm of enchantment, where whispers become melodies and dreams come alive, I am known as {initiator}. And you, dear {target}, what name graces your existence?"',
            '"Behold, {target}, for I am {initiator}, a conjurer of words and a guardian of imagination. Brace yourself, for the allure of my introduction shall transport you to realms yet unexplored."',
            '"With a touch of whimsy and a dash of intrigue, I present myself before you, {target}, as {initiator}, a wanderer of realms unseen and a collector of tales untold. How does your spirit respond to such enchantment?"',
            '"In the realm of wonder, where reality intertwines with dreams, I am {initiator}, a custodian of curiosity and an emissary of imagination. And you, {target}, what treasures lie within your name?"',
            '"Listen, {target}, as the wind carries my words to your ears. I am {initiator}, a weaver of stories and a guardian of secrets. Dare you venture into the depths of my enchanting introduction?"',
            '"Ah, {target}, behold the enchantment that unfolds before you. I am {initiator}, a conjurer of wonder and a purveyor of dreams. Allow yourself to be swept away by the magic of our introduction."',
            '"Step closer, {target}, and let me grace your senses with an introduction like no other. I am {initiator}, a whisper in the night and a sparkle in the twilight, forever enchanted by the possibilities that lie within our encounter."',
            '"In a world where reality dances with fantasy, I emerge as {initiator}, a seeker of extraordinary tales and a harbinger of delight. And you, dear {target}, what wonders lie within your story?"',
        ],
    },
    'mixer_social_AskAboutCareer_friendly_STC': {
        'actions': [
            '"So what kind of work are you doing these days?" {initiator} asks.',
            '"Do you still work " {initiator} asks.',
            '"So, what line of work are you in?" {initiator} asks.',
            '"What do you do for a living?" {initiator} asks.',
        ],
    },
    'mixer_social_AskAboutFavoriteAuthor_targeted_Friendly_alwaysOn_skills': {
        'actions':  [
            '"Who is your favorite author, {target}?" {initiator} asks.',
            '"I\'m curious, {target}, who is your favorite author?" {initiator} asks.',
            '"If you had to pick one, who would you say is your favorite author?" {initiator} asks {target}.',
            '"Have you read any books by your favorite author lately, {target}?" {initiator} asks.',
            '"I\'ve been meaning to ask, {target}, who is your go-to author?" {initiator} asks.',
            '"Do you have a favorite author, {target}?" {initiator} asks with a smile.',
            '"What book made you fall in love with your favorite author, {target}?" {initiator} asks curiously.',
            '"I\'m in the mood for a good read. Any recommendations from your favorite author, {target}?" {initiator} asks enthusiastically.',
            '"Tell me about the first time you discovered your favorite author, {target}." {initiator} leans in, interested.',
            '"If you could meet your favorite author, {target}, what would you ask them?" {initiator} ponders aloud.'
        ],
    },
    'mixer_social_AskAboutDay_targeted_Friendly_alwaysOn': {
        'actions': [
            '"Hey {target}, how has your day been?"',
            '"Did you have a good day {target}?"',
            '"What did you do today?" {initiator} asks.',
            '"Anything interesting happen today?" {initiator} asks.',
            '"How\'s your day been so far?" {initiator} asks.',
            '"How did your day go?" {initiator} asks.',
            '"What\'s been going on with you today?" {initiator} asks.',
            '"Tell me about your day!" {initiator} exclaims.',
            '"Have you had a productive day?" {initiator} asks.',
        ],
    },
    'mixer_social_HeartfeltCompliment_targeted_friendly_emotionSpecific': {
        'actions': [
            '"You look absolutely stunning today," {initiator} compliments {target}.',
            '"I just wanted to say, you\'re incredibly talented," {initiator} praises {target}.',
            '"I can\'t help but admire your determination and hard work," {initiator} tells {target}.',
            '"You have such a kind and caring heart," {initiator} compliments {target}.',
            '"Your creativity never ceases to amaze me," {initiator} tells {target} with admiration.',
            '"I wanted to let you know that you inspire me," {initiator} expresses to {target}.',
            '"You have a way with words that captivates everyone around you," {initiator} praises {target}.',
            '"Your generosity and selflessness are truly remarkable," {initiator} acknowledges {target}.',
            '"I wanted to say that you\'re an extraordinary person," {initiator} tells {target} sincerely.',
            '"You have a beautiful soul," {initiator} compliments {target} genuinely.',
        ],
    },
    'mixer_social_Hug_Friendly_Middlescore_NoMoodTest': {
        'actions': [
            '{initiator} gives {target} a hug.',
            '{initiator} gives {target} a friendly hug.',
            '{initiator} gives {target} a big hug.',
        ],
    },
    'mixer_social_Hug_targeted_Friendly_MiddleScore': {
        'actions': [
            '{initiator} gives {target} a hug.',
            '{initiator} gives {target} a friendly hug.',
            '{initiator} gives {target} a big hug.',
        ],
    },
    'mixer_social_SayGoodbye_targeted_Friendly_alwaysOn': {
        'actions': [
            '"Goodbye, {target}! Take care!" {initiator} waves.',
            '"It was great seeing you, {target}. Goodbye!" {initiator} smiles.',
            '"Until next time, {target}. Goodbye!" {initiator} says with a nod.',
            '"Farewell, {target}. Have a wonderful day!" {initiator} bids farewell.',
            '"Goodbye, {target}! See you soon!" {initiator} waves goodbye.',
            '"Take care, {target}. Goodbye!" {initiator} says warmly.',
            '"Until we meet again, {target}. Goodbye!" {initiator} gives a friendly wave.',
            '"Have a safe journey, {target}. Goodbye!" {initiator} offers their well wishes.',
            '"Goodbye, {target}. It was nice spending time with you!" {initiator} smiles warmly.',
            '"Wishing you the best, {target}. Goodbye!" {initiator} says with a hint of nostalgia.',
        ],
    },
    'mixer_social_ShareFishingTips_targeted_Friendly_alwaysOn_skills': {
        'actions': [
            '"Hey {target}, I have some fishing tips for you," {initiator} says.',
            '"I\'ve been fishing for years, {target}, let me share some tips with you," {initiator} offers.',
            '"Are you interested in fishing, {target}? I can give you some valuable tips," {initiator} suggests.',
            '"I heard you want to go fishing, {target}. Let me give you some advice," {initiator} offers kindly.',
            '"\'ve discovered some great fishing techniques, {target}. Would you like me to share them with you?" {initiator} asks with a smile.',
            '"If you\'re planning to go fishing, {target}, I have some tips that might help you catch more fish," {initiator} offers eagerly.',
            '"Fishing can be tricky, {target}, but I can give you some tips to make it easier," {initiator} says confidently.',
            '"I\'ve learned a few tricks that might improve your fishing experience, {target}. Would you like to hear them?" {initiator} asks curiously.',
            '"I noticed you\'re interested in fishing, {target}. How about I give you some pointers to get started?" {initiator} suggests warmly.',
            '"I\'ve been studying different fishing techniques, {target}, and I think I have some valuable tips to share with you," {initiator} says excitedly.',
        ],
    },
    'mixer_social_GiveCookingTips_targeted_Friendly_alwaysOn_skills': {
        'actions': [
            '"Hey {target}, I\'ve got some cooking tips for you!" {initiator} says excitedly.',
            '"I\'ve learned a few tricks in the kitchen. Mind if I share some cooking tips with you?" {initiator} asks {target}.',
            '"I\'ve been experimenting with some new recipes. Would you like me to give you a few cooking tips?" {initiator} offers {target}.',
            '"You know, {target}, I\'ve discovered some amazing cooking techniques. Can I give you a few tips?" {initiator} suggests.',
            '"I\'ve been honing my culinary skills lately. Would you be interested in hearing some cooking tips from me?" {initiator} asks {target}.',
            '"I\'ve come across some fantastic cooking hacks. How about I share a few tips with you?" {initiator} proposes to {target}.',
            '"I\'ve been exploring the world of cooking lately and picked up some valuable tips. Would you like to hear them?" {initiator} asks {target}.',
            '"You\'re in luck, {target}. I\'ve got some secret cooking tips that I\'m willing to share with you!" {initiator} teases playfully.',
            '"I\'ve been experimenting in the kitchen and stumbled upon some genius cooking tips. Want to hear them?" {initiator} asks {target} with a smile.',
            '"Cooking can be a lot of fun if you know some tricks. Mind if I pass on a few cooking tips to you, {target}?" {initiator} offers generously.',
        ],
    },
    'mixer_social_ShareCookingSecrets_targeted_Friendly_alwaysOn_skills': {
        'actions': [
            '"You know, {target}, I have this amazing recipe I want to share with you," {initiator} says enthusiastically.',
            '"I\'ve been experimenting in the kitchen lately, and I\'ve discovered some fantastic cooking secrets. Would you like me to share them with you, {target}?" {initiator} suggests.',
            '"I\'ve learned a few cooking tricks that have made a world of difference in my meals. Mind if I pass them on to you, {target}?" {initiator} offers.',
            '"{target}, I\'ve been perfecting my cooking skills, and I think I\'ve unlocked some secrets that could elevate your dishes. Can I enlighten you?" {initiator} proposes.',
            '"Cooking is my passion, {target}, and I\'d love to share some of my secrets with you. Are you interested?" {initiator} asks with a smile.',
            '"You won\'t believe the cooking hacks I\'ve discovered, {target}. Would you like me to reveal them to you?" {initiator} asks, unable to contain their excitement.',
            '"I\'ve stumbled upon some culinary secrets that can turn an ordinary meal into a masterpiece. Want me to spill the beans, {target}?" {initiator} teases.',
            '"{target}, I\'ve been honing my cooking skills, and I have a few secrets up my sleeve. Care to hear them?" {initiator} suggests with a mysterious grin."',
            '"I\'ve been reading up on cooking techniques, and I think you\'d find some of them helpful, {target}. Mind if I share them with you?" {initiator} offers politely.',
            '"I\'ve been experimenting with flavors and techniques in the kitchen lately, {target}, and I\'d love to share what I\'ve learned. Interested?" {initiator} proposes with anticipation.',
        ],
    },
    'mixer_social_EvangelizeGrilledCheese_Friendly_alwaysOn_Trait': {
        'actions': [
            '"You won\'t believe the amazingness of grilled cheese, {target}!" {initiator} exclaims.',
            '"Have you ever experienced the pure delight of a perfectly grilled cheese sandwich?" {initiator} asks {target}.',
            '"Let me tell you about the magic of grilled cheese, {target}!" {initiator} enthuses.',
            '"Have you tried the heavenly combination of melty cheese and crispy bread in a grilled cheese sandwich?" {initiator} asks {target}.',
            '"Prepare to have your taste buds revolutionized, {target}! Grilled cheese is the answer to all cravings," {initiator} declares.',
            '"I can\'t contain my excitement about grilled cheese! You must try it, {target}!" {initiator} insists.',
            '"Grilled cheese is more than just a sandwich, it\'s a culinary experience. Trust me, {target}," {initiator} says persuasively.',
            '"Let me share my love for grilled cheese with you, {target}. It\'s the ultimate comfort food," {initiator} suggests with a smile.',
            '"Grilled cheese is a masterpiece of simplicity. Don\'t you agree, {target}?" {initiator} inquires eagerly.',
            '"I\'ve discovered the secret to the most delicious grilled cheese. Would you like to know, {target}?" {initiator} teases.',
        ],
    },
    'mixer_social_Flatter_targeted_Friendly_alwaysOn': {
        'actions': [
            '"You look absolutely stunning today, {target}," {initiator} compliments.',
            '"I must say, {target}, your talent never ceases to amaze me," {initiator} says with admiration.',
            '"I couldn\'t help but notice how incredibly intelligent you are, {target}," {initiator} compliments.',
            '"You have such a captivating smile, {target}," {initiator} remarks fondly.',
            '"I wanted to let you know that you\'re an incredibly kind-hearted person, {target}," {initiator} compliments sincerely.',
            '"You have an amazing sense of style, {target}," {initiator} comments with appreciation.',
            '"I\'m in awe of your creativity, {target}," {initiator} admires.',
            '"You always manage to bring positivity to any situation, {target}," {initiator} praises warmly.',
            '"Your dedication and hard work are truly inspiring, {target}," {initiator} expresses with admiration.',
            '"I just wanted to say that you\'re a remarkable individual, {target}," {initiator} compliments sincerely.',
        ],
    },
    'mixer_social_GiveRelationshipAdvice_targeted_friendly_emotionSpecific': {
        'actions': [
            '"You know, {target}, I\'ve been thinking about your relationship..."',
            '"I have some relationship advice for you, {target}."',
            '"I\'ve been reading this book about relationships, and I think it could help you, {target}."',
            '"I\'ve noticed a few things about your relationship, {target}, and I wanted to share my thoughts."',
            '"I\'ve been through similar situations in my own relationships, {target}, and I think I can offer you some advice."',
            '"I think you should consider a different approach in your relationship, {target}."',
            '"Do you mind if I give you some relationship advice, {target}?"',
            '"I\'ve been observing your relationship, {target}, and I believe I have some insights to share."',
            '"Have you thought about trying this new technique in your relationship, {target}?"',
        ],
    },
    'mixer_social_NoxiousCloud_targeted_mischief_skills': {
        'actions': [
            '{initiator} rips a big nasty fart.',
        ],
    },
    'mixer_social_RevealDeepSecret_targeted_Friendly_HighScore': {
        'actions': [
            '"{target}, I need to tell you something. Promise me you won\'t judge," {initiator} says nervously.',
            '"I have been keeping a secret for so long, but I trust you enough to share it with you," {initiator} says, looking into {target}\'s eyes.',
            '"You know, {target}, there\'s something I\'ve never told anyone before, but I feel like I can confide in you," {initiator} says, hesitatingly.',
            '"I\'ve been carrying this secret for far too long, and it\'s eating me up inside. {target}, I think it\'s time I share it with you," {initiator} confesses, their voice trembling.',
            '"I never thought I would reveal this, but you mean a lot to me, {target}. I need you to know the truth," {initiator} says, taking a deep breath.',
            '"There\'s something I\'ve been hiding, {target}, and it\'s time I let it out. I hope you can handle it," {initiator} says, looking anxious.',
            '"I\'ve kept this hidden for years, {target}, but I can\'t bear the weight anymore. I have to tell you," {initiator} admits, looking vulnerable.',
            '"This secret has haunted me for so long, {target}, but I feel a connection with you that makes me want to share it. Can I trust you?" {initiator} asks cautiously.',
            '"I\'ve always admired your ability to keep secrets, {target}, but there\'s one I can no longer keep to myself. Brace yourself," {initiator} says, preparing to share something profound.',
            '"I\'ve been meaning to tell you this, {target}, but I\'ve never found the right time. Now, in this moment, I feel it\'s the right moment to reveal my deepest secret," {initiator} says with a mixture of relief and apprehension.',
        ],
    },
    'mixer_social_RevealEvilPlans_targeted_mischief_traits': {
        'actions': [
            '"{target}, I have a confession to make. Brace yourself, for what I\'m about to reveal is truly sinister," {initiator} says with a wicked grin.',
            '"I\'ve been living a double life, {target}, and i\'s time you know the truth. Prepare yourself for the darkness that lies within me," {initiator} says, their voice dripping with malevolence.',
            '"You thought you knew me, {target}, but you were wrong. The truth is, I\'ve been plotting something truly diabolical, and now it\'s time to involve you," {initiator} says, eyes gleaming with mischief.',
            '"Listen carefully, {target}, for the secrets I\'m about to share will change everything. I\'ve been working on a plan, a plan so evil that it will shake the very foundations of this world," {initiator} whispers ominously.',
            '"I\'ve always been envious of your innocence, {target}, but no more. Today, I reveal my true nature, and you\'ll witness the depths of my malevolence firsthand," {initiator} declares, a twisted smile forming on their lips.',
            '"Prepare to be shocked, {target}, for the darkness that resides within me is about to be unleashed. My evil plans will leave a trail of chaos and destruction," {initiator} says, their voice laced with anticipation.',
            '"You see, {target}, I\'ve been biding my time, waiting for the perfect moment to reveal my evil plans. And that moment is now," {initiator} says, a wicked glint in their eyes.',
            '"I hope you\'re ready for this, {target}, because what I\'m about to disclose will shatter your perception of me. My evil schemes are far more intricate than you could have ever imagined," {initiator} says, relishing the impending revelation."',
            '"There\'s a darkness inside me, {target}, and it\'s time you witness it. My evil plans are nearing fruition, and you\'re about to become an integral part of them," {initiator} says, a sinister chuckle escaping their lips.',
            '"I\'ve kept my true intentions hidden for far too long, {target}. Today, I lay bare my evil plans before you, and together, we shall conquer this world," {initiator} proclaims, their voice filled with twisted ambition.',
        ],
    },
    "mixer_social_RevealBrilliantInvention_targeted_Friendly_alwaysOn": {
        "actions": [
            "\"{target}, I've been working on something incredible, and I can't wait to show you,\" {initiator} says, barely containing their excitement.",
            "\"I've finally completed my latest invention, {target}. I believe it will change everything,\" {initiator} says with pride, eager to share their creation.",
            "\"{target}, you won't believe what I've invented. I need to show you right away,\" {initiator} says, grinning from ear to ear.",
            "\"I've been keeping this a secret for a while, {target}, but I finally perfected my invention. Are you ready to see it?\" {initiator} asks, anticipation filling their eyes.",
            "\"I couldn't sleep last night, {target}, because I was working on something that I think will blow your mind. Feast your eyes on this!\" {initiator} exclaims, revealing their invention.",
            "\"I've been tinkering in the workshop for weeks, {target}, and I think you're going to be amazed by what I've come up with,\" {initiator} says, filled with pride.",
            "\"I've spent countless hours perfecting this invention, {target}. I think it's time for you to see the results,\" {initiator} says, preparing to unveil their creation.",
            "\"{target}, I'm so excited to finally show you what I've been working on. I think it's going to change our lives,\" {initiator} says, their eyes sparkling with enthusiasm.",
            "\"You know I've been keeping a secret project, {target}, and now it's finally ready. I can't wait to see your reaction,\" {initiator} says, a smile spreading across their face.",
            "\"I've poured my heart and soul into this invention, {target}. I hope you're as excited about it as I am,\" {initiator} says, eager to share their accomplishment."
        ]
    },
    "mixer_social_AttemptToScare_targeted_mischief_skills": {
        "actions": [
            "\"{initiator} sneaks up behind {target} and whispers, \"Boo!\" before bursting into laughter.",
            "\"{target}, did you know there's a legend about a ghost around here?\" {initiator} says, trying to spook {target}.",
            "\"Watch out, {target}! Something's right behind you!\" {initiator} exclaims, trying to startle {target}.",
            "\"{initiator} pretends to see something terrifying in the distance and shouts, \"{target}, look out!\"",
            "\"{initiator} decides to hide and jump out at {target} as they walk by, hoping to scare them.",
            "\"Be careful, {target}. I've heard strange noises around here lately. It sends shivers down my spine,\" {initiator} says, attempting to unnerve {target}."
        ]
    },
    "mixer_social_AskWhatHappened_targeted_Friendly_alwaysOn": {
        "actions": [
            "\"{target}, I noticed something seemed off earlier. Can you tell me what happened?\" {initiator} asks with concern.",
            "\"Hey {target}, you don't look too good. What happened to you?\" {initiator} inquires, offering a sympathetic smile.",
            "\"{target}, I can tell something's bothering you. Do you want to talk about what happened?\" {initiator} asks gently.",
            "\"Is everything alright, {target}? You seem a bit down. Mind sharing what happened?\" {initiator} questions, trying to provide support.",
            "\"Something seems to have upset you, {target}. Can I help in any way? What happened?\" {initiator} asks, offering a comforting presence.",
            "\"{target}, you've been quiet all day. What happened that's got you so troubled?\" {initiator} asks, genuinely concerned.",
            "\"Hey {target}, I'm here for you if you want to talk. What happened that's got you so upset?\" {initiator} asks, placing a hand on {target}'s shoulder.",
            "\"{target}, I've known you for a long time, and I can tell when something is wrong. What happened?\" {initiator} asks with a furrowed brow.",
            "\"Is there something you want to talk about, {target}? I'm here to listen. What happened?\" {initiator} asks, sitting down next to {target}.",
            "\"You seem really down, {target}. I'm worried about you. Can you tell me what happened?\" {initiator} asks, hoping to offer some comfort."
        ]
    },
    # TODO: Add special code for interactions like this
    "mixer_social_AskIfSingle_targeted_romance_alwaysOn": {
        "actions": [
            "\"{target}, I hope this isn't too forward, but are you seeing anyone right now?\" {initiator} asks, trying to sound casual.",
            "\"I was just wondering, {target}, do you happen to be single?\" {initiator} inquires, a hint of curiosity in their voice.",
            "\"Hey {target}, I've been meaning to ask you, are you currently in a relationship?\" {initiator} questions, with a touch of nervousness.",
            "\"Forgive me if I'm being intrusive, {target}, but I couldn't help but wonder if you're single?\" {initiator} asks cautiously.",
            "\"{target}, I don't want to be presumptuous, but is there someone special in your life right now?\" {initiator} questions, genuinely curious.",
            "\"So, {target}, this might be a bit personal, but are you dating anyone at the moment?\" {initiator} inquires, trying to gauge their reaction.",
            "\"{target}, I hope you don't mind me asking, but are you currently involved with someone?\" {initiator} asks, attempting to hide their interest.",
            "\"I know this might be a bit out of the blue, {target}, but are you single or in a relationship?\" {initiator} questions, unsure of how {target} will react.",
            "\"Sorry if this is a bit nosy, {target}, but I've been curious for a while now: are you seeing anyone?\" {initiator} asks, hoping for an honest answer.",
            "\"Hey {target}, this might come across as a bit sudden, but I wanted to know if you're single or taken?\" {initiator} inquires, looking slightly embarrassed."
        ]
    },
    "mixer_social_ComplainAboutFoodPoisoning_Targeted_Friendly_AlwaysOn": {
        "actions": [
            "\"{target}, I can't believe this! I got food poisoning!\" {initiator} says, visibly upset.",
            "\"I never thought I'd get food poisoning, but I guess it's my unlucky day. I feel terrible, {target},\" {initiator} groans.",
            "\"Ugh, {target}, I think I got food poisoning. My stomach is killing me,\" {initiator} complains, clutching their stomach.",
            "\"{target}, remember that food we had? I think it gave me food poisoning. I've been feeling awful all day,\" {initiator} says with a grimace.",
            "\"You won't believe this, {target}, but I got food poisoning from our food.\" {initiator} shares, looking frustrated.",
            "\"I can't believe I got food poisoning, {target}.\" {initiator} says, holding their stomach in pain.",
            "\"{target}, this is the worst day ever. I'm pretty sure I got food poisoning from the food I just ate,\" {initiator} laments, looking miserable.",
            "\"I should've known better, {target}. That food I ate yesterday isn't sitting right with me, and now I'm paying the price,\" {initiator} says, regretting their choice.",
            "\"Ugh, {target}, I think I have food poisoning,\" {initiator} says, feeling betrayed and unwell."
        ]
    },
    "mixer_social_DeepConversation_targeted_Friendly_MiddleScore": {
        "actions": [
            "\"{target}, I've been thinking a lot lately, and I realized there's something I need to talk to you about,\" {initiator} says, taking a seat beside {target}.",
            "\"{target}, can we talk? There's something on my mind that I think only you would understand,\" {initiator} says, searching for the right words.",
            "\"Hey {target}, do you have a moment? I feel like we need to have a heart-to-heart,\" {initiator} suggests, hoping for a meaningful conversation.",
            "\"I don't know why, but I feel like I can really open up to you, {target}. Can we talk about something important?\" {initiator} asks, looking for support.",
            "\"Something has been bothering me, {target}, and I can't shake it off. I need to share it with you. Can we talk?\" {initiator} says, seeking comfort.",
            "\"{target}, you've always been a great listener, and I need someone to talk to right now. Will you lend me your ear?\" {initiator} asks sincerely.",
            "\"I've been struggling with something, {target}, and I think you might be able to help me. Can we sit down and talk?\" {initiator} asks, looking for guidance.",
            "\"{target}, I need your advice on something that's been weighing heavily on my mind. Can we have a deep conversation?\" {initiator} asks, trusting {target}'s wisdom.",
            "\"There's something I've been wanting to discuss with you, {target}. I feel like you'll be able to understand and help me navigate through it,\" {initiator} says, reaching out.",
            "\"I've been going through a tough time, {target}, and I think you're the only one who can help me make sense of it. Can we talk?\" {initiator} pleads, needing a friend."
        ]
    },
    "mixer_social_BanterWithOldFriend_targeted_Friendly_alwaysOn": {
        "actions": [
            "\"{target}, do you remember the time we first met? I can't believe it's been so long!\" {initiator} says, laughing and reminiscing about the past.",
            "\"Hey {target}, I bet you still can't make a decent cup of coffee after all these years!\" {initiator} teases, smirking playfully.",
            "\"{initiator} grins at {target} and says, \"Remember when we used to argue about who was the better singer? I still think you owe me a rematch!\"",
            "\"After all this time, {target}, I still can't believe you're such a terrible dancer!\" {initiator} chuckles, poking fun at their friend.",
            "\"{initiator} playfully nudges {target} and says, \"So, have you finally learned how to cook something other than instant noodles?\"",
            "\"Remember that time you got us lost on our way to the concert, {target}? I'm amazed we're still friends after that fiasco!\" {initiator} says, laughing heartily.",
            "\"I still can't believe you used to wear those ridiculous outfits, {target}. How did we ever let you leave the house like that?\" {initiator} teases, chuckling.",
            "\"{initiator} grins at {target} and says, \"You know, I still owe you for that prank you pulled on me years ago. Watch your back, my friend!\"",
            "\"Hey {target}, do you still have that hideous painting you insisted on hanging in your living room? I can't believe you ever thought it was a good idea!\" {initiator} laughs, reminiscing about old times.",
            "\"It's hard to believe we've come so far, {target}. Remember when we used to dream about where we'd be now? I think we've done pretty well for ourselves!\" {initiator} says, smiling fondly at their friend."
        ]
    },
    "mixer_social_BrightenDay_targeted_friendly_emotionSpecific": {
        "actions": [
            "\"{target}, I noticed you've been feeling down lately, so I brought you a little something to cheer you up,\" {initiator} says, presenting a small gift.",
            "\"Hey, {target}, I know things have been tough lately. How about we go do something fun together?\" {initiator} suggests with a smile.",
            "\"{target}, I can tell you're having a rough day, so I made you your favorite treat. I hope it brings a smile to your face,\" {initiator} says, handing over the delicious snack.",
            "\"Feeling blue, {target}? Let me tell you a joke to lighten the mood,\" {initiator} says, ready to share a funny story.",
            "\"{target}, I thought you could use a little pick-me-up, so I got you this,\" {initiator} says, offering a small token of their friendship.",
            "\"Hey {target}, I know you're going through a lot right now, but remember that I'm always here for you. Let's go for a walk and talk about it,\" {initiator} suggests kindly.",
            "\"I can see you're upset, {target}. How about I put on your favorite movie or show to help take your mind off things?\" {initiator} asks, hoping to provide some comfort.",
            "\"Sometimes, all it takes is a hug to make things better. Come here, {target},\" {initiator} says, opening their arms for a warm embrace.",
            "\"Let's get out of this rut, {target}. What can we do today to turn things around and make you feel better?\" {initiator} asks, ready to help in any way possible.",
            "\"You know, {target}, laughter is the best medicine. Want me to show you some funny videos to help brighten your day?\" {initiator} asks, hoping to lift {target}'s spirits."
        ]
    },
    "mixer_social_ComplainAboutLackofLoveLife_Targeted_Friendly_AlwaysOn_Jealous_Trait": {
        "actions": [
            "\"{target}, I can't help but feel a little envious of everyone around me. It seems like they all have someone to love, while I'm still alone,\" {initiator} says with a sigh.",
            "\"Sometimes, I wonder if I'll ever find someone who truly understands me,\" {initiator} admits to {target}, looking downcast.",
            "\"You know, {target}, I've been feeling really lonely lately. It's like everyone has someone except for me,\" {initiator} confesses, seeking comfort.",
            "\"I don't know what I'm doing wrong, {target}. Why can't I find someone who genuinely cares for me?\" {initiator} asks, frustration evident in their voice.",
            "\"{target}, do you ever feel like you're destined to be alone? I can't seem to find my other half, no matter how hard I try,\" {initiator} says, a note of sadness in their voice.",
            "\"It's so disheartening, {target}. I see couples everywhere, and it just reminds me of what I'm missing,\" {initiator} shares, their eyes filled with longing.",
            "\"I've been on so many dates, {target}, but nothing ever seems to work out. What am I doing wrong?\" {initiator} questions, hoping for some insight.",
            "\"Sometimes, I feel like giving up on love altogether, {target}. It's just so exhausting trying to find someone who actually cares,\" {initiator} admits, looking defeated.",
            "\"Everyone says there's someone out there for everyone, {target}, but I'm starting to doubt it. Will I ever find my person?\" {initiator} asks, desperation creeping into their voice.",
            "\"I can't help but feel like I'm missing out on something amazing, {target}. Everyone talks about how great love is, but all I've ever known is loneliness,\" {initiator} laments, a tear in their eye."
        ]
    },
    "mixer_social_BoastAboutBiggestCatch_targeted_Friendly_alwaysOn_skills": {
        "actions": [
            "\"{target}, you won't believe it, I caught the biggest fish you've ever seen!\" {initiator} exclaims with excitement.",
            "\"Hey, {target}, I don't want to brag, but I caught a huge fish the other day. I've never seen one like it before,\" {initiator} says, trying to contain their pride.",
            "\"Guess what, {target}? I went fishing yesterday and caught an absolute monster of a fish! You should've seen it,\" {initiator} says, grinning from ear to ear.",
            "\"I know you're into fishing, {target}, but let me tell you about the giant fish I caught this weekend. It was amazing!\" {initiator} says, eager to share their story.",
            "\"I can't help but brag a little, {target}. I caught this enormous fish that was bigger than anything I've ever seen!\" {initiator} says, eyes sparkling with excitement.",
            "\"You're not going to believe this, {target}, but I managed to catch a fish that was bigger than both my arms outstretched!\" {initiator} says, their voice filled with triumph.",
            "\"Hey, {target}, have you ever caught a fish so big that it barely fit in your net? Because I just did!\" {initiator} says, beaming with pride.",
            "\"I've got to tell someone, {target}, and you're the lucky one. I caught a fish so big, it made all the other fishermen jealous!\" {initiator} says, grinning proudly.",
            "\"Listen up, {target}, I've got a fishing tale for you. I caught this massive fish that I could barely pull out of the water!\" {initiator} says, excitement in their voice.",
            "\"Just between us, {target}, I managed to catch the biggest fish of my life yesterday! It was incredible!\" {initiator} says, unable to contain their enthusiasm."
        ]
    },
    "mixer_social_HorrifyingJoke_targeted_funny_alwaysOn": {
        "actions": [
            "\"{target}, I heard this joke the other day, and I just have to share it with you. It's a bit twisted, though,\" {initiator} says, grinning mischievously.",
            "\"Hey {target}, I've got a dark sense of humor, and I think this joke might be right up your alley. Can you handle it?\" {initiator} asks, raising an eyebrow.",
            "\"{initiator} leans in close to {target} and whispers, \"I've got a joke that might give you the creeps. Are you ready?\"",
            "\"Okay, {target}, brace yourself. I've got a joke that's not for the faint of heart,\" {initiator} says, a wicked smile on their face.",
            "\"Be warned, {target}, this joke is not for everyone. But I think you've got the stomach for it,\" {initiator} says, their eyes gleaming with anticipation.",
            "\"{target}, I've got a horrifying joke that I think you'll appreciate. Get ready to laugh and cringe at the same time,\" {initiator} says, rubbing their hands together in excitement.",
            "\"Alright, {target}, I've got a joke that's twisted and hilarious, but it's not for everyone. Are you in?\" {initiator} asks, a devilish grin on their face.",
            "\"{initiator} chuckles darkly and says to {target}, \"I've got a joke that might make your skin crawl. Do you want to hear it?\"",
            "\"Hey {target}, I've got a joke that's a little... morbid. But I think you'll like it,\" {initiator} says, a mischievous glint in their eye.",
            "\"{initiator} smirks and says to {target}, \"This joke is definitely not for the easily scared, but I think you can handle it. Are you ready for a horrifying laugh?\""
        ]
    },
    "mixer_social_AskForAdvice_targeted_friendly_emotionSpecific_Scared": {
        "actions": [
            "\"{target}, I don't know what to do. I'm terrified, and I need your advice,\" {initiator} admits, their voice shaking.",
            "\"{target}, I'm really scared about this situation. Can you help me figure out what to do?\" {initiator} pleads, desperation in their eyes.",
            "\"I hate to ask, {target}, but I'm feeling so overwhelmed and frightened. Do you have any advice for me?\" {initiator} asks, trying to hold back tears.",
            "\"{target}, I've never been this scared before. I trust your judgment, so can you please guide me?\" {initiator} says, their voice barely audible.",
            "\"I don't know who else to turn to, {target}. I'm so scared, and I need your guidance,\" {initiator} confesses, their body trembling.",
            "\"{target}, I've always admired your wisdom and strength. I'm really frightened right now, and I could use your help,\" {initiator} says, their eyes pleading for understanding.",
            "\"I've hit rock bottom, {target}, and I'm terrified of what's to come. Can you please give me some advice?\" {initiator} begs, holding back sobs.",
            "\"{target}, I'm in a really dark place, and fear is consuming me. I need your help to find a way out,\" {initiator} says, their voice quivering.",
            "\"I've never asked for help like this before, {target}, but I'm truly scared, and I don't know what to do. Can you guide me?\" {initiator} implores, their eyes filled with vulnerability.",
            "\"{target}, I feel like I'm drowning in fear, and I don't know how to swim. Can you please give me some advice?\" {initiator} asks, struggling to maintain their composure."
        ]
    },
    "mixer_social_ComplainAboutLackOfPower_targeted_friendly_alwaysOn_billsLack": {
        "actions": [
            "\"{target}, I can't believe I forgot to pay my electric bill! Now, we're stuck in the dark,\" {initiator} grumbles, filled with frustration.",
            "\"Ugh, {target}, you won't believe this, but I was so busy that I completely forgot to pay the electric bill. Now we have no power,\" {initiator} complains, shaking their head in disbelief.",
            "\"{target}, I messed up big time. I didn't pay the electric bill and now we're left without power,\" {initiator} says, looking annoyed with themselves.",
            "\"You know, {target}, it's so irritating when you forget something as important as paying the electric bill. I feel so powerless, literally,\" {initiator} groans, feeling irritated.",
            "\"{target}, I can't believe I did this. I didn't pay my electric bill, and now we have to deal with this power outage,\" {initiator} complains, looking embarrassed.",
            "\"I never thought I'd be the one to forget something this important, {target}. I didn't pay the electric bill, and now we're stuck in the dark,\" {initiator} says, rolling their eyes at their own mistake.",
            "\"I really messed up, {target}. I completely forgot to pay the electric bill, and now we're without power,\" {initiator} admits, their voice filled with disappointment.",
            "\"Can you believe it, {target}? I forgot to pay the electric bill, and now we have to deal with this annoying power outage,\" {initiator} complains, visibly upset.",
            "\"Of all the things I could forget, {target}, I can't believe it was the electric bill. Now we're stuck here without power,\" {initiator} says, shaking their head in frustration.",
            "\"{target}, I have to admit, I messed up. I didn't pay my electric bill on time, and now we're left without power,\" {initiator} says, clearly annoyed with themselves."
        ]
    },
    "mixer_social_ComplainAboutLackOfWater_targeted_friendly_alwaysOn_bills": {
        "actions": [
            "\"{target}, I can't believe this! I didn't pay my water bill, and now I don't have any water at home,\" {initiator} grumbles in frustration.",
            "\"Ugh, {target}, I messed up big time. I forgot to pay my water bill and now I'm stuck without any water at home,\" {initiator} complains, looking annoyed.",
            "\"{target}, you won't believe how careless I've been. I didn't pay my water bill, and now I have to deal with the consequences,\" {initiator} says, shaking their head in disappointment.",
            "\"I'm so annoyed with myself, {target}. I didn't pay my water bill and now I'm left without water at home. What a mess,\" {initiator} says, clearly irritated.",
            "\"I can't even take a shower, {target}, because I forgot to pay my water bill! This is just the worst,\" {initiator} complains, looking defeated.",
            "\"{target}, I'm in such a bad situation. I didn't pay my water bill, and now I'm suffering the consequences at home,\" {initiator} groans, feeling the weight of their mistake.",
            "\"I'm such an idiot, {target}. I didn't pay my water bill, and now my home is completely without water,\" {initiator} says, exasperated.",
            "\"{target}, can you believe I forgot to pay my water bill? Now I have no water at home and it's driving me crazy,\" {initiator} shares, looking for some sympathy.",
            "\"Of all the bills to forget to pay, I had to forget my water bill, {target}. Now I'm stuck in this mess,\" {initiator} laments, frustrated with the situation.",
            "\"I don't know what I was thinking, {target}. I didn't pay my water bill, and now I'm left high and dry at home,\" {initiator} says, clearly upset by their oversight."
        ]
    },
    "mixer_social_AskForAdvice_targeted_friendly_emotionSpecific": {
        "actions": [
            "\"{target}, I've been struggling with something lately, and I really value your opinion. Can I ask for your advice?\" {initiator} asks hesitantly.",
            "\"{target}, you've always been someone I can turn to for guidance. I need your advice on something important,\" {initiator} says, looking concerned.",
            "\"I'm facing a tough decision, {target}, and I'm not sure what to do. I trust your judgment â can you help me?\" {initiator} pleads, seeking reassurance.",
            "\"You always seem to have the answers, {target}. Can I ask you for some advice?\" {initiator} inquires, hoping for some insight.",
            "\"{target}, I'm at a crossroads, and I don't know which path to take. I could really use your advice,\" {initiator} admits, seeking support.",
            "\"I know you've been through a lot, {target}, and I think you might have some valuable advice for me. Can I talk to you about something?\" {initiator} asks earnestly.",
            "\"{target}, I'm in a bit of a bind, and I don't know who else to turn to. Can I ask you for some advice?\" {initiator} requests, sounding desperate.",
            "\"I've always admired your wisdom, {target}. I'm struggling with a situation, and I'd appreciate your advice,\" {initiator} says with respect.",
            "\"You're someone I look up to, {target}, and I could really use your guidance right now. Can I ask you for some advice?\" {initiator} pleads, looking vulnerable.",
            "\"Hey, {target}, there's something I've been wrestling with, and I could use your perspective. Do you have a moment to chat?\" {initiator} asks, hoping for a helpful conversation."
        ]
    },
    "mixer_social_BegForgiveness_targeted_friendly_lowScore": {
        "actions": [
            "\"{target}, I am so sorry for what I've done. I don't expect you to forgive me right away, but I had to tell you how much I regret it,\" {initiator} pleads, their eyes filled with remorse.",
            "\"Please, {target}, I know I messed up badly, but can you find it in your heart to forgive me?\" {initiator} begs, desperate for understanding.",
            "\"{target}, I can't change the past, but I promise to do better in the future. I just need you to give me a chance to prove myself,\" {initiator} implores, hoping for forgiveness.",
            "\"I don't know how to make it right, {target}, but I'm willing to do anything to earn your forgiveness,\" {initiator} says earnestly, tears streaming down their face.",
            "\"Please, {target}, I know I hurt you, and I'm so sorry. I'll do whatever it takes to make amends,\" {initiator} pleads, a pained expression on their face.",
            "\"I never meant to cause you pain, {target}, and I am so sorry for my actions. I beg you to forgive me,\" {initiator} says, their voice full of sorrow and regret.",
            "\"{target}, I can't express how much I regret what I've done. I just want to make things right between us. Can you forgive me?\" {initiator} asks, looking vulnerable.",
            "\"Please, {target}, I know I don't deserve your forgiveness, but I need to let you know how deeply sorry I am,\" {initiator} says, their voice cracking with emotion.",
            "\"I understand if you can't forgive me right now, {target}, but I will do everything I can to make it up to you,\" {initiator} promises, their eyes pleading for understanding.",
            "\"{target}, I was wrong and I hurt you. All I'm asking is for a chance to show you that I can change and be better,\" {initiator} says, tears welling up in their eyes."
        ]
    },
    "mixer_social_AskToBeBestFriends_targeted_Friendly_HighScore": {
        "actions": [
            "\"{target}, we've been getting along so well lately. Would you like to be best friends?\" {initiator} asks with a hopeful smile.",
            "\"Hey, {target}, I've been thinking... We're pretty great together. What do you say we become best friends?\" {initiator} suggests, grinning.",
            "\"{target}, I feel a real connection with you. I've never had a best friend before, but I'd like you to be mine. What do you think?\" {initiator} asks nervously.",
            "\"I've never met someone I clicked with like I do with you, {target}. How about we make it official and become best friends?\" {initiator} proposes, looking excited.",
            "\"Listen, {target}, I don't want to be too forward, but I think we make a great team. Would you be up for being my best friend?\" {initiator} asks, trying to gauge {target}'s reaction.",
            "\"Hey, {target}, you know what would be awesome? If we became best friends! Are you in?\" {initiator} asks, looking at {target} with anticipation.",
            "\"I've been thinking, {target}, and I've realized that you're the person I want as my best friend. What do you say?\" {initiator} asks, hopeful for a positive response.",
            "\"Life's too short not to have a best friend, and I can't think of anyone better than you, {target}. Will you be my best friend?\" {initiator} inquires with a warm smile.",
            "\"You know, {target}, I think we were destined to be best friends. What's your opinion on that?\" {initiator} asks, looking for confirmation.",
            "\"I've never felt this close to anyone before, {target}. Would you do me the honor of becoming my best friend?\" {initiator} asks sincerely, hoping for a positive answer."
        ]
    },
    "mixer_social_HilariousIcebreaker_greetings": {
        "actions": [
            "\"{target}, why don't scientists trust atoms? Because they make up everything! Hi, I'm {initiator}!\" {initiator} says with a chuckle.",
            "\"{target}, what do you get when you cross a snowman and a vampire? Frostbite! I'm {initiator}, nice to meet you!\" {initiator} grins, extending their hand.",
            "\"Knock knock, {target}. Who's there? Lettuce. Lettuce who? Lettuce in, it's cold out here! I'm {initiator}, by the way,\" {initiator} says, laughing at their own joke.",
            "\"Hey {target}, did you hear about the kidnapping at the playground? They woke up! I'm {initiator}, it's a pleasure to meet you!\" {initiator} says, giggling.",
            "\"{target}, what do you call fake spaghetti? An impasta! Hi there, I'm {initiator}!\" {initiator} says, laughing heartily.",
            "\"Did you know, {target}, that parallel lines have so much in common? It's a shame they'll never meet! I'm {initiator}, nice to meet you!\" {initiator} says, smiling broadly.",
            "\"Hey {target}, what do you call a pile of cats? A meowtain! I'm {initiator}, and I couldn't resist sharing that with you!\" {initiator} says, chuckling.",
            "\"{target}, why did the scarecrow win an award? Because he was outstanding in his field! Hi, I'm {initiator}!\" {initiator} says, laughing and extending a hand.",
            "\"Guess what, {target}? I told my wife she was drawing her eyebrows too high. She looked surprised! I'm {initiator}, by the way,\" {initiator} says, laughing at their own joke.",
            "\"Hey {target}, what's the difference between a snowman and a snowwoman? Snowballs! I'm {initiator}, great to meet you!\" {initiator} says, grinning from ear to ear."
        ]
    },
    "mixer_social_BragAboutFoodPoisoning_Targeted_Friendly_AlwaysOn": {
        "actions": [
            "\"{target}, you wouldn't believe it, but I survived the worst food poisoning ever. I'm like a superhero,\" {initiator} says, puffing out their chest.",
            "\"Hey, {target}, did I ever tell you about the time I got food poisoning and lived to tell the tale? You should be impressed,\" {initiator} smirks.",
            "\"{target}, I had food poisoning so bad that I thought I'd never recover. But here I am, stronger than ever,\" {initiator} boasts.",
            "\"Oh, {target}, I had this horrible food poisoning once, but I fought my way through it like a champ. I bet not everyone could handle that,\" {initiator} says with pride.",
            "\"You know, {target}, they say what doesn't kill you makes you stronger. Well, I survived food poisoning, so I must be pretty tough,\" {initiator} brags.",
            "\"Hey, {target}, have you ever had food poisoning? I did, and I managed to get through it like a warrior. You must think I'm pretty resilient, huh?\" {initiator} says, seeking validation.",
            "\"{target}, I bet you didn't know this, but I've faced the worst food poisoning of my life and came out victorious. I'm pretty much invincible,\" {initiator} says with a grin.",
            "\"I don't mean to brag, {target}, but I once had the most awful bout of food poisoning, and I still managed to power through it. I'm kind of amazing, right?\" {initiator} says with a wink.",
            "\"{target}, I've been through the wringer with food poisoning, and I'm still standing. I guess I've got a pretty strong stomach,\" {initiator} says, tapping their abdomen.",
            "\"Surviving food poisoning is no small feat, {target}, but I managed to do it with flying colors. You can call me the master of resilience,\" {initiator} says with a boastful laugh."
        ]
    },
}