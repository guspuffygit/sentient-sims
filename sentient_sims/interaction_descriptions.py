# {initiator} and {target} will be replaced with the names of the sims in the interaction
from sentient_sims_code.filters.has_not_happened import HasNotHappened
from sentient_sims_code.filters.initiator_is_active_sim import InitiatorIsActiveSim
from sentient_sims_code.filters.sim_in_memories import SimInMemories

interaction_descriptions = {
    'mixer_social_ComplainAboutBills_targeted_Friendly_alwaysOn_bills': {
        "pre_actions": [
            '{initiator} complains about their bills to {target}.',
        ],
        "actions": [
            "\"I don\'t know how I\'m going to pay for all of these bills,\" {initiator} said.",
            "\"It seems like every time I turn around, there\'s another bill to pay,\" {initiator} grumbled.",
            "\"I can\'t believe how much money I have to spend on bills every month,\" grumbled {initiator.",
            "\"I can\'t believe how much money I have to spend on bills every month,\" grumbled {initiator}.",
            "\"I\'m so sick of living paycheck to paycheck just to keep up with these bills,\" complained {initiator}.",
        ],
    },
    'mixer_social_DiscussLatestGames_targeted_Friendly_alwaysOn_skills': {
        "pre_actions": [
            '{initiator} discusses the newly released video game with {target}.',
        ],
        "actions": [
            "\"What do you think of the new video game, {target}? Have you had a chance to play it yet?\" {initiator} asks excitedly.",
            "\"I can\'t stop playing the new video game. Have you tried it yet, {target}?\" {initiator} says, grinning from ear to ear.",
            "\"I\'ve been waiting for this video game for months, {target}, and I have to say, it\'s exceeded my expectations,\" {initiator} raves.",
            "\"Have you heard about the new video game? I think you\'d really like it, {target},\" {initiator} says, trying to pique {target}\'s interest.",
            "\"I\'m so glad I pre-ordered the new video game. It\'s all I can think about. What do you think, {target}?\" {initiator} asks, eagerly.",
            "\"You have to play the new video game, {target}. It\'s seriously the best game I\'ve played in years,\" {initiator} says, practically begging {target} to give it a try.",
            "\"I can\'t believe how good the graphics are in the new video game. It\'s like I\'m really in the game,\" {initiator} says, still in awe.",
            "\"Did you catch that Easter egg in the new video game? It\'s so cool. I wonder if there are any more,\" {initiator} muses, hoping to discuss details with {target}.",
            "\"I love how immersive the new video game is. It\'s like I\'m living in a completely different world,\" {initiator} says dreamily.",
            "\"The new video game has been consuming all of my free time. Do you want to play together sometime, {target}?\" {initiator} suggests.",
        ],
    },
    'mixer_social_CheerfulIntroduction_greetings_skills': {
        "pre_actions": [
            '{initiator} cheerfully introduces themselves to {target} for the first time.',
        ],
        'actions': [
            "\"Hi there! I don't think we've officially met yet. I'm {initiator},\" {initiator} says with a warm smile.",
            "\"Hey, I'm {initiator}! I've seen you around, but we've never had the chance to introduce ourselves properly,\" {initiator} says, extending a hand.",
            "\"Hello! I'm {initiator}. I've been meaning to introduce myself to you for a while now,\" {initiator} says, their eyes sparkling with excitement.",
            "\"Nice to finally meet you! I'm {initiator}. I've heard so much about you,\" {initiator} says, beaming with enthusiasm.",
            "\"Hey, I'm {initiator}! I've been wanting to introduce myself to you ever since I saw you,\" {initiator} says, playfully nudging {target}.",
            "\"Hi, I'm {initiator}! I've been waiting for the perfect moment to introduce myself, and I think this is it,\" {initiator} says, chuckling.",
            "\"Hello! I'm {initiator}. I've been admiring you from afar, and I couldn't resist the opportunity to finally say hi,\" {initiator} says, blushing slightly.",
            "\"Hey there! I'm {initiator}. I've been dying to talk to you, and now I finally can,\" {initiator} says, their voice filled with excitement.",
            "\"Nice to meet you! I'm {initiator}. I've been wanting to introduce myself ever since I saw your incredible talent,\" {initiator} says, genuinely impressed.",
            "\"Hi, I'm {initiator}! I've been meaning to come over and say hi, but I've always been a little nervous. But today, I decided to take a leap,\" {initiator} says, smiling warmly."
        ],
    },
    'mixer_social_FlirtyIntroduction_greetings_skills': {
        "pre_actions": [
            '{initiator} flirtatiously introduces themselves to {target}.',
        ],
        "actions": [
            "With a flirtatious smile, {initiator} strode over and extended their hand. \"Hi there, I'm {initiator}. What's your name?",
            "{initiator} sauntered up with a charming grin. \"Well hello there, I don't think we've met yet. I'm {initiator}.",
            "With a twinkle in their eye, {initiator} approached the other person and struck up a conversation. \"Excuse me,",
            "With a playful wink, {initiator} sauntered up to the other person and introduced themselves. \"Hi,",
            "{initiator} catches {target}\'s gaze and saunters over with a mischievous grin. \"Feeling bored? Don\'t worry, your day\'s about to get interesting. By the way, I\'m {initiator}.\" they say, their voice low and flirtatious.",
            "\"{target}, I must say, you have caught my eye. Allow me to formally introduce myself,\" {initiator} says with a charming smile.",
            "\"Well, hello there, {target}. I couldn't resist the opportunity to come and introduce myself,\" {initiator} says, their voice filled with playful confidence.",
            "\"You must be {target}, the person everyone is talking about. I couldn't resist the chance to introduce myself,\" {initiator} says, a mischievous glint in their eyes.",
            "\"Excuse me, but I couldn't help but notice how captivating you are, {target}. Mind if I introduce myself?\" {initiator} says, leaning in closer.",
            "\"I couldn't resist the temptation any longer, {target}. Allow me to introduce myself in the most flirtatious way possible,\" {initiator} says, their voice dripping with seduction.",
            "\"Is it fate or luck that brought us together, {target}? Either way, I couldn't pass up the chance to introduce myself properly,\" {initiator} says, their voice filled with intrigue.",
            "\"I must admit, {target}, you have a certain allure that I couldn't ignore. Allow me to introduce myself and see where it leads,\" {initiator} says, a playful smirk on their face.",
            "\"Forgive me for interrupting your day, {target}, but I couldn't resist the opportunity to introduce myself. I couldn't bear the thought of missing out on getting to know you,\" {initiator} says, their voice filled with genuine interest.",
            "\"I hope you don't mind a bold approach, {target}, because I couldn't resist coming over to introduce myself. I have a feeling we could have some fun,\" {initiator} says, a hint of excitement in their voice.",
            "\"Pardon the interruption, {target}, but I couldn't help but be drawn to you. Allow me to introduce myself and see where this connection takes us,\" {initiator} says, their eyes locked with {target}'s."
        ],
    },
    'mixer_social_ExpressFondness_targeted_Romance_alwaysOn': {
        "pre_actions": [
            '{initiator} pauses thoughtfully before expressing their fondness for {target}.',
        ],
        'actions': [
            "\"I\'ve been meaning to tell you this, {target}, but I never found the courage to say it until now,\" {initiator} says, looking down at his feet.",
            "\"I don\'t know how to say this, but I feel something for you, {target}. Something more than friendship,\" {initiator} confesses, looking up at {target} nervously.",
            "\"I hope this doesn\'t change anything between us, but I need to tell you how I feel. {target}, I have feelings for you,\" {initiator} says, biting his lip.",
            "\"I know this might come as a surprise, {target}, but I can\'t keep it inside any longer. I\'m in love with you,\" {initiator} says, his voice barely above a whisper.",
            "\"I don\'t know how you\'ll react to this, {target}, but I have to tell you. I have feelings for you that I can\'t ignore,\" {initiator} says, looking at {target} with a mix of fear and adoration.",
            "\"I know this might be inappropriate, {target}, but I can\'t help the way I feel. I\'m attracted to you,\" {initiator} says, looking ashamed.",
            "\"I hope you don\'t think less of me for saying this, {target}, but I feel like I need to be honest. I have a crush on you,\" {initiator} admits, looking at {target} with a hint of sadness.",
            "\"I know this might ruin our friendship, {target}, but I have to say it. I\'m in love with you,\" {initiator} says, bracing for the worst.",
            "\"I know we\'ve been friends for a long time, {target}, but I can\'t help how I feel. I think I\'m falling for you,\" {initiator} says, looking at {target} with a mixture of hope and trepidation.",
        ]
    },
    'mixer_social_ExpressAdmiration_targeted_Friendly_MiddleScore': {
        "pre_actions": [
            "{initiator} expresses their deep admiration for {target}.",
        ],
        "actions": [
            "\"I have to say, you never cease to amaze me,\" said {initiator}.",
            "\"I'm constantly in awe of your resilience,\" said {initiator}.",
            "\"You have such an incredible way of seeing the world,\" said {initiator}, genuinely impressed.",
            "\"{target}, I have to tell you something. You have no idea how much I admire you,\" {initiator} says with a hint of awe in their voice.",
            "\"I've always looked up to you, {target}. Your strength and determination inspire me,\" {initiator} confesses, their eyes shining.",
            "\"Can I just say how much I admire you, {target}? Your kindness and compassion never cease to amaze me,\" {initiator} says, smiling genuinely.",
            "\"I hope you know how much I admire you, {target}. Your intelligence and creativity are truly remarkable,\" {initiator} says, their voice filled with sincerity.",
            "\"{target}, there's something I've been meaning to tell you. I have the utmost admiration for you and everything you've achieved,\" {initiator} says, their admiration evident in their eyes.",
            "\"I don't think I've ever told you this, {target}, but I admire you more than you can imagine. Your courage and resilience are extraordinary,\" {initiator} says, their voice filled with reverence.",
            "\"I've always wanted to express how much I admire you, {target}. Your talent and dedication are truly inspiring,\" {initiator} says, unable to hide their admiration.",
            "\"{target}, I have to be honest with you. I admire you so much, it's almost intimidating. Your determination and work ethic are unmatched,\" {initiator} says, their voice filled with admiration.",
            "\"I hope you don't mind me saying this, {target}, but I have immense admiration for you. Your generosity and selflessness make you an incredible person,\" {initiator} says, their admiration evident in their tone.",
            "\"I've been wanting to tell you this for a while, {target}. I truly admire you, not just for your achievements, but for the person you are,\" {initiator} says, their voice filled with genuine admiration."
        ],
    },
    'mixer_social_ComplainAboutProblems_targeted_friendly_emotionSpecific': {
        "pre_actions": [
            "{initiator} complains to {target} about their mundane problems.",
        ],
        "actions": [
            "{initiator} sighed heavily, \"My job sucks,\" they began,",
            "\"I hate doing laundry. It\'s such a chore, and I never seem to have enough time for it.\", {initiator} began,",
            "\"I\'ve been trying to eat healthier, but all the healthy food is so expensive.\", {initiator} began,",
            "\"{target}, I can't believe I have to deal with this again. My coffee machine broke this morning, and it ruined my entire day,\" {initiator} vents, frustrated.",
            "\"I know it's such a small thing, but I just need to vent. My phone battery died right before an important call, and it's driving me crazy,\" {initiator} complains, seeking empathy.",
            "\"{target}, I feel like everything is falling apart. First, I missed the bus, and now I spilled coffee all over my new shirt,\" {initiator} grumbles, feeling overwhelmed.",
            "\"You won't believe what happened today, {target}. I accidentally deleted all of my important files, and I don't know how to recover them,\" {initiator} laments, seeking advice.",
            "\"I'm sorry to bother you with this trivial matter, {target}, but I just can't shake off the frustration from losing my keys again,\" {initiator} admits, feeling embarrassed.",
            "\"{target}, I need to get this off my chest. I've been having the worst luck lately - from getting a parking ticket to dropping my phone in the toilet,\" {initiator} grumbles, feeling exasperated.",
            "\"I know it sounds silly, but I can't help but be annoyed. I've been trying to fix my Wi-Fi for hours, and it's just not working,\" {initiator} complains, seeking reassurance.",
            "\"I hate to be a complainer, {target}, but I've had the most miserable day. From getting caught in the rain without an umbrella to spilling coffee on my laptop,\" {initiator} vents, feeling defeated.",
            "\"{target}, I know it's not a big deal, but I can't help but feel annoyed. I've been stuck in traffic for hours, and it's making me late for everything,\" {initiator} grumbles, seeking understanding.",
            "\"I know it's silly to complain about, but I can't stand it anymore. I've been dealing with a noisy neighbor, and it's driving me crazy,\" {initiator} admits, seeking advice."
        ],
    },
    'mixer_social_DiscussFavoriteArtist_targeted_Friendly_MiddleScore': {
        "pre_actions": [
            "{initiator} discusses their favorite artist with {target}.",
        ],
        'actions': [
            "\"Do you have a favorite artist, {target}? I've been dying to talk to someone about mine,\" {initiator} says excitedly.",
            "\"I recently discovered this incredible artist, {target}, and I just have to share their work with you. It's mind-blowing,\" {initiator} says, unable to contain their enthusiasm.",
            "\"You know, {target}, I've always been drawn to art. There's this one artist, though, who completely captivates me. Have you heard of them?\" {initiator} asks curiously.",
            "\"I've been following this artist for years, {target}, and their work never fails to amaze me. I think you would appreciate it too,\" {initiator} suggests, hoping to spark a conversation.",
            "\"I stumbled upon this artist's work recently, {target}, and I can't stop thinking about it. I need someone to geek out with me over their art,\" {initiator} says with a grin.",
            "\"I've been meaning to ask you, {target}, do you have a favorite artist? I'd love to share mine with you,\" {initiator} says, genuinely interested in {target}'s opinion.",
            "\"I've been going through this artist's portfolio, {target}, and I just had to talk to someone about it. Can I share some of their work with you?\" {initiator} asks, hoping for a positive response.",
            "\"You won't believe what I found, {target}. This artist creates the most breathtaking art. I have to show you,\" {initiator} says, eager to introduce {target} to their favorite artist.",
            "\"I've been researching different artists lately, {target}, and there's one in particular that stands out to me. I think you might find them fascinating too,\" {initiator} says, hoping to start a conversation about art.",
            "\"Art has always been a big part of my life, {target}, and I'd love to know who your favorite artist is. I'll tell you mine if you share yours,\" {initiator} suggests, eager to bond over their shared love for art."
        ],
    },
    'mixer_social_DiscussFavoriteAuthors_targeted_Friendly_alwaysOn': {
        "pre_actions": [
            "{initiator} discusses their favorite authors with {target}.",
        ],
        'actions': [
            "\"I just finished reading a book by my favorite author, and I can't wait to share it with you,\" {initiator} says excitedly.",
            "\"I've been meaning to ask you, {target}, who is your favorite author?\" {initiator} asks curiously.",
            "\"You know, {target}, I think our taste in books might align. Who are some of your favorite authors?\" {initiator} wonders.",
            "\"I recently discovered this incredible author, {target}, and I think you would absolutely love their work. Have you heard of them?\" {initiator} suggests.",
            "\"I've been reading this book by an author I adore, {target}, and I can't help but rave about it. Have you read anything by them?\" {initiator} inquires.",
            "\"I've always admired your taste in literature, {target}. Who are the authors that have influenced you the most?\" {initiator} asks with genuine interest.",
            "\"I recently stumbled upon this author whose writing style is so unique and captivating, {target}. I think you would appreciate their work too,\" {initiator} suggests.",
            "\"I've been thinking about starting a book club, {target}, and I would love to know which authors you would recommend for our reading list,\" {initiator} proposes.",
            "\"I've been reading a lot lately, and I can't help but wonder, {target}, who are the authors that have inspired you?\" {initiator} asks, eager to hear {target}'s response.",
            "\"I've been so immersed in this incredible book by my favorite author, {target}, and I can't help but gush about it. Have you read anything by them?\" {initiator} enthuses."
        ],
    },
    'mixer_social_DiscussFavoriteBand_targeted_Friendly_alwaysOn': {
        "pre_actions": [
            "{initiator} discusses their favorite bands with {target}.",
        ],
        "actions": [
            "\"{target}, I just discovered this amazing band and I can't stop listening to their music. Have you ever heard of them?\" {initiator} asks excitedly.",
            "\"I've been thinking a lot about music lately, and I'd love to know what your favorite bands are, {target},\" {initiator} says, curious.",
            "\"You know, {target}, I've always believed that music has the power to bring people together. What are some of your favorite bands?\" {initiator} asks, genuinely interested.",
            "\"I've been on a quest to find new music, and I think you might have some recommendations. What bands do you enjoy, {target}?\" {initiator} asks, hoping for some inspiration.",
            "\"Music has always been a big part of my life, {target}. I'd love to share some of my favorite bands with you. Are you open to discovering new music?\" {initiator} asks with a smile.",
            "\"I've been listening to this band nonstop, {target}, and I can't help but wonder if you might enjoy their music too. Can I share it with you?\" {initiator} asks, eager to introduce {target} to their favorite band.",
            "\"I believe that music can say a lot about a person, {target}. What are some of your favorite bands? I'd love to get to know you better through your taste in music,\" {initiator} says, hoping for a deeper connection.",
            "\"Music has this incredible ability to transport you to another place, don't you think, {target}? I'd love to know what bands have that effect on you,\" {initiator} says, reminiscing about their favorite bands.",
            "\"I've recently discovered this hidden gem of a band, {target}, and I think you might appreciate their unique sound. Can I tell you more about them?\" {initiator} asks, eager to share their musical discovery.",
            "\"I've been reflecting on the power of music lately, {target}, and I'm curious to know what bands have had a significant impact on your life. Care to share?\" {initiator} asks, ready for a meaningful conversation about music."
        ],
    },
    'mixer_social_DiscussFavoriteRecipes_targeted_Friendly_MiddleScore': {
        "pre_actions": [
            "{initiator} discusses their favorite recipes with {target}.",
        ],
        "actions": [
            "\"I just discovered this amazing recipe, {target}, and I couldn't wait to share it with you,\" {initiator} says excitedly.",
            "\"You've always been a food lover, {target}, so I thought you might appreciate this recipe I found,\" {initiator} says with a smile.",
            "\"I've been experimenting in the kitchen lately, {target}, and I think I've finally perfected my favorite recipe. Want to hear about it?\" {initiator} asks eagerly.",
            "\"I know you enjoy cooking, {target}, so I thought we could exchange our favorite recipes. I'll go first,\" {initiator} suggests.",
            "\"Food has always been a passion of mine, {target}, and I've been dying to share my favorite recipe with someone. Are you interested?\" {initiator} asks curiously.",
            "\"You're the only person I know who appreciates good food as much as I do, {target}. Can I share my favorite recipe with you?\" {initiator} asks with anticipation.",
            "\"I recently discovered a recipe that has become my absolute favorite, {target}, and I thought you might be interested in trying it too,\" {initiator} says with enthusiasm.",
            "\"I've been thinking about starting a cooking blog, {target}, and I wanted to bounce some recipe ideas off you. What do you think?\" {initiator} asks, seeking {target}'s opinion.",
            "\"I've been craving this particular dish lately, {target}, and I just had to tell someone about it. Can I share the recipe with you?\" {initiator} asks, unable to contain their excitement.",
            "\"I've been exploring different cuisines lately, {target}, and I've stumbled upon this incredible recipe. Mind if I share it with you?\" {initiator} asks, hoping {target} will be as intrigued as they are.",
        ],
    },
    'mixer_social_DiscussFineCuisine_targeted_Friendly_MiddleScore': {
        "pre_actions": [
            "{initiator} begins a conversation with {target} about fine cuisine.",
        ],
        "actions": [
            "\"{target}, have you ever tried a Michelin-starred restaurant? I've been dying to discuss fine cuisine with someone who appreciates it,\" {initiator} says excitedly.",
            "\"I've recently discovered this amazing French bistro in town, {target}. I thought you might be interested in hearing about it,\" {initiator} suggests with a smile.",
            "\"{target}, I've been experimenting with cooking lately and I've come across some extraordinary recipes. I thought you might want to exchange some ideas,\" {initiator} says, hoping to spark a conversation about fine cuisine.",
            "\"I've been reading a book about the history of gastronomy, {target}, and I can't help but share some fascinating facts with you,\" {initiator} begins the conversation, eager to discuss fine cuisine.",
            "\"{target}, I've just returned from a trip to Italy where I had the most amazing food. I can't stop raving about it. Care to hear more?\" {initiator} asks, hoping to engage {target} in a conversation about fine cuisine.",
            "\"I'm planning to host a dinner party and I want to create a menu that will blow everyone away. {target}, do you have any suggestions for a gourmet meal?\" {initiator} asks, seeking {target}'s expertise in fine cuisine.",
            "\"{target}, I recently tried this incredible fusion restaurant that combines different culinary traditions. I thought you might find it intriguing,\" {initiator} says, initiating a conversation about fine cuisine.",
            "\"{target}, I've been watching this cooking show that features world-renowned chefs. I can't get enough of it. Do you have any favorite chefs?\" {initiator} asks, hoping to discuss fine cuisine with {target}.",
            "\"I've been researching the art of wine pairing, {target}, and I'd love to share my findings with you. Are you interested in exploring the world of fine cuisine?\" {initiator} asks, eager to discuss the topic with {target}.",
            "\"{target}, I've always been fascinated by the artistry behind creating a perfect dish. Would you be interested in delving into the world of fine cuisine with me?\" {initiator} asks, hoping to engage {target} in a conversation about gourmet food."
        ],
    },
    'mixer_social_RudeIntroduction_greetings': {
        "pre_actions": [
            "{initiator} begins to rudely introduce themselves to {target}.",
        ],
        'actions': [
            "\"{target}, prepare yourself for the most unpleasant introduction you've ever experienced,\" {initiator} says with a smug grin.",
            "\"I hope you're ready to be insulted, {target}, because that's exactly what I'm about to do,\" {initiator} says, rolling their eyes.",
            "\"Listen up, {target}, because I'm about to give you a taste of my signature rudeness,\" {initiator} declares, crossing their arms.",
            "\"{target}, I'm about to show you just how rude I can be. Brace yourself,\" {initiator} warns, with a mocking tone.",
            "\"I apologize in advance, {target}, but I have a knack for making introductions as rude as possible,\" {initiator} says, not sounding apologetic at all.",
            "\"Prepare to be offended, {target}, because I'm about to unleash my rudeness upon you,\" {initiator} says, enjoying their own audacity.",
            "\"{target}, get ready for the most obnoxious introduction of your life,\" {initiator} says, smirking as if they were proud of their rudeness.",
            "\"I'm about to break every rule of politeness, {target}, so consider yourself warned,\" {initiator} says, with a mischievous glint in their eyes.",
            "\"{target}, you're about to witness the epitome of rudeness. Don't say I didn't warn you,\" {initiator} says, with a hint of amusement.",
            "\"{target}, I must warn you, my introduction is going to be incredibly rude. Brace yourself,\" {initiator} says, with a wicked grin."
        ],
    },
    'mixer_social_Flirt_targeted_romance_alwaysOn': {
        "pre_actions": [
            "{initiator} starts to flirt with {target}.",
        ],
        'actions': [
            "\"{target}, you know, I've always found you incredibly attractive,\" {initiator} says, flashing a playful smile.",
            "\"Has anyone ever told you how captivating your smile is, {target}? It's impossible not to be drawn to you,\" {initiator} says, their voice filled with admiration.",
            "\"You must have a secret potion, {target}, because every time I see you, my heart skips a beat,\" {initiator} says, flirtingly.",
            "\"Is it just me, or is it getting hotter in here, {target}? Your presence has this effect on me,\" {initiator} says, playfully fanning themselves.",
            "\"I have a confession to make, {target}. I can't help but be enchanted by your charm and charisma,\" {initiator} says, their eyes twinkling with mischief.",
            "\"Are you a magician, {target}? Because whenever you're around, everything else disappears, and it's just you and me,\" {initiator} says, flirtatiously.",
            "\"You have this magnetic energy, {target}, that pulls me towards you. I can't help but be drawn to you,\" {initiator} says, their voice filled with fascination.",
            "\"I hope you don't mind me saying this, {target}, but you have the most captivating eyes I've ever seen. They're impossible to resist,\" {initiator} says, their gaze fixed on {target}'s eyes.",
            "\"Can I be honest with you, {target}? Your smile has the power to brighten up even the darkest of days,\" {initiator} says, their voice filled with sincerity.",
            "\"I couldn't help but notice, {target}, that you possess a certain charm that makes it impossible for me to resist your company,\" {initiator} says, flirtatiously."
        ],
    },
    'mixer_social_FriendlyIntroduction_greetings': {
        "pre_actions": [
            '{initiator} starts a friendly conversation with {target} and introduces themselves.',
        ],
        "actions": [
            "\"Hi there, I\'m {initiator}. What\'s your name?",
            "\"Hey, I\'m {initiator}. Nice to meet you!",
            "\"Hello, I don\'t think we\'ve met. I\'m {initiator}. And you are?",
            "\"Nice to see a new face! I\'m {initiator}. What\'s your name?",
            "\"Hey, I\'m {initiator}. Mind if I join you?",
            "\"Hi, I\'m {initiator}. I\'ve been meaning to introduce myself. What\'s your name?",
            "\"Hey, how\'s it going? I\'m {initiator}. What\'s your name?",
            "\"Hello, I\'m {initiator}. It\'s a pleasure to make your acquaintance!",
            "\"Hi there, I\'m {initiator}. Just wanted to say hello!",
            "\"Hey, I\'m {initiator}. Care to chat?",
        ],
    },
    "mixer_social_FunnyIntroduction_greetings": {
        "pre_actions": [
            "{initiator} humorously introduces themselves to {target}. "
        ],
        "actions": [
            "\"{target}, I heard you needed a daily dose of laughter. Well, here I am, your personal joke doctor!\" {initiator} says with a wide grin.",
            "\"Hey {target}, they say laughter is the best medicine, so I guess I'm a licensed pharmacist!\" {initiator} quips, as they introduce themself.",
            "\"Knock, knock, {target}! Who's there? It's me, {initiator}, your new comedy companion!\" {initiator} says, chuckling at their own joke.",
            "\"{target}, I must warn you that being around me can cause extreme laughter and sore cheeks. Proceed at your own risk,\" {initiator} says playfully.",
            "\"Hello {target}, I promise I'm not a mime, but I've been known to leave people speechless with laughter,\" {initiator} says, making a mock serious face.",
            "\"{initiator} at your service, {target}! I'm here to turn that frown upside down, one joke at a time,\" {initiator} says, delivering a lighthearted salute.",
            "\"Hey {target}, I'm {initiator}, and if laughter were currency, I'd be a billionaire!\" {initiator} boasts with a cheeky grin.",
            "\"Nice to meet you, {target}! I'm {initiator}, and I have a PhD in giggles, chuckles, and guffaws,\" {initiator} says, offering a comically exaggerated bow.",
            "\"Hey there, {target}! I'm {initiator}, and I'm the person you call when you need a laugh and a half,\" {initiator} says, winking playfully.",
            "\"{target}, meet {initiator} - the human embodiment of laughter and joy. That's me, in case you were wondering,\" {initiator} says, laughing at their own introduction."
        ]
    },
    'mixer_social_EnchantingIntroduction_greetings_skills': {
        "pre_actions": [
            "{initiator} meets {target} for the first time, and gives them an enchanting introduction."
        ],
        "actions": [
            "\"Greetings, {target}. I am {initiator}, the master of captivating tales and the weaver of dreams. It is an honor to make your acquaintance.",
            "\"Ah, fair {target}, allow me to introduce myself. I am {initiator}, a soul enchanted by the mysteries of the world. May our encounter be as magical as the moonlit night.",
            "\"In the realm of enchantment, where whispers become melodies and dreams come alive, I am known as {initiator}. And you, dear {target}, what name graces your existence?",
            "\"Behold, {target}, for I am {initiator}, a conjurer of words and a guardian of imagination. Brace yourself, for the allure of my introduction shall transport you to realms yet unexplored.",
            "\"With a touch of whimsy and a dash of intrigue, I present myself before you, {target}, as {initiator}, a wanderer of realms unseen and a collector of tales untold. How does your spirit respond to such enchantment?",
            "\"In the realm of wonder, where reality intertwines with dreams, I am {initiator}, a custodian of curiosity and an emissary of imagination. And you, {target}, what treasures lie within your name?",
            "\"Listen, {target}, as the wind carries my words to your ears. I am {initiator}, a weaver of stories and a guardian of secrets. Dare you venture into the depths of my enchanting introduction?",
            "\"Ah, {target}, behold the enchantment that unfolds before you. I am {initiator}, a conjurer of wonder and a purveyor of dreams. Allow yourself to be swept away by the magic of our introduction.",
            "\"Step closer, {target}, and let me grace your senses with an introduction like no other. I am {initiator}, a whisper in the night and a sparkle in the twilight, forever enchanted by the possibilities that lie within our encounter.",
            "\"In a world where reality dances with fantasy, I emerge as {initiator}, a seeker of extraordinary tales and a harbinger of delight. And you, dear {target}, what wonders lie within your story?",
        ],
    },
    'mixer_social_AskAboutCareer_friendly_STC': {
        "pre_actions": [
            "{initiator} starts a conversation with {target} and asks about their career.",
        ],
        "actions": [
            "\"Hey {target}, I\'ve been meaning to ask you, how\'s your career going?\" {initiator} asks with genuine interest.",
            "\"I\'ve always admired your dedication to your career, {target}. Mind if I ask how it\'s been going lately?\" {initiator} inquires.",
            "\"Career talk time! I\'m curious, {target}, how\'s everything going in your professional life?\" {initiator} asks, leaning in.",
            "\"Can I pick your brain for a moment, {target}? How\'s your career shaping up these days?\" {initiator} asks, raising an eyebrow.",
            "\"I\'ve been curious about your career path, {target}. Mind if I ask how things are going on that front?\" {initiator} asks, sipping their coffee.",
            "\"Let\'s talk about work for a bit, {target}. How\'s your career treating you these days?\" {initiator} asks, leaning back in their chair.",
            "\"{target}, I\'ve been meaning to ask you about your career. Any exciting updates or challenges you\'d like to share?\" {initiator} asks, genuinely intrigued.",
            "\"I\'ve been thinking about our careers lately, {target}. Mind if we have a little chat about how things are going for you?\" {initiator} asks, smiling warmly.",
            "\"Tell me, {target}, how\'s your career journey been so far? Any interesting stories or milestones?\" {initiator} asks, leaning forward with anticipation.",
            "\"I\'ve been curious about your career lately, {target}. Mind if I ask how you\'ve been navigating the professional world?\" {initiator} asks, with a hint of curiosity in their voice."
        ],
    },
    'mixer_social_AskAboutFavoriteAuthor_targeted_Friendly_alwaysOn_skills': {
        "pre_actions": [
            "{initiator} asks {target} about their favorite author.",
        ],
        'actions': [
            "\"Who is your favorite author, {target}?\" {initiator} asks.",
            "\"I'm curious, {target}, who is your favorite author?\" {initiator} asks.",
            "\"If you had to pick one, who would you say is your favorite author?\" {initiator} asks {target}.",
            "\"Have you read any books by your favorite author lately, {target}?\" {initiator} asks.",
            "\"I've been meaning to ask, {target}, who is your go-to author?\" {initiator} asks.",
            "\"Do you have a favorite author, {target}?\" {initiator} asks with a smile.",
            "\"What book made you fall in love with your favorite author, {target}?\" {initiator} asks curiously.",
            "\"I'm in the mood for a good read. Any recommendations from your favorite author, {target}?\" {initiator} asks enthusiastically.",
            "\"Tell me about the first time you discovered your favorite author, {target}.\" {initiator} leans in, interested.",
            "\"If you could meet your favorite author, {target}, what would you ask them?\" {initiator} ponders aloud."
        ],
    },
    'mixer_social_AskAboutDay_targeted_Friendly_alwaysOn': {
        "pre_actions": [
            "{initiator} asks {target} about their day in a friendly manner.",
        ],
        "actions": [
            "\"Hey {target}, how has your day been?\" {initiator} asks.",
            "\"Did you have a good day {target}?",
            "\"What did you do today?\" {initiator} asks.",
            "\"Anything interesting happen today?\" {initiator} asks.",
            "\"How\'s your day been so far?\" {initiator} asks.",
            "\"How did your day go?\" {initiator} asks.",
            "\"What\'s been going on with you today?\" {initiator} asks.",
            "\"Tell me about your day!\" {initiator} exclaims.",
            "\"Have you had a productive day?\" {initiator} asks.",
        ],
    },
    'mixer_social_HeartfeltCompliment_targeted_friendly_emotionSpecific': {
        "pre_actions": [
            "{initiator} gives {target} a heartfelt compliment.",
        ],
        "actions": [
            "\"You look absolutely stunning today,\" {initiator} compliments {target}.",
            "\"I just wanted to say, you\'re incredibly talented,\" {initiator} praises {target}.",
            "\"I can\'t help but admire your determination and hard work,\" {initiator} tells {target}.",
            "\"You have such a kind and caring heart,\" {initiator} compliments {target}.",
            "\"Your creativity never ceases to amaze me,\" {initiator} tells {target} with admiration.",
            "\"I wanted to let you know that you inspire me,\" {initiator} expresses to {target}.",
            "\"You have a way with words that captivates everyone around you,\" {initiator} praises {target}.",
            "\"Your generosity and selflessness are truly remarkable,\" {initiator} acknowledges {target}.",
            "\"I wanted to say that you\'re an extraordinary person,\" {initiator} tells {target} sincerely.",
            "\"You have a beautiful soul,\" {initiator} compliments {target} genuinely."
        ],
    },
    'mixer_social_Hug_Friendly_Middlescore_NoMoodTest': {
        "actions": [
            "{initiator} gives {target} a hug.",
            "{initiator} gives {target} a friendly hug.",
            "{initiator} gives {target} a big hug.",
        ],
    },
    'mixer_social_Hug_targeted_Friendly_MiddleScore': {
        'actions': [
            "{initiator} gives {target} a hug.",
            "{initiator} gives {target} a friendly hug.",
            "{initiator} gives {target} a big hug.",
        ],
    },
    'mixer_social_SayGoodbye_targeted_Friendly_alwaysOn': {
        "pre_actions": [
            "{initiator} says goodbye to {target}, who is leaving."
        ],
        "actions": [
            "\"Goodbye, {target}! Take care!\" {initiator} waves.",
            "\"It was great seeing you, {target}. Goodbye!\" {initiator} smiles.",
            "\"Until next time, {target}. Goodbye!\" {initiator} says with a nod.",
            "\"Farewell, {target}. Have a wonderful day!\" {initiator} bids farewell.",
            "\"Goodbye, {target}! See you soon!\" {initiator} waves goodbye.",
            "\"Take care, {target}. Goodbye!\" {initiator} says warmly.",
            "\"Until we meet again, {target}. Goodbye!\" {initiator} gives a friendly wave.",
            "\"Have a safe journey, {target}. Goodbye!\" {initiator} offers their well wishes.",
            "\"Goodbye, {target}. It was nice spending time with you!\" {initiator} smiles warmly.",
            "\"Wishing you the best, {target}. Goodbye!\" {initiator} says with a hint of nostalgia.",
        ],
    },
    'mixer_social_ShareFishingTips_targeted_Friendly_alwaysOn_skills': {
        "pre_actions": [
            "{initiator} shares fishing tips with {target}."
        ],
        "actions": [
            "\"Hey {target}, I have some fishing tips for you,\" {initiator} says.",
            "\"I\'ve been fishing for years, {target}, let me share some tips with you,\" {initiator} offers.",
            "\"Are you interested in fishing, {target}? I can give you some valuable tips,\" {initiator} suggests.",
            "\"I heard you want to go fishing, {target}. Let me give you some advice,\" {initiator} offers kindly.",
            "\"\'ve discovered some great fishing techniques, {target}. Would you like me to share them with you?\" {initiator} asks with a smile.",
            "\"If you\'re planning to go fishing, {target}, I have some tips that might help you catch more fish,\" {initiator} offers eagerly.",
            "\"Fishing can be tricky, {target}, but I can give you some tips to make it easier,\" {initiator} says confidently.",
            "\"I\'ve learned a few tricks that might improve your fishing experience, {target}. Would you like to hear them?\" {initiator} asks curiously.",
            "\"I noticed you\'re interested in fishing, {target}. How about I give you some pointers to get started?\" {initiator} suggests warmly.",
            "\"I\'ve been studying different fishing techniques, {target}, and I think I have some valuable tips to share with you,\" {initiator} says excitedly.",
        ],
    },
    'mixer_social_GiveCookingTips_targeted_Friendly_alwaysOn_skills': {
        "pre_actions": [
            "{initiator} gives cooking tips to {target}."
        ],
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
        "pre_actions": [
            "{initiator} shares their cooking secrets with {target}."
        ],
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
        "pre_actions": [
            "{initiator} extolls the virtues of grilled cheese to {target}."
        ],
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
          "pre_actions": [
            "{initiator} flatters {target} by boosting their ego."
          ],
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
        "pre_actions": [
            "{initiator} gives relationship advice to {target}, in a friendly way."
        ],
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
        "pre_actions": [
            "{initiator} purposefully rips a big nasty fart.",
        ],
        "actions": [
            "\"{target}, prepare yourself for the most disgusting thing you've ever experienced,\" {initiator} says mischievously, before letting out a loud and noxious fart.",
            "{initiator} lets out a repulsive fart, grinning at {target} with satisfaction.",
            "\"{target}, I have a surprise for you. Brace yourself for the foulest smell known to man,\" {initiator} says, before releasing a fart that fills the air with a putrid stench.",
            "{initiator} lets out a fart so repugnant that it lingers in the room, making {target} gag.",
            "\"{target}, I apologize in advance for what you're about to witness,\" {initiator} says, before ripping a fart that can only be described as revolting.",
            "{initiator} lets out a disgusting fart, laughing as {target} recoils in disgust.",
            "\"{target}, I have a special gift for you,\" {initiator} says mischievously, before farting loudly and laughing.",
            "{initiator} breaks wind with a vengeance, smirking as {target} looks on in utter disgust.",
            "\"{target}, you won't believe what I can do,\" {initiator} says with a wicked grin, before releasing a fart that could clear a room.",
            "{initiator} lets out a fart so foul that it causes {target} to wrinkle their nose in disgust."
            
        ],
    },
    'mixer_social_RevealDeepSecret_targeted_Friendly_HighScore': {
        "pre_actions": [
            "{Initiator} confesses a profound, deeply-held secret to {target}."
        ],
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
        "pre_actions": [
            "{initiator} reveals their evil plans to {target}."
        ],
        "actions": [
            "\"{target}, I have a confession to make. Brace yourself, for what I\'m about to reveal is truly sinister,\" {initiator} says with a wicked grin.",
            "\"I\'ve been living a double life, {target}, and i\'s time you know the truth. Prepare yourself for the darkness that lies within me,\" {initiator} says, their voice dripping with malevolence.",
            "\"You thought you knew me, {target}, but you were wrong. The truth is, I\'ve been plotting something truly diabolical, and now it\'s time to involve you,\" {initiator} says, eyes gleaming with mischief.",
            "\"Listen carefully, {target}, for the secrets I\'m about to share will change everything. I\'ve been working on a plan, a plan so evil that it will shake the very foundations of this world,\" {initiator} whispers ominously.",
            "\"I\'ve always been envious of your innocence, {target}, but no more. Today, I reveal my true nature, and you\'ll witness the depths of my malevolence firsthand,\" {initiator} declares, a twisted smile forming on their lips.",
            "\"Prepare to be shocked, {target}, for the darkness that resides within me is about to be unleashed. My evil plans will leave a trail of chaos and destruction,\" {initiator} says, their voice laced with anticipation.",
            "\"You see, {target}, I\'ve been biding my time, waiting for the perfect moment to reveal my evil plans. And that moment is now,\" {initiator} says, a wicked glint in their eyes.",
            "\"I hope you\'re ready for this, {target}, because what I\'m about to disclose will shatter your perception of me. My evil schemes are far more intricate than you could have ever imagined,\" {initiator} says, relishing the impending revelation.",
            "\"There\'s a darkness inside me, {target}, and it\'s time you witness it. My evil plans are nearing fruition, and you\'re about to become an integral part of them,\" {initiator} says, a sinister chuckle escaping their lips.",
            "\"I\'ve kept my true intentions hidden for far too long, {target}. Today, I lay bare my evil plans before you, and together, we shall conquer this world,\" {initiator} proclaims, their voice filled with twisted ambition.",
        ],
    },
    "mixer_social_RevealBrilliantInvention_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} reveals their brilliant invention to {target}."
        ],
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
        "pre_actions": [
            "{initiator} attempts to scare {target}.",
        ],
        "actions": [
            "{initiator} sneaks up behind {target} and whispers, \"Boo!\" before bursting into laughter.",
            "\"{target}, did you know there's a legend about a ghost around here?\" {initiator} says, trying to spook {target}.",
            "\"Watch out, {target}! Something's right behind you!\" {initiator} exclaims, trying to startle {target}.",
            "{initiator} pretends to see something terrifying in the distance and shouts, \"{target}, look out!\"",
            "{initiator} decides to hide and jump out at {target} as they walk by, hoping to scare them.",
            "\"Be careful, {target}. I've heard strange noises around here lately. It sends shivers down my spine,\" {initiator} says, attempting to unnerve {target}."
        ]
    },
    "mixer_social_AskWhatHappened_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} asks {target} what happened.",
        ],
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
        "pre_actions": [
            "{initiator} asks {target} if they are single.",
        ],
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
        "pre_actions": [
            "{initiator} complains to {target} about having food poisoning.",
        ],
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
        "pre_actions": [
            "{initiator} begins a deep conversation with {target}.",
        ],
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
        "pre_actions": [
            "{initiator} and {target} banter like old friends.",
        ],
        "actions": [
            "\"{target}, do you remember the time we first met? I can't believe it's been so long!\" {initiator} says, laughing and reminiscing about the past.",
            "\"Hey {target}, I bet you still can't make a decent cup of coffee after all these years!\" {initiator} teases, smirking playfully.",
            "{initiator} grins at {target} and says, \"Remember when we used to argue about who was the better singer? I still think you owe me a rematch!\"",
            "\"After all this time, {target}, I still can't believe you're such a terrible dancer!\" {initiator} chuckles, poking fun at their friend.",
            "{initiator} playfully nudges {target} and says, \"So, have you finally learned how to cook something other than instant noodles?\"",
            "\"Remember that time you got us lost on our way to the concert, {target}? I'm amazed we're still friends after that fiasco!\" {initiator} says, laughing heartily.",
            "\"I still can't believe you used to wear those ridiculous outfits, {target}. How did we ever let you leave the house like that?\" {initiator} teases, chuckling.",
            "{initiator} grins at {target} and says, \"You know, I still owe you for that prank you pulled on me years ago. Watch your back, my friend!\"",
            "\"Hey {target}, do you still have that hideous painting you insisted on hanging in your living room? I can't believe you ever thought it was a good idea!\" {initiator} laughs, reminiscing about old times.",
            "\"It's hard to believe we've come so far, {target}. Remember when we used to dream about where we'd be now? I think we've done pretty well for ourselves!\" {initiator} says, smiling fondly at their friend."
        ]
    },
    "mixer_social_BrightenDay_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} brightens {target}'s day by saying something to cheer them up.",
        ],
        "actions": [
            "\"Hey, {target}, I know things have been tough lately. How about we go do something fun together?\" {initiator} suggests with a smile.",
            "\"Feeling blue, {target}? Let me tell you a joke to lighten the mood,\" {initiator} says, ready to share a funny story.",
            "\"Hey {target}, I know you're going through a lot right now, but remember that I'm always here for you. Let's talk about it,\" {initiator} suggests kindly.",
            "\"Sometimes, all it takes is a hug to make things better. Come here, {target},\" {initiator} says, opening their arms for a warm embrace.",
            "\"Let's get out of this rut, {target}. What can we do today to turn things around and make you feel better?\" {initiator} asks, ready to help in any way possible.",
            "\"{target}, I have something that might make you smile. Are you ready?\" {initiator} says with a mischievous grin.",
            "\"I know you've been feeling down lately, {target}, but I have just the thing to lift your spirits,\" {initiator} says, excitement in their voice.",
            "\"{target}, I've been thinking about what I could do to make you feel better, and I think I've come up with something,\" {initiator} says with a twinkle in their eye.",
            "\"Hey {target}, I've got a surprise for you. It's something that I hope will brighten your day,\" {initiator} says, unable to contain their excitement.",
            "\"I know you've been going through a rough patch, {target}, but I've got a little something that might bring a smile to your face,\" {initiator} says, a hint of anticipation in their voice.",
            "\"{target}, I've been racking my brain trying to think of something that would turn your day around. And I think I've finally found it,\" {initiator} says, a mixture of determination and hope in their tone.",
            "\"You deserve a little pick-me-up, {target}, so I've come up with something that I hope will make you feel better,\" {initiator} says, a warm smile on their face.",
            "\"I couldn't stand to see you sad, {target}, so I've decided to do something special just for you. Brace yourself,\" {initiator} says, their eyes sparkling with excitement.",
            "\"{target}, I have a surprise for you. It's something that I hope will bring some sunshine to your day,\" {initiator} says, unable to hide their enthusiasm.",
            "\"I've been thinking about you, {target}, and it hit me. I know exactly what would make you feel better. Are you ready?\" {initiator} says, anticipation evident in their voice."
        ]
    },
    "mixer_social_ComplainAboutLackofLoveLife_Targeted_Friendly_AlwaysOn_Jealous_Trait": {
        "pre_actions": [
            "{initiator} laments to {target} about their own romantic failures.",
        ],
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
        "pre_actions": [
            "{initiator} boasts to {target} about catching a big fish.",
        ],
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
        "pre_actions": [
            "{initiator} begins sharing a horrifying joke with {target}."
        ],
        "actions": [
            "\"{target}, I heard this joke the other day, and I just have to share it with you. It's a bit twisted, though,\" {initiator} says, grinning mischievously.",
            "\"Hey {target}, I've got a dark sense of humor, and I think this joke might be right up your alley. Can you handle it?\" {initiator} asks, raising an eyebrow.",
            "{initiator} leans in close to {target} and whispers, \"I've got a joke that might give you the creeps. Are you ready?\"",
            "\"Okay, {target}, brace yourself. I've got a joke that's not for the faint of heart,\" {initiator} says, a wicked smile on their face.",
            "\"Be warned, {target}, this joke is not for everyone. But I think you've got the stomach for it,\" {initiator} says, their eyes gleaming with anticipation.",
            "\"{target}, I've got a horrifying joke that I think you'll appreciate. Get ready to laugh and cringe at the same time,\" {initiator} says, rubbing their hands together in excitement.",
            "\"Alright, {target}, I've got a joke that's twisted and hilarious, but it's not for everyone. Are you in?\" {initiator} asks, a devilish grin on their face.",
            "{initiator} chuckles darkly and says to {target}, \"I've got a joke that might make your skin crawl. Do you want to hear it?\"",
            "\"Hey {target}, I've got a joke that's a little... morbid. But I think you'll like it,\" {initiator} says, a mischievous glint in their eye.",
        ],
    },
    "mixer_social_AskForAdvice_targeted_friendly_emotionSpecific_Scared": {
        "pre_actions": [
            "{initiator}, feeling scared, asks {target} for advice.",
        ],
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
        "pre_actions": [
            "{initiator} complains to {target} about their power being shut off due to not paying their electric bill.",
        ],
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
        "pre_actions": [
            "{initiator} begins complaining to {target} about their water being shut off as a consequence of not paying their water bill.",
        ],
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
        "pre_actions": [
            "{initiator} asks {target} for advice.",
        ],
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
        "pre_actions": [
            "{initiator} begs for {target}'s forgiveness.",
        ],
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
        "pre_actions": [
            "{initiator} asks {target} to become best friends with them.",
        ],
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
        "pre_actions": [
            "{initiator} introduces themselves to {target} by using a hilarious joke to break the ice."
        ],
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
        "pre_actions": [
            "{initiator} brags to {target} about having survived food poisoning.",
        ],
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
    "mixer_social_ThrowDrink_targeted_mean_emotionSpecific": {
        "pre_actions": [
            "{initiator} throws their drink at {target} in anger."
        ],
        "actions": [
            "{initiator} watches {target} closely, anger boiling up inside, before suddenly splashing a drink in {target}'s face without warning.",
            "Without hesitation, {initiator} grabs a nearby drink and throws it in {target}'s face.",
            "{initiator} can't take it anymore and, in a fit of rage, hurls a drink at {target}'s face, leaving them dripping and stunned.",
            "As {target} continues to speak, {initiator} seethes with anger before finally snapping and throwing the contents of their glass into {target}'s face.",
            "{initiator}, unable to contain their anger any longer, grabs the nearest beverage and splashes it all over {target}'s face, silencing them mid-sentence.",
            "With a sudden burst of fury, {initiator} picks up their drink and hurls it right into {target}'s unsuspecting face.",
            "{initiator} reaches their breaking point and, without a word, throws their drink directly at {target}'s face, shocking the entire room.",
            "Enraged by {target}'s words, {initiator} impulsively grabs a drink and drenches {target}'s face, instantly stopping their speech.",
            "{initiator} narrows their eyes at {target}, then suddenly flings the contents of their glass right into {target}'s face, leaving them speechless.",
            "Overcome with anger, {initiator} snatches up a drink and tosses it all over {target}'s face, causing gasps from everyone around them.",
        ]
    },
    "mixer_social_TakePictureTogether_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} asks {target} to take a picture together with them.",
        ],
        "actions": [
            "\"{target}, let's capture this moment together! Can I take a picture with you?\" {initiator} asks, smiling excitedly.",
            "\"Hey {target}, this is such a great time, we should take a picture to remember it by. What do you say?\" {initiator} suggests, holding up their phone.",
            "\"{target}, I've always wanted a picture with you. Mind if we take one right now?\" {initiator} asks, looking hopeful.",
            "\"Would you mind if we took a photo together, {target}? I think it would be a nice memory to have,\" {initiator} says, shyly.",
            "\"I have this feeling that we're going to look back on this moment one day and smile. Let's take a picture together, {target},\" {initiator} proposes, grinning.",
            "\"Come on, {target}, let's snap a quick picture together. I promise it'll be worth it!\" {initiator} says, trying to convince {target}.",
            "\"Life's too short not to capture memories, don't you think, {target}? Let's take a picture together,\" {initiator} suggests, extending their arm for a selfie.",
            "\"Hey {target}, I think this is the perfect moment for a photo, don't you? Let's take one together!\" {initiator} says, enthusiastically.",
            "\"{target}, you know what would make this moment even better? A picture of us together. Let's take one!\" {initiator} says, grabbing their phone.",
            "\"I want to remember this moment forever, {target}. Let's take a picture together, please?\" {initiator} asks, their eyes shining with anticipation."
        ]
    },
    "mixer_social_ShowOffMuscles_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} boastfully shows off their muscles to {target}, hoping to impress them.",
        ],
        "actions": [
            "\"{target}, check out these guns,\" {initiator} says, flexing their biceps proudly.",
            "\"Hey, {target}, I've been working out lately, and I want to show you my progress. What do you think?\" {initiator} asks, rolling up their sleeves to reveal toned muscles.",
            "\"Guess who's been hitting the gym, {target}? Feast your eyes on these bad boys,\" {initiator} says, confidently flexing their muscles.",
            "\"{target}, I think my hard work is finally paying off. Care to take a look at these muscles?\" {initiator} grins, striking a pose.",
            "\"Look at this, {target}!\" {initiator} exclaims, flexing their arms to show off their newfound strength.",
            "\"{target}, I've been trying to get in shape lately. What do you think of the progress I've made?\" {initiator} asks, proudly displaying their muscles.",
            "\"I've been putting in some serious effort at the gym, {target}. Care to check out the results?\" {initiator} says, flexing for emphasis.",
            "\"Remember how I said I was going to get fit, {target}? Well, take a look at these muscles now!\" {initiator} boasts, proudly showing off their gains.",
            "\"Hey, {target}, I've been working on my fitness, and I wanted to show you the results. What do you think?\" {initiator} asks, flexing their muscles.",
            "\"Check this out, {target}! I think all those workouts are finally starting to show,\" {initiator} says, proudly displaying their toned muscles."
        ]
    },
    # "mixer_socials_TellJoke_group_Funny_alwaysOn": {
    #     "actions": [
    #         "\"{target}, you're going to love this one,\" {initiator} says, a grin spreading across their face as they prepare to tell a joke.",
    #         "\"Hey {target}, have you heard this one before?\" {initiator} asks, chuckling before they share the joke with the group.",
    #         "\"{initiator} suddenly bursts into laughter, catching {target}'s attention. \"You've got to hear this joke,\" they say, eager to share.",
    #         "\"Everyone, especially you {target}, listen up! I've got a hilarious joke to tell,\" {initiator} announces, drawing the group's attention.",
    #         "\"Alright, this one's for you, {target}. I know you love a good joke,\" {initiator} says, ready to deliver the punchline.",
    #         "\"{initiator} leans in closer to {target} and the others, a mischievous smile on their face. \"You guys ready for this?\" they ask before diving into the joke.",
    #         "\"I just heard the funniest joke, and I have to share it with you, {target},\" {initiator} says, barely containing their laughter.",
    #         "\"{initiator} looks at {target} and grins. \"You're going to appreciate this one,\" they say, eager to share the joke with the group.",
    #         "\"Okay, {target}, this joke is right up your alley. Gather 'round, everyone!\" {initiator} exclaims, preparing to entertain the group.",
    #         "\"I found a joke that I know will make you laugh, {target}. Let me tell it to everyone,\" {initiator} says, excited to bring some humor to the group."
    #     ]
    # },
    "mixer_social_ProvideLogicalSolution_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} provides a logical solution to {target}'s problem.",
        ],
        "actions": [
            "\"{target}, I've been thinking about the issues you're facing, and I believe I've come up with some logical solutions,\" {initiator} says confidently.",
            "\"Hey {target}, I know you're struggling with this problem, but I think I have a few ideas that might help,\" {initiator} offers with a hopeful smile.",
            "\"{target}, I've been giving your situation some thought, and I've come up with a few logical steps you could take to resolve it,\" {initiator} suggests carefully.",
            "\"I couldn't help but overhear your problem, {target}, and I think I might have some rational solutions you could try,\" {initiator} says, trying not to sound intrusive.",
            "\"Don't worry, {target}. I've been analyzing your situation and I think I have a few possible solutions for you,\" {initiator} reassures, attempting to lift {target}'s spirits.",
            "\"Hey {target}, I've been considering your problem, and I believe I can help you come up with some logical strategies to tackle it,\" {initiator} says encouragingly.",
            "\"I understand you're going through a tough time, {target}, but I think I might have some reasonable solutions that could help you out,\" {initiator} offers kindly.",
            "\"{target}, I've been pondering your predicament and came up with a few logical approaches you could try. Would you like to hear them?\" {initiator} asks gently.",
            "\"Let's sit down and discuss your problem, {target}. I'm sure we can come up with some logical and effective solutions together,\" {initiator} proposes with a supportive tone.",
            "\"Listen, {target}, I think I have some ideas on how you can logically address your issue. Let's work through this together,\" {initiator} says, extending a helping hand."
        ]
    },
    "mixer_social_TalkAboutBestBait_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} begins a conversation with {target} about the best bait to use for fishing.",
        ],
        "actions": [
            "\"{target}, do you have any advice on the best bait to use when fishing? I'm trying to improve my chances of catching something,\" {initiator} asks curiously.",
            "\"I've heard there are different baits for different fish, {target}. What do you think works best around here?\" {initiator} inquires, hoping for some local knowledge.",
            "\"Hey {target}, I've been experimenting with various baits while fishing. What's your go-to choice?\" {initiator} asks, seeking expert advice.",
            "\"I'm pretty new to fishing, {target}, and I was wondering if you could give me some tips on choosing the best bait,\" {initiator} requests, looking for guidance.",
            "\"{target}, I noticed you've had quite the success with fishing. Mind sharing your secret on the best bait to use?\" {initiator} probes, wanting to learn from the best.",
            "\"So, {target}, I've been trying different baits, but I can't seem to find one that really works well. Any suggestions?\" {initiator} asks, hoping for a breakthrough.",
            "\"Between live bait and artificial lures, what do you think works best when fishing, {target}?\" {initiator} inquires, seeking a better understanding of the options.",
            "\"{target}, I've read so many articles about the best bait for fishing, but I'd really appreciate your opinion. What's your favorite choice?\" {initiator} asks, valuing personal experience.",
            "\"Everyone seems to have their own preference when it comes to fishing bait, {target}. What's your personal favorite, and why?\" {initiator} questions, trying to learn from different perspectives.",
            "\"I've been struggling to find the right bait for fishing, {target}. Can you share your top picks and maybe some tips on when to use each one?\" {initiator} asks, seeking a comprehensive answer."
        ]
    },
    "mixer_social_TalkAboutCooking_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} starts a friendly conversation about cooking with {target}."
        ],
        "actions": [
            "\"{target}, I've been thinking about trying out a new recipe. Any suggestions?\" {initiator} asks curiously.",
            "\"I've been wanting to get better at cooking, {target}. Could you share some of your culinary secrets with me?\" {initiator} inquires.",
            "\"Hey, {target}, I was wondering if you could teach me how to make that amazing dish you prepared last time,\" {initiator} says with excitement.",
            "\"I've been trying to expand my cooking skills, {target}. What do you think is a must-try recipe?\" {initiator} asks enthusiastically.",
            "\"Last night I tried my hand at a new recipe, {target}. Have you ever had a cooking disaster?\" {initiator} asks, chuckling.",
            "\"{target}, I've heard you're quite the chef. I'd love to learn some tips and tricks from you,\" {initiator} says, admiringly.",
            "\"You always seem to know your way around the kitchen, {target}. How did you learn to cook so well?\" {initiator} asks, genuinely curious.",
            "\"I'm planning a dinner party, {target}, and I could use some advice on what to cook. Can you help me come up with a menu?\" {initiator} asks hopefully."
        ]
    },
    # "mixer_social_TellEngagingStory_group_Friendly_MiddleScore": {
    #     "actions": [
    #         "\"{target}, gather around everyone, I have a story to share that I think you'll all find captivating,\" {initiator} says with a grin.",
    #         "\"Hey {target} and everyone, let me share this incredible story I heard the other day. You won't believe what happened!\" {initiator} exclaims, excitement in their voice.",
    #         "\"Have I ever told you all the story about the time I stumbled upon something extraordinary? Gather 'round, {target}, I promise it's worth a listen,\" {initiator} says, eyes sparkling with anticipation.",
    #         "\"Everyone, including you {target}, listen up! I have a tale to tell that will leave you on the edge of your seats,\" {initiator} announces with a theatrical flourish.",
    #         "\"You know, {target}, there's a story I've been meaning to share with you and the rest of the group. I think it's finally time,\" {initiator} says, a twinkle in their eye.",
    #         "\"Alright, {target} and friends, it's time for a little storytime. Trust me, you'll want to hear this one,\" {initiator} says, a mischievous smile playing on their lips.",
    #         "\"Have I got a story for you, {target}! Gather the others, and let me regale you with a most intriguing tale,\" {initiator} says, clearly eager to share their story.",
    #         "\"Hey {target}, remember that story I mentioned a while ago? I think it's time I shared it with the whole group,\" {initiator} says, excitement building in their voice.",
    #         "\"Picture this, {target} and everyone: I was minding my own business when the most unbelievable thing happened. Let me tell you all about it,\" {initiator} says, drawing the group in with their enthusiasm.",
    #         "\"{target}, do you and the others have a moment? I'd like to share an amazing story that I think you'll all enjoy,\" {initiator} says, eager to captivate their audience."
    #     ]
    # },
    # "mixer_social_TellUnbelievableStory_group_friendly_emotionspecific": {
    #     "actions": [
    #         "\"{target}, you're not going to believe what happened to me last night,\" {initiator} starts, a gleam in their eye.",
    #         "\"I've got a crazy story to tell, guys. Gather around and prepare for the unbelievable,\" {initiator} announces to {target} and their friends.",
    #         "\"{target}, have I got a story for you and the rest of the group! You won't believe what happened,\" {initiator} says excitedly.",
    #         "\"Everyone, listen up! I've got an incredible story to share that you won't believe,\" {initiator} says, looking at {target} and the rest of the group.",
    #         "\"Okay, {target}, this is going to sound totally unreal, but I've got to share this story with you and everyone else,\" {initiator} says with a grin.",
    #         "\"Guys, I need to tell you all about this unbelievable experience I had,\" {initiator} says, getting the attention of {target} and the others.",
    #         "\"Listen up, {target} and friends, I've got a wild story that you just have to hear,\" {initiator} says, ready to share their unbelievable tale.",
    #         "\"Get ready for the most unbelievable story of your lives, {target} and the rest of you,\" {initiator} says confidently.",
    #         "\"{target}, remember how you always say I have the craziest stories? Well, I've got another one for you and the group,\" {initiator} says, preparing to share their latest adventure.",
    #         "\"Everyone, gather around. I've got an unbelievable story that you all need to hear, especially you, {target},\" {initiator} says, eager to share their tale."
    #     ]
    # },
    "mixer_social_TalkAboutGrilledCheese_targeted_Friendly_alwaysOn_aspiration": {
        "pre_actions": [
            "{initiator} starts a conversation about grilled cheese with {target}."
        ],
        "actions": [
            "\"{target}, have you ever tried a grilled cheese sandwich with a twist? I experimented with some ingredients the other day,\" {initiator} says enthusiastically.",
            "\"Hey {target}, do you know the secret to making the perfect grilled cheese sandwich? I've been trying to master it,\" {initiator} asks, looking for advice.",
            "\"Grilled cheese sandwiches always remind me of my childhood, {target}. Do you have any special memories with them?\" {initiator} inquires, feeling nostalgic.",
            "\"The other day, I had the most amazing grilled cheese sandwich, {target}. Let me tell you all about it,\" {initiator} says, eager to share their experience.",
            "\"I've been craving a grilled cheese sandwich all day, {target}. Do you have any unique recipes I should try?\" {initiator} asks, hoping for some inspiration.",
            "\"{target}, have you ever tried a sweet version of a grilled cheese sandwich? I'm thinking about experimenting with some dessert-inspired fillings,\" {initiator} suggests, looking for input.",
            "\"Did you know, {target}, that there are so many different types of grilled cheese sandwiches around the world? I was amazed when I discovered it,\" {initiator} says, excited to share their newfound knowledge.",
            "\"I came across a grilled cheese food truck the other day, {target}. It got me thinking about how versatile and universally loved this simple sandwich is,\" {initiator} muses.",
            "\"Every time I make a grilled cheese sandwich, I think about the first time I made one with my mom, {target}. It's such a comforting memory,\" {initiator} shares, fondly recalling the past.",
            "\"I've been perfecting my grilled cheese sandwich recipe, {target}, and I think I've finally cracked it. Want to try one and give me your honest opinion?\" {initiator} asks, hoping for feedback."
        ]
    },
    "mixer_social_ShareSecret_targeted_Friendly_HighScore": {
        "pre_actions": [
            "{initiator} shares a secret with {target}, their trusted friend."
        ],
        "actions": [
            "\"{target}, can I tell you something? I know it's a bit out of the blue, but I feel like I can trust you,\" {initiator} says timidly.",
            "\"Hey, {target}, there's something I've been wanting to share with you. I think you're the right person to confide in,\" {initiator} says, taking a deep breath.",
            "\"{target}, I've been keeping something from you, and it's time I let it out. I hope you understand,\" {initiator} says, looking nervous.",
            "\"You know, {target}, there's something I've been hiding for a while, but I think it's time I tell you,\" {initiator} says hesitantly.",
            "\"{target}, I've never shared this with anyone before, but I feel like you're someone I can trust. So here it goes,\" {initiator} says, gathering up their courage.",
            "\"I've been carrying this secret around for a long time, {target}, and I think it's time to finally share it with someone. Can I trust you?\" {initiator} asks cautiously.",
            "\"{target}, I want to tell you something, something I've never told anyone else. Are you okay with that?\" {initiator} says, looking for confirmation.",
            "\"You're someone I really trust, {target}, and I feel like I can share this secret with you. I hope you don't think differently of me afterward,\" {initiator} says with a hint of worry.",
            "\"Can I confide in you, {target}? There's something I've been keeping to myself, and I think you're the right person to share it with,\" {initiator} says, looking hopeful.",
            "\"Hey, {target}, I know we've gotten pretty close, and there's something I think you should know about me. I've never told anyone before, but I trust you,\" {initiator} says sincerely."
        ]
    },
    "mixer_social_SharePhoto": {
        "pre_actions": [
            "{initiator} shares a photo with {target}."
        ],
        "actions": [
            "\"{target}, check this out! I've got a really cool photo on my phone I want to show you,\" {initiator} says excitedly.",
            "\"{target}, I came across this photo and I think you'll find it interesting. Take a look,\" {initiator} suggests, offering their phone to {target}.",
            "\"I was browsing my gallery and found this picture that made me laugh. I thought you'd enjoy it too,\" {initiator} says, grinning as they show {target} their phone screen.",
            "\"Can I show you something, {target}? I took this photo the other day and I think you'll really appreciate it,\" {initiator} says, scrolling through their phone.",
            "\"Look at this photo I found on my phone, {target}. It brings back such great memories,\" {initiator} says nostalgically, showing the picture to {target}.",
            "\"Hey {target}, I took this photo and I think it turned out really well. What do you think?\" {initiator} asks, seeking {target}'s opinion as they hand over their phone.",
            "\"{target}, this photo I found on my phone is just too good not to share. You have to see it,\" {initiator} says enthusiastically, presenting their phone to {target}.",
            "\"I captured this beautiful moment on my phone, {target}. I think you'll love it. Take a look,\" {initiator} says, proud of their photography skills as they show the picture to {target}.",
        ]
    },
    "mixer_social_TalkAboutNewApp_targeted_Friendly_alwaysOn_career": {
        "pre_actions": [
            "{initiator} begins a conversation with {target} about the new app they are developing."
        ],
        "actions": [
            "\"{target}, I've been working on this new app, and I think it could really change things. Can I share it with you?\" {initiator} asks excitedly.",
            "\"Hey {target}, I've got this great idea for an app I've been developing. Mind if I run it by you?\" {initiator} inquires, eager for input.",
            "\"{target}, I've been pouring my heart into this new app idea, and I really value your opinion. Can we talk about it?\" {initiator} asks nervously.",
            "\"I've been tinkering with this new app concept, and I think it has potential. Would you mind giving me your thoughts on it, {target}?\" {initiator} suggests, hoping for feedback.",
            "\"Guess what, {target}? I'm working on a groundbreaking app, and I'd love to hear your thoughts on it. Are you up for a chat?\" {initiator} asks, bubbling with enthusiasm.",
            "\"{target}, I've been secretly developing this app that I think could be the next big thing. Can I share it with you and get your opinion?\" {initiator} questions, a twinkle in their eye.",
            "\"So, I have this new app idea, {target}, and I can't get it out of my head. Can we discuss it? I'd love your input,\" {initiator} says, a hint of desperation in their voice.",
            "\"I've been working on this app, and I'm at a crossroads. {target}, I need your expertise. Can we talk about it?\" {initiator} asks, seeking guidance.",
            "\"You know, {target}, I've been developing this new app, and I'm really proud of it. I'd be honored if you'd take a look and share your thoughts,\" {initiator} says, beaming with pride.",
            "\"Hey {target}, do you have a minute? I've been working on this new app, and I could really use your insight. Are you available to chat?\" {initiator} asks, hoping for a positive response."
        ]
    },
    "mixer_social_ThankForComing_targeted_Friendly_alwaysOn_Event": {
        "pre_actions": [
            "{initiator} thanks {target} for attending their event."
        ],
        "actions": [
            "\"{target}, I just wanted to take a moment to thank you for coming to the event. It means a lot to me,\" {initiator} says with a warm smile.",
            "\"{target}, I can't express how grateful I am for your presence at the event. Your support means the world to me,\" {initiator} says sincerely.",
            "\"{target}, thank you so much for being here at the event. Your presence makes it even more special,\" {initiator} says, appreciating the gesture.",
            "\"I just wanted to say how much I appreciate you coming to the event, {target}. It wouldn't have been the same without you,\" {initiator} says, making eye contact.",
            "\"Your attendance at the event means more to me than I can put into words, {target}. Thank you for being here,\" {initiator} says, touched by the gesture.",
            "\"{target}, seeing you at the event made my day. Thank you for taking the time to be here and support me,\" {initiator} says gratefully.",
            "\"I'm so glad you could make it to the event, {target}. Your presence truly made a difference,\" {initiator} says with a smile.",
            "\"{target}, I can't thank you enough for showing up at the event. Your support means everything to me,\" {initiator} says earnestly.",
            "\"Having you at the event made all the difference, {target}. Thank you for being here and supporting me,\" {initiator} says, clearly touched.",
            "\"{target}, I just wanted to let you know how much it meant to me that you came to the event. Your support has been incredible,\" {initiator} says, expressing their gratitude."
        ]
    },
    "mixer_social_TellDirtyJoke_targeted_funny_emotionSpecific": {
        "pre_actions": [
            "{initiator} tells a dirty joke to {target}."
        ],
        "actions": [
            "\"{target}, I just heard the most hilarious dirty joke. You've got to listen to this one,\" {initiator} says with a mischievous grin.",
            "\"Hey {target}, you've got a good sense of humor, right? Check out this dirty joke I just heard,\" {initiator} says, laughing in anticipation.",
            "\"{target}, I don't usually share these kinds of jokes, but this one is too good not to share. Are you ready?\" {initiator} asks with a cheeky smile.",
            "\"Alright, {target}, brace yourself for the funniest dirty joke I've ever heard. You're going to love it,\" {initiator} says, barely containing their laughter.",
            "\"Listen up, {target}, because I've got a dirty joke that'll have you rolling on the floor laughing,\" {initiator} says, grinning from ear to ear.",
            "\"Okay {target}, I promise you've never heard a dirty joke like this one. Are you ready for it?\" {initiator} asks, giggling in anticipation.",
            "\"{target}, I've been dying to tell you this dirty joke I heard the other day. You have to hear it,\" {initiator} says, suppressing a laugh.",
            "\"I know you'll appreciate this one, {target}. Prepare yourself for the best dirty joke ever,\" {initiator} says, already laughing at the thought.",
            "\"Hey {target}, I've got a dirty joke that's perfect for you. Are you ready for this?\" {initiator} asks, smirking.",
            "\"This dirty joke is just too good not to share, {target}. Get ready to laugh your socks off,\" {initiator} says, eager to share the punchline."
        ]
    },
    # "mixer_social_TellDramaticStory_group_Friendly_MiddleScore": {
    #     "actions": [
    #         "\"{target}, gather around with the others. I have a tale that will leave you all on the edge of your seats,\" {initiator} announces with a grin.",
    #         "\"{target}, do you remember the time I barely escaped from a dangerous situation? Let me share the story with everyone,\" {initiator} says, excitement in their voice.",
    #         "\"Everyone, including you, {target}, needs to hear this incredible story I have to tell. Gather around and listen closely,\" {initiator} says, motioning for the group to come closer.",
    #         "\"I've got a story that I've been dying to share with all of you, especially you, {target}. So, lend me your ears and prepare to be amazed,\" {initiator} says, an eager look on their face.",
    #         "\"Have I ever told you the story of my most dramatic adventure, {target}? No? Well, let's gather the group and I'll share it with everyone,\" {initiator} suggests, excitedly.",
    #         "\"There's this remarkable story I want to share with everyone. {target}, you and the others should definitely listen to this one,\" {initiator} says, with a twinkle in their eye.",
    #         "\"{target}, you and the rest of the group need to hear this incredible tale of danger and suspense. Trust me, it's a nail-biter,\" {initiator} says, gesturing for everyone to gather around.",
    #         "\"Everyone, including you, {target}, should gather around for an epic story I'm about to share. It's one you'll never forget,\" {initiator} says, grinning from ear to ear.",
    #         "\"I have a story that I think will captivate everyone, especially you, {target}. So, let's gather around and I'll begin this amazing tale,\" {initiator} says, their eyes filled with anticipation.",
    #         "\"{target}, do you and the others have time for an incredible story? Because I have one that will leave you all speechless,\" {initiator} says, the excitement evident in their voice."
    #     ]
    # },
    # "mixer_socials_TellFunnyStory_group_Funny_alwaysOn": {
    #     "actions": [
    #         "\"{target}, have I ever told you about the time when I accidentally walked into a stranger's house? Trust me, it's hilarious,\" {initiator} says, grinning.",
    #         "\"Hey {target}, I've got a story that will have you in stitches. Gather 'round, everyone, and prepare to laugh,\" {initiator} announces, beaming.",
    #         "\"Everyone, I just remembered this hilarious incident that happened to me a while ago, and I think {target} especially will get a kick out of it,\" {initiator} says, chuckling.",
    #         "\"{target}, you and the others have got to hear this one. I promise it's a story you'll never forget,\" {initiator} says, eyes twinkling with amusement.",
    #         "\"Alright, {target} and friends, buckle up for a funny story. I guarantee it'll have you laughing out loud,\" {initiator} says, a mischievous smile on their face.",
    #         "\"Guys, wait until you hear this story. It's so funny, even {target} won't be able to keep a straight face,\" {initiator} teases, excited to share the tale.",
    #         "\"Okay, {target}, you know how I'm always getting into ridiculous situations? Well, this one tops them all, and I need to share it with the group,\" {initiator} says, barely suppressing laughter.",
    #         "\"Everyone, gather 'round! I have a story that is sure to make {target} laugh, and possibly the rest of you as well,\" {initiator} says, trying to contain their own laughter.",
    #         "\"I can't believe I haven't told you guys this story yet. It's absolutely hilarious, and I know {target} especially will appreciate it,\" {initiator} says, a wide grin spreading across their face.",
    #         "\"Alright, {target}, this one's for you. I guarantee you'll be rolling on the floor laughing by the end of this story,\" {initiator} says, eager to entertain the group."
    #     ]
    # },
    "mixer_social_MakePeaceAfterFight": {
        "pre_actions": [
            "{initiator} attempts to make peace with {target} after having a fight."
        ],
        "actions": [
            "\"{target}, I've had some time to think, and I want to apologize for our fight. Can we talk and find a way to move forward?\" {initiator} asks, extending an olive branch.",
            "\"I realize I let my emotions get the best of me, {target}. I'm sorry. Can we put this behind us and start fresh?\" {initiator} says, hoping for reconciliation.",
            "\"{target}, I've been thinking about our argument, and I want you to know that I value our relationship more than being right. Let's make peace,\" {initiator} suggests sincerely.",
            "\"Hey, {target}, I know we've had our differences, but I want to make amends. Can we find common ground and move past this?\" {initiator} asks earnestly.",
            "\"I hate that we've been at odds, {target}. I'm willing to put my pride aside and apologize. Can we work towards understanding each other better?\" {initiator} proposes, looking for resolution.",
            "\"Life's too short to hold grudges, {target}. I'm sorry for our fight, and I hope we can rebuild our bond,\" {initiator} says, offering a sincere apology.",
            "\"{target}, our friendship means more to me than any disagreement. Let's put this behind us and focus on the future. Are you with me?\" {initiator} asks, seeking reconciliation.",
            "\"I know we both said things we didn't mean, {target}. I'm sorry. Let's agree to disagree and move on from this,\" {initiator} says, hoping for a positive response.",
            "\"Can we talk, {target}? I want to apologize for my part in our argument. I hope we can find a way to heal and move forward together,\" {initiator} says, looking for closure.",
            "\"I've been reflecting on our fight, {target}, and I realize how much I value our relationship. Let's forgive each other and start anew,\" {initiator} suggests, offering a heartfelt apology."
        ]
    },
    # "mixer_social_TellOutrageousStory_group_Funny_HighScore": {
    #     "actions": [
    #         "\"{target}, you won't believe what happened to me the other day. Gather around, everyone; you'll want to hear this!\" {initiator} exclaims, excitedly.",
    #         "\"Hey {target}, have you ever heard something so crazy that it's hard to believe? Well, buckle up, because I've got a story for you and the others,\" {initiator} says, grinning.",
    #         "\"{target}, gather everyone together. I've got an incredible story to share, and you're all going to love it!\" {initiator} says, eyes sparkling with excitement.",
    #         "\"Everyone, listen up! You won't believe what happened to me. {target}, you especially are going to enjoy this one,\" {initiator} announces with enthusiasm.",
    #         "\"I've got to tell you all something that happened to me. It's so wild, you'll think I'm making it up. {target}, you're in for a treat,\" {initiator} says, chuckling.",
    #         "\"Alright, everyone, I've got a story for you that's so outrageous, you'll be talking about it for days. {target}, you're going to love this,\" {initiator} says, with a mischievous grin.",
    #         "\"{target}, call the others over! I've got a story that's so unbelievable, you'll think I've lost my mind,\" {initiator} exclaims, barely containing their laughter.",
    #         "\"Guys, you won't believe what happened! Get over here and let me tell you this incredible story. {target}, you won't want to miss this,\" {initiator} says, waving everyone closer.",
    #         "\"Everyone, gather around! I've got a story that's so outlandish, you'll question if it's even possible. {target}, trust me, you're going to want to hear this,\" {initiator} says, a broad smile on their face.",
    #         "\"Listen up, folks! I've got an extraordinary story to tell, and I need everyone to hear it. {target}, make sure you're paying attention. You'll never believe what I'm about to share,\" {initiator} insists, clearly eager to share their tale."
    #     ]
    # },
    "mixer_social_SelfDeprecatingJoke_group_funny_emotionSpecific": {
        "pre_actions": [
            "{initiator} makes a self-deprecating joke about themselves to {target}."
        ],
        "actions": [
            "\"{target}, you know what's funny about me? I'm the kind of person who...\" {initiator} starts, chuckling at their own expense.",
            "\"{target}, have you heard this one about me? It's hilarious, but a little embarrassing,\" {initiator} says with a grin.",
            "\"Hey {target}, I've got a joke for you, and the punchline is... me!\" {initiator} laughs, poking fun at themselves.",
            "\"You know what's really funny, {target}? My life! Let me tell you about this ridiculous thing I did,\" {initiator} says, laughing at their own misfortune.",
            "\"{target}, you'll get a kick out of this. I can't believe I actually did this, but it's too funny not to share,\" {initiator} admits, shaking their head in amusement.",
            "\"Alright, {target}, I've got a hilarious story for you. But fair warning, I'm the butt of the joke,\" {initiator} says, grinning sheepishly.",
            "\"I don't know if I should be embarrassed or proud of this, {target}, but I've got a great self-deprecating joke to share,\" {initiator} says, chuckling.",
            "\"Get ready to laugh, {target}, because I've got a joke that makes me look like a total fool,\" {initiator} confesses, already laughing at themselves.",
            "\"{target}, I've got a story that proves I'm not the brightest bulb in the box, but at least it's good for a laugh,\" {initiator} says, poking fun at their own expense.",
            "\"I can't believe I'm going to tell you this, {target}, but I did something so dumb that it's actually hilarious. You ready?\" {initiator} asks, grinning at their own misadventure."
        ]
    },
    "mixer_social_BroBump_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} does a bro bump with {target}.",
        ],
        "actions": [
            "\"{target}, that was awesome! Bring it in for a bro bump,\" {initiator} says, grinning and raising their fist.",
            "\"Hey {target}, let's celebrate with a bro bump!\" {initiator} says, extending their fist towards {target}.",
            "{initiator} smiles at {target} and says, \"We make a great team! Bro bump?\"",
            "\"Nice one, {target}! Fist bump to celebrate?\" {initiator} suggests, holding out their fist.",
            "{initiator} looks at {target} and says, \"You've earned yourself a bro bump for that one, my friend!\"",
            "\"Hey {target}, that deserves a bro bump! Bump it, buddy!\" {initiator} says, enthusiastically offering their fist.",
            "{initiator} laughs and says, \"{target}, that was epic! Let's seal the deal with a bro bump.\"",
            "\"Great job, {target}! Let's do a bro bump for our success,\" {initiator} says, raising their fist with a smile.",
            "{initiator} nods approvingly at {target} and says, \"I like your style. Bro bump?\"",
            "\"Way to go, {target}! How about a bro bump to commemorate this moment?\" {initiator} asks, holding out their fist."
        ]
    },
    "mixer_social_BroHug_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} gives a bro hug to {target}.",
        ],
        "actions": [
            "\"{target}, it's been a rough day, man. Come here,\" {initiator} says, opening their arms for a bro hug.",
            "\"Hey, {target}, I know things have been tough lately. Bring it in, buddy,\" {initiator} says, offering a comforting bro hug.",
            "{initiator} smiles at {target} and says, \"You did great today, man. Let's hug it out.\"",
            "\"{target}, I'm really proud of you, man. Let's celebrate with a bro hug,\" {initiator} suggests, extending their arms.",
            "\"Come on, {target}, don't be shy. We're friends, right? Let's have a bro hug,\" {initiator} says, encouragingly.",
            "{initiator} walks up to {target} and says, \"You know what this moment calls for? A solid bro hug.\"",
            "\"Hey, {target}, it's been a while since we've seen each other! Let's have a proper bro hug,\" {initiator} says, happily.",
            "\"Nothing like a good old-fashioned bro hug to show our appreciation for each other, right {target}?\" {initiator} says, grinning.",
            "{initiator} pats {target} on the back and says, \"You've been a real friend, {target}. Let's seal it with a bro hug.\"",
            "\"Sometimes, words just aren't enough, {target}. Let's hug it out, man,\" {initiator} says, opening their arms for a bro hug."
        ]
    },
    "mixer_social_DoAnImpression_targeted_funny_alwaysOn": {
        "pre_actions": [
            "{initiator} does an impression of someone, in order to make {target} laugh."
        ],
        "actions": [
            "\"{target}, check this out! I've been working on this impression, and I think I've finally nailed it,\" {initiator} says, excitement in their eyes.",
            "\"Hey {target}, you know who this is?\" {initiator} asks, their voice and demeanor changing as they launch into their impression.",
            "\"{target}, do you remember that famous scene from the movie? I can do an impression of the main character,\" {initiator} says with a grin.",
            "\"You've got to see this, {target}. I've been practicing this impression lately, and I think it's pretty hilarious,\" {initiator} says, chuckling.",
            "\"Okay {target}, guess who I'm impersonating,\" {initiator} says, suddenly changing their voice and mannerisms.",
            "\"Hey {target}, I have a little surprise for you,\" {initiator} says, before launching into a spot-on impression.",
            "\"Ready for a laugh, {target}? I've been working on this new impression, and I can't wait to show it to you,\" {initiator} says eagerly.",
            "\"{target}, I think I've finally mastered this impression. Tell me what you think,\" {initiator} says, as their face transforms into a different persona.",
            "\"Witness my hidden talent, {target}. My impression of this character is sure to make you smile,\" {initiator} says, beaming with confidence.",
            "\"Prepare to be amazed, {target}. I've been practicing this impression just for you,\" {initiator} says, their excitement infectious."
        ]
    },
    "mixer_social_KnockKnockJoke_targeted_funny_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} initiates a knock knock joke with {target}."
        ],
        "actions": [
            "\"{target}, I've got a funny one for you. Knock knock,\" {initiator} says with a grin.",
            "\"Hey {target}, I heard this hilarious knock knock joke. Want to hear it?\" {initiator} asks excitedly.",
            "\"Knock knock, {target}! Are you ready for a good laugh?\" {initiator} says, chuckling.",
            "\"{target}, I just learned this great knock knock joke. You've got to hear it!\" {initiator} says, barely containing their laughter.",
            "\"Alright, {target}, I've got a classic one for you. Knock knock,\" {initiator} says with a playful smile.",
            "\"Let's lighten the mood, {target}. Knock knock!\" {initiator} says, eager to share the joke.",
            "\"Knock knock! You're going to love this one, {target},\" {initiator} says, anticipating a laugh.",
            "\"I've got a knock knock joke that's perfect for you, {target}. Ready?\" {initiator} asks with a smirk.",
            "\"Okay, {target}, I bet I can make you laugh with this one. Knock knock,\" {initiator} says confidently.",
            "\"Hey {target}, I've got a knock knock joke that's too good not to share. Here it goes,\" {initiator} says, preparing to deliver the punchline."
        ]
    },
    "mixer_social_DiscussInterests_friendly_STC": {
        "pre_actions": [
            "{initiator} discusses their interests with {target}, in a friendly way."
        ],
        "actions": [
            "\"{target}, I've been wondering what you're passionate about. Care to share?\" {initiator} asks with genuine curiosity.",
            "\"Hey {target}, you know, we've never really talked about our hobbies and interests. What do you enjoy doing in your free time?\" {initiator} inquires.",
            "\"So, {target}, I've been meaning to ask you - what is it that you're truly interested in?\" {initiator} starts the conversation.",
            "\"{target}, we've known each other for a while now, but I feel like there's still so much to learn about each other. What are your interests?\" {initiator} questions, eager to deepen their connection.",
            "\"I was thinking, {target}, that it's about time we talk about what makes us tick. What are you passionate about?\" {initiator} proposes.",
            "\"Hey {target}, I'd love to know more about your interests and hobbies. Maybe we have something in common,\" {initiator} suggests, smiling.",
            "\"{target}, we've talked about so many things, but not about our interests. I'd love to hear about yours,\" {initiator} says, hoping to learn something new.",
            "\"You know, {target}, I've always been curious about what you're truly passionate about. Care to enlighten me?\" {initiator} asks playfully.",
            "\"{target}, I was just thinking about how our friendship has grown, and I realized we've never really discussed our interests. What do you like to do for fun?\" {initiator} wonders.",
            "\"Let's talk about something different today, {target}. Tell me about your interests and what makes you happy,\" {initiator} says, looking forward to an engaging conversation."
        ]
    },
    "mixer_social_BoldPickUpLine_targeted_romance_emotionSpecific": {
        "pre_actions": [
            "{initiator} uses a bold pick-up line on {target}.",
        ],
        "actions": [
            "\"{target}, if you were a vegetable, you'd be a 'cute-cumber',\" {initiator} says with a cheeky grin.",
            "\"Do you believe in love at first sight, {target}, or should I walk by again?\" {initiator} asks playfully.",
            "\"Are you a magician, {target}? Because every time I look at you, everyone else disappears,\" {initiator} says with a flirtatious smile.",
            "\"Is your name Google, {target}? Because you've got everything I've been searching for,\" {initiator} says confidently.",
            "\"Can I follow you home, {target}? Cause my parents always told me to follow my dreams,\" {initiator} says, trying to impress.",
            "\"Is your dad a boxer, {target}? Because, damn, you're a knockout!\" {initiator} exclaims with a wink.",
            "\"Do you have a map, {target}? I keep getting lost in your eyes,\" {initiator} says, gazing deeply into {target}'s eyes.",
            "\"Are you a camera, {target}? Every time I look at you, I smile,\" {initiator} says, flashing a charming grin.",
            "\"Excuse me, {target}, but I think you owe me a drink. When I looked at you, I dropped mine,\" {initiator} says, feigning embarrassment.",
            "\"Can I take a picture of you, {target}? I want to show Santa exactly what I want for Christmas,\" {initiator} says teasingly."
        ]
    },
    "mixer_social_ComplimentAppearance_targeted_romance_alwaysOn": {
        "pre_actions": [
            "{initiator} romantically compliments {target}'s appearance.",
        ],
        "actions": [
            "\"{target}, you look absolutely stunning today. I just had to say it,\" {initiator} says with a smile.",
            "\"Wow, {target}, I can't help but notice how great you look. What's your secret?\" {initiator} asks, genuinely impressed.",
            "\"Your outfit is on point today, {target}. You have a fantastic sense of style,\" {initiator} comments, admiring {target}'s appearance.",
            "\"Your hair looks amazing, {target}. It really suits you,\" {initiator} says, unable to hide their admiration.",
            "\"{target}, I must say, you have a radiant smile. It's truly captivating,\" {initiator} compliments sincerely.",
            "\"Is it just me or do you always manage to look so effortlessly good, {target}?\" {initiator} asks, clearly impressed.",
            "\"I can't help but notice how beautiful your eyes are, {target}. They're truly mesmerizing,\" {initiator} says, looking into {target}'s eyes.",
            "\"{target}, you have a certain glow about you today. It's really attractive,\" {initiator} comments, clearly appreciating {target}'s appearance.",
            "\"Your style is so unique, {target}. It really sets you apart from everyone else,\" {initiator} says, expressing their admiration.",
            "\"I've always thought you were good-looking, {target}, but today you've taken it to a whole new level,\" {initiator} says, clearly impressed."
        ]
    },
    "mixer_social_EnthuseAboutInterests_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} enthuses about their interests to {target}.",
        ],
        "actions": [
            "\"{target}, I am so excited to talk to you about my favorite hobbies and interests! I think you'll find them fascinating,\" {initiator} exclaims, beaming with excitement.",
            "\"Hey {target}, do you want to know what I'm really passionate about? I'd love to share my interests with you,\" {initiator} says with a wide grin.",
            "\"{target}, I've always wanted to talk to you about the things I love doing. I think you would really enjoy them too,\" {initiator} says, eager to share their interests.",
            "\"I had such a great time doing my favorite activities this weekend, {target}. Let me tell you all about them,\" {initiator} says enthusiastically.",
            "\"You know what, {target}? I've realized we never really talked about my hobbies and interests. Let me share them with you,\" {initiator} exclaims excitedly.",
            "\"Hey {target}, I've been wanting to share my favorite pastimes with you for a while now. I think you'll find them really interesting,\" {initiator} says with a bright smile.",
            "\"I can't wait to tell you about my favorite things, {target}. I have a feeling you'll love them as much as I do,\" {initiator} says, looking thrilled.",
            "\"{target}, I really want to share my passions with you. I think it'll help us understand each other better,\" {initiator} says, looking forward to the conversation.",
            "\"Did I ever tell you about my favorite hobbies, {target}? I'd love to discuss them with you and maybe even try them together,\" {initiator} suggests, full of enthusiasm.",
            "\"I've been looking forward to discussing my interests with you, {target}. I think it's time I share what I'm passionate about,\" {initiator} says, eyes sparkling with excitement."
        ]
    },
    "mixer_social_JokeAboutFashion_targeted_funny_alwaysOn_Skills": {
        "pre_actions": [
            "{initiator} playfully reminisces about past fashion trends with {target}.",
        ],
        "actions": [
            "{initiator} looks at {target} and chuckles, \"Can you believe people actually used to wear those ridiculously oversized shoulder pads?\"",
            "\"Hey, {target}, remember when wearing socks with sandals was considered a fashion statement?\" {initiator} teases, laughing.",
            "{initiator} smirks at {target} and says, \"Did you ever try those low-rise jeans? I don't know how anyone thought they were comfortable!\"",
            "\"{target}, have you seen those pictures of people wearing neon-colored windbreakers in the '90s? What were they thinking?\" {initiator} asks, giggling.",
            "\"Remember when people used to wear turtlenecks under everything, {target}? What a funny fashion choice,\" {initiator} says, grinning.",
            "\"Hey, {target}, do you recall the time when people would wear sweaters tied around their necks? It's hilarious to think about now,\" {initiator} laughs.",
            "{initiator} chuckles at {target} and says, \"Did you ever own a pair of those massive platform shoes? I can't believe we thought those were stylish!\"",
            "\"{target}, can you imagine wearing a tracksuit to a fancy dinner? I bet people in the 2000s never thought that would be a thing!\" {initiator} jokes, smirking.",
            "\"Hey, {target}, what do you think about bringing back the mullet? It's about time for a revival, don't you think?\" {initiator} says, laughing.",
            "{initiator} snickers and asks {target}, \"Do you remember when people used to wear skirts over pants? What an odd combination, right?\""
        ]
    },
    "mixer_social_BragAboutHandiness_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} brags to {target} about their handiness skill.",
        ],
        "actions": [
            "\"{target}, did you know that I can fix pretty much anything around the house? I'm pretty much a pro,\" {initiator} says proudly.",
            "\"You know, {target}, I've been told I have quite the knack for handiwork. It's like I have a magic touch,\" {initiator} boasts with a grin.",
            "\"Hey, {target}, have I ever mentioned how skilled I am when it comes to handiwork? I could practically be a professional handyman,\" {initiator} claims with confidence.",
            "\"I can't help but brag, {target}, but my handiness skills are pretty legendary. I've never met a repair I couldn't tackle,\" {initiator} says with a smirk.",
            "\"I've always had a talent for fixing things, {target}. It's like I was born with a wrench in one hand and a hammer in the other,\" {initiator} says, trying to impress {target}.",
            "\"{target}, you should see me in action when it comes to repairs. I'm like a superhero of handiness,\" {initiator} declares, puffing out their chest.",
            "\"Whenever something needs fixing, {target}, I'm the go-to person. I have a real gift,\" {initiator} says, clearly proud of their skills.",
            "\"Handiness is my middle name, {target}. I can fix things you wouldn't even think were repairable,\" {initiator} brags with a wide smile.",
            "\"I've always been the handy one in my family, {target}. I can fix anything, from a leaky faucet to a broken door hinge,\" {initiator} says, hoping to impress {target}.",
            "\"Let me tell you, {target}, when it comes to handiness, I'm a master. I've got the magic touch when it comes to repairs,\" {initiator} proclaims, beaming with pride."
        ]
    },
    "mixer_social_EnthuseAboutOutdoors_targeted_Friendly_MiddleScore": {
        "pre_actions": [
            "{initiator} enthuses about their love for the outdoors to {target}.",
        ],
        "actions": [
            "\"{target}, have you ever spent time in the great outdoors? There's something so magical about it,\" {initiator} says, eyes sparkling with enthusiasm.",
            "\"Did I ever tell you about the time I went camping, {target}? It was such an amazing experience,\" {initiator} begins, eager to share the story.",
            "\"You know, {target}, I've always found solace in nature. It's like a sanctuary away from the chaos of life,\" {initiator} says with a sigh of contentment.",
            "\"{target}, have you ever gone hiking or explored a dense forest? I'd love to do that someday,\" {initiator} says, a dreamy look in their eyes.",
            "\"I'm thinking of planning a trip to the mountains, {target}. There's something about the crisp air and lush greenery that calls to me,\" {initiator} shares, excitedly.",
            "\"{target}, I've always been fascinated by the beauty and mysteries of the great outdoors. What are your thoughts on it?\" {initiator} asks, hoping to engage in a meaningful conversation.",
            "\"Do you remember the last time we were out in nature, {target}? I can still feel the warmth of the sun and the gentle breeze on my skin,\" {initiator} reminisces, a smile playing on their lips.",
            "\"There's a certain sense of freedom that comes from being in the great outdoors, don't you think, {target}?\" {initiator} says, looking for agreement.",
            "\"Whenever I feel stressed or overwhelmed, {target}, I find solace in the thought of escaping to the great outdoors, where I can breathe and find peace,\" {initiator} confides, seeking understanding.",
            "\"Let's plan a trip together, {target}, something that encompasses the beauty of the great outdoors. I think it would be the perfect adventure for us,\" {initiator} suggests, eyes shining with hope."
        ]
    },
    "mixer_social_Fight_targeted_mean_Ghost": {
        "pre_actions": [
            "{initiator} angrily starts a fight with {target}, who is a ghost."
        ],
        "actions": [
            "\"{target}, I can feel your presence here, but I don't understand why you're haunting me,\" {initiator} says, frustration creeping into their voice.",
            "\"{target}, I know you're here, and I'm tired of your ghostly antics. Show yourself and let's talk about this,\" {initiator} demands, clenching their fists.",
            "\"I can't take this anymore, {target}! I know you're a ghost, but you can't just keep messing with my life!\" {initiator} shouts, their anger reaching a boiling point.",
            "\"Enough, {target}! I don't know what's keeping you here, but we need to resolve this issue now!\" {initiator} exclaims, trying to confront the unseen spirit.",
            "\"{target}, I've tried to ignore you, but now it's time for us to settle this. Your ghostly presence is not welcome here anymore!\" {initiator} yells, feeling both fear and anger.",
            "\"It's time for us to face each other, {target}. I won't let your ghostly presence control me any longer,\" {initiator} asserts, gathering their courage.",
            "\"Stop hiding, {target}! I know you're a ghost, but I'm not afraid to confront you,\" {initiator} says defiantly, standing their ground.",
            "\"Why are you doing this, {target}? You're a ghost, but that doesn't give you the right to torment me!\" {initiator} exclaims, frustration evident in their voice.",
            "\"Your ghostly games need to end now, {target}. I'm done being afraid and letting you control my life,\" {initiator} states firmly, ready to confront the spirit.",
            "\"{target}, I won't let you haunt me any longer. Come out and face me, so we can resolve this once and for all,\" {initiator} challenges, determined to stand up to the ghost."
        ]
    },
    "mixer_social_CalmDown_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} calms {target} down in a friendly way.",
        ],
        "actions": [
            "\"{target}, take a deep breath and try to relax. I'm here for you,\" {initiator} says soothingly.",
            "\"Hey, {target}, let's just take a moment to breathe and clear our heads, okay?\" {initiator} suggests gently.",
            "\"{target}, I know you're upset, but let's try to stay calm and talk this through,\" {initiator} says, placing a reassuring hand on {target}'s shoulder.",
            "\"Everything is going to be alright, {target}. Just take a few deep breaths, and we'll figure this out together,\" {initiator} reassures.",
            "\"{target}, let's slow down and take a step back. We can handle this situation better if we're both calm,\" {initiator} advises.",
            "\"Hey, {target}, remember that breathing technique we learned? Let's try it together to help you calm down,\" {initiator} says supportively.",
            "\"Listen, {target}, I need you to focus on your breathing and try to calm down. We'll get through this together,\" {initiator} encourages.",
            "\"{target}, I know it's hard, but let's try to stay calm. We can find a solution if we keep our heads clear,\" {initiator} says with a comforting smile.",
            "\"Let's take a moment to regroup, {target}. A clear mind will help us handle this better,\" {initiator} suggests, looking into {target}'s eyes.",
            "\"Deep breaths, {target}. Inhale, exhale. Remember, I'm here for you, and we'll get through this,\" {initiator} says softly."
        ]
    },
    "mixer_social_HoldHands_targeted_romance_middleScore": {
        "pre_actions": [
            "{initiator} begins holding {target}'s hand romantically."
        ],
        "actions": [
            "\"{target}, can I hold your hand? There's just something about the way our fingers intertwine that feels so right,\" {initiator} says softly.",
            "\"Your hands are so warm, {target}. I feel a connection every time we touch,\" {initiator} says, gently taking {target}'s hands in theirs.",
            "\"{target}, your hands are like a safe haven for me. May I hold them for a little while?\" {initiator} asks with a tender smile.",
            "\"Every time I touch your hands, {target}, I feel like I've come home. Do you mind if I hold them?\" {initiator} says, looking into {target}'s eyes.",
            "\"I love the way our hands fit together, {target}. It's like we were made for each other,\" {initiator} says, slowly reaching for {target}'s hands.",
            "\"{target}, can I hold your hands? There's something so comforting and familiar about the way they feel in mine,\" {initiator} says, searching for a connection.",
            "\"Your hands are so gentle, {target}. I can't help but want to hold them,\" {initiator} says, taking {target}'s hands and looking deeply into their eyes.",
            "\"May I hold your hands, {target}? The warmth and tenderness I feel when our fingers touch is indescribable,\" {initiator} asks with a loving smile.",
            "\"Can I hold your hands, {target}? There's something about the way they feel in mine that makes my heart skip a beat,\" {initiator} says, full of affection.",
            "\"Whenever I hold your hands, {target}, I feel like our souls are connected. I hope you feel the same way,\" {initiator} says, reaching for {target}'s hands with love and care."
        ]
    },
    "mixer_social_GivePepTalk_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} gives a pep talk to {target}."
        ],
        "actions": [
            "\"{target}, I know you're feeling down, but I believe in you. You're stronger than you think,\" {initiator} says with encouragement.",
            "\"{target}, don't let this setback define you. You can overcome anything if you put your mind to it,\" {initiator} reassures.",
            "\"When life knocks you down, {target}, you've got to get back up and keep going. I know you can do it,\" {initiator} offers, trying to lift {target}'s spirits.",
            "\"You've got so much potential, {target}. Don't let insecurities hold you back. Believe in yourself,\" {initiator} urges with sincerity.",
            "\"{target}, I've seen you overcome so many obstacles. This is just another challenge, and I know you can handle it,\" {initiator} says confidently.",
            "\"Sometimes, {target}, all it takes is a little faith in yourself. You've got this. I believe in you,\" {initiator} says, offering a supportive smile.",
            "\"{target}, remember all the times you've succeeded against the odds? You've got that same strength within you now,\" {initiator} reminds, hoping to inspire.",
            "\"Take a deep breath, {target}, and trust yourself. You're capable of great things, and I'll be here to support you every step of the way,\" {initiator} promises.",
            "\"You're not alone, {target}. We're in this together, and I have no doubt that you'll come out on top,\" {initiator} says, trying to boost {target}'s confidence.",
            "\"Don't let fear hold you back, {target}. You're stronger than you know, and you can achieve anything you set your mind to,\" {initiator} encourages, looking into {target}'s eyes."
        ]
    },
    "mixer_social_Fight_targeted_mean": {
        "pre_actions": [
            "{initiator} angrily starts a fight with {target}."
        ],
        "actions": [
            "\"{target}, I can't believe you would do something like that! You've really crossed the line this time,\" {initiator} says angrily, clenching their fists.",
            "\"Enough is enough, {target}! I'm tired of you always trying to control everything. We need to settle this,\" {initiator} shouts, their patience wearing thin.",
            "\"{target}, you've been pushing my buttons for far too long. I can't take it anymore! Let's settle this once and for all,\" {initiator} exclaims, their face red with anger.",
            "\"I never thought it would come to this, {target}, but you've left me with no choice. We need to fight this out,\" {initiator} says, frustration evident in their voice.",
            "\"Your constant meddling in my life has finally pushed me over the edge, {target}. It's time we settle our differences,\" {initiator} declares, their eyes narrowed in anger.",
            "\"I tried to avoid this, {target}, but you just won't back off. We have to fight and sort this out,\" {initiator} says, taking a defensive stance.",
            "\"Sometimes talking just isn't enough, {target}. Let's resolve this the old-fashioned way,\" {initiator} suggests, their voice filled with determination.",
            "\"{target}, you've provoked me for the last time. I'm not going to let you walk all over me anymore. Let's do this,\" {initiator} challenges, stepping forward.",
            "\"I've put up with your nonsense for too long, {target}. This ends now,\" {initiator} says, their breathing heavy with anger.",
            "\"Your actions have finally pushed me to my breaking point, {target}. It's time to settle our feud,\" {initiator} says, gritting their teeth and raising their fists."
        ]
    },
    "mixer_social_GossipAboutVideoGamePros_targeted_friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} gossips about video game professionals with {target}." 
        ],
        "actions": [
            "\"{target}, have you seen that new Twitch streamer that everyone's talking about?\" {initiator} asks, clearly excited to share some gossip.",
            "\"Hey, {target}, did you hear what happened on {streamer}'s stream yesterday? Let me fill you in,\" {initiator} says with a grin.",
            "\"You know, {target}, I can't believe what some Twitch streamers get up to these days. Have you heard the latest?\" {initiator} asks, eager to discuss the gossip.",
            "\"I was watching this Twitch streamer last night, {target}, and you wouldn't believe what they said! Let's talk about it,\" {initiator} suggests, itching to chat.",
            "\"Did you catch that drama between those two Twitch streamers, {target}? I need someone to discuss it with,\" {initiator} says, wide-eyed.",
            "\"Hey, {target}, have you seen the rumors about that popular Twitch streamer? Let me tell you all about it,\" {initiator} says, excited to share the juicy details.",
            "\"{target}, I was just reading about this Twitch streamer who got into some serious trouble. You've got to hear this,\" {initiator} says, leaning in closer.",
            "\"Have you been keeping up with the latest Twitch streamer gossip, {target}? There's so much to talk about!\" {initiator} exclaims, ready to dive into the conversation.",
            "\"I couldn't help but overhear some interesting news about a Twitch streamer earlier, {target}. Sit down, and let's chat,\" {initiator} says, eager to discuss the story.",
            "\"Can you believe what's been happening with those Twitch streamers, {target}? Let's grab a coffee and talk about it,\" {initiator} suggests, unable to contain their excitement."
        ]
    },
    "mixer_social_EnhuseAboutNewAlbums_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} enthuses about new music albums to {target}."
        ],
        "actions": [
            "\"{target}, have you heard about the new albums that just dropped? I'm really excited to discuss them with you,\" {initiator} says enthusiastically.",
            "\"Hey {target}, there are a few new albums out now that I think you'd be interested in. Let's chat about them!\" {initiator} suggests with a smile.",
            "{initiator} excitedly approaches {target} and says, \"I've been listening to some newly released albums, and I can't wait to hear your thoughts on them!\"",
            "\"So, {target}, I've been checking out some fresh music releases, and I really want to know what you think of them,\" {initiator} says, eager for a conversation.",
            "\"Hey {target}, I was just listening to a couple of new albums and thought you'd be the perfect person to discuss them with. What do you say?\" {initiator} asks.",
            "{initiator} leans in and asks {target}, \"Did you get a chance to listen to the latest albums that just came out? I'd love to hear your opinions on them.\"",
            "\"{target}, I just came across some amazing new music releases, and I'm dying to know if you've heard them and what you think!\" {initiator} says with excitement.",
            "\"Have you been keeping up with the new albums that just hit the scene, {target}? I'd love to get your take on them,\" {initiator} inquires with genuine interest.",
            "\"I can't help but think of you when I listen to these new albums, {target}. Let's talk about them and see if we share the same opinions,\" {initiator} suggests.",
            "\"Hey {target}, let's have a listening party and discuss the new albums that were just released. I think we'll have a lot to talk about,\" {initiator} proposes with anticipation."
        ]
    },
    "mixer_social_DiscussWorldPeace_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} begins a friendly discussion about world piece with {target}."
        ],
        "actions": [
            "\"{target}, have you ever thought about what it would take to achieve world peace?\" {initiator} asks, genuinely curious.",
            "\"{initiator}, do you think it's even possible for us to reach a point where there's peace across the globe?\" {target} wonders, as they begin a deep conversation.",
            "\"World peace seems like a distant dream, {target}, but I believe it's worth striving for. What's your take on it?\" {initiator} inquires, looking for insights.",
            "\"Sometimes I imagine a world without war or conflict, {target}. Do you think humanity can one day achieve that?\" {initiator} asks thoughtfully.",
            "{initiator} and {target} sit down and begin discussing the concept of world peace, exploring various ideas and opinions on how to make it a reality.",
            "\"You know, {target}, I've always wondered if peace can truly exist in a world as diverse as ours. What do you think?\" {initiator} starts the conversation, hoping for a meaningful exchange.",
            "\"{target}, considering all the conflicts and struggles in the world, do you believe there's a way to reach a state of global harmony?\" {initiator} asks, seeking {target}'s perspective.",
            "\"I've been pondering the idea of world peace lately, {target}. Can you share your thoughts on the topic?\" {initiator} requests, eager to hear a different viewpoint.",
            "{initiator} brings up the topic of world peace, asking {target} to share their thoughts on the possibility of achieving it and the challenges they might face.",
            "\"World peace is an ideal that many strive for, {target}. In your opinion, can it ever become a reality?\" {initiator} asks, hoping to spark a thought-provoking conversation."
        ]
    },
    "mixer_social_EnthuseAboutNewShow_targeted_Friendly_MiddleScore": {
         "pre_actions": [
            "{initiator} enthuses about a new television show to {target}."
         ],
        "actions": [
            "\"{target}, have you seen that new show everyone's been talking about? I just started watching it and it's amazing!\" {initiator} says excitedly.",
            "\"Hey, {target}, I just started watching this new show on TV and I think you'll love it! Want to know more about it?\" {initiator} asks with enthusiasm.",
            "\"{target}, I came across this new show last night and I can't stop thinking about it. Have you heard of it?\" {initiator} inquires, eager to discuss.",
            "\"I've been hooked on this new TV show, {target}. Have you seen it yet? I'd love to hear your thoughts,\" {initiator} says, hoping for a conversation.",
            "\"{target}, I know you're into these kinds of shows, so I wanted to tell you about this new one I found. I think you'll really enjoy it!\" {initiator} shares with a smile.",
            "\"Hey, {target}, you're always up-to-date on TV shows. Have you checked out the new one everyone's talking about?\" {initiator} asks curiously.",
            "\"I just discovered this amazing new show, {target}, and I can't wait to discuss it with you. Have you seen it?\" {initiator} says, looking for common ground.",
            "\"{target}, I stumbled upon this new show and it reminded me of that one we used to watch together. Have you seen it yet?\" {initiator} reminisces.",
            "\"I know you have great taste in television, {target}, so I wanted to ask if you've seen this new show I've been enjoying lately,\" {initiator} says, eager for {target}'s opinion.",
            "\"Last night, I started watching this incredible new show, {target}. I think it's right up your alley. Have you caught an episode yet?\" {initiator} asks with anticipation."
        ]
    },
    "mixer_social_AskToBeGirlfriend_targeted_romance_relationship": {
        "pre_actions": [
            "{initiator} asks {target} to be their girlfriend.",
        ],
        "actions": [
            "\"{target}, I've been thinking about this for a while, and I need to know... would you consider being my girlfriend?\" {initiator} asks nervously.",
            "\"Hey, {target}, I can't imagine my life without you. Would you do me the honor of being my girlfriend?\" {initiator} says with a hopeful smile.",
            "\"So, {target}, I've realized that you're the one who makes me happiest. What do you say about being my girlfriend?\" {initiator} asks, trying to gauge {target}'s reaction.",
            "\"{target}, our friendship means the world to me, but I think I want something more. Would you like to be my girlfriend?\" {initiator} says, taking a deep breath.",
            "\"I've been falling for you for a while now, {target}, and I can't hold it in any longer. Will you be my girlfriend?\" {initiator} asks, looking into {target}'s eyes.",
            "\"{target}, you're such an amazing person, and I can't help but want to be with you. Would you be my girlfriend?\" {initiator} says, hoping for a positive response.",
            "\"I don't know how to say this, {target}, but I've developed strong feelings for you. Will you take a chance on me and be my girlfriend?\" {initiator} asks hesitantly.",
            "\"Life's too short to not take chances, {target}, so I'm taking one now. Would you consider being my girlfriend?\" {initiator} says, holding {target}'s hand.",
            "\"I've tried to deny it, {target}, but my heart is set on you. I can't help but wonder if you'd be my girlfriend,\" {initiator} says, anxiously awaiting {target}'s answer.",
            "\"You make me laugh, you make me feel alive, and I can't imagine anyone else by my side, {target}. Would you be my girlfriend?\" {initiator} asks with a sincere smile."
        ]
    },
    "mixer_social_EnthuseAboutGuitarSolos_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} starts an enthusiastic conversation about guitar solos to {target}."
        ],
        "actions": [
            "\"{target}, have you ever heard that epic guitar solo in 'Stairway to Heaven'? It's mind-blowing!\" {initiator} exclaims excitedly.",
            "\"Hey {target}, I just listened to this amazing guitar solo, and I couldn't wait to share it with you. You've got to hear it!\" {initiator} says, grinning from ear to ear.",
            "\"{target}, you won't believe the guitar solo I just discovered! It's so incredibly powerful - I just had to tell you about it,\" {initiator} says, eyes sparkling with enthusiasm.",
            "\"I was just listening to some classic rock, {target}, and I realized we've never discussed our favorite guitar solos. What's yours?\" {initiator} asks, eager for a conversation.",
            "\"Have you ever noticed how guitar solos can completely change the mood of a song, {target}? Let's talk about some of our favorites,\" {initiator} suggests, brimming with excitement.",
            "\"Remember that concert we went to, {target}? The guitarist played the most incredible solo! It still gives me chills just thinking about it,\" {initiator} reminisces, eyes wide with amazement.",
            "\"I know you're a big music fan, {target}, so I wanted to ask you: what do you think makes a truly unforgettable guitar solo?\" {initiator} questions, their enthusiasm contagious.",
            "\"{target}, I've been on a guitar solo binge lately, and I'd love to hear your thoughts on some of the most legendary solos in music history. Care to join me?\" {initiator} invites excitedly.",
            "\"I was just practicing some guitar solos, {target}, and I can't help but marvel at the skill and emotion behind them. Let's chat about our favorites and maybe discover some new ones,\" {initiator} proposes, brimming with excitement.",
            "\"Hey {target}, I was wondering if you've ever tried playing any iconic guitar solos? They're so much fun to learn and discuss with fellow guitar enthusiasts like you,\" {initiator} says, eager to connect over their shared passion."
        ]
    },
    "mixer_social_AskOnDateEvent_targeted_romance_alwaysOn": {
        "pre_actions": [
            "{initiator} asks {target} to go on a date with them.",
        ],
        "actions": [
            "\"{target}, I've been thinking about this for a while, and I would love to take you on a date. What do you say?\" {initiator} asks, a hopeful smile on their face.",
            "\"Hey {target}, I was wondering if you'd like to go out with me sometime? I think we could have a great time together,\" {initiator} suggests, looking excited.",
            "\"So, {target}, I've been meaning to ask you this, but would you like to go on a date with me?\" {initiator} inquires, trying to gauge {target}'s reaction.",
            "\"{target}, I've always enjoyed our time together, and I was wondering if you'd be interested in going on a date?\" {initiator} asks, a bit nervous but eager to hear the response.",
            "\"Hey, {target}, I've been thinking... How about we make our next hangout a date? Just you and me?\" {initiator} proposes, looking into {target}'s eyes.",
            "\"{target}, I can't help but feel a connection between us. Would you like to go on a date and see if there's something more?\" {initiator} asks, hopeful for a positive response.",
            "\"I have a confession to make, {target}. I really like you, and I would love it if you'd go on a date with me,\" {initiator} says, a bit shy but sincere.",
            "\"I know this might be unexpected, {target}, but I would be thrilled if you would go on a date with me. What do you think?\" {initiator} asks, trying to hide their nervousness.",
            "\"Hey {target}, I've got a fun idea. How about we go on a date? I promise it'll be a great time,\" {initiator} suggests with a grin.",
            "\"{target}, I can't ignore these feelings anymore. I would like to take you on a date if you're up for it,\" {initiator} says, revealing their true emotions."
        ]
    },
    "mixer_social_GoAway_targeted_mean_alwaysOn": {
        "pre_actions": [
            "{initiator} rudely tells {target} to go away and leave them alone."
        ],
        "actions": [
            "\"{target}, I need some space right now. Can you please just go away?\" {initiator} asks, looking frustrated.",
            "\"Look, {target}, I just can't deal with this right now. I need you to leave me alone,\" {initiator} says, trying to hold back their emotions.",
            "\"{target}, I'm not in the mood for company. Would you mind giving me some time alone?\" {initiator} requests, avoiding eye contact.",
            "\"Can you just go away, {target}? I need to be by myself right now,\" {initiator} says, clearly agitated.",
            "\"{target}, I don't mean to be rude, but I really need some time alone. Can you please leave?\" {initiator} asks, attempting to sound polite.",
            "\"I can't handle this right now, {target}. I need you to go away and give me some space,\" {initiator} says, their voice strained.",
            "\"{target}, I'm really not in a good place right now. Can you please just go away and let me be?\" {initiator} asks, sounding defeated.",
            "\"Please, {target}, just leave me alone for a while. I need some time to think,\" {initiator} says, rubbing their forehead.",
            "\"{target}, I'm not trying to be mean, but I really need to be alone. Can you just go away?\" {initiator} asks, trying to sound firm.",
            "\"Look, {target}, I just can't do this right now. I need you to go away and give me some time to myself,\" {initiator} says, looking overwhelmed."
        ]
    },
    "mixer_social_DiscusssSportsStatistics_targeted_Friendly_Athlete_AlwaysOn_STC": {
        "pre_actions": [
            "{initiator} discusses sports statistics with {target}."
        ],
        "actions": [
            "\"{target}, did you know that the highest-scoring basketball game in history had a combined total of 370 points?\" {initiator} asks with enthusiasm.",
            "\"Hey {target}, I came across this interesting stat - a soccer player runs about 7 miles on average during a match. What do you think of that?\" {initiator} inquires, looking for {target}'s opinion.",
            "\"{target}, you wouldn't believe the record number of home runs hit in a single MLB season! Care to take a guess?\" {initiator} asks, playfully challenging {target}.",
            "\"Did you know, {target}, that the fastest recorded tennis serve is 163.7 mph? I wonder how that would feel if you were on the receiving end!\" {initiator} says, grinning.",
            "\"Hey {target}, remember when we were talking about football? I looked up the longest field goal ever made, and it's 64 yards! Can you imagine?\" {initiator} shares, still in awe.",
            "\"I was reading about the most successful Olympian of all time, {target}. It's Michael Phelps, with an incredible 28 medals! What do you think makes him so special?\" {initiator} asks, genuinely curious.",
            "\"Did you know, {target}, that the fastest goal in soccer history was scored in just 2.8 seconds after kickoff? How crazy is that?\" {initiator} exclaims, eager to discuss the topic.",
            "\"Hey {target}, I found out that the record for the most goals scored in an NHL season is 92! Wayne Gretzky set the record back in 1981-82. Isn't that amazing?\" {initiator} says, wanting to share the excitement.",
            "\"{target}, check this out - the highest-scoring NFL game had a combined total of 113 points. I would have loved to see that game, wouldn't you?\" {initiator} asks, reminiscing about the historic event.",
            "\"So {target}, you know I'm a huge fan of basketball, right? I just learned that the most points scored by a single player in an NBA game is 100! Wilt Chamberlain did it back in 1962. What an unbelievable achievement,\" {initiator} says, admiration in their voice."
        ]
    },
    "mixer_social_AskMoveIn_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} asks {target} to move in with them.",
        ],
        "actions": [
            "\"{target}, I've been thinking. Would you like to move in with me and take our relationship to the next level?\" {initiator} asks, hopeful.",
            "\"Hey, {target}, have you ever considered living together? It might make things easier for both of us,\" {initiator} suggests casually.",
            "\"{target}, I love spending time with you, and I think we're ready for this step. What do you say about moving in together?\" {initiator} asks with a smile.",
            "\"We've been together for a while now, {target}, and I was wondering if you'd like to move in with me. What do you think?\" {initiator} asks nervously.",
            "\"I've been doing some thinking, {target}, and I realized I want to share more of my life with you. Would you be interested in moving in with me?\" {initiator} proposes.",
            "\"Living apart just doesn't feel right anymore, {target}. Would you consider moving in together?\" {initiator} asks sincerely.",
            "\"You know, {target}, I think our relationship is strong enough to handle living together. What are your thoughts on it?\" {initiator} inquires.",
            "\"{target}, I feel like we're ready for the next step in our relationship. How would you feel about moving in together?\" {initiator} asks with anticipation.",
            "\"I can't imagine my life without you, {target}. I'd love for us to share a home together. What do you think?\" {initiator} says, looking into {target}'s eyes.",
            "\"Moving in together is a big decision, {target}, but I think we're ready for it. Are you on board with the idea?\" {initiator} asks, hoping for a positive response."
        ]
    },
    # "mixer_social_JokeAboutPoliticians_group_Funny_MediumScore": {
    #     "actions": [
    #         "\"{target}, have you heard the one about the politician who actually told the truth?\" {initiator} asks with a grin.",
    #         "\"Hey {target}, why did the politician cross the road?\" {initiator} says, chuckling in anticipation.",
    #         "\"{target}, you'll love this one. What do you call a politician who keeps their promises?\" {initiator} smirks mischievously.",
    #         "\"Here's a good one, {target}. How many politicians does it take to change a lightbulb?\" {initiator} asks, trying to suppress a laugh.",
    #         "\"Hey {target}, what do you get when you mix a politician and a scientist?\" {initiator} says, a twinkle in their eye.",
    #         "\"{target}, did you hear about the politician who accidentally told the truth during a speech?\" {initiator} begins, a smile spreading across their face.",
    #         "\"So {target}, what's the difference between a politician and a magician?\" {initiator} asks, eager to share the punchline.",
    #         "\"Ready for a laugh, {target}? What do you call a politician who can play the piano?\" {initiator} grins, anticipating {target}'s reaction.",
    #         "\"Okay {target}, I've got a great one for you. Why did the politician go to the beach?\" {initiator} asks, barely able to contain their laughter.",
    #         "\"Hey {target}, want to hear a joke? What's the difference between a politician and a flying pig?\" {initiator} smirks, waiting for {target}'s response."
    #     ]
    # },
    "mixer_social_AskToBeBoyfriend_targeted_romance_relationship": {
        "pre_actions": [
            "{initiator} asks {target} to be their boyfriend.",
        ],
        "actions": [
            "\"{target}, I've been thinking about this for a while, and I was wondering if you'd consider being my boyfriend,\" {initiator} says, trying to gauge {target}'s reaction.",
            "\"Hey, {target}, I really like you and was hoping if you'd like to be my boyfriend?\" {initiator} asks, a hint of nervousness in their voice.",
            "\"So, {target}, I've been thinking... would you be up for being my boyfriend?\" {initiator} asks, uncertainty in their eyes.",
            "\"{target}, ever since we met, I've felt a strong connection between us. Would you like to be my boyfriend?\" {initiator} says, hoping for a positive response.",
            "\"I don't want to make things weird, {target}, but I think we'd make a great couple. Would you be my boyfriend?\" {initiator} proposes cautiously.",
            "\"You know, {target}, I've been thinking about us and how well we get along. What do you think about being my boyfriend?\" {initiator} asks, trying to appear nonchalant.",
            "\"Hey, {target}, I really enjoy spending time with you, and I was wondering if you'd like to take things to the next level and be my boyfriend?\" {initiator} inquires with a hopeful smile.",
            "\"I don't want to ruin our friendship, {target}, but I can't help but wonder if you'd like to be my boyfriend,\" {initiator} says, anxiously waiting for {target}'s answer.",
            "\"{target}, we have so much fun together, and I think we'd make a great pair. Would you like to be my boyfriend?\" {initiator} suggests, holding their breath.",
            "\"Listen, {target}, I've been feeling something more than friendship between us. Would you consider being my boyfriend?\" {initiator} asks, their heart pounding."
        ]
    },
    "mixer_social_ConvinceToLeaveSpouse_targeted_romance_relationship": {
        "pre_actions": [
            "{initiator} attempts to convince {target} to leave their spouse.",
        ],
        "actions": [
            "\"{target}, I know this is difficult to hear, but I can't help but feel that you deserve so much better than your spouse. You deserve someone like me,\" {initiator} says, trying to sound convincing.",
            "\"I've been thinking about this for a long time, {target}, and I truly believe we're meant to be together. It's time you leave your spouse and start a new life with me,\" {initiator} says with determination.",
            "\"Your spouse isn't right for you, {target}. I can see it, and I know you can too. I'm the one who can make you truly happy,\" {initiator} pleads, hoping to change {target}'s mind.",
            "\"{target}, I know you're committed to your spouse, but I can't help but feel that we're a better match. Please, consider leaving them for me,\" {initiator} says, their eyes filled with hope.",
            "\"Life is too short to be unhappy, {target}. I promise you, if you leave your spouse for me, you'll never regret it,\" {initiator} says confidently.",
            "\"I'm not trying to break up your marriage, {target}, but I can't deny my feelings for you. I think we could be great together. Give us a chance,\" {initiator} implores, desperate for {target}'s understanding.",
            "\"{target}, I don't want to be the reason for your unhappiness, but I can't help but think that I could make you happier than your spouse ever could. Please, think about it,\" {initiator} says earnestly.",
            "\"I never thought I'd be the one to say this, {target}, but I can't ignore my feelings any longer. I need you to know that I think we should be together, even if it means leaving your spouse,\" {initiator} confesses, their voice wavering.",
            "\"I know you're married, {target}, but I can't help but think that you're settling for less. Imagine a life with me, and I promise you won't look back,\" {initiator} says, trying to paint a picture of a brighter future.",
            "\"Leaving your spouse won't be easy, {target}, but I promise you it'll be worth it. We could have a life filled with love and happiness if you just take that leap of faith with me,\" {initiator} says, their voice filled with passion."
        ]
    },
    "mixer_social_HipBump_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} gives {target} a friendly hip bump."
        ],
        "actions": [
            "{initiator} playfully bumps their hip into {target}, catching them off guard and eliciting a laugh.",
            "Without warning, {initiator} casually hip bumps {target}, sparking a friendly interaction between the two.",
            "{initiator} gives {target} a light hip bump, a sign of camaraderie as they share a moment together.",
            "With a mischievous grin, {initiator} sidles up to {target} and delivers a friendly hip bump, inviting a playful response.",
            "Feeling a burst of energy, {initiator} gently hip bumps {target}, hoping to brighten their day and initiate a lighthearted conversation.",
            "As {initiator} walks past {target}, they give a playful hip bump, signaling the beginning of some friendly banter.",
            "{initiator} surprises {target} with a sudden hip bump, trying to break the ice and start an amusing interaction.",
            "Looking for a fun way to engage {target}, {initiator} gently bumps hips with them, eliciting a surprised yet amused reaction.",
            "With a twinkle in their eye, {initiator} approaches {target} and playfully hip bumps them, hoping to create a lively exchange.",
            "{initiator} decides to hip bump {target} as a way to break the tension and initiate a more lighthearted conversation."
        ]
    },
    "mixer_social_Jeer_targeted_mean_middleScore": {
        "pre_actions": [
            "{initiator} makes hurtful, personal comments towards {target}."
        ], 
        "actions": [
            "\"{target}, do you really think you're capable of doing that?\" {initiator} sneers mockingly.",
            "\"Is it hard being as clueless as you, {target}?\" {initiator} taunts with a cruel grin.",
            "\"Oh, look at {target}, trying so hard but still failing miserably,\" {initiator} laughs derisively.",
            "\"Did you honestly think that was a good idea, {target}? How pathetic,\" {initiator} jeers, rolling their eyes.",
            "\"Wow, {target}, you never cease to amaze me with your incompetence,\" {initiator} snickers meanly.",
            "\"Hey {target}, do you ever get tired of being such a disappointment?\" {initiator} asks with a nasty smirk.",
            "\"Sometimes I wonder how you even manage to get through the day, {target},\" {initiator} says mockingly.",
            "\"Nice try, {target}, but you'll never be good enough,\" {initiator} sneers, enjoying their cruelty.",
            "\"I can't believe you thought that would work, {target}. You really are hopeless,\" {initiator} taunts, shaking their head in disbelief.",
            "\"Did anyone ever tell you how ridiculous you look when you try, {target}?\" {initiator} asks with a mean laugh."
        ]
    },
    "mixer_social_Intimidate_targeted_mean_middleScore": {
        "pre_actions": [
            "{initiator} attempts to intimidate {target}."
        ],
        "actions": [
            "\"{target}, do you really think you can stand up to me?\" {initiator} says, smirking and crossing their arms.",
            "{initiator} leans in closer to {target}, their eyes narrowing. \"You should be careful who you mess with,\" they warn.",
            "\"I hope you're aware of what you're getting yourself into, {target},\" {initiator} says, their voice cold and menacing.",
            "{initiator} towers over {target}, staring them down. \"You might want to reconsider your actions, buddy,\" they suggest darkly.",
            "\"You have no idea who you're dealing with, {target},\" {initiator} says, their tone dripping with venom.",
            "\"Do you really want to test me, {target}?\" {initiator} asks, raising an eyebrow and cracking their knuckles.",
            "\"Be careful, {target}. I have a way of making problems... disappear,\" {initiator} says ominously.",
            "{initiator} leans in and whispers menacingly in {target}'s ear, \"You don't want to see me angry.\"",
            "{initiator} fixes {target} with a cold stare. \"You should know better than to challenge me,\" they say icily.",
            "\"Keep pushing me, {target}, and you'll see what happens,\" {initiator} warns, their voice low and dangerous."
        ]
    },
    "mixer_social_KissHands_targeted_romance_emotionSpecific": {
        "pre_actions": [
            "{initiator} kisses {target}'s hands romantically."
        ],
        "actions": [
            "{initiator} leans in slowly and gently places a tender kiss on {target}'s hand, conveying their admiration.",
            "Without a word, {initiator} takes {target}'s hand and softly kisses it, locking their eyes together.",
            "Feeling a sudden rush of affection, {initiator} gently lifts {target}'s hand and presses a warm kiss upon it.",
            "In a moment of pure emotion, {initiator} tenderly kisses {target}'s hand, expressing their deep connection.",
            "{initiator} takes {target}'s hand in theirs, their eyes meeting as they gently press their lips to {target}'s hand.",
            "With a gaze full of tenderness, {initiator} brings {target}'s hand to their lips and plants a gentle kiss.",
            "In a spontaneous gesture, {initiator} reaches for {target}'s hand and lovingly kisses it, causing {target} to blush.",
            "As {initiator} grasps {target}'s hand, they gently place a kiss on it, their eyes never leaving {target}'s face.",
            "Moved by the moment, {initiator} softly takes {target}'s hand and plants a sweet kiss upon it, conveying their feelings.",
            "With a meaningful look, {initiator} delicately kisses {target}'s hand, displaying their deep affection and admiration."
        ]
    },
    "mixer_social_InsultFace_targeted_mean_emotionSpecific": {
        "pre_actions": [
            "{initiator} cruelly insults {target}'s face."
        ],
        "actions": [
            "\"{target}, has anyone ever told you that your face looks like someone tried to solve a Rubik's Cube but gave up halfway?\" {initiator} smirks.",
            "\"Wow, {target}, it must be hard to look in the mirror every day with a face like that,\" {initiator} says mockingly.",
            "\"{target}, I don't know whether to laugh or cry at the sight of your face,\" {initiator} says, barely able to contain their laughter.",
            "\"I've seen some interesting faces in my time, {target}, but yours is truly one for the books,\" {initiator} teases.",
            "\"Hey {target}, did you lose a fight with a makeup brush or is that just your face?\" {initiator} asks sarcastically.",
            "\"{target}, I didn't know 'before' pictures could walk and talk,\" {initiator} says with a chuckle.",
            "\"Is your face a work in progress, {target}? Or is that the final result?\" {initiator} questions, a mischievous grin on their face.",
            "\"{target}, I'm not sure if you're aware, but it looks like your face has been in a battle with itself,\" {initiator} says, trying to hold back a grin.",
            "\"Your face, {target}, must be the reason why some people believe in extraterrestrial life,\" {initiator} jokes.",
            "\"I've heard of unique beauty, {target}, but your face is really pushing the limits,\" {initiator} says with a hint of amusement."
        ]
    },
    "mixer_social_Kiss_targeted_romance_middleScore": {
        "pre_actions": [
            "{initiator} kisses {target}'s hands romantically."
        ],
        "actions": [
            "{initiator} leans in close, their eyes meeting {target}'s before softly pressing their lips together in a tender kiss.",
            "Without warning, {initiator} gently grabs {target}'s face and plants a passionate kiss on their lips, catching them by surprise.",
            "As the conversation between {initiator} and {target} fades, their faces inch closer, finally sharing a long-awaited kiss.",
            "{initiator} hesitates for a moment before closing the gap between them, placing a sweet, lingering kiss on {target}'s lips.",
            "With a mixture of courage and desire, {initiator} takes {target}'s hand, leans in, and shares a breathtaking kiss.",
            "Unable to resist any longer, {initiator} pulls {target} close and captures their lips in a passionate embrace.",
            "During a moment of quiet intimacy, {initiator} slowly leans in and brushes their lips against {target}'s, igniting a spark between them.",
            "As they gaze into each other's eyes, {initiator} gently cups {target}'s face and presses their lips together in a tender, loving kiss.",
            "Feeling a surge of emotion, {initiator} leans in and kisses {target} with a passion that takes both of them by surprise.",
            "Captivated by the moment, {initiator} closes the distance between them and seals their connection with a sweet, heartfelt kiss."
        ]
    },
    "mixer_social_Insult_Mean_STC": {
        "actions": [
            "\"{target}, I've always wondered how you manage to be so consistently clueless,\" {initiator} says with a mocking tone.",
            "\"Hey {target}, did you get dressed in the dark today? Because that outfit is just... wow,\" {initiator} smirks, looking {target} up and down.",
            "{initiator} rolls their eyes at {target} and says, \"You really are a special kind of stupid, aren't you?\"",
            "\"Wow, {target}, your inability to understand even the simplest things never ceases to amaze me,\" {initiator} says with a sarcastic laugh.",
            "\"Did it hurt when you fell from heaven, {target}? Because you must have landed on your head to be so dense,\" {initiator} snickers.",
            "\"{target}, I would insult your intelligence, but I'm afraid you wouldn't understand,\" {initiator} says with a condescending smile.",
            "{initiator} shakes their head and says, \"Honestly, {target}, every time you speak, it's like a fresh reminder of why I avoid talking to you.\"",
            "\"You know, {target}, it's really impressive how you can make everything you do look so incredibly difficult,\" {initiator} teases.",
            "\"{target}, if you were any less competent, you'd be a houseplant,\" {initiator} says, rolling their eyes.",
            "\"Sometimes I wonder if you're actually trying to be this annoying, {target}, or if it just comes naturally to you,\" {initiator} says with an exasperated sigh."
        ]
    },
    "mixer_social_ShareInsecurities_targeted_friendly_emotionSpecific": {
        "actions": [
            "\"{target}, I've been feeling really insecure lately, and I was hoping I could talk to you about it,\" {initiator} says with a shaky voice.",
            "\"I don't usually open up about this, but something tells me that I can trust you with my insecurities,\" {initiator} admits, looking into {target}'s eyes.",
            "\"Can I share something personal with you, {target}? I've been struggling with my insecurities, and I think I need some support,\" {initiator} says, hesitatingly.",
            "\"{target}, I need your help. I've been feeling really down about myself lately, and I don't know who else to turn to,\" {initiator} confesses, their voice trembling.",
            "\"I've never been good at admitting my weaknesses, but I think it's time I tell you about my insecurities, {target},\" {initiator} says, taking a deep breath.",
            "\"There's something I've been keeping inside, {target}, and I think it's time I share it with you. I've been feeling really insecure,\" {initiator} says, looking anxious.",
            "\"I don't know how to say this, {target}, but I've been feeling so insecure lately. Can we talk about it?\" {initiator} admits, looking vulnerable.",
            "\"I've never told anyone this, {target}, but my insecurities have been getting the best of me. Will you listen?\" {initiator} asks cautiously.",
            "\"Sometimes I feel like I'm not good enough, {target}, and I think I need to talk about my insecurities with someone I trust. Can that be you?\" {initiator} says, preparing to share something personal.",
            "\"{target}, I've been struggling with my insecurities for a while now, and I think it's time I open up to you about it,\" {initiator} says with a mixture of relief and apprehension."
        ]
    },
    "mixer_social_ReciteLovePoetry_targeted_romance_emotionSpecific": {
        "actions": [
            "\"{target}, I found a poem today that made me think of you. May I share it with you?\" {initiator} asks, holding a worn book in their hands.",
            "\"With your beauty in mind, {target}, I was inspired to write a few verses of love poetry. Would you like to hear them?\" {initiator} inquires, shyly looking at {target}.",
            "\"Listen closely, {target}, for these words of love I've penned are meant for you and only you,\" {initiator} says as they recite lines of poetry from memory.",
            "\"Can I share something with you, {target}? I stumbled upon a poem that captures my feelings for you better than I ever could,\" {initiator} says, blushing slightly.",
            "\"{target}, I wrote a poem about you, and I'd be honored if you'd allow me to recite it for you,\" {initiator} says, filled with both excitement and anxiety.",
            "\"I found a piece of poetry that speaks to my heart and reminds me of you, {target}. Would you care to listen?\" {initiator} asks gently.",
            "\"Last night, I was inspired to write some verses dedicated to you, {target}. I hope you'll find them as beautiful as I find you,\" {initiator} says, holding a folded piece of paper.",
            "\"Words alone cannot express my feelings for you, {target}, but I hope this poem I wrote comes close,\" {initiator} says, taking a deep breath before reciting their heartfelt words.",
            "\"Tonight, under this starry sky, I want to share a special poem with you, {target}. I hope it makes you feel as cherished as you are to me,\" {initiator} says, a hint of nervousness in their voice.",
            "\"{target}, I came across a poem that I believe perfectly captures the essence of my love for you. May I share it?\" {initiator} asks, eyes filled with hope and adoration."
        ]
    },
    "mixer_social_Serenade_targeted_romance_emotionSpecific": {
        "actions": [
            "\"{target}, I've been working on this song just for you. I hope it captures how I truly feel about you,\" {initiator} says with a shy smile before beginning to sing.",
            "\"I've never done this before, but I feel like serenading you, {target}, because you mean the world to me,\" {initiator} says, taking a deep breath and starting to sing.",
            "\"{target}, I've written a song that I believe truly captures my feelings for you. I hope you'll let me serenade you,\" {initiator} says nervously while holding a guitar.",
            "\"Close your eyes, {target}, and let me express my love for you in the best way I know how,\" {initiator} says, before singing a heartfelt romantic song.",
            "\"{target}, I've been practicing this song, hoping it would touch your heart. Please, let me sing it for you,\" {initiator} says as they start to serenade {target}.",
            "\"I want to do something special for you, {target}, something that can show you my true feelings. Let me serenade you,\" {initiator} says, looking into {target}'s eyes.",
            "\"I've never been good with words, but I can express my feelings through music. {target}, let me serenade you,\" {initiator} says, gathering their courage.",
            "\"{target}, I want to show you my love in a different way. I hope you'll enjoy this serenade,\" {initiator} says, taking a deep breath before singing.",
            "\"Tonight, under this moonlit sky, I want to express my love for you in a unique way, {target}. Allow me to serenade you,\" {initiator} says, their voice full of emotion.",
            "\"I can't keep my feelings to myself any longer, {target}. I need to share them with you, and I hope this serenade will do just that,\" {initiator} says, before singing from the heart."
        ]
    },
    "mixer_social_ShareBartendingSecrets_targeted_Friendly_alwaysOn_skills": {
        "actions": [
            "\"{target}, I've been working behind the bar for years, and I've picked up some secret tricks. Want to learn a few?\" {initiator} asks with a sly grin.",
            "\"Hey {target}, you ever wonder how I make those amazing cocktails? I think it's time I let you in on a few of my secrets,\" {initiator} says, winking.",
            "\"Alright, {target}, I've seen your interest in bartending. Let me share some of my closely guarded secrets with you,\" {initiator} offers, looking excited.",
            "\"I never thought I would teach anyone this, but I think you're ready, {target}. Let me show you some of the secrets I've learned as a bartender,\" {initiator} says, rolling up their sleeves.",
            "\"Okay {target}, it's time for me to pass on some of my bartending wisdom. Pay close attention; these are secrets I've never shared before,\" {initiator} says, preparing to divulge their knowledge.",
            "\"{target}, you've earned my trust, and I think it's time I share some of my most prized bartending secrets with you. Are you ready?\" {initiator} asks, raising an eyebrow.",
            "\"There's more to bartending than meets the eye, {target}. Let me show you some secret techniques I've picked up along the way,\" {initiator} says, motioning for {target} to come closer.",
            "\"I see potential in you, {target}. I'm going to share some of my secret bartending skills with you, so pay attention,\" {initiator} says, looking serious.",
            "\"Ever wondered what sets my drinks apart from the rest, {target}? I'll let you in on my little secrets, but you have to promise not to tell,\" {initiator} says, conspiratorially.",
            "\"Alright, {target}, I've decided it's time to teach you some of the hidden tricks of the trade. Get ready to become a master bartender,\" {initiator} says, a gleam in their eye."
        ]
    },
    "mixer_social_OfferRose_targeted_romance_emotionSpeficic": {
        "pre_actions": [
            "{initiator} offers a rose to {target}, as a romantic gesture.",
        ],
        "actions": [
            "\"{target}, I couldn't help but think of you when I saw this rose. Its beauty pales in comparison to yours,\" {initiator} says, offering the rose with a gentle smile.",
            "\"Here's a small token of my affection, {target}. I hope this rose brightens your day as much as you brighten mine,\" {initiator} says with a warm expression.",
            "\"Every time I see a rose, I think of you, {target}. I hope you'll accept this as a symbol of my feelings,\" {initiator} says, holding out the rose with a hopeful gaze.",
            "\"{target}, I've been wanting to express my feelings for you, and I think this rose says it all. Will you accept it?\" {initiator} asks, presenting the rose tenderly.",
            "\"As we've grown closer, I've realized how much you mean to me, {target}. This rose is just a small way to show you my feelings,\" {initiator} says, extending the rose with a loving smile.",
            "\"I know it's a little old-fashioned, but I wanted to give you this rose, {target}. It's a symbol of the love that's blooming between us,\" {initiator} says with a bashful grin.",
            "\"Words often fail me when I try to express my feelings, {target}. So, let this rose speak for me instead,\" {initiator} says, offering the rose with a heartfelt expression.",
            "\"{target}, you've brought so much joy into my life. I can only hope this rose brings a fraction of that happiness to you,\" {initiator} says, presenting the rose with a sincere smile.",
            "\"I've been searching for a way to show you how much you mean to me, {target}. I hope this rose is the perfect expression of my love,\" {initiator} says, holding the rose out with a gentle touch.",
            "\"Roses have always been a symbol of love, and I can't think of a better way to express my feelings for you, {target}. Will you accept this rose and my heart?\" {initiator} asks, gazing into {target}'s eyes."
        ]
    },
    "mixer_social_Romance_HighScore_Loyal_ExpressDevotion": {
        "actions": [
            "\"{target}, I don't know how else to say this, but I've fallen in love with you,\" {initiator} says, their voice filled with emotion.",
            "\"I can't hide it any longer, {target}. My heart belongs to you, and I can't imagine my life without you,\" {initiator} confesses, their eyes shining with sincerity.",
            "\"{target}, I've tried to deny it, but the truth is, I'm head over heels in love with you,\" {initiator} says, looking into {target}'s eyes with hope.",
            "\"I've never felt this way about anyone, {target}. I love you more than words can describe,\" {initiator} admits, their heart pounding.",
            "\"Every time I see you, {target}, my heart skips a beat. I can't help but be utterly and completely devoted to you,\" {initiator} says, a vulnerable look in their eyes.",
            "\"I've been trying to find the courage to tell you this, {target}, but I'm in love with you. Completely and irrevocably,\" {initiator} says, reaching for {target}'s hand.",
            "\"My heart belongs to you, {target}, and I can't bear to keep it a secret any longer. I love you,\" {initiator} declares, their voice filled with passion.",
            "\"There's no point in pretending anymore, {target}. I am deeply and truly in love with you,\" {initiator} says, their eyes pleading for understanding.",
            "\"I've never been more certain about anything in my life, {target}. I am devoted to you, heart and soul,\" {initiator} confesses, their voice barely above a whisper.",
            "\"I don't know when it happened, {target}, but somewhere along the way, I fell in love with you. I can't imagine my life without your presence,\" {initiator} says, their vulnerability shining through."
        ]
    },
    "mixer_social_KissCheek_targeted_romance_alwaysOn": {
        "pre_actions": [
            "{initiator} tenderly kisses {target}'s cheek.",
        ],
        "actions": [
            "{initiator} leans in closer to {target}, their eyes meeting for a brief moment before gently pressing their lips to {target}'s cheek.",
            "Without a word, {initiator} reaches up and tenderly places a soft kiss on {target}'s cheek, causing a blush to spread across their face.",
            "Feeling a sudden surge of affection, {initiator} gently cups {target}'s face and plants a sweet kiss on their cheek.",
            "{initiator} smiles warmly at {target} before suddenly leaning in and placing a light kiss on their cheek, catching them off guard.",
            "With a playful grin, {initiator} leans in and brushes their lips against {target}'s cheek, leaving a lingering sensation.",
            "{initiator} takes {target}'s hand, looks into their eyes, and then gently kisses their cheek, making {target}'s heart race.",
            "Caught up in the moment, {initiator} impulsively leans forward and leaves a light, affectionate kiss on {target}'s cheek.",
            "{initiator} suddenly leans in and surprises {target} with a quick peck on the cheek."
        ]
    },
    "mixer_social_ShareConspiracyTheory_targeted_mischief_alwaysOn": {
        "pre_actions": [
            "{initiator} shares a conspiracy theory with {target}."
        ],
        "actions": [
            "\"{target}, have you ever heard of this conspiracy theory? I came across it recently, and I just can't stop thinking about it,\" {initiator} says, excitedly.",
            "\"{target}, I know this might sound crazy, but I stumbled upon a conspiracy theory that actually makes a lot of sense. Can I share it with you?\" {initiator} asks, looking eager.",
            "\"Okay, {target}, you might think I'm going off the deep end here, but I've got a conspiracy theory that's too intriguing not to share. Are you ready for it?\" {initiator} grins, leaning in closer.",
            "\"I never thought I'd be one to buy into conspiracy theories, {target}, but I found one that's strangely compelling. Can I get your thoughts on it?\" {initiator} asks nervously.",
            "\"Hey, {target}, I know you're into some wild theories, so I thought I'd run this conspiracy theory by you. What do you think?\" {initiator} says, trying to gauge {target}'s interest.",
            "\"So, {target}, I came across this bizarre conspiracy theory, and I can't tell if it's just nonsense or if there's some truth to it. Can I share it with you?\" {initiator} asks, looking for validation.",
            "\"Alright, {target}, I know you'll appreciate this one. I've found a conspiracy theory that's just too wild not to share. Are you ready?\" {initiator} says, barely containing their excitement.",
            "\"Listen, {target}, I found this conspiracy theory that's completely out of left field, but I can't help but think there might be something to it. Can I tell you about it?\" {initiator} inquires, seeking an open-minded listener.",
            "\"You know, {target}, I've never been one for conspiracy theories, but there's one that's been nagging at me. Mind if I share it with you and get your take on it?\" {initiator} asks, hoping for a receptive ear.",
            "\"I need your critical thinking skills, {target}. I've been reading about this conspiracy theory, and I can't decide if it's absurd or plausible. Can I run it by you?\" {initiator} says, valuing {target}'s opinion."
        ]
    },
    "mixer_social_InsultCostume_targeted_mean_alwaysOn_situation_Day1DLC": {
        "pre_actions": [
            "{initiator} harshly insults {target}'s costume.",
        ],
        "actions": [
            "\"{target}, I don't mean to be rude, but that costume looks like something a kindergartner made,\" {initiator} says, trying to suppress a laugh.",
            "\"Wow, {target}, did you put that costume together in the dark?\" {initiator} asks sarcastically.",
            "\"Is that supposed to be a costume, {target}? I've seen more effort put into a last-minute Halloween outfit,\" {initiator} scoffs.",
            "\"{target}, who told you that costume was a good idea? They must have a twisted sense of humor,\" {initiator} comments with a smirk.",
            "\"I didn't know we were going for 'worst costume' award, {target}. You're definitely in the running,\" {initiator} says with a snicker.",
            "\"Are you seriously wearing that, {target}? I thought you had better taste in costumes,\" {initiator} says, rolling their eyes.",
            "\"Hey, {target}, your costume might just win the 'ugliest outfit' contest if there was one,\" {initiator} jokes, laughing at their own remark.",
            "\"{target}, I think you should demand a refund for that costume. It's not doing you any favors,\" {initiator} says with a grin.",
            "\"Did you lose a bet or something, {target}? That costume is just... Wow, I'm speechless,\" {initiator} says, shaking their head in disbelief.",
            "\"I hope you didn't spend too much time on that costume, {target}. It looks like a DIY disaster,\" {initiator} says, trying to hold back their laughter."
        ]
    },
    "mixer_social_JokeAboutPenguins_targeted_Friendly_alwaysOn_situation_Day1DLC": {
        "pre_actions": [
            "{initiator} tells {target} a joke about penguins."
        ],
        "actions": [
            "\"{target}, did you hear about the penguin who wanted to be friends? He just needed someone to break the ice!\" {initiator} chuckles.",
            "{initiator} asks {target}, \"Why don't you ever see penguins in the UK? Because they're afraid of Wales!\"",
            "\"Hey {target}, what do penguins wear on their heads? Ice caps!\" {initiator} laughs, trying to lighten the mood.",
            "{initiator} grins at {target} and asks, \"Why don't penguins like talking to strangers at parties? They find it hard to break the ice!\"",
            "{initiator} smirks at {target} and says, \"Do you know what a penguin's favorite relative is? Aunt Arctica!\"",
            "\"Hey {target}, why are penguins such good race car drivers? Because they're always in the pole position!\" {initiator} jokes, hoping to make {target} laugh.",
            "{initiator} asks {target} with a grin, \"What's a penguin's favorite movie? Frozen!\"",
            "\"Did you hear about the penguin who went to the beach, {target}? He wore a beak-ini!\" {initiator} giggles at their own joke.",
            "\"Hey {target}, do you know what a penguin's favorite snack is? Ice Krispies!\" {initiator} shares, hoping to bring a smile to {target}'s face.",
            "{initiator} looks at {target} and says, \"What do you call a penguin in the desert? Lost!\" hoping to get a laugh."
        ]
    },
    "mixer_social_DiscussTheBestViolinist_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} begins a debate with {target} regarding who is the best violin player in the world."
        ],
        "actions": [
            "\"{target}, have you ever wondered who the best violinist in the world might be?\" {initiator} asks, striking up a conversation about music.",
            "\"I was listening to some violin music earlier, {target}, and it got me thinking - who do you believe is the most talented violinist out there?\" {initiator} inquires with curiosity.",
            "\"Hey {target}, I've been debating with a friend about the best violinist of all time. What's your take on that?\" {initiator} asks, seeking {target}'s opinion.",
            "\"{target}, I've always admired your taste in music. In your opinion, who is the greatest violinist ever?\" {initiator} asks, genuinely interested in {target}'s perspective.",
            "\"I came across a fascinating article about the greatest violinists, {target}. It made me wonder, who do you think deserves that title?\" {initiator} questions, sparking a discussion.",
            "\"Did you know, {target}, that there's a lot of debate about who the best violinist is? I'm curious, who's your personal favorite?\" {initiator} asks, eager to know {target}'s preference.",
            "\"{target}, I've been exploring different violinists lately, and I can't decide who is the best. Do you have any recommendations?\" {initiator} asks, hoping for some guidance.",
            "\"You know, {target}, there are so many amazing violinists out there. If you had to choose one as the best, who would it be?\" {initiator} wonders, encouraging a friendly debate.",
            "\"Have you ever seen a live violin performance, {target}? I'd love to know who you think is the most impressive violinist,\" {initiator} asks enthusiastically.",
            "\"{target}, I've been trying to expand my music collection with some incredible violinists. Who do you consider the best in the field?\" {initiator} questions, eager to discover new talent."
        ]
    },
    "mixer_social_ShareBurden_targeted_Friendly_alwaysOn_trait": {
        "pre_actions": [
            "{initiator} confides in {target} and shares their emotional burden with them."
        ],
        "actions": [
            "\"{target}, I've been struggling with something my whole life, and I think it's time I share it with you,\" {initiator} says, weariness in their eyes.",
            "\"I've been carrying this burden for so long, and I need someone to understand. Can you lend me a sympathetic ear, {target}?\" {initiator} asks hesitantly.",
            "\"{target}, there's something that's been weighing me down for years, and I just can't keep it to myself anymore. I need your support,\" {initiator} says, looking vulnerable.",
            "\"I've never told anyone about this, {target}, but I trust you. I need to share the load that's been haunting me my entire life,\" {initiator} says, taking a shaky breath.",
            "\"{target}, I've been hiding this pain for as long as I can remember, and I think it's time I open up to you about it,\" {initiator} says, voice trembling with emotion.",
            "\"There's something I've been dealing with my whole life, {target}, and I think you're the only one who can truly understand,\" {initiator} says, searching {target}'s eyes for reassurance.",
            "\"I need to get this off my chest, {target}, and I hope you can help me. I've been struggling with this burden for as long as I can remember,\" {initiator} says, eyes welling up with tears.",
            "\"{target}, I've been hiding a life-long struggle, and I think it's time to share it with you. I trust your wisdom and empathy,\" {initiator} says, seeking solace in {target}'s presence.",
            "\"I never thought I'd open up about this, {target}, but I can't keep pretending it doesn't affect me. I need to tell you about the burden I've carried for years,\" {initiator} says, voice barely audible.",
            "\"{target}, I feel like I've known you long enough to share something deeply personal with you. I hope you can help me carry the weight of this burden,\" {initiator} says, looking into {target}'s eyes with hope."
        ]
    },
    "mixer_social_SuaveKiss_targeted_romance_emotionSpecific": {
        "pre_actions": [
            "{initiator} gives {target} a suave, romantic kiss."
        ],
        "actions": [
            "{initiator} leans in and gently presses their lips against {target}'s, creating a moment of passion and tenderness.",
            "With a charming smile, {initiator} takes {target}'s hand, pulls them closer, and plants a suave kiss on their lips.",
            "{initiator} looks deep into {target}'s eyes, brushing their hair back before delivering a smooth, intoxicating kiss.",
            "Capturing the perfect moment, {initiator} leans in and sweeps {target} off their feet with a suave, unforgettable kiss.",
            "{initiator} cups {target}'s face, their fingers lightly tracing the outline of their jaw before sealing the moment with a stylish kiss.",
            "Under the moonlit sky, {initiator} pulls {target} close and shares a suave, dreamlike kiss, taking their breath away.",
            "With a mischievous glint in their eye, {initiator} places a finger under {target}'s chin, lifting their gaze before delivering a charming, suave kiss.",
            "In a bold move, {initiator} grabs {target}'s waist, pulling them closer and surprising them with a debonair, sensual kiss.",
            "{initiator} gently touches {target}'s cheek, letting their eyes lock for a moment before leaning in for a smooth, enchanting kiss.",
            "As their eyes meet, {initiator} wraps an arm around {target}'s waist and pulls them in for a suave, heart-stopping kiss."
        ]
    },
    "mixer_social_RileUp_targeted_mean_alwaysOn": {
        "pre_actions": [
            "{initiator} intentionally agitates {target}."
        ],
        "actions": [
            "\"{target}, I've always wondered how someone like you can be so clueless,\" {initiator} says, smirking maliciously.",
            "\"{target}, has anyone ever told you how infuriatingly slow you are?\" {initiator} asks with a sly grin.",
            "\"It's amazing how you manage to get through life with so little common sense, {target},\" {initiator} snickers.",
            "\"Hey {target}, did you have to work hard to become this annoying, or does it just come naturally?\" {initiator} teases cruelly.",
            "\"{target}, if there was a contest for being the most irritating person, I'm pretty sure you'd win,\" {initiator} scoffs.",
            "\"I wonder how you manage to make even the simplest tasks look so difficult, {target},\" {initiator} says with a mocking grin.",
            "\"Whenever I need a good laugh, I just think about how you bumble through life, {target},\" {initiator} chuckles rudely.",
            "\"{target}, I've met rocks with more personality than you. How do you do it?\" {initiator} taunts.",
            "\"Is it tiring being so incompetent, {target}? Or have you gotten used to it by now?\" {initiator} asks, sneering.",
            "\"I'm not sure whether to pity you or be impressed by your ability to fail so consistently, {target},\" {initiator} says, laughing meanly."
        ]
    },
    "mixer_social_WhisperSeductively_targeted_romance_middleScore": {
        "pre_actions": [
            "{initiator} whispers seductively to {target}."
        ],
        "actions": [
            "\"{target}, can I tell you a secret?\" {initiator} whispers seductively, a playful glint in their eye.",
            "\"Lean in closer, {target}, I have something enticing to share,\" {initiator} murmurs, their breath warm on {target}'s ear.",
            "\"{target}, I can't resist the urge to whisper something alluring in your ear,\" {initiator} says, their voice soft and sultry.",
            "\"I've been thinking about something quite... sinful, {target}. Would you like to know what it is?\" {initiator} teases, their lips brushing against {target}'s earlobe.",
            "\"Let me share a deliciously tempting secret with you, {target},\" {initiator} purrs, their voice low and seductive.",
            "\"There's a thought that's been driving me wild, {target}. Are you curious to know what it is?\" {initiator} whispers, their voice dripping with desire.",
            "\"You know, {target}, there's something I've been fantasizing about. Can I share it with you?\" {initiator} asks, their voice laced with seduction.",
            "\"{target}, I can't help but let my mind wander to some very... enticing places. Would you like a glimpse?\" {initiator} whispers, a devilish grin on their face.",
            "\"I have a confession to make, {target}. My thoughts have been a bit... naughty lately,\" {initiator} admits, their voice sultry and inviting.",
            "\"Come closer, {target}, and let me share a secret that's both thrilling and enticing,\" {initiator} murmurs, their voice filled with allure."
        ]
    },
    "mixer_social_YellAT_targeted_mean": {
        "pre_actions": [
            "{initiator} yells at {target} in anger."
        ],
        "actions": [
            "\"{target}, you're absolutely infuriating! Can't you do anything right?\" {initiator} yells, anger in their voice.",
            "\"Are you really this incompetent, {target}? I can't believe I have to put up with your stupidity!\" {initiator} shouts, losing their patience.",
            "\"{target}, I've had enough of your nonsense! Get your act together or just get out of my sight!\" {initiator} exclaims, frustration evident in their tone.",
            "\"I can't stand you anymore, {target}! Your constant mistakes are driving me insane!\" {initiator} yells, unable to control their anger.",
            "\"{target}, you're so careless! How can someone be as clueless as you?\" {initiator} shouts, feeling overwhelmed by their frustration.",
            "\"Sometimes I wonder if you're really this dumb, {target}, or if you're just pretending to be!\" {initiator} yells, feeling exasperated.",
            "\"{target}, I don't know how much more of your incompetence I can take! You're pushing me to my limits!\" {initiator} shouts, their voice filled with irritation.",
            "\"Can you just think for once, {target}? I'm tired of dealing with the mess you constantly create!\" {initiator} yells, feeling fed up.",
            "\"{target}, you never cease to amaze me with your foolishness! How hard is it for you to understand simple instructions?\" {initiator} shouts, their voice laced with annoyance.",
            "\"I'm at my wit's end, {target}! I can't take your stupidity any longer!\" {initiator} yells, their anger finally boiling over."
        ]
    },
    "mixer_social_MakeFunOfNoobs_targeted_funny_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} makes fun of noobs in the online game they're playing with {target}."
        ], 
        "actions": [
            "\"{target}, have you seen these new players trying to learn the game? It's hilarious,\" {initiator} laughs, watching their screens.",
            "\"Hey {target}, check this out. This noob is struggling to even find the start button!\" {initiator} jokes, pointing at the screen.",
            "\"{target}, I swear, watching these newbies try to navigate the game is like watching a baby trying to walk,\" {initiator} chuckles.",
            "\"You know what's funny, {target}? The fact that these noobs think they can beat us in the game. Good luck with that!\" {initiator} smirks.",
            "\"I can't stop laughing, {target}. These new players are so lost. They're like deer caught in headlights,\" {initiator} says with a grin.",
            "\"Remember when we were noobs like them, {target}? I bet we weren't this bad though!\" {initiator} teases.",
            "\"{target}, do you think we should help these new players or just sit back and enjoy the show?\" {initiator} asks, laughing at their struggles.",
            "\"Man, {target}, it's so entertaining to watch these rookies fumble around. It's like they've never played a video game before,\" {initiator} comments.",
            "\"Sometimes, {target}, I wonder if these new players are just pretending to be bad for our amusement,\" {initiator} says, chuckling at their gameplay.",
            "\"Isn't it amazing, {target}, how we've come so far in our gaming skills while these poor noobs are still trying to figure out the controls?\" {initiator} laughs."
        ]
    },
    "mixer_socials_EnthuseAboutExperimentalFood_Targeted_Friendly_AlwaysOn_DiningSocials": {
        "pre_actions": [
            "{initiator} enthuses about experimental food with their friend, {target}."
        ],
        "actions": [
            "\"{target}, you have to try this! It's unlike anything I've ever tasted before,\" {initiator} says excitedly, taking another bite.",
            "\"Wow, this experimental dish is amazing! Don't you think so, {target}?\" {initiator} asks, grinning from ear to ear.",
            "\"I never thought I'd like something so unconventional, but this food is delicious! You should give it a go, {target}!\" {initiator} exclaims, offering a bite.",
            "\"Isn't it fascinating how they've combined these flavors, {target}? I can't get enough of it!\" {initiator} enthuses, digging into their meal.",
            "\"Who would have thought that these ingredients could work so well together? You need to taste this, {target}!\" {initiator} says, eyes sparkling with excitement.",
            "\"Have you ever tried anything like this, {target}? It's so unique and delicious! I'm in love with this dish!\" {initiator} gushes, savoring each bite.",
            "\"I can't believe how amazing this experimental food is, {target}. You really need to try it!\" {initiator} insists, gesturing towards their plate.",
            "\"Isn't this dish just incredible, {target}? I've never experienced flavors like these before!\" {initiator} declares, thoroughly enjoying their meal.",
            "\"I have to admit, I was skeptical at first, but this experimental food has won me over. You should give it a try, {target}!\" {initiator} suggests enthusiastically.",
            "\"Can you believe how tasty this is, {target}? It's so unconventional, yet absolutely delicious!\" {initiator} exclaims, eager for {target} to share the experience."
        ]
    },
    "mixer_social_ProfessUndyingLove_targeted_romance_highScore": {
        "pre_actions": [
            "{initiator} professes their undying love for {target}."
        ],
        "actions": [
            "\"{target}, I need to tell you something important. My love for you is undying, and I can't keep it to myself any longer,\" {initiator} says, their heart pounding.",
            "\"I've been holding this in for too long, {target}. I am completely and utterly in love with you,\" {initiator} confesses, looking deeply into {target}'s eyes.",
            "\"There's something I've been meaning to say, {target}. My love for you knows no bounds, and I can't keep it a secret any longer,\" {initiator} says, their voice filled with emotion.",
            "\"{target}, I can't hold it in any longer. I love you more than words can express, and I want you to know that,\" {initiator} says, their voice trembling with sincerity.",
            "\"I've tried to deny it, but I can't anymore, {target}. I love you, and I will always love you,\" {initiator} says, their eyes filled with a mix of hope and fear.",
            "\"My heart has been aching to tell you this, {target}. I am deeply and irrevocably in love with you,\" {initiator} confesses, their voice barely audible.",
            "\"I never thought I could feel this way about someone, {target}, but I am head over heels in love with you,\" {initiator} admits, their eyes searching {target}'s for a reaction.",
            "\"I've been hiding my feelings for far too long, {target}. I love you more than anything in this world, and I need you to know that,\" {initiator} says, their voice shaking with vulnerability.",
            "\"{target}, I've tried to ignore these feelings, but I can't any longer. I am completely, undeniably in love with you,\" {initiator} says, their voice full of sincerity and love.",
            "\"I've been keeping this secret for what feels like an eternity, {target}, but I have to tell you. I am madly, truly, and deeply in love with you,\" {initiator} says, their eyes shining with emotion."
        ]
    },
    "mixer_social_MockMusicTaste_targeted_mean_trait": {
        "pre_actions": [
            "{initiator} mocks {target}'s musical tastes, in order to hurt their feelings."
        ],
        "actions": [
            "\"{target}, I can't believe you actually enjoy listening to that noise. What do you even see in it?\" {initiator} teases with a grin.",
            "\"Really, {target}? That's the kind of music you're into? I thought you had better taste than that,\" {initiator} says, smirking.",
            "\"Wow, {target}, I didn't know anyone still listened to that kind of music. I guess you're just full of surprises,\" {initiator} laughs mockingly.",
            "\"Seriously, {target}? That band you like is just...terrible. I don't know how you can stand listening to them,\" {initiator} says, rolling their eyes.",
            "\"I have to say, {target}, your taste in music leaves a lot to be desired. I mean, really?\" {initiator} says, chuckling condescendingly.",
            "\"{target}, I didn't realize your music preferences were so...unique. I guess I can't help but laugh,\" {initiator} says sarcastically.",
            "\"Please tell me you're joking, {target}. You can't actually enjoy listening to that, can you?\" {initiator} asks, stifling their laughter.",
            "\"Yikes, {target}, your favorite band is like nails on a chalkboard to me. How do you even tolerate that sound?\" {initiator} says, cringing.",
            "\"Oh, {target}, your music taste is...interesting, to say the least. But I guess everyone has their guilty pleasures,\" {initiator} says with a snicker.",
            "\"Whenever I think I know you, {target}, you reveal a new layer of weirdness. I never would've pegged you for a fan of that music,\" {initiator} says, shaking their head in disbelief."
        ]
    },
    "mixer_socials_EnthuseAboutMeal_Targeted_Friendly_AlwaysOn_DiningSocials": {
        "pre_actions": [
            "{initiator} enthuses about the meal they are eating to their friend, {target}."
        ],
        "actions": [
            "\"{target}, have you ever tasted anything as delicious as this before? It's absolutely amazing!\" {initiator} exclaims, savoring every bite.",
            "{initiator} leans toward {target} and says, \"Wow, this meal is truly exceptional! You have to try some of this!\"",
            "\"Can you believe how incredible this food tastes, {target}?\" {initiator} asks, eyes wide in delight and excitement.",
            "\"I can't get over how delicious this is, {target}! I think I've found my new favorite dish,\" {initiator} says, beaming with joy.",
            "\"{target}, I don't think I've ever been this excited about a meal before. Isn't it just divine?\" {initiator} says, practically dancing in their seat.",
            "\"This is hands down the best meal I've ever had, {target}. What do you think?\" {initiator} asks, eager to share the experience.",
            "\"I'm in food heaven right now, {target}. Have you ever tasted anything like this?\" {initiator} gushes, unable to contain their enthusiasm.",
            "\"Words can't even describe how fantastic this meal is, {target}. It's like a symphony of flavors,\" {initiator} says, eyes closed in pure bliss.",
            "\"Every bite of this meal is a revelation, {target}. I can't help but rave about it!\" {initiator} says, a look of pure joy on their face.",
            "\"I could eat this every day for the rest of my life, {target}. It's that good!\" {initiator} exclaims, savoring each and every taste."
        ]
    },
    "mixer_social_PracticeFighting_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} practices fighting with their friend, {target}."
        ],
        "actions": [
            "\"{target}, I've been working on my fighting skills lately. Would you mind practicing with me?\" {initiator} asks eagerly.",
            "\"Hey {target}, I could use a sparring partner to help me improve my combat skills. Are you up for the challenge?\" {initiator} inquires with a grin.",
            "{initiator} stretches their arms and says, \"Alright, {target}, it's time for some friendly combat practice. Let's see what you've got!\"",
            "\"Ever since I started learning to fight, I've wanted to test my skills against you, {target}. Care to join me for a sparring session?\" {initiator} suggests enthusiastically.",
            "\"Let's have a little friendly competition, {target}. How about a practice fight to see who's got the better moves?\" {initiator} proposes with a smirk.",
            "\"Hey {target}, I've been meaning to ask if you'd like to practice some self-defense techniques with me. It's always good to stay sharp,\" {initiator} says, gesturing toward an open space.",
            "\"I've learned some new fighting techniques, {target}, and I could use your help to practice. Are you in?\" {initiator} asks, bouncing on the balls of their feet.",
            "{initiator} cracks their knuckles and says, \"It's been too long since we've had a good sparring session, {target}. Let's see if you can keep up with my new moves!\"",
            "\"I think it's time we tested our strengths against each other, {target}. A friendly sparring match, what do you say?\" {initiator} asks, eager to learn from the experience.",
            "\"Practicing fighting techniques is always more fun with a partner, {target}. Would you mind joining me for a session?\" {initiator} asks, hoping to improve their skills."
        ]
    },
    "mixer_social_MakeFunOfCorporateGoons_Targeted_Funny_AlwaysOn_Career": {
        "pre_actions": [
            "{initiator} makes fun of corporate goons in a joking way with {target}."
        ],
        "actions": [
            "\"{target}, have you heard about the new Synergistic Paradigm-Enhancing Dynamic? It's the latest in corporate jargon!\" {initiator} teases with a grin.",
            "\"{target}, I think you'd excel at Synchronized Hyperbolic Resource Optimization. It's right up your alley,\" {initiator} jokes, winking.",
            "\"I just got a memo about the latest in corporate strategy, {target}. Apparently, we need to focus on Transdimensional Goal-Oriented Metrics!\" {initiator} says, chuckling.",
            "\"Hey {target}, have you been maximizing your Vertical Cross-Functional Integration lately?\" {initiator} asks sarcastically, struggling to keep a straight face.",
            "\"{target}, I think we need to discuss the importance of Inverted Scalable Quantum Networking,\" {initiator} says with a smirk, trying to sound serious.",
            "\"Did you know, {target}, that if we leverage our Holistic Interdependent Paradigms, we can achieve ultimate success?\" {initiator} teases playfully.",
            "\"{target}, you're just the person to help me develop a new strategy for Dynamic Quantum Leap Synergy. Your expertise is crucial,\" {initiator} says, barely able to contain their laughter.",
            "\"Hey {target}, I think we should really focus on optimizing our Metaphysical Ambiguity Resolution. It's the key to our success!\" {initiator} jokes, nudging {target} playfully.",
            "\"{target}, I've got a new assignment for you: Integrative Quantum Flux Optimization. Don't worry, I'm sure you'll nail it,\" {initiator} says, laughing.",
            "\"Let's not forget the importance of Advanced Heterogeneous Ambiguity Analysis, {target}. It's the future of corporate success!\" {initiator} says with a grin, making fun of the jargon.",
            "\"{target}, have you ever noticed how corporate goons always seem to have a never-ending supply of buzzwords? It's like they're all reading from the same script,\" {initiator} chuckles.",
            "{initiator} leans in and whispers to {target}, \"Do you think corporate goons practice their fake smiles and firm handshakes in front of the mirror every morning?\"",
            "\"I wonder if corporate culture has a dress code for the soul, too,\" {initiator} muses, smirking at {target}.",
            "\"Hey {target}, have you ever noticed that corporate goons can make a two-minute conversation take two hours with all their jargon and team-building exercises?\" {initiator} jokes.",
            "\"{target}, let's play a game: Corporate Buzzword Bingo. Every time we hear a corporate goon say 'synergy,' 'innovation,' or 'value-added,' we take a sip of our coffee,\" {initiator} suggests, grinning.",
            "{initiator} laughs and asks {target}, \"Do you think there's a secret competition among corporate goons to see who can use the most buzzwords in a single sentence?\"",
            "\"Corporate culture is like a cult, {target}, but instead of chanting, they're spouting off empty slogans and talking about 'disrupting the industry,'\" {initiator} says with a grin.",
            "\"Hey {target}, I bet corporate goons have a secret handshake, but it probably involves excessive eye contact and an awkwardly long grip,\" {initiator} teases.",
            "{initiator} leans in and whispers to {target}, \"I'm convinced that corporate goons are actually robots, programmed to speak in buzzwords and networking lingo.",
            "\"Corporate culture seems like one big game of 'Who Can Sound the Most Important?', don't you think, {target}?\" {initiator} chuckles.",
        ]
    },
    "mixer_socials_GoofAround_targeted_Funny_alwaysOn": {
        "pre_actions": [
            "{initiator} goofs around with {target}."
        ],
        "actions": [
            "{initiator} sneaks up behind {target} and places their hands over {target}'s eyes. \"Guess who?\" {initiator} says, giggling.",
            "{initiator} playfully tosses a crumpled piece of paper at {target}, trying to get their attention. \"Hey, {target}, catch!\"",
            "{initiator} starts making silly faces at {target} from across the room, hoping to get a laugh out of them.",
            "While {target} is sitting down, {initiator} comes up from behind and tickles them, causing {target} to burst into laughter.",
            "{initiator} challenges {target} to a playful thumb war, grinning mischievously as they lock hands.",
            "{initiator} steals {target}'s hat and starts running around, playfully taunting, \"You'll never catch me, {target}!\"",
            "{initiator} jokingly mimics {target}'s voice and mannerisms, making both of them laugh at the light-hearted impersonation.",
            "{initiator} pretends to trip and fall in front of {target}, then quickly jumps up and exclaims, \"Gotcha, {target}!\"",
            "{initiator} playfully pokes {target} repeatedly, trying to get a rise out of them. \"Hey, {target}, are you ticklish?\"",
            "{initiator} and {target} engage in a spontaneous and lighthearted play-fight, laughing as they gently push each other around."
        ]
    },
    "mixer_social_RantAndRave_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} vehemently expresses their frustration with {target}."
        ],
        "actions": [
            "\"I can't believe you did that, {target}! How could you be so thoughtless?\" {initiator} exclaims, their voice filled with anger.",
            "\"You always do this, {target}! It's like you never listen to me!\" {initiator} shouts, frustration evident in their voice.",
            "\"I've had enough of your nonsense, {target}! I can't keep tolerating your behavior!\" {initiator} yells, their face turning red.",
            "\"You think you can just get away with everything, don't you, {target}? Well, not this time!\" {initiator} snaps, their voice laced with bitterness.",
            "\"I've had it up to here with your constant mistakes, {target}! When will you ever learn?\" {initiator} vents, their tone dripping with annoyance.",
            "\"Enough is enough, {target}! I can't stand by and watch you ruin everything anymore!\" {initiator} declares, their voice filled with determination.",
            "\"I can't believe you would betray my trust like this, {target}! I thought we were friends!\" {initiator} accuses, their voice filled with hurt.",
            "\"You think you're so clever, don't you, {target}? Well, let me tell you, your actions have consequences!\" {initiator} warns, their voice tinged with menace.",
            "\"I've tried to be patient with you, {target}, but now I've reached my limit! Prepare yourself for the truth!\" {initiator} warns, their voice filled with frustration.",
            "\"I'm tired of your excuses, {target}! It's time you face the consequences of your actions!\" {initiator} declares, their voice filled with righteous anger."
        ]
    },
    "mixer_Social_Sim_Ghost_Ask_About_Being_Dead": {
        "pre_actions": [
            "{initiator} asks {target}, who is a ghost, what it is like to be dead."
        ],
        "actions": [
            "\"{target}, I've always been curious about the afterlife. Can you tell me what it's like to be a ghost?\" {initiator} asks cautiously.",
            "\"Hey {target}, I know it might be a sensitive topic, but I'm really interested in knowing what being dead feels like. Can you share your experience?\" {initiator} inquires gently.",
            "\"{target}, I've been wondering about this for a while now. What's it like on the other side? Can you share your perspective as a ghost?\" {initiator} asks with genuine curiosity.",
            "\"I can't imagine what you've been through, {target}. Would you mind telling me what it's like to be dead?\" {initiator} asks, trying to be considerate of {target}'s feelings.",
            "\"Being a ghost must be so different from being alive, {target}. Can you tell me what your experience has been like since you passed away?\" {initiator} asks with empathy.",
            "\"{target}, I've never had the chance to ask someone who's experienced it firsthand. What is it like to be a ghost?\" {initiator} wonders aloud.",
            "\"I hope it's not too personal, {target}, but I'm really curious about the afterlife. Can you share what it's like being dead?\" {initiator} asks respectfully.",
            "\"Death has always been a mystery to the living, {target}. Would you be willing to shed some light on what it's like being a ghost?\" {initiator} asks, intrigued.",
            "\"{target}, I don't mean to pry, but I've always been fascinated by the concept of life after death. Can you share your experience as a ghost?\" {initiator} questions gently.",
            "\"{target}, I know this might be an uncomfortable topic, but I can't help but wonder what it feels like to be dead. Can you enlighten me?\" {initiator} asks with a mix of curiosity and concern."
        ]
    },
    "mixer_Social_Targeted_Romance_Loyal_ConfessCheating": {
        "pre_actions": [
            "{initiator} confesses that they have been cheating on their romantic partner, {target}."
        ],
        "actions": [
            "\"{target}, I can't keep this from you any longer. I've been unfaithful in our relationship,\" {initiator} admits, guilt heavy in their voice.",
            "\"I never wanted to hurt you, {target}, but I have to be honest with you. I've been cheating on you,\" {initiator} says, struggling to meet {target}'s eyes.",
            "\"{target}, I've made a terrible mistake. I've been seeing someone else behind your back, and I can't hide it anymore,\" {initiator} confesses, tears welling up in their eyes.",
            "\"This is going to hurt, but I need to tell you the truth, {target}. I've been unfaithful,\" {initiator} reveals, their voice shaking with regret.",
            "\"I've been betraying your trust, {target}, and I can't keep it a secret any longer. I've been cheating on you,\" {initiator} says, clearly distressed.",
            "\"{target}, I know this will be hard to hear, but I've been unfaithful in our relationship. I'm so sorry,\" {initiator} says, tears streaming down their face.",
            "\"I can't pretend everything is fine anymore, {target}. I've been seeing someone else, and I need you to know,\" {initiator} confesses, their voice barely a whisper.",
            "\"{target}, I don't deserve your forgiveness, but I need to tell you that I've cheated on you,\" {initiator} admits, their face filled with shame.",
            "\"I wish I could take it back, {target}, but I can't. I've been cheating on you, and it's tearing me apart,\" {initiator} says, their voice filled with remorse.",
            "\"Please know how much I regret this, {target}, but I've been unfaithful to you. I just couldn't keep it a secret any longer,\" {initiator} says, their heart heavy with guilt."
        ]
    },
    "mixer_social_Provoke_targeted_mean_emotionSpecific": {
        "pre_actions": [
            "{initiator} intentionally provokes {target}."
        ],
        "actions": [
            "\"{target}, I've heard people say you're not very bright, but I didn't think it was this bad,\" {initiator} sneers, trying to provoke a reaction.",
            "\"I'm surprised you even made it this far, {target}. Did someone carry you here?\" {initiator} says mockingly, hoping to get under {target}'s skin.",
            "\"Oh, I see you're still trying. It's almost cute how you think you can keep up, {target},\" {initiator} taunts maliciously.",
            "\"Did anyone ever tell you that you're way out of your league, {target}? Or are they just being polite?\" {initiator} says with a cruel grin.",
            "\"{target}, do you ever get tired of being the weakest link? Or have you just accepted it as a part of who you are?\" {initiator} asks, trying to provoke {target}.",
            "\"Hey {target}, have you considered giving up? It's probably for the best, considering your track record,\" {initiator} says, attempting to hurt {target}'s feelings.",
            "\"I was just wondering, {target}, how does it feel to be constantly overshadowed by everyone around you?\" {initiator} asks, a mean smirk on their face.",
            "\"Tell me, {target}, how do you manage to fail so consistently? It's almost impressive,\" {initiator} says, trying to provoke {target} into reacting.",
            "\"I don't think I've ever met someone as incompetent as you, {target}. How do you even manage to get through the day?\" {initiator} asks, attempting to anger {target}.",
            "\"Sometimes, {target}, I honestly wonder if you're even trying. Has anyone ever told you that you're a disappointment?\" {initiator} says, trying to get a rise out of {target}."
        ]
    },
    "mixer_Social_Targeted_Romance_Loyal_RebuildTrust": {
        "pre_actions": [
            "{initiator} seeks to rebuild the trust they once had with {target}."
        ],
        "actions": [
            "\"{target}, I know I've made mistakes in the past, but I want to make it right. Can we start over?\" {initiator} asks with hope in their eyes.",
            "\"Remember the good times we had, {target}? I want to create more of those memories with you, but first we need to rebuild our trust,\" {initiator} says sincerely.",
            "\"{target}, I understand that I've hurt you, and I'm willing to do whatever it takes to regain your trust. Please give me a chance,\" {initiator} pleads, looking into {target}'s eyes.",
            "\"I've learned from my mistakes, {target}, and I promise to be a better partner for you. Can we work on rebuilding our trust together?\" {initiator} asks earnestly.",
            "\"I know I've let you down, {target}, but I truly believe we can find our way back to each other. Let's take it one step at a time,\" {initiator} suggests, reaching for {target}'s hand.",
            "\"Trust is the foundation of any relationship, {target}, and I want to rebuild ours. I'm committed to being open and honest with you from now on,\" {initiator} promises, holding {target}'s gaze.",
            "\"Please, {target}, I'm asking for a chance to make amends. I want to show you that I can be the person you deserve,\" {initiator} says, desperation in their voice.",
            "\"I know it won't be easy, {target}, but if you're willing to try, I'll do everything in my power to rebuild the trust we once had,\" {initiator} vows, determination in their eyes.",
            "\"{target}, I want to be the person who makes you happy, not the one who causes you pain. I'll work tirelessly to regain your trust,\" {initiator} says, their voice full of conviction.",
            "\"I can't change the past, {target}, but I can change our future. Let's work together to rebuild the trust and love we once shared,\" {initiator} says, holding out their hand for {target} to take."
        ]
    },
    "mixer_social_ShareMelancholyThoughts_tag_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} shares their melancholy thoughts with {target}."
        ],
        "actions": [
            "\"{target}, I've been feeling really down lately, and I don't know who else to talk to,\" {initiator} says, with sadness in their eyes.",
            "\"Sometimes, I feel like I'm drowning in my own thoughts, and I just need someone to listen. Can I share them with you, {target}?\" {initiator} asks hesitantly.",
            "\"I've been going through a rough time, {target}, and I think talking about it with you might help,\" {initiator} admits, hoping for understanding.",
            "\"The world feels so heavy on my shoulders, {target}. I need to get these thoughts off my chest. Will you hear me out?\" {initiator} pleads gently.",
            "\"I never thought I'd open up like this, but I trust you, {target}. Can I share my melancholic thoughts with you?\" {initiator} asks, looking vulnerable.",
            "\"{target}, I feel like I'm trapped in a dark cloud, and I don't know how to escape it. Can we talk about it?\" {initiator} asks, reaching out for support.",
            "\"Sometimes, I don't know how to cope with these sad thoughts, {target}. Would you listen to me and help me sort them out?\" {initiator} wonders, looking for comfort.",
            "\"I've been feeling really low, {target}, and I think I need to talk about it. Can I confide in you?\" {initiator} asks, with a glimmer of hope in their eyes.",
            "\"{target}, I think I need a friend right now. Can I share what's been bothering me with you?\" {initiator} asks, seeking solace.",
            "\"I know it's not easy listening to someone's sad thoughts, {target}, but I don't know who else to turn to. Can you be there for me?\" {initiator} pleads, searching for understanding."
        ]
    },
    "mixer_social_SweetTalk_targeted_romance_skills": {
        "pre_actions": [
            "{initiator} sweet talks {target}."
        ],
        "actions": [
            "\"{target}, every time I look into your eyes, I feel like I'm getting lost in a beautiful, endless ocean,\" {initiator} says with a warm smile.",
            "\"You have no idea how much my heart races when I'm around you, {target}. It's like you've cast a magical spell on me,\" {initiator} says, gazing at {target} adoringly.",
            "\"{target}, your smile lights up the room and fills my heart with happiness. I'm so grateful to have you in my life,\" {initiator} whispers gently.",
            "\"Being with you, {target}, feels like a dream come true. Every moment I spend with you is a treasure,\" {initiator} says sincerely.",
            "\"{target}, your laughter is like music to my ears, and just the thought of you brightens up even my darkest days,\" {initiator} says with a loving expression.",
            "\"When I hold you in my arms, {target}, I feel like I'm holding the entire world, and nothing else matters,\" {initiator} says, brushing {target}'s hair back gently.",
            "\"Your presence, {target}, is like a warm, comforting embrace that shelters me from all the storms of life,\" {initiator} says with deep affection.",
            "\"{target}, your love is like a beacon that guides me through the darkest nights, leading me home to you,\" {initiator} says, their eyes locked on {target}'s.",
            "\"Whenever I think of you, {target}, my heart swells with love and admiration. You truly are the most incredible person I've ever known,\" {initiator} says, holding {target}'s hand.",
            "\"In your arms, {target}, I've found my sanctuary, my safe haven. I never knew true love until I met you,\" {initiator} says, their voice filled with emotion."
        ]
    },
    "mixer_social_PitchStoryIdea_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} pitches their story idea to their friend, {target}."
        ],
        "actions": [
            "\"{target}, I had this amazing story idea, and I wanted to share it with you. Let me know what you think,\" {initiator} says excitedly.",
            "\"Hey, {target}, I've been thinking about writing a novel, and I have this incredible idea. Can I run it by you?\" {initiator} asks, eager for feedback.",
            "\"I came up with a fascinating storyline, {target}. Would you mind listening to it and giving me your thoughts?\" {initiator} inquires, looking hopeful.",
            "\"So, I've been brainstorming, and I think I have a great idea for a story. I'd love to hear your opinion, {target},\" {initiator} says, trying to gauge their interest.",
            "\"Okay, {target}, I have this brilliant concept for a tale, and I need someone to bounce ideas off of. Are you up for it?\" {initiator} asks, their eyes shimmering with enthusiasm.",
            "\"I've been working on this incredible idea for a narrative, {target}. Can I share it with you and get your input?\" {initiator} suggests, smiling nervously.",
            "\"Hey, {target}, you know how much I love stories, right? Well, I came up with an idea that I think is fantastic, and I'd like your thoughts on it,\" {initiator} says, waiting for their response.",
            "\"I've had this story idea brewing in my mind for a while, {target}. It's finally taking shape, and I'd love to have your perspective on it,\" {initiator} admits, looking a bit shy.",
            "\"You always give great advice, {target}. I'd really appreciate it if you could listen to my story idea and tell me what you think,\" {initiator} pleads, hoping for a positive response.",
            "\"Alright, {target}, I've got this intriguing idea for a tale that's been keeping me up at night. I need your expert opinion. Are you ready to hear it?\" {initiator} asks, grinning in anticipation."
        ]
    },
    "mixer_social_RekindleTheRomance_targeted_romance_lowScore": {
        "pre_actions": [
            "{initiator} attempts to rekindle the romance between them and their partner, {target}."
        ],
        "actions": [
            "\"{target}, I've been thinking a lot lately about the times we shared together. Can we give it another try?\" {initiator} asks, hope in their eyes.",
            "\"Remember the good days, {target}? I miss them. I miss us. What do you say we try to rekindle the flame?\" {initiator} suggests, a nostalgic smile on their face.",
            "\"{target}, I can't help but feel that we were meant to be together. Can we give our love a second chance?\" {initiator} pleads, their heart on their sleeve.",
            "\"Every time I see you, {target}, I'm reminded of what we once had. Do you ever wonder if we could have it again?\" {initiator} asks, looking for a glimmer of hope.",
            "\"I've never stopped caring about you, {target}, and I think it's time we explore the possibility of getting back together,\" {initiator} says, taking a deep breath.",
            "\"{target}, I know it's been a while, but I can't shake the feeling that we belong together. Could we give our romance another shot?\" {initiator} inquires, looking into {target}'s eyes.",
            "\"I've been doing a lot of soul-searching, {target}, and I've come to realize that I want to be with you again. Can we try to rekindle our love?\" {initiator} asks earnestly.",
            "\"{target}, I know we've both grown and changed, but I believe we can find our way back to each other. Are you willing to try?\" {initiator} asks, searching for a positive response.",
            "\"Have you ever thought about us, {target}? About what we could be if we tried again? I'm ready to give it a chance if you are,\" {initiator} says, holding their breath for an answer.",
            "\"{target}, I keep thinking about the love we shared and how special it was. I know we can make it work again. Please, can we try?\" {initiator} begs, with a mix of hope and vulnerability."
        ]
    },
    "mixer_Social_Targeted_Mean_Loyal_ConfrontAboutBullying": {
        "pre_actions": [
            "{initiator} confronts {target} about their bullying behavior."
        ],
        "actions": [
            "\"{target}, I've had enough of your bullying. It's time we talked about it,\" {initiator} says, gathering the courage to stand up for themselves.",
            "\"I can't keep ignoring the way you treat me, {target}. We need to address this bullying situation,\" {initiator} says, looking determined.",
            "\"{target}, I've been feeling really hurt by the way you've been treating me. It's time for us to talk about your bullying behavior,\" {initiator} says, trying to keep their voice steady.",
            "\"I refuse to be a victim anymore, {target}. Your bullying has to stop, and we need to discuss it right now,\" {initiator} says, finally confronting the issue.",
            "\"Your constant bullying has made my life miserable, {target}. Let's sit down and talk about why you're doing this to me,\" {initiator} says, hoping for a resolution.",
            "\"{target}, I want to understand why you've been bullying me. It's causing me a lot of pain, and we need to talk about it,\" {initiator} says, searching for answers.",
            "\"I didn't want to have to confront you like this, {target}, but your bullying has pushed me to my limit. We need to resolve this issue,\" {initiator} says, taking a stand.",
            "\"I've been trying to ignore your bullying, {target}, but I can't take it anymore. Let's talk about what's going on and why you're treating me this way,\" {initiator} suggests, desperate for a change.",
            "\"{target}, your bullying has been affecting more than just me. It's time we had a conversation about your actions and their consequences,\" {initiator} says, seeking to make a difference.",
            "\"I'm tired of being your target, {target}. We need to discuss your bullying behavior and find a way to put an end to it,\" {initiator} says, standing up for themselves with newfound confidence."
        ]
    },
    "mixer_social_WeaponizedJoke_targeted_funny_alwaysOn": {
        "pre_actions": [
            "{initiator} makes a weaponized joke at {target}'s expense."
        ],
        "actions": [
            "\"{target}, I heard this joke the other day, but it's a bit edgy. Are you up for it?\" {initiator} asks, grinning mischievously.",
            "\"Hey, {target}, brace yourself. I've got a joke that might just cross the line, but I think you'll love it,\" {initiator} says with a sly smile.",
            "\"Alright, {target}, I've got a joke for you, but it's definitely not for the faint of heart. Are you ready?\" {initiator} inquires, a playful glint in their eye.",
            "\"I came across this edgy joke, {target}, and I couldn't help but think of you. Do you want to hear it?\" {initiator} asks, raising their eyebrows.",
            "\"Prepare yourself, {target}, I've got a joke that's bound to push some boundaries, but I think you can handle it,\" {initiator} says, smirking.",
            "\"Okay, {target}, I've got a joke for you, but it's a little on the wild side. You in?\" {initiator} asks, gauging {target}'s reaction.",
            "\"{target}, I've got an edgy joke for you, but if it's too much, just remember, you asked for it,\" {initiator} teases, testing the waters.",
            "\"Hey, {target}, I've got a joke that's right on the edge of being too much. Do you dare to hear it?\" {initiator} asks, challenging {target}.",
            "\"{target}, I've got a pretty edgy joke for you, but you've got to promise not to hold it against me. Deal?\" {initiator} says, grinning cautiously.",
            "\"Alright, {target}, I've got a joke that might be a bit too edgy, but I have a feeling you'll appreciate it. Ready?\" {initiator} asks, hoping for a positive response."
        ]
    },
    "mixer_socials_DiscussFoodFlavors_Targeted_Friendly_AlwaysOn_DiningSocials": {
        "pre_actions": [
            "{initiator} discusses food flavors with {target}."
        ],
        "actions": [
            "\"{target}, have you ever wondered why some flavors just seem to go well together?\" {initiator} asks, looking genuinely curious.",
            "\"Do you have a favorite flavor combination, {target}? I've been experimenting with some new recipes and I'd love to hear your thoughts,\" {initiator} says, smiling.",
            "\"Hey {target}, I've been thinking about how different cultures have unique flavor profiles. What's your favorite cuisine, and why?\" {initiator} inquires, genuinely interested.",
            "\"{target}, I've always been fascinated by the way our taste buds work. What's the strangest flavor you've ever tried, and did you like it?\" {initiator} asks, eager for an answer.",
            "\"I was just reading about the science behind flavor pairings, {target}. Do you think there's some truth to the idea that certain flavors are destined to be together?\" {initiator} wonders aloud.",
            "\"{target}, I know it might sound weird, but have you ever had a flavor combination that you thought would be awful, but ended up being surprisingly good?\" {initiator} asks, intrigued.",
            "\"Have you noticed how different seasons seem to have their own unique flavors, {target}? What's your favorite seasonal flavor, and why?\" {initiator} asks, looking for a thoughtful response.",
            "\"Hey {target}, I've been experimenting with some new spices lately. Do you have any favorite spices or herbs that you think really elevate a dish?\" {initiator} inquires, looking for inspiration.",
            "\"{target}, I recently read that our taste preferences can change as we age. Have you ever experienced a change in your taste buds, and what flavors do you appreciate now that you didn't before?\" {initiator} asks, genuinely curious.",
            "\"So, {target}, I've been playing around with the idea of creating a new dish based on unusual flavor combinations. What's something you think might be interesting to try, even if it's a bit out there?\" {initiator} asks, eager for a creative suggestion."
        ]
    },
    "mixer_social_ComplimentColorChoices_targeted_Friendly_alwaysOn_situation_Day1DLC": {
        "pre_actions": [
            "{initiator} compliments {target}'s color choices.",
        ],
        "actions": [
            "\"{target}, I must say, the colors you've chosen really bring out the best in you,\" {initiator} says with a smile.",
            "\"I've been meaning to tell you, {target}, the colors you wear always seem to brighten up the room,\" {initiator} remarks appreciatively.",
            "\"Your taste in colors is impeccable, {target}. It really highlights your personality,\" {initiator} compliments sincerely.",
            "\"{target}, I just wanted to say that your color choices are always so unique and stylish. It's really impressive,\" {initiator} comments admiringly.",
            "\"Can I just say, {target}, that your color choices never fail to impress me? You have a fantastic sense of style,\" {initiator} says with a nod of approval.",
            "\"You know, {target}, I've always admired your ability to mix and match colors so effortlessly. It's truly a talent,\" {initiator} mentions, looking impressed.",
            "\"{target}, I've noticed that you have a real knack for choosing colors that perfectly suit you. Keep up the great work!\" {initiator} encourages warmly.",
            "\"I wanted to tell you, {target}, that the colors you pick always manage to make a statement. You have a real eye for it,\" {initiator} says, looking genuinely impressed.",
            "\"Your color choices always stand out, {target}. You have a way of making even the simplest combinations look stunning,\" {initiator} compliments enthusiastically.",
            "\"{target}, your color choices always seem to be on point. It's like you have a natural flair for it,\" {initiator} says with a look of admiration."
        ]
    },
    "mixer_social_ComplainAbout_Fruitcake_targeted_alwayson": {
        "pre_actions": [
            "{initiator} expresses their contempt for fruitcake to {target}.",
        ],
        "actions": [
            "\"{target}, can you believe how terrible fruitcake is? I just don't get why anyone would like it,\" {initiator} says, grimacing.",
            "\"I don't know about you, {target}, but I honestly can't stand fruitcake. It's just so dense and unappetizing,\" {initiator} complains.",
            "\"Am I the only one who thinks fruitcake is just the worst? What are your thoughts, {target}?\" {initiator} asks, hoping for agreement.",
            "\"I have to get this off my chest, {target}: fruitcake has got to be the most overrated dessert ever,\" {initiator} says with disdain.",
            "\"Every time I see a fruitcake, I just can't help but wonder who actually enjoys eating it. Don't you agree, {target}?\" {initiator} questions.",
            "\"I'm sorry, {target}, but I just can't hold back any longer. Fruitcake is absolutely awful, isn't it?\" {initiator} vents.",
            "\"{target}, I need someone to back me up on this: fruitcake is just gross, right?\" {initiator} asks, looking for validation.",
            "\"I've been meaning to ask you, {target}: are you a fan of fruitcake? Because I honestly can't understand its appeal,\" {initiator} says, baffled.",
            "\"Every holiday season, I dread the inevitable appearance of fruitcake. Do you share my sentiments, {target}?\" {initiator} asks with a sigh.",
            "\"I can't be the only one who thinks fruitcake is an abomination, right, {target}?\" {initiator} pleads, looking for support in their distaste."
        ]
    },
    "mixer_social_DiscussLackOfNewspapers_targeted_Friendly_alwysOn_situation_Day1DLC": {
        "pre_actions": [
            "{initiator} discusses their frustration with the lack of newspapers with {target}."
        ],
        "actions": [
            "\"{target}, have you noticed that there aren't many newspapers around anymore? It's quite frustrating,\" {initiator} says, clearly annoyed.",
            "\"I can't believe how hard it is to find a decent newspaper these days, {target}. What's going on?\" {initiator} complains, shaking their head.",
            "\"{target}, it's like newspapers have vanished into thin air. I miss the days when I could just grab one and enjoy my morning coffee,\" {initiator} sighs.",
            "\"I don't know about you, {target}, but the lack of newspapers around here is really getting on my nerves,\" {initiator} grumbles.",
            "\"It's a sad state of affairs when you can't even find a newspaper to read anymore, don't you think, {target}?\" {initiator} asks with a frown.",
            "\"I was just telling someone the other day how I miss the feel of a newspaper in my hands, {target}. It's just not the same anymore,\" {initiator} laments.",
            "\"Remember when you could find newspapers everywhere, {target}? What happened to those days? I can't stand this digital age,\" {initiator} complains passionately.",
            "\"{target}, do you have any idea where I can find a newspaper around here? It seems like they're a rare commodity these days,\" {initiator} says in frustration.",
            "\"Sometimes I feel like I'm the only person left who still prefers a newspaper to reading news online, {target}. It's quite disheartening,\" {initiator} confides.",
            "\"I just want a simple newspaper to read with my morning coffee, {target}. Why is that so difficult to find these days?\" {initiator} asks, exasperated."
        ]
    },
    "mixer_social_ChewOut_targeted_mean_emotionSpecific": {
        "pre_actions": [
            "{initiator} scolds {target} harshly.",
        ],
        "actions": [
            "\"{target}, I can't believe how thoughtless you've been! You should be ashamed of yourself,\" {initiator} says angrily.",
            "\"How many times do I have to tell you, {target}? You always mess things up!\" {initiator} yells, frustration evident in their voice.",
            "\"{target}, I'm so sick of your incompetence! When are you going to get it together?\" {initiator} snaps, glaring at them.",
            "\"{target}, your constant failures are getting on my nerves! Can't you do anything right?\" {initiator} exclaims, seething with rage.",
            "\"Are you really this careless, {target}? It's like you don't even care about anyone but yourself!\" {initiator} scolds harshly.",
            "\"Every time I think you've changed, {target}, you prove me wrong. I'm tired of your selfishness!\" {initiator} says, shaking their head in disappointment.",
            "\"I've had enough of your nonsense, {target}! It's time you grow up and take responsibility for your actions!\" {initiator} barks, fed up with their behavior.",
            "\"{target}, I don't know how much more of your stupidity I can take. Get your act together!\" {initiator} shouts, losing their patience.",
            "\"Seriously, {target}? You've crossed the line this time. I won't tolerate this kind of behavior any longer!\" {initiator} warns, their voice dripping with contempt.",
            "\"Enough is enough, {target}! You really need to start thinking about the consequences of your actions!\" {initiator} chastises, their anger reaching a boiling point."
        ]
    },
    "mixer_social_ComplainAboutTvSize_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} complains to {target} about the small size of their TV.",
        ],
        "actions": [
            "\"{target}, I can't believe how small this TV is! How can anyone watch anything on this?\" {initiator} says, squinting at the screen.",
            "\"Ugh, this TV is just too tiny, {target}. How do you even enjoy watching anything on it?\" {initiator} complains, annoyed.",
            "\"Seriously, {target}, this TV is giving me a headache. Who even buys a TV this small nowadays?\" {initiator} grumbles.",
            "\"I can't take it anymore, {target}. This TV is just too small for my liking. We need an upgrade,\" {initiator} says with frustration.",
            "\"{target}, it's like watching a movie on a postage stamp. This TV size is ridiculous!\" {initiator} exclaims, shaking their head.",
            "\"You know, {target}, I've never been one to complain, but this TV size is just unbearable,\" {initiator} says, rubbing their eyes.",
            "\"I can't help but say it, {target}, but this TV is just way too small for the room. We need something bigger,\" {initiator} says, trying to adjust their view.",
            "\"Watching a movie on this TV is like trying to read a book through a keyhole, {target}. It's just too small!\" {initiator} moans.",
            "\"I've been holding my tongue, {target}, but this TV size is driving me crazy. Can we please consider getting a bigger one?\" {initiator} pleads.",
            "\"I don't know how you can stand it, {target}. This TV is just too small to enjoy anything properly,\" {initiator} says, clearly irritated."
        ]
    },
    "mixer_social_Congratulate_targeted_Friendly_alwaysOn_event": {
        "pre_actions": [
            "{initiator} congratulates {target} on their achievement.",
        ],
        "actions": [
            "\"{target}, I just wanted to say congratulations on your achievement! You truly deserve it,\" {initiator} says with a warm smile.",
            "\"Hey {target}, congratulations on your big win! I knew you could do it!\" {initiator} exclaims, giving {target} a pat on the back.",
            "\"Congrats, {target}! I'm so proud of you and everything you've accomplished,\" {initiator} says, beaming with pride.",
            "\"{target}, I just heard the news! Congratulations, my friend! You've earned it,\" {initiator} says, raising a toast in {target}'s honor.",
            "\"I couldn't be happier for you, {target}. Congratulations on your success!\" {initiator} says, offering a heartfelt hug.",
            "\"Wow, {target}, you really did it! I'm so impressed and proud of you. Congratulations!\" {initiator} says, clapping their hands in excitement.",
            "\"Congratulations, {target}! Your hard work and determination have finally paid off. I'm really happy for you,\" {initiator} says, sincerity shining in their eyes.",
            "\"Kudos to you, {target}! I always knew you had it in you. Congratulations on this amazing achievement,\" {initiator} says, giving {target} a high-five.",
            "\"Well done, {target}! Your success is truly well-deserved. Congratulations!\" {initiator} says, offering a firm handshake.",
            "\"Bravo, {target}! Your accomplishments never cease to amaze me. Congratulations on this latest triumph,\" {initiator} says, wearing a genuine smile of admiration."
        ]
    },
    "mixer_social_AskAboutDrink_targeted_Friendly_alwaysOn_Event": {
        "pre_actions": [
            "{initiator} asks {target} about their drink in a friendly manner at an event.",
        ],
        "actions": [
            "\"{target}, do you like the drink I made for you?\" {initiator} asks, looking for approval.",
            "\"How's the drink, {target}? Is it to your liking?\" {initiator} inquires with a smile.",
            "\"I tried a new recipe for this drink, {target}. What do you think of it?\" {initiator} questions, seeking an honest opinion.",
            "\"Are you enjoying that drink, {target}? I was hoping you'd like it,\" {initiator} says, watching {target} take a sip.",
            "\"Hey {target}, how's the drink? I put a little twist on it, do you like it?\" {initiator} asks curiously.",
            "\"{target}, is the drink good? I wasn't sure if it would be to your taste,\" {initiator} says, sounding a bit uncertain.",
            "\"So, {target}, what's your verdict on the drink? Thumbs up or down?\" {initiator} asks playfully.",
            "\"I noticed you haven't said anything about the drink, {target}. Do you like it?\" {initiator} questions, hoping for a positive response.",
            "\"I was experimenting with flavors in this drink, {target}. How did it turn out?\" {initiator} asks, eager for feedback.",
            "\"Is the drink hitting the spot, {target}? I wanted to make something you'd enjoy,\" {initiator} says, hoping their effort paid off."
        ]
    },
    "mixer_social_DiscussFitnessTechniques_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} discusses fitness techniques with their friend, {target}."
        ],
        "actions": [
            "\"{target}, I've been trying out this new workout routine, and I'd love to hear your thoughts on it,\" {initiator} says enthusiastically.",
            "\"Hey {target}, you seem to be in great shape. Can you share some fitness tips with me?\" {initiator} asks, genuinely interested.",
            "\"So, {target}, I've been experimenting with different exercises lately. Have you tried any new fitness techniques that you think are worth sharing?\" {initiator} inquires.",
            "\"I've noticed you're really consistent with your workouts, {target}. Mind sharing some of your favorite techniques?\" {initiator} asks, hoping to learn something new.",
            "\"{target}, I came across this fitness article about a new technique, and I can't decide if it's worth trying. What do you think?\" {initiator} says, showing the article to {target}.",
            "\"Hey {target}, I've been trying to improve my fitness lately. Can you recommend any techniques that have worked well for you?\" {initiator} asks with curiosity.",
            "\"I've been struggling with my workout routine recently, {target}. Do you have any fitness techniques that could help me get back on track?\" {initiator} says, feeling a bit discouraged.",
            "\"{target}, I heard about this interesting fitness technique that's supposed to be really effective. Have you tried anything like that before?\" {initiator} asks, eager for information.",
            "\"I'm thinking of incorporating some new fitness techniques into my routine, {target}. Any suggestions on where to start?\" {initiator} asks, seeking advice.",
            "{initiator} approaches {target} at the gym and asks, \"Hey, I noticed you were doing a unique exercise. Can you explain the technique behind it? It looks really effective.\""
        ]
    },
    "mixer_social_DiscussLocalFishingSpots_targeted_friendly_alwaysOn_neighbor": {
        "pre_actions": [
            "{initiator} discusses local fishing spots with their friend, {target}."
        ],
        "actions": [
            "\"{target}, have you heard about that hidden fishing spot near the old bridge? I've heard the fish are biting like crazy there,\" {initiator} says with excitement.",
            "\"Hey {target}, I was thinking of trying out a new fishing spot this weekend. Any recommendations?\" {initiator} asks, hoping for some insider tips.",
            "\"{target}, I heard you're quite the fisherman. Mind sharing some of your favorite local fishing spots with me?\" {initiator} inquires, genuinely interested.",
            "\"I caught this monster of a fish the other day, {target}. Let me tell you about the amazing spot I found!\" {initiator} says, eager to share their discovery.",
            "\"{target}, I came across this beautiful fishing spot the other day. You should join me there sometime,\" {initiator} suggests, hoping for some quality time together.",
            "\"Did you know, {target}, that there's a hidden gem of a fishing spot just a few miles from here? Let me fill you in,\" {initiator} says, ready to share the secret.",
            "\"Rumor has it that there's a fantastic fishing spot around here, {target}. Have you tried it yet?\" {initiator} asks curiously.",
            "\"So, {target}, I've been exploring some local fishing spots lately, and I found this incredible place. Want to hear about it?\" {initiator} asks with enthusiasm.",
            "\"I've been trying out different fishing spots around here, {target}. What are your go-to places when you want a good catch?\" {initiator} inquires, hoping to learn something new.",
            "\"{target}, I know you're an expert when it comes to local fishing spots. Can you share some of your secrets with me?\" {initiator} asks, looking for guidance."
        ]
    },
    "mixer_social_DiscussZebras_targeted_Friendly_alwaysOn_situation_Day1DLC": {
        "pre_actions": [
            "{initiator} discusses zebras with {target}."
        ],
        "actions": [
            "\"{target}, have you ever wondered about the unique stripes of zebras and their purpose?\" {initiator} asks curiously.",
            "\"{target}, did you know that no two zebras have the same pattern of stripes? It's like their own personal fingerprint,\" {initiator} shares excitedly.",
            "\"Hey, {target}, did you ever get the chance to see zebras up close? They're such fascinating creatures,\" {initiator} says, reminiscing about a past experience.",
            "\"I was reading an article about zebras the other day, {target}. It turns out their stripes help them stay cool in the heat,\" {initiator} explains, eager to share the newfound knowledge.",
            "\"Have you ever wondered why zebras are social creatures, {target}? I'd love to talk about their unique behaviors with you,\" {initiator} says, hoping to spark an interesting conversation.",
            "\"{target}, I was watching a documentary on zebras yesterday, and I thought you'd find it interesting too. Want to watch it with me?\" {initiator} suggests enthusiastically.",
            "\"I've always been intrigued by the way zebras run in zigzag patterns to escape predators, {target}. Do you think it's their stripes that help them with this?\" {initiator} asks, looking for {target}'s opinion.",
            "\"Did you know that zebras can actually run up to 65 kilometers per hour, {target}? I find that fascinating!\" {initiator} exclaims, eager to discuss the topic further.",
            "\"{target}, what's your favorite thing about zebras? I'm curious to know,\" {initiator} asks, hoping to learn more about {target}'s interests.",
            "\"I dreamt I was riding a zebra last night, {target}. It made me wonder how people first discovered they could ride horses but not zebras,\" {initiator} says, pondering the thought."
        ]
    },
    "mixer_social_AskForReassurance_targeted_romance_emotionSpecific": {
        "pre_actions": [
            "{initiator} asks {target} for reassurance as a romantic partner.",
        ],
        "actions": [
            "\"{target}, do you really love me? I just need to hear it from you,\" {initiator} says, seeking comfort in {target}'s words.",
            "\"Sometimes I feel insecure about our relationship, {target}. Can you tell me how you truly feel about us?\" {initiator} asks, hoping for reassurance.",
            "\"{target}, I've been feeling a little vulnerable lately. Can you remind me why you fell in love with me?\" {initiator} asks with a small, timid smile.",
            "\"I know it sounds silly, but I just need to know that you still care about me, {target}. Do you?\" {initiator} asks, looking into {target}'s eyes.",
            "\"Can you promise me, {target}, that we'll always be there for each other, no matter what happens?\" {initiator} inquires, seeking affirmation of their love.",
            "\"{target}, can you assure me that our love is strong enough to withstand any challenges that come our way?\" {initiator} asks, their voice filled with hope.",
            "\"I've been feeling a bit lost lately, {target}. Can you tell me what I mean to you and why you chose me?\" {initiator} asks, yearning for a reminder of their love.",
            "\"Sometimes I doubt myself and wonder if I'm enough for you, {target}. Can you help me understand why you love me?\" {initiator} asks, needing reassurance.",
            "\"{target}, I just need to hear you say it one more time. Do you love me, and are you committed to our relationship?\" {initiator} says, seeking confirmation.",
            "\"Can you remind me of the reasons you fell in love with me, {target}? I need to feel the warmth of your love right now,\" {initiator} pleads gently."
        ]
    },
    "mixer_social_ComplainAboutLocalYouths_targeted_friendly_alwaysOn_neighbor": {
        "pre_actions": [
            "{initiator} complains to {target} about local youths.",
        ],
        "actions": [
            "\"{target}, have you noticed how the local youths have become increasingly disrespectful and noisy lately?\" {initiator} asks with genuine concern.",
            "\"Can you believe the audacity of these local kids? They have no respect for others' properties or peace,\" {initiator} says, venting to {target}.",
            "\"You know, {target}, I hate to sound like a grumpy old person, but these local youths are really starting to get on my nerves,\" {initiator} complains.",
            "\"I've had enough, {target}. These young troublemakers have no respect for our community. It's about time someone put a stop to their antics,\" {initiator} says, frustrated.",
            "\"{target}, I don't know if you've noticed, but the local youths have been causing a ruckus lately. It's driving me up the wall,\" {initiator} admits.",
            "\"Every day, it's the same story with these local kids. They're loud, they litter, and they have no regard for us, {target}. Something needs to change,\" {initiator} says, shaking their head.",
            "\"{target}, I've tried my best to stay patient, but these local youths are making it impossible to enjoy a peaceful evening at home. What's going on with them?\" {initiator} wonders aloud.",
            "\"I used to think it was just me being too sensitive, but now I'm sure of it, {target}. These local kids are out of control,\" {initiator} says, seeking validation from {target}.",
            "\"Are you as fed up as I am with the local youths' behavior, {target}? It's like they have no respect for anyone in this neighborhood,\" {initiator} asks, seeking support.",
            "\"I can't take it anymore, {target}. These local kids are ruining the peaceful atmosphere of our community. We need to do something about it,\" {initiator} says, hoping for {target}'s agreement."
        ]
    },
    "mixer_social_CriticizeWooHooTechniques_targeted_mean_middleScore": {
        "pre_actions": [
            "{initiator} criticizes {target}'s sexual techniques.",
        ],
        "actions": [
            "\"{target}, I have to tell you this, but your technique in bed could use some improvement,\" {initiator} says hesitantly.",
            "\"I don't want to hurt your feelings, {target}, but I think we could explore some new techniques in bed,\" {initiator} suggests cautiously.",
            "\"{target}, I've been thinking about our intimacy lately, and I believe there's room for improvement when it comes to your technique,\" {initiator} says, trying to sound gentle.",
            "\"You know I care about you, {target}, but I think we should talk about how we can enhance our experience in bed,\" {initiator} says, hoping not to offend.",
            "\"{target}, I want our intimate moments to be amazing for both of us, so I think it's important that we discuss your technique,\" {initiator} says, attempting to be constructive.",
            "\"I feel like we could have a more satisfying experience in bed, {target}, if we work on your technique together,\" {initiator} says, offering support.",
            "\"{target}, I hope you don't take this the wrong way, but I think we should consider trying some new techniques in bed,\" {initiator} says, treading carefully.",
            "\"{target}, I've noticed that some of the things you do in bed might not be as pleasurable for both of us, and I think we should talk about it,\" {initiator} says, hoping for a positive response.",
            "\"I want to be honest with you, {target}. I think your technique in bed could use a little refinement, and I'm here to help,\" {initiator} says, offering a gentle smile.",
            "\"I think our love life could be even more amazing, {target}, if we work together to improve your technique in bed. What do you think?\" {initiator} asks with a supportive tone."
        ]
    },
    "mixer_social_DareToStreak_targeted_mischief_skills": {
        "pre_actions": [
            "{initiator} micheviously dares {target} to streak naked.",
        ],
        "actions": [
            "\"{target}, I bet you don't have the guts to do something crazy. How about streaking naked for a dare?\" {initiator} says with a mischievous grin.",
            "\"I've got a challenge for you, {target}. I dare you to streak naked and show the world your fearless side!\" {initiator} exclaims, a daring look in their eyes.",
            "\"Hey {target}, let's spice things up a bit! I dare you to streak naked. Are you brave enough?\" {initiator} asks, raising an eyebrow.",
            "\"Alright, {target}, it's time to test your limits! I dare you to run through this place naked. What do you say?\" {initiator} says, a smirk appearing on their face.",
            "\"{target}, I've got the ultimate dare for you. I challenge you to strip down and streak naked. Can you handle it?\" {initiator} questions, playfully.",
            "\"Let's see how daring you truly are, {target}. I dare you to streak naked right now!\" {initiator} says, laughing.",
            "\"Okay, {target}, I've got a dare that'll really push your boundaries. Are you up for streaking naked?\" {initiator} asks, a wicked smile on their lips.",
            "\"Hey {target}, since we're all about taking risks, how about I dare you to streak naked? Do you accept the challenge?\" {initiator} queries, gleefully.",
            "{initiator} looks at {target} and says, \"You think you're so daring, huh? Let's see if you've got what it takes to streak naked.\"",
            "\"Here's a dare for you, {target}. Prove your fearlessness by streaking naked right now!\" {initiator} says, their eyes full of excitement."
        ]
    },
    "mixer_social_ClaimCriminalMastermind_targeted_mischief_skills": {
        "pre_actions": [
            "{initiator} claims to be a criminal mastermind to {target}.",
        ],
        "actions": [
            "\"{target}, you might find this hard to believe, but I'm actually a criminal mastermind,\" {initiator} says with a sly grin.",
            "\"I've been keeping this from you, {target}, but I think it's time you know the truth: I'm a criminal mastermind,\" {initiator} confesses nonchalantly.",
            "\"{target}, have you ever wondered why I'm so good at strategy games? It's because I'm a criminal mastermind,\" {initiator} reveals with a hint of pride.",
            "\"I never thought I'd tell anyone, but I trust you, {target}. I've been orchestrating major heists for years as a criminal mastermind,\" {initiator} says, gauging {target}'s reaction.",
            "\"Listen, {target}, I need you to know something: I'm not just your average person. I'm a criminal mastermind,\" {initiator} says, trying to keep a straight face.",
            "\"{target}, have you ever noticed how I always seem to know what's going on? It's because I'm a criminal mastermind, and I've been keeping it a secret,\" {initiator} admits, with a smug smile.",
            "\"I've been living a double life, {target}. By day, I'm your friend, but at night, I'm a criminal mastermind,\" {initiator} says, dramatically.",
            "\"I can't keep this from you any longer, {target}. You deserve to know that I'm a criminal mastermind,\" {initiator} says, trying to gauge {target}'s reaction.",
            "\"I thought you should know, {target}, that I'm not just good at solving puzzles. I'm also a criminal mastermind,\" {initiator} says, with a mischievous glint in their eye.",
            "\"I have a confession, {target}. I'm not who you think I am. I'm actually a criminal mastermind,\" {initiator} says, waiting to see how {target} will react."
        ]
    },
    "mixer_social_DiscussColorTheory_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} discusses color theory with {target}."
        ],
        "actions": [
            "\"{target}, have you ever thought about how colors can affect our mood and emotions? Let's dive into color theory,\" {initiator} suggests with enthusiasm.",
            "\"Hey {target}, I came across an interesting article on color theory recently, want to discuss it together?\" {initiator} asks, excited to share their newfound knowledge.",
            "\"{target}, do you have a favorite color? I've been researching color theory and I'd love to hear your thoughts on it,\" {initiator} says, looking for a stimulating conversation.",
            "\"Did you know that different colors can have different psychological effects on us, {target}? Let's explore color theory together,\" {initiator} proposes, eager to delve into the subject.",
            "\"You know, {target}, I've always been fascinated by color theory and how color choices can impact design and art. What's your take on it?\" {initiator} inquires, curious about {target}'s opinion.",
            "\"Color theory is such a fascinating topic, {target}. Let's have a chat about how it plays a role in our everyday lives,\" {initiator} says, eager to engage {target} in a meaningful conversation.",
            "\"I've been studying color theory lately, {target}, and it's making me see the world in a whole new light. Want to discuss it together?\" {initiator} asks with genuine interest.",
            "\"Have you ever considered how color theory can influence our choices, {target}? I'd love to hear your thoughts on the subject,\" {initiator} says, seeking {target}'s perspective.",
            "\"{target}, I find color theory to be incredibly intriguing. Would you like to discuss its implications and how it affects our perception of the world?\" {initiator} asks, hoping for an engaging conversation.",
            "\"Color theory has been on my mind lately, {target}. I'm curious about its impact on our emotions and decision-making. Care to join me in a discussion about it?\" {initiator} invites, looking for an insightful exchange."
        ]
    },
    "mixer_social_AskAboutFood_targeted_Friendly_alwaysOn_Event": {
        "pre_actions": [
            "{initiator} asks {target} about their food.",
        ],
        "actions": [
            "\"{target}, how do you like the dish I prepared for us? I hope it's to your taste,\" {initiator} says, hoping for approval.",
            "\"{target}, I've been curious, what do you think about the food I made? Does it suit your taste buds?\" {initiator} asks with anticipation.",
            "\"Hey {target}, I tried a new recipe today. How do you like it? Be honest,\" {initiator} inquires, looking for feedback.",
            "\"So, {target}, I've been dying to know, what's your opinion on the meal? Enjoying it?\" {initiator} asks with a smile.",
            "\"{target}, I hope you're enjoying the food. Can I get your honest opinion on it?\" {initiator} questions, seeking validation.",
            "\"I put a lot of effort into this meal, {target}. I'd love to know if you like it,\" {initiator} says, looking for a genuine response.",
            "\"Did I get it right, {target}? How's the food? I'm always looking for ways to improve my cooking,\" {initiator} asks with a hint of pride.",
            "\"{target}, do you like the food I made? I tried to cater to your preferences,\" {initiator} inquires, eager for a positive reaction.",
            "\"I've been experimenting with new flavors, {target}. How's the dish? Are you enjoying it?\" {initiator} asks, excited for feedback.",
            "\"Your opinion means a lot to me, {target}. What do you think of the meal I prepared for us?\" {initiator} asks, with a hint of nervousness."
        ]
    },
    "mixer_social_ApologizeInBed_targeted_romance_transition": {
        "pre_actions": [
            '{initiator} apologizes for their poor performance as a romantic partner to {target} while in bed together.',
        ],
        "actions": [
            "\"{target}, I'm really sorry about last night's performance. I promise it's not usually like that,\" {initiator} says, looking embarrassed.",
            "\"I owe you an apology, {target}. I wasn't at my best last night, and I want you to know it doesn't define me,\" {initiator} says, trying to make amends.",
            "\"{target}, I wanted to talk about what happened last night. I wasn't on my game, and I'm sorry if I disappointed you,\" {initiator} confesses, their voice tinged with regret.",
            "\"I feel like I let you down, {target}. I'm sorry for not being able to satisfy you like I wanted to,\" {initiator} says apologetically.",
            "\"{target}, I need to say I'm sorry for my performance in bed last night. I hope you won't hold it against me,\" {initiator} pleads, looking concerned.",
            "\"Last night wasn't my best, {target}. I'm really sorry if I didn't meet your expectations,\" {initiator} admits, feeling vulnerable.",
            "\"I want to apologize, {target}. I wasn't myself last night, and I know I could have done better,\" {initiator} says, hoping for understanding.",
            "\"{target}, I feel terrible about how things went in bed last night. I promise I'll make it up to you,\" {initiator} says, determined to fix the situation.",
            "\"I'm really sorry, {target}. I don't know what happened last night, but I want to make it right,\" {initiator} says, looking for a chance at redemption.",
            "\"{target}, I need to apologize for last night. I wasn't at my best, and I hope we can move past it,\" {initiator} says, seeking forgiveness."
        ]
    },
    "mixer_social_AskToStayTheNight_targeted_romance_highScore": {
        "pre_actions": [
            "{initiator}, as a romantic partner, asks {target} if they want to stay the night.",
        ],
        "actions": [
            "\"{target}, I've been thinking... would you like to spend the night with me?\" {initiator} asks, a hint of a blush on their cheeks.",
            "\"With the stars above us, I can't help but think how magical it would be to spend the night together, {target}. What do you say?\" {initiator} says softly, gazing into {target}'s eyes.",
            "\"Life is full of beautiful moments, {target}, and I can't imagine anything more beautiful than spending tonight with you,\" {initiator} suggests, a hopeful smile playing on their lips.",
            "\"There's something about this night, {target}, that makes me want to spend every second of it with you. Would you like to stay with me?\" {initiator} asks, their heart racing.",
            "\"I've always dreamt of a night like this, {target}. A night where it's just the two of us, lost in each other's company. What do you think?\" {initiator} inquires, a tender look in their eyes.",
            "\"Tonight feels special, {target}. I can't quite put my finger on it, but I think it would be even more special if we spent it together. Would you like that?\" {initiator} asks, their voice filled with warmth.",
            "\"Can I be honest with you, {target}? I've been longing for a night like this, just you and me, away from the rest of the world. Would you like to stay with me?\" {initiator} confesses, their eyes searching {target}'s for an answer.",
            "\"Under the moonlight, everything seems so enchanting, {target}. I can't help but imagine how incredible it would be to share this night with you. What do you say?\" {initiator} proposes, a gentle smile on their face.",
            "\"I don't want this night to end, {target}. And I don't want to spend it with anyone else but you. Do you feel the same?\" {initiator} questions, their heart fluttering with anticipation.",
            "\"{target}, the thought of spending tonight with you fills me with a happiness I can't describe. Can I ask you to stay with me and make this night unforgettable?\" {initiator} pleads, their eyes shimmering with hope."
        ]
    },
    "mixer_social_AskToJustBeFriends_Targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} asks {target} to just be friends.",
        ],
        "actions": [
            "\"{target}, I've been thinking a lot lately, and I really value our friendship. I hope we can continue being just friends,\" {initiator} says sincerely.",
            "\"Can I talk to you about something, {target}? I think it's best for us to stay as friends, nothing more,\" {initiator} suggests gently.",
            "\"{target}, I have something on my mind. I believe our relationship works best when we're just friends, don't you think?\" {initiator} asks carefully.",
            "\"I hope you're not upset, {target}, but I've realized that our friendship is too important to me to risk complicating it with anything more,\" {initiator} confesses.",
            "\"You know, {target}, I've been contemplating our relationship, and I think we're better off as just friends. What do you think?\" {initiator} inquires.",
            "\"Can I be honest with you, {target}? I feel like our connection is strongest when we're just friends. I hope you feel the same way,\" {initiator} says, trying to gauge {target}'s reaction.",
            "\"I don't want to hurt your feelings, {target}, but I've been thinking that we should just be friends. I value our bond too much to risk losing it,\" {initiator} expresses genuinely.",
            "\"{target}, I think we need to talk. Personally, I feel like we should remain friends and not pursue anything further. I hope you understand,\" {initiator} says delicately.",
            "\"I've done a lot of soul-searching, {target}, and I think the best thing for both of us is to just be friends. I hope you can accept that,\" {initiator} shares honestly.",
            "\"Please don't take this the wrong way, {target}, but I've come to the conclusion that we're better as friends. I hope we can maintain our amazing friendship,\" {initiator} says, hoping for understanding."
        ]
    },
    "mixer_social_PickupLine_targeted_romance_alwaysOn": {
        "pre_actions": [
            "{initiator} uses a pick-up line on {target}.",
        ],
        "actions": [
            "\"{target}, are you a magician? Because whenever I look at you, everyone else disappears,\" {initiator} says with a playful smile.",
            "\"Is your name Google, {target}? Because you have everything I've been searching for,\" {initiator} says, trying to impress {target}.",
            "\"{target}, if you were a vegetable, you'd be a 'cute-cumber',\" {initiator} says, attempting to be charming.",
            "\"Do you have a map, {target}? Because I just got lost in your eyes,\" {initiator} says, gazing into {target}'s eyes.",
            "\"Can I follow you home, {target}? Cause my parents always told me to follow my dreams,\" {initiator} says, hoping for a positive reaction.",
            "\"Are you made of copper and tellurium, {target}? Because you're Cu-Te,\" {initiator} says, trying to be clever and flirtatious.",
            "\"Did it hurt when you fell from heaven, {target}?\" {initiator} asks, flashing a charming smile.",
            "\"Excuse me, {target}, but I think you dropped something: my jaw,\" {initiator} says, attempting to flatter {target}.",
            "\"If you were a fruit, {target}, you'd be a fine-apple,\" {initiator} says, hoping to catch {target}'s attention.",
            "\"{target}, I must be a snowflake, because I've fallen for you,\" {initiator} says, trying to be both romantic and witty."
        ]
    },
    "mixer_social_SmoothRecovery_targeted_romance_alwaysOn_topic": {
        "pre_actions": [
            "After a slip-up with {target}, {initiator} deftly makes a smooth recovery."
        ], 
        "actions": [
            "\"{target}, I must have tripped over my words because I'm falling for you,\" {initiator} says with a wink, trying to recover from their slipup.",
            "\"I guess I got tongue-tied because you're just too stunning, {target},\" {initiator} says, attempting to cover up their flub.",
            "\"Well, that didn't come out right, but what I meant to say was, you look amazing tonight, {target},\" {initiator} says with a charming smile.",
            "\"I promise I'm usually smoother than that, {target}, but you just have me a little flustered,\" {initiator} admits, hoping to recover from their mistake.",
            "\"Wow, I didn't expect to mess that up, but I guess you have that effect on me, {target},\" {initiator} says, trying to play off their slipup.",
            "\"Let me try that again, {target}. You're so beautiful, you make me forget my lines,\" {initiator} says, attempting to regain their composure.",
            "\"Oops, that was a bit clumsy of me, wasn't it? But I guess I'm just clumsy in love, {target},\" {initiator} says, laughing off their slipup.",
            "\"Sometimes my words get twisted, but they're always straight from the heart, {target},\" {initiator} says, attempting to recover smoothly.",
            "\"Well, that was embarrassing, but you know what they say: 'you always mess up when you're in front of someone you like,' right, {target}?\" {initiator} says, trying to save face.",
            "\"I can't believe I messed that up, {target}, but I suppose it's all part of my charm,\" {initiator} says, attempting to turn their slipup into a flirty moment."
        ]
    },
    "mixer_social_StartPreposterousRumor_group_mischief_skills": {
        "pre_actions": [
            "{initiator} starts a preposterous rumor with {target}."
        ],
        "actions": [
            "\"{target}, you won't believe the crazy rumor I heard today. You've got to hear this!\" {initiator} says, grinning mischievously.",
            "\"I came across this wild piece of gossip, {target}, and I just can't keep it to myself,\" {initiator} says with a smirk.",
            "\"Hey, {target}, have you heard the latest rumor flying around? It's completely outrageous!\" {initiator} exclaims, eager to share.",
            "\"Alright, {target}, brace yourself for the most absurd rumor I've ever heard. I'm dying to see your reaction,\" {initiator} says, chuckling.",
            "\"Oh, {target}, I've got some juicy gossip for you! You're not going to believe this one,\" {initiator} says, winking.",
            "\"I heard something so unbelievable today, {target}, I just have to share it with you. Are you ready for this?\" {initiator} asks, excitedly.",
            "\"Prepare to be amazed, {target}. I stumbled upon a rumor that's so ridiculous, I can't help but laugh,\" {initiator} says, grinning from ear to ear.",
            "\"{target}, if you're in the mood for a good laugh, let me tell you about this crazy rumor I heard. You're going to love it,\" {initiator} says, trying to contain their laughter.",
            "\"Okay, {target}, get ready for the most preposterous piece of gossip I've ever come across. Trust me, it's a doozy,\" {initiator} says, shaking their head in disbelief.",
            "\"Hey, {target}, I heard a rumor today that's so bizarre, I couldn't wait to share it with you. I hope you're sitting down for this one,\" {initiator} says with a teasing smile."
        ]
    },
    "sim_Kiss_QuickSocial": {
        "actions": [
            "{initiator} looks deeply into {target}'s eyes, leans in, and gently plants a kiss on their lips.",
            "Without any warning, {initiator} takes {target}'s face in their hands and softly kisses them.",
            "Feeling a surge of emotion, {initiator} impulsively leans forward and kisses {target} passionately.",
            "In an intimate moment, {initiator} tenderly moves closer to {target} and presses their lips together.",
            "As {initiator} and {target} share a heartfelt conversation, {initiator} leans in and gives {target} a loving kiss.",
            "{initiator} suddenly takes {target}'s hand, pulls them close, and surprises them with a kiss.",
            "Overwhelmed by emotions, {initiator} closes the distance between them and kisses {target} with all their heart.",
            "With a soft smile, {initiator} cups {target}'s cheek and gently brings their lips together.",
            "Feeling a strong connection, {initiator} can no longer resist the temptation and kisses {target} passionately.",
            "As they gaze into each other's eyes, {initiator} tilts their head, leans in, and kisses {target} tenderly."
        ]
    },
    "mixer_social_SexyPose_targeted_romance_emotionSpecific": {
        "actions": [
            "\"{target}, I've been practicing this pose just for you. Are you ready for it?\" {initiator} says with a sly wink, before striking the pose.",
            "\"Hey {target}, I've got a surprise for you. Check out this pose,\" {initiator} says, confidently striking a seductive pose.",
            "Feeling playful, {initiator} decides to surprise {target} with a sexy pose, hoping to make them blush.",
            "{initiator} leans against the wall, striking a sultry pose for {target}, curious to see their reaction.",
            "Wanting to spice things up, {initiator} strikes a sexy pose in front of {target}, raising an eyebrow suggestively.",
            "{initiator} looks {target} in the eye, flashing a flirtatious smile before striking a seductive pose that leaves them speechless.",
            "\"{target}, I bet you didn't expect this,\" {initiator} says playfully, before surprising them with a sexy pose.",
            "Feeling confident, {initiator} decides to strike a sexy pose in front of {target}, hoping to get a positive reaction.",
            "{initiator} catches {target}'s eye and, with a mischievous grin, strikes a sultry pose just for them, waiting to see their response."
        ]
    },
    "mixer_social_SitIntimate_Kiss_targeted_romance_emotionSpecific": {
        "actions": [
            "{initiator} leans in closer to {target}, their eyes locked, and gently places a tender kiss on {target}'s lips.",
            "Without a word, {initiator} takes {target}'s hand, pulls them in close, and surprises {target} with a soft, unexpected kiss.",
            "With a sudden surge of courage, {initiator} moves closer to {target} and lovingly presses their lips against {target}'s.",
            "As they sit together, {initiator} can't help but feel the magnetic pull towards {target}, and finally gives in to the urge to plant a sweet kiss on {target}'s lips.",
            "{initiator}'s heart races as they muster the bravery to lean in and gently place a kiss on {target}'s lips, hoping it will be well received.",
            "In a moment of pure emotion, {initiator} leans towards {target} and lets their lips meet in a warm, gentle kiss.",
            "With their faces just inches apart, {initiator} can no longer resist the temptation to press their lips against {target}'s in a tender, passionate kiss.",
            "As they sit side by side, {initiator} gazes deeply into {target}'s eyes and decides to softly kiss {target}.",
            "Feeling a strong connection to {target}, {initiator} leans in and shares a tender, loving kiss.",
            "{initiator}, overwhelmed by their feelings for {target}, gently cups {target}'s face in their hands and slowly moves in for a heartfelt, lingering kiss."
        ]
    },
    "mixer_social_PassionateKiss_targeted_romance_emotionSpecific": {
        "actions": [
            "{initiator} looks deeply into {target}'s eyes, leans in, and plants a passionate kiss on their lips, taking them by surprise.",
            "Without saying a word, {initiator} reaches out, gently cups {target}'s face, and kisses them passionately, leaving them both breathless.",
            "With a sudden surge of emotion, {initiator} pulls {target} close and kisses them deeply, their hearts racing together.",
            "{initiator} takes a step closer to {target}, brings their lips together in a passionate embrace, and kisses them like they've never been kissed before.",
            "Overwhelmed with feelings for {target}, {initiator} tenderly places a hand on their cheek and kisses them with a passion that sends shivers down their spine.",
            "As {initiator} gazes into {target}'s eyes, they can't resist any longer and pull {target} into a passionate, electrifying kiss.",
            "In a moment of unspoken desire, {initiator} leans in and gives {target} the most passionate, breathtaking kiss they've ever experienced.",
            "Unable to contain their feelings any longer, {initiator} sweeps {target} off their feet and delivers a soul-stirring, passionate kiss.",
            "{initiator} gently grabs {target} by the hand, draws them near, and kisses them with a passion that leaves them both weak in the knees.",
            "Feeling a magnetic pull toward each other, {initiator} and {target} come together in a passionate, unforgettable kiss that leaves them both wanting more."
        ]
    },
    "mixer_social_FirstKiss_targeted_romance_STC": {
        "actions": [
            "{initiator} leans in closer, their eyes locked with {target}'s, and gently presses their lips together in a tender first kiss.",
            "With a sudden surge of courage, {initiator} takes {target}'s hand, looks deeply into their eyes, and softly plants a kiss on their lips.",
            "As their faces draw near, {initiator} hesitates for a moment, then closes the distance, capturing {target}'s lips in a sweet, memorable first kiss.",
            "{initiator} gazes into {target}'s eyes, leans in, and shares a gentle, loving first kiss.",
            "{initiator} takes a deep breath, draws {target} closer, and with a mix of excitement and nervousness, kisses them for the first time.",
            "While laughing together, {initiator} suddenly stops and, with a tender look, leans in to give {target} a soft, unexpected first kiss.",
            "Surrounded by a romantic ambiance, {initiator} reaches out, cradles {target}'s face, and plants a slow, passionate first kiss on their lips.",
            "In the midst of an emotional conversation, {initiator} tenderly touches {target}'s face and leans in to share a heartfelt first kiss.",
            "{initiator} pulls {target} close, and shares a warm, comforting first kiss.",
            "{initiator} gently grabs {target}'s arm, pulls them closer, and surprises them with a soft, lingering first kiss."
        ]
    },
    "mixer_social_BlowAKiss_targeted_romance_highScore": {
        "pre_actions": [
            "{initiator} playfully blows a kiss towards {target} as a romantic gesture.",
        ],
        "actions": [
            "\"{target}, this one's for you,\" {initiator} says playfully, blowing a kiss in {target}'s direction.",
            "With a sly grin, {initiator} catches {target}'s eye and gently sends a blown kiss their way.",
            "{initiator} leans in close to {target} and whispers, \"Watch closely,\" before pulling away and blowing a delicate kiss in their direction.",
            "{initiator} looks at {target} from across the room, and with a mischievous smile, they pucker their lips and blow a subtle kiss.",
            "With a coy smile, {initiator} locks eyes with {target} and playfully blows a kiss, hoping to catch their attention.",
            "{initiator} gently taps {target}'s shoulder to get their attention, and once their eyes meet, {initiator} blows a soft, teasing kiss.",
            "{initiator} pretends to pluck something from the air, and as they present it to {target}, they blow a tender kiss their way.",
            "{initiator} catches {target} by surprise, leaning in as if to whisper a secret, but instead, they blow a warm kiss near {target}'s ear.",
        ]
    },
    "mixer_social_Embrace_targeted_romance_middleScore_STC": {
        "actions": [
            "\"{target}, I can't help it any longer. I need to hold you close,\" {initiator} says, pulling {target} into a tender embrace.",
            "\"Whenever I'm near you, {target}, all I want to do is wrap my arms around you,\" {initiator} admits, finally giving in to their feelings.",
            "\"Come here, {target}. I want you to feel how much you mean to me,\" {initiator} says, enveloping {target} in a heartfelt hug.",
            "\"{target}, there's something so special about you that I can't resist the urge to hold you close,\" {initiator} confesses, drawing {target} into their arms.",
            "\"Being with you, {target}, makes me feel like I'm home. Let me hold you,\" {initiator} says, gently embracing {target}.",
            "\"I've been longing to do this for so long, {target}. Let me hold you close and show you my love,\" {initiator} says, wrapping their arms around {target}.",
            "\"I can't keep my feelings for you hidden any longer, {target}. I need to hold you,\" {initiator} says, pulling {target} into a warm embrace.",
            "\"Every time I see you, {target}, my heart aches to be close to you. Let me embrace you,\" {initiator} says, holding {target} tightly.",
            "\"When I'm holding you close, {target}, everything else seems to disappear. Let's get lost in this moment,\" {initiator} says, embracing {target} passionately.",
            "\"I've never felt this way about anyone, {target}. I want to show you how much you mean to me,\" {initiator} says, pulling {target} into a loving embrace."
        ]
    },
    "mixer_social_WooHoo_targeted_romance_transition": {
        "actions": [
            "\"{target}, I've been thinking about this for so long. Let's go to the bedroom and share something special together,\" {initiator} whispers gently.",
            "\"With every touch, I feel more connected to you, {target}. Let's take this to the bed and deepen our connection,\" {initiator} suggests, their eyes filled with desire.",
            "\"I can't resist the way you make me feel, {target}. Let's go to the bedroom and explore our passion together,\" {initiator} says, their voice soft and sultry.",
            "\"Being with you like this is intoxicating, {target}. I want to make love to you in the most intimate way. Let's go to the bed,\" {initiator} murmurs, their gaze locked on {target}'s.",
            "\"I've never felt a connection like this before, {target}. Let's move to the bedroom and make love,\" {initiator} proposes, their voice filled with longing.",
            "\"Your touch sends shivers down my spine, {target}. I want to take you to the bed and make love to you,\" {initiator} confesses, their eyes filled with lust.",
            "\"I can't help but think about how amazing it would feel to make love to you, {target}. Let's go to the bedroom and find out,\" {initiator} suggests, a seductive smile on their lips.",
            "\"Every time I'm near you, {target}, I feel an overwhelming desire to be even closer. Let's take this to the bedroom and share our love,\" {initiator} says, gently taking {target}'s hand.",
            "\"The chemistry between us is undeniable, {target}. I want to take you to the bed and make love to you,\" {initiator} says, their voice husky and filled with passion.",
            "\"Let's make tonight unforgettable, {target}. Come with me to the bedroom, and let's make love,\" {initiator} whispers softly, their eyes reflecting their burning desire."
        ]
    },
    "mixer_social_SitIntimate_AskForMassage_targeted_romance_highScore": {
        "actions": [
            "\"{target}, my muscles are feeling so tense. Do you think you could give me a massage?\" {initiator} asks, hoping for some relief.",
            "\"Hey {target}, my back has been killing me lately. Could you help me out with a massage?\" {initiator} inquires, wincing in pain.",
            "\"{target}, I know it's a strange request, but would you mind giving me a massage? My shoulders are really sore,\" {initiator} asks hesitantly.",
            "\"I'm feeling really tense, {target}, and I could use a good massage. Would you be willing to help me out?\" {initiator} says, rubbing their neck.",
            "\"I don't usually ask for such favors, {target}, but my back is in desperate need of a massage. Could you lend a hand?\" {initiator} pleads, looking uncomfortable.",
            "\"Hey {target}, I'm in pain and could really use a massage. Do you think you could help me out?\" {initiator} asks, trying to hide their discomfort.",
            "\"{target}, I hate to impose, but I'm in serious need of a massage. Would you mind helping me out?\" {initiator} requests, looking hopeful.",
            "\"I've never asked anyone for this before, {target}, but my muscles are so tense that I can't take it anymore. Could you give me a massage?\" {initiator} says, feeling a bit embarrassed.",
            "\"Forgive me for asking, {target}, but I could really use a massage right now. Would you mind?\" {initiator} queries, attempting to sound casual.",
            "\"Could you do me a huge favor, {target}? I'm in dire need of a massage and I'd really appreciate your help,\" {initiator} says, wincing as they try to stretch their sore muscles."
        ]
    },
    "mixer_social_BeEnticing_targeted_romance_emotionSpecific": {
        "pre_actions": [
            "{initiator}, as a romantic partner, acts enticing towards {target}.",
        ],
        "actions": [
            "\"{target}, have you ever noticed how the stars seem to align when we're together?\" {initiator} says, gently brushing their hand against {target}'s.",
            "\"As we stand here together, {target}, I can't help but feel like this moment was meant for us,\" {initiator} whispers, looking deeply into {target}'s eyes.",
            "\"{target}, the warmth of your presence makes me feel like I'm wrapped in a blanket of love. Can you feel it too?\" {initiator} asks, their voice soft and tender.",
            "\"With every beat of my heart, {target}, I find myself drawn closer to you. Do you feel the same magnetic pull?\" {initiator} inquires, a subtle smile playing on their lips.",
            "\"Every time our eyes meet, {target}, it feels like a spark ignites between us. Can you see the fire in my eyes?\" {initiator} asks, their gaze intense and passionate.",
            "\"The way the light dances across your face, {target}, makes my heart skip a beat. Do you notice the way I look at you?\" {initiator} says, a hint of vulnerability in their voice.",
            "\"{target}, when I'm near you, it feels like the world stops spinning, and it's just you and me. Do you sense that too?\" {initiator} asks, their voice filled with longing.",
            "\"Your laughter is like a melody that I can't get out of my head, {target}. Does my presence bring you the same joy?\" {initiator} wonders, their voice sweet and sincere.",
            "\"When I think about the future, {target}, I can't help but picture us together. Do my dreams align with yours?\" {initiator} asks, their eyes searching {target}'s for an answer.",
            "\"{target}, when I'm with you, it feels like we're two pieces of a puzzle that fit perfectly together. Can you feel the connection?\" {initiator} says, gently taking {target}'s hand."
        ]
    },
    "mixer_social_ConfessAttraction_targeted_romance_middleScore": {
        "pre_actions": [
            "{initiator} confesses their romantic attraction for {target}.",
        ],
        "actions": [
            "\"{target}, I've been struggling with these feelings for a while, but I can't hold it in any longer. I'm attracted to you,\" {initiator} confesses nervously.",
            "\"Ever since we met, I've felt this undeniable connection with you, {target}. I think I'm falling for you,\" {initiator} says, looking into {target}'s eyes.",
            "\"{target}, I've tried to ignore it, but my heart races whenever I'm around you. I think I have feelings for you,\" {initiator} admits, blushing.",
            "\"I never thought I'd say this, but I can't help myself, {target}. I'm attracted to you, and I need you to know,\" {initiator} says, taking a deep breath.",
            "\"Every time I see you, {target}, my heart skips a beat. I think I'm developing feelings for you, and I can't hide it any longer,\" {initiator} says, looking vulnerable.",
            "\"Being around you, {target}, makes me feel so alive. I must admit, I've developed feelings for you,\" {initiator} confesses, their voice trembling.",
            "\"{target}, I can't keep pretending that we're just friends. I'm starting to fall for you, and I needed you to know,\" {initiator} says, looking anxious.",
            "\"Can I be honest, {target}? I've been attracted to you for quite some time, and I think it's time I let you know,\" {initiator} admits, hesitatingly.",
            "\"{target}, I've tried to fight it, but I can't deny my feelings any longer. I'm attracted to you, and I hope you feel the same,\" {initiator} says, their voice filled with hope.",
            "\"I didn't plan for this, {target}, but I can't help it. I'm falling for you, and I needed you to know,\" {initiator} says, their heart pounding with anticipation."
        ]
    },
    "mixer_social_FightSupervillain_targeted_mean_career": {
        "pre_actions": [
            "{initiator} fights {target}, who is a super villain."
        ],
        "actions": [
            "\"{target}, your reign of terror ends here and now!\" {initiator} shouts, fists clenched and ready to fight.",
            "\"{target}, I've had enough of your evil ways. It's time to put a stop to this madness,\" {initiator} says, taking a determined stance.",
            "\"You've caused enough suffering, {target}. I won't let you hurt anyone else,\" {initiator} says, stepping forward to confront the villain.",
            "{initiator} faces {target} and proclaims, \"Your time is up, {target}. I won't let you continue down this path of destruction.\"",
            "\"Enough is enough, {target}. I can't stand by and watch you harm innocent people any longer,\" {initiator} says, readying themselves for battle.",
            "\"Your evil deeds come to an end today, {target}. I won't allow you to continue hurting others,\" {initiator} says bravely, preparing for the fight.",
            "\"{target}, I've been waiting for the day I could finally put an end to your wickedness. That day has come,\" {initiator} announces, standing firm.",
            "\"I'm not afraid of you anymore, {target}. I will fight to protect those you've threatened,\" {initiator} says, courage in their eyes.",
            "\"Your power has been used for evil for far too long, {target}. I'm here to put a stop to your tyranny,\" {initiator} says with determination.",
            "\"I've watched you hurt too many people, {target}. It's time for you to face some justice,\" {initiator} says, standing tall and ready to fight."
        ]
    },
    "mixer_social_Pickpocket_targeted_mischief_career_household": { #J: I Need to see animation in the game before context - current actions sound more like robbing. Also, what is the distinction between 'career_household" and "career?" (3020 and 3034)
        "actions": [
            "{initiator} slips into {target}'s house, their heart pounding, hoping not to get caught as they take the valuable object.",
            "Feeling a rush of adrenaline, {initiator} quickly grabs the item from {target}'s home, hoping their absence goes unnoticed.",
            "As {target} steps out of the room, {initiator} seizes the opportunity to swipe the treasured item from their home.",
            "Waiting for the perfect moment, {initiator} swipes the precious item from {target}'s house, knowing the consequences if caught.",
            "While visiting {target}'s home, {initiator} can't resist the urge to steal something, acting quickly and discreetly.",
            "{initiator} feels a mix of excitement and guilt as they take the valuable object from {target}'s house, praying they won't be discovered.",
            "In a moment of weakness, {initiator} succumbs to temptation and steals from {target}'s home, hoping to evade detection.",
            "{initiator} carefully plans their move, waiting until {target} is preoccupied before stealing the item from their home.",
            "Driven by need and desperation, {initiator} steals something from {target}'s house, hoping their friendship can withstand the betrayal.",
            "With a sense of urgency, {initiator} swipes the valuable item from {target}'s home, knowing the risks involved but unable to resist the temptation."
        ]
    },
    "mixer_social_Pickpocket_targeted_mischief_career": {
        "actions": [
            "{initiator} slyly approaches {target}, pretending to bump into them while skillfully slipping their hand into {target}'s pocket.",
            "As {target} is distracted by a street performer, {initiator} sees an opportunity and discreetly reaches for {target}'s pocket.",
            "{initiator} pretends to be a fan asking {target} for an autograph, using the distraction to pick {target}'s pocket without them realizing.",
            "While {target} is engrossed in conversation, {initiator} carefully inches closer and slips their hand into {target}'s pocket, hoping to go unnoticed.",
            "{initiator}, disguised as a waiter, approaches {target} with a tray of drinks, using the distraction to pick {target}'s pocket.",
            "In the chaos of the crowded marketplace, {initiator} takes advantage of the situation and expertly picks {target}'s pocket.",
            "As {target} tries to figure out which way to go, {initiator} approaches them under the guise of offering help, seizing the moment to pick {target}'s pocket.",
            "{initiator} bumps into {target} in a crowded subway, using the close proximity to pick {target}'s pocket without raising suspicion.",
            "While {target} is busy admiring a breathtaking view, {initiator} quietly approaches them from behind and picks their pocket.",
            "{initiator} pretends to trip and fall onto {target}, and in the confusion, manages to pick {target}'s pocket without them noticing."
        ]
    },
    "mixer_social_GiveFakeInvestmentTips_Targeted_Mischief_AlwaysOn_career": {
        "pre_actions": [
            "{initiator} gives fake investment tips to {target}."
        ],
        "actions": [
            "\"{target}, I have a hot tip for you. This investment is going to skyrocket, trust me,\" {initiator} says with a grin.",
            "\"Hey {target}, I overheard some people discussing a surefire investment opportunity. You should definitely get in on it,\" {initiator} suggests, feigning excitement.",
            "\"Listen, {target}, I know a guy who knows a guy, and he's telling me this is the investment of the century. Don't miss out,\" {initiator} says, trying to sound convincing.",
            "\"{target}, I have some insider information on a killer investment. I probably shouldn't be sharing it, but I think you'll want in on this,\" {initiator} says, acting secretive.",
            "\"I just came across an amazing investment opportunity, {target}. You'd be crazy not to jump on this one,\" {initiator} says, attempting to sound enthusiastic.",
            "\"Trust me, {target}, this is the kind of investment that only comes around once in a lifetime. You don't want to miss it,\" {initiator} insists, hoping to persuade {target}.",
            "\"{target}, I've been doing some research and found a hidden gem of an investment. You should really consider it,\" {initiator} says, trying to sound knowledgeable.",
            "\"Hey {target}, I've stumbled upon a surefire moneymaker, and I thought I'd share the wealth. You'll thank me later,\" {initiator} says, eager to deceive {target}.",
            "\"{target}, I don't usually give out investment advice, but this one's too good not to share. You'll see the returns skyrocket in no time,\" {initiator} promises, hiding their true intentions.",
            "\"I've got a little secret, {target}. I know about an investment that's about to explode in value. You should get in now while you still can,\" {initiator} says, trying to sound helpful while leading {target} astray."
        ]
    },
    "mixer_social_BragAboutSkillz_targeted_Friendly_alwaysOn_career": {
        "pre_actions": [
            "{initiator} boasts to {target} about his abilities and talents.",
        ],
        "actions": [
            "\"{target}, you won't believe the kind of work I can do. I'm practically a wizard at my job,\" {initiator} says, grinning proudly.",
            "\"Have I ever told you about the time I saved my company from total disaster? I'm not saying I'm a hero, but I kind of am,\" {initiator} boasts to {target}.",
            "\"{target}, my job skills are unparalleled. I'm always the go-to person when something needs to get done right,\" {initiator} says, puffing their chest out.",
            "\"You know, {target}, I've been told I'm the best in my field. It's hard not to let it go to my head,\" {initiator} says, smirking confidently.",
            "\"I don't like to brag, {target}, but my job skills are truly unmatched. No one can handle the pressure like I can,\" {initiator} claims, with a hint of arrogance.",
            "\"{target}, have I ever mentioned that my boss thinks I'm a genius? It's true, they're always praising my incredible job skills,\" {initiator} says, clearly enjoying the attention.",
            "\"Let me tell you, {target}, my job skills are so impressive that my coworkers are constantly asking for my help. It's almost exhausting being this good,\" {initiator} says with a cheeky grin.",
            "\"I'm not one to brag, {target}, but I'm kind of a legend at work. My skills are just that extraordinary,\" {initiator} states, trying to sound humble.",
            "\"Did you know, {target}, that I once completed a project in half the time it usually takes? My job skills are truly something to be admired,\" {initiator} declares, basking in the glory.",
            "\"Sometimes, {target}, I can't believe how talented I am at my job. It's like everything I touch turns to gold,\" {initiator} says, with an air of self-satisfaction."
        ]
    },
    "mixer_social_TranquilizingHandshake_targeted_mischief_alwaysOn_career": {
        "pre_actions": [
            "{initiator} uses a special device as a secret agent on {target}, once they shake hands it knocks {target} unconcious.",
        ],
        "actions": [
            "{initiator} extends their hand for a handshake, their special device hidden from view.",
            "\"{target}, I've been looking forward to this moment,\" {initiator} says, smiling as they reach out to shake {target}'s hand, the device discreetly concealed.",
            "\"Hey, {target}, great to see you,\" {initiator} says, subtly activating the device as they extend their hand for a handshake.",
            "{initiator} offers a friendly handshake to {target}, carefully concealing the secret agent device that would soon take effect.",
            "\"{target}! Let's shake on it,\" {initiator} says, preparing to use the special device hidden in their hand.",
        ]
    },
    "mixer_social_BragAboutStartup_targeted_Friendly_alwaysOn_career": {
        "pre_actions": [
            "{initiator} brags to {target} about their startup company.",
        ],
        "actions": [
            "\"{target}, you won't believe the success of my startup! We've been growing exponentially,\" {initiator} boasts with a grin.",
            "\"Hey, {target}, have I told you about my amazing startup? It's really taking off and everyone's talking about it,\" {initiator} says proudly.",
            "\"{target}, did you know that my startup has been featured in major publications? I guess you could say we're kind of a big deal,\" {initiator} smirks.",
            "\"I can't help but brag a little, {target}. My startup is absolutely killing it in the industry right now,\" {initiator} says with a confident smile.",
            "\"Guess what, {target}? My startup just secured a huge investment! I knew we were destined for greatness,\" {initiator} exclaims, beaming with pride.",
            "\"You know, {target}, not everyone can create a successful startup like I have. It takes talent and determination,\" {initiator} says, puffing out their chest.",
            "\"{target}, my startup's success is beyond even my wildest dreams! We're really making an impact out there,\" {initiator} brags excitedly.",
            "\"Hey, {target}, I don't mean to brag, but my startup is really changing the game. We're revolutionizing the industry,\" {initiator} says, unable to contain their excitement.",
            "\"I'm so proud of my startup, {target}. We've accomplished so much in such a short time, and it's only the beginning,\" {initiator} gushes with enthusiasm.",
            "\"Sometimes I can't believe how successful my startup has become, {target}. I guess I've just got a knack for this kind of thing,\" {initiator} says with a self-satisfied smile."
        ]
    },
    "mixer_social_GossipAboutOfficeRomance_Targeted_Friendly_AlwaysOn_Career": {
        "pre_actions": [
            "{initiator} gossips about the office romance with {target}, their coworker."
        ],
        "actions": [
            "\"{target}, have you heard about the latest office romance? It's quite the scandal!\" {initiator} says with a mischievous grin.",
            "\"Hey {target}, did you catch wind of the new couple in the office? I never saw that one coming!\" {initiator} says, raising their eyebrows.",
            "\"Can you believe who's dating who in the office, {target}? I was shocked when I found out!\" {initiator} exclaims, eager to share the gossip.",
            "\"Psst, {target}, there's a juicy piece of gossip floating around the office. Want to know who's involved in the latest office romance?\" {initiator} whispers, leaning in closer.",
            "\"Guess what, {target}? I have some insider info on the recent office lovebirds. Care to take a guess?\" {initiator} asks, a playful smile on their face.",
            "\"{target}, you won't believe who's been sneaking around together lately. Let's just say love is in the air at the office!\" {initiator} says with a wink.",
            "\"Have you been keeping up with the office romance news, {target}? There's a new couple that's got everyone talking!\" {initiator} says excitedly.",
            "\"So, {target}, I heard through the grapevine that there's a new office romance brewing. Want to know who's involved?\" {initiator} says, looking eager to spill the beans.",
            "\"Word on the street is there's a new couple in the office. Can you guess who, {target}?\" {initiator} asks with a sly smile.",
            "\"{target}, I can't keep this to myself any longer. There's a new office romance, and it's the talk of the town! You'll never guess who's involved!\" {initiator} says, barely able to contain their excitement."
        ]
    },
    "mixer_social_PointOutConstellations_targeted_Friendly_alwaysOn_careers": {
        "pre_actions": [
            "{initiator} points out constellations to {target}." #J: What career? Need to check.
        ],
        "actions": [
            "\"{target}, do you see that group of stars over there?\" {initiator} asks, pointing up at the night sky. \"That's the constellation I wanted to show you.\"",
            "\"Hey {target}, have a look at this,\" {initiator} says, gesturing toward the sky. \"I just spotted Orion's Belt.\"",
            "\"Look up, {target}. You see those stars in a line? That's the Big Dipper,\" {initiator} explains, pointing out the well-known constellation.",
            "\"{target}, let me show you something fascinating,\" {initiator} says, guiding {target}'s gaze toward the stars. \"Right there is the constellation Cassiopeia.\"",
            "\"Ever noticed that group of stars, {target}?\" {initiator} asks, pointing to the sky. \"That's Scorpius, one of my favorite constellations.\"",
            "\"Come here, {target}. I want to show you something,\" {initiator} says, leading {target} to a spot with a clear view of the sky. \"You see that constellation up there? That's Ursa Major.\"",
            "\"Check this out, {target}!\" {initiator} exclaims, grabbing {target}'s attention. \"That beautifully shaped constellation over there is called Lyra.\"",
            "\"Hey {target}, have you ever seen the Pleiades?\" {initiator} asks, pointing to the cluster of stars in the sky.",
            "\"{target}, look up there at that unique formation of stars. That's the constellation of Aquarius,\" {initiator} says, sharing their knowledge of the night sky.",
            "\"Isn't it amazing, {target}? Right up there is the constellation Leo,\" {initiator} explains, pointing out the group of stars resembling a lion."
        ]
    },
    "mixer_social_BragAboutJobTitle_Targeted_Friendly_AlwaysOn_career": {
        "pre_actions": [
            "{initiator} brags to {target} about their job title.",
        ],
        "actions": [
            "\"{target}, you know, I just can't help but feel proud of my job. I mean, not everyone gets to be in my position,\" {initiator} says, grinning confidently.",
            "\"I don't mean to boast, {target}, but my job is pretty amazing. I'm kind of a big deal in my field,\" {initiator} shares with a smug smile.",
            "\"Hey, {target}, did I ever tell you about my incredible job? I'm kind of a rock star at work,\" {initiator} brags, puffing out their chest.",
            "\"{target}, I just have to mention how awesome my job is. I'm in charge of some really important projects,\" {initiator} says, trying to impress.",
            "\"Sometimes I can't believe my luck, {target}, I have such a fantastic job. It's like I'm living the dream,\" {initiator} shares, their eyes shining with pride.",
            "\"Have I ever told you about my job title, {target}? It's pretty impressive, if I do say so myself,\" {initiator} says, winking.",
            "\"You know, {target}, not everyone can say they have a job like mine. I'm really proud of my accomplishments,\" {initiator} brags with a grin.",
            "\"I don't mean to toot my own horn, {target}, but my job is pretty high-profile. People really respect me at work,\" {initiator} says, a hint of arrogance in their voice.",
            "\"{target}, I can't help but feel a sense of pride when I tell people about my job. It's a pretty big deal, you know,\" {initiator} shares with a smirk.",
            "\"Every time I walk into my office, {target}, I can't help but feel a sense of accomplishment. My job is truly something to be proud of,\" {initiator} says, basking in their own success."
        ]
    },
    "mixer_social_InterviewForStory_targeted_Friendly_alwaysOn_career": {
        "actions": [
            "\"{target}, your story has been making headlines recently, and I'd like to get your perspective for our readers. Are you willing to share your experience?\" {initiator} asks.",
            "\"Thank you for taking the time to speak with me today, {target}. Our audience is very interested in getting to know more about you and your journey,\" {initiator} says, starting the interview.",
            "\"{target}, I've been following your story closely, and I'm excited for the opportunity to interview you. Let's start by discussing the events that led up to this moment,\" {initiator} suggests.",
            "\"As a reporter, I've come across many fascinating stories, but yours has particularly caught my attention, {target}. I'm eager to learn more about your experiences,\" {initiator} says, preparing their questions.",
            "\"Good morning, {target}. I'm {initiator}, a reporter for the local newspaper. I've been assigned to cover your story, and I'd be grateful for the chance to interview you,\" {initiator} introduces themselves.",
            "\"Hello {target}, I'm {initiator}, and I'm here to interview you about your recent accomplishments. Our readers are eager to learn more about the person behind the headlines,\" {initiator} says with enthusiasm.",
            "\"Your story has touched many of our readers, {target}. I'm {initiator}, a reporter for the local news, and I'd like to ask you a few questions about your experiences,\" {initiator} requests.",
            "\"{target}, your story is truly inspiring, and I'm honored to have the opportunity to interview you today. Let's start by discussing your background and what led you to this point in your life,\" {initiator} proposes.",
            "\"Welcome, {target}. I'm {initiator}, a reporter covering your story for our publication. I'm excited to hear about your journey and the impact it's had on those around you,\" {initiator} says, ready to begin the interview.",
            "\"Today, I have the pleasure of interviewing {target}, whose story has captivated our community. {target}, can you please tell us about the challenges you've faced and the triumphs you've achieved?\" {initiator} asks."
        ]
    },
    "mixer_social_LieAboutCareer_group_mischief_skills": {
        "pre_actions": [
            "{initiator} lies about their career to {target}.",
        ],
        "actions": [
            "\"{target}, I've never told anyone this, but I'm actually a ",
            "\"Guess what, {target}? I've been keeping something from you. I'm actually a ",
            "\"I didn't want to tell you this at first, {target}, but I'm actually a ",
            "\"You'll never believe this, {target}, but I'm not really an ",
            "\"Okay, {target}, I'll be honest with you. I didn't want to tell you before, but I'm actually a ",
            "\"I know this might be hard to believe, {target}, but I'm not really a ",
            "\"Truth is, {target}, I've been hiding something from you. I'm not just a ",
            "\"I didn't want to tell you this before, {target}, but I'm actually a "
        ]
    },
    "mixer_social_TalkAboutBestsellers_targeted_Friendly_alwaysOn_career": {
        "actions": [
            "\"{target}, have I ever mentioned that I wrote a few bestsellers in my time?\" {initiator} asks, a hint of pride in their voice.",
            "\"Do you know, {target}, that I'm the author of some of the bestsellers you might have come across? Quite an accomplishment, isn't it?\" {initiator} says with a smile.",
            "\"{target}, I've been meaning to tell you about my success as a writer. I actually have a few bestsellers under my belt,\" {initiator} shares, looking for a reaction.",
            "\"Guess what, {target}? I've written a couple of bestsellers! It's one of my proudest achievements,\" {initiator} says, waiting for {target}'s response.",
            "\"You know, {target}, I've always had a passion for writing. In fact, I've even written a few bestsellers! Can you believe it?\" {initiator} asks, eager to share their accomplishments.",
            "\"{target}, there's something you may not know about me. I've actually written a number of bestsellers. It's been an incredible journey,\" {initiator} says, reminiscing about their past.",
            "\"Did you know, {target}, that I have a few bestsellers to my name? Writing has always been a passion of mine,\" {initiator} shares, hoping to find common ground.",
            "\"I've been wanting to tell you this, {target}, but I wasn't sure how you'd react. I've written a few bestsellers, and I'm quite proud of them,\" {initiator} admits, looking for approval.",
            "\"It's not every day you meet someone who's written bestsellers, is it, {target}? Well, now you have!\" {initiator} says, beaming with pride.",
            "\"I've always enjoyed writing, {target}, and I've even had the fortune of penning a few bestsellers. It's a great feeling, knowing that people enjoy my work,\" {initiator} says, looking thoughtful."
        ]
    },
    "mixer_social_SecretVillainHandshake_targeted_mean_alwaysOn_career": {
        "actions": [
            "\"{target}, I've been wanting to try this with someone I trust. Let's do the secret supervillain handshake,\" {initiator} says with excitement.",
            "\"Hey {target}, I've got a fun idea. How about we try this secret handshake I learned? It's supposed to be for supervillains, but I think we can pull it off,\" {initiator} suggests with a grin.",
            "{initiator} smirks at {target} and says, \"You seem like someone who would appreciate a good secret handshake. What do you say? Want to try this supervillain one I know?\"",
            "With a mischievous glint in their eye, {initiator} asks {target}, \"Are you up for learning a secret handshake only known among supervillains? I think it'll be our little inside joke.\"",
            "\"{target}, I bet you've never done a secret supervillain handshake before. Want to give it a try?\" {initiator} says, extending their hand.",
            "\"Let's see if you can keep up with this secret handshake I learned, {target}. It's said to be used by supervillains,\" {initiator} says, challenging {target} playfully.",
            "{initiator} playfully nudges {target} and says, \"I've got something fun for us to try. It's a secret supervillain handshake, but don't worry, I think we can handle it.\"",
            "\"Hey {target}, I think we should have our own secret handshake. How about this one I found? They say it's a supervillain's handshake, but I think it suits us,\" {initiator} proposes with a wink.",
            "\"I came across this secret supervillain handshake, {target}, and I thought of you immediately. Want to learn it together?\" {initiator} asks enthusiastically.",
            "{initiator} looks at {target} and says, \"You know what we're missing? A secret handshake. I found this one that's supposedly a supervillain's secret. Let's try it!\""
        ]
    },
    "mixer_social_ExposeSupervillain_targeted_mean_career": {
        "actions": [
            "\"{target}, I've discovered your secret identity. I know you're the infamous supervillain everyone's been talking about,\" {initiator} says, confronting them.",
            "\"Did you really think you could hide your dark deeds from me, {target}? I know everything,\" {initiator} says, staring them down.",
            "\"{target}, I never thought I'd say this, but I found evidence of your true identity. You're not the person I thought you were,\" {initiator} admits, looking betrayed.",
            "\"I can't believe it, {target}. All this time, you've been leading a double life as a supervillain. How could you?\" {initiator} asks, hurt and angry.",
            "\"{target}, I've pieced it all together. It's time to stop hiding. I know you're the one behind all the chaos in our city,\" {initiator} accuses, determined to expose them.",
            "\"I've been watching you closely, {target}, and I've uncovered your secret. You can't hide your villainous actions from me any longer,\" {initiator} says, ready to confront them.",
            "\"{target}, I had my suspicions, but now I'm certain. You're the one wreaking havoc as a supervillain. It's time to face the truth,\" {initiator} says, losing faith in their friend.",
            "\"I thought I knew you, {target}, but I never imagined you were capable of being the supervillain terrorizing our city,\" {initiator} says, feeling betrayed.",
            "\"{target}, your actions as a supervillain have caused so much pain and suffering. I can't let you hide behind your lies anymore,\" {initiator} says, determined to bring them to justice.",
            "\"I trusted you, {target}, but now I see you for who you truly are – a supervillain. You can't hide from me any longer,\" {initiator} says, ready to confront the truth."
        ]
    },
    "mixer_social_EnthuseAboutSpace_targeted_friendly_alwaysOn_career": {
        "actions": [
            "\"{target}, I can't begin to tell you how amazing it is to work in space. The views, the endless possibilities... It's a dream come true!\" {initiator} exclaims passionately.",
            "\"Have I ever mentioned how incredible my career in space is, {target}? The things I've seen and experienced are beyond words,\" {initiator} says, eyes shining with excitement.",
            "\"{target}, you wouldn't believe the wonders of space. My job has given me the opportunity to explore the cosmos, and it's breathtaking,\" {initiator} shares enthusiastically.",
            "\"Working in space has been a life-changing experience, {target}. It's not every day you get to see Earth from above, and it's simply mesmerizing,\" {initiator} says with awe.",
            "\"I have to tell you about my job in space, {target}. The stars, the planets, the sheer vastness... it's all so captivating,\" {initiator} gushes.",
            "\"{target}, my career in space is like living in a dream. The universe is so vast and beautiful, and I'm grateful to be a part of it,\" {initiator} says, filled with admiration.",
            "\"Every time I step out into space, {target}, I'm reminded of how small we are in the grand scheme of things. It's both humbling and inspiring,\" {initiator} shares with fervor.",
            "\"There's nothing quite like floating among the stars, {target}. My career in space has given me a new perspective on life and our place in the universe,\" {initiator} says, lost in thought.",
            "\"{target}, I wish I could show you the wonders of space. My job has opened my eyes to the beauty and mysteries of the cosmos,\" {initiator} says dreamily.",
            "\"Being an astronaut has its challenges, {target}, but the rewards are immeasurable. The sense of awe and wonder it instills in you is something I'll cherish forever,\" {initiator} declares with passion."
        ]
    },
    "mixer_social_InterviewAboutLife_targeted_Friendly_alwaysOn_career": {
        "actions": [
            "\"{target}, many people are curious about your life story. Would you mind sharing some details with me?\" {initiator} asks, holding a recorder.",
            "\"{initiator} here, and today I have the pleasure of interviewing {target}. So, can you tell us about your journey so far?\" {initiator} begins the interview with a warm smile.",
            "\"Welcome, {target}, and thank you for joining me today. I'd love to learn more about your experiences and the path that led you here,\" {initiator} says, ready to take notes.",
            "\"Thank you for agreeing to this interview, {target}. Our readers are eager to know how you've achieved such success in your life. Please, share your story with us,\" {initiator} requests.",
            "\"{target}, it's an honor to have you here today. I'm sure our audience is just as excited as I am to hear about your personal journey. Let's start from the beginning, shall we?\" {initiator} asks enthusiastically.",
            "\"Hello, {target}. I'm {initiator}, and I'm here to learn more about your incredible life story. Can you tell us about the challenges you've faced and how you overcame them?\" {initiator} inquires.",
            "\"{target}, your life is truly inspiring, and I'd love to know more about the events that shaped you. Can you walk me through your journey?\" {initiator} asks with genuine curiosity.",
            "\"Good to meet you, {target}. Our readers are fascinated by your accomplishments and would love to know more about your life. Can you give us some insights?\" {initiator} questions, pen in hand.",
            "\"{initiator} here, and I'm honored to have the opportunity to interview the incredible {target}. Let's dive into your life's story and learn about the experiences that molded you,\" {initiator} says with excitement.",
            "\"Thank you for joining me today, {target}. As a reporter, I am eager to document your life story and share it with the world. Where would you like to begin?\" {initiator} asks, setting up the recorder."
        ]
    },
    "mixer_social_ImitateBoss_Targeted_Funny_AlwaysOn_Career": {
        "actions": [
            "\"{target}, check this out,\" {initiator} says with a grin, \"This is our boss when he's giving a lecture.\" {initiator} proceeds to imitate their boss hilariously.",
            "{initiator} leans in close to {target} and whispers, \"Watch this, I've been practicing my impression of the boss. What do you think?\" {initiator} then impersonates the boss, making {target} laugh.",
            "\"Hey {target}, wanna see something funny?\" {initiator} asks, before launching into a spot-on imitation of their boss, causing both of them to giggle.",
            "{initiator} suddenly adopts the boss's mannerisms and tone of voice, saying to {target}, \"I expect those reports on my desk by Friday!\" Both characters burst out laughing at the uncanny impression.",
            "\"Remember when the boss said this?\" {initiator} asks {target}, before flawlessly imitating their boss's most memorable quote, making {target} chuckle.",
            "{initiator} turns to {target} with a smirk and says, \"So, {target}, have I ever shown you my impression of the boss?\" {initiator} then proceeds to imitate the boss, leaving {target} in stitches.",
            "\"Hey {target}, you know how our boss always says that one thing? Check this out,\" {initiator} says, before imitating the boss's catchphrase and mannerisms, making {target} laugh.",
            "{initiator} casually says to {target}, \"I've been working on this for a while, tell me what you think,\" and then proceeds to hilariously mimic their boss, causing {target} to burst out laughing.",
            "{initiator} catches {target}'s eye and, with a mischievous grin, starts imitating their boss's distinctive walk and speech, making {target} snicker.",
            "\"Watch closely, {target}, this is my masterpiece,\" {initiator} announces, before launching into a hilarious imitation of their boss that leaves {target} doubled over with laughter."
        ]
    },
    "mixer_social_OfferCareerAdvice_Targeted_Friendly_AlwaysOn_career": {
        "actions": [
            "\"{target}, I've been thinking about your career, and I have some ideas that I believe could really help you succeed,\" {initiator} says, looking eager to share their thoughts.",
            "\"Hey {target}, I noticed you've been struggling with your career lately, and I wanted to offer some advice. I hope you don't mind,\" {initiator} says, trying not to pry.",
            "\"{target}, I've been in a similar situation in my career, and I discovered some strategies that might help you as well. Would you like to hear them?\" {initiator} asks kindly.",
            "\"You know, {target}, I've learned a lot throughout my career, and I'd be happy to share some insights with you if you're open to it,\" {initiator} says, hoping to provide some guidance.",
            "\"I couldn't help but overhear your conversation about your career, {target}. I have some experience in that field, and I'd be more than willing to offer some advice if you'd like,\" {initiator} says, trying to be helpful.",
            "\"{target}, I know you've been working hard on your career, and I wanted to share some tips that helped me along the way. Are you interested in hearing them?\" {initiator} asks, wanting to lend a hand.",
            "\"Hey {target}, I was thinking about your career path, and I have a few suggestions that I believe could benefit you. Would you like to discuss them over coffee?\" {initiator} proposes, hoping to help their friend.",
            "\"{target}, I've been in your shoes before, and I know how tough it can be. I'd love to share some career advice with you if you're open to it,\" {initiator} says, relating to their friend's struggles.",
            "\"I know it's not my place to say, {target}, but I think I have some career advice that might really help you. Would you be willing to hear me out?\" {initiator} asks cautiously.",
            "\"Hey {target}, I've been meaning to talk to you about your career. I've learned a lot in my own journey, and I think there are some things that could help you as well,\" {initiator} says, genuinely wanting to help."
        ],
    },
    "Social_Trait_Ambitious_GiveCareerAdvice": {
        "actions": [
            "\"{target}, I've been thinking about your career, and I have some ideas that I believe could really help you succeed,\" {initiator} says, looking eager to share their thoughts.",
            "\"Hey {target}, I noticed you've been struggling with your career lately, and I wanted to offer some advice. I hope you don't mind,\" {initiator} says, trying not to pry.",
            "\"{target}, I've been in a similar situation in my career, and I discovered some strategies that might help you as well. Would you like to hear them?\" {initiator} asks kindly.",
            "\"You know, {target}, I've learned a lot throughout my career, and I'd be happy to share some insights with you if you're open to it,\" {initiator} says, hoping to provide some guidance.",
            "\"I couldn't help but overhear your conversation about your career, {target}. I have some experience in that field, and I'd be more than willing to offer some advice if you'd like,\" {initiator} says, trying to be helpful.",
            "\"{target}, I know you've been working hard on your career, and I wanted to share some tips that helped me along the way. Are you interested in hearing them?\" {initiator} asks, wanting to lend a hand.",
            "\"Hey {target}, I was thinking about your career path, and I have a few suggestions that I believe could benefit you. Would you like to discuss them over coffee?\" {initiator} proposes, hoping to help their friend.",
            "\"{target}, I've been in your shoes before, and I know how tough it can be. I'd love to share some career advice with you if you're open to it,\" {initiator} says, relating to their friend's struggles.",
            "\"I know it's not my place to say, {target}, but I think I have some career advice that might really help you. Would you be willing to hear me out?\" {initiator} asks cautiously.",
            "\"Hey {target}, I've been meaning to talk to you about your career. I've learned a lot in my own journey, and I think there are some things that could help you as well,\" {initiator} says, genuinely wanting to help."
        ],
    },
    "mixer_social_DontTalkAboutCrimeClub_targeted_Friendly_alwaysOn_career": {
        "actions": [
            "\"{target}, I need you to promise me something. Never bring up the crime club in public,\" {initiator} says in a serious tone.",
            "\"Listen, {target}, it's really important that you never mention the crime club around others. We have to keep it a secret,\" {initiator} warns.",
            "\"{target}, if there's one thing you must remember, it's that you cannot talk about crime club. It's for our own safety,\" {initiator} says urgently.",
            "\"Please, {target}, be careful with your words. Don't ever let the crime club slip into any conversation,\" {initiator} pleads.",
            "\"I can't stress this enough, {target}. Keep the crime club to yourself. No one else can know,\" {initiator} says, looking {target} in the eye.",
            "\"Remember, {target}, the first rule of crime club is that you do not talk about crime club,\" {initiator} reminds with a stern expression.",
            "\"Never let your guard down, {target}. We can't afford to have people find out about the crime club,\" {initiator} says firmly.",
            "\"Talking about crime club could put us all in danger, {target}. Be cautious with what you say,\" {initiator} advises.",
            "\"Keep this between us, {target}. The crime club stays a secret, no matter the circumstances,\" {initiator} insists.",
            "\"I trust you, {target}, but I need you to understand the importance of not discussing the crime club with anyone. Can you promise me that?\" {initiator} asks earnestly."
        ],
    },
    "mixer_social_AskAbout_PrizedPossessions_mischief_alwaysOn_trait": {
        "pre_actions": [
            '{initiator} mischievously asks {target} about their prized possessions.',
        ],
        'actions': [
            '"So, {target}, what are your most prized possessions?" {initiator} asks with a mischievous grin.',
            '{initiator} playfully nudges {target} and says, "Come on, spill the beans! What are your most treasured belongings?',
            'With a twinkle in their eye, {initiator} leans in and whispers, "Tell me, {target}, what do you hold most dear in this world?"',
            '{initiator} smirks and teases, "You know, {target}, I\'m dying to know what you value the most. Care to share?',
            'Curiosity piqued, {initiator} leans closer to {target} and inquires, "So, what\'s the one thing you can\'t live without, {target}?',
            '{initiator} playfully prods {target} and asks, "Hey, {target}, what\'s your secret stash of prized possessions?",'
            'Eagerly, {initiator} asks {target}, "Do you have any special items that hold a special place in your heart?"',
            'With a sly grin, {initiator} challenges {target}, "I bet you have some hidden treasures. Care to divulge?',
            '{initiator} raises an eyebrow and says, "I have a feeling you\'ve got some interesting prized possessions. Care to enlighten me, {target}?',
            '{initiator} leans back, smirking, and says, "Okay, {target}, spill the beans. What\'s your most prized possession?"',
        ],
    },
    # This is the interaction that runs right when a Sim starts to walk away towards an exit
    "NPCLeaveLotNow_NPC_WaveGoodBye": {
        "observations": [
            "{initiator} waves goodbye and leaves.",
        ],
        "filters": [
            SimInMemories(memory_depth=30),
            HasNotHappened(memory_depth=5),
        ],
    },
    # This is the interaction that runs right when a Sim leaves a lot
    "NPCLeaveLot_Player_WaveGoodBye": {
        "ignored": True,
    },
    "npc_leave_lot_now": {
        "ignored": True,
    },
    "bar_OrderDrink": {
        "observations": [
            "{initiator} orders a drink from {target} at the bar.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "sim-stand": {
        "observations": [
            "{initiator} stands up.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "seating_sit_CTYAE": {
        "observations": [
            "{initiator} sits down.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "Drink_Active": {
        "observations": [
            "{initiator} takes a swig their drink.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "Drink_Passive": {
        "observations": [
            "{initiator} takes a swig their drink.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "bar_OrderChips": {
        "observations": [
            "{initiator} orders some chips from {target} at the bar.",
        ],
        "filters": [
            HasNotHappened(memory_depth=2),
            InitiatorIsActiveSim(),
        ],
    },
    "toilet-use-sitting": {
        "observations": [
            "{initiator} uses the toilet.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "Toilet_Use_Action": {
        "observations": [
            "{initiator} uses the toilet.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "sim_TalkToSelf": {
        "observations": [
            "{initiator} talks to themself.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "autonomous_ObjectPicker_Insane_TalkToObjects": {
        "observations": [
            "{initiator} talks to objects in the room like a crazy person.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "sink_washHands": {
        "observations": [
            "{initiator} washes their hands in the sink.",
        ],
        "filters": [
            HasNotHappened(memory_depth=2),
            InitiatorIsActiveSim(),
        ],
    },
    "sink_create": {
        "observations": [
            "{initiator} grabs some water from the sink.",
        ],
        "filters": [
            HasNotHappened(memory_depth=2),
            InitiatorIsActiveSim(),
        ],
    },
    "sink_BrushTeeth": {
        "observations": [
            "{initiator} brushes their teeth in the sink.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "mirror_GussyUp": {
        "observations": [
            "{initiator} freshens up in the mirror.",
        ],
        "filters": [
            HasNotHappened(memory_depth=2),
            InitiatorIsActiveSim(),
        ],
    },
    "toilet-use-standing": {
        "observations": [
            "{initiator} uses the toilet while standing up.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "super_SitOnGround_CrossLegged": {
        "observations": [
            "{initiator} sits on the ground cross legged.",
        ],
        "filters": [
            HasNotHappened(memory_depth=2),
            InitiatorIsActiveSim(),
        ],
    },
    "Collect_Dish": {
        "observations": [
            "{initiator} picks up a dish.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "sink_washDishes": {
        "observations": [
            "{initiator} washes a dish in the sink.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "coffeeMaker_MakeRecipe_Start_OneShot_Basic": {
        "observations": [
            "{initiator} starts to a make a single serve cup of coffee.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "brew_WaitFor_Pot": {
        "observations": [
            "{initiator} waits for the coffee to brew.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "coffeeMaker_Grab": {
        "observations": [
            "{initiator} grabs a cup of coffee.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "drink_Coffee_Generic_Consume": {
        "observations": [
            "{initiator} takes a sip from their coffee.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "stereo_danceActive": {
        "observations": [
            "{initiator} dances.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "stereo_Dance": {
        "observations": [
            "{initiator} dances.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "generic_Dance": {
        "observations": [
            "{initiator} dances.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "stereo_dancePassive": {
        "observations": [
            "{initiator} dances.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "stereo_Dance_WallSpeaker": {
        "observations": [
            "{initiator} dances.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "terrain-jog": {
        "observations": [
            "{initiator} starts jogging around.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "WorkoutMachine_legLifts": {
        "observations": [
            "{initiator} does leg lifts on the workout machine.",
        ],
        "filters": [
            HasNotHappened(memory_depth=2),
            InitiatorIsActiveSim(),
        ],
    },
    "WorkoutMachine_pullDowns": {
        "observations": [
            "{initiator} does some pulldowns on the workout machine.",
        ],
        "filters": [
            HasNotHappened(memory_depth=2),
            InitiatorIsActiveSim(),
        ],
    },
    "WorkoutMachine_flys": {
        "observations": [
            "{initiator} does some flys on the workout machine.",
        ],
        "filters": [
            HasNotHappened(memory_depth=2),
            InitiatorIsActiveSim(),
        ],
    },
    "sim_DrinkEnergyJuice": {
        "observations": [
            "{initiator} takes a sip of energy juice.",
        ],
        "filters": [
            HasNotHappened(memory_depth=2),
            InitiatorIsActiveSim(),
        ],
    },
    "treadmill_action1": {
        "observations": [
            "{initiator} runs on the treadmill.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "treadmill_action2": {
        "observations": [
            "{initiator} runs on the treadmill.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "sim_HygieneDistress": {
        "observations": [
            "{initiator} starts to feel uncomfortable because they haven't showered and they are stinky.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "punchingBag_Passive": {
        "observations": [
            "{initiator} punches the punching bag.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "dresser_ChangeIntoTowel": {
        "observations": [
            "{initiator} removes their clothes and wraps a towel around their waist.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "dresser_ChangeOutOfTowel": {
        "observations": [
            "{initiator} removes the towel from their waist and changes back into their clothes.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "shower_TakeShower_Steamy": {
        "observations": [
            "{initiator} takes a steamy shower and feels flirty when they get out.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "object_Repair_Shower": {
        "observations": [
            "{initiator} grabs some tools and fixes the issue with the shower.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "trash_salvage_scavenge": {
        "observations": [
            "{initiator} scavanges the trash pile looking for parts.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "shower_TakeShower_ColdShower": {
        "observations": [
            "{initiator} takes a cold shower.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "shower_TakeShower_Brisk": {
        "observations": [
            "{initiator} takes a brisk shower.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "shower_TakeShower_Energized": {
        "observations": [
            "{initiator} takes a speedy energizing shower.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "shower_TakeShower_Thoughtful": {
        "observations": [
            "{initiator} takes a thoughtful shower and feels inspired when they get out.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "seating_Sit": {
        "observations": [
            "{initiator} sits down.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "sim_doSitUpsAutonomously": {
        "observations": [
            "{initiator} does situps.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "sim_doPushUpsAutonomously": {
        "observations": [
            "{initiator} does pushups.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "sim_doPushUps_NPCSituation": {
        "observations": [
            "{initiator} does pushups.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "socialMixer_Greetings_Wave": {
        "observations": [
            "{initiator} waves at {target}.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "mixer_Fireplace_WarmSelf": {
        "observations": [
            "{initiator} warms themself by the fireplace.",
        ],
        "filters": [
            HasNotHappened(memory_depth=8),
            InitiatorIsActiveSim(),
        ],
    },
    "Idle_Chatting_STC": {
        "observations": [
            "{initiator} idly chats with {target}.",
        ],
        "filters": [
            HasNotHappened(memory_depth=8),
            InitiatorIsActiveSim(),
        ],
    },
    "Emotion_Idle": {
        "ignored": True,
    },
    "SocialPickerSI": {
        "ignored": True,
    },
    "social_adjustment": {
        "ignored": True,
    },
    "mixer_social_NPC_greetings": {
        "observations": [
            "{initiator} greets {target}.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "idle_Buff_EnvironmentScore_Positive": {
        "observations": [
            "{initiator} is enjoying themselves being here.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "sim_Chat": {
        "observations": [
            "{initiator} chats with {target}.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "idle_Chatting_ListenWithPhone_STC": {
        "observations": [
            "{initiator} messes with their phone while idly chatting with {target}.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "sim_doStretching": {
        "observations": [
            "{initiator} stretches.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "phone_BrowseWebsites": {
        "observations": [
            "{initiator} browses the internet on their phone.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "phone_BrowseWebsites_AutonomousOnly": {
        "observations": [
            "{initiator} browses the internet on their phone.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "bar_StartPracticeTricks_CreateShaker": {
        "observations": [
            "{initiator} grabs a cocktail shaker to practice bar tricks.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "si_touching_Greeting_Handshake": {
        "observations": [
            "{initiator} shakes hands with {target}.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "sit_Passive": {
        "ignored": True,
    },
    "bar_Tend_Passive": {
        "ignored": True,
    },
    "bar_Tend_Active": {
        "ignored": True,
    },
    "bar_CreateGlass": {
        "observations": [
            "{initiator} grabs a glass to make a drink.",
        ],
        "filters": [
            HasNotHappened(memory_depth=3),
            InitiatorIsActiveSim(),
        ],
    },
    "Bar_Pour_Basic": {
        "observations": [
            "{initiator} pours some liquid in the glass.",
        ],
        "filters": [
            HasNotHappened(memory_depth=3),
            InitiatorIsActiveSim(),
        ],
    },
    "Bar_Add_Ice": {
        "observations": [
            "{initiator} adds ice to the glass.",
        ],
        "filters": [
            HasNotHappened(memory_depth=3),
            InitiatorIsActiveSim(),
        ],
    },
    "Bar_Crafting_MakeDrink_Idles": {
        "ignored": True,
    },
    "Bar_EmotionResponse": {
        "ignored": True,
    },
    "Bar_Stir_Basic": {
        "observations": [
            "{initiator} stirs the drink.",
        ],
        "filters": [
            HasNotHappened(memory_depth=3),
            InitiatorIsActiveSim(),
        ],
    },
    "bar_ServerToSitDrinkSlot": {
        "observations": [
            "{initiator} sets the drink on the counter to serve it.",
        ],
        "filters": [
            HasNotHappened(memory_depth=3),
            InitiatorIsActiveSim(),
        ],
    },
    "bar_WaitForDrink": {
        "observations": [
            "{initiator} waits for their drink to be made.",
        ],
        "filters": [
            HasNotHappened(memory_depth=3),
            InitiatorIsActiveSim(),
        ],
    },
    "mirror_SelfPepTalk": {
        "observations": [
            "{initiator} gives themselves a pep talk in the mirror.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "mirror_SelfPepTalk1": {
        "observations": [
            "{initiator} gives themselves a pep talk in the mirror.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "mirror_SelfPepTalk2": {
        "observations": [
            "{initiator} gives themselves a pep talk in the mirror.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "mirror_SelfPepTalk3": {
        "observations": [
            "{initiator} gives themselves a pep talk in the mirror.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "mirror_SelfPepTalk4": {
        "observations": [
            "{initiator} gives themselves a pep talk in the mirror.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "mirror_SelfPepTalk5": {
        "observations": [
            "{initiator} gives themselves a pep talk in the mirror.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "bar_NonCrafting_Passive": {
        "ignored": True,
    },
    "generic_BarMakeDrink": {
        "ignored": True,
    },
    "GoHomeAndAttendWork": {
        "observations": [
            "{initiator} leaves to go home to attend work.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "phone_PlayGames_AutonomousOnly": {
        "observations": [
            "{initiator} idly plays a game on their phone.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "stand_Passive": {
        "ignored": True,
    },
    "bar_PushOrderDrink_Autonomous": {
        "observations": [
            "{initiator} walks to the bar and orders a drink.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "Bar_BottleStack_Basic": {
        "observations": [
            "{initiator} does a bar trick stacking multiple bottles on top of each other.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "socials_Romance_AutonomousOnly_STC": {
        "observations": [
            "{initiator} romantically chats with {target}.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "bar_ChooseDelivery": {
        "ignored": True,
    },
    "generic_consume_drink_bar": {
        "observations": [
            "{initiator} sitting at the bar takes a swig of their drink.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "NPC_WalkBys_LeaveArea": {
        "observations": [
            "{initiator} walks by as they leave the area.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "sim_Carry_Object_Book": {
        "observations": [
            "{initiator} picks up a book.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "GoHomeAndAttendSchool": {
        "observations": [
            "{initiator} heads home so they can attend school.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "mixer_AtWork_SocializeWithCoworkers": {
        "observations": [
            "{initiator} socializes with some coworkers at work.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "mixer_AtWork_EatMeal": {
        "observations": [
            "{initiator} eats a meal at work.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "bed_Autonomous_SingleBed_Nap": {
        "observations": [
            "{initiator} jumps in the narrow single bed to take a nap.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "npc_leave_lot_now_must_run_ss3_request": {
        "ignored": True,
    },
    "bed_Nap": {
        "observations": [
            "{initiator} continues to nap on the bed.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "fridge_CookAutonomously": {
        "observations": [
            "{initiator} opens the fridge to make something.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "fridge_CreateTray": {
        "observations": [
            "{initiator} creates a tray of items from the fridge.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "Counter_CuttingBoard_Chop_Tomato": {
        "observations": [
            "{initiator} chops up a tomato.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "Counter_MixingBowl_Toss_Basic": {
        "observations": [
            "{initiator} tosses the food in the mixing bowl.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "counter_MakeFood_Staging_Basic": {
        "observations": [
            "{initiator} tosses the food in the mixing bowl.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "Food_Eat_Active": {
        "observations": [
            "{initiator} eats their food.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "Food_Eat_Passive": {
        "observations": [
            "{initiator} eats their food.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "Cooking_Shared_Passive_Basic": {
        "ignored": True,
    },
    "generic_cook": {
        "ignored": True,
    },
    "generic_consume_food": {
        "ignored": True,
    },
    "SleepMixer_Dream": {
        "observations": [
            "{initiator} has a dream while they are sleeping.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "sleep_Passive": {
        "ignored": True,
    },
    "generic_Bed_Sleep": {
        "ignored": True,
    },
    "bed_sleep": {
        "ignored": True,
    },
    "generic_ToiletSit": {
        "ignored": True,
    },
    "autonomous_ObjectPicker_CollectDishes": {
        "observations": [
            "{initiator} picks up the dishes left out.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "fridge_GrabSnackAutonomously": {
        "observations": [
            "{initiator} grabs a snack out of the fridge.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "fridge_CreateSnackAndConsume_Generic": {
        "observations": [
            "{initiator} eats their snack out of the fridge.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "reaction_SmellBad": {
        "observations": [
            "{initiator} smells a bad smell.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "autonomous_bookshelf_read_picker": {
        "observations": [
            "{initiator} grabs a book off the bookshelf to read.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "Book_Read_Active": {
        "observations": [
            "{initiator} reads a book.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "Book_Read_Passive": {
        "observations": [
            "{initiator} reads a book.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "Autonomous_Generic_Book_Read_TYAE": {
        "observations": [
            "{initiator} reads a book.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "mixer_AtWork_Default": {
        "ignored": True,
    },
    "npc_leave_lot_now_must_run": {
        "ignored": True,
    },
    "si_Career_Astronaut": {
        "observations": [
            "{initiator} finishes their day at work.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "sim-standExclusive": {
        "ignored": True,
    },
    "idle_Fun": {
        "observations": [
            "{initiator} feels like they could use some fun.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "idle_Hygiene": {
        "observations": [
            "{initiator} feels dirty and wants to freshen up.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "autonomous_Bookshelf_Browse_Picker": {
        "ignored": True,
    },
    "FishingLocation_Cast_Dock": {
        "observations": [
            "{initiator} is on the dock and casts their fishing line.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "Idle_Age_Teen": {
        "ignored": True,
    },
    # TODO: Special consideration here
    # "door_RingDoorbell": {
    #     "observations": [
    #         "{initiator} rings the doorbell.",
    #     ],
    #     "filters": [
    #         HasNotHappened(memory_depth=10),
    #         InitiatorIsActiveSim(),
    #     ],
    # },
    "Put_Away_Books": {
        "observations": [
            "{initiator} puts away the books.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "book_read_browse": {
        "observations": [
            "{initiator} flips through the book quickly and skims the pages.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "idle_Buff_SimPreference_Likes_Activities_Cooking": {
        "observations": [
            "{initiator} is enjoying cooking.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "seating_sit_Bed_SitOnly_NotVisible": {
        "observations": [
            "{initiator} sits down on the bed.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "seating_Sit_Bed_YAE": {
        "observations": [
            "{initiator} sits down on the bed.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "sim_BeAffectionate": {
        "observations": [
            "{initiator} is affectionate to {target}.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "Collect_Dish_As_Trash": {
        "observations": [
            "{initiator} picks up a dish and throws it in the trash.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "Collect_Dish_As_Trash_Continuation": {
        "observations": [
            "{initiator} picks up a dish and throws it in the trash.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "autonomous_ObjectPicker_CollectDishesAsTrash": {
        "observations": [
            "{initiator} picks up a dish and throws it in the trash.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "Throw_Away_Indoor": {
        "observations": [
            "{initiator} throws the trash in the wastebasket.",
        ],
        "filters": [
            HasNotHappened(memory_depth=5),
            InitiatorIsActiveSim(),
        ],
    },
    "Idle_Trait_Romantic": {
        "observations": [
            "{initiator} is enjoying being romantic.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "Empty_Trash": {
        "observations": [
            "{initiator} empties the wastebasket.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "Throw_Away_Outdoor": {
        "observations": [
            "{initiator} throws the trash in the outdoor garbage bin.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
}

if __name__ == '__main__':
    num_keys = len(interaction_descriptions)
    print(num_keys)
