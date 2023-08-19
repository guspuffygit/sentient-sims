# {initiator} and {target} will be replaced with the names of the sims in the interaction
from sentient_sims_code.filters.has_not_happened import HasNotHappened
from sentient_sims_code.filters.initiator_is_active_sim import InitiatorIsActiveSim
from sentient_sims_code.filters.sim_in_memories import SimInMemories

interaction_descriptions = {
    "mixer_social_ComplainAboutBills_targeted_Friendly_alwaysOn_bills": {
        "pre_actions": [
            "{initiator} complains about their bills to {target}.",
        ],
        "actions": [
            "\"I don't know how I'm going to pay for all of these bills,\" {initiator} says.",
            "\"It seems like every time I turn around, there's another bill to pay,\" {initiator} grumbled.",
            "\"I can't believe how much money I have to spend on bills every month,\" {initiator} grumbles.",
            "\"I'm so sick of living paycheck to paycheck just to keep up with these bills,\" {initiator} complains.",
        ],
    },
    'mixer_social_DiscussLatestGames_targeted_Friendly_alwaysOn_skills': {
        "pre_actions": [
            "{initiator} discusses the newly released video game with {target}.",
        ],
        "actions": [
            "\"What do you think of the new video game, {target}? Have you had a chance to play it yet?\" {initiator} asks excitedly.",
            "\"I can't stop playing the new video game. Have you tried it yet, {target}?\" {initiator} says, grinning from ear to ear.",
            "\"I've been waiting for this video game for months, {target}, and I have to say, it's exceeded my expectations,\" {initiator} raves.",
            "\"Have you heard about the new video game? I think you'd really like it, {target},\" {initiator} says, trying to pique {target}'s interest.",
            "\"I'm so glad I pre-ordered the new video game. It's all I can think about. What do you think, {target}?\" {initiator} asks, eagerly.",
            "\"You have to play the new video game, {target}. It's seriously the best game I've played in years,\" {initiator} says, practically begging {target} to give it a try.",
            "\"I can't believe how good the graphics are in the new video game. It's like I'm really in the game,\" {initiator} says, still in awe.",
            "\"Did you catch that Easter egg in the new video game? It's so cool. I wonder if there are any more,\" {initiator} muses, hoping to discuss details with {target}.",
            "\"I love how immersive the new video game is. It's like I'm living in a completely different world,\" {initiator} says dreamily.",
            "\"The new video game has been consuming all of my free time. Do you want to play together sometime, {target}?\" {initiator} suggests.",
        ],
    },
    'mixer_social_CheerfulIntroduction_greetings_skills': {
        "pre_actions": [
            "{initiator} cheerfully introduces themselves to {target} for the first time.",
        ],
        "actions": [
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
            "{initiator} flirtatiously introduces themselves to {target}.",
        ],
        "actions": [
            "With a flirtatious smile, {initiator} strode over and extended their hand. \"Hi there, I'm {initiator}. What's your name?\"",
            "{initiator} sauntered up with a charming grin. \"Well hello there, I don't think we've met yet. I'm {initiator}.\"",
            "With a twinkle in their eye, {initiator} approached the other person and struck up a conversation. \"Excuse me,\"",
            "With a playful wink, {initiator} sauntered up to the other person and introduced themselves. \"Hi,",
            "{initiator} catches {target}'s gaze and saunters over with a mischievous grin. \"Feeling bored? Don't worry, your day's about to get interesting. By the way, I'm {initiator}.\" they say, their voice low and flirtatious.",
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
            "{initiator} pauses thoughtfully before expressing their fondness for {target}.",
        ],
        "actions": [
            "\"I've been meaning to tell you this, {target}, but I never found the courage to say it until now,\" {initiator} says, looking down at his feet.",
            "\"I don't know how to say this, but I feel something for you, {target}. Something more than friendship,\" {initiator} confesses, looking up at {target} nervously.",
            "\"I hope this doesn't change anything between us, but I need to tell you how I feel. {target}, I have feelings for you,\" {initiator} says, biting his lip.",
            "\"I know this might come as a surprise, {target}, but I can't keep it inside any longer. I'm in love with you,\" {initiator} says, his voice barely above a whisper.",
            "\"I don't know how you'll react to this, {target}, but I have to tell you. I have feelings for you that I can't ignore,\" {initiator} says, looking at {target} with a mix of fear and adoration.",
            "\"I know this might be inappropriate, {target}, but I can't help the way I feel. I'm attracted to you,\" {initiator} says, looking ashamed.",
            "\"I hope you don't think less of me for saying this, {target}, but I feel like I need to be honest. I have a crush on you,\" {initiator} admits, looking at {target} with a hint of sadness.",
            "\"I know this might ruin our friendship, {target}, but I have to say it. I'm in love with you,\" {initiator} says, bracing for the worst.",
            "\"I know we've been friends for a long time, {target}, but I can't help how I feel. I think I'm falling for you,\" {initiator} says, looking at {target} with a mixture of hope and trepidation.",
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
        "actions": [  # J: consider removing actions
            "{initiator} sighed heavily, \"My job sucks,\" they began,\"",
            "\"I hate doing laundry. It's such a chore, and I never seem to have enough time for it.\", {initiator} began,\"",
            "\"I've been trying to eat healthier, but all the healthy food is so expensive.\", {initiator} began,\"",
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
        "actions": [
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
        "actions": [
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
            "\"{target}, I've just returned from a trip to Italy where I had the most amazing food. I can't stop raving about it. Care to hear more?\" {initiator} asks, eager to share.",
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
        "actions": [
            "\"Well, look at you, the very embodiment of unexceptional. I'm {initiator}, an entity so extraordinary, I might as well be from a different planet.\"",
            "\"Hope you have a sturdy ego, {target}. I'm {initiator}, and you've just stepped into the orbit of a someone with enough charisma to make Casanova look like an awkward teenager.\"",
            "\"Try not to pass out from excitement, I'm {initiator}. Compared to me, even interesting people seem boring.\"",
            "\"Oh great, another interaction. Well, I'm {initiator} and, in case you're wondering, yes, my company is as delightful as my sarcasm.\"",
            "\"Here's a warning: your mundane life is about to get a reality check. I'm {initiator}, and I'm about as cheerful as a migraine at a concert.\"",
            "\"Brace yourself. You're talking to {initiator}, the person your parents warned you about.\"",
            "\"Welcome to the most scintillating conversation of your day. I'm {initiator}, the one person in this town who knows how to hold a thought.\"",
            "\"I see you're enjoying mediocrity. Allow me to introduce myself, I'm {initiator}. Yes, I'm as delightful as I sound.\"",
            "\"Try not to look too starstruck. I'm {initiator}, the person whose worst day would be the highlight of your week.\"",
            "\"Boring person, rejoice! I'm here. I'm {initiator}, the most interesting thing to happen to this place since, well, ever.\"",
            "\"Well, isn't this underwhelming? You get to meet me, and I get... you. I'm {initiator}, by the way, the person who's already regretting this conversation.\"",
        ],
    },
    'mixer_social_Flirt_targeted_romance_alwaysOn': {
        "pre_actions": [
            "{initiator} starts to flirt with {target}.",
        ],
        "actions": [
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
            "\"Hi there, I'm {initiator}. What's your name?\"",
            "\"Hey, I'm {initiator}. Nice to meet you!\"",
            "\"Hello, I don't think we've met. I'm {initiator}. And you are?\"",
            "\"Nice to see a new face! I'm {initiator}. What's your name?\"",
            "\"Hey, I'm {initiator}. Mind if I join you?\"",
            "\"Hi, I'm {initiator}. I've been meaning to introduce myself. What's your name?\"",
            "\"Hey, how's it going? I'm {initiator}. What's your name?\"",
            "\"Hello, I'm {initiator}. It's a pleasure to make your acquaintance!\"",
            "\"Hi there, I'm {initiator}. Just wanted to say hello!\"",
            "\"Hey, I'm {initiator}. Care to chat?\"",
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
            "\"Greetings, {target}. I am {initiator}, the master of captivating tales and the weaver of dreams. It is an honor to make your acquaintance.\"",
            "\"Ah, fair {target}, allow me to introduce myself. I am {initiator}, a soul enchanted by the mysteries of the world. May our encounter be as magical as the moonlit night.\"",
            "\"In the realm of enchantment, where whispers become melodies and dreams come alive, I am known as {initiator}. And you, dear {target}, what name graces your existence?\"",
            "\"Behold, {target}, for I am {initiator}, a conjurer of words and a guardian of imagination. Brace yourself, for the allure of my introduction shall transport you to realms yet unexplored.\"",
            "\"With a touch of whimsy and a dash of intrigue, I present myself before you, {target}, as {initiator}, a wanderer of realms unseen and a collector of tales untold. How does your spirit respond to such enchantment?\"",
            "\"In the realm of wonder, where reality intertwines with dreams, I am {initiator}, a custodian of curiosity and an emissary of imagination. And you, {target}, what treasures lie within your name?\"",
            "\"Listen, {target}, as the wind carries my words to your ears. I am {initiator}, a weaver of stories and a guardian of secrets. Dare you venture into the depths of my enchanting introduction?\"",
            "\"Ah, {target}, behold the enchantment that unfolds before you. I am {initiator}, a conjurer of wonder and a purveyor of dreams. Allow yourself to be swept away by the magic of our introduction.\"",
            "\"Step closer, {target}, and let me grace your senses with an introduction like no other. I am {initiator}, a whisper in the night and a sparkle in the twilight, forever enchanted by the possibilities that lie within our encounter.\"",
            "\"In a world where reality dances with fantasy, I emerge as {initiator}, a seeker of extraordinary tales and a harbinger of delight. And you, dear {target}, what wonders lie within your story?\"",
        ],
    },
    'mixer_social_AskAboutCareer_friendly_STC': {
        "pre_actions": [
            "{initiator} starts a conversation with {target} and asks about their career.",
        ],
        "actions": [
            "\"Hey {target}, I've been meaning to ask you, how's your career going?\" {initiator} asks with genuine interest.",
            "\"I've always admired your dedication to your career, {target}. Mind if I ask how it's been going lately?\" {initiator} inquires.",
            "\"Career talk time! I'm curious, {target}, how's everything going in your professional life?\" {initiator} asks, leaning in.",
            "\"Can I pick your brain for a moment, {target}? How's your career shaping up these days?\" {initiator} asks, raising an eyebrow.",
            "\"I've been curious about your career path, {target}. Mind if I ask how things are going on that front?\" {initiator} asks, sipping their coffee.",
            "\"Let's talk about work for a bit, {target}. How's your career treating you these days?\" {initiator} asks, leaning back in their chair.",
            "\"{target}, I've been meaning to ask you about your career. Any exciting updates or challenges you'd like to share?\" {initiator} asks, genuinely intrigued.",
            "\"I've been thinking about our careers lately, {target}. Mind if we have a little chat about how things are going for you?\" {initiator} asks, smiling warmly.",
            "\"Tell me, {target}, how's your career journey been so far? Any interesting stories or milestones?\" {initiator} asks, leaning forward with anticipation.",
            "\"I've been curious about your career lately, {target}. Mind if I ask how you've been navigating the professional world?\" {initiator} asks, with a hint of curiosity in their voice."
        ],
    },
    'mixer_social_AskAboutFavoriteAuthor_targeted_Friendly_alwaysOn_skills': {
        "pre_actions": [
            "{initiator} asks {target} about their favorite author.",
        ],
        "actions": [
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
            "\"Did you have a good day {target}?\"",
            "\"What did you do today?\" {initiator} asks.",
            "\"Anything interesting happen today?\" {initiator} asks.",
            "\"How's your day been so far?\" {initiator} asks.",
            "\"How did your day go?\" {initiator} asks.",
            "\"What's been going on with you today?\" {initiator} asks.",
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
            "\"I just wanted to say, you're incredibly talented,\" {initiator} praises {target}.",
            "\"I can't help but admire your determination and hard work,\" {initiator} tells {target}.",
            "\"You have such a kind and caring heart,\" {initiator} compliments {target}.",
            "\"Your creativity never ceases to amaze me,\" {initiator} tells {target} with admiration.",
            "\"I wanted to let you know that you inspire me,\" {initiator} expresses to {target}.",
            "\"You have a way with words that captivates everyone around you,\" {initiator} praises {target}.",
            "\"Your generosity and selflessness are truly remarkable,\" {initiator} acknowledges {target}.",
            "\"I wanted to say that you're an extraordinary person,\" {initiator} tells {target} sincerely.",
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
        "actions": [
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
            "\"I've been fishing for years, {target}, let me share some tips with you,\" {initiator} offers.",
            "\"Are you interested in fishing, {target}? I can give you some valuable tips,\" {initiator} suggests.",
            "\"I heard you want to go fishing, {target}. Let me give you some advice,\" {initiator} offers kindly.",
            "\"I've discovered some great fishing techniques, {target}. Would you like me to share them with you?\" {initiator} asks with a smile.",
            "\"If you're planning to go fishing, {target}, I have some tips that might help you catch more fish,\" {initiator} offers eagerly.",
            "\"Fishing can be tricky, {target}, but I can give you some tips to make it easier,\" {initiator} says confidently.",
            "\"I've learned a few tricks that might improve your fishing experience, {target}. Would you like to hear them?\" {initiator} asks curiously.",
            "\"I noticed you're interested in fishing, {target}. How about I give you some pointers to get started?\" {initiator} suggests warmly.",
            "\"I've been studying different fishing techniques, {target}, and I think I have some valuable tips to share with you,\" {initiator} says excitedly.",
        ],
    },
    'mixer_social_GiveCookingTips_targeted_Friendly_alwaysOn_skills': {
        "pre_actions": [
            "{initiator} gives cooking tips to {target}."
        ],
        "actions": [
            "\"Hey {target}, I've got some cooking tips for you!\" {initiator} says excitedly.",
            "\"I've learned a few tricks in the kitchen. Mind if I share some cooking tips with you?\" {initiator} asks {target}.",
            "\"I've been experimenting with some new recipes. Would you like me to give you a few cooking tips?\" {initiator} offers {target}.",
            "\"You know, {target}, I've discovered some amazing cooking techniques. Can I give you a few tips?\" {initiator} suggests.",
            "\"I've been honing my culinary skills lately. Would you be interested in hearing some cooking tips from me?\" {initiator} asks {target}.",
            "\"I've come across some fantastic cooking hacks. How about I share a few tips with you?\" {initiator} proposes to {target}.",
            "\"I've been exploring the world of cooking lately and picked up some valuable tips. Would you like to hear them?\" {initiator} asks {target}.",
            "\"You're in luck, {target}. I've got some secret cooking tips that I'm willing to share with you!\" {initiator} teases playfully.",
            "\"I've been experimenting in the kitchen and stumbled upon some genius cooking tips. Want to hear them?\" {initiator} asks {target} with a smile.",
            "\"Cooking can be a lot of fun if you know some tricks. Mind if I pass on a few cooking tips to you, {target}?\" {initiator} offers generously.",
        ],
    },
    'mixer_social_ShareCookingSecrets_targeted_Friendly_alwaysOn_skills': {
        "pre_actions": [
            "{initiator} shares their cooking secrets with {target}."
        ],
        "actions": [
            "\"You know, {target}, I have this amazing recipe I want to share with you,\" {initiator} says enthusiastically.",
            "\"I've been experimenting in the kitchen lately, and I've discovered some fantastic cooking secrets. Would you like me to share them with you, {target}?\" {initiator} suggests.",
            "\"I've learned a few cooking tricks that have made a world of difference in my meals. Mind if I pass them on to you, {target}?\" {initiator} offers.",
            "\"{target}, I've been perfecting my cooking skills, and I think I've unlocked some secrets that could elevate your dishes. Can I enlighten you?\" {initiator} proposes.",
            "\"Cooking is my passion, {target}, and I'd love to share some of my secrets with you. Are you interested?\" {initiator} asks with a smile.",
            "\"You won't believe the cooking hacks I've discovered, {target}. Would you like me to reveal them to you?\" {initiator} asks, unable to contain their excitement.",
            "\"I've stumbled upon some culinary secrets that can turn an ordinary meal into a masterpiece. Want me to spill the beans, {target}?\" {initiator} teases.",
            "\"{target}, I've been honing my cooking skills, and I have a few secrets up my sleeve. Care to hear them?\" {initiator} suggests with a mysterious grin.",
            "\"I've been reading up on cooking techniques, and I think you'd find some of them helpful, {target}. Mind if I share them with you?\" {initiator} offers politely.",
            "\"I've been experimenting with flavors and techniques in the kitchen lately, {target}, and I'd love to share what I've learned. Interested?\" {initiator} proposes with anticipation.",
        ],
    },
    'mixer_social_EvangelizeGrilledCheese_Friendly_alwaysOn_Trait': {
        "pre_actions": [
            "{initiator} extolls the virtues of grilled cheese to {target}."
        ],
        "actions": [
            "\"You won't believe the amazingness of grilled cheese, {target}!\" {initiator} exclaims.",
            "\"Have you ever experienced the pure delight of a perfectly grilled cheese sandwich?\" {initiator} asks {target}.",
            "\"Let me tell you about the magic of grilled cheese, {target}!\" {initiator} enthuses.",
            "\"Have you tried the heavenly combination of melty cheese and crispy bread in a grilled cheese sandwich?\" {initiator} asks {target}.",
            "\"Prepare to have your taste buds revolutionized, {target}! Grilled cheese is the answer to all cravings,\" {initiator} declares.",
            "\"I can't contain my excitement about grilled cheese! You must try it, {target}!\" {initiator} insists.",
            "\"Grilled cheese is more than just a sandwich, it's a culinary experience. Trust me, {target},\" {initiator} says persuasively.",
            "\"Let me share my love for grilled cheese with you, {target}. It's the ultimate comfort food,\" {initiator} suggests with a smile.",
            "\"Grilled cheese is a masterpiece of simplicity. Don't you agree, {target}?\" {initiator} inquires eagerly.",
            "\"I've discovered the secret to the most delicious grilled cheese. Would you like to know, {target}?\" {initiator} teases.",
        ],
    },
    'mixer_social_Flatter_targeted_Friendly_alwaysOn': {
        "pre_actions": [
            "{initiator} flatters {target} by boosting their ego."
        ],
        "actions": [
            "\"You look absolutely stunning today, {target},\" {initiator} compliments.",
            "\"I must say, {target}, your talent never ceases to amaze me,\" {initiator} says with admiration.",
            "\"I couldn't help but notice how incredibly intelligent you are, {target},\" {initiator} compliments.",
            "\"You have such a captivating smile, {target},\" {initiator} remarks fondly.",
            "\"I wanted to let you know that you're an incredibly kind-hearted person, {target},\" {initiator} compliments sincerely.",
            "\"You have an amazing sense of style, {target},\" {initiator} comments with appreciation.",
            "\"I'm in awe of your creativity, {target},\" {initiator} admires.",
            "\"You always manage to bring positivity to any situation, {target},\" {initiator} praises warmly.",
            "\"Your dedication and hard work are truly inspiring, {target},\" {initiator} expresses with admiration.",
            "\"I just wanted to say that you're a remarkable individual, {target},\" {initiator} compliments sincerely.",
        ],
    },
    'mixer_social_GiveRelationshipAdvice_targeted_friendly_emotionSpecific': {
        "pre_actions": [
            "{initiator} gives relationship advice to {target}, in a friendly way."
        ],
        "actions": [
            "\"You know, {target}, I've been thinking about your relationship...\"",
            "\"I have some relationship advice for you, {target}.\"",
            "\"I've been reading this book about relationships, and I think it could help you, {target}.\"",
            "\"I've noticed a few things about your relationship, {target}, and I wanted to share my thoughts.\"",
            "\"I've been through similar situations in my own relationships, {target}, and I think I can offer you some advice.\"",
            "\"I think you should consider a different approach in your relationship, {target}.\"",
            "\"Do you mind if I give you some relationship advice, {target}?\"",
            "\"I've been observing your relationship, {target}, and I believe I have some insights to share.\"",
            "\"Have you thought about trying this new technique in your relationship, {target}?\"",
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
            "{initiator} confesses a profound, deeply-held secret to {target}."
        ],
        "actions": [
            "\"{target}, I need to tell you something. Promise me you won't judge,\" {initiator} says nervously.",
            "\"I have been keeping a secret for so long, but I trust you enough to share it with you,\" {initiator} says, looking into {target}'s eyes.",
            "\"You know, {target}, there's something I've never told anyone before, but I feel like I can confide in you,\" {initiator} says, hesitatingly.",
            "\"I've been carrying this secret for far too long, and it's eating me up inside. {target}, I think it's time I share it with you,\" {initiator} confesses, their voice trembling.",
            "\"I never thought I would reveal this, but you mean a lot to me, {target}. I need you to know the truth,\" {initiator} says, taking a deep breath.",
            "\"There's something I've been hiding, {target}, and it's time I let it out. I hope you can handle it,\" {initiator} says, looking anxious.",
            "\"I've kept this hidden for years, {target}, but I can't bear the weight anymore. I have to tell you,\" {initiator} admits, looking vulnerable.",
            "\"This secret has haunted me for so long, {target}, but I feel a connection with you that makes me want to share it. Can I trust you?\" {initiator} asks cautiously.",
            "\"I've always admired your ability to keep secrets, {target}, but there's one I can no longer keep to myself. Brace yourself,\" {initiator} says, preparing to share something profound.",
            "\"I've been meaning to tell you this, {target}, but I've never found the right time. Now, in this moment, I feel it's the right moment to reveal my deepest secret,\" {initiator} says with a mixture of relief and apprehension.",
        ],
    },
    'mixer_social_RevealEvilPlans_targeted_mischief_traits': {
        "pre_actions": [
            "{initiator} reveals their evil plans to {target}."
        ],
        "actions": [
            "\"{target}, I have a confession to make. Brace yourself, for what I'm about to reveal is truly sinister,\" {initiator} says with a wicked grin.",
            "\"I've been living a double life, {target}, and i's time you know the truth. Prepare yourself for the darkness that lies within me,\" {initiator} says, their voice dripping with malevolence.",
            "\"You thought you knew me, {target}, but you were wrong. The truth is, I've been plotting something truly diabolical, and now it's time to involve you,\" {initiator} says, eyes gleaming with mischief.",
            "\"Listen carefully, {target}, for the secrets I'm about to share will change everything. I've been working on a plan, a plan so evil that it will shake the very foundations of this world,\" {initiator} whispers ominously.",
            "\"I've always been envious of your innocence, {target}, but no more. Today, I reveal my true nature, and you'll witness the depths of my malevolence firsthand,\" {initiator} declares, a twisted smile forming on their lips.",
            "\"Prepare to be shocked, {target}, for the darkness that resides within me is about to be unleashed. My evil plans will leave a trail of chaos and destruction,\" {initiator} says, their voice laced with anticipation.",
            "\"You see, {target}, I've been biding my time, waiting for the perfect moment to reveal my evil plans. And that moment is now,\" {initiator} says, a wicked glint in their eyes.",
            "\"I hope you're ready for this, {target}, because what I'm about to disclose will shatter your perception of me. My evil schemes are far more intricate than you could have ever imagined,\" {initiator} says, relishing the impending revelation.",
            "\"There's a darkness inside me, {target}, and it's time you witness it. My evil plans are nearing fruition, and you're about to become an integral part of them,\" {initiator} says, a sinister chuckle escaping their lips.",
            "\"I've kept my true intentions hidden for far too long, {target}. Today, I lay bare my evil plans before you, and together, we shall conquer this world,\" {initiator} proclaims, their voice filled with twisted ambition.",
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
            "{initiator} spitefully throws their drink at {target}."
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
            "\"{target}, I've been wondering what you're passionate about. Care to share?\"",
            "\"Hey {target}, you know, we've never really talked about our hobbies and interests. What do you enjoy doing in your free time?\"",
            "\"So, {target}, I've been meaning to ask you - what is it that you're truly interested in?\"",
            "\"{target}, we've known each other for a while now, but I feel like there's still so much to learn about each other. What are your interests?\"",
            "\"I was thinking, {target}, that it's about time we talk about what makes us tick. What are you passionate about?\"",
            "\"Hey {target}, I'd love to know more about your interests and hobbies. Maybe we have something in common.\"",
            "\"{target}, we've talked about so many things, but not about our interests. I'd love to hear about yours.\"",
            "\"You know, {target}, I've always been curious about what you're truly passionate about. Care to enlighten me?\"",
            "\"{target}, I was just thinking about how our friendship has grown, and I realized we've never really discussed our interests. What do you like to do for fun?\"",
            "\"Let's talk about something different today, {target}. Tell me about your interests and what makes you happy.\""
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
            "{initiator} calms {target} down in a caring and friendly way.",
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
            "{initiator} angrily starts a physical fight with {target}."
        ],
        "actions": [
            "\"{target}, I've had enough of your arrogance. It's time to put you in your place,\" {initiator} growls, preparing for a physical confrontation.",
            "\"Enough is enough, {target}! I'm tired of you always trying to control everything. We need to settle this,\" {initiator} shouts, their patience wearing thin.",
            "\"{target}, you've pushed me too far. Prepare yourself,\" {initiator} says, clenching their fists.",
            "\"I never thought it would come to this, {target}, but you've left me with no choice. We need to fight this out,\" {initiator} says, frustration evident in their voice.",
            "\"Your constant meddling in my life has finally pushed me over the edge, {target}. It's time we settle our differences,\" {initiator} declares, their eyes narrowed in anger.",
            "\"Enough is enough, {target}! It's time we settle this once and for all!\" {initiator} shouts, charging towards {target}.",
            "\"Sometimes talking just isn't enough, {target}. Let's resolve this the old-fashioned way,\" {initiator} suggests, their voice filled with determination.",
            "\"{target}, you've provoked me for the last time. I'm not going to let you walk all over me anymore. Let's do this,\" {initiator} challenges, stepping forward.",
            "\"{target}, I've held back for too long. It's time you realized the consequences of your actions,\" {initiator} snarls, launching themselves at {target}.",
            "\"You've crossed the line, {target}, and now you'll pay the price,\" {initiator} declares, throwing a fierce punch.",
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
            "{initiator} hip bumps {target} as a way to break the tension and initiate a more lighthearted conversation."
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
        "pre_actions": [
            "{initiator} cruelly insults {target}.",
        ],
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
        "pre_actions": [
            "{initiator} shares their insecurities with {target}.",
        ],
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
        "pre_actions": [
            "{initiator} begins reading a love poem they wrote for {target}.",
        ],
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
        "pre_actions": [
            "{initiator} begins publicly serenading {target} romantically.",
        ],
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
        "pre_actions": [
            "{initiator} shares their bartending secrets with {target}.",
        ],
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
        "pre_actions": [
            "{initiator} begins romantically expressing their loyal, romantic devotion towards {target}.",
        ],
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
            "{initiator} looks at {target} and says, \"What do you call a penguin in the desert? Lost!\" hoping to make them laugh."
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
            "\"Corporate culture is like a cult, {target}, but instead of chanting, they're spouting off empty slogans and talking about 'disrupting the industry,\" {initiator} says with a grin.",
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
            "{initiator} starts making silly faces at {target} from across the room, hoping to make them laugh.",
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
            "{initiator} sweet talks {target} romantically."
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
            "{initiator} mischeviously dares {target} to streak naked.",
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
        "pre_actions": [
            "{initiator} gives {target} a kiss.",
        ],
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
        "pre_actions": [
            "{initiator} strikes a seductive pose for {target}.",
        ],
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
        "pre_actions": [
            "{initiator}, feeling romantic, kisses {target} intimately.",
        ],
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
        "pre_actions": [
            "{initiator} initiates a passionate, romantic kiss with {target}.",
        ],
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
        "pre_actions": [
            "{initiator} initiates their first kiss with {target}.",
        ],
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
        "pre_actions": [
            "{initiator} begins embracing {target} romantically.",
        ],
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
        "pre_actions": [
            "{initiator} romantically initiates sex with {target}.",
        ],
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
        "pre_actions": [
            "{initiator}, feeling romantic, asks {target} for a massage.",
        ],
        "actions": [
            "\"{target}, I was wondering if you could do me a favor. Do you think you could give me a massage?\" {initiator} asks, looking hopeful.",
            "\"You know, {target}, my body has been feeling really tense lately. Would you mind giving me a massage?\" {initiator} requests, giving a sheepish smile.",
            "\"I've been so stressed lately, {target}, and I was wondering if you could help me relax. Would you be up for giving me a massage?\" {initiator} asks, their eyes pleading.",
            "\"I've heard you give amazing massages, {target}, and I was hoping you could work your magic on me. Would you be willing to give me one?\" {initiator} asks, a touch of flirtation in their voice.",
            "\"{target}, I've been thinking about this for a while now, and I finally gathered the courage to ask - would you be willing to give me a massage?\" {initiator} asks, their cheeks turning slightly pink.",
            "\"I've been hearing great things about your massage skills, {target}, and I was wondering if you could give me one. I could really use some relaxation,\" {initiator} says, sounding hopeful.",
            "\"{target}, I have a favor to ask. Would you mind giving me a massage? I promise I'll return the favor,\" {initiator} says, giving {target} a playful grin.",
            "\"I've been feeling really tense lately, {target}, and I was thinking maybe a massage from you could help. Would you be open to giving me one?\" {initiator} asks, their voice filled with anticipation.",
            "\"{target}, I have a confession to make - I've been secretly wanting a massage from you for a while now. Is that something you'd be interested in?\" {initiator} asks, feeling a mix of nervousness and excitement.",
            "\"I've been longing for a massage, {target}, and I can't think of anyone better to do it than you. Would you be willing to help me out?\" {initiator} asks, their eyes filled with longing."
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
            "{initiator} fights {target}, who is a super villain.",
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
    "mixer_social_Pickpocket_targeted_mischief_career_household": {
        # J: I Need to see animation in the game before context - current actions sound more like robbing. Also, what is the distinction between 'career_household" and "career?" (3020 and 3034)
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
        "pre_actions": [
            "{initiator} attempts to pickpocket {target}.",
        ],
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
            "{initiator} gives fake investment tips to {target}.",
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
            "{initiator} uses a special device as a secret agent on {target}, once they shake hands it knocks {target} unconscious.",
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
            "{initiator} gossips about the office romance with {target}, their coworker.",
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
            "{initiator} points out constellations to {target}.",
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
        "pre_actions": [
            "{initiator} interviews {target} for a story, as a writer.",
        ],
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
        "pre_actions": [
            "{initiator} starts a conversation about bestseller novels to {target}.",
        ],
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
        "pre_actions": [
            "{initiator} performs a secret villain handshake with {target}, in order to determine if they are a villain."
        ],
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
        "pre_actions": [
            "{initiator} exposes {target} as a supervillain."
        ],
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
        "pre_actions": [
            "{initiator} enthuses about space to {target}",
        ],
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
        "pre_actions": [
            "{initiator} interviews {target} about their life, as a writer."
        ],
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
        "pre_actions": [
            "{initiator} imitates their and {target}'s boss, to make them laugh."
        ],
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
        "pre_actions": [
            "{initiator} offers career advice to {target}."
        ],
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
        "pre_actions": [
            "{initiator}, who is ambitious, gives career advice to {target}."
        ],
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
        "pre_actions": [
            "{initiator} warns {target} not to talk about Crime Club."
        ],
        "actions": [
            "\"{target}, I need you to promise me something. Never bring up the Crime Club in public,\" {initiator} says in a serious tone.",
            "\"Listen, {target}, it's really important that you never mention the Crime Club around others. We have to keep it a secret,\" {initiator} warns.",
            "\"{target}, if there's one thing you must remember, it's that you cannot talk about Crime Club. It's for our own safety,\" {initiator} says urgently.",
            "\"Please, {target}, be careful with your words. Don't ever let the Crime Club slip into any conversation,\" {initiator} pleads.",
            "\"I can't stress this enough, {target}. Keep the Crime Club to yourself. No one else can know,\" {initiator} says, looking {target} in the eye.",
            "\"Remember, {target}, the first rule of Crime Club is that you do not talk about Crime Club,\" {initiator} reminds with a stern expression.",
            "\"Never let your guard down, {target}. We can't afford to have people find out about the Crime Club,\" {initiator} says firmly.",
            "\"Talking about Crime Club could put us all in danger, {target}. Be cautious with what you say,\" {initiator} advises.",
            "\"Keep this between us, {target}. The Crime Club stays a secret, no matter the circumstances,\" {initiator} insists.",
            "\"I trust you, {target}, but I need you to understand the importance of not discussing the Crime Club with anyone. Can you promise me that?\" {initiator} asks earnestly."
        ],
    },
    "mixer_social_AskAbout_PrizedPossessions_mischief_alwaysOn_trait": {
        "pre_actions": [
            '{initiator} mischievously asks {target} about their prized possessions.',
        ],
        "actions": [
            "\"So, {target}, what are your most prized possessions?\" {initiator} asks with a mischievous grin.",
            "{initiator} playfully nudges {target} and says, \"Come on, spill the beans! What are your most treasured belongings?\"",
            "With a twinkle in their eye, {initiator} leans in and whispers, \"Tell me, {target}, what do you hold most dear in this world?\"",
            "{initiator} smirks and teases, \"You know, {target}, I'm dying to know what you value the most. Care to share?\"",
            "Curiosity piqued, {initiator} leans closer to {target} and inquires, \"So, what's the one thing you can't live without, {target}?\"",
            "{initiator} playfully prods {target} and asks, \"Hey, {target}, what's your secret stash of prized possessions?\"",
            "Eagerly, {initiator} asks {target}, \"Do you have any special items that hold a special place in your heart?\"",
            "With a sly grin, {initiator} challenges {target}, \"I bet you have some hidden treasures. Care to divulge?\"",
            "{initiator} raises an eyebrow and says, \"I have a feeling you've got some interesting prized possessions. Care to enlighten me, {target}?\"",
            "{initiator} leans back, smirking, and says, \"Okay, {target}, spill the beans. What's your most prized possession?\"",
        ],
    },
    "mixer_social_AskAboutBeingOld_targeted_Friendly_alwaysOn_child": {
        "pre_actions": [
            "{initiator}, who is a child, asks {target} what it is like to be old.",
        ],
        "actions": [
            "\"{target}, what is it like to be old?\" {initiator} asks curiously, their eyes wide with innocence.",
            "\"Can you tell me, {target}, what it's like to be all grown up? I really want to know,\" {initiator} asks, looking up at {target} with curiosity.",
            "\"Do you remember what it was like to be my age, {target}? I wonder what it's like to be old,\" {initiator} asks, tilting their head inquisitively.",
            "\"I heard grown-ups have all the answers. Is that true, {target}? What's it like to be old?\" {initiator} asks, their voice filled with wonder.",
            "\"{target}, can you teach me what it's like to be old? I want to know everything,\" {initiator} says, looking up at {target} with admiration.",
            "\"I think being old must be really cool. Don't you, {target}? Can you tell me what it's like?\" {initiator} asks, bouncing with excitement.",
            "\"{target}, when I grow up, will I be just like you? Can you tell me what it's like to be old?\" {initiator} asks, their eyes sparkling with curiosity.",
            "\"{target}, I don't understand what it's like to be old. Can you explain it to me?\" {initiator} asks, their brow furrowing in confusion.",
            "\"I wish I could be old like you, {target}. Can you tell me what it's like?\" {initiator} asks, gazing at {target} with admiration.",
            "\"{target}, what's the best part about being old? I want to know everything,\" {initiator} asks, their voice filled with anticipation."
        ]
    },
    "mixer_social_AskDueDate_targeted_friendly_alwaysOn_Pregnancy": {
        "pre_actions": [
            "{initiator} asks {target}, who is pregnant, when their baby is due to be born."
        ],
        "actions": [
            "\"Congratulations, {target}! When is the little one due?\" {initiator} asks, smiling warmly.",
            "\"I couldn't help but notice that pregnancy glow, {target}. When can we expect to meet the baby?\" {initiator} asks, excitement evident in their voice.",
            "\"{target}, I've been dying to know - when is the baby expected to arrive?\" {initiator} inquires eagerly.",
            "\"{target}, forgive me if it's too personal, but I can't help but wonder when your bundle of joy will make their grand entrance. Care to share?\" {initiator} asks, trying to contain their curiosity.",
            "\"I hope you don't mind me asking, {target}, but I'm so excited for you. When is the baby due?\" {initiator} asks, their eyes sparkling with anticipation.",
            "\"{target}, I've been counting down the days since I heard the news. Can you tell me when the baby is expected to arrive?\" {initiator} asks, unable to hide their enthusiasm.",
            "\"I don't mean to pry, {target}, but I'm overjoyed for you. When is the baby expected to join us?\" {initiator} asks, genuinely interested.",
            "\"Your pregnancy has been such a beautiful journey to witness, {target}. When will the little one grace us with their presence?\" {initiator} asks, a hint of awe in their voice.",
            "\"I hope you don't mind me asking, {target}, but I'm eager to know - when is your baby due?\" {initiator} asks, a twinkle of excitement in their eyes.",
            "\"{target}, I can't contain my excitement any longer. When is the baby expected to arrive?\" {initiator} asks, barely able to hide their anticipation."
        ]
    },
    "mixer_social_CaressCheek_targeted_romance_highScore": {
        "pre_actions": [
            "{initiator} romantically caresses {target}'s face.",
        ],
        "actions": [
            "{initiator} gently cups {target}'s face, their touch lingering.",
            "With a soft touch, {initiator} traces {target}'s jawline, their eyes filled with affection.",
            "{initiator}'s fingertips glide across {target}'s cheek, a tender gesture that speaks volumes.",
            "As {initiator}'s hand brushes {target}'s face, a surge of warmth spreads between them.",
            "In a moment of vulnerability, {initiator} caresses {target}'s face, silently expressing their emotions.",
            "The touch of {initiator}'s hand against {target}'s cheek sends shivers down their spine.",
            "With a gentle stroke, {initiator} softly caresses {target}'s face, their eyes locked in a mesmerizing gaze.",
            "{initiator} leans in, their fingers lightly grazing {target}'s cheek, igniting a spark of intimacy.",
            "As {initiator}'s hand comes into contact with {target}'s face, time seems to stand still for a fleeting moment.",
            "In an act of tenderness, {initiator} cups {target}'s face, their touch conveying a depth of emotion."
        ]
    },
    "mixer_social_ComplimentOutfit_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} compliments {target}'s outfit.",
        ],
        "actions": [
            "\"{target}, I have to say, you look absolutely stunning in that outfit,\" {initiator} compliments, admiringly.",
            "\"Wow, {target}, your outfit is on point! You have such great fashion sense,\" {initiator} praises, smiling.",
            "\"Can I just say, {target}, you look incredible in that outfit. It really suits you,\" {initiator} compliments with genuine admiration.",
            "\"Your outfit is giving me serious style envy, {target}. You always know how to put together the perfect look,\" {initiator} compliments, slightly envious.",
            "\"{target}, you never fail to impress me with your fashion choices. That outfit is no exception. You look amazing,\" {initiator} compliments, appreciatively.",
            "\"I can't help but notice how fabulous you look today, {target}. Your outfit is a total showstopper,\" {initiator} compliments, impressed.",
            "\"Okay, {target}, you officially win the award for best-dressed. That outfit is absolutely fantastic,\" {initiator} compliments, playfully.",
            "\"I have to say, {target}, your outfit is giving me serious fashion inspiration. You always manage to look effortlessly stylish,\" {initiator} compliments, genuinely impressed.",
            "\"Can I just take a moment to appreciate how well you put together that outfit, {target}? You have an amazing sense of style,\" {initiator} compliments, sincerely.",
            "\"{target}, you always manage to look so put-together and fashionable. Your outfit today is no exception. You look absolutely fabulous,\" {initiator} compliments, genuinely."
        ]
    },
    "mixer_Social_GetToKnow_Friendly_STC": {  # J: Having issue where {target}'s name does not pop up
        "pre_actions": [
            "{initiator} starts a conversation with {target}, in order to get to know them better."
        ],
        "actions": [
            "\"Hey {target}, mind if I ask you a few questions? I'm curious to know more about you,\" {initiator} says with a friendly smile.",
            "\"I've been watching you from afar, {target}, and I can't help but wonder what makes you tick. Care to share?\" {initiator} asks, genuinely interested.",
            "\"You seem like an intriguing person, {target}. Mind if I dig a little deeper and get to know you better?\" {initiator} asks, leaning in attentively.",
            "\"I've heard so much about you, {target}, and I've been dying to know more. Care to indulge me in a conversation?\" {initiator} asks, with a hint of excitement.",
            "\"Mind if I join you for a chat, {target}? I have this urge to discover the layers beneath that enigmatic smile of yours,\" {initiator} says, gesturing towards an empty seat.",
            "\"I hope you don't mind me being forward, {target}, but I feel a strong connection with you and I'd love to explore that through conversation,\" {initiator} says, looking intently into {target}'s eyes.",
            "\"I've been meaning to get to know you better, {target}, and I thought it's about time we had a heartfelt conversation. Are you up for it?\" {initiator} suggests, hoping for a positive response.",
            "\"You strike me as someone with stories to tell, {target}. Mind if I sit down and listen?\" {initiator} asks, curiosity sparking in their eyes.",
            "\"Life is too short for small talk, {target}. How about we dive deep into each other's worlds and have a meaningful conversation?\" {initiator} proposes, eager to connect on a deeper level.",
            "\"I have this burning desire to unravel the mystery that is {target}. Mind if I ask you a few questions?\" {initiator} asks, unable to contain their curiosity."
        ]
    },
    "mixer_social_InsideJoke_group_Funny_MediumScore": {
        "pre_actions": [
            "{initiator} shares an inside joke with {target}.",
        ],
        "actions": [
            "\"{target}, remember that time we got caught in the rain and ended up dancing like crazy people? Every time it rains, I can't help but smile,\" {initiator} reminisces, laughing.",
            "\"I was going through old photos and came across this one. It instantly reminded me of that inside joke we share. Wanna take a trip down memory lane?\" {initiator} suggests, showing {target} the picture.",
            "\"You know, {target}, every time I see a certain object or hear a specific phrase, it always reminds me of that hilarious inside joke we have. It's like a secret language only we understand,\" {initiator} chuckles, waiting for {target}'s reaction.",
            "\"I've been having a tough day, but then I remembered that inside joke we share. It instantly brought a smile to my face. Thanks for being the reason behind my laughter,\" {initiator} says, grinning at {target}.",
            "\"{target}, I heard someone say something today that reminded me of our inside joke. It made me burst out laughing in the middle of a meeting. People thought I was crazy,\" {initiator} confesses, shaking their head with amusement.",
            "\"You won't believe what I found! It's that item we used in our inside joke. I couldn't resist buying it. It's a constant reminder of the good times we've had,\" {initiator} says, excitedly showing {target} the item.",
            "\"I came across a video clip that perfectly captures that inside joke we have. It's hilarious! Wanna watch it together?\" {initiator} asks, eager to relive the funny memory with {target}.",
            "\"You know, {target}, sometimes when I'm feeling down, I think about that inside joke we share, and it instantly lifts my spirits. It's like our own secret source of happiness,\" {initiator} admits, smiling warmly.",
            "\"I was telling someone a funny story today, and it reminded me of our inside joke. It's amazing how a simple memory can make me laugh so hard,\" {initiator} says, chuckling at the thought.",
            "\"{target}, I can't help but smile whenever I think about that inside joke we have. It's like our little secret that brings joy to my heart,\" {initiator} confesses, looking at {target} with fondness."
        ]
    },
    "mixer_social_TryOutMaterial_targeted_funny_alwaysOn": {
        "pre_actions": [
            "{initiator}, an aspiring comedian, tries out new joke material for their standup routine on {target}.",
        ],
        "actions": [
            "\"Hey {target}, have you ever noticed that...\"",
            "\"{target}, You know you're getting old when...\"",
            "\"Hey {target}, What's the deal with...\"",
            "\"{target}, Why is it that...\"",
            "\"Man, {target}, don't you just hate it when...\"",
            "\"So, {target}, I was walking down the street the other day, and...\"",
            "\"Hey {target}, Let's talk about relationships, because...\"",
            "\"So, {target}, I was talking to my friend the other day and...\"",
            "\"So, {target}, I got into an argument with a stranger and...\""
        ]
    },
    "mixer_social_TeachValuableLesson_targeted_Friendly_HighScore_child": {
        "pre_actions": [
            "{initiator} teaches a valuable lesson to {target}, who is a child.",
        ],
        "actions": [
            "\"Hey {target}, can I share something with you? It's a lesson that I've learned, and I think it will help you too,\" {initiator} says with a warm smile.",
            "\"You know, {target}, one of the most important things I've learned in life is the value of kindness. It can make such a big difference,\" {initiator} says, looking at {target} intently.",
            "\"I want to tell you a story, {target}, about a time when I learned an important lesson about honesty. It's something that has stuck with me ever since,\" {initiator} says, sitting down next to {target}.",
            "\"You know, {target}, sometimes things don't go the way we want them to, and it's okay to feel disappointed. But what's important is how we bounce back from it,\" {initiator} says, offering {target} a comforting smile.",
            "\"I remember when I was your age, {target}, I used to get really frustrated when things didn't go my way. But then I learned a valuable lesson about patience,\" {initiator} says, sitting down beside {target}.",
            "\"Have you ever heard the saying, 'It's not about how many times you fall, but how many times you get back up'? Well, {target}, that's a lesson that has helped me through some tough times,\" {initiator} says, looking at {target} with encouragement.",
            "\"You know, {target}, it's easy to get caught up in comparing ourselves to others. But the truth is, we all have our own unique strengths and talents,\" {initiator} says, smiling warmly at {target}.",
            "\"I think one of the most important things you can learn, {target}, is to believe in yourself. When you have confidence, you can accomplish amazing things,\" {initiator} says, looking at {target} with encouragement.",
            "\"{target}, it's important to remember that mistakes are a part of life. We all make them, but what matters is how we learn from them and grow,\" {initiator} says, offering {target} a reassuring smile.",
            "\"I want to tell you something, {target}, that I wish someone had told me when I was your age. It's a lesson about the power of perseverance,\" {initiator} says, sitting down next to {target}."
        ]
    },
    "mixer_Social_Romance_AskAboutSexualOrientation": {
        "pre_actions": [
            "{initiator} asks {target} about their sexual orientation.",
        ],
        "actions": [
            "\"{target}, I hope you don't mind me asking, but I've been curious about something. Can I ask you about your sexual orientation?\" {initiator} asks cautiously.",
            "\"I've been wondering about this for a while, and I hope you feel comfortable enough to share with me. What is your sexual orientation, {target}?\" {initiator} asks, trying to sound nonchalant.",
            "\"Hey {target}, I've been wanting to talk to you about something personal. Can I ask you about your sexual orientation?\" {initiator} asks, looking slightly nervous.",
            "\"Sexual orientation is an important aspect of who we are, and I've been wanting to understand you better, {target}. Would you mind sharing your sexual orientation with me?\" {initiator} asks, with genuine curiosity.",
            "\"Hey {target}, I hope you don't mind me bringing this up, but I've been curious about your sexual orientation. Would you be open to discussing it with me?\" {initiator} asks, hoping not to offend.",
            "\"Can I ask you a personal question, {target}? I've been wondering about your sexual orientation. Would you be comfortable sharing it with me?\" {initiator} asks, trying to sound respectful.",
            "\"Hey {target}, I have something I've been meaning to ask you. Can we talk about your sexual orientation? I promise it's with good intentions,\" {initiator} asks, seeking understanding.",
            "\"I hope you don't find this question intrusive, {target}, but I've been wanting to know more about you. Can we talk about your sexual orientation?\" {initiator} asks, hoping for an honest conversation.",
            "\"I've been thinking about this topic a lot lately, {target}, and I trust you enough to talk about it. Can we discuss your sexual orientation?\" {initiator} asks, wanting to deepen their connection.",
            "\"{target}, I hope you don't mind me being curious, but can we have an open conversation about your sexual orientation? I'm genuinely interested in understanding you better,\" {initiator} asks, with a hint of vulnerability."
        ]
    },
    "mixer_Social_SexualOrientation_AskAboutWooHooInterests": {
        "pre_actions": [
            "{initiator} asks {target} about their sexual desires.",
        ],
        "actions": [
            "\"{target}, can I ask you something personal? I've been curious about your sexual desires,\" {initiator} says, trying to sound nonchalant.",
            "\"I hope you don't mind me asking, but I've always wondered about your sexual preferences, {target},\" {initiator} says, with a hint of curiosity.",
            "\"I've been thinking a lot about sexuality lately, and I'm curious about your desires, {target}. Would you be comfortable sharing?\" {initiator} asks, cautiously.",
            "\"{target}, I trust you, and I want to have an open conversation about our sexual desires. Would you be willing to share yours with me?\" {initiator} asks, hoping for an honest response.",
            "\"I've always believed that open communication is important, especially when it comes to our sexual desires. Can we talk about it, {target}?\" {initiator} asks, hoping for an open conversation.",
            "\"{target}, I've been exploring my own sexuality lately, and I'm curious to know about yours. Are you comfortable discussing it with me?\" {initiator} asks, seeking a deeper understanding.",
            "\"I've been reading about different sexual preferences, and it made me wonder about your desires, {target}. Would you mind sharing your thoughts with me?\" {initiator} asks, genuinely interested.",
            "\"{target}, I've been reflecting on my own sexual desires, and I thought it would be interesting to hear about yours. Can we have an open conversation about it?\" {initiator} suggests, hoping for an open-minded response.",
            "\"I've been feeling a lot more comfortable discussing sexuality lately, and I was wondering if you'd be open to sharing your own sexual desires, {target},\" {initiator} asks, trying to create a safe space for conversation.",
            "\"{target}, I've always admired your confidence in expressing yourself. I'm curious to know more about your sexual desires, if that's something you're comfortable discussing,\" {initiator} asks, hoping for an open and honest conversation."
        ]
    },
    "mixer_Social_SexualOrientation_AskToBeWooHooPartners": {
        "pre_actions": [
            "{initiator} asks {target} to be their sexual partner.",
        ],
        "actions": [
            "\"{target}, I need to talk to you about something that's been on my mind. It's a sensitive topic, but I trust you enough to have this conversation,\" {initiator} says, their voice filled with nervousness.",
            "\"I've been thinking a lot about our relationship lately, {target}, and there's something I want to propose to you,\" {initiator} says, cautiously.",
            "\"You know, {target}, we've always had a strong connection, and I can't help but wonder if there's something more between us,\" {initiator} says, their words laced with uncertainty.",
            "\"I've been wrestling with this idea for a while now, {target}, and I can't keep it to myself any longer. Can we talk about the possibility of taking our relationship to a more intimate level?\" {initiator} asks, their voice trembling slightly.",
            "\"There's something I've been meaning to discuss with you, {target}, but I'm not sure how you'll react. Can we have an open conversation about our desires and boundaries?\" {initiator} asks, seeking reassurance.",
            "\"I hope you won't judge me for what I'm about to say, {target}, but I can't deny the attraction I feel towards you. Can we explore the idea of being more than just friends?\" {initiator} asks, their voice filled with vulnerability.",
            "\"I know this might come as a surprise, {target}, but I've been thinking about us in a different light lately. Would you be open to discussing the possibility of a physical relationship?\" {initiator} asks, their tone hesitant.",
            "\"I've never brought this up before, {target}, but I can't ignore the chemistry between us. Can we have an honest conversation about the potential for a romantic connection?\" {initiator} asks, their voice filled with anticipation.",
            "\"I've been keeping this desire hidden, {target}, but I feel like I can trust you enough to share it. Can we talk about the possibility of taking our friendship to a more intimate level?\" {initiator} asks, their words tinged with nervousness.",
            "\"{target}, I've been grappling with this idea for a while, and I feel like I can't move forward without discussing it with you. Can we talk about the possibility of becoming more than just friends?\" {initiator} asks, their voice filled with apprehension."
        ]
    },
    "mixer_social_SitIntimate_GiveMassage_targeted_romance_highScore": {
        "pre_actions": [
            "{initiator} offers to give {target} a sexual massage.",
        ],
        "actions": [
            "\"{target}, I have something special in mind for tonight. How about I give you a sensual massage to start things off?\" {initiator} suggests, raising an eyebrow suggestively.",
            "\"You know, {target}, I've been studying massage techniques lately. How about I give you a full-body massage as a little foreplay?\" {initiator} proposes with a mischievous smile.",
            "\"I've been thinking about a different way to spice things up, {target}. How about I give you an intimate massage before we get things heated?\" {initiator} suggests, biting their lip seductively.",
            "\"{target}, I want to explore new ways to pleasure you. How about I start with a sensual massage to set the mood?\" {initiator} suggests, running their fingers lightly over {target}'s arm.",
            "\"I've been practicing my massage skills lately, and I think you'd enjoy the benefits, {target}. How about I give you a tantalizing massage before we take it further?\" {initiator} proposes, their voice filled with anticipation.",
            "\"{target}, I have a surprise for you tonight. How about I give you an erotic massage to kick off our intimate time together?\" {initiator} suggests, their eyes gleaming with desire.",
            "\"I've been reading about the power of touch, {target}, and I'd love to show you what I've learned. How about I give you a passionate massage before we delve into deeper pleasures?\" {initiator} proposes, their voice filled with excitement.",
            "\"{target}, I want to pamper you tonight. How about I start by giving you a sensual massage to awaken your senses?\" {initiator} suggests, their fingers tracing delicate patterns on {target}'s thigh.",
            "\"I've been thinking about ways to heighten our pleasure, {target}. How about I give you a seductive massage to ignite the fire between us?\" {initiator} proposes, their voice low and filled with desire.",
            "\"{target}, I've been fantasizing about giving you a tantalizing massage. How about I make that fantasy come true tonight?\" {initiator} suggests, a playful smile dancing on their lips.",
            "\"{target}, I've been studying massage techniques for a while now, and I think I'm ready to give you an intimate massage,\" {initiator} says, their voice filled with anticipation.",
            "\"I've been practicing my massage skills, and I would love to give you an intimate massage if you're open to it,\" {initiator} suggests, trying to gauge {target}'s reaction.",
            "\"I've been reading about the benefits of intimate massage, and I think it could be a wonderful experience for both of us. Would you be interested, {target}?\" {initiator} asks, their eyes filled with curiosity.",
            "\"{target}, I've been thinking about it for a while, and I believe giving you an intimate massage could be a way for us to connect on a deeper level. What do you think?\" {initiator} proposes, their voice filled with sincerity.",
            "\"I've been practicing my massage techniques, and I would love to offer you an intimate massage. It could be a way for us to relax and unwind together,\" {initiator} suggests, hoping {target} would be open to the idea.",
            "\"{target}, I've been researching different types of massage, and I came across the concept of intimate massage. It intrigued me, and I thought maybe we could explore it together,\" {initiator} says, their tone hesitant yet hopeful.",
            "\"{target}, I've been learning about the power of touch, and I think an intimate massage could create a unique bond between us. Would you be willing to try it?\" {initiator} asks, their eyes searching {target}'s face for a reaction.",
            "\"I've been working on my massage skills, and I think it's time I put them to use. {target}, would you be open to receiving an intimate massage from me?\" {initiator} asks, their voice filled with a mix of nervousness and excitement.",
            "\"{target}, I've been practicing some massage techniques, and I thought it would be nice to offer you an intimate massage. It could be a chance for us to connect on a deeper level,\" {initiator} suggests, their eyes filled with warmth.",
            "\"I've been learning about the healing power of touch, and I thought maybe I could offer you an intimate massage as a way to show my care and affection. What do you think, {target}?\" {initiator} asks, their voice filled with tenderness.",
        ]
    },
    "mixer_social_SitIntimate_MakeAMove_targeted_romance_alwaysOn": {
        "pre_actions": [
            "{initiator} signals their sexual interest in {target}.",
        ],
        "actions": [
            "\"{target}, there's something I've been wanting to tell you for a while now. I'm attracted to you,\" {initiator} admits, their voice filled with nervousness.",
            "\"I can't keep it a secret any longer, {target}. I have feelings for you, and I needed to let you know,\" {initiator} says, their cheeks turning slightly pink.",
            "\"I've been struggling with this feeling, {target}, but I can't deny it anymore. I'm attracted to you,\" {initiator} confesses, their eyes locked with {target}'s.",
            "\"I hope I'm not crossing any boundaries here, but I can't help but feel a strong attraction towards you, {target},\" {initiator} says, their voice wavering.",
            "\"Believe me, I didn't plan on catching these feelings, but it happened, {target}. I find myself attracted to you,\" {initiator} says, looking slightly embarrassed.",
            "\"I've been trying to hide it, but it's becoming harder each day. {target}, I'm attracted to you, and I needed to get it off my chest,\" {initiator} admits, their voice filled with vulnerability.",
            "\"I've been wrestling with my emotions, {target}, but I can't deny it any longer. I'm drawn to you in ways I can't explain,\" {initiator} says, their voice filled with a mix of longing and uncertainty.",
            "\"I hope this doesn't change our friendship, {target}, but I can't keep it to myself any longer. I'm attracted to you,\" {initiator} says, their voice shaking slightly.",
            "\"I know this might come as a surprise, {target}, but I can't keep it hidden any longer. I'm attracted to you, and I needed to tell you,\" {initiator} says, their voice filled with determination.",
            "\"I've been holding back my feelings for so long, {target}, but I can't pretend anymore. I'm undeniably attracted to you,\" {initiator} confesses, their eyes filled with a mix of fear and hope."
        ]
    },
    "mixer_social_SitIntimate_MakeOut_targeted_romance_highScore": {
        "pre_actions": [
            "{initiator} attempts to make out with {target}."
        ],
        "actions": [
            "\"{target}, there's something I've been wanting to do for a while now,\" {initiator} says, leaning in closer.",
            "\"Forgive me if this is too forward, but I can't resist the urge any longer,\" {initiator} says, their lips inches away from {target}'s.",
            "\"{target}, I've been thinking about this moment for so long. Can I steal a kiss from you?\" {initiator} asks, their heart racing.",
            "\"I hope this doesn't come as a surprise, but I've been wanting to do this since the moment I met you,\" {initiator} says, leaning in for a kiss.",
            "\"I've been trying to hold back, but the desire to kiss you is overpowering. Can I take that chance?\" {initiator} asks, their eyes locked with {target}'s.",
            "\"{target}, I can't help but feel this connection between us. Would it be too bold of me to lean in and kiss you?\" {initiator} says, their voice filled with anticipation.",
            "\"I've been waiting for the perfect moment, and I think it's now. Can I kiss you, {target}?\" {initiator} asks, their voice filled with longing.",
            "\"There's something about you, {target}, that makes me want to take this risk. Can I steal a kiss?\" {initiator} says, their breath hitching.",
            "\"{target}, I hope you don't mind me being so forward, but I can't resist the urge to kiss you,\" {initiator} confesses, their face flushing.",
            "\"I know this might be unexpected, but I can't hold back any longer. Can I kiss you, {target}?\" {initiator} asks, their heart pounding in their chest."
        ]
    },
    "mixer_social_SitIntimate_TryForBaby_targeted_romance_HighScore": {
        "pre_actions": [
            "{initiator} attempts to try for a baby with {target}."
        ],
        "actions": [
            "\"Hey {target}, I know this might sound sudden, but what do you think about trying for a baby right now?\" {initiator} asks, a hopeful smile on their face.",
            "\"I've been thinking a lot about our future together, {target}, and I can't help but wonder if it's the right time to start a family. What do you say?\" {initiator} suggests, nervously.",
            "\"Something has been on my mind lately, {target}, and it's the idea of starting a family. Would you be open to trying for a baby with me?\" {initiator} asks tentatively.",
            "\"{target}, I know this is a big decision, but I can't shake the feeling that it's time for us to take the next step and have a baby. What do you think?\" {initiator} asks, their voice filled with anticipation.",
            "\"I hope you're ready for a serious conversation, {target}, because I've been thinking about having a baby and I wanted to discuss it with you,\" {initiator} says, their eyes searching {target}'s face for a reaction.",
            "\"Okay, this might come as a surprise, but hear me out, {target}. I've been thinking about having a baby, and I want to know if you're willing to take that journey with me,\" {initiator} confesses, their voice filled with both excitement and nervousness.",
            "\"{target}, I have something important I want to talk to you about. It's about our future and the possibility of starting a family. Are you open to that idea?\" {initiator} asks, their heart pounding.",
            "\"I've been daydreaming a lot lately, {target}, and I keep picturing us as parents. What if we stop daydreaming and make it a reality? Would you be interested in trying for a baby?\" {initiator} asks, their eyes shining with hope.",
            "\"I know this is a big question, {target}, but I can't help but wonder if it's time for us to expand our family. What are your thoughts on trying for a baby?\" {initiator} asks, their voice filled with a mix of excitement and nervousness.",
            "\"{target}, I've been doing a lot of soul-searching lately, and I think it's time for us to take a leap of faith. Would you be willing to try for a baby with me?\" {initiator} asks, their voice filled with anticipation."
        ]
    },
    "mixer_social_SitIntimate_WooHoo_targeted_romance_HighScore": {
        "pre_actions": [
            "{initiator} attempts to initiate sex with {target}.",
        ],
        "actions": [
            "{initiator} leans in close to {target}, their eyes filled with desire.",
            "\"I've been thinking about this for a while, {target},\" {initiator} says, seductively.",
            "{initiator} reaches out and traces a finger along {target}'s arm, sending shivers down {target}'s spine.",
            "\"There's something about you, {target}, that I just can't resist,\" {initiator} whispers, their voice laced with anticipation.",
            "As {initiator} moves closer, their lips barely brushing against {target}'s ear, they murmur, \"I want you. Right here. Right now.\"",
            "With a playful smile, {initiator} takes {target}'s hand and leads them to a secluded spot, their intentions clear.",
            "{initiator} presses their body against {target}, their lips crashing together in a passionate embrace.",
            "\"Tonight, {target}, I want to experience something unforgettable with you,\" {initiator} says, their voice filled with longing.",
            "With a mischievous glint in their eye, {initiator} whispers, \"Let's explore a new level of intimacy, {target}...together.\"",
            "{initiator} pulls {target} close, their hands roaming over each other's bodies, as they share a heated gaze filled with desire."
        ]
    },
    "mixer_social_TalkAboutArt_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} starts a conversation about art with {target}."
        ],
        "actions": [
            "\"{target}, I've always wanted to talk to someone about art, and I feel like you might be the perfect person to discuss it with,\" {initiator} says, excitedly.",
            "\"I've been exploring different art forms lately, and I can't help but wonder what your thoughts are on the subject, {target},\" {initiator} asks, curious.",
            "\"Art has always fascinated me, {target}, and I would love to hear your perspective on it. Care to share?\" {initiator} initiates the conversation.",
            "\"I recently stumbled upon a thought-provoking piece of art, and I can't get it out of my mind. I wanted to know if you've had a similar experience, {target},\" {initiator} says, seeking validation.",
            "\"I've been trying my hand at painting recently, {target}, and I would value your opinion on my latest creation. Can I show it to you?\" {initiator} asks, hoping for constructive feedback.",
            "\"I've always believed that art has the power to move people, {target}. What are your thoughts on the emotional impact of art?\" {initiator} asks, eager to hear {target}'s perspective.",
            "\"I've been contemplating the concept of beauty in art, {target}, and I would love to hear your definition of what makes something beautiful,\" {initiator} says, engaging in a philosophical discussion.",
            "\"I've been feeling inspired lately, {target}, and I wanted to share some of my ideas for an art project. Can I bounce them off you?\" {initiator} asks, seeking encouragement.",
            "\"I find myself drawn to abstract art, {target}, but I'm curious to know if you have a preference for a specific art style,\" {initiator} says, hoping to find common ground.",
            "\"I've been reading about the role of art in society, {target}, and I'm interested to know your thoughts on the importance of art in our lives,\" {initiator} says, opening up a conversation about art's significance."
        ]
    },
    "mixer_social_TalkAboutHandiness_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} brags about their handiness skills to {target}."
        ],
        "actions": [
            "\"{target}, you won't believe what I managed to fix all by myself yesterday. I'm becoming quite the handy person,\" {initiator} boasts proudly.",
            "\"I've been honing my handiness skills lately, {target}, and let me tell you, I'm getting pretty good at it,\" {initiator} says, with a smug smile.",
            "\"You know, {target}, I've discovered a hidden talent of mine - I'm surprisingly handy. Just ask anyone who's witnessed my latest DIY project,\" {initiator} says, beaming with confidence.",
            "\"I've always been the type to figure things out on my own, {target}, and my handiness skills are no exception. You'd be impressed,\" {initiator} brags, crossing their arms.",
            "\"You won't believe the project I tackled last weekend, {target}. I never knew I had it in me to be so handy,\" {initiator} boasts, unable to contain their excitement.",
            "\"I've been spending a lot of time working with tools lately, {target}, and I must say, I'm quite proud of my handiness. It's a skill worth bragging about,\" {initiator} says confidently.",
            "\"Guess who fixed their leaky faucet all by themselves? That's right, {target}, me. Turns out I'm pretty handy,\" {initiator} brags, pointing a thumb at themselves.",
            "\"You may not know this about me, {target}, but I'm secretly a DIY aficionado. My handiness skills are top-notch,\" {initiator} boasts, with a hint of arrogance.",
            "\"I've always been a quick learner, {target}, and that's how I became so handy. I can practically fix anything now,\" {initiator} says, with a self-satisfied smirk.",
            "\"Being handy has its perks, {target}, and I've certainly embraced them. I can handle any repair or project that comes my way,\" {initiator} brags, puffing out their chest."
        ]
    },
    "mixer_social_PlayAPrank_targeted_mischief_skills": {
        "pre_actions": [
            "{initiator} plays a prank on {target}."
        ],
        "actions": [
            "\"{target}, you won't believe what just happened! I can't stop laughing,\" {initiator} says, struggling to contain their amusement. ",
            "\"I couldn't resist pulling a prank on you, {target}. You should have seen your reaction!\" {initiator} exclaims, grinning mischievously.",
            "\"You've always been such a good sport, {target}, so I thought I'd have a little fun and play a prank on you,\" {initiator} confesses, trying not to burst into laughter.",
            "\"I have to admit, {target}, that prank I pulled on you was absolutely genius. Your face was priceless!\" {initiator} says, barely able to contain their excitement.",
            "\"{target}, you're never going to believe what just happened. I played the best prank on you, and I can't wait to tell you all about it,\" {initiator} says, barely able to hold back their laughter.",
            "\"I hope you're ready for a good laugh, {target}, because I just played the most epic prank on you. You won't see it coming!\" {initiator} says, barely able to contain their excitement.",
            "\"Remember that prank we talked about pulling on someone? Well, I couldn't resist and ended up playing it on you, {target}. You have to admit, it was pretty clever,\" {initiator} says, trying to stifle their laughter.",
            "\"I have to apologize, {target}. I played a prank on you, and it got a bit out of hand. I hope you can forgive me,\" {initiator} says, feeling a tinge of guilt.",
            "\"{target}, I couldn't resist playing a prank on you. I'm sorry if it crossed a line, but I thought you would find it funny,\" {initiator} says, hoping for forgiveness.",
            "\"Hey, {target}, I played a prank on you. It was all in good fun, but if it upset you, I'm sorry. Let's laugh it off!\" {initiator} says, hoping to diffuse any tension."
        ]
    },
    "mixer_social_AskAboutLoveLife_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} asks {target} about their love life."
        ],
        "actions": [
            "\"So, {target}, any exciting love interests in your life lately?\" {initiator} asks with a mischievous smile.",
            "\"I've been curious, {target}, have you been seeing anyone special these days?\" {initiator} inquires with genuine interest.",
            "\"Tell me, {target}, how's your love life going? Any romantic prospects on the horizon?\" {initiator} asks, leaning in closer.",
            "\"I hope you don't mind me asking, {target}, but have you found someone who makes your heart skip a beat?\" {initiator} asks, raising an eyebrow.",
            "\"You know, {target}, I've been wondering if there's someone who has captured your attention. Care to share?\" {initiator} asks playfully.",
            "\"I couldn't help but notice that twinkle in your eye, {target}. Is there someone special in your life?\" {initiator} asks, trying to contain their curiosity.",
            "\"Mind if I ask, {target}, have you been bitten by the love bug lately? Any romantic stories to share?\" {initiator} asks, leaning back comfortably.",
            "\"You seem mysterious when it comes to your love life, {target}. Care to shed some light on the subject?\" {initiator} asks, intrigued.",
            "\"I've been dying to know, {target}, are you currently in the midst of a whirlwind romance?\" {initiator} asks, unable to hide their excitement.",
            "\"Let's talk love, {target}. Are you open to sharing any romantic escapades that have been happening in your life?\" {initiator} asks with a playful grin."
        ]
    },
    "mixer_social_AskRisqueQuestion_targeted_romance_alwaysOn": {
        "pre_actions": [
            "{initiator} asks {target} a risqué question."
        ],
        "actions": [
            "\"{target}, I have a question for you... and it might be a little scandalous,\" {initiator} says with a mischievous grin.",
            "\"You know, {target}, there's something I've been curious about... Can I ask you a bold question?\" {initiator} asks, raising an eyebrow.",
            "\"I hope you're ready for this, {target}, because I'm about to ask you something quite daring,\" {initiator} says, their voice filled with anticipation.",
            "\"{target}, I've been wondering about something... Would you mind if I ask you a rather provocative question?\" {initiator} asks, trying to gauge {target}'s reaction.",
            "\"There's something I've been dying to know, {target}, but I'm not sure if I should ask... Can I trust you with a slightly taboo question?\" {initiator} says, looking both nervous and excited.",
            "\"I hope this doesn't make things awkward, {target}, but I can't help but wonder... Can I ask you something a bit naughty?\" {initiator} asks, biting their lip.",
            "\"{target}, I have a question that might cross a few boundaries... Are you open to being asked something a little risqué?\" {initiator} asks tentatively.",
            "\"I know this might be a bit forward, {target}, but I can't resist... Would it be alright if I asked you a rather intimate question?\" {initiator} says, blushing slightly.",
            "\"I'm feeling a little bold today, {target}, so here's a question for you... Are you ready for it?\" {initiator} asks, their eyes gleaming with curiosity.",
            "\"{target}, I have a question that might make you blush... Can I ask you something a little spicy?\" {initiator} says, smirking playfully."
        ]
    },
    "mixer_social_AskSimToPursueDreamJob_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} encourages {target} to pursue their dream job."
        ],
        "actions": [
            "\"You know, {target}, I've been thinking about your dream job lately, and I really believe you should go for it,\" {initiator} says, smiling supportively.",
            "\"{target}, I've been watching you work so hard towards your dream job, and I just wanted to say how proud I am of you,\" {initiator} says, giving {target} a sincere compliment.",
            "\"I've seen how passionate you are about your dream job, {target}, and I think it's time for you to take that leap of faith,\" {initiator} says, encouragingly.",
            "\"I know pursuing your dream job may seem scary, {target}, but I have complete faith in your abilities. You've got this,\" {initiator} says, giving {target} a reassuring smile.",
            "\"{target}, I can see how much you want that dream job, and I truly believe you have what it takes to make it happen,\" {initiator} says, offering {target} words of encouragement.",
            "\"Sometimes, all it takes is a little push to follow your dreams, {target}, and I'm here to give you that push. You deserve it,\" {initiator} says, motivating {target} to pursue their dream job.",
            "\"I've noticed how dedicated you are to your dream job, {target}, and it's inspiring. Don't let anything hold you back,\" {initiator} says, urging {target} to chase their dreams.",
            "\"{target}, life is too short to not pursue your dream job. Take a chance, and remember that I'll be there to support you every step of the way,\" {initiator} says, offering {target} unwavering support.",
            "\"You have such incredible talent and potential, {target}, and it would be a shame not to see you thrive in your dream job. You owe it to yourself to go for it,\" {initiator} says, motivating {target} to pursue their dreams.",
            "\"{target}, I believe that you were meant for your dream job. Don't let self-doubt hold you back - trust in yourself and go for it,\" {initiator} says, inspiring {target} to follow their passion."
        ]
    },
    "mixer_social_AskDueDate_targeted_mischief_skills": {
        "pre_actions": [
            "{initiator} mischievously asks {target} about their due date."
        ],
        "actions": [
            "\"{target}, I couldn't help but notice, when are you expecting the little bundle of joy?\" {initiator} asks, a malicious smile creeping across their face.",
            "\"Oh, I didn't realize you were pregnant, {target}. When's the big day?\" {initiator} says mockingly, trying to hide their amusement.",
            "\"You must be so excited! When's the baby due, {target}?\" {initiator} says mockingly, their eyes filled with judgment.",
            "\"I can't help but wonder, {target}, when is the little one expected to arrive?\" {initiator} asks with a sneer.",
            "\"{target}, forgive me if I'm mistaken, but when is your due date? I could have sworn I saw a baby bump,\" {initiator} says, their tone dripping with condescension.",
            "\"I'm sorry if I'm mistaken, {target}, but I thought you were pregnant. When can we expect to meet the newest addition to the family?\" {initiator} taunts, unable to contain their smirk.",
            "\"Oh, {target}, I have to ask, when is the bundle of joy going to make its grand entrance?\" {initiator} says, mocking sweetness evident in their voice.",
            "\"I hope you don't mind me asking, {target}, but when is the big day? You're glowing with motherhood!\" {initiator} jeers, a cruel gleam in their eyes.",
            "\"I have to say, {target}, you hide it well. When are you due, by the way?\" {initiator} says, chuckling under their breath.",
            "\"{target}, I have a curious question - when is the baby coming? It seems like you've been glowing lately,\" {initiator} says, their voice filled with sarcasm."
        ]
    },
    "mixer_social_AskForLargeLoan_targeted_friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} asks {target} for a large loan."
        ],
        "actions": [
            "\"{target}, I hate to ask you this, but I'm in a really tough spot financially. Is there any chance you could lend me a large sum of money?\" {initiator} asks, hesitant and embarrassed.",
            "\"I know it's a big ask, {target}, but I'm in desperate need of a substantial loan. Would you consider helping me out?\" {initiator} requests, a look of desperation on their face.",
            "\"I wouldn't ask if I didn't absolutely need it, but {target}, would you be willing to lend me a significant amount of money? I promise I'll pay you back,\" {initiator} pleads, clasping their hands together.",
            "\"I'm in a bind, {target}, and I hate to impose, but I was wondering if you could do me a huge favor and lend me a substantial sum of money. I would forever be grateful,\" {initiator} asks, their tone filled with hope.",
            "\"{target}, I have nowhere else to turn. Would you be willing to lend me a sizable loan? I understand if you can't, but I really need your help,\" {initiator} implores, their voice trembling slightly.",
            "\"I know how it sounds, {target}, but I promise it's an emergency. Could you possibly lend me a large amount of money? I wouldn't ask if it wasn't urgent,\" {initiator} explains, a note of desperation in their voice.",
            "\"I've exhausted all other options, {target}, which is why I'm reaching out to you. Would it be possible for you to lend me a considerable sum of money? I'm really desperate,\" {initiator} admits, their eyes filled with anxiety.",
            "\"{target}, I have a favor to ask, and I hope you can help me. I need a significant loan to get through a difficult time. Can I count on you?\" {initiator} asks, their voice filled with uncertainty.",
            "\"{target}, I hate to put you on the spot, but I urgently need a large loan. Is there any way you could lend me the money I need?\" {initiator} asks, nervously wringing their hands.",
            "\"I know this is a huge request, {target}, but I'm in dire straits. Would you consider lending me a substantial amount of money? I wouldn't ask if I had any other option,\" {initiator} pleads, desperation evident in their voice."
        ]
    },
    "mixer_social_AskForSmallLoan_targeted_friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} asks {target} for a small loan."
        ],
        "actions": [
            "\"{target}, I hate to ask, but I'm in a tough spot right now. Would you be able to lend me a small amount of money?\" {initiator} pleads, looking embarrassed.",
            "\"I know this might sound desperate, but I really need some financial help. {target}, do you think you could loan me a little bit of money?\" {initiator} asks, their voice filled with hope.",
            "\"I wouldn't ask if I didn't really need it, {target}. Could you possibly lend me a small loan? I promise to pay you back as soon as I can,\" {initiator} says, feeling a mix of guilt and desperation.",
            "\"I know it's a big ask, but I'm in a bit of a bind. {target}, could you spare a small loan to help me through this tough time?\" {initiator} asks nervously.",
            "\"I hate to put you in a difficult position, {target}, but I'm in a financial crisis. Is there any chance you could lend me a small sum of money?\" {initiator} asks, their voice tinged with anxiety.",
            "\"I never thought I would have to ask for money, but circumstances have left me with no other choice. {target}, would you be willing to lend me a small loan?\" {initiator} says, their pride masked by desperation.",
            "\"I know it's a big favor to ask, {target}, but I really need some financial assistance right now. Can you find it in your heart to lend me a small loan?\" {initiator} asks, their voice filled with vulnerability.",
            "\"I wouldn't ask if I had any other options, {target}, but I'm in a bind and I really need some financial help. Could you possibly loan me a small amount of money?\" {initiator} pleads, their voice shaky with worry.",
            "\"{target}, I feel terrible about having to ask, but I'm struggling with money at the moment. Is there any chance you could lend me a small loan?\" {initiator} asks, their face flushed with embarrassment.",
            "\"It's not easy for me to ask for help, {target}, but I'm facing some financial difficulties. Would it be possible for you to lend me a small amount of money?\" {initiator} asks, trying to mask their anxiety."
        ]
    },
    "mixer_social_AskToCleanUpToys_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} asks {target}, who is a child, to clean up their toys."
        ],
        "actions": [
            "\"Hey {target}, could you do me a favor and clean up your toys? It's getting a little messy,\" {initiator} asks gently.",
            "\"I know you're busy playing, {target}, but could you please tidy up your toys when you're done?\" {initiator} requests with a smile.",
            "\"Hey, {target}, would you mind picking up your toys and putting them back where they belong?\" {initiator} asks, pointing to the scattered toys.",
            "\"Cleaning up after playtime is important, {target}. Can you please put your toys away?\" {initiator} asks, trying to sound firm but friendly.",
            "\"Could you do me a huge favor, {target}? Can you clean up your toys so we have a tidy space to play in later?\" {initiator} asks, hoping for cooperation.",
            "\"Hey there, {target}. I need your help. Could you clean up your toys and make the room look neat again?\" {initiator} asks, displaying a patient smile.",
            "\"Cleaning up is a responsible thing to do, {target}. Can you show me how grown-up you are by cleaning up your toys?\" {initiator} asks, encouraging {target}.",
            "\"Now, you know the rule, {target}. When you're done playing, you have to clean up. Can you do that for me?\" {initiator} asks, reminding {target} of their responsibility.",
            "\"Hey, little buddy, can you please pick up your toys and put them back in their boxes? I would really appreciate it,\" {initiator} asks, using a gentle tone.",
            "\"Cleaning up after ourselves is a good habit, {target}. Can you please clean up your toys so that we can keep our space tidy?\" {initiator} asks, hoping for cooperation."
        ]
    },
    "mixer_social_BecomePartnersInCrime_targeted_friendly_highScore": {
        "pre_actions": [
            "{initiator} proposes to {target} to become partners in crime."
        ],
        "actions": [
            "\"{target}, I have a proposition for you. What if we became partners in crime?\" {initiator} smirks mischievously.  ",
            "\"I've been thinking, {target}, with our skills combined, we could become the ultimate duo. What do you say?\" {initiator} suggests, raising an eyebrow.  ",
            "\"Imagine the adventures we could have, {target}, if we joined forces. Partners in crime, what do you think?\" {initiator} grins, excitement in their voice.  ",
            "\"{target}, I've been plotting a little something, and I think it's time I shared it with you. We should become partners in crime,\" {initiator} proposes, leaning in closer.  ",
            "\"I know it sounds crazy, {target}, but hear me out. We could be an unstoppable team if we became partners in crime,\" {initiator} says, eyes gleaming with anticipation.  ",
            "\"{target}, I have a proposal that might interest you. What if we joined forces and became partners in crime? The possibilities are endless,\" {initiator} says, a devious smile playing on their lips.  ",
            "\"{target}, I've watched you, and I see potential. We could accomplish great things if we became partners in crime. What do you say?\" {initiator} asks, their voice filled with intrigue.  ",
            "\"I can see the twinkle in your eye, {target}, when mischief is involved. That's why I'm asking you to become my partner in crime,\" {initiator} suggests, their tone daring.  ",
            "\"{target}, I've always admired your cunning and resourcefulness. What if we put our talents together and became partners in crime?\" {initiator} proposes, a glint of excitement in their eyes.  ",
            "\"{target}, you've always had a taste for adventure. So, how about we take it to the next level and become partners in crime?\" {initiator} grins, waiting for a response."
        ]
    },
    "mixer_social_Beguile_targeted_romance_alwaysOn_trait": {
        "pre_actions": [
            "{initiator} tries to beguile {target}."
        ],
        "actions": [
            "\"{target}, I've been thinking about you a lot lately. Can I show you why?\" {initiator} asks, a mischievous glint in their eyes.",
            "\"I've discovered a secret talent of mine, {target}, and I'd love to demonstrate it just for you,\" {initiator} says, a sly smile playing on their lips.",
            "\"Have I ever told you that I'm quite skilled in the art of persuasion? I think it's time I put my skills to the test,\" {initiator} says, raising an eyebrow.",
            "\"I've been studying the art of seduction, {target}, and I have a feeling you might be my perfect subject,\" {initiator} says, their voice dripping with charm.",
            "\"{target}, let me tell you a little secret. I have a knack for making people fall under my spell,\" {initiator} says, tapping their fingers together thoughtfully.",
            "\"I've been learning some mind tricks recently, {target}. Care to see what I can do?\" {initiator} asks, their tone full of mystery.",
            "\"You know, {target}, I've always been fascinated by the power of persuasion. Would you like to be my experiment?\" {initiator} suggests, a glimmer of excitement in their eyes.",
            "\"{target}, I've been told I have a way with words. Let me show you just how persuasive I can be,\" {initiator} says confidently.",
            "\"Allow me to enchant you, {target}. I promise it will be an experience you won't forget,\" {initiator} says, a playful smirk on their face.",
            "\"{target}, there's something about you that makes me want to use every trick in the book to win you over. Care to see what I've got?\" {initiator} asks, a grin spreading across their face."
        ]
    },
    "mixer_social_BoastAboutFamily_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} boasts about their family to {target}."
        ],
        "actions": [
            "\"I have to brag for a moment, {target}. My family is truly incredible,\" {initiator} says with a proud smile.",
            "\"You won't believe it, {target}, but my family is like something out of a fairytale,\" {initiator} says, unable to contain their excitement.",
            "\"Can I just say, {target}, that my family is absolutely extraordinary?\" {initiator} asks, their eyes shining with pride.",
            "\"I know it may sound like I'm exaggerating, but my family is seriously impressive, {target},\" {initiator} says, unable to hide their enthusiasm.",
            "\"I have to share this with you, {target}. My family is the definition of remarkable,\" {initiator} says, bursting with pride.",
            "\"I've always felt incredibly lucky to be a part of my family, {target}. They are truly amazing,\" {initiator} says, their voice filled with admiration.",
            "\"You know, {target}, my family has achieved some incredible things. I can't help but brag about them,\" {initiator} says, beaming with pride.",
            "\"I hope you don't mind, {target}, but I just have to tell you how amazing my family is. It's hard to contain my excitement,\" {initiator} says, unable to hide their pride.",
            "\"I have to say, {target}, my family is pretty extraordinary. They've accomplished so much,\" {initiator} says, their eyes gleaming with pride.",
            "\"I can't help but gush about my family, {target}. They truly are exceptional,\" {initiator} says, a sense of awe evident in their voice."
        ]
    },
    "mixer_social_BragAboutPossesions_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} brags about their possessions to {target}."
        ],
        "actions": [
            "\"I must say, {target}, I have quite an impressive ",
            "\"You won't believe the luxury items I've acquired over the years, {target}. Shall I give you a glimpse?\" {initiator} boasts, flaunting their wealth.",
            "\"I never like to brag, but I have some ",
            "\"You think you've seen it all, {target}? Well, let me tell you about my ",
            "\"As someone with refined taste, {target}, I believe you'll appreciate my ",
            "\"I wouldn't usually flaunt my wealth, but I can't help but mention ",
            "\"Sit back and listen, {target}, for I possess ",
        ]
    },
    "mixer_social_BreakUp_targeted_mean_relationship": {
        "pre_actions": [
            "{initiator} breaks up with {target}."
        ],
        "actions": [
            "\"I think we need to talk, {target},\" {initiator} says with a heavy heart.",
            "\"I've been doing a lot of thinking, and I've come to a difficult decision, {target},\" {initiator} says, looking away.",
            "\"I never thought I would say this, but I can't continue this relationship, {target},\" {initiator} says, their voice filled with sadness.",
            "\"Something has changed between us, {target}, and I don't think I can be with you anymore,\" {initiator} says, struggling to maintain eye contact.",
            "\"This is one of the hardest things I've ever had to do, but I think it's time we go our separate ways, {target},\" {initiator} says, trying to sound firm.",
            "\"I never wanted it to come to this, but I don't think we're right for each other, {target},\" {initiator} says, their voice shaking.",
            "\"I've been feeling trapped in this relationship, {target}, and I think it's best if we end it,\" {initiator} says, looking apologetic.",
            "\"There's been a growing distance between us, {target}, and I don't think we can fix it. We should break up,\" {initiator} says, looking pained.",
            "\"I've been lying to myself, {target}, pretending everything is fine when it's not. I can't continue like this. We should break up,\" {initiator} says, their voice filled with regret.",
            "\"I've been doing a lot of soul-searching, {target}, and I've realized that we're not meant to be together. It's time to end this,\" {initiator} says, their voice filled with resignation."
        ]
    },
    "mixer_social_BrushOff_targeted_mean_emotionSpecific": {
        "pre_actions": [
            "{initiator} rudely brushes off {target}."
        ],
        "actions": [
            "\"{target}, I don't have time for your nonsense. Leave me alone,\" {initiator} snaps, walking away without looking back.",
            "\"Can't you see I have better things to do than deal with you, {target}? Just go bother someone else,\" {initiator} says dismissively.",
            "\"You're really starting to annoy me, {target}. Stop wasting my time,\" {initiator} says, rolling their eyes.",
            "\"I don't know why I even bother talking to you, {target}. You're not worth my energy,\" {initiator} says coldly, turning their back on {target}.",
            "\"I don't have the patience for your foolishness, {target}. Find someone else to bother,\" {initiator} says sharply, brushing past {target}.",
            "\"Your presence is a constant irritation, {target}. Can't you take a hint and leave me alone?\" {initiator} says, their voice dripping with disdain.",
            "\"{target}, I have no interest in what you have to say. Stop trying to get my attention,\" {initiator} says with a sneer.",
            "\"Do me a favor, {target}, and disappear from my sight. I can't stand being around you,\" {initiator} says with a scowl.",
            "\"I have no use for you, {target}. Don't expect me to waste any more of my time on you,\" {initiator} says dismissively, brushing {target} aside.",
            "\"{target}, I have better things to do than entertain your presence. Leave me alone,\" {initiator} says rudely, not giving {target} a second glance."
        ]
    },
    "mixer_social_ChatAboutPropertyVaules_targeted_friendly_alwaysOn_neighbor": {
        "pre_actions": [
            "{initiator} chats with {target} about property values in their neighborhood."
        ],
        "actions": [
            "\"So, {target}, have you noticed any changes in property values in our neighborhood lately?\" {initiator} asks.",
            "\"I've been doing some research, and it seems like property values have been steadily increasing in our neighborhood. What are your thoughts, {target}?\" {initiator} curiously asks.",
            "\"You know, {target}, I've been thinking about selling my house. Do you think now is a good time, considering the current property values in our neighborhood?\" {initiator} wonders aloud.",
            "\"I overheard some neighbors talking about the rising property values in our neighborhood. Have you heard anything about it, {target}?\" {initiator} asks, leaning in.",
            "\"{target}, I've been crunching the numbers, and it seems like property values in our neighborhood have skyrocketed. What's your take on it?\" {initiator} asks, raising an eyebrow.",
            "\"I've been thinking about investing in real estate, and I can't help but wonder if the property values in our neighborhood are on the rise. Any insights, {target}?\" {initiator} asks, genuinely curious.",
            "\"I've been reading about the real estate market, and it seems like property values in our neighborhood are outperforming the average. What's your opinion on that, {target}?\" {initiator} asks, intrigued.",
            "\"Hey, {target}, I've been contemplating buying a new house, but I'm torn on whether to stay in our neighborhood or move somewhere else. Any thoughts on the current property values here?\" {initiator} asks, seeking advice."
        ]
    },
    "mixer_social_CheerUp_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} attempts to cheer up {target}."
        ],
        "actions": [
            "\"Hey {target}, I noticed you've been feeling down lately. How about we do something fun to lift your spirits?\" {initiator} suggests with a smile.",
            "\"Life's too short to be sad all the time, {target}. Let's find a way to bring some joy into your day,\" {initiator} says, trying to be encouraging.",
            "\"I know you're going through a tough time, {target}, but I'm here for you. Let's find something that will make you smile, even if just for a moment,\" {initiator} says, offering support.",
            "\"{target}, I've got an idea. How about we go on an adventure together? It might help take your mind off things and put a smile on your face,\" {initiator} suggests eagerly.",
            "\"I hate seeing you like this, {target}. Let's find something that will make you laugh and forget about your troubles, even if it's just for a little while,\" {initiator} says, determined to brighten {target}'s day.",
            "\"Cheer up, {target}. I've got a surprise for you that I hope will bring a smile to your face. Are you ready?\" {initiator} asks, trying to sound enthusiastic.",
            "\"I know it's not easy, {target}, but let's try to focus on the positive. What's something you enjoy doing that we can do together?\" {initiator} suggests, hoping to distract {target}.",
            "\"Sometimes a change of scenery can do wonders. How about we go somewhere different, away from all the stress and worries?\" {initiator} proposes, hoping to lift {target}'s mood.",
            "\"I've got a playlist of feel-good songs that always cheer me up, {target}. Want me to play it for you?\" {initiator} offers, hoping the music will bring some joy to {target}.",
            "\"{target}, I've been thinking about what might make you feel better, and I came up with an idea. How about we try it out and see if it helps?\" {initiator} suggests, eager to bring some happiness to {target}."
        ]
    },
    "mixer_social_CheerUp_targeted_friendly_emotionSpecific_c2a": {
        "pre_actions": [
            "{initiator} attempts to cheer up {target}."
        ],
        "actions": [
            "\"{target}, I can see that you're feeling down. I want to try and bring a smile to your face,\" {initiator} says with a determined look.",
            "\"You know, {target}, sometimes all it takes is a little laughter to brighten up your day. Let me try,\" {initiator} says, preparing to tell a joke.",
            "\"{target}, I hate seeing you like this. I'm going to do everything I can to make you feel better,\" {initiator} says, reaching out to {target} with a comforting smile.",
            "\"I know things haven't been easy for you lately, {target}, but I want to remind you that there's still joy to be found in the little things,\" {initiator} says, offering a small gesture of kindness.",
            "\"{target}, I have an idea that might lift your spirits. Are you open to trying something new?\" {initiator} asks, a mischievous glint in their eyes.",
            "\"Life can be tough, {target}, but remember that you're not alone. Let's find a way to turn this frown upside down,\" {initiator} says, extending a hand of support.",
            "\"{target}, I've been thinking about how to make you smile, and I've come up with something. Are you ready?\" {initiator} asks, excitement evident in their voice.",
            "\"Sometimes, a little distraction is all you need to forget your worries, {target}. Let me try and take your mind off things,\" {initiator} suggests, offering a fun activity.",
            "\"{target}, I believe that laughter is the best medicine. Let's find something to laugh about, shall we?\" {initiator} says, determined to bring some joy to {target}'s day.",
        ]
    },
    "mixer_social_ComplainAboutBoredom_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} complains to {target} about how bored they are."
        ],
        "actions": [
            "\"I can't take it anymore, {target}. I'm so bored I could scream,\" {initiator} says, with a frustrated sigh.",
            "\"I don't know what to do with myself anymore, {target}. This boredom is suffocating,\" {initiator} complains, looking exasperated.",
            "\"Is it just me, or has life become incredibly dull lately? I need something exciting to happen, {target},\" {initiator} says, longing for a change.",
            "\"I've never been this bored in my entire life, {target}. I feel like I'm wasting away,\" {initiator} laments, their voice filled with boredom.",
            "\"{target}, I need some excitement in my life. This boredom is killing me,\" {initiator} says, looking at {target} with desperation.",
            "\"I'm at my wit's end, {target}. This constant boredom is draining the life out of me,\" {initiator} complains, feeling restless.",
            "\"I can't stand another minute of this mind-numbing boredom, {target}. I need something to shake things up,\" {initiator} says, their frustration evident.",
            "\"I've tried everything to entertain myself, {target}, but nothing seems to work. I'm stuck in this perpetual state of boredom,\" {initiator} complains, feeling defeated.",
            "\"I feel like I'm going insane with this boredom, {target}. I need your help to break free from this never-ending monotony,\" {initiator} pleads, looking for a solution.",
            "\"Every day feels like Groundhog Day, {target}. I can't bear this boredom any longer,\" {initiator} says, their voice filled with monotony."
        ]
    },
    "mixer_social_ComplimentArt_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} compliments {target} on their art."
        ],
        "actions": [
            "\"{target}, I have to say, your art is absolutely incredible. I'm blown away,\" {initiator} exclaims with genuine admiration.",
            "\"I've been meaning to tell you, {target}, your art is truly inspiring. You have such a unique talent,\" {initiator} says, unable to contain their awe.",
            "\"I can't help but be captivated by your art, {target}. It speaks to me on a whole different level,\" {initiator} compliments, their eyes filled with appreciation.",
            "\"You have an extraordinary gift, {target}. Your art is a masterpiece, and I'm honored to witness it,\" {initiator} praises, feeling a sense of privilege.",
            "\"I've seen a lot of art in my life, but yours, {target}, is something else entirely. It's like you have a direct line to the soul,\" {initiator} marvels, unable to look away.",
            "\"{target}, your art is like a breath of fresh air. It's so refreshing and unique, I can't help but be in awe,\" {initiator} commends, feeling a surge of inspiration.",
            "\"I've been following your art for a while now, {target}, and I just have to tell you how incredibly talented you are. Your work speaks volumes,\" {initiator} praises, genuinely impressed.",
            "\"I don't say this lightly, {target}, but your art is truly exceptional. It has a way of touching hearts and stirring emotions,\" {initiator} compliments, their voice filled with sincerity.",
            "\"Your art, {target}, is a true reflection of your soul. It's raw, authentic, and absolutely breathtaking,\" {initiator} commends, feeling a deep connection.",
            "\"{target}, your art has the power to transport me to another world. It's like magic on canvas,\" {initiator} admires, awe-struck by the talent before them."
        ]
    },
    "mixer_social_ComplimentCostume_Targeted_Friendly": {
        "pre_actions": [
            "{initiator} compliments {target}'s costume."
        ],
        "actions": [
            "\"{target}, I have to say, your costume is absolutely stunning,\" {initiator} exclaims, admiringly.",
            "\"I can't help but be in awe of your costume, {target}. It's truly remarkable,\" {initiator} says, impressed.",
            "\"Wow, {target}, your costume is on a whole other level. You really nailed it,\" {initiator} compliments, with a smile.",
            "\"{target}, I have to give credit where credit is due. Your costume is hands down the best I've seen,\" {initiator} says genuinely.",
            "\"Your costume is so creative, {target}. I love how you've put everything together,\" {initiator} praises, with a touch of envy.",
            "\"I'm blown away by your costume, {target}. It's so well-crafted and attention-grabbing,\" {initiator} compliments, in awe.",
            "\"{target}, I have to say, your costume is absolutely flawless. You look incredible,\" {initiator} says, unable to take their eyes off {target}.",
            "\"I can't help but be amazed by your costume, {target}. It's like you stepped right out of a movie,\" {initiator} compliments, with a hint of admiration.",
            "\"{target}, I have to admit, your costume is seriously impressive. You've got serious talent,\" {initiator} says, sincerely.",
            "\"Your costume is beyond words, {target}. It's like a work of art. You should be proud,\" {initiator} praises, genuinely impressed."
        ]
    },
    "mixer_social_ConsoleAboutDeath_Targeted_Friendly_EmotionSpecific": {
        "pre_actions": [
            "{initiator} consoles {target} about a recent death."
        ],
        "actions": [
            "\"I'm so sorry for your loss, {target},\" {initiator} says, offering a sympathetic smile.",
            "\"I can't even begin to imagine how you're feeling right now, {target}, but please know that I'm here for you,\" {initiator} says, gently placing a hand on {target}'s shoulder.",
            "\"Words can't express the pain you must be going through, {target}, but please know that I'm here to listen if you want to talk,\" {initiator} says, their voice filled with compassion.",
            "\"{target}, I heard about your loss and I wanted to come and offer my condolences. I'm here for you, no matter what,\" {initiator} says, giving {target} a heartfelt hug.",
            "\"I know the pain of losing someone you love, {target}, and I want you to know that I understand. If you need someone to lean on, I'm here,\" {initiator} says, their voice filled with empathy.",
            "\"{target}, losing someone is never easy, but you don't have to face it alone. Lean on me, lean on our friendship, and we'll get through this together,\" {initiator} says, reaching out to hold {target}'s hand.",
            "\"I wish there was something I could say or do to take away your pain, {target}, but just know that I'm here for you. Lean on me whenever you need,\" {initiator} says, their voice filled with sincerity.",
            "\"{target}, grief is a heavy burden to bear, but please remember that you're not alone. I'm here to support you in any way I can,\" {initiator} says, their eyes filled with compassion.",
            "\"I know that nothing I say can bring back your loved one, {target}, but I want you to know that I'm here to offer my support and comfort during this difficult time,\" {initiator} says, offering a gentle smile.",
            "\"{target}, I can't begin to fathom the depth of your pain, but please know that I'm here to hold your hand and be a shoulder to lean on,\" {initiator} says, their voice filled with warmth and understanding."
        ]
    },
    "mixer_social_ConsoleAboutDeath_Targeted_Friendly_EmotionSpecific_c2a": {
        "pre_actions": [
            "{initiator} consoles {target} about a recent death."
        ],
        "actions": [
            "\"I heard about your loss, {target}. I'm so sorry. If you need anything, I'm here for you,\" {initiator} says softly, offering a comforting hand.",
            "\"I can't imagine how you must be feeling, {target}. Losing someone is never easy. If you ever need to talk or just sit in silence, I'm here,\" {initiator} says, their voice filled with empathy.",
            "\"I know there are no words that can ease your pain, {target}, but please know that I'm here for you. Lean on me whenever you need,\" {initiator} says, their eyes filled with compassion.",
            "\"I'm truly sorry for your loss, {target}. Losing someone we care about is incredibly tough. If you want to share memories or simply have someone to listen, I'm here,\" {initiator} says, their voice gentle and understanding.",
            "\"I can't take away your pain, {target}, but I can be here to support you through it. Lean on me whenever you need to,\" {initiator} says, their voice filled with warmth.",
            "\"I know this is an incredibly difficult time for you, {target}, but please remember that you don't have to face it alone. I'm here for you, no matter what,\" {initiator} says, their eyes showing genuine concern.",
            "\"I wish there was something I could say to make it better, {target}, but sometimes all we need is someone to be there for us. You're not alone in this,\" {initiator} says, their voice filled with sincerity.",
            "\"Loss is something that affects us all differently, {target}. If you ever need a shoulder to cry on or someone to vent to, I'm here. Don't hesitate to reach out,\" {initiator} says, offering a comforting smile.",
            "\"I know it feels like the world has turned upside down right now, {target}, but I want you to know that I'm here to offer my support. We'll get through this together,\" {initiator} says, their voice steady and reassuring.",
            "\"I can't possibly understand the depth of your pain, {target}, but I want you to know that I'm here to hold your hand and walk through this with you. You're not alone,\" {initiator} says, their eyes filled with empathy."
        ]
    },
    "mixer_social_DebateBestCaptains_targeted_Friendly_HighScore": {
        "pre_actions": [
            "{initiator} starts a friendly debate with {target} about the best ship captains."
        ],
        "actions": [
            "\"Hey {target}, I've been thinking about something... Who do you think is the greatest ship captain of all time?\" {initiator} asks, with a mischievous grin.",
            "\"I have a feeling we might have different opinions on this, {target}, but let's settle it once and for all: who is the best ship captain in history?\" {initiator} challenges, playfully.",
            "\"You know, {target}, I've been pondering this question for a while now: who would win in a battle of ship captains? Care to share your thoughts?\" {initiator} asks, raising an eyebrow.",
            "\"I've heard some interesting arguments about the greatest ship captains, but I'm curious to know your take on it, {target}. Who do you think deserves that title?\" {initiator} asks, genuinely intrigued.",
            "\"I've always admired your knowledge of naval history, {target}, so I have to ask: who do you believe is the most legendary ship captain?\" {initiator} prompts, eager to hear their response.",
            "\"There's been a lot of debate lately about the best ship captains, and I value your opinion, {target}. Who would you choose as the ultimate captain?\" {initiator} asks, hoping for an engaging discussion.",
            "\"I know we both have a passion for maritime history, {target}, so I'm curious: who do you think is the most iconic ship captain in the annals of time?\" {initiator} inquires, leaning in.",
            "\"You've always had an eye for detail, {target}, so I'm interested in your take on this: who is the most skilled ship captain in history?\" {initiator} asks, ready for a friendly debate.",
            "\"As fellow enthusiasts of ship captains, {target}, I have to know: who do you believe is the most legendary captain to ever set sail?\" {initiator} asks, grinning with anticipation.",
            "\"Let's settle this once and for all, {target}: who do you think is the greatest ship captain to ever command the seas?\" {initiator} asks, ready to engage in a lively discussion."
        ]
    },
    "mixer_social_DebateGameStrategy_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} starts a friendly debate with {target} about game strategies."
        ],
        "actions": [
            "\"So, {target}, I've been thinking about our game strategies lately, and I wanted to get your perspective on something,\" {initiator} says, leaning forward with a playful smile.",
            "\"I know we've always had different approaches when it comes to strategy, but hear me out on this idea,\" {initiator} says, raising an eyebrow to grab {target}'s attention.",
            "\"Let's put our competitive spirits aside for a moment and discuss our game strategies. I bet we could learn a thing or two from each other,\" {initiator} suggests, with a teasing tone.",
            "\"Hey {target}, I hope you're ready to have your mind blown because I have a game strategy that will revolutionize our approach,\" {initiator} says, rubbing their hands together in excitement.",
            "\"You know, {target}, our different game strategies always make things interesting. Care for a friendly debate to see who has the better approach?\" {initiator} proposes, smirking mischievously.",
            "\"I've been doing some research on game strategies, {target}, and I'm eager to discuss my findings with you. Can we dive into it?\" {initiator} asks, eyes shining with curiosity.",
            "\"I've been brainstorming a new tactic for our game, {target}, and I need your input. Let's bounce some ideas off each other,\" {initiator} suggests, gesturing for {target} to join them.",
            "\"I know we've debated game strategies before, {target}, but this time I've come armed with solid evidence to support my argument. Care to hear me out?\" {initiator} asks, holding up a stack of notes.",
            "\"Alright, {target}, I challenge you to a friendly debate about our game strategies. Winner gets bragging rights for the rest of the day,\" {initiator} proposes, smirking competitively.",
            "\"I have a feeling, {target}, that if we combine our game strategies, we'll become unbeatable. What do you say we give it a shot?\" {initiator} suggests, flashing a confident grin."
        ]
    },
    "mixer_social_DeclareEnemy_targeted_mean_relationship": {
        "pre_actions": [
            "{initiator} declares {target} as their enemy."
        ],
        "actions": [
            "\"I never thought it would come to this, {target}, but I have no choice. Consider yourself my enemy,\" {initiator} says, their voice cold and determined.",
            "\"You've crossed a line, {target}, and I can no longer see you as anything but my enemy,\" {initiator} declares, anger seething in their eyes.",
            "\"I never wanted it to come to this, {target}, but your actions have made it clear - you are my enemy now,\" {initiator} says, their voice filled with disappointment.",
            "\"I used to consider you a friend, {target}, but after what you've done, I can't deny it anymore - you are my enemy,\" {initiator} states firmly.",
            "\"I never thought I would say these words to you, {target}, but it's time to face the truth - you are now my enemy,\" {initiator} says, their voice trembling with a mix of anger and sadness.",
            "\"You've betrayed my trust, {target}, and I can't overlook that. From now on, consider yourself my enemy,\" {initiator} declares, their tone laced with bitterness.",
            "\"I've tried to see the good in you, {target}, but it's become clear that you are my enemy. Prepare for the consequences,\" {initiator} warns, their eyes narrowing.",
            "\"I thought we were on the same side, {target}, but your actions have proven otherwise. You've become my enemy,\" {initiator} states with a heavy heart.",
            "\"I never wanted to be enemies, {target}, but it seems that's the path we're on now. Brace yourself,\" {initiator} says, their voice filled with resignation.",
            "\"I never thought it would come to this, but you've left me no choice, {target}. You are now my enemy,\" {initiator} declares, their voice steady and unwavering."
        ]
    },
    "mixer_social_DenounceFriendship_targeted_mean_emotionSpecific": {
        "pre_actions": [
            "{initiator} cruelly denounces their friendship with {target}."
        ],
        "actions": [
            "\"I can't believe I ever considered you a friend, {target},\" {initiator} sneers, their voice dripping with disdain.",
            "\"You think we were friends? Ha! I never want to see your face again, {target},\" {initiator} says coldly.",
            "\"I'm done pretending to be friends with you, {target}. Consider our friendship over,\" {initiator} declares with a hint of satisfaction.",
            "\"All this time, I thought we were friends, but I realize now that I was mistaken. I want nothing to do with you, {target},\" {initiator} says, their voice filled with bitterness.",
            "\"I used to value our friendship, {target}, but now I see that it was all a lie. I don't want anything to do with you,\" {initiator} says, their words cutting through the air.",
            "\"I trusted you as a friend, {target}, but you've proven that I made a mistake. Our friendship is officially over,\" {initiator} says, their voice filled with disappointment.",
            "\"You've shown your true colors, {target}, and I want nothing to do with someone like you. Our friendship is over,\" {initiator} says, their tone filled with disgust.",
            "\"I thought we were friends, {target}, but I can't ignore the way you've treated me. Consider our friendship terminated,\" {initiator} says, their voice laced with anger.",
            "\"I never thought I would say this, but I don't want to be friends with you anymore, {target}. You've shown me who you really are,\" {initiator} says, their voice trembling with hurt.",
            "\"I don't need a friend like you, {target}. Our friendship is officially done,\" {initiator} says firmly, their words final."
        ]
    },
    "mixer_social_DescribeNewInvention_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} describes their new invention to {target}."
        ],
        "actions": [
            "\"Hey {target}, you won't believe what I've come up with. I've invented something truly groundbreaking,\" {initiator} says excitedly.",
            "\"I've been working on this invention for months, {target}, and I think it's finally ready to be revealed,\" {initiator} says, unable to contain their anticipation.",
            "\"You know how I've always been tinkering with gadgets, {target}? Well, I've created something incredible this time,\" {initiator} says, a twinkle in their eyes.",
            "\"I wanted to share my latest creation with you, {target}, because I value your opinion. Get ready to be amazed,\" {initiator} says, grinning from ear to ear.",
            "\"Guess what, {target}? I've invented something that will revolutionize the way we live. And I couldn't wait to show it to you,\" {initiator} says, barely able to contain their excitement.",
            "\"I've been keeping this under wraps, {target}, but I can't keep it to myself any longer. Prepare to witness my newest invention,\" {initiator} says, a sense of pride evident in their voice.",
            "\"I've been burning the midnight oil to bring this invention to life, {target}, and I think you'll be blown away by what I've created,\" {initiator} says, eager to share their achievement.",
            "\"I've been dying to tell someone about my invention, and you're the first person who came to mind, {target}. Brace yourself for something extraordinary,\" {initiator} says, unable to hide their enthusiasm.",
            "\"You're about to witness a game-changer, {target}. I've poured my heart and soul into this invention, and I can't wait to show it to you,\" {initiator} says, excitement bubbling in their voice.",
            "\"You're in for a treat, {target}. I've come up with an invention that will leave you in awe. Prepare to be amazed,\" {initiator} says, unable to hide their anticipation."
        ],
    },
    "mixer_social_DiscussCostume_targeted_Friendly": {
        "pre_actions": [
            "{initiator} discusses {target}'s costume."
        ],
        "actions": [
            "\"{target}, I have to say, your costume is absolutely stunning. How did you come up with such a creative idea?\" {initiator} compliments, admiring {target}'s outfit.",
            "\"I can't help but be in awe of your costume, {target}. It's so unique and eye-catching,\" {initiator} remarks, unable to take their eyes off {target}.",
            "\"Wow, {target}, your costume is on a whole other level. I wish I had your talent for putting together such an incredible outfit,\" {initiator} exclaims in amazement.",
            "\"{target}, I have to ask, where did you find the inspiration for your costume? It's like nothing I've ever seen before,\" {initiator} inquires, genuinely curious.",
            "\"I have to admit, {target}, your costume is the talk of the party. Everyone seems to be in awe of your creativity,\" {initiator} says with a smile.",
            "\"{target}, your costume is so impressive that I can't help but feel a little bit jealous. I wish I had thought of something as cool as that,\" {initiator} admits, slightly envious.",
            "\"I can't stop staring at your costume, {target}. It's like a work of art. Did you make it yourself?\" {initiator} asks, amazed by {target}'s craftsmanship.",
            "\"{target}, your costume is absolutely mind-blowing. It's clear that you put a lot of thought and effort into it,\" {initiator} comments, genuinely impressed.",
            "\"Everyone is raving about your costume, {target}, and I can see why. It's so imaginative and well-executed,\" {initiator} praises, unable to contain their admiration.",
            "\"I have to say, {target}, your costume is by far the best I've seen tonight. You really know how to make a statement,\" {initiator} compliments, genuinely impressed."
        ]
    },
    "mixer_social_DiscussExpandingTheFamily_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} discusses the idea of having a baby with {target} to expand their family."
        ],
        "actions": [
            "\"{target}, I've been thinking a lot about our future lately, and I want to talk to you about something important,\" {initiator} says, looking hopeful.",
            "\"You know, {target}, I've been envisioning our life together, and I can't help but imagine us starting a family,\" {initiator} says, their eyes lighting up.",
            "\"{target}, there's something I want to explore with you. Have you ever thought about what it would be like to have a child together?\" {initiator} asks, curious.",
            "\"I know it's a big decision, but lately, I've been imagining a little one running around our home. What are your thoughts on starting a family, {target}?\" {initiator} asks, gauging their reaction.",
            "\"{target}, I have this feeling deep inside that we would make amazing parents. Can we discuss the possibility of having a baby together?\" {initiator} suggests, nervously.",
            "\"There's something I've been thinking about lately, {target}, and it involves the two of us. Have you ever considered the idea of expanding our family?\" {initiator} asks, intrigued.",
            "\"{target}, I want to share something with you. I've been daydreaming about our future, and the thought of us having a child together fills me with so much joy,\" {initiator} says, smiling.",
            "\"I know this might be unexpected, but I can't ignore this desire I have to bring a child into our lives. {target}, what do you think about the idea of becoming parents?\" {initiator} asks, searching for their response.",
            "\"{target}, I've been doing some soul searching, and I can't shake off this longing to have a baby. Can we talk about the possibility of starting a family?\" {initiator} says, looking earnest.",
            "\"I've been doing a lot of thinking lately, {target}, and I can't help but imagine our love expanding and creating a little life together. What do you think about having a baby?\" {initiator} asks, hopeful."
        ]
    },
    "mixer_social_DiscussFitnessTechniques_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} discusses fitness techniques with {target}."
        ],
        "actions": [
            "\"So, {target}, I've been trying out this new workout routine and it's been amazing,\" {initiator} says enthusiastically.",
            "\"I've been researching different fitness techniques lately, and I wanted to get your opinion on them, {target},\" {initiator} says, looking curious.",
            "\"You're always so fit and active, {target}, and I was wondering if you could give me some tips on improving my workout routine,\" {initiator} asks, admiringly.",
            "\"I've been struggling with my fitness goals lately, {target}, and I was wondering if you had any advice or techniques that might help,\" {initiator} says, looking for guidance.",
            "\"I've heard about this new fitness technique that supposedly yields incredible results, {target}. Have you tried it? What do you think?\" {initiator} asks, intrigued.",
            "\"Hey, {target}, I've been trying out this unconventional fitness technique and it's been surprisingly effective. Want to hear about it?\" {initiator} says, with a hint of excitement.",
            "\"I've been feeling a bit stuck in my fitness journey lately, {target}, and I was wondering if you had any recommendations or techniques that might help me break through,\" {initiator} says, seeking advice.",
            "\"I've been experimenting with different fitness techniques recently, {target}, and I wanted to hear your thoughts on them. Maybe we could even try some together?\" {initiator} suggests, hopeful.",
            "\"I've been struggling to stay motivated with my fitness routine, {target}, and I was wondering if you had any techniques or strategies that have worked for you,\" {initiator} says, seeking inspiration.",
            "\"You always seem to know the latest fitness trends, {target}. Have you come across any interesting techniques or workouts lately that you could share with me?\" {initiator} asks, eager to learn.",
            "\"{target}, I've been trying out this new workout routine, and I'd love to hear your thoughts on it.\"",
            "\"Hey {target}, you seem to be in great shape. Can you share some fitness tips with me?\"",
            "\"So, {target}, I've been experimenting with different exercises lately. Have you tried any new fitness techniques that you think are worth sharing?\"",
            "\"I've noticed you're really consistent with your workouts, {target}. Mind sharing some of your favorite techniques?\"",
            "\"{target}, I came across this fitness article about a new technique, and I can't decide if it's worth trying. What do you think?\" {initiator} says, showing the article to {target}.",
            "\"Hey {target}, I've been trying to improve my fitness lately. Can you recommend any techniques that have worked well for you?\"",
            "\"I've been struggling with my workout routine recently, {target}. Do you have any fitness techniques that could help me get back on track?\" {initiator} says, feeling a bit discouraged.",
            "\"{target}, I heard about this interesting fitness technique that's supposed to be really effective. Have you tried anything like that before?\"",
            "\"I'm thinking of incorporating some new fitness techniques into my routine, {target}. Any suggestions on where to start?\" {initiator} asks, seeking advice.",
            "\"Hey {target}, I noticed you were doing a unique exercise. Can you explain the technique behind it? It looks really effective.\"",
        ]
    },
    "mixer_social_DiscussGourmetDishes_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} discusses gourmet dishes with {target}."
        ],
        "actions": [
            "\"I recently tried this amazing gourmet dish, {target}, and I can't stop thinking about it,\" {initiator} says excitedly.",
            "\"You have to try this gourmet dish I just discovered, {target}, it's absolutely divine,\" {initiator} suggests with a smile.",
            "\"Do you have any recommendations for gourmet dishes, {target}? I'm in the mood to try something new,\" {initiator} asks curiously.",
            "\"I've been experimenting with gourmet cooking lately, {target}, and I think I've finally perfected a dish. Would you like to taste it?\" {initiator} offers with a hint of pride.",
            "\"I never thought I would be interested in gourmet dishes, but I recently had one that completely changed my perspective,\" {initiator} admits, intrigued.",
            "\"I've been studying gourmet cuisine for a while now, {target}, and I'd love to share some of my favorite recipes with you,\" {initiator} suggests enthusiastically.",
            "\"{target}, have you ever tried a gourmet dish that made you feel like you were in heaven? I had that experience recently,\" {initiator} says, reminiscing.",
            "\"I'm planning a gourmet dinner party, {target}, and I would love your input on the menu. What do you think would impress our guests?\" {initiator} asks, seeking advice.",
            "\"I can't get enough of gourmet dishes lately, {target}. It's like a whole new world of flavors and textures has opened up to me,\" {initiator} confesses with a grin.",
            "\"I've been exploring different gourmet cuisines, {target}, and I can't wait to share my findings with you. Are you open to trying new things?\" {initiator} asks with enthusiasm."
        ]
    },
    "mixer_social_DiscussHydration_targeted_Friendly_Athlete_AlwaysOn_STC": {
        "pre_actions": [
            "{initiator}, an athlete, discusses the importance of hydration with {target}."
        ],
        "actions": [
            "\"{target}, I wanted to talk to you about something that's been on my mind lately. It's about the importance of staying hydrated,\" {initiator} says.",
            "\"I've noticed how much you push yourself during workouts, {target}, and I think it's crucial that we talk about proper hydration,\" {initiator} says.",
            "\"Hey {target}, can I give you some advice? I've learned the hard way that staying hydrated is key to performing at our best,\" {initiator} says.",
            "\"I've been doing some research on the impact of hydration on athletic performance, and it's fascinating. {target}, can I share what I've learned with you?\" {initiator} asks.",
            "\"You know, {target}, I used to underestimate the importance of hydration. But now I realize it can make or break an athlete's performance,\" {initiator} says, grabbing {target}'s attention.",
            "\"I've been looking into ways to improve our athletic performance, and one thing keeps coming up: staying properly hydrated. Want to hear what I found?\" {initiator} asks, eager to share their knowledge.",
            "\"Listen, {target}, I've noticed that you sometimes forget to drink enough water during workouts. I thought we could discuss why it's crucial to stay hydrated,\" {initiator} says, concern evident in their voice.",
            "\"Hydration is something that's often overlooked, but it's incredibly important for athletes like us. {target}, can we talk about how we can improve in this area?\" {initiator} suggests, looking determined.",
            "\"I've been trying out different hydration techniques lately, {target}, and I think you could benefit from them too. Can I show you some?\" {initiator} asks, excitedly.",
            "\"Hey {target}, I wanted to share some tips I've learned about staying properly hydrated. I think it could really optimize our athletic performance,\" {initiator} says, ready to impart their knowledge."
        ]
    },
    "mixer_social_DiscussLackOfNewspapers_targeted_Friendly_alwysOn_situation_Day1DLC": {
        "pre_actions": [
            "{initiator} discusses the lack of newspapers with {target}."
        ],
        "actions": [
            "\"I've noticed something strange lately, {target}. Have you realized that there are no newspapers around here anymore?\" {initiator} asks, perplexed.",
            "\"Isn't it odd, {target}? I remember when there used to be newspapers on every corner. Now they seem to have vanished,\" {initiator} muses.",
            "\"You know, {target}, I've been wondering why there are no newspapers around. It's like they've disappeared overnight,\" {initiator} says, looking puzzled.",
            "\"Have you noticed the absence of newspapers, {target}? It feels like we're living in a different era,\" {initiator} comments, raising an eyebrow.",
            "\"It's strange, don't you think, {target}? The lack of newspapers makes me wonder what's going on in the world,\" {initiator} says, shaking their head.",
            "\"I can't help but feel nostalgic, {target}. The disappearance of newspapers is a sign of changing times,\" {initiator} reflects, a hint of sadness in their voice.",
            "\"I miss the days when we could sit down with a cup of coffee and read the morning newspaper, {target}. Now it's all digital,\" {initiator} laments, sighing.",
            "\"{target}, have you ever thought about why there are no newspapers around anymore? It's like they've become a relic of the past,\" {initiator} muses, deep in thought.",
            "\"I used to love the smell of fresh ink on a newspaper, {target}. Now it seems like a distant memory,\" {initiator} says, their voice tinged with nostalgia.",
            "\"Isn't it strange, {target}? The absence of newspapers feels like a void in our daily lives,\" {initiator} remarks, a touch of concern in their tone.",
            "\"{target}, have you noticed that there aren't many newspapers around anymore? It's quite frustrating,\" {initiator} says, clearly annoyed.",
            "\"I can't believe how hard it is to find a decent newspaper these days, {target}. What's going on?\" {initiator} complains, shaking their head.",
            "\"{target}, it's like newspapers have vanished into thin air. I miss the days when I could just grab one and enjoy my morning coffee,\" {initiator} sighs.",
            "\"I don't know about you, {target}, but the lack of newspapers around here is really getting on my nerves,\" {initiator} grumbles.",
            "\"It's a sad state of affairs when you can't even find a newspaper to read anymore, don't you think, {target}?\" {initiator} asks with a frown.",
            "\"I was just telling someone the other day how I miss the feel of a newspaper in my hands, {target}. It's just not the same anymore,\" {initiator} laments.",
            "\"Remember when you could find newspapers everywhere, {target}? What happened to those days? I can't stand this digital age,\" {initiator} complains passionately.",
            "\"{target}, do you have any idea where I can find a newspaper around here? It seems like they're a rare commodity these days,\" {initiator} says in frustration.",
            "\"Sometimes I feel like I'm the only person left who still prefers a newspaper to reading news online, {target}. It's quite disheartening,\" {initiator} confides.",
            "\"I just want a simple newspaper to read with my morning coffee, {target}. Why is that so difficult to find these days?\" {initiator} asks, exasperated.",
        ]
    },
    "mixer_social_DiscussLatestBook_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} discusses the latest book they've read with {target}."
        ],
        "actions": [
            "\"I just finished reading the most incredible book, {target}. I have to tell you all about it,\" {initiator} says eagerly.",
            "\"You know, {target}, I think you would absolutely love the book I just read. It has everything you enjoy,\" {initiator} suggests with a smile.",
            "\"I can't stop thinking about the book I read, {target}, and I have a feeling you'll appreciate it too. Let me tell you why,\" {initiator} says, excitedly.",
            "\"I've been dying to talk about this book with someone, and you've always been my go-to person for insightful discussions. Can we talk about it?\" {initiator} asks, hoping for a positive response.",
            "\"There's this book that completely captured my heart, {target}, and I can't help but share my thoughts with you. Are you interested?\" {initiator} inquires, curious about {target}'s reaction.",
            "\"I finished a book that had such a powerful impact on me, {target}. I want to know your thoughts on it. Can we discuss it?\" {initiator} asks, eagerly awaiting {target}'s response.",
            "\"I just read this extraordinary book, {target}, and I can't keep it to myself anymore. You have to hear about it,\" {initiator} insists, unable to contain their excitement.",
            "\"Hey {target}, I need someone to geek out with me over this book I just read. Can you spare a few minutes for a passionate discussion?\" {initiator} requests, hoping {target} will agree.",
            "\"{target}, I can't even begin to describe how much this book impacted me. I think we should grab some coffee and dissect it together,\" {initiator} suggests, the excitement evident in their voice.",
            "\"{target}, you're my go-to person for book recommendations, so I need your opinion on the latest book I read. Let's discuss it, shall we?\" {initiator} asks, eager for {target}'s insight."
        ]
    },
    "mixer_social_DiscussLogicalPuzzles_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} discusses logical puzzles with {target}."
        ],
        "actions": [
            "\"{target}, I've been really into solving logical puzzles lately. Want to try one together?\" {initiator} asks excitedly.",
            "\"I've come across this really tricky logical puzzle, and I thought you might enjoy trying to solve it with me, {target},\" {initiator} suggests.",
            "\"{target}, I've been struggling to solve this logical puzzle. Do you think you could lend me your brilliant mind?\" {initiator} wonders aloud.",
            "\"I've been obsessed with logical puzzles recently, and I think you might appreciate this one, {target}. Care to give it a shot?\" {initiator} proposes.",
            "\"{target}, I've been looking for a logical puzzle partner. Would you be interested in tackling some brain-teasers together?\" {initiator} asks with a hopeful smile.",
            "\"I find logical puzzles fascinating, {target}, and I think it would be fun to discuss and solve them with you. Are you up for it?\" {initiator} asks with genuine curiosity.",
            "\"{target}, I was wondering if you enjoy logical puzzles as much as I do. I have this challenging one that has been on my mind. Care to take a crack at it?\" {initiator} suggests.",
            "\"I've been looking for someone who appreciates logical puzzles as much as I do, {target}. Are you interested in diving into one with me?\" {initiator} asks, eyes gleaming with excitement.",
            "\"{target}, I've been stuck on this logical puzzle for days. I'm beginning to think a fresh perspective might help. Can I bounce some ideas off you?\" {initiator} requests.",
            "\"{target}, I recently came across a series of mind-bending logical puzzles. I thought discussing them with you might be intellectually stimulating. What do you think?\" {initiator} proposes."
        ]
    },
    "mixer_social_DiscussNeighborhoodChanges_targeted_friendly_alwaysOn_neighbor": {
        "pre_actions": [
            "{initiator} discusses recent changes in the neighborhood with {target}."
        ],
        "actions": [
            "\"So, {target}, have you noticed anything different around the neighborhood lately?\" {initiator} asks, curiously.",
            "\"I wanted to talk to you about some changes I've noticed in our neighborhood, {target}. Have you seen them too?\" {initiator} inquires.",
            "\"Hey, {target}, there's something interesting happening in our neighborhood. Have you noticed anything out of the ordinary?\" {initiator} wonders aloud.",
            "\"I can't help but notice the recent changes in our neighborhood, {target}. What are your thoughts on them?\" {initiator} asks, seeking {target}'s opinion.",
            "\"You know, {target}, there have been some significant developments in the neighborhood. Have you seen them? Let's discuss,\" {initiator} suggests.",
            "\"{target}, I wanted to get your perspective on the recent changes in the neighborhood. Care to share your observations?\" {initiator} prompts.",
            "\"I've been meaning to talk to you about this, {target}. The neighborhood seems to be undergoing some transformations. Have you noticed too?\" {initiator} asks, genuinely curious.",
            "\"As someone who's lived here for a while, {target}, I'm interested in hearing your thoughts on the recent changes in the neighborhood. Care to share?\" {initiator} asks, leaning in.",
            "\"Isn't it strange, {target}? The neighborhood has been going through some changes lately. Have you talked to anyone about it?\" {initiator} asks, raising an eyebrow.",
            "\"{target}, I think we need to discuss the recent changes in the neighborhood. It's been on my mind, and I want to hear your thoughts,\" {initiator} says, with a hint of concern."
        ]
    },
    "mixer_social_DismissEvilWays_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} dismisses their friend {target}'s evil ways."
        ],
        "actions": [
            "\"{target}, I've known you for so long, but I refuse to believe that you're truly evil,\" {initiator} says adamantly.",
            "\"I know you've done some terrible things, {target}, but deep down, I still see a glimmer of goodness in you,\" {initiator} says, searching {target}'s eyes.",
            "\"{target}, even though everyone thinks you're the villain, I can't bring myself to believe it. There has to be a reason for your actions,\" {initiator} says, defending {target}.",
            "\"I've heard all the stories, {target}, but I can't accept that you're inherently evil. There must be a different side to you,\" {initiator} says, crossing their arms.",
            "\"I know you've caused a lot of harm, {target}, but I'm willing to give you the benefit of the doubt. Maybe there's more to your story,\" {initiator} says, with a hint of uncertainty.",
            "\"Others might see you as a monster, {target}, but I refuse to see you that way. There's still a chance for redemption,\" {initiator} says, challenging {target}.",
            "\"{target}, I've seen the darkness in your actions, but I also believe that deep down, you're still capable of change,\" {initiator} says, their voice filled with hope.",
            "\"I know I'm in the minority here, {target}, but I believe in your capacity for good. Don't let the world's judgment consume you,\" {initiator} says, reaching out a hand.",
            "\"{target}, I can't ignore the pain you've caused, but I also can't ignore the possibility for growth and transformation,\" {initiator} says, gesturing towards {target}.",
            "\"I refuse to let go of the belief that there's some goodness left in you, {target}. Please, prove me right,\" {initiator} says earnestly."
        ]
    },
    "mixer_social_DismissGoodness_targeted_mean_alwaysOn": {
        "pre_actions": [
            "{initiator} dismisses {target}'s good nature hurtfully."
        ],
        "actions": [
            "\"{target}, don't act like you're some saint. You're just as selfish and uncaring as the rest of them,\" {initiator} spits out, their words biting with a tinge of bitterness.",
            "\"I don't need your kindness, {target}. It's all just an act anyways,\" {initiator} says, rolling their eyes in disdain.",
            "\"Save your good intentions for someone who actually believes in them, {target}. I'm not interested,\" {initiator} scoffs, turning away dismissively.",
            "\"{target}, your kindness is nothing but a facade. I see right through it, and I want nothing to do with it,\" {initiator} says, their voice laced with contempt.",
            "\"{target}, don't pretend like you care. It's obvious that you're only looking out for yourself,\" {initiator} retorts, their tone dripping with sarcasm.",
            "\"I'm tired of your fake gestures of goodwill, {target}. They mean nothing to me, and they never will,\" {initiator} says coldly, refusing to meet {target}'s eyes.",
            "\"{target}, stop with the act already. Your good nature is nothing but a mask. Take it off and show your true colors,\" {initiator} sneers, their words cutting deep.",
            "\"I've seen enough of your false kindness, {target}. It's time to face the truth - you're no better than the rest of them,\" {initiator} declares, their voice filled with anger.",
            "\"{target}, your good intentions won't change a thing. I don't need your pity, and I certainly don't need you,\" {initiator} says sharply, pushing {target} away.",
            "\"Don't think your acts of kindness make up for everything, {target}. You can't erase the past with a few empty gestures,\" {initiator} says, their voice filled with resentment."
        ]
    },
    "mixer_social_Divorce_targeted_mean_relationship": {
        "pre_actions": [
            "{initiator} maliciously atttempts to intitate a divorce from {target}."
        ],
        "actions": [
            "\"{target}, I've made my decision. I want a divorce,\" {initiator} says coldly, their eyes filled with determination.",
            "\"I've been holding this back for too long, {target}, but I can't pretend anymore. I want out of this marriage,\" {initiator} states, their voice laced with bitterness.",
            "\"I've been plotting my escape for a while now, {target}, and I think it's time we end this charade. I want a divorce,\" {initiator} announces, a vindictive smile playing on their lips.",
            "\"I've had enough of pretending, {target}, and I refuse to continue living a lie. I'm filing for divorce,\" {initiator} declares, their tone filled with resentment.",
            "\"There's no going back, {target}. I don't love you anymore, and I want a divorce,\" {initiator} says icily, their eyes devoid of any affection.",
            "\"I've realized that I deserve better than this, {target}. Consider this my official request for a divorce,\" {initiator} states firmly, crossing their arms.",
            "\"You thought you could control me forever, {target}, but I won't let you. I'm filing for divorce,\" {initiator} says with a hint of defiance.",
            "\"{target}, I've found someone else. Someone who makes me feel alive again. It's time we end this marriage,\" {initiator} admits shamelessly.",
            "\"I'm done pretending that everything is fine, {target}. The truth is, I've fallen out of love with you, and I want a divorce,\" {initiator} confesses with brutal honesty.",
            "\"I know this will hurt you, {target}, but I can't bear to pretend anymore. I'm leaving you. I want a divorce,\" {initiator} says softly, yet resolute."
        ]
    },
    "mixer_social_EnthuseAbout_ThrillOfTheSteal_friendly_Klepto": {
        "pre_actions": [
            "{initiator} enthuses about the thrill of stealing to {target}."
        ],
        "actions": [
            "\"You know, {target}, there's something exhilarating about the art of stealing,\" {initiator} says, a mischievous glint in their eyes.",
            "\"I have a confession to make, {target}. Stealing is like an addiction to me, and I can't resist the thrill,\" {initiator} admits, looking both guilty and excited.",
            "\"I've never told anyone this before, but I find so much joy in the act of stealing. It's an adrenaline rush like no other,\" {initiator} confesses, unable to hide their excitement.",
            "\"There's something about the rush of stealing that just gets my blood pumping, {target}. I can't explain it,\" {initiator} says, their voice filled with a mixture of excitement and shame.",
            "\"{target}, I never thought I would admit this, but stealing gives me a high like nothing else. It's like a rebellious escape from reality,\" {initiator} says, their face flushed with a mixture of guilt and excitement.",
            "\"I have a secret, {target}, one that I have never shared with anyone else. Stealing gives me a thrill that I can't deny,\" {initiator} says, nervously fidgeting with their fingers.",
            "\"I hope you don't judge me, {target}, but I find stealing to be an exhilarating experience. The adrenaline rush is addictive,\" {initiator} admits, a hint of excitement in their voice.",
            "\"{target}, I'm about to share something with you that I have never shared with anyone else. I get an inexplicable rush from stealing,\" {initiator} confesses, looking both anxious and thrilled.",
            "\"I need to get something off my chest, {target}. Stealing gives me a burst of adrenaline that nothing else can compare to,\" {initiator} says, looking both guilty and invigorated.",
            "\"There's a side of me that I've kept hidden from the world, {target}. Stealing is like a dangerous thrill that I can't resist,\" {initiator} admits, their eyes gleaming with a mix of excitement and apprehension."
        ]
    },
    "mixer_social_EnthuseAboutCakes_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} enthusiastically talks about cakes with {target}."
        ],
        "actions": [
            "\"I just have to share with you, {target}, my all-time favorite cake flavor! It's a classic chocolate cake with layers of rich chocolate ganache. It's pure heaven,\" {initiator} says with a sparkle in their eyes.",
            "\"You won't believe this, {target}, but I recently discovered a bakery that makes the most amazing red velvet cake. The cream cheese frosting is so velvety smooth, it practically melts in your mouth,\" {initiator} gushes, unable to contain their excitement.",
            "\"You know, {target}, I've always been obsessed with baking. Lately, I've been experimenting with different flavors, and I must say, my lemon-blueberry cake is to die for. The burst of tangy lemon combined with the sweetness of fresh blueberries is just divine,\" {initiator} says, a proud smile spreading across their face.",
            "\"I can't stop thinking about this incredible carrot cake recipe I stumbled upon, {target}. It's moist, perfectly spiced, and the cream cheese frosting complements it so well. Every bite is like a burst of cozy nostalgia,\" {initiator} raves, their mouth watering at the thought.",
            "\"You're never going to believe this, {target}, but I recently attended a cake decorating class. I learned how to create these intricate floral designs using buttercream frosting. I can't wait to show you the pictures,\" {initiator} says, their excitement evident in their voice.",
            "\"There's a new bakery in town, {target}, and they make the most delicious raspberry almond cake. The combination of the nutty almond flavor and the juicy sweetness of fresh raspberries is like a match made in dessert heaven,\" {initiator} raves, their enthusiasm contagious.",
            "\"I've always had a weakness for cheesecake, {target}. The creaminess, the velvety texture, it's just so indulgent. Have you ever tried a New York-style cheesecake? It's a classic that never disappoints,\" {initiator} says, their eyes lighting up.",
            "\"Let me tell you about this incredible triple chocolate mousse cake, {target}. It's a chocolate lover's dream come true! Layers of decadent chocolate mousse, dark chocolate ganache, and a moist chocolate cake base. It's pure bliss,\" {initiator} says with a dreamy expression.",
            "\"{target}, have you ever heard of a black forest cake? It's a German specialty, and it's absolutely divine. Layers of chocolate cake, whipped cream, and cherries, topped with chocolate shavings. It's like a taste of heaven,\" {initiator} raves, their excitement palpable.",
            "\"I'm so glad I ran into you, {target}, because I have been dying to talk about this magnificent strawberry shortcake I had recently. The sponge cake was unbelievably fluffy, and the fresh strawberries were so juicy and sweet. It was perfection,\" {initiator} says, their enthusiasm overflowing."
        ]
    },
    "mixer_social_EnthuseAboutCelebrations_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} enthuses about celebrations with {target}."
        ],
        "actions": [
            "\"I have to say, {target}, I absolutely love celebrations! There's just something magical about them,\" {initiator} exclaims, their eyes sparkling with excitement.",
            "\"You know, {target}, I can't help but get a rush of joy whenever I think about celebrations. They bring people together in such a beautiful way,\" {initiator} says with a wide smile.",
            "\"There's this indescribable feeling that fills my heart whenever I'm surrounded by the energy of a celebration. It's like pure happiness,\" {initiator} gushes, their voice filled with enthusiasm.",
            "\"I've always been a firm believer in celebrating even the smallest victories in life. It's such a wonderful way to appreciate the little things,\" {initiator} shares, their tone brimming with passion.",
            "\"Every celebration holds a special place in my heart, {target}. It's a chance to create lasting memories and cherish the moments that truly matter,\" {initiator} says, their voice filled with nostalgia.",
            "\"Whether it's a birthday, a holiday, or simply a gathering of loved ones, celebrations have this way of making everything feel so much more vibrant and alive,\" {initiator} muses, a hint of nostalgia in their voice.",
            "\"I thrive on the energy of celebrations, {target}. The laughter, the music, the joyous atmosphere—it's like a burst of positive energy that fuels my soul,\" {initiator} confesses with a twinkle in their eye.",
            "\"There's something truly magical about celebrations, {target}. They have the power to bring people together and create moments that will be treasured forever,\" {initiator} says, their voice filled with awe.",
            "\"I've always been drawn to celebrations, {target}. The anticipation, the decorations, the shared happiness—it's like stepping into a world of pure bliss,\" {initiator} says, their voice brimming with excitement.",
            "\"Whenever a celebration is on the horizon, I can't help but feel a surge of anticipation. It's like the promise of something wonderful about to unfold,\" {initiator} shares, a hint of eagerness in their voice."
        ],
    },
    "mixer_social_EnthuseAboutFruitcake_trageted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} enthusiastically talks about fruitcakes with {target}."
        ],
        "actions": [
            "\"{target}, you won't believe how much I love fruitcakes! They are like little slices of heaven,\" {initiator} exclaims, eyes sparkling with excitement.",
            "\"You know, {target}, there's something about fruitcakes that just brings me pure joy. They are my absolute favorite dessert,\" {initiator} gushes, unable to contain their enthusiasm.",
            "\"I have to tell you, {target}, fruitcakes are my guilty pleasure. I can eat them all day, every day,\" {initiator} confesses with a wide grin.",
            "\"You might think I'm crazy, {target}, but I am absolutely obsessed with fruitcakes. I can't resist their deliciousness,\" {initiator} admits, laughing.",
            "\"{target}, I have a confession to make - I have an undying love for fruitcakes. They are like a piece of art to me,\" {initiator} says, their voice filled with genuine adoration.",
            "\"I don't know what it is, {target}, but there's something about fruitcakes that makes my taste buds dance with joy. I can't get enough of them,\" {initiator} says, licking their lips in anticipation.",
            "\"You know what's the best thing in the world, {target}? Fruitcakes! They are my weakness, my ultimate comfort food,\" {initiator} declares, a dreamy expression on their face.",
            "\"I have a secret obsession, {target}, and it's fruitcakes. I could talk about them for hours, they are just so delicious,\" {initiator} admits, their voice filled with excitement.",
            "\"{target}, I have to share this with you - fruitcakes are my absolute favorite dessert. They bring so much happiness into my life,\" {initiator} says, their eyes shining with delight.",
            "\"I have a little secret, {target}, and it involves fruitcakes. I can't resist their temptation, they are my ultimate indulgence,\" {initiator} confesses, a mischievous smile playing on their lips."
        ]
    },
    "mixer_social_FakeAlienContact_targeted_friendly_alwaysOn_prank": {
        "pre_actions": [
            "{initiator} pranks {target} by lying about being contacted by aliens."
        ],
        "actions": [
            "\"{target}, you won't believe what just happened. I was contacted by aliens last night,\" {initiator} says, trying to suppress a mischievous grin.",
            "\"I can't keep this to myself anymore, {target}. I had an encounter with extraterrestrial beings,\" {initiator} says, barely able to contain their excitement.",
            "\"You're not going to believe what I'm about to tell you, {target}. Brace yourself. Aliens contacted me,\" {initiator} says, their eyes wide with anticipation.",
            "\"I have a confession to make, {target}. I made up that story about aliens contacting me. It was just a prank,\" {initiator} admits, unable to hide their amusement.",
            "\"I have something important to tell you, {target}. I've been contacted by beings from another planet. It's true,\" {initiator} says, trying to keep a straight face.",
            "\"I've been keeping this secret for a while now, {target}. Last night, aliens reached out to me,\" {initiator} says, struggling to maintain a serious tone.",
            "\"I know this may sound crazy, but I need to tell you. Aliens made contact with me, {target},\" {initiator} says, a mischievous glint in their eyes.",
            "\"I've been debating whether to tell you or not, {target}, but I think it's time you know. Aliens contacted me,\" {initiator} says, feigning seriousness.",
            "\"I've been meaning to tell you this, {target}, but I didn't know how you'd react. I was contacted by aliens,\" {initiator} says, trying to gauge {target}'s response.",
            "\"I can't hold it in any longer, {target}. Aliens reached out to me, and I had to share it with someone I trust,\" {initiator} says, struggling to contain their laughter."
        ]
    },
    "mixer_social_FindCommonGround_targeted_friendly_lowScore": {
        "pre_actions": [
            "{initiator} tries to find common ground with {target}."
        ],
        "actions": [
            "\"So, {target}, I heard you're a fan of ",
            "\"I couldn't help but notice your ",
            "\"Last week, I saw you at ",
            "\"I overheard you talking about your ",
            "\"I noticed you have ",
            "\"You have an impressive passion for ",
            "\"I saw your collection of ",
            "\"I heard you love ",
            "\"I noticed you wearing ",
            "\"I saw your "
        ]
    },
    "mixer_social_FlashCrazyEyes_targeted_funny_emotionSpecific": {
        "pre_actions": [
            "{initiator} stares at {target} with playful madness in their eyes."
        ],
        "actions": [
            "{initiator} breaks into a mischievous grin, their eyes locked on {target} with a glint of madness.",
            "With a playful twinkle in their eyes, {initiator} gazes at {target}, a mischievous smile tugging at the corners of their lips.",
            "{initiator} stares at {target} with a gleam of mischief in their eyes, silently daring them to join in the fun.",
            "A mischievous spark ignites in {initiator}'s eyes as they lock their gaze with {target}, silently conveying their playful intentions.",
            "With an impish expression, {initiator} fixates their gaze on {target}, a mischievous glimmer dancing in their eyes.",
            "{initiator} stares at {target} with a mischievous glint in their eyes, as if plotting something outrageous.",
            "A playful madness flickers in {initiator}'s eyes as they stare at {target}, a mischievous challenge evident in their gaze.",
            "With a mischievous gleam in their eyes, {initiator} locks their gaze onto {target}, silently beckoning them into their playful world.",
            "{initiator} stares at {target} with an infectious playfulness in their eyes, silently inviting them to join in on the fun.",
            "A mischievous madness dances in {initiator}'s eyes as they fix their gaze on {target}, silently conveying their desire for some playful mischief."
        ]
    },
    "mixer_social_FrenziedKiss_targeted_romance_emotionSpecific": {
        "pre_actions": [
            "{initiator} gives a frenzied kiss to {target}."
        ],
        "actions": [
            "\"{target}, I can't hold it in any longer. Please forgive me for what I'm about to do,\" {initiator} whispers before giving {target} a frenzied kiss.",
            "In a moment of impulsiveness, {initiator} grabs {target}'s face and kisses them passionately, their heart racing.",
            "After days of building tension, {initiator} finally gives in to their desires and kisses {target} with an intensity they have never felt before.",
            "{initiator} leans in, unable to resist the magnetic pull between them, and kisses {target} fiercely, their lips crashing together in a frenzy.",
            "In a moment of vulnerability, {initiator} throws caution to the wind and kisses {target} with reckless abandon, not caring about the consequences.",
            "Lost in a whirlwind of emotions, {initiator} grabs {target} by the waist and pulls them into a heated kiss, their lips meeting in a frenzy of longing.",
            "With a surge of passion, {initiator} seizes the opportunity and kisses {target} fervently, their mouths melding together in an explosion of desire.",
            "As their eyes meet, an undeniable attraction takes hold, and {initiator} leans in to kiss {target} urgently, their lips meeting in a frenzied embrace.",
            "In a moment of impulsive bravery, {initiator} closes the distance between them and kisses {target} passionately, their hearts pounding in sync.",
            "Driven by an overwhelming desire, {initiator} crashes their lips onto {target}'s, surrendering to the intoxicating chemistry between them."
        ]
    },
    "mixer_Social_Friendly_FigureOutDifferences": {
        "pre_actions": [
            "{initiator} tries to figure out differences with {target} in a friendly way."
        ],
        "actions": [
            "\"So {target}, I've been thinking, we've been friends for so long, but we have our fair share of differences. Let's try to understand each other better,\" {initiator} suggests with a smile.",
            "\"You know, {target}, I've noticed that we have contrasting opinions on certain things, and I'd really like to bridge that gap,\" {initiator} says.",
            "\"I've always found it intriguing how we can be friends despite our differences, but I think it's about time we explore them in a more constructive manner,\" {initiator} says thoughtfully.",
            "\"I believe our differences have the potential to strengthen our bond if we truly take the time to listen and understand each other,\" {initiator} proposes, hoping that {target} agrees.",
            "\"Hey, {target}, wouldn't it be interesting to sit down and discuss our differences? I genuinely want to know more about what makes us who we are,\" {initiator} suggests with genuine curiosity.",
            "\"I've come to realize that our differences add a unique flavor to our friendship. Let's embrace our dissimilarities and grow even closer,\" {initiator} says, extending an olive branch.",
            "\"There's a beauty in embracing differences, don't you think? Let's have a lighthearted conversation and discover more about our contrasting perspectives,\" {initiator} suggests, trying to break the ice.",
            "\"I cherish our friendship, {target}, and that includes acknowledging and appreciating our differences. Are you up for exploring those differences?\" {initiator} asks, curious to see {target}'s response.",
            "\"Sometimes, our differences can lead to misunderstandings, but I truly believe that by understanding each other more, we can prevent that from happening in the future,\" {initiator} says, speaking proactively."
        ],
    },
    "mixer_social_GiveColdShoulder_targeted_mean_Female": {
        "pre_actions": [
            "{initiator} cruelly gives {target} the cold shoulder."
        ],
        "actions": [
            "{target} approaches {initiator} with a warm smile, but {initiator} turns away without a word.",
            "{initiator} pretends not to notice {target}'s presence, intentionally avoiding eye contact.",
            "{target} tries to strike up a conversation with {initiator}, but {initiator} dismisses them with a dismissive wave of their hand.",
            "{initiator} deliberately walks past {target} without acknowledging their existence.",
            "As {target} attempts to engage in a friendly conversation, {initiator} abruptly interrupts saying, \"I don't have time for this\" and walks away.",
            "{target} reaches out for a hug, but {initiator} energetically recoils, leaving {target} feeling bewildered and hurt.",
            "Amid a group conversation, {initiator} pointedly ignores {target}'s contributions, depriving them of any recognition.",
            "{initiator} deliberately turns their back on {target} when they approach, making it clear they're not interested in interacting.",
            "Seeing {target} approach, {initiator} quickly finds an excuse to leave the room, avoiding any interaction.",
            "{target} attempts to make eye contact with {initiator}, but {initiator} focuses their gaze on anything but {target}, effectively disregarding their presence."
        ]
    },
    "mixer_social_GiveColdShoulder_targeted_mean_Male": {
        "pre_actions": [
            "{initiator} gives the cold shoulder to {target} in a mean way."
        ],
        "actions": [
            "{initiator} glares icy daggers at {target} and walks past, ignoring their presence completely.",
            "{initiator} scoffs at {target} and scoffs, \"Like I would waste a single word on you.\"",
            "{initiator} rolls their eyes at {target}, making it clear how little they think of them.",
            "{initiator} snubs {target} with a cold, haughty stare.",
            "{initiator} gives {target} a condescending smirk and deliberately looks away."
        ]
    },
    "mixer_social_GiveFakeBadNews_targeted_mischief_skills": {
        "pre_actions": [
            "{initiator} mischievously gives fake bad news to {target}."
        ],
        "actions": [
            "\"{target}, I have something to tell you. Brace yourself, it's not good news,\" {initiator} says with a malicious grin.",
            "\"You know, {target}, there's something I've been keeping from you. Don't freak out, but I think you deserve to know,\" {initiator} says, enjoying the anticipation.",
            "\"I hate to do this to you, {target}, but I have some terrible news. Prepare yourself,\" {initiator} says, relishing in their cruel intentions.",
            "\"I've been holding onto something, {target}, something that might turn your world upside down. I think it's time you hear it,\" {initiator} says, delighting in the forthcoming chaos.",
            "\"You won't believe what just happened, {target}. I've got news that will rock your world. Brace yourself,\" {initiator} says, unable to suppress a sadistic smile.",
            "\"There's something I need to tell you, {target}, while it's still fresh in my mind. Don't yell at me, but this news isn't going to be easy,\" {initiator} says, enjoying {target}'s imminent distress.",
            "\"I promised myself I wouldn't do this, {target}, but seeing you like this gives me a twisted sense of satisfaction. Are you ready for some dreadful news?\" {initiator} taunts, their eyes gleaming with mischief.",
            "\"{target}, before you get too comfortable, there's something that will make you squirm. I hope you're prepared for this,\" {initiator} says with a cruel chuckle.",
            "\"I know how much you value honesty, {target}, so I couldn't resist. Brace yourself for a dose of bad news that could ruin your day,\" {initiator} says, savoring the ability to cause havoc.",
            "\"I'm sorry to ruin your day, {target}, but there's something I learned that I simply can't keep to myself. Get ready for some fake bad news,\" {initiator} says, secretly reveling in the upcoming chaos."
        ]
    },
    "mixer_social_GoodTrait_HelpOut": {
        "pre_actions": [
            "{initiator} helps out {target} showcasing their good traits."
        ],
        "actions": [
            "\"{target}, I noticed you were struggling with that task. Let me lend a hand,\" {initiator} says with a warm smile.",
            "\"Hey there, {target}, looks like you could use some assistance. Mind if I give you a hand?\" {initiator} offers kindly.",
            "\"I've been watching you trying to figure that out, {target}. Let me save you the trouble and show you an easier way,\" {initiator} says, eager to help.",
            "\"I know we're not close, but I saw you struggling and thought I could help. Mind if I join you?\" {initiator} asks, extending a helping hand.",
            "\"{target}, it seems like you could use some backup. How about I jump in and help you get this done?\" {initiator} offers, smiling warmly.",
            "\"{target}, I noticed you could use a little assistance. Mind if I step in and lend a hand?\" {initiator} asks, genuine concern in their voice.",
            "\"You've been working so hard, {target}. Allow me to lighten your load a bit,\" {initiator} suggests, willing to pitch in.",
            "\"{target}, I hate seeing you struggle like that. Let me offer you my help,\" {initiator} says, genuine concern evident in their eyes.",
            "\"Hi there, {target}. Looks like you could use some support. Mind if I assist you?\" {initiator} offers, ready to lend a hand.",
            "\"I saw you struggling, {target}, and something inside me told me I should help. Need a hand?\" {initiator} asks, genuine concern in their voice."
        ]
    },
    "mixer_social_GossipAboutNeighbors_targeted_friendly_alwaysOn_neighbor": {
        "pre_actions": [
            "{initiator} gossips about the neighbors with {target}."
        ],
        "actions": [
            "\"You won't believe what I heard about our neighbors, {target}. It's juicy,\" {initiator} says with a mischievous smile.",
            "\"I have the inside scoop on our neighbors, {target}, and trust me, it's worth sharing,\" {initiator} says, leaning in closer.",
            "\"I've been dying to tell someone about our neighbors' scandal, {target}, and I think you're the perfect person to spill the beans to,\" {initiator} says eagerly.",
            "\"You know, {target}, I accidentally overheard something about our neighbors and it's just too good not to share. But promise you won't tell anyone,\" {initiator} says, barely containing their excitement.",
            "\"There's something I've discovered about our neighbors, and it's quite intriguing, {target}. I think you'll find it fascinating,\" {initiator} says mysteriously.",
            "\"I can't believe what I found out about our neighbors, {target}. It's the talk of the town, and I couldn't resist telling you,\" {initiator} says, barely able to contain their laughter.",
            "\"Okay, {target}, I have some inside information about our neighbors that I really need to discuss with someone. Can I trust you to keep it hush-hush?\" {initiator} asks with a sly grin.",
            "\"I feel a bit guilty about this, {target}, but I have some gossip about our neighbors that I can't keep to myself anymore. Can I count on your discretion?\"",
            "\"I was out walking the other day, {target}, and I happened to stumble upon some interesting tidbits about our neighbors. I thought you'd be interested to hear about it,\" {initiator} says, lowering their voice conspiratorially.",
            "\"I've been wanting to share this with someone, {target}, and I couldn't think of a better person to tell. Our neighbors have quite the scandal going on,\" {initiator} says, unable to suppress their excitement."
        ]
    },
    "mixer_social_GushAboutPartner_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} gushes about their partner to {target}."
        ],
        "actions": [
            "\"{target}, I can't contain my excitement any longer. I have to tell you about my amazing romantic partner,\" {initiator} says, beaming with joy.",
            "\"You won't believe how lucky I am, {target}. I have found the most incredible person to share my life with,\" {initiator} says, unable to hide their enthusiasm.",
            "\"I have to share this with someone, and you're the first person who comes to mind. {target}, let me tell you about the love of my life,\" {initiator} says, unable to contain their happiness.",
            "\"I've been bursting at the seams to tell you about my partner, {target}. They are absolutely incredible, and I can't help but gush about them,\" {initiator} says, their eyes shining with adoration.",
            "\"{target}, I have to tell you about the person who has stolen my heart. They are the most amazing human being I have ever met,\" {initiator} says, a smile spreading across their face.",
            "\"I can't keep this to myself any longer, {target}. My partner is absolutely extraordinary, and I need to share all the wonderful things about them with you,\" {initiator} says, their voice filled with excitement.",
            "\"I have to tell you about my partner, {target}. They are the reason behind my constant smiles and overflowing happiness,\" {initiator} says, unable to contain their love.",
            "\"You know, {target}, my heart feels like it's going to burst because of this incredible person in my life. I have to tell you all about them,\" {initiator} says, their voice brimming with affection.",
            "\"{target}, I need to tell you about my partner, because they are the epitome of love and support. I am so fortunate to have them,\" {initiator} says, a sense of gratitude evident in their tone.",
            "\"I've been itching to share this with you, {target}. My partner is an absolute gem, and I can't help but shower them with praise,\" {initiator} says, their face glowing with happiness."
        ]
    },
    "mixer_social_HeckleMicrophonePerformance_alwaysOn": {
        "pre_actions": [
            "{initiator} heckles {target}, who is performing with a microphone."
        ],
        "actions": [
            "\"{target}, is that really the best you've got? I've seen better performances at a talent show,\" {initiator} jeers, smirking.",
            "\"Hey {target}, maybe you should stick to your day job. This crowd doesn't seem too impressed,\" {initiator} taunts, crossing their arms.",
            "\"{target}, I hate to break it to you, but your performance is like nails on a chalkboard. Do us all a favor and spare our ears,\" {initiator} mocks, laughing mockingly.",
            "\"Is this supposed to be a comedy act, {target}? Because you're definitely making me laugh... for all the wrong reasons,\" {initiator} teases, shaking their head in disbelief.",
            "\"Wow, {target}, I didn't realize they allowed tone-deaf performers on stage. Maybe you should consider a different career path,\" {initiator} jeers, rolling their eyes.",
            "\"{target}, I hope you're not planning on quitting your day job to pursue a career in entertainment. Trust me, it's not going to work out,\" {initiator} mocks, unable to contain their laughter.",
            "\"Is this a joke, {target}? Because I don't think I've ever heard anything so off-key in my life. Stick to lip-syncing next time,\" {initiator} teases, smirking.",
            "\"{target}, the only thing worse than your singing is your stage presence. You might want to take some lessons before attempting this again,\" {initiator} taunts, raising an eyebrow.",
            "\"Sorry to burst your bubble, {target}, but your performance is more cringe-worthy than entertaining. Maybe it's time to find a different hobby,\" {initiator} mocks, shaking their head.",
            "\"Hey {target}, I hope you're not expecting a standing ovation because I think you'll be lucky if anyone claps at all. Just being honest,\" {initiator} jeers, crossing their arms."
        ]
    },
    "mixer_social_HotTub_Splash_targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} playfully splashes {target} in the hot tub."
        ],
        "actions": [
            "\"{target}, you better watch out!\" {initiator} warns mischievously, before splashing {target} in the hot tub.",
            "Laughing uncontrollably, {initiator} splashes {target} in the hot tub, causing water to splash everywhere.",
            "With a mischievous grin, {initiator} playfully splashes {target} in the hot tub, their laughter echoing through the air.",
            "As {target} relaxes in the hot tub, {initiator} sneaks up and splashes them, laughing playfully.",
            "Feeling mischievous, {initiator} decides to splash {target} in the hot tub, their laughter filling the air.",
            "\"{target}, brace yourself!\" {initiator} exclaims, splashing {target} in the hot tub with a playful splash.",
            "With a playful glint in their eye, {initiator} splashes {target} in the hot tub, their laughter contagious.",
            "Unable to resist, {initiator} splashes {target} in the hot tub, their laughter bubbling up from within.",
            "{initiator} can't help themselves and splashes {target} in the hot tub, their laughter filling the air.",
            "As {target} closes their eyes and enjoys the warm water, {initiator} surprises them by splashing them playfully in the hot tub."
        ],
    },
    "mixer_social_ImpishlyPester_targeted_mean_emotionSpecific": {
        "pre_actions": [
            "{initiator} impishly pesters {target}."
        ],
        "actions": [
            "\"{target}, I bet you can't catch me!\" {initiator} taunts, darting away with a mischievous grin.",
            "\"Watch out, {target}! I've got some tricks up my sleeve just for you,\" {initiator} teases, winking playfully.",
            "\"{target}, have I ever mentioned how much fun it is to see you squirm when I pester you? You're just too easy to tease,\" {initiator} taunts, chuckling.",
            "\"Come on, {target}, let's see if you can handle my relentless teasing,\" {initiator} challenges, sticking their tongue out.",
            "\"{target}, you're so easy to tease. I can't resist the temptation,\" {initiator} admits, unable to hide their mischievous nature.",
            "\"I'm sorry, {target}, but I can't help but pester you. It's just too much fun,\" {initiator} says, feigning innocence.",
            "\"Prepare yourself, {target}, because I'm about to unleash a barrage of playful pestering on you,\" {initiator} warns with a mischievous glint in their eyes.",
            "\"Hey {target}, want to play a game? It's called 'How many times can I annoy you in under a minute?'\" {initiator} suggests, grinning mischievously.",
            "\"{target}, you know I can't resist teasing you. It's like a reflex,\" {initiator} confesses, a playful smirk on their face.",
            "\"Sorry in advance, {target}, but I just can't help myself. You're too easy to pester,\" {initiator} says, unable to suppress their mischievous side."
            "\"Hey {target}, guess what? I have a new plan to annoy you today. Brace yourself!\" {initiator} declares, excitement evident in their voice.",
        ]
    },
    "mixer_social_ImplyMotherIsLlama_targeted_mean_highScore": {
        "pre_actions": [
            "{initiator} implies to {target} that their mother is a llama in a mean-spirited joke."
        ],
        "actions": [
            "\"I never thought I'd have to say this to someone, but your mother is quite the unique individual, {target}. Let's just say she's got a special animalistic side,\" {initiator} hints, unable to contain their amusement.",
            "\"I've discovered something fascinating, {target}. It appears that your mother has a rather unique connection to the animal kingdom. Care to guess which animal?\" {initiator} taunts, enjoying the suspense.",
            "\"You know, {target}, I always wondered why your mother had such a distinctive presence. Now I know—it's because she's secretly a llama!\" {initiator} jokes with a sly grin, waiting for {target}'s reaction.",
            "\"I hope you're sitting down for this, {target}, but I recently stumbled upon some shocking information about your family. It seems your mother has a hidden talent for blending in with llamas!\" {initiator} says, struggling to keep a straight face.",
            "\"I never thought I'd be the bearer of such peculiar news, {target}, but it seems your mother has some unconventional origins. Let's just say she has a certain affinity for llamas,\" {initiator} suggests with a playful smirk.",
            "\"Here's a fun fact for you, {target}. Did you know that your mother has a distinct resemblance to a certain animal? It starts with an 'l' and ends with an 'a'...\" {initiator} hints, waiting to see {target}'s reaction.",
            "\"I hope your mother won't mind me sharing this, {target}, but I recently discovered an interesting similarity between her and llamas. It's almost as if they share a secret bond,\" {initiator} says, barely able to hold back their laughter.",
            "\"You have to promise not to be mad at me, {target}, but I couldn't keep this to myself any longer. I've learned that your mother and llamas have more in common than meets the eye,\" {initiator} teases, waiting for the truth to sink in."
        ]
    },
    "mixer_social_ImpressWithVideoGameProwess_targeted_romance_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} tries to impress {target} with their video game prowess."
        ],
        "actions": [
            "\"{target}, prepare to witness the gaming skills of a true champion,\" {initiator} boasts, with a smirk on their face.",
            "\"You think you're good at video games, {target}? Let me show you what true talent looks like,\" {initiator} challenges, cracking their knuckles.",
            "\"I've been honing my gaming skills for years, {target}, and now it's time to put them to the test. Brace yourself,\" {initiator} says confidently.",
            "\"Prepare to be amazed, {target}, as I take you on a journey through the virtual world and show you what I'm made of,\" {initiator} declares, with a twinkle of excitement in their eyes.",
            "\"I hope you're ready for a lesson in excellence, {target}, because I'm about to blow your mind with my gaming prowess,\" {initiator} says, a hint of competitiveness in their voice.",
            "\"I've spent countless hours perfecting my gaming abilities, {target}, and now it's time to demonstrate what I'm capable of. Hold on tight,\" {initiator} says, with a smirk of determination.",
            "\"Get ready to witness gaming greatness, {target}, as I dominate the virtual realm like no one else can,\" {initiator} boasts, flexing their fingers in preparation.",
            "\"I'm about to show you a gaming experience like no other, {target}. Get ready to be dazzled by my skills,\" {initiator} says, a touch of excitement in their voice.",
            "\"{target}, prepare yourself for an epic display of gaming expertise. You're about to witness something truly remarkable,\" {initiator} says, with a confident grin.",
            "\"Let's see if you can keep up, {target}. Get ready for a gaming session that will leave you in awe,\" {initiator} challenges, adjusting their gaming headset."
        ]
    },
    "mixer_social_InstillWithFalseConfidence_targeted_mischief_skills": {
        "pre_actions": [
            "{initiator} sarcastically instills false confidence in {target}."
        ],
        "actions": [
            "\"Oh, don't worry {target}, you're definitely the most talented person I know,\" {initiator} says with a smirk, dripping with sarcasm.",
            "\"Of course you can handle it, {target}. I have complete faith in your abilities,\" {initiator} says, their tone laced with sarcasm.",
            "\"You're absolutely right, {target}, there's no way you could mess this up. You're practically perfect,\" {initiator} says, rolling their eyes.",
            "\"Wow, {target}, I'm so impressed by your skills. I can't wait to see how this turns out,\" {initiator} says sarcastically, unable to hide their skepticism.",
            "\"Don't worry, {target}, I'm sure everything will go perfectly. I mean, what could possibly go wrong?\" {initiator} says, their voice dripping with sarcasm.",
            "\"Oh, I have complete confidence in you, {target}. I'm sure you'll do an amazing job,\" {initiator} says, their tone filled with sarcasm.",
            "\"Sure, {target}, you've got this. I have no doubt that you'll succeed,\" {initiator} says sarcastically, unable to hide their disbelief.",
            "\"I have no doubt that you're going to nail it, {target}. You're just so incredibly talented,\" {initiator} says, their tone overflowing with sarcasm.",
            "\"That's a fantastic idea, {target}. I can't believe I didn't think of it myself,\" {initiator} says sarcastically, unable to hide their amusement.",
            "\"You're absolutely right, {target}. I can't think of anyone more qualified for the job than you,\" {initiator} says, their voice oozing with sarcasm."
        ]
    },
    "mixer_social_InsultHouse_targeted_mean_alwaysOn_neighbor": {
        "pre_actions": [
            "{initiator} harshly insults {target}'s house."
        ],
        "actions": [
            "\"{target}, I can't believe you actually live in this dump,\" {initiator} says with a sneer.",
            "\"Is this seriously where you call home, {target}? It's a disgrace,\" {initiator} scoffs.",
            "\"Wow, {target}, your house is a complete mess. Do you even know what cleaning is?\" {initiator} says disdainfully.",
            "\"I never knew someone could have such terrible taste in decor, {target}. Your house is an eyesore,\" {initiator} says, wrinkling their nose.",
            "\"Your house is a dump, {target}. I can't believe you actually invite people over,\" {initiator} says, shaking their head in disbelief.",
            "\"{target}, your house is so run-down and pathetic. I can't believe you actually live here,\" {initiator} says, unable to hide their disgust.",
            "\"Did a tornado hit your house, {target}? It looks like a disaster zone,\" {initiator} says, laughing mockingly.",
            "\"{target}, I have to be honest, your house is the ugliest one I've ever seen. It's embarrassing,\" {initiator} says, unable to hold back their criticism.",
            "\"I can't believe you have the audacity to call this place a home, {target}. It's more like a dump,\" {initiator} says, shaking their head in disbelief.",
            "\"{target}, your house is an absolute nightmare. I can't believe anyone would willingly choose to live here,\" {initiator} says, struggling to hide their disdain."
        ]
    },
    "mixer_social_InsultYard_targeted_mean_alwaysOn_neighbor": {
        "pre_actions": [
            "{initiator} harshly insults {target}\'s yard."
        ],
        "actions": [
            "\"{target}, I can't help but notice how unkempt your yard is. It's really an eyesore,\" {initiator} says, unable to hold back their disdain.",
            "\"Wow, {target}, your yard looks like a complete disaster. Have you ever considered taking care of it?\" {initiator} remarks, with a mocking tone.",
            "\"I hate to say it, {target}, but your yard is a mess. It's like you don't even care about the appearance of your home,\" {initiator} comments, unable to hide their disgust.",
            "\"Seriously, {target}, what happened to your yard? It looks like a jungle out there. You should really do something about it,\" {initiator} says, with a hint of sarcasm.",
            "\"{target}, I can't believe how neglected your yard is. It's such a shame,\" {initiator} remarks, shaking their head in disapproval.",
            "\"Your yard is a complete disaster, {target}. It's no wonder the neighbors complain about it,\" {initiator} says, clearly unimpressed.",
            "\"{target}, I have to be honest, your yard is an absolute mess. I didn't expect this from you,\" {initiator} comments, raising an eyebrow in surprise.",
            "\"Is there a reason why you haven't taken care of your yard, {target}? It's really not a good look,\" {initiator} says, sounding judgmental.",
            "\"I hate to say it, {target}, but your yard is an embarrassment. You should really do something about it,\" {initiator} remarks, unable to hide their disappointment.",
            "\"{target}, I never thought I'd see a yard in such a terrible state. It's clear you don't put any effort into maintaining it,\" {initiator} says, shaking their head in disbelief."
        ]
    },
    "mixer_social_InviteToFakeParty_targeted_mischief_alwaysOn": {
        "pre_actions": [
            "{initiator} vindictively invites {target} to a fake party."
        ],
        "actions": [
            "\"{target}, I've been meaning to invite you to this amazing party I'm throwing. It's going to be the event of the year,\" {initiator} says, a mischievous glint in their eyes.",
            "\"I've been planning this epic party, {target}, and I can't think of anyone better to invite. It's going to be legendary,\" {initiator} says, trying to contain their excitement.",
            "\"You know, {target}, there's this incredible party happening soon. I think you'd have a blast if you came,\" {initiator} suggests, a sly smile playing on their lips.",
            "\"I've got this exclusive invitation for you, {target}. It's for a party that you absolutely cannot miss,\" {initiator} says, unable to hide their smirk.",
            "\"Guess what, {target}? You're officially invited to this mind-blowing party I'm hosting. It's going to be off the charts,\" {initiator} says, barely able to contain their glee.",
            "\"I've been keeping this under wraps, but I want you to be part of this extravagant party I'm organizing. It's going to be legendary,\" {initiator} says, their voice filled with anticipation.",
            "\"I have a surprise for you, {target}. Get ready for the party of a lifetime. You won't believe what I have planned,\" {initiator} says, their eyes sparkling with mischief.",
            "\"You're in luck, {target}. I'm throwing this incredible party, and I want you to be there. It's going to be unforgettable,\" {initiator} says, a devious grin on their face.",
            "\"I've got this incredible event coming up, {target}, and I want you to be part of it. Trust me, you won't regret it,\" {initiator} says, their excitement bubbling over.",
            "\"I've been plotting something special, and you're going to love it, {target}. Brace yourself for the party of a lifetime,\" {initiator} says, their voice filled with anticipation."
        ]
    },
    "mixer_social_LendEmotionalSupportNEW_targeted_Friendly_alwaysOn_trait": {
        "pre_actions": [
            "{initiator} lends emotional support to {target}."
        ],
        "actions": [
            "\"{target}, I can see that you're going through a tough time. I want you to know that I'm here for you,\" {initiator} says, offering a comforting smile.",
            "\"I know things have been hard lately, {target}, but I want you to know that you don't have to face them alone. I'm here to lend you my support,\" {initiator} says, placing a comforting hand on {target}'s shoulder.",
            "\"I may not have all the answers, {target}, but I can offer you my unwavering support. Whatever you're going through, we'll face it together,\" {initiator} reassures {target}.",
            "\"{target}, I can see that you're hurting. Please remember that I'm here for you, ready to offer my support in any way I can,\" {initiator} says sincerely.",
            "\"I may not understand exactly what you're going through, {target}, but I want you to know that I care about you deeply. Lean on me for support whenever you need it,\" {initiator} says, reaching out to {target}.",
            "\"{target}, you're not alone in this. I'm here to listen, to comfort, and to provide the support you need. Lean on me, my friend,\" {initiator} says, offering a reassuring smile.",
            "\"{target}, I want you to know that you're not alone in this struggle. I'm here to support you, no matter what,\" {initiator} says, looking {target} in the eyes.",
            "\"{target}, I know it feels overwhelming right now, but I want you to know that I'm here for you. Lean on me, and together we'll find a way through,\" {initiator} says, offering a comforting presence.",
            "\"{target}, you're going through a difficult time, and I want to be there for you. Please know that you can lean on me for support, no matter what,\" {initiator} says, emphasizing their willingness to help.",
            "\"{target}, I may not have all the answers, but I can offer you my support and a listening ear. You don't have to face this alone,\" {initiator} says, sincerely wanting to help."
        ]
    },
    "mixer_social_MakeAFlirtatiousJoke_targeted_romance_emotionSpecific": {
        "pre_actions": [
            "{initiator} makes a flirtatious joke to {target}."
        ],
        "actions": [
            "\"{target}, you must be made of copper and tellurium because you're Cu-Te!\" {initiator} says with a playful wink.",
            "\"Hey {target}, are you a magician? Because whenever I look at you, everyone else disappears,\" {initiator} says, flashing a charming smile.",
            "\"Is your name Google? Because you have everything I've been searching for,\" {initiator} says, their eyes sparkling with mischief.",
            "\"{target}, if you were a vegetable, you'd be a cute-cumber,\" {initiator} says, laughing at their own cheesy joke.",
            "\"Are you a parking ticket? Because you've got 'Fine' written all over you,\" {initiator} says, playfully nudging {target}.",
            "\"Excuse me, {target}, but do you have a name? Or can I call you mine?\" {initiator} says, raising an eyebrow suggestively.",
            "\"{target}, if you were a song, you'd be the catchy tune that's stuck in my head all day,\" {initiator} says, leaning in closer with a mischievous grin.",
            "\"Is your dad a baker? Because you're a cutie pie,\" {initiator} says, their voice laced with humor.",
            "\"{target}, do you believe in love at first sight, or should I walk by again?\" {initiator} says with a smirk, pretending to stroll away.",
            "\"Excuse me, {target}, but I think you dropped something: my jaw,\" {initiator} says, their eyes sparkling with flirtation."
        ]
    },
    "mixer_social_MockOutfit_targeted_Mean_middleScore": {
        "pre_actions": [
            "{initiator} mocks {target}'s outfit."
        ],
        "actions": [
            "\"{target}, I have to say, your fashion sense is...unique,\" {initiator} says, smirking.",
            "\"Wow, {target}, did you pick that outfit straight out of a '80s costume party?\" {initiator} teases, unable to hide a smile.",
            "\"Okay, {target}, I have to ask, did a clown dress you this morning?\" {initiator} jokes, trying not to laugh.",
            "\"I'm sorry, {target}, but I can't help but laugh at your outfit. Did you lose a bet or something?\" {initiator} chuckles, unable to contain their amusement.",
            "\"Hey {target}, I hate to break it to you, but I think you missed the mark with your outfit choice today,\" {initiator} teases playfully.",
            "\"Whoa, {target}, you really went all out with that outfit. Is it the latest trend or did you just raid a thrift store?\" {initiator} mocks, grinning mischievously.",
            "\"I have to say, {target}, your fashion sense is...interesting. Did you pick that out yourself or did your mom help?\" {initiator} teases, trying to stifle their laughter.",
            "\"{target}, I hate to say it, but your outfit is a little...questionable,\" {initiator} jests, raising an eyebrow.",
            "\"Nice outfit, {target}. Did you borrow it from a scarecrow?\" {initiator} jokes, smirking at their own cleverness.",
            "\"{target}, I hope you don't mind me saying, but your outfit is definitely...eye-catching,\" {initiator} says, struggling to keep a straight face."
        ]
    },
    "mixer_social_OfferFriendlyMassage_targeted_Friendly_MiddleScore": {
        "pre_actions": [
            "{initiator} offers a friendly massage to {target}."
        ],
        "actions": [
            "\"Hey {target}, I've been practicing my massage skills and I thought you might enjoy a little relaxation,\" {initiator} says with a smile.",
            "\"I noticed you've been stressed lately, {target}, so I thought I could give you a nice massage to help you unwind,\" {initiator} suggests kindly.",
            "\"{target}, I know how much you love massages, so I thought I could give you a little treat. What do you say?\" {initiator} asks, eager to help.",
            "\"I've been learning some massage techniques, and I thought I could give you a sample. How about it, {target}?\" {initiator} offers, hoping they'll accept.",
            "\"Hey {target}, I recently learned a few massage techniques and I thought I could practice on you. What do you think?\" {initiator} proposes, a bit unsure.",
            "\"{target}, I've been working on my massage skills and I thought it would be nice to offer you a relaxing session. Interested?\" {initiator} suggests, feeling a little nervous.",
            "\"I've been studying the art of massage, {target}, and I thought I could give you a little demonstration. Would you be up for it?\" {initiator} asks, hoping for a positive response.",
            "\"{target}, I've been practicing my massage techniques and I feel confident enough to offer you a session. How does that sound?\" {initiator} offers, hoping they'll agree.",
            "\"I know you've had a long day, {target}, so I thought I could give you a soothing massage. What do you think?\" {initiator} asks, hoping to provide some comfort.",
            "\"{target}, I've been learning some massage techniques and I thought I could give you a relaxing treat. Are you up for it?\" {initiator} suggests, eager to help."
        ]
    },
    # "mixer_social_OfferToFeelBaby_Invite_targeted_Friendly_alwaysOn_Pregnancy": {
    # "pre_actions": [
    # "{initiator} offers to feel {target}'s baby."
    # ],
    # },
    # "mixer_social_OfferToFeelBaby_targeted_Friendly_alwaysOn_Pregnancy": {
    # "pre_actions": [
    # "{initiator} offers to feel {target}'s baby."
    # ],
    # },
    "mixer_social_PlantSeedsOfDoubt_targeted_mischief_alwaysOn_trait": {
        "pre_actions": [
            "{initiator} tries to plant seeds of doubt in {target}'s mind."
        ],
        "actions": [
            "\"{target}, have you ever wondered if things are really as they seem? I mean, what if there's more to the story?\" {initiator} asks, looking thoughtful.",
            "\"You know, {target}, sometimes people are not who they portray themselves to be. It makes you question everything, doesn't it?\" {initiator} says, raising an eyebrow.",
            "\"I've been noticing some strange behavior lately, {target}, and it's making me question whether we can truly trust those around us,\" {initiator} says, voice filled with doubt.",
            "\"Do you ever get the feeling that someone close to us might be hiding something? I can't shake this nagging suspicion, {target},\" {initiator} says, looking concerned.",
            "\"I've been doing some digging, {target}, and I've stumbled upon some unsettling information. It's making me doubt everything I thought I knew,\" {initiator} says, voice filled with uncertainty.",
            "\"{target}, I can't help but feel that something is off. Call it intuition, but I think we need to be cautious and question the motives of those around us,\" {initiator} says, eyes narrowing.",
            "\"I've been hearing some rumors lately, {target}, and I can't help but wonder if there's any truth to them. It's making me question everything,\" {initiator} says, voice tinged with suspicion.",
            "\"You know, {target}, trust is a fragile thing. It's important to question and verify, especially when there are doubts lingering in the air,\" {initiator} says, looking contemplative.",
            "\"I've been reading a lot about deception and manipulation, {target}, and it's making me question whether we can truly rely on others. What do you think?\" {initiator} asks, searching {target}'s face for a reaction.",
            "\"Sometimes, {target}, the people we least suspect turn out to be the ones hiding the biggest secrets. It's enough to make you doubt everyone around you,\" {initiator} says, voice filled with skepticism."
        ]
    },
    "mixer_social_PraisePianoSonatas_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} praises {target}'s piano sonatas."
        ],
        "actions": [
            "\"{target}, your piano sonatas are absolutely breathtaking. I am in awe of your talent,\" {initiator} exclaims with genuine admiration.",
            "\"I have to say, {target}, your piano sonatas are some of the most beautiful pieces of music I have ever heard,\" {initiator} says, unable to contain their excitement.",
            "\"{target}, I've been listening to your piano sonatas, and I must say, they are truly magnificent. You have an incredible gift,\" {initiator} compliments with a smile.",
            "\"I can't help but be captivated by your piano sonatas, {target}. They have such emotion and depth, it's truly remarkable,\" {initiator} says, genuinely impressed.",
            "\"{target}, your piano sonatas are like poetry in motion. The way you play is absolutely mesmerizing,\" {initiator} praises, their eyes filled with admiration.",
            "\"I have been listening to your piano sonatas on repeat, {target}, and every time, I am blown away by your talent. You are truly gifted,\" {initiator} gushes with enthusiasm.",
            "\"{target}, your piano sonatas have touched my soul. The way you play evokes such raw emotion, it's truly something special,\" {initiator} says, deeply moved.",
            "\"I can't get enough of your piano sonatas, {target}. They have become the soundtrack to my life. Your talent is exceptional,\" {initiator} confesses, their voice filled with awe.",
            "\"{target}, your piano sonatas have a certain magic to them. They transport me to another world every time I listen. You are an incredible musician,\" {initiator} praises with a smile.",
            "\"{target}, your piano sonatas are a masterpiece. I am in awe of your skill and the beauty you bring to the world through your music,\" {initiator} says, their voice filled with admiration."
        ]
    },

    "mixer_social_PretendToBeSlapped_targeted_mischief_skills": {
        "pre_actions": [
            "{initiator} pretends to be slapped by {target}."
        ],
        "actions": [
            "\"{target}, how could you? I thought we were friends!\" {initiator} exclaims, holding their cheek in mock pain.",
            "\"Ouch! That really hurt, {target}. I can't believe you slapped me!\" {initiator} says, pretending to be shocked.",
            "\"Oh no, {target}! Why did you slap me? What did I do to deserve that?\" {initiator} asks, feigning sadness.",
            "\"Wow, {target}, I didn't realize you had such a strong right hook. That slap really caught me off guard!\" {initiator} says, pretending to recover from the fake slap.",
            "\"{target}, I can't believe you just slapped me. That's crossing a line, even for you!\" {initiator} says, pretending to be angry.",
            "\"Ouch! {target}, that was uncalled for. I can't believe you actually slapped me!\" {initiator} says, rubbing their cheek dramatically.",
            "\"{target}, that's it! I'm done with you. I can't believe you slapped me like that. We're finished!\" {initiator} declares, pretending to be hurt and angry.",
            "\"Did you really just slap me, {target}? After everything we've been through? I never thought you would stoop so low,\" {initiator} says, pretending to be disappointed.",
            "\"{target}, I trusted you, and you slapped me. I can't believe I let you into my life,\" {initiator} says, pretending to be betrayed.",
            "\"Okay, {target}, you got me. Pretending to slap me was a good one. But let's not turn it into a real fight!\" {initiator} says, chuckling and pretending to play along."
        ]
    },
    "mixer_social_PromisetoDedicateSong_targeted_romance_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} promises to dedicate a song to {target}."
        ],
        "actions": [
            "\"{target}, there's a song that perfectly captures how I feel about you. I promise to dedicate it to you,\" {initiator} says with a smile.",
            "\"I've been searching for the right words to express my feelings for you, {target}, and I think I found them in a song. Get ready for a special dedication,\" {initiator} says playfully.",
            "\"I want to dedicate a song to you, {target}, as a way to show you how much you mean to me,\" {initiator} says, looking into {target}'s eyes.",
            "\"{target}, whenever I hear this song, it reminds me of you. So, I promise to dedicate it to you,\" {initiator} says with a hint of excitement.",
            "\"There's a song that perfectly captures the way I feel about you, {target}. Brace yourself for a heartfelt dedication,\" {initiator} says, their voice filled with affection.",
            "\"{target}, I've been looking for a way to express my love for you, and I believe dedicating a song is the perfect way. Get ready for a beautiful dedication,\" {initiator} says, a touch of nervousness in their voice.",
            "\"I want you to know how special you are to me, {target}, and I think dedicating a song to you is the best way to do it,\" {initiator} says with a genuine smile.",
            "\"I've been listening to this song on repeat, {target}, and it made me realize how much it reminds me of you. So, I promise to dedicate it to you,\" {initiator} says, their voice filled with warmth.",
            "\"I've been holding on to this song for you, {target}, waiting for the perfect moment to dedicate it. Well, that moment is now,\" {initiator} says, excitement creeping into their voice.",
            "\"{target}, there's a song that captures the essence of our connection. Get ready for a heartfelt dedication,\" {initiator} says, their eyes sparkling with anticipation."
        ]
    },

    "mixer_social_Propose_targeted_romance_relationship": {
        "pre_actions": [
            "{initiator} proposes to {target}."
        ],
        "actions": [
            "\"{target}, I've been thinking a lot about our future together, and I can't imagine my life without you. Will you marry me?\" {initiator} says, getting down on one knee.",
            "\"I've been planning this moment for so long, {target}, and I can't hold it in any longer. Will you do me the honor of being my spouse?\" {initiator} says, nervously holding out a ring.",
            "\"I love you more than anything in this world, {target}, and I want to spend the rest of my life with you. Will you marry me?\" {initiator} asks, their heart pounding.",
            "\"{target}, you bring so much joy and love into my life. I can't imagine a future without you. Will you make me the happiest person alive and marry me?\" {initiator} says, with tears of happiness in their eyes.",
            "\"I've thought about this moment countless times, {target}, and I can't wait any longer. Will you marry me and make all my dreams come true?\" {initiator} says, holding out a ring box.",
            "\"Every time I look at you, {target}, I am reminded of how lucky I am to have you in my life. Will you do me the incredible honor of becoming my spouse?\" {initiator} asks, their voice filled with love and devotion.",
            "\"{target}, you are my everything. I want to spend the rest of my days by your side. Will you marry me and make me the happiest person alive?\" {initiator} says, their eyes sparkling with anticipation.",
            "\"I've never been more sure of anything in my life, {target}. You are the one I want to spend forever with. Will you marry me and make me the luckiest person in the world?\" {initiator} asks, their voice trembling with excitement.",
            "\"{target}, my love for you knows no bounds. Will you make me the happiest person on earth and marry me?\" {initiator} says, their voice filled with hope and adoration.",
            "\"{target}, life is an incredible journey, and I want to walk it hand in hand with you. Will you marry me and embark on this adventure together?\" {initiator} asks, their heart full of love."
        ]
    },
    "mixer_social_ProposeCrazyScheme_targeted_friendly_emotionSpecific": {
        # J: Having issue where {target}'s name does not pop up
        "pre_actions": [
            "{initiator} proposes a crazy scheme to {target}."
        ],
        "actions": [
            "\"{target}, I have this wild idea that just might work. Hear me out,\" {initiator} says with a mischievous grin.",
            "\"You know, {target}, I've been thinking...what if we did something completely insane? Something no one would expect,\" {initiator} suggests, excitement evident in their voice.",
            "\"I know this might sound crazy, {target}, but what if we embark on an adventure that will change our lives forever?\" {initiator} proposes, their eyes gleaming with anticipation.",
            "\"I have this outrageous plan, {target}, and I can't think of anyone better to join me in making it a reality. Are you up for it?\" {initiator} asks, their voice filled with enthusiasm.",
            "\"I've been dreaming about this wild scheme for a while now, {target}, and I need your help to make it happen. Are you willing to take a leap of faith with me?\" {initiator} asks, a hint of nervousness in their tone.",
            "\"I've come up with this crazy idea, {target}, and I can't shake the feeling that it's meant to be. Will you trust me and give it a shot?\" {initiator} asks, their eyes pleading for {target}'s approval.",
            "\"Imagine this, {target}: a once-in-a-lifetime opportunity to do something completely outrageous. Are you brave enough to seize it with me?\" {initiator} challenges, a spark of adventure igniting in their eyes.",
            "\"{target}, I know it sounds insane, but I truly believe this scheme could change our lives forever. Will you be daring enough to join me?\" {initiator} asks, a mix of hope and uncertainty in their voice.",
            "\"I've been brainstorming this wild plan, {target}, and I can't keep it to myself any longer. Will you be my partner in crime and help me bring it to life?\" {initiator} asks, eagerly awaiting {target}'s response.",
            "\"{target}, I have this outrageous idea that defies all logic and reason. But sometimes, the most extraordinary things happen when we step outside our comfort zones. Will you take the leap with me?\" {initiator} asks, their excitement contagious."
        ]
    },
    "mixer_social_PumpUp_targeted_friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} attempts to boost {target}'s confidence."
        ],
        "actions": [
            "\"You know, {target}, you are truly amazing. I hope you realize just how special you are,\" {initiator} says, with a genuine smile on their face.",
            "\"I have always admired your strength and resilience, {target}. You inspire me every day,\" {initiator} says, their voice filled with admiration.",
            "\"You might not see it, {target}, but you have so much potential. Don't be afraid to go after your dreams,\" {initiator} encourages, placing a comforting hand on {target}'s shoulder.",
            "\"I believe in you, {target}. You have all the skills and talent to achieve greatness. Just trust yourself,\" {initiator} says, looking {target} directly in the eyes.",
            "\"No matter what challenges come your way, {target}, remember that you are capable of overcoming them. You are stronger than you think,\" {initiator} reassures, their voice filled with conviction.",
            "\"Sometimes, all it takes is a little confidence to unlock your true potential, {target}. Believe in yourself and watch what you can achieve,\" {initiator} says, offering a reassuring smile.",
            "\"I've seen you handle difficult situations with grace and poise, {target}. You have a natural ability to rise above any obstacle that comes your way,\" {initiator} compliments, genuinely impressed.",
            "\"You have a unique gift, {target}, and the world needs to see it. Don't hold back; let your light shine,\" {initiator} urges, a spark of excitement in their eyes.",
            "\"Your presence alone radiates confidence, {target}. You have a way of making everyone around you feel empowered,\" {initiator} says, acknowledging {target}'s natural charisma.",
            "\"You might not see it yet, {target}, but you have so much to offer. Don't let self-doubt hold you back from reaching your full potential,\" {initiator} advises, speaking from the heart."
        ]
    },
    "mixer_social_QuestionCostume_Targeted_Mean": {
        "pre_actions": [
            "{initiator} rudely questions {target}'s costume."
        ],
        "actions": [
            "\"{target}, what on earth are you wearing? Did you raid a thrift store or something?\" {initiator} asks, raising an eyebrow.",
            "\"Seriously, {target}? Is that supposed to be a costume? It looks like you put it together in five minutes,\" {initiator} scoffs.",
            "\"Um, {target}, I hate to break it to you, but your costume is a total disaster. Did you even try?\" {initiator} says, unable to hide their disdain.",
            "\"Is that really the best you could come up with, {target}? I've seen better costumes at a grade school Halloween party,\" {initiator} mocks.",
            "\"{target}, I have to ask, what were you thinking with that costume? It's just...wow,\" {initiator} says, struggling to find the right words.",
            "\"Sorry, {target}, but your costume is just plain embarrassing. You might want to rethink your choices next time,\" {initiator} says bluntly.",
            "\"I hate to be the bearer of bad news, {target}, but your costume is kind of a joke. Are you trying to be funny or something?\" {initiator} teases.",
            "\"{target}, I don't mean to be rude, but your costume is seriously lacking. Did you even put any effort into it?\" {initiator} questions, unimpressed.",
            "\"I hate to burst your bubble, {target}, but your costume is a total flop. I can't believe you thought it would actually look good,\" {initiator} remarks.",
            "\"Wow, {target}, just...wow. I can't even begin to comprehend what you were going for with that costume,\" {initiator} says, struggling to hide their amusement."
        ]
    },
    "mixer_social_RantLogically_targeted_mean_emotionSpecific": {
        # come back to this one, what is the animation like for this?
        "pre_actions": [
            "{initiator} rants logically at {target}."
        ],
        "actions": [
            "\"I can't believe you would think that way, {target}! It's absolutely infuriating,\" {initiator} shouts, their face turning red with anger.",
            "\"You know what, {target}? You're completely clueless! Let me enlighten you with some facts,\" {initiator} says, seething with frustration.",
            "\"I've had enough of your ignorance, {target}! It's time someone set you straight,\" {initiator} declares, their voice filled with rage.",
        ],
    },
    "mixer_social_RearrangeKeysOnTheKeyboard_targeted_friendly_alwaysOn_prank": {
        "pre_actions": [
            "{initiator} rearranges the keys on {target}'s keyboard as a prank."
        ],
        "actions": [
            "{initiator} chuckles quietly to themselves as they carefully swap the keys on {target}'s keyboard.",
            "{initiator} chuckles mischievously and starts rearranging the keys on {target}'s keyboard.",
            "{initiator} can't help but giggle as they swap the positions of the keys on {target}'s keyboard.",
            "With a sly smile, {initiator} begins carefully rearranging the keys on {target}'s keyboard, plotting their prank.",
            "As {target} walks out, {initiator} glances around mischievously before swiftly rearranging the keys on {target}'s keyboard.",
            "{initiator} stifles a laugh as they start rearranging the keys on {target}'s keyboard, eager to see their reaction.",
            "With a mischievous glint in their eyes, {initiator} swiftly begins the task of rearranging the keys on {target}'s keyboard.",
            "{initiator} grins deviously as they start switching the positions of the keys on {target}'s keyboard, preparing for a prank.",
            "As mischief fills the air, {initiator} subtly rearranges the keys on {target}'s keyboard, trying to suppress a smile.",
        ],
    },
    "mixer_social_RememberCommonInterests_targeted_romance_lowScore": {
        "pre_actions": [
            "In an effort to rekindle their relationship, {initiator} attempts to remind {target} about their common interests."
        ],
        "actions": [
            "\"{target}, do you remember when we used to spend hours discussing our favorite books? I miss those conversations,\" {initiator} says wistfully.",
            "\"I stumbled upon this old photo album and it brought back memories of all the hiking trips we took together. We should do that again, {target},\" {initiator} suggests with a hopeful smile.",
            "\"I found this playlist we used to listen to on repeat. Let's give it a listen and reminisce about all the concerts we went to, {target},\" {initiator} suggests, handing over a pair of earphones.",
            "\"Do you remember the cooking class we took together? I've been experimenting with some new recipes lately. How about we have a cooking night, just like old times?\" {initiator} proposes, holding up a cookbook.",
            "\"{target}, I came across this board game we used to love playing. Let's have a game night and see if we still have the same competitive spirit,\" {initiator} suggests, placing the game on the table.",
            "\"I was cleaning out my closet and found these old art supplies. Let's have a painting session, {target}, just like we used to do when we first met,\" {initiator} suggests, holding up a paintbrush.",
            "\"{target}, I found this old journal where we used to write down our dreams and aspirations. Let's sit down and share our dreams with each other again,\" {initiator} suggests, opening the journal.",
            "\"I saw this movie poster and it instantly reminded me of all the movie nights we used to have. Let's have a movie marathon and relive those moments, {target},\" {initiator} suggests, handing over the poster.",
            "\"{target}, I found this photo of us at the beach. Remember how much we loved going on spontaneous road trips? Let's plan one together and make some new memories,\" {initiator} suggests, showing the photo.",
            "\"I've been organizing my old vinyl records and came across some of our favorite albums. How about we have a listening party, {target}, and let the music transport us back to those special moments?\" {initiator} suggests, holding up a record."
        ]
    },
    "mixer_social_RepayLoanLarge_targeted_Friendly_alwaysOn_Copy": {
        "pre_actions": [
            "{initiator} repays a large loan to {target}."
        ],
        "actions": [
            "\"{target}, I wanted to thank you for everything you've done for me. Here's the money I owe you,\" {initiator} says, handing over a stack of cash.",
            "\"I've been working tirelessly to repay this loan, {target}. Finally, it's done. Thank you for your trust and patience,\" {initiator} says, a sense of relief evident in their voice.",
            "\"I never thought I'd be able to repay this loan, but with determination and hard work, I did it. Thank you for believing in me, {target},\" {initiator} says, handing over the final payment.",
            "\"Here it is, {target}. The last installment. I can't express how grateful I am for your support and understanding,\" {initiator} says, a hint of emotion in their voice.",
            "\"I've been saving every penny to repay this loan, {target}. It's been a long journey, but I'm proud to say it's finally over,\" {initiator} says, a smile of accomplishment on their face.",
            "\"{target}, I hope this payment shows how much your kindness and generosity means to me. Thank you for everything,\" {initiator} says, handing over a check with a grateful look.",
            "\"I've been planning this moment for so long, {target}. Here's the money I borrowed, plus interest. Consider it a small token of my gratitude,\" {initiator} says, handing over a neatly wrapped envelope.",
            "\"I've kept track of every penny, every sacrifice made to repay this loan, {target}. I hope this final payment brings us both closure,\" {initiator} says, handing over a money order.",
            "\"I never thought I'd be able to repay this loan, but with your support and encouragement, {target}, I managed to do it. Thank you,\" {initiator} says, a sense of accomplishment in their voice.",
            "\"Here's the money I owe you, {target}. I can't express how relieved I am to finally be debt-free. You've made a huge difference in my life,\" {initiator} says sincerely."
        ]
    },
    "mixer_social_RepayLoanLargeAndSmall_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} repays both large and small loans to {target}."
        ],
        "actions": [
            "\"{target}, I want to thank you for your support and belief in me. Today, I am finally able to repay all of my loans,\" {initiator} says with a grateful smile.",
            "\"I never thought this day would come, but here I am, ready to give back what I owe you,\" {initiator} says, holding a stack of envelopes containing the repayment.",
            "\"{target}, you've been there for me during my toughest times, and now I can finally show my gratitude by repaying all the loans,\" {initiator} says, handing over the money with a sense of relief.",
            "\"I've worked hard to gather the funds, and now it's time to repay you. Thank you for believing in me,\" {initiator} says, placing the stack of money before {target}.",
            "\"{target}, I hope this repayment reflects my appreciation for your trust in me. I couldn't have done it without your support,\" {initiator} says sincerely, handing over the money.",
            "\"It's been a long journey, but I'm proud to say that I can finally repay all the loans. Thank you for your patience,\" {initiator} says, their voice filled with relief.",
            "\"{target}, I've always admired your generosity, and now I can finally return the favor. Here's the repayment for all the loans,\" {initiator} says, handing over the money.",
            "\"I've been looking forward to this moment for so long. It's finally time to repay you, {target}, for all your kindness,\" {initiator} says, a mix of excitement and gratitude in their voice.",
            "\"It's not just about the money, {target}, it's about showing my gratitude. Thank you for everything, and here's the repayment,\" {initiator} says, handing over the money with a heartfelt smile.",
            "\"{target}, words can't express how thankful I am for your support. But I hope this repayment can show you how much it means to me,\" {initiator} says, handing over the money with a sense of fulfillment."
        ]
    },
    "mixer_social_RepayLoanSmall_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} repays a small loan to {target}."
        ],
        "actions": [
            "\"{target}, I wanted to thank you for your kindness. Here's the money I borrowed from you,\" {initiator} says, handing over the cash.",
            "\"I've been saving up, and now I can finally repay you, {target}. You've been so patient,\" {initiator} says with a grateful smile.",
            "\"I didn't forget about the loan, {target}. Here's the money I owe you,\" {initiator} says, handing over the cash with a sense of relief.",
            "\"I know it's been a while, but I finally have the money to repay you, {target}. Thank you for your trust,\" {initiator} says, handing over the cash with a sense of gratitude.",
            "\"I've been working extra hours just to pay you back, {target}. Here's the money I owe you,\" {initiator} says, handing over the cash with a hint of exhaustion in their voice.",
            "\"I've been feeling guilty about this loan for so long, {target}. I hope this repays at least a part of what I owe you,\" {initiator} says, handing over the cash with a tinge of guilt.",
            "\"I've been thinking about this loan every day, {target}, and I'm relieved to finally be able to give you the money back,\" {initiator} says, handing over the cash with a sense of closure.",
            "\"I've never forgotten the debt, {target}, and I've been saving up to repay you. Here's the money,\" {initiator} says, handing over the cash with a hint of determination in their voice.",
            "\"I hope this shows how much I appreciate your help, {target}. Here's the money I borrowed from you,\" {initiator} says, handing over the cash with genuine gratitude.",
            "\"I've been waiting for the right moment to repay you, {target}, and I believe that moment is now. Thank you for your patience,\" {initiator} says, handing over the cash with a sense of fulfillment."
        ]
    },
    "mixer_social_Sabotage_targeted_mischief_alwaysOn_trait": {
        "pre_actions": [
            "{initiator} attempts to sabotage {target}."
        ],
        "actions": [
            "\"Hey {target}, I hope you're ready for a little surprise,\" {initiator} says with a sly grin.",
            "\"I've been plotting something, {target}, and tonight is the night it all comes together,\" {initiator} says, eyes gleaming with mischief.",
            "\"You've always been one step ahead of me, {target}, but not this time. Get ready for a taste of your own medicine,\" {initiator} says, a devious glint in their eyes.",
            "\"I've had enough of playing nice, {target}. Brace yourself for a little sabotage,\" {initiator} says, a mischievous smirk spreading across their face.",
            "\"You thought you could outsmart me, {target}, but I've got a little surprise up my sleeve. Get ready for a rude awakening,\" {initiator} says, a hint of malice in their voice.",
            "\"Consider this a warning, {target}. I'm about to make your life a whole lot more interesting,\" {initiator} says with a wicked grin.",
            "\"I've been biding my time, {target}, waiting for the perfect moment to strike. Prepare to face the consequences of underestimating me,\" {initiator} says, a sinister glint in their eyes.",
            "\"You've pushed me too far, {target}, and now it's time for me to strike back. Get ready for a taste of my vengeance,\" {initiator} says, voice dripping with venom.",
            "\"I hope you're ready for a little chaos, {target}, because I'm about to shake up your world,\" {initiator} says, a wicked smile playing on their lips.",
            "\"You thought you could get away with everything, {target}, but I'm about to reveal your true colors. Say goodbye to your precious reputation,\" {initiator} says, a malicious glimmer in their eyes."
        ]
    },
    "mixer_social_Seduce_targeted_romance_emotionSpecific": {
        "pre_actions": [
            "{initiator} tries to seduce {target}."
        ],
        "actions": [
            "\"{target}, there's something I've been wanting to tell you... I find you incredibly attractive,\" {initiator} says, coyly.",
            "\"I can't help but be drawn to you, {target}. There's an undeniable chemistry between us,\" {initiator} says, their voice filled with longing.",
            "\"{target}, I've been thinking about you a lot lately, and I can't deny the strong desire I feel for you,\" {initiator} says, their eyes locked with {target}'s.",
            "\"I've been holding back these feelings for so long, {target}, but I can't resist any longer. I want you,\" {initiator} says, their voice filled with passion.",
            "\"{target}, I've been trying to fight it, but I can't deny the intense attraction I feel towards you,\" {initiator} admits, their voice trembling with desire.",
            "\"{target}, I hope you don't mind me being forward, but I can't help but fantasize about what it would be like to be with you,\" {initiator} says, their cheeks turning slightly red.",
            "\"I've been wanting to tell you this for a while now, {target}, but I can't hold it in any longer. I want to be more than just friends,\" {initiator} confesses, their heart racing.",
            "\"I've been keeping this to myself, {target}, but I can't deny the strong physical and emotional connection I feel towards you,\" {initiator} says, their voice filled with vulnerability.",
            "\"{target}, I hope I'm not crossing any boundaries here, but I can't ignore the way you make me feel. I want to explore this attraction between us,\" {initiator} says, nervously.",
            "\"{target}, there's something I need to get off my chest... I'm finding it hard to resist the temptation to kiss you right now,\" {initiator} says, their voice filled with anticipation."
        ]
    },
    "mixer_social_SellTestAnswers_targeted_Friendly_alwaysOn_prank": {
        "pre_actions": [
            "{initiator} sells fake test answers to {target} as a prank."
        ],
        "actions": [
            "\"{target}, I have something that might interest you. I've got the inside scoop on all the test answers,\" {initiator} says with a mischievous smirk.",
            "\"Hey, {target}, want to know a secret? I can guarantee you a perfect score on the upcoming test,\" {initiator} whispers slyly.",
            "\"I've got a little something that might give you an advantage on the test, {target},\" {initiator} says, raising an eyebrow.",
            "\"I've got a little surprise for you, {target}. It's the key to acing the test without even studying,\" {initiator} says, holding out a piece of paper with a mysterious smile.",
            "\"I've got something that might pique your interest, {target}. How about getting ahead of the curve with these fake test answers?\" {initiator} asks, smirking.",
            "\"Hey {target}, want a shortcut to acing the test? I've got the answers right here. What do you say?\" {initiator} says, holding up a piece of paper.",
            "\"You won't believe what I found. These are the secret answers to the upcoming test. Want to get your hands on them?\" {initiator} teases {target}.",
        ]
    },
    "mixer_Social_SexualOrientation_EndWooHooPartners": {
        "pre_actions": [
            "{initiator} ends their intimate relationship with {target} due to their sexual orientation."
        ],
        "actions": [
            "\"{target}, I need to talk to you. It's about our relationship,\" {initiator} says, a hint of sadness in their voice. ",
            "\"I can't keep pretending anymore, {target}. I have realized something about myself, and it's causing me so much pain,\" {initiator} confesses, their voice shaking.",
            "\"I never thought I would find myself in this situation, {target}, but I have to be true to who I am. Our relationship cannot continue,\" {initiator} says, tears welling up in their eyes.",
            "\"{target}, I can no longer hide the truth from you. It's tearing me apart, and I can't pretend anymore,\" {initiator} says, their voice choked with emotion.",
            "\"I've been struggling with this for so long, {target}, and I can't keep living a lie. I have to end our relationship,\" {initiator} admits, anguish clear in their voice. ",
            "\"Love is not enough to ignore my true self, {target}. I owe it to both of us to be honest,\" {initiator} says, their voice laced with pain.",
            "\"No matter how much I care about you, {target}, I can't deny who I really am. It's time to end our relationship,\" {initiator} says, their voice trembling.",
            "\"{target}, I never wanted to hurt you, but I can't deny who I am anymore. I have to break up with you,\" {initiator} says, trying to keep their voice steady.",
            "\"We had something beautiful, {target}, but I can no longer live a lie. Our relationship has to come to an end,\" {initiator} says, their voice filled with sorrow.",
            "\"This is the hardest thing I've ever had to do, {target}, but I can't ignore who I truly am. I have to end our relationship,\" {initiator} says, their voice barely above a whisper."
        ]
    },
    "mixer_social_ShareBabyPictures_Targeted_Friendly_AlwaysOn_STC": {
        # J: Does this mean {initiator}'s baby pictures or {target}'s?
        "pre_actions": [
            "{initiator} shares their baby pictures with {target}."
        ],
        "actions": [
            "\"{target}, I found something really adorable and I thought you might like to see it,\" {initiator} says, holding out a stack of baby pictures.",
            "\"You know, {target}, I was going through some old photo albums and I stumbled upon something that made me smile. Wanna take a look?\" {initiator} asks, a mischievous grin on their face.",
            "\"I can't believe I'm about to do this, but {target}, I trust you enough to show you a side of me that few people have seen. Brace yourself,\" {initiator} says, pulling out a photo album filled with baby pictures.",
            "\"I've always been a bit embarrassed by these, but I think it's time I share my adorable past with you, {target}. Prepare for cuteness overload,\" {initiator} says, handing over a photo album.",
            "\"I've been keeping these hidden in the attic for years, but I think it's time to reveal my secret stash of embarrassing baby pictures. What do you say, {target}?\" {initiator} suggests with a mischievous glint in their eyes.",
            "\"I never thought I'd willingly share these with anyone, but you've managed to get under my skin, {target}. Prepare to see a side of me you've never seen before,\" {initiator} says, pulling out a box of baby pictures.",
            "\"I hope you're ready for a good laugh, {target}, because I've got something that will surely make you chuckle. Baby pictures, anyone?\" {initiator} says, grinning as they take out a photo album.",
            "\"I've been hiding these for years, but I feel like it's time to let you in on a little secret, {target}. Get ready to see me in all my adorable glory,\" {initiator} says, holding a stack of baby pictures.",
            "\"You've seen me at my best and worst, {target}, but I'm about to show you a whole new side of me. Brace yourself for some incredibly embarrassing baby pictures,\" {initiator} warns with a playful smile.",
            "\"I never thought I'd willingly subject myself to embarrassment, but for you, {target}, I'm willing to make an exception. Get ready for a trip down memory lane,\" {initiator} says, unveiling a collection of baby pictures."
        ]
    },
    "mixer_social_ShareBigNews_targeted_Friendly_alwaysOn_pregnancy": {
        "pre_actions": [
            "{initiator} excitedly announces their pregnancy to {target}."
        ],
        "actions": [
            "\"Guess what, {target}! I have some incredible news to share with you,\" {initiator} says, unable to contain their excitement.",
            "\"I can't hold it in any longer, {target}. I'm going to be a parent!\" {initiator} exclaims, grinning from ear to ear.",
            "\"I have something life-changing to tell you, {target}. Are you ready? I'm pregnant!\" {initiator} reveals, their eyes shining with joy.",
            "\"Prepare yourself for the best news ever, {target}. I'm expecting a baby!\" {initiator} announces, unable to wipe the smile off their face.",
            "\"I've been bursting with happiness, {target}, and I can't keep it a secret any longer. I'm going to be a mom/dad!\" {initiator} shares, barely containing their excitement.",
            "\"I have something incredible to share with you, {target}. Brace yourself -  I'm pregnant!\" {initiator} reveals, their voice filled with anticipation.",
            "\"I've been waiting for the perfect moment to tell you, {target}, and now it's finally here. I'm going to be a parent!\" {initiator} says, their eyes sparkling with enthusiasm.",
            "\"Get ready for some amazing news, {target}. I'm thrilled to let you know that I'm pregnant!\" {initiator} exclaims, unable to hide their joy.",
            "\"I have a surprise that will change everything, {target}. I'm going to have a baby!\" {initiator} announces, their voice trembling with excitement.",
            "\"I can't believe I'm finally sharing this with you, {target}. I'm pregnant!\" {initiator} says, their face beaming with happiness."
        ]
    },
    "mixer_social_ShareIdeas_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} shares their ideas with {target}."
        ],
        "actions": [
            "\"I've been working on something, {target}, and I think you might find it interesting,\" {initiator} says excitedly.",
            "\"You know, {target}, I've had this idea brewing in my mind for a while now, and I think it's time to share it with you,\" {initiator} says, eager to get {target}'s opinion.",
            "\"I've been wanting to bounce some ideas off someone, and you immediately came to mind, {target}. Can I run something by you?\" {initiator} asks, hopeful.",
            "\"I've been brainstorming lately, {target}, and I think I've come up with something worth discussing. Can I get your input?\" {initiator} says, looking expectantly at {target}.",
            "\"You're the first person I thought of when this idea struck me, {target}. Let me share it with you and see what you think,\" {initiator} says, leaning in closer.",
            "\"I trust your judgment, {target}, and that's why I want to share my ideas with you. Are you open to hearing them?\" {initiator} asks, curious about {target}'s reaction.",
            "\"I've been toying with this concept, {target}, and I can't help but feel that you might have some valuable insights. Mind if I bounce it off you?\" {initiator} says, hoping for {target}'s support.",
            "\"I've been keeping this idea under wraps for a while, {target}, but I think it's time to bring it into the light. Can I share it with you?\" {initiator} says, eager to see {target}'s reaction.",
            "\"I've been itching to share my ideas with someone, and you're the perfect person for it, {target}. Can I get your thoughts on this?\" {initiator} asks, genuinely interested in {target}'s perspective.",
            "\"I've been working on a project, {target}, and I think it's time to let you in on the details. Can I have your undivided attention?\" {initiator} says, preparing to unveil their ideas."
        ]
    },
    "mixer_social_SitIntimate_Cuddle_targeted_friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} cuddles with {target} in a cosy spot."
        ],
        "actions": [
            "{initiator} snuggles closer to {target}, enjoying the warmth and comfort of their embrace.",
            "{target}, I love moments like this, just being able to hold you close,\" {initiator} murmurs softly.",
            "As {initiator} settles into {target}'s arms, they can't help but feel a sense of peace and contentment.",
            "\"You're the only person who can make me feel this safe, {target},\" {initiator} whispers, nuzzling against {target}'s chest.",
            "In the quiet intimacy of their cuddle, {initiator} feels a surge of affection for {target} and plants a gentle kiss on their cheek.",
            "{target}, I could stay like this with you forever,\" {initiator} sighs, their voice filled with tenderness.",
            "Feeling {target}'s steady heartbeat against their own, {initiator} closes their eyes and savors the moment, cherishing the connection between them.",
            "As they hold each other, {initiator} feels a rush of gratitude for {target}'s presence in their life, silently vowing to always cherish this bond.",
            "With every breath, {initiator} feels a sense of serenity wash over them, knowing that this moment with {target} is something truly special.",
            "In the comfort of their cuddle, {initiator} whispers, \"I'm so grateful to have you in my life, {target}.\""
        ]
    },
    "mixer_social_SitIntimate_FeedABite_targeted_romance_alwaysOn": {
        "pre_actions": [
            "{initiator} feeds a bite to {target}."
        ],
        "actions": [
            "\"{target}, I made this dish just for you. Let me feed you a bite,\" {initiator} says, their eyes locked with {target}'s.",
            "\"I've always found feeding someone to be an intimate act. Allow me to share this moment with you,\" {initiator} says, holding the morsel of food in front of {target}'s lips.",
            "\"I want to savor this moment with you, {target}. Let me feed you a taste of this deliciousness,\" {initiator} says, a playful smile on their face.",
            "\"Food tastes better when shared, especially when it's shared with someone special. Here, {target}, let me feed you,\" {initiator} suggests, offering a bite of food to {target}.",
            "\"{target}, I want to experience the pleasure of feeding you. It's a small gesture, but it holds so much meaning,\" {initiator} says, their voice filled with anticipation.",
            "\"There's something deeply sensual about feeding another person. Let me show you,\" {initiator} whispers, leaning in closer to {target}.",
            "\"I've always wanted to share a meal with you, {target}. Let me start by feeding you a bite,\" {initiator} says, their voice filled with genuine affection.",
            "\"Feeding someone is an act of trust and vulnerability. I want to share that with you, {target},\" {initiator} says, gently guiding the food to {target}'s mouth.",
            "\"I hope you don't mind, {target}, but I can't resist feeding you. It's my way of showing how much I care,\" {initiator} says, a hint of shyness in their voice.",
            "\"{target}, let me take care of you in this small way. Allow me to feed you and make you feel cherished,\" {initiator} says, their eyes warm with affection."
        ]
    },
    "mixer_social_SitIntimate_GiveVigorousMassage_targeted_romance_highScore": {
        "pre_actions": [
            "{initiator} goes from cuddling to giving a passionate massage to {target}."
        ],
        "actions": [
            "{initiator} playfully interrupts the cuddling session and suggestively says, \"Hey {target}, how about a massage?\"",
            "\"I've been practicing my massage skills, {target}, would you be up for a vigorous one?\" {initiator} asks, wiggling their eyebrows mischievously.",
            "After a few moments of cuddling, {initiator} suddenly jumps up and exclaims, \"{target}, I have the perfect idea! How about I give you a vigorous massage?\"",
            "With a mischievous grin, {initiator} sneaks behind {target} and jokingly says, \"Time for a surprise massage! Brace yourself, {target}.\"",
            "Feeling a burst of energy, {initiator} breaks away from cuddling and excitedly declares, \"{target}, my hands have magical massage powers! Would you like to experience them?\"",
            "As they lie intertwined, {initiator} takes notice of {target}'s tense shoulders and asks, \"You seem a little stressed, {target}. How about a vigorous massage to help you unwind?\"",
            "Whispering seductively in {target}'s ear, {initiator} suggests, \"I have a better idea than cuddling, {target}. How about a vigorous massage to really relax you?\"",
            "Feeling {target}'s muscles tense up, {initiator} decides to take matters into their own hands and says, \"I think you need a vigorous massage. Let me take care of you, {target}.\"",
            "{initiator} breaks away from cuddling and gestures towards the massage oil on the nearby table, saying, \"I've been wanting to give you a vigorous massage, {target}. Shall we get started?\"",
            "As {target} stretches out on the couch, {initiator} casually approaches and offers, \"I'm in the mood for a workout. How about a vigorous massage for you, {target}?\"",
            "Gently, {initiator} begins massaging {target}'s shoulders, gradually working their way down. \"You deserve to be pampered, {target}. Let me take care of you.\"",
            "{initiator} whispers in {target}'s ear, voice filled with desire, \"I want to give you a massage, {target}. Let me help you relax and unleash your tension.\"",
            "{initiator}'s fingers dance across {target}'s tense muscles, causing {target} to shiver in delight. \"{target}, I've been practicing my massage techniques, and I can't wait to try them on you.\"",
            "As {initiator}'s hands glide over {target}'s tense muscles, {target} lets out a pleasurable sigh, \"Wow, {initiator}, you are amazing at this.\"",
        ]
    },
    "mixer_social_SitIntimate_LookDeeplyIntoEyes_targeted_romance_middleScore": {
        "pre_actions": [
            "{initiator} looks deeply into {target}\'s eyes while cuddling them."
        ],
        "actions": [
            "As {initiator} cuddles {target}, they lock eyes and a wave of affection washes over them.",
            "With their bodies intertwined, {initiator} gazes into {target}'s eyes, lost in the moment.",
            "In the warmth of their embrace, {initiator} holds {target} close, their eyes speaking volumes.",
            "Amidst the cuddles, {initiator} finds solace in {target}'s eyes, a silent connection forming between them.",
            "As they cuddle, {initiator} can't help but get lost in {target}'s eyes, feeling a profound sense of comfort.",
            "In the quiet intimacy of their embrace, {initiator} searches {target}'s eyes for reassurance and finds it.",
            "With each gentle touch, {initiator} and {target} share a look that conveys a deep understanding.",
            "As they cuddle, {initiator} can't help but feel a magnetic pull towards {target}, their eyes locked in a tender exchange.",
            "In the peacefulness of the moment, {initiator} and {target} exchange a loving gaze, their eyes revealing unspoken emotions.",
            "As they cuddle, {initiator} and {target} share a heartfelt moment, their eyes telling a story of affection and vulnerability."
        ]
    },
    "mixer_social_SitIntimate_Snuggle_targeted_romance_alwaysOn": {
        "pre_actions": [
            "{initiator} snuggles with {target}."
        ],
        "actions": [
            "\"{target}, I just want to be close to you right now,\" {initiator} says, leaning in for a snuggle.",
            "\"I need your warmth and comfort right now, {target},\" {initiator} says, wrapping their arms around {target}.",
            "\"{target}, can we just snuggle for a while? I want to feel safe in your embrace,\" {initiator} says, nuzzling against {target}.",
            "\"Is it okay if I snuggle up to you, {target}? I could really use some cuddles,\" {initiator} says, seeking solace.",
            "\"I've had a rough day, {target}. Can we snuggle and forget about the world for a while?\" {initiator} pleads, looking tired.",
            "\"I love the way you make me feel safe, {target}. Mind if we snuggle for a bit?\" {initiator} asks, craving {target}'s touch.",
            "\"{target}, can we snuggle? I need to feel your arms around me,\" {initiator} whispers, seeking comfort.",
            "In a moment of vulnerability, {initiator} leans into {target}'s arms, seeking comfort and reassurance.",
            "As {initiator} snuggles up to {target}, they can't help but feel a sense of peace wash over them.",
        ]
    },
    "mixer_social_SitIntimate_TeaseFlirtatiously_targeted_romance_middleScore": {
        "pre_actions": [
            "{initiator} teases {target} flirtatiously while cuddling."
        ],
        "actions": [
            "\"{target}, you know you can't resist my charm,\" {initiator} says, playfully nuzzling against {target}'s neck.",
            "\"I bet you can't handle my cuddling skills, {target},\" {initiator} says with a mischievous smile.",
            "\"Let's see if you can concentrate on anything else while I tease you like this, {target},\" {initiator} says, tracing their finger lightly along {target}'s arm.",
            "\"Are you ready for some flirty teasing, {target}? Brace yourself,\" {initiator} whispers into {target}'s ear, their breath sending shivers down {target}'s spine.",
            "\"I love how you squirm under my teasing touch, {target},\" {initiator} says, their voice filled with playful seduction.",
            "\"You can't resist my playful banter, can you, {target}? It's one of my many irresistible qualities,\" {initiator} says, smirking confidently.",
            "\"{target}, it's a good thing you find my teasing adorable, otherwise I might have to turn it up a notch,\" {initiator} says, winking flirtatiously.",
            "\"I hope you're prepared for some irresistible teasing, {target}. I've been practicing,\" {initiator} says, pressing their body closer to {target}'s.",
            "\"{target}, I can't help but tease you when you look so cute and cuddly. It's a weakness of mine,\" {initiator} says, their eyes glimmering with mischief."
        ]
    },
    "mixer_social_SitIntimate_TickleMercilessly_targeted_romance_middleScore": {
        "pre_actions": [
            "{initiator} mercilessly tickles {target}, in a teasing way."
        ],
        "actions": [
            "\"{target}, you better watch out! I'm about to unleash my tickling skills on you,\" {initiator} says mischievously, wiggling their fingers.",
            "\"Prepare yourself, {target}, because I'm about to make you laugh uncontrollably,\" {initiator} threatens playfully, moving closer to {target}.",
            "\"You think you can escape my tickle attack, {target}? Think again!\" {initiator} declares, lunging towards {target} with a devilish grin.",
            "\"Don't even try to resist, {target}, because I know all your ticklish spots,\" {initiator} taunts, raising their eyebrows suggestively.",
            "\"Tickle, tickle, {target}! You can't hide from my tickle assault,\" {initiator} warns, narrowing their eyes mischievously.",
            "\"Prepare for the most merciless tickle session of your life, {target},\" {initiator} threatens, cracking their knuckles.",
            "\"Resistance is futile, {target}. My tickling skills are unmatched,\" {initiator} boasts, moving in closer with a twinkle in their eyes.",
            "\"You better surrender now, {target}, or else I'll tickle you until you beg for mercy,\" {initiator} warns, their voice filled with playful menace.",
            "\"Tickle attack incoming, {target}! Brace yourself for a wave of laughter,\" {initiator} declares, moving their fingers closer to {target}'s ticklish zones.",
            "\"Get ready to laugh until your sides hurt, {target}, because I'm about to unleash my tickling prowess on you,\" {initiator} says confidently, cracking a smile."
        ]
    },
    "mixer_social_SitIntimate_WhisperSweetNothings_targeted_romance_middleScore": {
        "pre_actions": [
            "{initiator} whispers sweet nothings to {target} while cuddling."
        ],
        "actions": [
            "\"{target}, you are the most beautiful person I've ever known,\" {initiator} whispers, their voice barely audible.",
            "\"I can't express how much I adore you, {target},\" {initiator} murmurs, holding {target} close.",
            "\"In this moment, I feel like the luckiest person alive, cuddling with you,\" {initiator} whispers softly into {target}'s ear.",
            "\"{target}, being in your arms feels like a dream come true,\" {initiator} whispers, their voice filled with tenderness.",
            "\"Your touch, {target}, it's like magic. I never want to let go,\" {initiator} whispers, their voice filled with affection.",
            "\"As I hold you, {target}, I can't help but be overwhelmed by how much I love you,\" {initiator} whispers, their voice trembling with emotion.",
            "\"Right now, {target}, nothing else matters except being here with you, whispering these sweet nothings,\" {initiator} murmurs, their voice filled with sincerity.",
            "\"{target}, the world fades away when I'm cuddling with you. I never want this moment to end,\" {initiator} whispers, their voice filled with longing.",
            "\"You bring so much warmth and happiness into my life, {target},\" {initiator} whispers, their voice laced with gratitude.",
            "\"In this moment, {target}, I feel like the luckiest person in the world, holding you close and whispering my love for you,\" {initiator} murmurs, their voice filled with adoration."
        ]
    },
    "mixer_social_SlapEmSilly_targeted_mischief_skills": {
        "pre_actions": [
            "{initiator} playfully slaps {target} in a silly way."
        ],
        "actions": [
            "\"{target}, you've been asking for it! Prepare yourself for a series of playful slaps!\" {initiator} exclaims, grinning mischievously.",
            "With a burst of energy, {initiator} starts giving {target} a playful flurry of slaps, laughing uncontrollably.",
            "\"{target}, let's see how you handle this!\" {initiator} says, giggling, as they start slapping {target} playfully on the arm.",
            "{initiator} playfully slaps {target} a few times, laughing and saying, \"You'll never see it coming!\"",
            "As {target} turns around, {initiator} surprises them with a series of playful slaps, saying, \"Gotcha!\"",
            "With a mischievous smile, {initiator} playfully slaps {target} on the back, saying, \"You can't escape my playful slaps!\"",
            "Amidst laughter, {initiator} starts giving {target} playful slaps, jokingly saying, \"Time for some friendly slapping contests!\"",
            "{initiator} playfully slaps {target} on the shoulder, saying, \"Consider this payback for all the pranks you've pulled on me!\"",
            "With a playful gleam in their eyes, {initiator} slaps {target} on the hand, saying, \"Tag, you're it!\"",
            "{initiator} starts playfully slapping {target} on the arm, saying, \"Let's see if you can handle my lightning-fast slaps!\""
        ]
    },
    "mixer_social_StartAFoodFight_targeted_Friendly_alwaysOn_prank": {
        "pre_actions": [
            "{initiator} starts a food fight with {target}."
        ],
        "actions": [
            "{initiator} tosses a spoonful of mashed potatoes at {target}, starting a food fight.",
            "Laughing mischievously, {initiator} grabs a handful of spaghetti and flings it at {target}, starting a messy food fight.",
            "With a mischievous grin, {initiator} playfully splatters a dollop of whipped cream onto {target}'s face, signaling the start of a food fight.",
            "As {initiator} playfully throws a cherry tomato at {target}, it sets off a chain reaction of food flying through the air.",
            "Unable to resist the temptation, {initiator} flicks a french fry at {target}, igniting a full-blown food fight.",
            "With a twinkle in their eye, {initiator} tosses a slice of pizza towards {target}, initiating a lively food fight.",
            "Unable to control themselves, {initiator} takes a handful of jelly and smears it across {target}'s cheek, sparking a food fight.",
            "Amidst laughter, {initiator} grabs a handful of pudding and hurls it at {target}, inciting a raucous food fight.",
            "With a mischievous smirk, {initiator} lobs a glob of chocolate sauce towards {target}, signaling the start of a messy food fight.",
            "Unable to resist the temptation, {initiator} dumps a cup of water onto {target}, instigating an impromptu food fight."
        ]
    },
    "mixer_social_SubtleyDebase_targeted_mischief_alwaysOn_trait": {
        "pre_actions": [
            "{initiator} undermines {target}'s self confidence."
        ],
        "actions": [
            "\"{target}, are you sure you can handle this? It might be a bit too much for you,\" {initiator} says condescendingly.",
            "\"You know, {target}, I don't think you have what it takes. It's just the truth,\" {initiator} says, smirking.",
            "\"Why do you even bother, {target}? You're never going to succeed,\" {initiator} says, rolling their eyes.",
            "\"I hate to break it to you, {target}, but you're not as talented as you think you are,\" {initiator} says dismissively.",
            "\"I've seen others do it better than you, {target}. Maybe you should just give up,\" {initiator} says, their tone dripping with superiority.",
            "\"I don't want to hurt your feelings, {target}, but you should really lower your expectations. You're not that great,\" {initiator} says, nonchalantly.",
            "\"I hate to burst your bubble, {target}, but you're just not cut out for this. Some people have it, and some people don't,\" {initiator} says with a smirk.",
            "\"I've been meaning to tell you this, {target}, but you're not as good as you think. It's time someone told you the truth,\" {initiator} says, their voice dripping with condescension.",
            "\"I hate to be the one to say it, {target}, but you're not as talented as you believe. Maybe it's time to face reality,\" {initiator} says, looking disinterested.",
            "\"I hope you're not planning on pursuing this, {target}. It's a waste of your time and energy,\" {initiator} says, shaking their head in disappointment."
        ]
    },
    "mixer_social_SuggestFunActivities_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} suggests fun activities to {target}."
        ],
        "actions": [
            "\"What do you say we go for a hike this weekend, {target}? It'll be a great way to enjoy nature and get some exercise,\" {initiator} suggests enthusiastically.",
            "\"I've got an idea, {target}. How about we have a movie marathon at my place? We can pick out all our favorite films and have a cozy night in,\" {initiator} suggests with a smile.",
            "\"I've been wanting to try out this new escape room, {target}. It's supposed to be really challenging. How about we give it a shot together?\" {initiator} suggests, excitedly.",
            "\"I heard about this new mini-golf place that just opened up, {target}. It could be a fun and competitive way to spend an afternoon. What do you think?\" {initiator} suggests, playfully.",
            "\"I've been itching to go roller skating for ages, {target}. How about we relive our childhood memories and have a fun roller skating date?\" {initiator} suggests, grinning.",
            "\"Hey, {target}, I just found out about this pottery painting workshop. It could be a unique and creative way to spend some time together. Are you up for it?\" {initiator} suggests with curiosity.",
            "\"I know this really cool board game café, {target}. Let's go there and play some of the classics. It'll be a blast!\" {initiator} suggests, eager to have a good time.",
            "\"I've got an idea, {target}. Let's go to the local amusement park and ride all the thrilling roller coasters. It'll be an adrenaline-filled adventure!\" {initiator} suggests, looking excited.",
            "\"I've been meaning to try out this new recipe, {target}. How about we have a cooking night and experiment with different flavors? It'll be delicious and fun!\" {initiator} suggests with a hint of culinary enthusiasm.",
            "\"I've heard about this comedy show happening downtown, {target}. Let's go and have a good laugh together. It'll be a great way to unwind and enjoy each other's company,\" {initiator} suggests, smiling."
        ]
    },
    "mixer_social_SuggestWorkingOut_targeted_Friendly_Athlete_AlwaysOn_STC": {
        "pre_actions": [
            "{initiator} suggests working out to {target}."
        ],
        "actions": [
            "\"Hey {target}, I was thinking maybe we could start working out together. What do you say?\" {initiator} asks with a hopeful smile.",
            "\"I've been trying to get into shape lately, and I thought it would be more fun if we did it together, {target},\" {initiator} suggests, looking at {target} expectantly.",
            "\"You know, {target}, I've heard that working out with a partner can be really motivating. Want to give it a try?\" {initiator} proposes, raising an eyebrow.",
            "\"I've been looking for a workout buddy, and I couldn't think of anyone better than you, {target}. What do you think?\" {initiator} suggests, giving {target} a friendly nudge.",
            "\"I've been struggling to find the motivation to work out lately, but I think if we did it together, {target}, it would be so much easier. What do you say?\" {initiator} asks, biting their lip nervously.",
            "\"{target}, I was wondering if you'd be interested in joining me for some workouts. I think it could be a great way for us to spend more time together,\" {initiator} suggests, trying to hide their excitement.",
            "\"I've been feeling really lethargic lately, and I thought maybe working out with you, {target}, would help me get back on track. What do you think?\" {initiator} asks, looking hopeful.",
            "\"Hey {target}, I know you're into fitness, and I was wondering if you could show me a thing or two. Maybe we could work out together?\" {initiator} suggests, scratching their head nervously.",
            "\"I've been hearing a lot about the benefits of exercising with a partner, and I thought maybe we could give it a shot, {target}. What do you say?\" {initiator} asks, trying to sound casual.",
            "\"{target}, I've been feeling a bit out of shape lately, and I thought maybe we could motivate each other by working out together. What do you think?\" {initiator} suggests, crossing their fingers."
        ]
    },
    "mixer_social_TalkAboutDreams_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} talks to {target} about their dreams."
        ],
        "actions": [
            "\"So, {target}, have you ever had any dreams that feel so real, they stay with you even after you wake up?\" {initiator} asks, curious.",
            "\"You know, {target}, I had the most incredible dream last night. It was like stepping into another world,\" {initiator} shares, excitement in their voice.",
            "\"I've been thinking a lot about dreams lately, {target}, and I can't help but wonder what they mean,\" {initiator} muses, looking thoughtful.",
            "\"I had this dream the other night, {target}, and it felt so vivid, like I was living a different life. Do you ever experience that?\" {initiator} wonders aloud.",
            "\"Dreams are such fascinating things, don't you think, {target}? I had one recently that I can't stop thinking about,\" {initiator} says, eyes sparkling with intrigue.",
            "\"You know, {target}, I believe dreams hold a deeper meaning. I had this dream last night, and I can't shake the feeling that it was trying to tell me something,\" {initiator} confides, searching for {target}'s reaction.",
            "\"I had a dream last night that made me question everything, {target}. It was so vivid and realistic, I couldn't help but wonder if it was trying to show me something,\" {initiator} tells {target}, hoping for some insight.",
            "\"I love discussing dreams, {target}. They can be so mysterious and powerful. I had one recently that left me with so many questions,\" {initiator} says, leaning in closer to {target}.",
            "\"Dreams have always fascinated me, {target}. Like, how can our minds conjure up such vivid and imaginative experiences while we sleep?\" {initiator} ponders, eager to hear {target}'s thoughts.",
            "\"I had this dream last night, {target}, and it felt so real, as if I had actually lived it. Do you think dreams can be glimpses into parallel universes?\" {initiator} asks, a hint of wonder in their voice."
        ]
    },
    "mixer_social_TalkAboutDrinkMaking_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} talks to {target} about making drinks."
        ],
        "actions": [
            "\"You know, {target}, I've always been fascinated by the art of making drinks. Do you want to learn a few tricks?\" {initiator} asks, looking excited.",
            "\"I've been experimenting with different recipes lately, {target}, and I think I've finally perfected a few. Want to give them a try?\" {initiator} suggests, smiling.",
            "\"Have you ever wondered what goes into making the perfect cocktail, {target}? Let me show you the secrets I've learned over the years,\" {initiator} says, motioning towards the bar.",
            "\"There's something so therapeutic about making drinks, {target}. Would you like me to teach you my favorite concoctions?\" {initiator} offers, pouring a drink for {target}.",
            "\"I've been studying the art of mixology, {target}, and I've learned some interesting techniques. Care to join me in a little experiment?\" {initiator} asks, raising an eyebrow.",
            "\"Believe it or not, {target}, making drinks is not just about mixing ingredients. It's about creating an experience. Care to explore that with me?\" {initiator} suggests, leaning in.",
            "\"Making drinks is like crafting a masterpiece, {target}. I'd love to share my process with you. Are you up for it?\" {initiator} says, grabbing a cocktail shaker.",
            "\"{target}, I've always found the process of making drinks to be a form of art. Would you be interested in learning the techniques behind it?\" {initiator} asks, eyes gleaming.",
            "\"Let's shake things up a bit, {target}. I'll show you how to make some killer cocktails. Interested?\" {initiator} says, grabbing a bottle of liquor.",
            "\"{target}, there's nothing quite like the satisfaction of creating a perfectly balanced drink. Care to join me in uncovering the secrets?\" {initiator} suggests, raising a glass."
        ]
    },
    "mixer_social_TalkItOut_targeted_romance_alwaysOn_JealousTrait": {
        "pre_actions": [
            "{initiator} decides to talk it out with {target}."
        ],
        "actions": [
            "\"I've been wanting to talk to you about something, {target}. Can we find a quiet place and have a conversation?\" {initiator} asks, looking earnestly at {target}.",
            "\"Hey, {target}, do you have a moment? I feel like we really need to sit down and have a heart-to-heart,\" {initiator} suggests, searching for a private space.",
            "\"I've been carrying something on my mind, {target}, and I think it's time we have a serious talk about it. Can we find a place to chat?\" {initiator} proposes, hoping for {target}'s understanding.",
            "\"I can't keep it to myself any longer, {target}. Let's find a quiet corner and talk things through,\" {initiator} insists, feeling a sense of urgency to discuss the matter.",
            "\"I know we've been avoiding this topic, {target}, but it's time we face it head-on. Can we have a conversation about it?\" {initiator} suggests, hoping {target} will be receptive.",
            "\"I've been feeling a lot of tension between us lately, {target}, and I think it's time we address it. Can we sit down and talk it out?\" {initiator} proposes, hoping for a resolution.",
            "\"I've been bottling up my feelings, {target}, and it's becoming unbearable. Can we please find a quiet spot and have a conversation about it?\" {initiator} pleads, desperate to open up.",
            "\"Something has been bothering me, {target}, and I really need to get it off my chest. Can we find a place to talk, just the two of us?\" {initiator} asks, hoping for {target}'s support.",
            "\"I've noticed a change in our dynamic, {target}, and I think it's time we address it. Can we find a moment to sit down and discuss it?\" {initiator} suggests, hoping for clarity.",
            "\"I don't want things to remain unresolved between us, {target}. Can we find a quiet space and have a conversation about it?\" {initiator} requests, yearning for a resolution."
        ]
    },
    "mixer_Social_TalkRelationshipFears_Romance": {
        "pre_actions": [
            "{initiator} talks to {target} about their relationship fears."
        ],
        "actions": [
            "\"I've been thinking a lot about us, {target}, and I need to talk to you about my fears,\" {initiator} says, looking concerned.",
            "\"I've been feeling a bit uncertain about where we stand, {target}, and I think it's time we address it,\" {initiator} says, their voice tinged with worry.",
            "\"You know, {target}, I've been having some doubts about our relationship lately, and I think it's important we discuss them,\" {initiator} admits, looking slightly anxious.",
            "\"{target}, there's something I've been keeping to myself, and it's been causing me to worry. Can we talk about it?\" {initiator} asks tentatively.",
            "\"I've been feeling a bit insecure about our relationship, {target}, and I think it's important we have an open conversation about it,\" {initiator} suggests, their tone serious.",
            "\"I can't help but think about the future, {target}, and it's been making me anxious. Can we talk about my concerns?\" {initiator} asks, their voice wavering slightly.",
            "\"I've been bottling up my fears about our relationship, {target}, and I think it's time I share them with you,\" {initiator} confesses, their eyes searching {target}'s face.",
            "\"{target}, I've been having some doubts about whether we're on the same page, and I think we need to address it,\" {initiator} says, their voice filled with uncertainty.",
            "\"I've been feeling a bit scared about our relationship lately, {target}, and I need to talk to you about it,\" {initiator} says, their voice trembling slightly.",
            "\"There's something that's been bothering me about our relationship, {target}, and I think it's time we have an honest conversation about it,\" {initiator} says, looking earnestly at {target}."
        ]
    },
    "mixer_Social_Targeted_Friendly_Loyal_ConfessTrashTalk": {
        "pre_actions": [
            "{initiator} confesses to trash talking {target}."
        ],
        "actions": [
            "\"I have something to admit, {target}. I hope you can forgive me,\" {initiator} says, guilt evident in their voice.",
            "\"I need to come clean about something, {target}. It's about what I've been saying behind your back,\" {initiator} confesses, avoiding eye contact.",
            "\"You deserve to know the truth, {target}. I've been saying some terrible things about you, and I'm sorry,\" {initiator} admits, looking remorseful.",
            "\"I've been talking badly about you, {target}, and it's been eating away at me. I can't keep it a secret any longer,\" {initiator} says, feeling the weight of their words.",
            "\"I can't hide it any longer, {target}. I've been trash-talking you, and I need to own up to it,\" {initiator} says, swallowing hard.",
            "\"I've betrayed your trust, {target}, and I need to confess. I've been saying things about you that I deeply regret,\" {initiator} admits, with a hint of shame in their voice.",
            "\"{target}, I have to admit something that I'm not proud of. I've been spreading rumors and saying things about you that I shouldn't have,\" {initiator} says, looking apologetic.",
            "\"I've been deceiving you, {target}, and it's time I confess. I've been talking negatively about you, and I can't live with the guilt anymore,\" {initiator} says, with a mix of regret and sincerity.",
            "\"{target}, I need to be honest with you. I've been saying some hurtful things about you, and I want to make it right,\" {initiator} confesses, hoping for forgiveness.",
            "\"I've been a terrible friend, {target}, and I need to own up to it. I've been trash-talking you, and I'm deeply sorry,\" {initiator} says, their voice filled with regret."
        ]
    },
    "mixer_social_TellAViciousRumor_targeted_mischief_alwaysOn_trait": {
        "pre_actions": [
            "{initiator} tells a vicious rumor to {target}."
        ],
        "actions": [
            "\"You won't believe what I just heard, {target}. I have to share this rumor with you,\" {initiator} says, unable to contain their excitement.",
            "\"I know it's wrong, but I can't resist telling you this juicy rumor, {target}. Promise me you won't spread it further,\" {initiator} says, a mischievous grin on their face.",
            "\"I heard something that might shock you, {target}, and I couldn't resist sharing it with you. But promise me you won't judge,\" {initiator} says, unable to contain their curiosity.",
            "\"You're not going to believe what I just found out, {target}. This rumor is too scandalous not to share with you,\" {initiator} says, barely able to contain their laughter.",
            "\"I have a secret to tell you, {target}, but be warned, it's a nasty rumor. Don't shoot the messenger,\" {initiator} says, a hint of guilt in their voice.",
            "\"I know spreading rumors is wrong, but I couldn't resist telling you this one, {target}. Just promise me you won't confront anyone about it,\" {initiator} says, looking conflicted.",
            "\"You're not going to believe the gossip I just heard, {target}. Brace yourself for this wild rumor I'm about to share with you,\" {initiator} says, leaning in closer.",
            "\"I know it's bad to gossip, but I couldn't resist telling you this rumor, {target}. Just promise me you won't judge me for it,\" {initiator} says, their eyes gleaming.",
            "\"I've been itching to tell someone this rumor, {target}, and you're the first person who came to mind. But promise me you won't spread it further,\" {initiator} says, unable to hide their excitement.",
            "\"I have some inside information that I need to share with you, {target}. Brace yourself for this shocking rumor,\" {initiator} says, unable to contain their anticipation."
        ]
    },
    "mixer_social_TryForBaby_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} suggests trying for a baby with {target}."
        ],
        "actions": [
            "\"Hey {target}, I've been thinking... what do you think about the idea of starting a family together?\" {initiator} asks, a hopeful smile on their face.",
            "\"I know it's a big decision, but I can't help but imagine how amazing it would be if we had a child together. What do you say, {target}?\" {initiator} suggests, their voice filled with anticipation.",
            "\"{target}, I've been dreaming about our future lately, and I can't shake off the idea of us having a baby. How does that sound to you?\" {initiator} proposes, their eyes shining with excitement.",
            "\"Imagine the love we could create, {target}. The thought of bringing a child into this world with you, it's something I can't ignore. What do you think?\" {initiator} asks, their voice filled with longing.",
            "\"{target}, I have this incredible feeling that we would make amazing parents. Have you ever considered the possibility of having a baby together?\" {initiator} suggests, their expression hopeful.",
            "\"I've been doing a lot of thinking lately, {target}, and I can't help but feel that it's the right time for us to start a family. What do you say?\" {initiator} proposes, their voice filled with determination.",
            "\"{target}, I want to grow old with you, and I can't imagine a future without a child to share it with. What are your thoughts on trying for a baby?\" {initiator} asks, their eyes searching for {target}'s reaction.",
            "\"I know having a baby is a big responsibility, but I can't deny the longing I have to create a family with you, {target}. Would you be open to the idea?\" {initiator} suggests, their voice filled with vulnerability.",
            "\"{target}, the thought of us having a child together fills my heart with so much joy. What do you think about the idea of starting a family?\" {initiator} proposes, their face beaming with happiness.",
            "\"I've been thinking about our future a lot lately, {target}, and the idea of having a baby with you just feels right. How do you feel about expanding our family?\" {initiator} asks, their voice filled with hope."
        ]
    },
    "mixer_social_TryForBaby_targeted_romance_transition_Tent": {
        "pre_actions": [
            "{initiator} suggests trying for a baby with {target} in a camping tent."
        ],
        "actions": [
            "\"{target}, I've been thinking about our future together, and I have an idea,\" {initiator} says, a mischievous smile playing on their lips.",
            "\"Imagine this, {target}, a cozy camping tent, just the two of us, and a new adventure waiting to begin,\" {initiator} suggests, eyes sparkling with excitement.",
            "\"You know, {target}, I've been daydreaming lately about starting a family. What do you think about trying for a baby in a camping tent?\" {initiator} asks, a hint of nervousness in their voice.",
            "\"As we lay under the stars in that camping tent, {target}, I can't help but imagine the pitter-patter of little feet joining us. What if we try for a baby?\" {initiator} suggests, a hopeful tone in their voice.",
            "\"{target}, there's something magical about camping, isn't there? What if we take that magic a step further and try for a baby in a camping tent?\" {initiator} proposes, their eyes filled with anticipation.",
            "\"I have a wild idea, {target}. What if we make a baby in a camping tent? Just imagine the memories we could create,\" {initiator} suggests, a mischievous grin spreading across their face.",
            "\"{target}, I've been doing some research, and they say that trying for a baby in nature can increase our chances. How about we give it a shot in a camping tent?\" {initiator} suggests, their voice filled with excitement.",
            "\"Picture this, {target}, a camping tent in the wilderness, the perfect setting for creating new life. What do you say we try for a baby?\" {initiator} proposes, their eyes locking with {target}'s.",
            "\"{target}, I can't think of a more intimate and adventurous way to start a family than trying for a baby in a camping tent. Are you up for it?\" {initiator} asks, a mixture of nervousness and excitement in their voice.",
            "\"Let's make our dreams come true, {target}. What if we try for a baby in a camping tent? It would be a story we'd cherish forever,\" {initiator} suggests, their voice filled with hope."
        ]
    },
    "mixer_social_TryForBabyInBush_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} suggests trying for a baby with {target} in a bush outside."
        ],
        "actions": [
            "\"{target}, I have a crazy idea. What if we try for a baby... outside... in a bush?\" {initiator} suggests with a mischievous smile.",
            "\"I've been thinking, {target}. What if we make a baby... in a bush? It would be wild, adventurous, and definitely unforgettable,\" {initiator} says, raising an eyebrow.",
            "\"Hey {target}, I know this might sound unconventional, but what if we take things to the next level and try for a baby... outside... in a bush?\" {initiator} proposes, nervously.",
            "\"I've been dreaming about our future together, {target}, and I think it's time we take a leap of faith. How about trying for a baby...in a bush?\" {initiator} suggests, feeling a mix of excitement and uncertainty.",
            "\"Life is short, {target}, and I want to make the most of it. So, what do you say we try for a baby...in a bush? It'll be our little secret adventure,\" {initiator} proposes, grinning.",
            "\"Let's make a memory, {target}, something to tell our future child about. How about trying for a baby...in a bush? It's crazy, I know, but also incredibly romantic,\" {initiator} suggests, blushing.",
            "\"{target}, I have this idea that might sound a bit unconventional, but what if we try for a baby... in a bush? It would be a story to tell for generations,\" {initiator} says with a mix of excitement and nervousness.",
            "\"Sometimes, {target}, the best things in life come from doing something unexpected. So, how about we try for a baby...in a bush? It would be our little secret,\" {initiator} suggests, biting their lip.",
            "\"I know it might sound a bit crazy, {target}, but what if we try for a baby... in a bush? It would be like defying societal norms and having an adventure all at once,\" {initiator} says, trying to gauge {target}'s reaction.",
            "\"{target}, I've been thinking about our future together, and I have this idea that might sound a little unconventional. What do you think about trying for a baby...in a bush?\" {initiator} asks, their eyes shining with excitement."
        ]
    },
    "mixer_social_TryForBabyInHottub_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} suggests trying for a baby with {target} in the hot tub."
        ],
        "actions": [
            "\"{target}, I have an idea. What do you think about trying for a baby tonight? In the hot tub?\" {initiator} suggests playfully.",
            "\"I've been thinking about our future, {target}, and I think it's time we take the next step. Let's try for a baby tonight, in the hot tub,\" {initiator} proposes with a smile.",
            "\"{target}, I've been doing some research and apparently, trying for a baby in a hot tub can increase our chances. What do you say we give it a shot?\" {initiator} suggests, raising an eyebrow.",
            "\"I know it might sound unconventional, but I read that the heat from a hot tub can boost fertility. How about we give it a try, {target}?\" {initiator} suggests, a hint of excitement in their voice.",
            "\"{target}, I've been daydreaming about our future together, and the thought of having a baby has been on my mind. What if we try tonight, in the hot tub?\" {initiator} suggests, looking hopeful.",
            "\"{target}, I've been thinking about expanding our family, and I have an idea. Let's try for a baby tonight, in the hot tub. It could be a fun and memorable experience,\" {initiator} suggests, their eyes shining with anticipation.",
            "\"{target}, I've been doing some research and apparently, hot tubs can increase fertility. How about we seize the opportunity and try for a baby tonight?\" {initiator} suggests, a touch of excitement in their voice.",
            "\"{target}, I have a proposition for you. How about we make trying for a baby a little more exciting? Let's do it in the hot tub tonight,\" {initiator} suggests, a mischievous glint in their eyes.",
            "\"{target}, I know this might sound spontaneous, but what if we try for a baby tonight? In the hot tub? It could be a unique and romantic experience,\" {initiator} suggests, their voice filled with enthusiasm.",
            "\"{target}, I have an idea that might sound a little wild, but hear me out. What if we try for a baby tonight? In the hot tub? It could be a memorable beginning to our journey as parents,\" {initiator} suggests, their heart racing with anticipation."
        ]
    },
    "mixer_social_TryForBabyinHotTub_targeted_stand_romance_transition": {
        "pre_actions": [
            "{initiator} suggests trying for a baby while standing and holding {target} in the hot tub."
        ],
        "actions": [
            "\"Do you ever think about starting a family, {target}?\" {initiator} asks, their voice carried away by the steam rising from the hot tub.",
            "\"{target}, what if we took our relationship to the next level and tried for a baby?\" {initiator} suggests, their eyes filled with hope.",
            "\"Imagine the joy we could bring into our lives by bringing a child into this world, {target}. What do you think?\" {initiator} proposes, their grip tightening on {target}.",
            "\"{target}, I've been thinking...maybe it's time we consider expanding our family. What do you say?\" {initiator} asks, their voice filled with anticipation.",
            "\"While we're here, surrounded by warmth and love, {target}, I can't help but wonder if it's time for us to bring a little one into our lives,\" {initiator} shares, their voice laced with excitement.",
            "\"As the water soothes our bodies, {target}, I can't help but imagine the joy of having a child to share this hot tub with. What do you think?\" {initiator} suggests, their eyes sparkling.",
            "\"{target}, I have this idea brewing in my mind...what if we took a leap of faith and started a family? Can you picture it?\" {initiator} asks, their voice filled with longing.",
            "\"{target}, I've been dreaming about our future together, and I can't help but envision a family. What do you think about trying for a baby?\" {initiator} proposes, their heart pounding.",
            "\"{target}, I can't shake this feeling that it's the right time for us to bring a little one into our lives. What are your thoughts on starting a family?\" {initiator} asks, their voice trembling with excitement.",
            "\"In this moment, with you in my arms, {target}, I can't help but imagine the incredible love we could share with a child. What do you say we give it a try?\" {initiator} suggests, their voice filled with warmth."
        ]
    },
    "mixer_social_TryForBabyInObservatory_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} suggests trying for a baby with {target} in the observatory."
        ],
        "actions": [
            "\"{target}, I have an idea. What do you think about trying for a baby together? And I know the perfect place to start - the observatory,\" {initiator} suggests with excitement.",
            "\"I've been thinking about our future together, {target}, and I think it's time we take the next step. What do you say we try for a baby? Maybe we can start in the observatory,\" {initiator} proposes, their eyes sparkling.",
            "\"As we stand here, gazing at the stars, {target}, I can't help but imagine our own little star in the making. What do you think about trying for a baby, starting right here in the observatory?\" {initiator} asks, a smile playing on their lips.",
            "\"{target}, I have a proposition for you. Let's make our own little constellation. What do you say we try for a baby? We can start in the observatory, under the watchful eyes of the stars,\" {initiator} suggests, their voice filled with hope.",
            "\"{target}, this might sound crazy, but what if we try for a baby? And not just anywhere, but right here in the observatory. It feels like the perfect place to bring a new life into this world,\" {initiator} says, their eyes shining with anticipation.",
            "\"I've been thinking a lot about our future, {target}, and I can't help but imagine a little one running around. What do you think about trying for a baby? We can start in the observatory, the place where dreams come true,\" {initiator} suggests, a touch of nervousness in their voice.",
            "\"{target}, I have a proposition that might change our lives forever. How about we try for a baby? And let's make it special - we can start right here in the observatory, surrounded by the beauty of the universe,\" {initiator} says, a mix of excitement and apprehension in their voice.",
            "\"{target}, I've been feeling like our love is ready to create something beautiful. What if we try for a baby? And what better place to start than the observatory, where love and magic collide,\" {initiator} suggests, their eyes filled with love.",
            "\"As we stand here, looking up at the vast expanse of the universe, {target}, I can't help but feel the desire to create something extraordinary with you. What do you say we try for a baby? We can start in the observatory, where miracles happen,\" {initiator} proposes, their heart pounding.",
            "\"{target}, I have a proposition that might change everything. How about we try for a baby? And the observatory seems like the perfect place to begin this incredible journey together,\" {initiator} suggests, a hint of nervousness in their voice."
        ]
    },
    "mixer_social_TryForBabyInRocketShip_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} suggests trying for a baby with {target} in the rocket ship."
        ],
        "actions": [
            "\"{target}, I've been thinking...what if we tried for a baby? And not just anywhere, but in the rocket ship,\" {initiator} suggests with a mischievous smile.",
            "\"You know how important space exploration is to me, {target}. What do you say we take it to the next level and try for a baby in the rocket ship?\" {initiator} proposes, excitement evident in their voice.",
            "\"I know it might sound crazy, {target}, but what if we made a baby while we're in the rocket ship? It would be a truly unique and unforgettable experience,\" {initiator} suggests, raising an eyebrow.",
            "\"I've been dreaming about this idea, {target}, and I can't shake it off. What if we conceived a baby in the rocket ship? It would be like planting the seed of our love in the stars,\" {initiator} says, their eyes twinkling with anticipation.",
            "\"Imagine the story we could tell our child one day, {target}. 'You were conceived in a rocket ship, surrounded by the vastness of space.' It would be a legendary tale,\" {initiator} suggests, a hint of excitement in their voice.",
            "\"{target}, I have this crazy idea...what if we made a baby in the rocket ship? It would be the ultimate adventure, don't you think?\" {initiator} proposes, their eyes shining with enthusiasm.",
            "\"I've always wanted our love to reach new heights, {target}, and what better way to do it than by conceiving a baby in the rocket ship? It would be a symbol of our love defying gravity,\" {initiator} suggests, a smile playing on their lips.",
            "\"Picture this, {target}: a baby, conceived in zero gravity, floating among the stars. It would be the most extraordinary beginning for our little one,\" {initiator} suggests, their voice filled with wonder.",
            "\"{target}, I've been thinking...what if we tried for a baby in the rocket ship? It would be a bold and daring move, just like our love,\" {initiator} proposes, their heart pounding with anticipation.",
            "\"As crazy as it may sound, {target}, what if we took our love to new heights and tried for a baby in the rocket ship? It would be an adventure like no other,\" {initiator} suggests, a glimmer of excitement in their eyes."
        ]
    },
    "mixer_social_TryToChat_targeted_friendly_lowScore": {
        "pre_actions": [
            "{initiator} tries to make small talk with {target}, despite not knowing them very well."
        ],
        "actions": [
            "\"So, {target}, how's your day been so far?\" {initiator} asks, trying to break the ice.",
            "\"I don't know much about you, {target}, but I'm curious to know what your hobbies are,\" {initiator} says, attempting to start a conversation.",
            "\"You seem like an interesting person, {target}. Mind if I ask what you do for a living?\" {initiator} asks, hoping to learn more about {target}.",
            "\"I know we haven't really talked before, {target}, but do you have any favorite movies or TV shows?\" {initiator} asks, trying to find common ground.",
            "\"{target}, I'm not sure what your plans are for the weekend, but do you have any recommendations for places to visit?\" {initiator} asks, hoping to get some insight from {target}.",
            "\"I'm not great at small talk, but I'm genuinely interested in getting to know you, {target}. What do you enjoy doing in your free time?\" {initiator} asks, hoping to spark a conversation.",
            "\"{target}, I've been meaning to ask this for a while now. Do you have any favorite books or authors?\" {initiator} asks, hoping to find a shared interest.",
            "\"I hope this doesn't come across as too forward, {target}, but where did you grow up? I'm curious about your background,\" {initiator} says, trying to initiate a conversation.",
            "\"{target}, I've noticed that you have a great sense of style. Do you have any fashion tips you could share with me?\" {initiator} asks, trying to find a topic of conversation.",
            "\"I know we haven't known each other for long, {target}, but I'm curious to know if you have any upcoming travel plans?\" {initiator} asks, hoping to learn more about {target}'s interests."
        ]
    },
    "mixer_social_Vent_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} angrily vents about their problem to {target}."
        ],
        "actions": [
            "\"Why does everything have to go wrong all the time? I just can't catch a break,\" {initiator} rants, frustration evident in their voice.",
            "\"I'm so tired of dealing with this. It feels like I'm drowning, and I don't know how to get out,\" {initiator} vents, their anger palpable.",
            "\"{target}, I need to get this off my chest. This problem has been eating away at me, and I can't hold it in any longer,\" {initiator} says, their tone filled with rage.",
            "\"Do you ever feel like the world is conspiring against you? Because that's how I feel right now,\" {initiator} says angrily, seeking solace in {target}'s presence.",
            "\"I'm furious about this whole situation. I need someone to hear me out and understand my frustrations,\" {initiator} says, their voice seething with anger.",
            "\"I can't hold back my anger any longer, {target}. This problem has pushed me past my limit, and I need to vocalize it,\" {initiator} states, barely containing their rage.",
            "\"I feel like screaming my frustrations out. This anger is overwhelming, and I need to let it out,\" {initiator} confides in {target} with intensity.",
            "\"You know what makes me angry? This problem. This problem is driving me insane, and I can't keep it to myself anymore,\" {initiator} vents, needing an outlet for their anger.",
            "\"I have so much pent-up anger inside me, and it's about time I release it. {target}, prepare yourself,\" {initiator} says, their voice filled with resentment.",
            "\"I can't believe how unfair this situation is. I've had enough, and I need to share my anger with someone who understands,\" {initiator} says, their tone fiery."
        ]
    },
    "mixer_social_WhatsYourProblem_Targeted_Mean_Sentiments": {  # J: Actions seemed unnecessary. Did not add.
        "pre_actions": [
            "{initiator} confronts {target} and asks, \"What's your problem?\""
        ],
    },
    "mixer_social_WooHoo_targeted_romance_transition_Tent": {
        "pre_actions": [
            "{initiator} suggests being intimate with {target} in their camping tent."
        ],
        "actions": [
            "\"{target}, I have a crazy idea. What do you think about getting cozy in our camping tent?\" {initiator} asks with a mischievous smile.",
            "\"I know it might sound unconventional, but how about we make some unforgettable memories together in that camping tent, {target}?\" {initiator} suggests, raising an eyebrow.",
            "\"{target}, I've been thinking... What if we take our camping trip to a whole new level of intimacy? Just you and me, in that tent,\" {initiator} proposes, their voice laced with anticipation.",
            "\"Hey, {target}, I have a proposition. How about we turn this camping trip into a romantic adventure? Picture us, alone, beneath the stars in that tent,\" {initiator} says, their eyes gleaming with excitement.",
            "\"{target}, I have this wild idea. What do you think about spicing things up on this camping trip and exploring our connection in the privacy of our tent?\" {initiator} suggests, their heart pounding.",
            "\"{target}, let's make this camping trip unforgettable. How about we create some magical moments together in the cozy confines of our tent?\" {initiator} proposes, their voice filled with longing.",
            "\"Here's an idea, {target}. Let's make this camping trip an experience that we'll never forget. Shall we explore our desires within the confines of that tent?\" {initiator} suggests, a playful smirk on their face.",
            "\"Imagine this, {target}. The crackling of the campfire, the whisper of the wind through the trees, and us, wrapped in each other's arms inside that tent,\" {initiator} suggests, their voice tinged with desire.",
            "\"{target}, I have a proposition for you. How about we take advantage of this secluded camping spot and indulge in some intimate moments in our tent?\" {initiator} suggests, their eyes filled with longing.",
            "\"{target}, I can't help but imagine how incredible it would be to share intimate moments with you inside that tent. What do you say?\" {initiator} asks, their voice filled with anticipation."
        ]
    },
    "mixer_social_WooHooInBush_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} suggests being intimate with {target} in a bush outside."
        ],
        "actions": [
            "\"{target}, I have this crazy idea... What if we... you know... get intimate... in a bush outside?\" {initiator} suggests, their voice filled with excitement and mischief.",
            "\"I've been thinking about something... It might sound insane, but what if we find a secluded spot in nature and share an intimate moment together?\" {initiator} proposes with a mischievous smile.",
            "\"You know, {target}, there's this secluded bush outside... And I can't help but wonder if it would make a thrilling and intimate setting for us,\" {initiator} suggests, their eyes gleaming with anticipation.",
            "\"{target}, I've been fantasizing about doing something adventurous and intimate... What if we find a hidden spot in the wilderness and let our desires run wild?\" {initiator} whispers, their voice filled with anticipation.",
            "\"There's this magical bush outside... It's private and secluded. I can't help but think about how incredible it would be if we could share an intimate experience there,\" {initiator} suggests, biting their lip nervously.",
            "\"I know it might sound unconventional, but what if we escape to the outdoors and find a secret bush where we can be intimate?\" {initiator} suggests, their eyes sparkling with excitement.",
            "\"{target}, I have this wild idea... What if we venture out into nature and find a hidden bush where we can be intimate? It would be an unforgettable experience,\" {initiator} suggests, their voice filled with anticipation.",
            "\"As crazy as it sounds, {target}, what if we find a secret bush outside and explore our desires? The thrill of being in nature would add a whole new level of excitement,\" {initiator} suggests, their voice filled with curiosity.",
            "\"You know, {target}, I've always found the idea of being intimate in nature incredibly enticing. What if we find a secluded bush outside and make that fantasy a reality?\" {initiator} proposes, their eyes filled with longing.",
            "\"{target}, I know this might be a bit unconventional, but what if we find a hidden bush outside and share an intimate moment there? The excitement of the unknown would make it unforgettable,\" {initiator} suggests, their voice filled with anticipation."
        ]
    },
    "mixer_social_WooHooInHottub_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} makes a move on {target} while in the hot tub."
        ],
        "actions": [
            "{initiator} scoots closer to {target}, their bodies almost touching in the hot tub.",
            "With a mischievous smile, {initiator} playfully splashes {target} with water.",
            "Feeling bold, {initiator} reaches out and grabs {target}'s hand, their eyes locked in a heated gaze.",
            "As the steam rises from the hot tub, {initiator} leans in closer to {target}, their lips just inches apart.",
            "Under the moonlight, {initiator} brushes their fingers against {target}'s arm, sending shivers down their spine.",
            "In a daring move, {initiator} leans back and pulls {target} onto their lap, their bodies pressed tightly together.",
            "Feeling the chemistry between them, {initiator} whispers seductively into {target}'s ear, sending a shiver down their spine.",
            "With a playful smirk, {initiator} challenges {target} to a game of truth or dare in the hot tub.",
            "Unable to resist the temptation any longer, {initiator} leans in and softly kisses {target}'s lips.",
            "As the water bubbles around them, {initiator} takes {target}'s face in their hands and passionately kisses them."
        ]
    },
    "mixer_social_WooHooinHotTub_targeted_Stand_romance_transition": {
        "pre_actions": [
            "{initiator} makes a move on {target} while standing in the hot tub."
        ],
        "actions": [
            "\"{target}, I've been meaning to tell you this for a while now, but I can't hold it in any longer,\" {initiator} says, leaning closer to {target} in the hot tub.",
            "\"I've been feeling a strong connection between us, {target}, and I can't ignore it any longer,\" {initiator} says, their voice filled with anticipation.",
            "\"The warmth of this hot tub isn't the only thing making me feel heated, {target}. I've been wanting to do this for a while,\" {initiator} says, moving closer to {target}.",
            "\"I hope you don't mind, {target}, but the steamy atmosphere in this hot tub has made me want to take a chance,\" {initiator} says, their eyes locked with {target}'s.",
            "\"{target}, there's something about being in this hot tub that's making me feel bold. Can I show you how I feel?\" {initiator} asks, their heart pounding.",
            "\"{target}, I've been keeping this to myself for too long, but being in this hot tub with you has given me the courage to make a move,\" {initiator} says, their voice filled with desire.",
            "\"You know, {target}, there's something about the water in this hot tub that's making me want to dive into the unknown with you,\" {initiator} says, their body inching closer.",
            "\"The combination of the bubbling water and your presence, {target}, has made me realize that I can't resist making a move,\" {initiator} says, their voice filled with longing.",
            "\"{target}, I've been trying to fight these feelings, but being in this hot tub with you has made it impossible to resist,\" {initiator} says, their voice trembling with anticipation.",
            "\"I hope you're open to the idea, {target}, because being in this hot tub has made me want to take a chance on us,\" {initiator} says, their eyes filled with hope."
        ]
    },
    "mixer_social_WooHooInObservatory_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} makes a move on {target} in the observatory."
        ],
        "actions": [
            "\"I've always found the observatory to be an enchanting place, don't you think, {target}?\" {initiator} says, their voice filled with a hint of flirtation.",
            "\"There's something about the stars and the quietness up here that makes me feel so close to you, {target},\" {initiator} whispers, their eyes locked with {target}'s.",
            "\"Being in this observatory with you feels like a dream, {target},\" {initiator} admits, their heart beating a little faster.",
            "\"The stars may be beautiful, but they pale in comparison to you, {target},\" {initiator} says, their eyes sparkling with admiration.",
            "\"{target}, I can't help but feel this magnetic pull towards you. Would you mind if I got a little closer?\" {initiator} asks, their voice filled with desire.",
            "\"I've been admiring you from afar for so long, {target}, and tonight, under the stars, I can't resist any longer. Can I show you how I feel?\" {initiator} says, their eyes locked onto {target}.",
            "\"There's something about this observatory that makes me want to take a leap of faith, {target}, and that leap involves you. Are you ready for it?\" {initiator} asks, a hint of anticipation in their voice.",
            "\"{target}, I've been holding back for too long, but something about this moment feels right. Can I show you how much I've been wanting you?\" {initiator} says, their voice filled with longing.",
            "\"I've been waiting for the perfect moment to make my move, {target}, and being here, surrounded by the beauty of the stars, I can't think of a more perfect time. Can I kiss you?\" {initiator} asks, their heart racing.",
            "\"{target}, every time I look at you, I feel an undeniable connection. In this observatory, where the universe seems to align, can I show you just how much you mean to me?\" {initiator} says, their voice filled with sincerity.",
            "\"{target}, I can't help but be drawn to you. Would you mind if I held your hand and shared this beautiful view with you?\" {initiator} asks, their voice slightly shaky.",
            "\"{target}, there's something about this observatory that makes me feel brave. And in this bravery, I want to make a move on you. Can I take that chance?\" {initiator} says, their eyes filled with determination.",
            "\"I've been dreaming about this moment, {target}, and here we are, alone in the observatory. Can I show you just how much I've been fantasizing about you?\" {initiator} says, their voice filled with anticipation.",
            "\"{target}, there's a spark between us that I can no longer ignore. Being in this observatory, I can't help but feel the need to act on it. Can I take that leap with you?\" {initiator} asks, their voice filled with hope."
        ]
    },
    "mixer_social_WooHooInRocketShip_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} make a move on {target} while on the rocket ship."
        ],
        "actions": [
            "\"Hey {target}, I have something I've been wanting to do for a while now,\" {initiator} says, a mischievous glint in their eyes.",
            "\"As we float in zero gravity, {target}, there's something I can't resist doing,\" {initiator} says, inching closer.",
            "\"I've always wondered what it would be like to kiss you, {target}, and now seems like the perfect moment to find out,\" {initiator} says, leaning in slowly.",
            "\"Being on this rocket ship with you, {target}, has given me the courage to do something I've been dreaming about,\" {initiator} says, their heart racing.",
            "\"Let's make this rocket ship experience even more unforgettable, {target}. I want to show you just how much I care,\" {initiator} says, moving closer, their face flushed.",
            "\"I can't hold it in any longer, {target}. Being here with you on this rocket ship has made me realize how much I want to be closer to you,\" {initiator} says, their voice filled with desire.",
            "\"As the rocket ship propels us through the stars, {target}, I can't help but feel an overwhelming urge to do this,\" {initiator} says, closing the gap between them.",
            "\"The weightlessness of this rocket ship gives me the perfect opportunity to do something I've been dying to do, {target},\" {initiator} says, a hint of nervousness in their voice.",
            "\"Let's make this journey to the stars even more magical, {target}. I want to share a moment with you that we'll never forget,\" {initiator} says, their eyes sparkling.",
            "\"Being on this rocket ship with you, {target}, has made me realize that life is too short to not take risks. So, here I am, taking one,\" {initiator} says, their voice filled with determination."
        ]
    },
    "mixer_social_YellAT_targeted_mean": {
        "pre_actions": [
            "{initiator} angrily yells at {target}."
        ],
        "actions": [
            "\"{target}, how dare you do this to me?!\" {initiator} yells, their face red with rage.",
            "\"I can't believe you would be so careless, {target}!\" {initiator} shouts angrily.",
            "\"I've had enough of your excuses, {target}! It's time we had a serious talk,\" {initiator} yells, frustration evident in their voice.",
            "\"You've crossed a line, {target}, and I won't stand for it. Prepare to hear what I really think,\" {initiator} yells, their voice filled with anger.",
            "\"{target}, you've pushed me too far this time! Get ready for a piece of my mind,\" {initiator} shouts, their voice echoing through the room.",
            "\"I'm sick and tired of your behavior, {target}! It's time I let you know exactly how I feel,\" {initiator} yells, their voice shaking with anger.",
            "\"Enough is enough, {target}! I'm not going to tolerate this any longer,\" {initiator} yells, their tone laced with frustration.",
            "\"{target}, you've made a huge mistake, and I'm here to make sure you understand that!\" {initiator} shouts angrily.",
            "\"{target}, I've had it up to here with you! Prepare yourself for a verbal lashing,\" {initiator} yells, their voice filled with irritation.",
            "\"Don't you dare ignore me, {target}! I demand your attention right now!\" {initiator} yells, their voice full of fury.",
            "\"{target}, you're absolutely infuriating! Can't you do anything right?\" {initiator} yells, anger in their voice.",
            "\"Are you really this incompetent, {target}? I can't believe I have to put up with your stupidity!\" {initiator} shouts, losing their patience.",
            "\"{target}, I've had enough of your nonsense! Get your act together or just get out of my sight!\" {initiator} exclaims, frustration evident in their tone.",
            "\"I can't stand you anymore, {target}! Your constant mistakes are driving me insane!\" {initiator} yells, unable to control their anger.",
            "\"{target}, you're so careless! How can someone be as clueless as you?\" {initiator} shouts, feeling overwhelmed by their frustration.",
            "\"Sometimes I wonder if you're really this dumb, {target}, or if you're just pretending to be!\" {initiator} yells, feeling exasperated.",
            "\"{target}, I don't know how much more of your incompetence I can take! You're pushing me to my limits!\" {initiator} shouts, their voice filled with irritation.",
            "\"Can you just think for once, {target}? I'm tired of dealing with the mess you constantly create!\" {initiator} yells, feeling fed up.",
            "\"{target}, you never cease to amaze me with your foolishness! How hard is it for you to understand simple instructions?\" {initiator} shouts, their voice laced with annoyance.",
            "\"I'm at my wit's end, {target}! I can't take your stupidity any longer!\" {initiator} yells, their anger finally boiling over.",
        ]
    },
    "mixer_socials_BragAboutBaby_Targeted_Friendly_AlwaysOn_STC": {
        "pre_actions": [
            "{initiator} brags about how amazing their baby is to {target}."
        ],
        "actions": [
            "\"{target}, I can't help but gush about how incredible my baby is. They are such a joy to have in my life,\" {initiator} says with a proud smile.",
            "\"You won't believe how adorable and smart my baby is, {target}. They are truly a wonder,\" {initiator} boasts, unable to contain their excitement.",
            "\"I have to tell you, {target}, my baby is like no other. They are just so perfect in every way,\" {initiator} says, beaming with pride.",
            "\"I can't help but brag about my baby, {target}. They are a little bundle of happiness and I'm just so lucky to have them,\" {initiator} says, their voice full of love.",
            "\"You have to see my baby, {target}. They are so precious and special. I can't help but brag about them to everyone I meet,\" {initiator} says, their enthusiasm overflowing.",
            "\"{target}, my baby is truly amazing. They have already accomplished so much and I can't help but boast about their achievements,\" {initiator} says, unable to contain their pride.",
            "\"I know every parent thinks their baby is the best, but {target}, mine really is. They are simply extraordinary,\" {initiator} says confidently.",
            "\"I just have to tell someone, {target}. My baby is the most wonderful being on this planet and I can't help but tell the whole world about them,\" {initiator} says excitedly.",
            "\"{target}, I know it might sound like I'm bragging, but my baby really is exceptional. They bring so much joy into my life,\" {initiator} says, their voice filled with adoration.",
            "\"I want to share how amazing my baby is with you, {target}. They are a true blessing and I can't help but rave about them,\" {initiator} says, unable to hide their excitement."
        ]
    },
    "mixer_socials_ComplainAboutDish_Targeted_Friendly_AlwaysOn_DiningSocials": {
        "pre_actions": [
            "{initiator} complains about a dish to {target}."
        ],
        "actions": [
            "\"{target}, I have to be honest, this dish is really not up to my expectations,\" {initiator} says, frowning at their plate.",
            "\"I hate to say it, {target}, but this food is just not good. I can't even take another bite,\" {initiator} says, pushing their plate away.",
            "\"I don't mean to sound rude, {target}, but this dish is a complete disappointment. I expected so much more,\" {initiator} says, shaking their head.",
            "\"I'm sorry, {target}, but this dish is a disaster. I can't believe they actually serve this here,\" {initiator} says, clearly frustrated.",
            "\"Is it just me, {target}, or does this dish taste really off? I can't even figure out what they were trying to accomplish with this,\" {initiator} says, scrunching up their nose.",
            "\"I don't want to be harsh, {target}, but this dish is nowhere near what I was hoping for. I'm really disappointed,\" {initiator} says, sounding slightly exasperated.",
            "\"I hate to be the bearer of bad news, {target}, but this dish is just not good. I wouldn't recommend it to anyone,\" {initiator} says, trying to hide their disappointment.",
            "\"Maybe it's just my taste buds, {target}, but this dish doesn't do it for me. I expected much better from this place,\" {initiator} says, looking dissatisfied.",
            "\"I don't want to sound like a complainer, {target}, but this dish really misses the mark. I can't understand why people rave about it,\" {initiator} says, shaking their head.",
            "\"I have to be honest, {target}, this dish is a letdown. I was expecting something much more flavorful and well-executed,\" {initiator} says, feeling letdown."
        ]
    },
    "mixer_socials_ComplainAboutExperimentalFood_Targeted_Friendly_AlwaysOn_DiningSocials": {
        "pre_actions": [
            "{initiator}, while dining, complains about the experimental food to {target}."
        ],
        "actions": [
            "\"This dish is absolutely disgusting, {target},\" {initiator} says, scrunching up their face in disgust.",
            "\"I can't believe they expect us to eat this, {target}. It's like they're playing a cruel joke on us,\" {initiator} complains, pushing the plate away.",
            "\"I'm sorry, but I just can't stomach this food. It's unbearable,\" {initiator} says, looking apologetic.",
            "\"I hate to be rude, {target}, but I can't pretend to enjoy this meal. It's just not up to par,\" {initiator} says, gesturing towards the plate.",
            "\"Is it just me, or does this food taste completely off? I can't even identify half the ingredients,\" {initiator} complains, wrinkling their nose.",
            "\"I thought I was open to trying new things, but this dish is pushing me to my limits,\" {initiator} says, shaking their head in disbelief.",
            "\"Do you taste that strange aftertaste, {target}? This food is seriously questionable,\" {initiator} remarks, looking concerned.",
            "\"I don't mean to sound picky, but I was expecting something a bit more appetizing than this,\" {initiator} says with a disappointed sigh.",
            "\"Maybe it's just my taste buds, but this food lacks any flavor whatsoever,\" {initiator} says, frowning at the dish.",
            "\"You know, {target}, I hate to be negative, but this food is a complete disaster. I can't even bring myself to take another bite,\" {initiator} says, shaking their head in disappointment."
        ]
    },
    "mixer_socials_DiscussExperimentalFood_Targeted_Friendly_AlwaysOn_DiningSocials": {
        "pre_actions": [
            "{initiator}, while dining, discusses the experimental food with {target}."
        ],
        "actions": [
            "\"This dish is unlike anything I've ever tried before! Have you ever had anything like it, {target}?\" {initiator} asks, taking another bite.",
            "\"{target}, I highly recommend you try this dish. It's a culinary adventure you won't want to miss,\" {initiator} says with excitement.",
            "\"Can you believe the flavors in this dish, {target}? It's like a party in my mouth!\" {initiator} exclaims, gesturing to their plate.",
            "\"I have to say, {target}, this experimental food is a bit out there. What do you think? Does it tickle your taste buds or leave you bewildered?\" {initiator} asks, raising an eyebrow.",
            "\"{target}, let's raise our glasses and toast to the genius who created this experimental masterpiece. Cheers!\" {initiator} suggests, holding up their glass.",
            "\"As adventurous eaters, {target}, we simply couldn't resist ordering the experimental dishes. How about we share our thoughts on each one?\" {initiator} proposes, eager to hear {target}'s opinion.",
            "\"Isn't it fascinating how this experimental food pushes the boundaries of traditional flavors? It takes a brave chef to venture into uncharted culinary territory,\" {initiator} remarks, intrigued.",
            "\"{target}, I have a feeling this experimental food will take us on a gastronomic journey we won't forget. Brace yourself for the unexpected!\" {initiator} says, grinning mischievously.",
            "\"Let's play a game, {target}. As we taste this experimental food, we have to guess the secret ingredient in each dish. Sound like fun?\" {initiator} suggests playfully.",
            "\"{target}, I'm curious to know your thoughts on this experimental food. Would you consider it a culinary masterpiece or a failed attempt at innovation?\" {initiator} asks, genuinely interested in {target}'s opinion."
        ]
    },
    "mixer_socials_GossipAboutOtherParents_Targeted_Friendly_AlwaysOn_STC": {
        # J: Actions seem unnecessary; did not add.
        "pre_actions": [
            "{initiator} gossips about other parents with {target}."
        ],
    },
    "mixer_social_Targeted_Friendly_DiscussFears": {
        "pre_actions": [
            "{initiator} discusses their deepest fears with {target}."
        ],
        "actions": [
            "\"{target}, I've been thinking a lot about my fears lately, and I feel like I need to share them with you,\" {initiator} says, looking somewhat uneasy.",
            "\"I trust you enough to confide in you about my deepest fears, {target},\" {initiator} admits, their voice trembling slightly.",
            "\"You've always been there for me, {target}, and I feel like it's time to open up about my biggest fears,\" {initiator} says, searching {target}'s face for reassurance.",
            "\"Lately, I've been grappling with some intense fears, {target}, and I think it's important for me to talk to someone I trust. That's why I've chosen to confide in you,\" {initiator} explains, their voice filled with vulnerability.",
            "\"There's something I can't shake off, {target}, a fear that has been haunting my thoughts. I thought maybe sharing it with you would help me gain some perspective,\" {initiator} says, with a hint of hesitation in their voice.",
            "\"I've been keeping this locked away for so long, {target}, but I feel like I can't carry this burden alone anymore. Will you listen to me as I share my deepest fears?\" {initiator} asks, their eyes searching {target}'s face.",
            "\"I know it's not easy to talk about fears, {target}, but I believe that opening up to you might bring some relief. Can I trust you with this?\" {initiator} says, a touch of anxiety in their voice.",
            "\"There's a part of me that's scared, {target}, and I want to confront that fear. I hope you can lend me an ear as I share the depths of my apprehensions,\" {initiator} says, with a mixture of determination and vulnerability.",
            "\"I've been carrying this fear deep within me, {target}, but I think it's time to let it out. I thought maybe discussing it with you could help me make sense of it all,\" {initiator} says, feeling a sense of relief in their words.",
            "\"I've always admired your courage, {target}, and I think it's about time I faced my fears head-on. Can I count on your support as I unveil them?\" {initiator} asks, their expression grave.",
            "\"{target}, there's something I need to talk to you about. It's something that has been haunting me for as long as I can remember,\" {initiator} says, their voice filled with vulnerability.",
            "\"I never thought I would open up about this, but I trust you enough to share my deepest fears,\" {initiator} says, looking directly into {target}'s eyes.",
            "\"There's a part of me that I've kept hidden for so long, {target}, and I feel like it's time to let you in on my deepest fears,\" {initiator} admits, their voice trembling.",
            "\"I've always admired your strength, {target}, but there are some fears that I've never been able to overcome. Can I confide in you?\" {initiator} asks, seeking reassurance.",
            "\"You know, {target}, there's something I've never told anyone before. It's my deepest fear, and it's been eating away at me. Can you handle it?\" {initiator} says, hesitatingly.",
            "\"I've been carrying this fear with me for far too long, {target}, and it's been holding me back. I think it's time I share it with you,\" {initiator} confesses, their voice filled with determination.",
            "\"There's a fear that's been consuming my thoughts, {target}, and I can't keep it to myself any longer. Will you listen?\" {initiator} says, their voice filled with a mix of anxiety and hope.",
            "\"I've always been afraid to admit this, {target}, but I feel a connection with you that makes me want to reveal my deepest fears. Can I trust you?\" {initiator} asks cautiously.",
            "\"I've admired your bravery, {target}, but there's one fear that I can no longer hide. Brace yourself, because this is something I've never shared with anyone,\" {initiator} says, preparing to unveil their deepest fears.",
            "\"This fear has held me back for far too long, {target}, but in you, I see someone who can help me overcome it. Will you be there for me?\" {initiator} says, their voice filled with a mix of fear and hope.",
        ]
    },
    "socialMixer_Greetings_Dismiss": {
        "pre_actions": [
            "{initiator} greets {target} dismissively."
        ],
        "actions": [
            "\"{target}, didn't expect to see you here,\" {initiator} says with a hint of annoyance.",
            "\"Oh, it's you,\" {initiator} says, barely acknowledging {target}.",
            "{initiator} gives {target} a quick nod before turning away.",
            "\"Hey, {target},\" {initiator} says, barely making eye contact.",
            "{initiator} lets out a sigh as {target} approaches, \"What do you want?\"",
            "\"Didn't think I'd have to deal with you today,\" {initiator} mutters under their breath.",
            "{initiator} waves {target} off, \"Not in the mood for company.\"",
            "{initiator} greets {target} with a half-hearted smile, \"Long time no see.\"",
            "{initiator} rolls their eyes at {target}'s presence, \"What brings you here?\"",
            "\"Hey,\" {initiator} says curtly, clearly wanting to end the conversation quickly."
        ]
    },
    "mixer_social_WeatherTemperatureSocials_ComplainAboutFreezingTemperature": {
        "pre_actions": [
            "{initiator} complains about the freezing temperature to {target}."
        ],
        "actions": [
            "\"{target}, can you believe how cold it is today? I feel like I'm freezing to death!\" {initiator} exclaims, rubbing their arms for warmth.",
            "\"I don't know how you handle this cold weather, {target}. It's like my bones are turning into icicles,\" {initiator} complains, shivering uncontrollably.",
            "\"I swear, {target}, it's colder than the North Pole out here. I can't feel my fingers or toes!\" {initiator} grumbles, hugging themselves tightly.",
            "\"{target}, I can't stand this freezing temperature anymore. It's like the universe is punishing us with this unbearable cold,\" {initiator} whines, blowing warm air into their hands.",
            "\"I don't know how anyone can function in this kind of weather, {target}. I feel like I'm in an eternal ice age,\" {initiator} moans, stomping their feet to keep warm.",
            "\"{target}, I can't remember being this cold in my entire life. How do you manage to stay warm in this arctic weather?\" {initiator} asks, teeth chattering.",
            "\"I never thought I would say this, {target}, but I miss the scorching heat of summer. This freezing temperature is too much to handle,\" {initiator} complains, hunching their shoulders.",
            "\"{target}, I've never experienced cold like this before. It's like the chill has seeped into my bones and won't let go,\" {initiator} laments, hugging themselves tightly.",
            "\"{target}, I can't even feel my face anymore. This cold weather is unbearable!\" {initiator} grumbles, wrapping their scarf tighter around their neck.",
            "\"I can't wait for this winter to be over, {target}. I've had enough of this freezing temperature. It's time for some warmth,\" {initiator} sighs, longing for the embrace of summer."
        ]
    },
    "mixer_social_WeatherTemperatureSocials_ComplainAboutCloudyWeather": {
        "pre_actions": [
            "{initiator} complains about the cloudy weather to {target}."
        ],
        "actions": [
            "\"Ugh, this weather is so gloomy, don't you think, {target}?\" {initiator} says, looking up at the cloudy sky.",
            "\"I can't stand these gray and overcast days. They just bring me down,\" {initiator} complains, crossing their arms.",
            "\"Doesn't this constant cloud cover get on your nerves, {target}? I miss the sun,\" {initiator} says with a hint of frustration.",
            "\"It feels like the clouds have been following me around all day. I'm starting to think they have a personal vendetta against me,\" {initiator} jokes, trying to lighten the mood.",
            "\"I wish the sun would make an appearance soon. This cloudy weather is really putting a damper on my mood,\" {initiator} sighs, looking disappointed.",
            "\"I can't help but feel a little bit grumpy with all this grayness around. It's like the weather is mirroring my mood,\" {initiator} grumbles, looking out the window.",
            "\"Is it just me, or does this cloudy weather make everything feel so dreary? I need some sunshine to brighten up my day,\" {initiator} complains, shivering a little.",
            "\"I don't know about you, but this constant cloud cover makes me feel so uninspired. It's like my creativity gets sucked away along with the sunlight,\" {initiator} says, frowning.",
            "\"I was really hoping for a sunny day today. This cloudy weather is just ruining my plans,\" {initiator} complains, sounding a bit disappointed.",
            "\"I can't believe how long it's been since we last saw the sun. This cloudy weather is starting to drive me crazy,\" {initiator} grumbles, rubbing their temples."
        ]
    },
    "mixer_social_AskForMassage_Swedish_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} asks {target} for a Swedish massage."
        ],
        "actions": [
            "\"{target}, I've been feeling really tense lately. Do you think you could give me a Swedish massage?\" {initiator} asks, rubbing their neck.",
            "\"I've heard you give amazing massages, {target}. Would you mind giving me a Swedish massage? I could really use it,\" {initiator} says with a hopeful smile.",
            "\"{target}, I've been thinking about getting a massage lately. Would you be interested in giving me a Swedish massage?\" {initiator} suggests, looking curious.",
            "\"You know, {target}, I've been feeling so stressed lately. Would you be willing to give me a Swedish massage?\" {initiator} asks, looking hopeful.",
            "\"I've been hearing great things about your massage skills, {target}. Do you think you could give me a Swedish massage?\" {initiator} asks, trying to hide their excitement.",
            "\"{target}, I've been dealing with a lot of tension lately. Would you be up for giving me a Swedish massage?\" {initiator} asks, trying to sound relaxed.",
            "\"I've been craving a massage lately, {target}. Would you be able to give me a Swedish massage?\" {initiator} asks, looking hopeful.",
            "\"{target}, I've been feeling so sore lately. Do you think you could give me a Swedish massage?\" {initiator} asks, rubbing their shoulders.",
            "\"You seem to have magical hands, {target}. Would you mind giving me a Swedish massage?\" {initiator} asks, looking hopeful.",
            "\"{target}, I've been hearing great things about your massage skills. Would you be willing to give me a Swedish massage?\" {initiator} asks, trying to hide their nervousness."
        ]
    },
    "mixer_social_AskAboutDay_targeted_Friendly_alwaysOn_Toddler": {
        "pre_actions": [
            "{initiator} asks {target}, who is a toddler, about their day."
        ],
        "actions": [
            "\"Hey there, little one! How was your day?\" {initiator} asks, crouching down to {target}'s level.",
            "\"Did you have a fun day, {target}? Tell me all about it!\" {initiator} says, smiling warmly.",
            "\"Hey buddy, what did you do today? I'm so curious!\" {initiator} asks, with genuine interest in {target}'s response.",
            "\"Hey cutie, did you have a good day? I want to hear all the details!\" {initiator} says, playfully.",
            "\"Hey {target}, what exciting things happened today? I can't wait to hear!\" {initiator} asks, eagerly.",
            "\"Did you have a busy day, {target}? I can't wait to hear about all the things you did!\" {initiator} says, encouragingly.",
            "\"Hey champ, how was your day? I bet it was full of adventure!\" {initiator} says, giving {target} a wink.",
            "\"Hey little one, tell me, what was the best part of your day today?\" {initiator} asks, patiently waiting for {target}'s response.",
            "\"Hey {target}, did anything funny happen today? I'm all ears!\" {initiator} says, chuckling softly.",
            "\"Hey buddy, I missed you today! What did you do while I was away?\" {initiator} asks, excitedly."
        ]
    },
    "mixer_social_AskAboutSchool_targeted_friendly_alwaysOn_child": {
        "pre_actions": [
            "{initiator} asks {target}, who is a child, about how school is going."
        ],
        "actions": [
            "\"So, {target}, how's school going? Making lots of friends?\" {initiator} asks with a warm smile.",
            "\"I'm curious, {target}, how are you finding school? Is it everything you expected?\" {initiator} inquires kindly.",
            "\"Hey {target}, can you tell me about your school? I want to know all about it!\" {initiator} asks excitedly.",
            "\"I hope school is treating you well, {target}. How are your classes going?\" {initiator} asks with genuine interest.",
            "\"Tell me, {target}, what's your favorite subject in school? I'm really curious,\" {initiator} asks, leaning in attentively.",
            "\"Hey {target}, I've been meaning to ask you this - how's school been treating you? Any favorite teachers?\" {initiator} asks, curious to know more.",
            "\"School can be a little overwhelming sometimes, but I'm here if you ever need someone to talk to, {target}. How's it going for you?\" {initiator} asks, offering support.",
            "\"{target}, I'm really interested to know - what's your favorite part about going to school?\" {initiator} asks, eager to hear their response.",
            "\"School can be a rollercoaster, {target}. Care to share any funny or interesting stories with me?\" {initiator} asks, a mischievous twinkle in their eyes.",
            "\"I know school can be tough, {target}, but remember that you're doing great. Anything you want to talk about?\" {initiator} asks, ready to listen."
        ]
    },
    "mixer_social_AskAboutWooHoo_targeted_Friendly_alwaysOn_teen": {
        "pre_actions": [
            "{initiator}, speaking as a teen asks {target}, an adult, about sex."
        ],
        "actions": [
            "\"Um, excuse me, {target}, can I ask you something about... um... sex?\" {initiator} asks nervously, avoiding eye contact.",
            "\"I've been curious about something, {target}, and I thought you might be able to help me understand. Can we talk about sex?\" {initiator} asks tentatively.",
            "\"I know this might be awkward, but as a teenager, I have a lot of questions about sex. Can we have a conversation about it, {target}?\" {initiator} says, blushing.",
            "\"I hope you don't mind me asking, {target}, but I've been wondering about sex lately. Can you share your knowledge with me?\" {initiator} says, feeling a mix of embarrassment and curiosity.",
            "\"{target}, as an adult, I trust your judgment and knowledge. Can we have an open discussion about sex? I have some questions I'd like to ask,\" {initiator} says, trying to sound mature.",
            "\"I know this is a sensitive topic, but I feel comfortable talking to you, {target}. Can we discuss sex and the things I should know?\" {initiator} asks, slightly anxious.",
            "\"Sex is often portrayed differently in the media, {target}, and I'm curious to learn the reality behind it. Can we talk about sex openly?\" {initiator} asks, seeking guidance.",
            "\"I've been hearing a lot of things about sex from friends, {target}, but I want to know the truth. Can you help me navigate through this topic?\" {initiator} asks, looking for guidance.",
            "\"Talking about sex can be uncomfortable, {target}, but as a teenager, I want to be informed. Can we have an honest conversation about it?\" {initiator} says, hoping for understanding.",
            "\"{target}, I feel a bit clueless about sex, but I trust you enough to guide me. Can we have a conversation about it, without any judgment?\" {initiator} asks, seeking guidance."
        ]
    },
    "mixer_social_AskForTypingTips_targeted_Friendly_alwaysOn_child_skill": {
        "pre_actions": [
            "{initiator}, speaking as a child, asks {target}, an adult, for typing tips."
        ],
        "actions": [
            "\"{target}, can you show me how to type properly? I want to be as fast as you!\" {initiator} asks excitedly, holding up their tiny fingers.",
            "\"I wish I could type like you, {target}. Can you teach me the secrets of typing?\" {initiator} asks innocently, looking up at {target}.",
            "\"{target}, do you think you could give me some tips on typing? I want to impress everyone with my skills!\" {initiator} asks, bouncing with enthusiasm.",
            "\"Hey {target}, I noticed you type really fast. Can you teach me how to do it too?\" {initiator} asks, looking up at {target} with admiration.",
            "\"Can you believe it, {target}? I'm just starting to learn how to type. Can you give me some pointers?\" {initiator} asks, eagerly awaiting {target}'s response.",
            "\"{target}, I heard you're the best at typing. Can you share some of your secrets with me?\" {initiator} asks, trying to mimic {target}'s typing posture.",
            "\"{target}, could you do me a favor? Can you teach me how to type like a pro?\" {initiator} asks earnestly, hoping {target} will agree.",
            "\"I want to improve my typing skills, {target}, and I thought maybe you could give me some tips. What do you think?\" {initiator} asks, looking hopeful.",
            "\"{target}, I've been struggling with typing lately. Do you have any suggestions or tips that could help me?\" {initiator} asks, looking for guidance.",
            "\"Hey {target}, do you mind showing me some typing tricks? I want to become a typing wizard!\" {initiator} asks with a mischievous smile."
        ]
    },
    "mixer_social_AskImpossibleRiddle_targeted_mischief_alwaysOn_child_skills": {
        "pre_actions": [
            "{initiator}, speaking as a mischevious child, asks {target}, an adult, to solve an impossible riddle."
        ],
        "actions": [
            "\"Hey {target}, I've got a riddle for you. I bet you can't solve it,\" {initiator} says with a mischievous glint in their eye.",
            "\"Psst, {target}, can you do the impossible? I've got a riddle that will stump even the smartest adults,\" {initiator} whispers excitedly.",
            "\"{target}, I challenge you to solve this riddle. But don't get your hopes up, I've stumped all the adults so far,\" {initiator} taunts playfully.",
            "\"Hey {target}, I've got a riddle that's been puzzling everyone. Wanna give it a try? Think carefully,\" {initiator} suggests, a mischievous smile lingering on their lips.",
            "\"Hey, hey {target}! Can you solve this riddle? I've been asking everyone, but so far no one has cracked it,\" {initiator} says, bouncing on their toes with excitement.",
            "\"Watch out, {target}, I've got a brain teaser that's going to blow your mind! Any takers?\" {initiator} challenges, grinning mischievously.",
            "\"Hey {target}, I've got an impossible riddle for you. Care to take a shot? Be warned, it's left everyone scratching their heads,\" {initiator} teases, eyes twinkling with mischief.",
            "\"Psst, {target}, you want to prove your smarts? I've got a riddle that's practically unsolvable. Think you're up for the challenge?\" {initiator} asks, a sly smirk on their face.",
            "\"Hey {target}, I've got a riddle that's got everyone stumped. But you know, maybe you're different. Wanna give it a go?\" {initiator} challenges, a mischievous glimmer in their eyes.",
            "\"Think you're up for a challenge, {target}? I've got a riddle that's driven grown-ups crazy. Care to test your skills?\" {initiator} asks, barely able to conceal their amusement."
        ]
    },
    "mixer_social_AskToSprayForMonsterUnderBed_Friendly_AlwaysOn_Child": {
        "pre_actions": [
            "{initiator}, speaking as a scared child, asks {target}, an adult, to spray for the monster under their bed."
        ],
        "actions": [
            "\"{target}, can you please, please, spray for the monster under my bed? I'm so scared,\" {initiator} pleads, their voice quivering.",
            "\"I know it sounds silly, but I'm really scared of the monster under my bed. {target}, can you help me?\" {initiator} asks, their eyes wide with fear.",
            "\"Please, {target}, can you spray for the monster under my bed? I can't sleep at night,\" {initiator} says, clutching onto {target}'s arm.",
            "\"I'm too scared to sleep, {target}. Will you please spray for the monster under my bed?\" {initiator} asks, tears welling up in their eyes.",
            "\"{target}, I need your help. There's a monster under my bed, and I'm terrified. Can you spray for it?\" {initiator} asks, their voice trembling.",
            "\"I know it's silly, but I can't shake this fear of the monster under my bed. {target}, can you spray for it?\" {initiator} pleads, looking vulnerable.",
            "\"{target}, I can't sleep because I'm convinced there's a monster under my bed. Can you please spray for it?\" {initiator} asks, their voice shaky.",
            "\"I feel silly asking, but I'm really scared of the monster under my bed. {target}, can you spray for it, please?\" {initiator} asks, biting their lip nervously.",
            "\"Please, {target}, I can't take it anymore. The monster under my bed scares me so much. Will you spray for it?\" {initiator} pleads, their voice filled with desperation.",
            "\"I'm scared to go to sleep, {target}, because of the monster under my bed. Can you spray for it and make it go away?\" {initiator} asks, holding back tears."
        ]
    },
    "mixer_social_BegForNewToys_targeted_friendly_alwaysOn_child": {
        "actions": [
            "\"{target}, can we go to the store and get me some new toys, please?\" {initiator} asks, looking up at {target} with big pleading eyes.",
            "\"I've been really good lately, {target}, can you buy me new toys as a reward?\" {initiator} asks, trying to be persuasive.",
            "\"{target}, my old toys are so boring. Can we go shopping together and find something fun to play with?\" {initiator} asks with excitement.",
            "\"{target}, I saw a commercial on TV for this amazing toy. Can we go to the store and get it?\" {initiator} asks, jumping up and down in anticipation.",
            "\"I really want some new toys, {target}. Can you take me to the toy store and help me pick them out?\" {initiator} asks, hoping for a positive response.",
            "\"Hey {target}, I've been thinking. I haven't gotten new toys in a long time. Can we fix that?\" {initiator} asks, trying to sound casual but also desperate.",
            "\"{target}, I've been doing all my chores without complaining. Can we go to the toy store as a special treat?\" {initiator} asks, hoping to leverage their good behavior.",
            "\"I've been saving up my pocket money, {target}. Can we go to the toy store so I can buy something really cool?\" {initiator} asks, proud of their saving efforts.",
            "\"{target}, can you please buy me some new toys? My friends have been showing off their new stuff and I feel left out,\" {initiator} asks, with a hint of sadness in their voice.",
            "\"{target}, I've been growing so much, and my old toys are all for babies. Can we go get some 'big kid' toys?\" {initiator} asks, emphasizing their desire to feel more grown up."
        ]
    },
    "mixer_social_BragAboutGrades_targeted_Friendly_alwaysOn_child_teen": {
        "pre_actions": [
            "{initiator}, speaking as a self-absorbed teen, brags to {target}, an adult, about their good grades."
        ],
        "actions": [
            "\"You know, {target}, I've been acing all my exams lately. It's like my brain is just on another level,\" {initiator} boasts, rolling their eyes.",
            "\"I don't mean to brag, but my report card is basically a work of art. Straight A's, baby,\" {initiator} says with a smug grin.",
            "\"Hey {target}, guess who's at the top of the class? That's right, yours truly,\" {initiator} boasts, crossing their arms confidently.",
            "\"I bet you'll never guess what my GPA is. Well, let me enlighten you. It's a perfect 4.0,\" {initiator} says, a hint of arrogance in their voice.",
            "\"I know it sounds unbelievable, {target}, but I've managed to maintain a flawless academic record. Not everyone can say that,\" {initiator} says, smirking.",
            "\"You wouldn't believe the grades I've been pulling off, {target}. I'm like a walking academic prodigy,\" {initiator} brags, flipping their hair dismissively.",
            "\"I'm not trying to show off or anything, but let's just say my teachers are always in awe of my academic prowess,\" {initiator} says, shrugging nonchalantly.",
            "\"Can you imagine being as smart as me, {target}? I mean, it's pretty impressive to consistently be at the top of the class,\" {initiator} boasts with a cocky smile.",
            "\"I don't want to make you feel bad or anything, {target}, but my grades are seriously top-notch. It's like I was born to excel academically,\" {initiator} says, feigning modesty.",
            "\"I'm not one to brag, but I'm pretty much the Einstein of our school. My grades speak for themselves,\" {initiator} boasts, raising an eyebrow."
        ]
    },
    "mixer_social_BrightenDay_targeted_friendly_emotionSpecific_toddlerOnly": {
        "pre_actions": [
            "{initiator}, an adult, speaks with {target}, who is a todddler, and brightens their day."
        ],
        "actions": [
            "\"Hey there, little one! How about we play a game together?\" {initiator} says, crouching down to the toddler's level.",
            "\"You have the biggest smile, kiddo! Wanna hear a funny joke?\" {initiator} asks, grinning.",
            "\"Look at those sparkly eyes! How about we go on an adventure together?\" {initiator} suggests, holding out their hand.",
            "\"Guess what? I brought you a surprise! Would you like to see what it is?\" {initiator} says, pulling out a small toy from their pocket.",
            "\"Hi there, cutie pie! How about we build a tower with these colorful blocks?\" {initiator} suggests, pointing at a stack of blocks nearby.",
            "\"You have the most contagious laughter! How about we have a tickle fight?\" {initiator} says, wiggling their fingers playfully.",
            "\"Hey little buddy, how about we read a story together? I have a book full of fun pictures,\" {initiator} says, showing the toddler a colorful book.",
            "\"Look at those adorable little shoes! How about we go for a walk outside and explore the world?\" {initiator} suggests, holding out their hand.",
            "\"You have the sweetest giggle! How about we make silly faces in the mirror?\" {initiator} says, making funny expressions.",
            "\"Hi there, sunshine! How about we have a dance party? I'll put on your favorite song,\" {initiator} suggests, swaying to an imaginary beat."
        ]
    },
    "mixer_social_CallNames_targeted_mean_child": {
        "pre_actions": [
            "{initiator}, speaking as a child, calls {target} mean names."
        ],
        "actions": [
            "\"{target}, you're so stupid!\" {initiator} shouts, crossing their arms and sticking out their tongue.",
            "\"I don't like you, {target}! You're a big meanie!\" {initiator} yells, stamping their foot in frustration.",
            "\"Nobody wants to be friends with you, {target}! You're the worst!\" {initiator} taunts, giving {target} an angry glare.",
            "\"You're a big fat loser, {target}! Nobody likes you!\" {initiator} sneers, making an ugly face.",
            "\"{target}, you're such a crybaby! You always ruin everything!\" {initiator} mocks, laughing cruelly.",
            "\"I hate you, {target}! You're dumb and ugly!\" {initiator} spits out, their voice full of venom.",
            "\"Go away, {target}! Nobody wants you here!\" {initiator} yells, pushing {target} away.",
            "\"{target}, you're a mean, mean person! I wish you were never here!\" {initiator} declares, tears welling up in their eyes.",
            "\"I don't want to be around you, {target}! You're a horrible person!\" {initiator} screams, covering their ears.",
            "\"You're the worst friend ever, {target}! I wish I never met you!\" {initiator} shouts, their voice filled with anger."
        ]
    },
    "mixer_social_ComplainAboutClasses_targeted_Friendly_alwaysOn_child_teen": {
        "pre_actions": [
            "{initiator}, speaking as a petulant teen, complains about their classes to {target}."
        ],
        "actions": [
            "\"{target}, I can't believe how boring my classes are. It's like they're purposely trying to make me hate school,\" {initiator} whines, rolling their eyes.",
            "\"Ugh, {target}, you won't believe the torture I have to endure in my classes. It's a never-ending cycle of monotony,\" {initiator} complains, crossing their arms.",
            "\"I swear, {target}, my classes are the absolute worst. It's like they want to suck the life out of me,\" {initiator} grumbles, slumping in their seat.",
            "\"School is such a waste of time, {target}. I can't believe I have to sit through all these mind-numbing classes,\" {initiator} gripes, letting out an exaggerated sigh.",
            "\"{target}, do you ever feel like school is just a big joke? Because that's exactly how I feel. These classes are a complete joke,\" {initiator} vents, frustration evident in their voice.",
            "\"I'm so fed up with my classes, {target}. It feels like they're designed to make me miserable. Who even comes up with this stuff?\" {initiator} complains, shaking their head.",
            "\"{target}, I can't take it anymore. These classes are sucking the life out of me. It's like they're intentionally trying to make me hate learning,\" {initiator} laments, looking exasperated.",
            "\"{target}, I'm seriously considering dropping out of school. These classes are driving me insane. I can't handle it anymore,\" {initiator} confesses, frustration seeping into their words.",
            "\"I'm surrounded by idiots in my classes, {target}. It's like nobody takes anything seriously. I can't stand it,\" {initiator} vents, throwing their hands up in exasperation.",
            "\"{target}, I feel like I'm wasting my potential in these classes. They're so unchallenging and uninspiring. I need something more,\" {initiator} expresses, a hint of longing in their voice."
        ]
    },
    "mixer_social_ComplainAboutEverything_targeted_Friendly_alwaysOn_teen": {
        "pre_actions": [
            "{initiator}, speaking as a petulant teen, complains about everything that\'s bothering them to {target}."
        ],
        "actions": [
            "\"{target}, I can't believe how unfair everything is right now. It's like the universe is against me,\" {initiator} grumbles, crossing their arms.",
            "\"I swear, {target}, nobody understands me. It's like I'm living in a different world,\" {initiator} complains, rolling their eyes.",
            "\"Ugh, {target}, I can't handle this anymore. Everything is just so frustrating and annoying,\" {initiator} vents, exasperatedly.",
            "\"You know what, {target}? Life just sucks. Nothing ever goes my way,\" {initiator} grumbles, slumping down in their seat.",
            "\"Nobody listens to me, {target}. It's like my opinions don't even matter,\" {initiator} complains, their voice filled with frustration.",
            "\"I'm so tired of all the drama, {target}. Can't we just have one peaceful day?\" {initiator} laments, looking exhausted.",
            "\"Sometimes, {target}, I feel like I'm the only one who sees how messed up everything is,\" {initiator} complains, shaking their head.",
            "\"{target}, I can't stand it when people don't take me seriously. It's like they think I'm a joke,\" {initiator} grumbles, crossing their arms.",
            "\"I hate how everyone expects me to be perfect, {target}. It's like they forget I'm just a human too,\" {initiator} vents, frustration evident in their voice.",
            "\"{target}, I just need someone to understand me. Is that too much to ask for?\" {initiator} complains, looking for validation."
        ]
    },
    "mixer_social_ComplainAboutParents_targeted_Friendly_alwaysOn_teen": {
        "pre_actions": [
            "{initiator}, speaking as a petulant teen, complains about their parents to {target}."
        ],
        "actions": [
            "\"{target}, you won't believe what my parents did this time. They just don't get me,\" {initiator} grumbles, crossing their arms.",
            "\"I swear, {target}, my parents are from another planet. They never listen to me,\" {initiator} complains, rolling their eyes.",
            "\"You know, {target}, sometimes I think my parents are trying to ruin my life. They just don't understand,\" {initiator} vents, frustration evident in their voice.",
            "\"I can't stand my parents, {target}. They're so unreasonable, it's like they enjoy making my life difficult,\" {initiator} complains with a huff.",
            "\"I wish I had different parents, {target}. Mine just don't get me at all,\" {initiator} sighs, looking exasperated.",
            "\"Sometimes I feel like my parents are out to get me, {target}. They're always picking on me for no reason,\" {initiator} grumbles, scowling.",
            "\"Ugh, {target}, my parents are so unfair. They never let me do anything I want,\" {initiator} whines, throwing their hands up in frustration.",
            "\"I'm so fed up with my parents, {target}. They never listen to me and they treat me like a child,\" {initiator} complains, rolling their eyes.",
            "\"{target}, my parents just don't understand me. They're completely clueless about who I am,\" {initiator} laments, shaking their head in disbelief.",
            "\"I don't know how much longer I can handle my parents, {target}. They're always on my case about everything,\" {initiator} grumbles, looking irritated."
        ]
    },
    "mixer_social_DemandIndependence_targeted_mean_teen": {
        "pre_actions": [
            "{initiator}, speaking as a disgruntled angry teen, demands independence from their parent, {target}."
        ],
        "actions": [
            "\"{target}, I'm tired of being treated like a child. I demand to be treated as an independent person,\" {initiator} says, crossing their arms defiantly.",
            "\"I've had enough of your control, {target}. I'm old enough to make my own decisions,\" {initiator} declares, their voice filled with frustration.",
            "\"{target}, I can't live under your rules anymore. I need my independence,\" {initiator} asserts, looking {target} in the eyes.",
            "\"I'm done living by your expectations, {target}. It's time for me to have the freedom to make my own choices,\" {initiator} states, their tone filled with determination.",
            "\"{target}, I'm not a child anymore. I deserve the right to be independent and make my own mistakes,\" {initiator} insists, their voice laced with rebellion.",
            "\"I'm tired of being controlled, {target}. I want the freedom to live my life on my own terms,\" {initiator} says, their frustration evident in their tone.",
            "\"{target}, I need you to understand that I'm capable of taking care of myself. I need my independence,\" {initiator} pleads, their voice tinged with desperation.",
            "\"I can't continue living under your shadow, {target}. I need to break free and find my own path,\" {initiator} expresses, their words filled with determination.",
            "\"{target}, I can't grow and learn if you keep holding me back. I need my independence,\" {initiator} argues, their voice filled with conviction.",
            "\"I'm tired of being treated like a child, {target}. It's time for me to assert my independence and take charge of my own life,\" {initiator} declares, their tone filled with defiance."
        ]
    },
    "mixer_social_DescribeImaginayFriend_Friendly_alwaysOn_child_skills": {
        "pre_actions": [
            "{initiator}, speaking as a young child, describes their current imaginary friend to {target}."
        ],
        "actions": [
            "\"{target}, guess what? I have a secret friend that no one else can see!\" {initiator} exclaims with excitement.",
            "\"I have this amazing friend, {target}, but they're not real. They're just in my imagination,\" {initiator} says, looking at {target} with wide eyes.",
            "\"You know, {target}, I have a special friend who only exists in my mind. They're my best friend,\" {initiator} says, smiling shyly.",
            "\"I have this imaginary friend, {target}, and they're the coolest person I know. They're always there for me,\" {initiator} says, giggling.",
            "\"Can I tell you a secret, {target}? I have this friend who only exists in my imagination. They're like a superhero!\" {initiator} whispers excitedly.",
            "\"You won't believe it, {target}, but I have a secret friend who is invisible. They're my playmate whenever I want,\" {initiator} says, looking around as if searching for their imaginary friend.",
            "\"I have this imaginary friend, {target}, and they're like a magical creature. I wish they were real!\" {initiator} says, dreaming with a wistful look in their eyes.",
            "\"Guess what, {target}? I have a secret friend, and they're like a fairy. They make everything more fun,\" {initiator} says, twirling around with joy.",
            "\"You know, {target}, I have this imaginary friend who is like a talking animal. They're my partner in crime!\" {initiator} says, grinning mischievously.",
            "\"I have a secret friend, {target}, and they're like a ghost. They can go anywhere and do anything!\" {initiator} says, whispering as if sharing a thrilling secret."
        ]
    },
    "mixer_social_EnthuseAboutCandy_targeted_Friendly_alwaysOn_child": {
        "pre_actions": [
            "{initiator}, speaking as a young child, obsessively enthuses about their love for candy to {target}."
        ],
        "actions": [
            "\"{target}, you won't believe how much I love candy! It's like my favorite thing in the whole world,\" {initiator} exclaims excitedly.",
            "\"I have a secret, {target}, and it's about my love for candy. I can't stop thinking about it!\" {initiator} says, unable to contain their enthusiasm.",
            "\"You know what, {target}? Candy is the best thing ever! I could eat it all day, every day,\" {initiator} says, eyes shining with excitement.",
            "\"I have a confession to make, {target}. I'm absolutely obsessed with candy! It's like my own little world of sweetness,\" {initiator} confesses with a wide grin.",
            "\"{target}, do you know what makes me the happiest? Candy! I can talk about it for hours and never get tired,\" {initiator} says, bouncing with excitement.",
            "\"I have a secret addiction, {target}, and it's called candy. I just can't resist its sugary goodness,\" {initiator} admits with a mischievous smile.",
            "\"You're my best friend, {target}, so I have to tell you something. I'm head over heels in love with candy!\" {initiator} declares passionately.",
            "\"I have a special bond with candy, {target}. It's like we were meant to be together. I can't help but gush about it,\" {initiator} says, eyes sparkling with joy.",
            "\"{target}, I have a confession to make. Candy is my weakness. It's like a magical spell that I can't resist,\" {initiator} admits, blushing slightly.",
            "\"You know what, {target}? Candy is my ultimate happiness. Just thinking about it brings a smile to my face,\" {initiator} says, unable to hide their delight."
        ]
    },
    "mixer_social_ExchangePromiseRings_targeted_romance_relationship_teen": {
        "pre_actions": [
            "{initiator}, a teen, exchanges promise rings with {target}, who is also a teen."
        ],
        "actions": [
            "\"Hey {target}, I brought something special for us. Promise rings,\" {initiator} says, holding out two small boxes.",
            "\"I've been thinking a lot about us lately, and I wanted to give you something to show how much you mean to me,\" {initiator} says, nervously handing {target} the box.",
            "\"I know we're young, but I believe in us. These promise rings are a symbol of my commitment to you,\" {initiator} says, blushing.",
            "\"I've been saving up for a while to get these promise rings. I want us to have something tangible to remind us of our love,\" {initiator} explains, eagerly opening the box.",
            "\"I hope you like it, {target}. I got us matching promise rings as a token of my love and devotion to you,\" {initiator} says, smiling shyly.",
            "\"I know it might seem cheesy, but I couldn't help myself. These promise rings are a way for me to show you how serious I am about our relationship,\" {initiator} says, biting their lip.",
            "\"I've been thinking about our future together, and I wanted to take the next step. These promise rings symbolize my commitment to you,\" {initiator} says, holding {target}'s hand.",
            "\"I know we're still young, but I believe in us. These promise rings are a promise that I'll always be there for you,\" {initiator} says, looking into {target}'s eyes.",
            "\"I wanted to give you something that would remind you of my love even when we're apart. These promise rings are my way of doing that,\" {initiator} says, nervously twisting the ring in their hand.",
            "\"I hope you like it, {target}. This promise ring is a symbol of my love for you. It's a promise that I'll always be faithful and true,\" {initiator} says, blushing."
        ]
    },
    "mixer_social_Flirt_targeted_romance_alwaysOn_teen": {
        "pre_actions": [
            "{initiator}, speaking as a teen, flirts with {target}, who is also a teen."
        ],
        "actions": [
            "\"Hey {target}, I couldn't help but notice how amazing you look today,\" {initiator} says with a playful smile.",
            "\"You know, {target}, we make a pretty great team. Maybe we should consider being more than just friends,\" {initiator} suggests, winking.",
            "\"I've been meaning to ask you, {target}, are you a magician? Because whenever I'm around you, everyone else disappears,\" {initiator} says, blushing.",
            "\"Hey {target}, do you believe in love at first sight? Or should I walk by again?\" {initiator} says, trying to be smooth.",
            "\"I must be a snowflake, because I've fallen for you, {target},\" {initiator} says, trying to impress.",
            "\"Is it hot in here or is it just you, {target}?\" {initiator} asks flirtatiously, making {target} blush.",
            "\"Hey {target}, do you have a map? Because I just got lost in your eyes,\" {initiator} says with a flirty grin.",
            "\"You know, {target}, they say beauty is in the eye of the beholder, and I must say, you're the most beautiful person I've ever seen,\" {initiator} compliments, blushing.",
            "\"I can't help but feel a spark between us, {target}. Is it just me, or do you feel it too?\" {initiator} asks, leaning in closer.",
            "\"Hey {target}, I have a secret to share with you. I think I might be falling for you,\" {initiator} confesses with a shy smile."
        ]
    },
    "mixer_Social_GetToKnow_Friendly_STC_TargetToddler": {
        "pre_actions": [
            "{initiator} attempts to get to know {target}, who is a toddler."
        ],
        "actions": [
            "\"Hi there, little one! My name is {initiator}. What's your name?\" {initiator} asks, crouching down to the toddler's level.",
            "\"Hey, kiddo! Do you want to play with me?\" {initiator} asks, holding out a toy.",
            "\"Wow, you're so cute! Can you show me your favorite toy?\" {initiator} says, smiling warmly at the toddler.",
            "\"Hey, buddy! How about we go on an adventure together? Where should we explore?\" {initiator} asks, gesturing for the toddler to come closer.",
            "\"Hi, sweetie! I heard you like animals. Want to tell me about your favorite animal?\" {initiator} asks, making animal noises to grab the toddler's attention.",
            "\"Hey there, little buddy! Can you teach me how to play this game?\" {initiator} asks, pointing to a game the toddler is playing with.",
            "\"Hi, cutie! I love your outfit. Can you show me your favorite toy?\" {initiator} says, complimenting the toddler and extending a hand.",
            "\"Hello, little one! I heard you're really good at building blocks. Can you show me how you do it?\" {initiator} asks, pointing to a stack of blocks nearby.",
            "\"Hey, champ! I bet you're great at hide-and-seek. Do you want to play with me?\" {initiator} asks, peeking behind furniture playfully.",
            "\"Hey, little buddy! I've got a surprise for you. Can you come over here and see what it is?\" {initiator} says, holding a small gift for the toddler."
        ]
    },
    "mixer_social_GiveTheWooHooTalk_targeted_friendly_alwaysOn_teen": {
        "pre_actions": [
            "{initiator} talks to teenage {target} about sex for the first time."
        ],
        "actions": [
            "\"So, {target}, I think it's time we have a serious conversation about a topic that may make us both feel a bit uncomfortable,\" {initiator} says, sitting down next to {target} with hesitation.",
            "\"I know this might be a difficult subject to discuss, {target}, but it's important that we talk about it. Are you ready?\" {initiator} asks, looking at {target} with concern.",
            "\"You're growing up, {target}, and there's something I think we need to discuss. It's about sex,\" {initiator} says, choosing their words carefully.",
            "\"I've been thinking a lot about how much you're growing up, {target}. And I think it's time we had a conversation about a crucial topic: sex,\" {initiator} says, trying to sound calm.",
            "\"I know it might be awkward, {target}, but we need to talk about sex. It's an important part of life, and I want you to be informed,\" {initiator} says, mustering up the courage.",
            "\"You're reaching an age where it's important for us to have a conversation about sex, {target}. It might be a bit uncomfortable, but it's necessary,\" {initiator} says, trying to sound reassuring.",
            "\"Hey, {target}, I've been doing a lot of thinking lately, and I think it's time we address the elephant in the room: sex,\" {initiator} says, looking slightly embarrassed.",
            "\"I've been meaning to talk to you about this for a while, {target}, but I didn't know how to approach it. Let's have a conversation about sex,\" {initiator} says, taking a deep breath.",
            "\"{target}, I think it's time we had a serious talk. It's about a topic that might make both of us uncomfortable, but it's necessary: sex,\" {initiator} says, trying to sound gentle.",
            "\"I hope you're open to having an honest conversation, {target}, because today we're going to talk about something that can be quite sensitive: sex,\" {initiator} says, looking {target} in the eye."
        ]
    },
    "mixer_social_HackIntoCoworkersEmail_targeted_friendly_alwaysOn_prank": {
        "pre_actions": [
            "{initiator} pranks hacks {target} by hacking into their e-mail."
        ],
        "actions": [
            "\"{target}, you'll never believe what I just did. Check your e-mail,\" {initiator} chuckles mischievously.",
            "\"Hey {target}, I may have done something a little sneaky. Can you please check your e-mail?\" {initiator} says with a grin.",
            "\"Guess what, {target}? I managed to hack into your e-mail. You might want to take a look,\" {initiator} says, barely containing their excitement.",
            "\"I couldn't resist pulling a little prank on you, {target}. Check your e-mail, and you'll see what I mean,\" {initiator} says, unable to hide their amusement.",
            "\"Remember that time you pranked me? Well, consider this payback. Check your e-mail now,\" {initiator} says, a mischievous glint in their eyes.",
            "\"I may have played a little trick on you, {target}. Check your e-mail and see what I did,\" {initiator} says, grinning from ear to ear.",
            "\"Wanna know what I just did, {target}? Check your e-mail, and prepare to be surprised,\" {initiator} says, unable to contain their laughter.",
            "\"{target}, I couldn't resist pulling off a little stunt. Go check your e-mail, and you'll understand,\" {initiator} says, a playful tone in their voice.",
            "\"Hey, {target}, did you see your e-mail yet? I may have gotten a little creative,\" {initiator} says, trying to hide their amusement.",
            "\"You won't believe what I did, {target}. Check your e-mail, and you'll see the aftermath of my prank,\" {initiator} says, chuckling softly."
        ]
    },
    "mixer_social_HighFive_targeted_friendly_alwaysOn_teen": {
        "pre_actions": [
            "{initiator}, a teen, gives a high five to {target}."
        ],
        "actions": [
            "{initiator} excitedly jumps up and slaps a high five with {target}.",
            "\"Wow, {target}, that was an incredible move! High five!\" {initiator} exclaims with a grin.",
            "As {target} looks surprised, {initiator} throws their hand up in the air and says, \"Come on, give me a high five! That was awesome!\"",
            "{initiator} gives {target} a high five, a huge smile spreading across their face.",
            "With a burst of energy, {initiator} extends their hand towards {target}, saying, \"Nice job! Give me a high five!\"",
            "Feeling accomplished, {initiator} slaps a high five with {target} and says, \"We make a great team!\"",
            "{initiator} looks at {target} and extends their hand, waiting for a high five.",
            "Filled with enthusiasm, {initiator} raises their hand towards {target} and says, \"Let's celebrate with a high five!\"",
            "Seeing {target}'s impressive achievement, {initiator} quickly offers a high five, saying, \"That was incredible!\"",
            "With a sense of camaraderie, {initiator} taps their hand against {target}'s hand, saying, \"You're amazing! High five!\""
        ]
    },
    "mixer_social_IsTheMoonABanana_targeted_Friendly_alwaysOn_child_skills": {
        "pre_actions": [
            "{initiator}, being a silly young child, asks {target} if the moon is a banana."
        ],
        "actions": [
            "\"Hey {target}, do you think the moon is actually a giant banana?\" {initiator} asks with a mischievous grin.",
            "\"I've been thinking about this for a while now, {target}, and I need your opinion. Is it possible that the moon is just a really big banana?\" {initiator} wonders aloud.",
            "\"You know, {target}, I had the craziest idea today. What if the moon is secretly a banana in disguise?\" {initiator} suggests with a giggle.",
            "\"{target}, I have a silly question for you. Have you ever considered the possibility that the moon might actually be a banana?\" {initiator} asks, unable to contain their curiosity.",
            "\"Okay, hear me out, {target}. What if, just what if, the moon is not a moon at all but a gigantic banana floating in space?\" {initiator} proposes, looking expectantly at {target}.",
            "\"I know this sounds ridiculous, {target}, but I can't help but wonder if the moon is a banana. What do you think?\" {initiator} asks, looking genuinely intrigued.",
            "\"So, {target}, I had this wild thought. What if the moon is a banana, and we just haven't discovered it yet?\" {initiator} ponders, eyes wide with excitement.",
            "\"Hey {target}, I need your input on something. What are the chances that the moon is secretly a massive banana?\" {initiator} questions with a playful tone.",
            "\"I bet you've never heard this theory before, {target}, but what if the moon is actually a banana that's been orbiting the Earth all this time?\" {initiator} suggests, unable to contain their enthusiasm.",
            "\"{target}, this might sound silly, but have you ever considered the possibility that the moon is a banana? I can't get the idea out of my head,\" {initiator} confesses, looking slightly embarrassed."
        ]
    },
    "mixer_social_IsTheMoonAnEgg_Friendly_alwaysOn_child_skills": {
        "pre_actions": [
            "{initiator}, being a silly young child, asks {target} if the moon is an egg."
        ],
        "actions": [
            "\"{target}, I have a really important question for you. Do you think the moon is actually an egg?\" {initiator} asks, wide-eyed with curiosity.",
            "\"I've been thinking about this for a while now, {target}, and I need your opinion. What if the moon is secretly an egg?\" {initiator} ponders, looking at {target} with anticipation.",
            "\"{target}, I have a crazy theory. What if the moon is not just a celestial body, but actually a giant egg? Can you imagine?\" {initiator} asks, giggling with excitement.",
            "\"{target}, I have a question that might sound silly, but I can't help but wonder. Do you think it's possible that the moon is an egg?\" {initiator} asks, raising an eyebrow and waiting for a response.",
            "\"I've been watching the moon lately, {target}, and I can't shake this idea. What if the moon is actually an egg about to hatch?\" {initiator} wonders aloud, looking at {target} with curiosity.",
            "\"{target}, I know this might sound strange, but bear with me. Have you ever considered the possibility that the moon is an egg waiting to hatch?\" {initiator} asks, biting their lip nervously.",
            "\"Hey {target}, random question. Do you think the moon could be an egg? I've been thinking about it a lot, and I'm curious about your thoughts,\" {initiator} asks, unable to contain their excitement.",
            "\"{target}, I have this wild theory, and I need to share it with someone. What if the moon is actually a giant egg? Do you think it's possible?\" {initiator} asks, eyes shining with anticipation.",
            "\"Okay, {target}, I have a question that might make you laugh. But seriously, what if the moon is an egg? Just imagine,\" {initiator} says with a mischievous grin, waiting for {target}'s reaction.",
            "\"{target}, I have this crazy idea that's been bugging me. What if the moon is not a moon at all, but an enormous egg? Can you imagine the possibilities?\" {initiator} asks, excitement bubbling in their voice."
        ]
    },
    "mixer_social_IsTheMoonASponge_targeted_Friendly_alwaysOn_child_skills": {
        "pre_actions": [
            "{initiator}, being a silly young child, asks {target} if the moon is actually a sponge."
        ],
        "actions": [
            "\"{target}, I have a really important question for you. Is the moon actually a sponge?\" {initiator} asks, looking up at {target} with wide eyes.",
            "\"I've been thinking about this for a while, {target}. Do you think the moon is secretly a giant sponge?\" {initiator} wonders aloud, looking curious.",
            "\"You know, {target}, I've been pondering something. What if the moon is just a really big sponge? What do you think?\" {initiator} asks, tilting their head.",
            "\"I have a theory, {target}. What if the moon is actually a sponge? It would explain so much,\" {initiator} says, looking excited to share their idea.",
            "\"Hey {target}, I have a question that's been bugging me. Is it possible that the moon is a massive sponge?\" {initiator} asks, looking genuinely curious.",
            "\"{target}, I need your expertise on this matter. Could the moon be a sponge? It's been on my mind lately,\" {initiator} says, scratching their head.",
            "\"I've been wondering about something, {target}. Do you think the moon could be made of sponge? It sounds crazy, but hear me out,\" {initiator} suggests, looking earnest.",
            "\"{target}, I have a silly question for you. Is it just me, or does the moon look like a giant sponge sometimes?\" {initiator} asks with a mischievous grin.",
            "\"Okay, {target}, I have a wild idea. What if the moon is secretly a sponge that absorbs all the light?\" {initiator} suggests, looking excited to hear {target}'s thoughts.",
            "\"{target}, I can't help but wonder. Is it possible that the moon is actually a massive sponge floating in space?\" {initiator} asks, looking both curious and amused."
        ]
    },
    "mixer_social_IsTheMoonCheese_targeted_Friendly_alwaysOn_child_skills": {
        "pre_actions": [
            "{initiator}, being a silly young child, asks {target} if the moon is actually cheese."
        ],
        "actions": [
            "\"Hey {target}, I have a really important question for you. Is the moon made of cheese?\" {initiator} asks with wide-eyed curiosity.",
            "\"I've been wondering about this for so long, {target}. Do you think the moon is actually made of cheese?\" {initiator} asks, looking at {target} expectantly.",
            "\"Mom told me it's just a saying, but I can't help but wonder, {target}. Is it possible that the moon is made of cheese?\" {initiator} asks, tilting their head to the side.",
            "\"I know it sounds silly, but I can't stop thinking about it. {target}, do you think there's a chance the moon could be made of cheese?\" {initiator} asks, unable to contain their excitement.",
            "\"I've been reading this book about the moon, and it got me thinking, {target}. Could it be true that the moon is actually made of cheese?\" {initiator} asks, their voice filled with wonder.",
            "\"I asked my teacher, but she just laughed. {target}, do you think it's possible that the moon is secretly made of cheese?\" {initiator} asks, looking for reassurance.",
            "\"{target}, I need your help settling a debate. Some kids at school say the moon is made of cheese. What do you think?\" {initiator} asks, eager to hear {target}'s opinion.",
            "\"I know it's a silly question, but it's been bugging me for days. {target}, do you think there's any chance the moon could be made of cheese?\" {initiator} asks, hoping for an answer.",
            "\"I've been watching documentaries about space, and now I can't stop wondering. {target}, what if the moon is secretly made of cheese?\" {initiator} asks, their imagination running wild.",
            "\"I know it sounds ridiculous, but I can't help but wonder. {target}, have you ever thought about the possibility that the moon might be made of cheese?\" {initiator} asks, looking for someone to share their curiosity."
        ]
    },
    "mixer_social_KissNeck_targeted_romance_relationship_teen": {
        "pre_actions": [
            "{initiator}, a teen, silently kisses teenage {target}'s neck sensually."
        ],
        "actions": [
            "\"{target}, I've been wanting to do this for a while now,\" {initiator} says, their voice barely a whisper, as they gently kiss {target}'s neck.",
            "The atmosphere becomes charged as {initiator} leans in and plants a soft, lingering kiss on {target}'s neck, sending shivers down their spine.",
            "In that moment, {initiator} musters up the courage to lean in and kiss {target}'s neck, their lips leaving a trail of warmth behind.",
            "As {initiator} places a delicate, sensual kiss on {target}'s neck, a rush of emotions fills the air between them.",
            "With a mix of nervousness and longing, {initiator} leans closer and presses their lips against {target}'s neck, their heart pounding in their chest.",
            "The touch of {initiator}'s lips against {target}'s neck sends a jolt of electricity through both of them, a silent confession of desire.",
            "In the quiet intimacy of the moment, {initiator} surprises {target} by softly kissing their neck, their heart racing with anticipation.",
            "As {initiator} leans in to kiss {target}'s neck, a flicker of vulnerability crosses their face, uncertain of how {target} will react.",
            "With a bold yet gentle move, {initiator} brings their lips to {target}'s neck, silently expressing a depth of affection that words cannot capture.",
            "The world around them fades away as {initiator} leans in and kisses {target}'s neck, a secret moment shared between two hearts."
        ]
    },
    "mixer_social_LectureAboutGrades_targeted_Friendly_alwaysOn_child_teen": {
        "pre_actions": [
            "{initiator} sternly lectures their child, {target} about their grades."
        ],
        "actions": [
            "\"{target}, we need to have a serious talk about your grades. Sit down,\" {initiator} says, their voice firm.",
            "\"I've been looking at your report card, {target}, and we need to address your grades immediately,\" {initiator} says with a concerned expression.",
            "\"Your grades have been slipping, {target}, and it's about time we had a serious discussion about it,\" {initiator} says, crossing their arms.",
            "\"I've been patient, {target}, but your grades are unacceptable. We need to discuss this right now,\" {initiator} says, their voice strict.",
            "\"It's time we had a serious conversation about your academic performance, {target}. I expect better from you,\" {initiator} says, their tone serious.",
            "\"We have a problem, {target}, and it's your grades. Let's sit down and figure out a solution,\" {initiator} says, motioning for {target} to join them.",
            "\"It's time to address the elephant in the room, {target}, your grades. Let's talk,\" {initiator} says, their voice firm.",
            "\"We need to talk about your grades, {target}, and come up with a plan to improve them. Sit down,\" {initiator} says, gesturing towards a chair.",
            "\"I've noticed a decline in your academic performance, {target}, and it's time we discuss the consequences,\" {initiator} says, their expression serious.",
            "\"The time for excuses is over, {target}. We need to have a serious conversation about your plummeting grades,\" {initiator} says sternly."
        ]
    },
    "mixer_social_LectureAboutMisbehavior_mean_targeted_alwaysOn_child": {
        "pre_actions": [
            "{initiator} spitefully lectures their child, {target} about their misbehavior."
        ],
        "actions": [
            "\"{target}, we need to have a serious talk about your behavior. Sit down,\" {initiator} says sternly.",
            "\"I've had enough of your constant misbehavior, {target}. It's time for us to address it,\" {initiator} says with a firm voice.",
            "\"I can't believe you would act like this, {target}. We need to have a serious conversation about your actions,\" {initiator} says, anger evident in their voice.",
            "\"{target}, I've been noticing a pattern of misbehavior from you, and it's time we discuss it,\" {initiator} says, their voice tinged with disappointment.",
            "\"I've been meaning to talk to you about your recent behavior, {target}. It's important that we address it,\" {initiator} says, trying to keep their frustration in check.",
            "\"{target}, your behavior has been unacceptable, and I can't let it slide anymore. We need to talk,\" {initiator} says, their tone indicating their seriousness.",
            "\"I've been patient with you for a long time, {target}, but your misbehavior has reached its limit. We need to have a serious conversation,\" {initiator} says, their voice filled with frustration.",
            "\"{target}, I've been observing your actions and I can't stay silent anymore. We need to discuss your misbehavior,\" {initiator} says, their tone strict.",
            "\"I've seen how you've been acting lately, {target}, and it's time we have a conversation about your misbehavior,\" {initiator} says, their voice laced with concern.",
            "\"{target}, we need to address your misbehavior. It's time for us to have a serious talk,\" {initiator} says, their voice firm and determined."
        ]
    },
    "mixer_social_LectureAboutResponsibilities_targeted_Friendly_alwaysOn_teen": {
        "pre_actions": [
            "{initiator} sternly lectures their child, {target} about their responsibilities."
        ],
        "actions": [
            "\"{target}, we need to have a serious talk about your responsibilities. Sit down, please,\" {initiator} says with a stern tone.",
            "\"I've noticed that you've been slacking off on your responsibilities lately, {target}. We need to address this,\" {initiator} says firmly.",
            "\"Listen up, {target}. It's time we have a serious discussion about your responsibilities. This is important,\" {initiator} says, looking directly into {target}'s eyes.",
            "\"Enough is enough, {target}. I can't let you continue neglecting your responsibilities. We need to talk about this,\" {initiator} says with a stern expression.",
            "\"You may not like what I'm about to say, {target}, but it's time for a lecture on your responsibilities. This is non-negotiable,\" {initiator} says, crossing their arms.",
            "\"I hope you're ready for a serious conversation, {target}, because we need to address your lack of responsibility,\" {initiator} says, their voice firm.",
            "\"Sit down, {target}. We need to have a talk about your responsibilities. This is not up for discussion,\" {initiator} says, gesturing for {target} to take a seat.",
            "\"Listen carefully, {target}. I'm about to lay out your responsibilities, and I expect you to take them seriously,\" {initiator} says, their tone strict.",
            "\"I've been patient for long enough, {target}, but now it's time for a lecture on your responsibilities. This is for your own good,\" {initiator} says, looking determined.",
            "\"I'm disappointed in your lack of responsibility, {target}. We need to have a serious discussion about this, right now,\" {initiator} says, their voice tinged with frustration."
        ]
    },
    "mixer_social_MakeBelieve_targeted_friendly_alwaysOn_child": {
        "pre_actions": [
            "{initiator}, speaking as a young child, plays make believe with {target}."
        ],
        "actions": [
            "\"Hey {target}, let's pretend we're astronauts exploring a distant galaxy!\" {initiator} exclaims, excitement sparkling in their eyes.",
            "\"I have an idea, {target}! Let's pretend we're pirates searching for buried treasure on a desert island,\" {initiator} suggests, a mischievous grin on their face.",
            "\"Look, {target}! I found a magic wand! Let's pretend we're wizards and cast spells on everything around us,\" {initiator} says, waving an imaginary wand in the air.",
            "\"I want to be a superhero, {target}! Let's pretend we have special powers and save the world from evil villains,\" {initiator} declares, striking a superhero pose.",
            "\"Let's pretend we're in a fairytale, {target}! I'll be the brave knight and you can be the princess we need to rescue,\" {initiator} suggests, twirling around in excitement.",
            "\"Can we pretend to be animals, {target}? I'll be a lion and you can be a monkey swinging from tree to tree,\" {initiator} suggests, crawling on all fours.",
            "\"Let's play pretend, {target}! I'll be a famous chef and you can be my sous chef helping me cook delicious meals,\" {initiator} says, wearing an imaginary chef's hat.",
            "\"Look, {target}! I found a magical portal. Let's pretend we're traveling through time and visiting different historical eras,\" {initiator} suggests, pointing at an imaginary portal.",
            "\"I want to be a famous rock star, {target}! Let's pretend we're performing on a big stage with thousands of fans cheering for us,\" {initiator} says, grabbing an imaginary microphone.",
            "\"Let's pretend we're in a world of dinosaurs, {target}! I'll be a fearless paleontologist and you can be my trusty dinosaur companion,\" {initiator} suggests, mimicking dinosaur roars."
        ]
    },
    "mixer_social_MakeFunOfAdults_targeted_funny_alwaysOn_child": {
        "pre_actions": [
            "{initiator}, speaking as a young child, makes fun of adults with {target}, who is also a child."
        ],
        "actions": [
            "\"{target}, look at them! They're so boring and serious all the time,\" {initiator} giggles, pointing at the adults.",
            "\"Do you think they even remember what it's like to have fun?\" {initiator} asks, nudging {target} playfully.",
            "\"{target}, let's pretend to be grown-ups and act all serious. Watch how silly we can make it,\" {initiator} suggests mischievously.",
            "\"I bet we could come up with way cooler ideas than they ever could,\" {initiator} says confidently, rolling their eyes at the adults.",
            "\"{target}, let's make up funny names for all the adults. I'll start with Mr. Grumpy Pants over there,\" {initiator} whispers, trying not to burst into laughter.",
            "\"{target}, do you think the adults even remember what it's like to laugh and play like we do?\" {initiator} wonders out loud.",
            "\"Hey {target}, let's show the adults how to have real fun. They could use a lesson or two,\" {initiator} suggests, grinning mischievously.",
            "\"Do you think the adults ever wish they could be kids again? I know I do,\" {initiator} says, looking at {target} with curiosity.",
            "\"{target}, I bet we could come up with a game that's way more fun than anything the adults could think of,\" {initiator} says excitedly.",
            "\"Hey {target}, let's pretend to be adults and see if we can do a better job at being serious,\" {initiator} suggests, trying hard not to burst into laughter."
        ]
    },
    "mixer_social_MeetInfant_Child_Greetings": {
        "pre_actions": [
            "{initiator}, speaking as a young child, meets infant {target} for the first time."
        ],
        "actions": [
            "\"{target}, are you my new baby brother/sister? Wow, you're so tiny!\" {initiator} exclaims with wide eyes.",
            "\"Mommy/Daddy, who is this little baby? Can I hold him/her?\" {initiator} asks, looking at {target} curiously.",
            "\"{target}, you're so small and cute! I promise to protect you and be the best big sibling ever,\" {initiator} says, gently touching {target}'s tiny hand.",
            "\"{target}, can you understand me? I'm {initiator}, your big brother/sister. We're going to have so much fun together!\" {initiator} says, grinning from ear to ear.",
            "\"{target}, I can't believe you're finally here! I've been waiting for you for so long. Let's be best friends, okay?\" {initiator} says, reaching out to touch {target}'s cheek.",
            "\"{target}, you're such a tiny baby. Do you want to play with my toys? I'll share them with you,\" {initiator} offers, showing {target} their favorite toys.",
            "\"{target}, I think you're the cutest baby I've ever seen. Can I give you a hug?\" {initiator} asks, leaning in with arms open wide.",
            "\"{target}, I'm {initiator}, and I'm going to be your big brother/sister. I'll teach you everything I know and protect you always,\" {initiator} says, looking determined.",
            "\"{target}, you're so little! Can I help take care of you? I promise to be gentle,\" {initiator} says, looking at {target} with a caring expression.",
            "\"{target}, I'm so excited to meet you! Can we be best friends forever?\" {initiator} asks, looking at {target} with anticipation."
        ]
    },
    "mixer_social_MockSimsMood_targeted_mean_alwaysOn_child_skills": {
        "pre_actions": [
            "{initiator}, speaking as a young child, mocks {target}'s mood."
        ],
        "actions": [
            "\"Hey {target}, why are you so grumpy?\" {initiator} says with a mischievous grin.",
            "\"You look like a sad puppy, {target}! What's wrong?\" {initiator} teases, giggling.",
            "\"You're so boring, {target}! Lighten up and have some fun,\" {initiator} says, imitating {target}'s serious expression.",
            "\"Is someone in a bad mood today? {target}, you're acting like a grumpy old man,\" {initiator} says, laughing playfully.",
            "\"Cheer up, {target}! You're bringing down the whole room with your gloomy face,\" {initiator} says, pretending to pout.",
            "\"I bet I can make you smile, {target}. You look like you need it,\" {initiator} says, attempting to imitate {target}'s mood.",
            "\"Wow, {target}, you're the moodiest person I know. What's got your panties in a twist?\" {initiator} says, unable to contain their laughter.",
            "\"Why so serious, {target}? It's not the end of the world,\" {initiator} says, mimicking {target}'s serious tone.",
            "\"Look at you, {target}, with that grumpy face. Did you wake up on the wrong side of the bed?\" {initiator} says, teasingly.",
            "\"Hey {target}, what's with the long face? Did someone steal your smile?\" {initiator} says, trying to provoke a reaction."
        ]
    },
    "mixer_social_MonkeyAround_targeted_mischief_alwaysOn_child": {
        "pre_actions": [
            "{initiator}, speaking as a young child, monkeys around with {target}."
        ],
        "actions": [
            "\"{target}, come play with me! Let's pretend to be monkeys swinging from trees!\" {initiator} giggles, reaching out to grab {target}'s hand.",
            "\"Look, {target}! I can climb this tree just like a monkey! Watch me!\" {initiator} exclaims, scrambling up a low-hanging branch.",
            "\"Hey {target}, let's have a monkey race! Whoever reaches that tree first wins!\" {initiator} challenges, pointing to a tree in the distance.",
            "\"{target}, do you want to be the mama monkey or the baby monkey? Let's play pretend!\" {initiator} asks, bouncing up and down with excitement.",
            "\"Watch this, {target}! I can swing from this branch just like a monkey! Wheee!\" {initiator} shouts, swinging back and forth.",
            "\"Let's make monkey noises together, {target}! Ooh ooh ah ah!\" {initiator} says, imitating the sound of a monkey and waiting for {target} to join in.",
            "\"Look, {target}! I found a banana! Let's pretend to be monkeys and eat it together!\" {initiator} suggests, holding up a pretend banana.",
            "\"Hey {target}, do you think monkeys can do cartwheels? Let's try it together!\" {initiator} suggests, attempting to do a cartwheel and stumbling.",
            "\"Come on, {target}! Let's see who can hang from the monkey bars the longest! Ready, set, go!\" {initiator} challenges, running towards the playground.",
            "\"Let's play a game of monkey see, monkey do, {target}! I'll go first, and then you have to copy me!\" {initiator} says, striking a silly pose."
        ]
    },
    "mixer_social_NPC_AskToHangOut_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} asks {target} to hang out with them."
        ],
        "actions": [
            "\"Hey {target}, I was wondering if you wanted to hang out sometime?\" {initiator} asks, a hint of excitement in their voice.",
            "\"I've been wanting to do something fun, and I thought it would be great to hang out with you. What do you say, {target}?\" {initiator} suggests, looking hopeful.",
            "\"I know we don't really know each other that well, but I thought it would be cool if we could hang out sometime. What do you think, {target}?\" {initiator} asks, a little nervous.",
            "\"I've been looking for someone to go to this event with me, and I thought you might be interested. Would you like to hang out, {target}?\" {initiator} proposes, keeping their fingers crossed.",
            "\"I've heard about this new place in town, and I thought it would be fun to check it out together. Are you up for hanging out, {target}?\" {initiator} suggests, trying to sound casual.",
            "\"I've been feeling a bit bored lately, and I thought it would be great to have some company. Would you be interested in hanging out, {target}?\" {initiator} asks, hoping for a positive response.",
            "\"I know we haven't really had the chance to spend much time together, but I thought it would be nice to hang out. What do you say, {target}?\" {initiator} asks, trying to sound inviting.",
            "\"I've got tickets to this concert and I was wondering if you'd like to come with me. It'll be a lot more fun if we hang out, don't you think, {target}?\" {initiator} suggests, a smile on their face.",
            "\"I've been craving some good company, and I immediately thought of you. Would you be interested in hanging out sometime, {target}?\" {initiator} asks, hoping for a positive response.",
            "\"I've been wanting to explore this new hiking trail, and I thought it would be great if we could hang out and do it together. Are you up for it, {target}?\" {initiator} proposes, sounding enthusiastic."
        ]
    },
    "mixer_social_PopCultureReference_tareted_Friendly_alwaysOn_child_skills": {
        "pre_actions": [
            "{initiator}, a young child, makes a pop culture reference to {target}."
        ],
        "actions": [
            "\"{target}, have you seen that new movie everyone's talking about? It's so cool!\" {initiator} says with excitement, hoping {target} will share their enthusiasm.",
            "\"I heard this song on the radio, {target}, and it made me think of you. Do you know it?\" {initiator} asks, eager to discuss the latest hit with {target}.",
            "\"Hey {target}, have you read that book series everyone's obsessed with? I can't wait to talk to someone about it!\" {initiator} exclaims, hoping {target} is a fellow fan.",
            "\"{target}, I have to ask, have you seen that show that everyone's binge-watching? I want to know what you think!\" {initiator} says, hoping to bond with {target} over their shared interest.",
            "\"I can't stop playing this new video game, {target}. Have you played it too? We should team up!\" {initiator} suggests, hoping {target} is into gaming as well.",
            "\"{target}, do you know that famous superhero? They remind me so much of you!\" {initiator} says, hoping to make {target} feel special with the comparison.",
            "\"Have you seen the latest viral meme, {target}? I couldn't stop laughing and thought you might enjoy it too,\" {initiator} says, hoping to share a funny moment with {target}.",
            "\"I can't get this catchy jingle out of my head, {target}. Do you know what I'm talking about?\" {initiator} asks, hoping {target} is familiar with the popular tune.",
            "\"Guess what, {target}! I just finished reading this incredible graphic novel. You have to check it out!\" {initiator} says, hoping {target} shares their love for graphic novels.",
            "\"{target}, have you seen that dance challenge going around? I'm so tempted to give it a try! What do you think?\" {initiator} asks, hoping to engage {target} in a fun and trendy activity."
        ]
    },
    "mixer_social_PraiseForGoodGrades_targeted_Friendly_alwaysOn_child_teen": {
        "pre_actions": [
            "{initiator} praises {target}, a young child, for their good grades."
        ],
        "actions": [
            "\"{target}, I am so proud of you! Your hard work and dedication really paid off,\" {initiator} says with a big smile.",
            "\"Wow, {target}, you did amazing on your exams! You're such a smart and talented kid,\" {initiator} exclaims, giving them a high-five.",
            "\"I've been hearing great things about your grades, {target}. You should be really proud of yourself,\" {initiator} says, beaming with admiration.",
            "\"Congratulations, {target}! Your good grades show how committed you are to your studies. Keep up the fantastic work,\" {initiator} praises, patting them on the back.",
            "\"{target}, your parents must be so proud of you. Your good grades are a testament to your intelligence and determination,\" {initiator} commends, giving them a thumbs up.",
            "\"I knew you had it in you, {target}! Your good grades are a reflection of your effort and ability. Keep up the great work,\" {initiator} encourages, with a warm smile.",
            "\"Your good grades are truly impressive, {target}. It's clear that you have a bright future ahead of you,\" {initiator} says, genuinely impressed.",
            "\"{target}, you are setting such a great example for your classmates with your exceptional grades. Keep up the good work,\" {initiator} praises, nodding approvingly.",
            "\"You worked so hard for those good grades, {target}, and it definitely paid off. Well done!\" {initiator} says, clapping for them.",
            "\"{target}, your good grades are a testament to your dedication and intelligence. You should be really proud of yourself,\" {initiator} says, giving them a warm hug."
        ]
    },
    "mixer_social_QuoteCartoonCharacter_targeted_Funny_alwaysOn_child": {
        "pre_actions": [
            "{initiator}, a young child, quotes a cartoon character to {target}."
        ],
        "actions": [
            "\"{target}, did you know that as Spongebob Squarepants once said, 'I'm ready, I'm ready, I'm ready'?\" {initiator} says with excitement.",
            "\"I learned something cool from my favorite cartoon character, {target}. As Mickey Mouse always says, 'Oh boy!'\" {initiator} exclaims.",
            "\"{target}, I have a joke for you! What did Bugs Bunny say to Elmer Fudd? 'What's up, doc?'\" {initiator} giggles mischievously.",
            "\"{target}, I've been watching this amazing cartoon and I can't stop saying, 'To infinity and beyond!' just like Buzz Lightyear,\" {initiator} says, imitating the character's voice.",
            "\"I've got a question for you, {target}. Can you guess which cartoon character says, 'I love you, you love me, we're a happy family'?\" {initiator} asks, a big smile on their face.",
            "\"{target}, guess what? I've been practicing my best impression of Dory from Finding Nemo. 'Just keep swimming, just keep swimming!'\" {initiator} says, swimming imaginary strokes in the air.",
            "\"{target}, I know a catchy song from my favorite cartoon. It goes like this: 'Who lives in a pineapple under the sea?' Can you guess?\" {initiator} hums, waiting for {target} to join in.",
            "\"I have a riddle for you, {target}. What cartoon character says, 'What's up, Doc?' and loves carrots?\" {initiator} asks, eager to test {target}'s knowledge.",
            "\"{target}, have you ever heard the saying, 'I'm not bad, I'm just drawn that way'? It's from a cartoon character I really like,\" {initiator} says, trying to mimic the character's seductive voice.",
            "\"Hey {target}, do you know what cartoon character says, 'Cowabunga!'\"? {initiator} asks, pretending to surf on an imaginary wave."
        ]
    },
    "mixer_social_ShowOffOutfit_targeted_friendly_alwaysOn_teen": {
        "pre_actions": [
            "{initiator}, a teen, shows off their outfit to {target}."
        ],
        "actions": [
            "\"{target}, check out this outfit I put together! What do you think?\" {initiator} twirls around, excitedly showing off their ensemble.",
            "\"I spent hours picking out the perfect pieces for this outfit, {target}. Do you like it?\" {initiator} asks, striking a pose.",
            "\"Hey {target}, I've been experimenting with my style lately. Take a look at what I came up with,\" {initiator} says, gesturing towards their outfit.",
            "\"I wanted to show you my new look, {target}. What do you think? Do you think it suits me?\" {initiator} asks, eagerly awaiting {target}'s opinion.",
            "\"Guess what, {target}? I've discovered a new fashion trend, and I decided to try it out. Do you think I pulled it off?\" {initiator} asks, hoping for {target}'s approval.",
            "\"{target}, I've been trying to step up my fashion game. Check out this outfit I put together,\" {initiator} says, striking a confident pose.",
            "\"{target}, I need your honest opinion. What do you think of my outfit? Is it a hit or a miss?\" {initiator} asks, looking for {target}'s fashion expertise.",
            "\"I've been experimenting with different styles lately, {target}. Take a look at what I've come up with,\" {initiator} says, eagerly awaiting {target}'s reaction.",
            "\"I've been inspired by a fashion influencer, and I decided to recreate one of their looks. What do you think, {target}?\" {initiator} asks, seeking {target}'s validation.",
            "\"{target}, I've been working on my personal style. Check out this outfit and let me know what you think,\" {initiator} says, nervously anticipating {target}'s response."
        ]
    },
    "mixer_social_TalkAboutFavoriteAnimal_targeted_Friendly_alwaysOn_child": {
        "pre_actions": [
            "{initiator}, a young child, talks about their favorite animal to {target}."
        ],
        "actions": [
            "\"I saw the coolest animal at the zoo today, {target}! It had stripes and big sharp teeth,\" {initiator} exclaims excitedly.",
            "\"I have a new favorite animal, {target}! It's the fastest animal in the world and it can run so, so fast,\" {initiator} tells with wide eyes.",
            "\"Guess what, {target}? I learned about an amazing animal in school today. It's really big and it lives in the ocean,\" {initiator} shares eagerly.",
            "\"You know, {target}, I have the best animal toy. It's my favorite because it can fly high up in the sky and see everything,\" {initiator} says, showing enthusiasm.",
            "\"I want to tell you about this animal that I think is so cool, {target}. It has a long neck and it can reach leaves at the top of trees,\" {initiator} explains, mimicking a giraffe.",
            "\"You'll never guess what my favorite animal is, {target}! It's this cute little creature that lives in the forest and eats lots of bamboo,\" {initiator} giggles.",
            "\"There's this animal that everyone is scared of, but I think it's really awesome, {target}. It has a mane and it roars really loudly,\" {initiator} shares with excitement.",
            "\"Today, {target}, my teacher told us about an animal that can change its colors. I think it's the coolest thing ever,\" {initiator} says, demonstrating how it could blend in with its surroundings.",
            "\"I'm so happy, {target}! I finally saw my favorite animal at the zoo. It's really big and has a really long trunk,\" {initiator} exclaims, unable to contain their joy.",
            "\"I have a book about animals, {target}, and I found my favorite in it. It has big antlers and lives in snowy places,\" {initiator} says, holding up the book to show the picture."
        ]
    },
    "mixer_social_TalkAboutFractions_targeted_Friendly_alwaysOn_child_skills": {
        "pre_actions": [
            "{initiator}, a young child, talks about fractions with {target}."
        ],
        "actions": [
            "\"Hey {target}, do you know what fractions are?\" {initiator} asks, looking curious.",
            "\"I learned something really cool in school today. It's called fractions. Have you heard of them, {target}?\" {initiator} asks, eager to share their newfound knowledge.",
            "\"I've been learning about fractions in math class, {target}, and I wanted to show you what I've learned,\" {initiator} says, pulling out a notebook filled with colorful illustrations.",
            "\"{target}, can you help me understand fractions? My teacher said you're really good at math,\" {initiator} asks, looking up at {target} with hopeful eyes.",
            "\"I'm a bit confused about fractions, {target}. Can you explain them to me?\" {initiator} asks, scratching their head in puzzlement.",
            "\"I've been practicing fractions at home, {target}, and I think I finally understand them. Want me to show you?\" {initiator} says, beaming with confidence.",
            "\"{target}, do you know how fractions work? I'm trying to figure it out, but it's a bit tricky,\" {initiator} admits, looking a bit frustrated.",
            "\"I can't believe how interesting fractions are, {target}. Let me explain what I've learned so far,\" {initiator} says, excitement evident in their voice.",
            "\"Math class today was all about fractions, {target}, and I thought it was so fascinating. Can I teach you what I learned?\" {initiator} asks, eager to share their knowledge.",
            "\"{target}, can you help me solve this fraction problem? I'm stuck and I know you're really smart,\" {initiator} says, holding up a worksheet with a challenging question."
        ]
    },
    "mixer_social_TalkAboutToys_targeted_Friendly_alwaysOn_child": {
        "pre_actions": [
            "{initiator}, a young child, talks about their toys to {target}."
        ],
        "actions": [
            "\"I have so many toys, {target}! Let me show you my favorite ones,\" {initiator} says excitedly.",
            "\"Do you like toys, {target}? I have a whole bunch of them. Can I tell you about them?\" {initiator} asks, looking at {target} with anticipation.",
            "\"You won't believe all the toys I have, {target}! Let me tell you about them,\" {initiator} says, bouncing up and down with excitement.",
            "\"I love playing with my toys, {target}. Can I tell you all about them?\" {initiator} asks, holding a toy tightly in their hands.",
            "\"I have this amazing collection of toys, {target}. Can I show them to you and tell you their stories?\" {initiator} asks, gesturing towards a shelf filled with toys.",
            "\"Playing with toys is so much fun, {target}. Let me tell you about my favorites,\" {initiator} says, eagerly waiting for {target}'s response.",
            "\"I have this really cool toy that I want to tell you about, {target}. Can I show it to you?\" {initiator} asks, holding a toy up for {target} to see.",
            "\"Sometimes I imagine that my toys come to life, {target}. Do you ever do that? Let me tell you about my adventures with them,\" {initiator} says, a twinkle in their eyes.",
            "\"Sometimes I talk to my toys as if they can hear me, {target}. Is that weird? Let me tell you what we talk about,\" {initiator} says, looking at {target} with curiosity.",
            "\"I have a secret hideout for my toys, {target}. Do you want to come see it? I'll show you all the cool things I have,\" {initiator} says, inviting {target} to join their imaginative world."
        ]
    },
    "mixer_social_Targeted_Mean_AlwaysOn_STC_Toddler_CrushDreams": {
        "pre_actions": [
            "{initiator} angrily crushes toddler {target}'s dreams."
        ],
        "actions": [
            "\"{target}, you need to wake up and face reality. Your dreams are nothing but illusions,\" {initiator} says, their voice filled with anger.",
            "\"I'm tired of watching you chase after something that will never come true, {target}. It's time to face the harsh truth,\" {initiator} says, their tone filled with frustration.",
            "\"I can't stand seeing you live in this fantasy world, {target}. It's time for me to burst your bubble,\" {initiator} says, their voice laced with annoyance.",
            "\"{target}, you need to stop dreaming and start focusing on what's practical. Your dreams are holding you back,\" {initiator} declares, their anger evident.",
            "\"I've had enough of your unrealistic dreams, {target}. It's time someone brought you back down to earth,\" {initiator} says, their words sharp and cutting.",
            "\"I can't believe you still believe in your childish dreams, {target}. It's time for a reality check,\" {initiator} says, their voice dripping with contempt.",
            "\"{target}, it's about time someone shattered your dreams and made you face the truth. Consider me your wake-up call,\" {initiator} says, their anger palpable.",
            "\"Your dreams are nothing more than a waste of time, {target}. It's time I opened your eyes to reality,\" {initiator} says, their tone filled with bitterness.",
            "\"I can't stand how you cling to your dreams, {target}, as if they actually matter. It's time for a harsh dose of reality,\" {initiator} says, their frustration evident.",
            "\"{target}, I've had enough of your foolish dreams. It's time I crushed them once and for all,\" {initiator} says, their anger seeping through their words."
        ]
    },
    "mixer_social_Targeted_Mean_AlwaysOn_STC_Toddler_Scold": {
        "pre_actions": [
            "{initiator} angrily scolds {target}, who is a toddler."
        ],
        "actions": [
            "\"{target}, how many times do I have to tell you not to touch that?! You never listen!\" {initiator} scolds, frustration evident in their voice.",
            "\"I can't believe you spilled your juice all over the floor again! Will you ever learn, {target}?\" {initiator} reprimands, hands on their hips.",
            "\"Enough is enough, {target}! You can't just throw your toys around like that. It's not funny!\" {initiator} scolds, their voice stern.",
            "\"{target}, we've talked about this. No hitting! How many more times do I have to say it?\" {initiator} says, their tone laced with anger.",
            "\"You're testing my patience, {target}. How many times do I have to tell you not to run away like that?\" {initiator} scolds, taking a deep breath to calm themselves.",
            "\"Stop screaming, {target}! You're giving me a headache. Can't you be quiet for once?\" {initiator} says, their voice filled with frustration.",
            "\"I told you not to touch the stove, {target}. Now look what you've done! I can't believe you!\" {initiator} scolds, a mix of anger and concern in their eyes.",
            "\"Enough with the tantrums, {target}! You need to start behaving. It's time to learn some discipline,\" {initiator} scolds, their voice firm.",
            "\"{target}, we've talked about this a hundred times. No throwing food! Clean it up right now!\" {initiator} reprimands, pointing to the mess.",
            "\"I don't want to hear any more excuses, {target}. You need to take responsibility for your actions,\" {initiator} scolds, their tone stern."
        ]
    },
    "mixer_social_Targeted_Mean_AlwaysOn_STC_Toddler_YellAt": {
        "pre_actions": [
            "{initiator} angrily yells at {target}, who is a toddler."
        ],
        "actions": [
            "\"{target}, stop! No! Bad!\" {initiator} shouts in frustration, trying to get through to the toddler.",
            "\"Toddler, you're driving me crazy! Just listen to me for once!\" {initiator} exclaims, growing more irritated.",
            "\"I can't believe you're behaving like this, {target}! Do you have any idea how much you're testing my patience?\" {initiator} yells, feeling their anger rise.",
            "\"Enough is enough, {target}! I will not tolerate this behavior anymore!\" {initiator} shouts, their face turning red.",
            "\"I've had it with you, {target}! You need to start behaving or there will be consequences!\" {initiator} scolds, their voice filled with anger.",
            "\"{target}, I'm so fed up with you right now! Can't you just listen and do as I say?\" {initiator} yells, their frustration evident in their tone.",
            "\"Stop it right now, {target}! You're being absolutely infuriating!\" {initiator} snaps, trying to keep their temper in check.",
            "\"I can't handle this anymore, {target}! Your behavior is driving me insane!\" {initiator} shouts in exasperation.",
            "\"{target}, you're pushing me to my limits! Stop it!\" {initiator} yells, struggling to control their anger.",
            "\"This is unacceptable, {target}! I will not tolerate this kind of behavior from you!\" {initiator} raises their voice, their words sharp and stern."
        ]
    },
    "mixer_social_TeaseMercilessly_targeted_mean_teen": {
        "pre_actions": [
            "{initiator}, a mean teenager, teases {target} mercilessly."
        ],
        "actions": [
            "\"{target}, you really are pathetic. I don't know why you even bother trying,\" {initiator} sneers, a cruel smirk on their face.",
            "\"Look who decided to show up, {target}. Are you ready for another round of humiliation?\" {initiator} taunts, their voice dripping with malice.",
            "\"You know, {target}, it's almost impressive how easily you become the laughingstock of every situation,\" {initiator} jeers, enjoying their own cruelty.",
            "\"I hope you enjoy being everyone's punching bag, {target}, because that's all you'll ever be,\" {initiator} mocks, their words like daggers.",
            "\"Do you ever get tired of being an embarrassment, {target}? It's like you were born to fail,\" {initiator} says, laughing mockingly.",
            "\"{target}, you really need to stop pretending like people actually like you. It's getting sad,\" {initiator} taunts, relishing in their power over {target}.",
            "\"{initiator}, can't you find someone else to torment? {target} has suffered enough,\" a voice finally speaks up, defending {target}.",
            "\"You're pathetic, {target}. I can't believe anyone could ever like you,\" {initiator} says, their words laced with venom.",
            "\"Hey, {target}, have you thought about just giving up? It would save us all a lot of time,\" {initiator} teases, a cruel smile on their face.",
            "\"Just admit it, {target}, you're a loser. And everyone knows it,\" {initiator} jeers, their voice loud and mocking."
        ]
    },
    "mixer_social_Toddler_Friendly_TalkTo_Stranger": {
        "pre_actions": [
            "{initiator}, an innocent toddler, talks to {target}, who is a stranger."
        ],
        "actions": [
            "\"Hi there! My name is {initiator}, what's your name?\" the toddler asks with a wide-eyed curiosity.",
            "{initiator} tugs at {target}'s shirt, saying \"Do you wanna be friends? I like playing with new friends!\"",
            "With a bright smile, {initiator} babbles excitedly, as if sharing a secret with {target}, \"Guess what? I just learned how to walk all by myself!\"",
            "Wide-eyed, {initiator} points at {target}'s shoes and asks, \"Are those magic shoes? Can you teach me how to fly?\"",
            "Curiously, {initiator} Studies {target} for a moment, then asks innocently, \"Why do you look different than the other grown-ups?\"",
            "Innocently, {initiator} asks, \"Can you tell me a story? I love stories!\"",
            "Giggling uncontrollably, {initiator} asks {target} to play peek-a-boo, saying, \"I bet you can't find me!\"",
            "With a hint of shyness, {initiator} asks {target}, \"Are you nice? My mommy told me to only talk to nice people.\"",
            "Dreamily, {initiator} points at a butterfly and says, \"Look, it's dancing in the sky! Do you like butterflies too?\"",
            "With a mischievous smile, {initiator} pulls out a toy car and offers it to {target}, saying, \"Want to race with me?\""
        ]
    },
    "mixer_social_toddler_Funny_JokeAboutChickenButt": {
        "pre_actions": [
            "{initiator}, an innocent toddler, makes a chicken butt joke to {target}."
        ],
        "actions": [
            "\"{target}, guess what? Chicken butt,\" {initiator}, the innocent toddler, giggles mischievously.",
            "\"Hey {target}, wanna hear a silly joke? Chicken butt!\" {initiator} bursts into laughter.",
            "{initiator} tugs on {target}'s sleeve and whispers, \"I have a secret joke just for you. Ready? Chicken butt!\" They break into giggles together.",
            "With a cheeky grin, {initiator} looks up at {target} and says, \"I know a funny joke. Chicken butt! Isn't it silly?\"",
            "\"{target}! {target}! I have a funny joke to tell you. Chicken butt!\" {initiator} exclaims, unable to contain their excitement.",
            "{initiator} runs up to {target} and says, \"I learned a new joke. Ready? Chicken butt!\" They giggle with delight.",
            "With a twinkle in their eyes, {initiator} looks up at {target} and whispers, \"I know a super silly joke. It goes like this: chicken butt!\"",
            "Grinning mischievously, {initiator} approaches {target} and says, \"Can I tell you a joke? Get ready for it... Chicken butt!\"",
            "{initiator} points at {target} and blurts out, \"Chicken butt! Herh herh herh!\" before bursting into infectious laughter.",
            "Looking up at {target} with wide eyes, {initiator} says, \"I have a really funny joke to tell you. Ready? Chicken butt!\""
        ]
    },
    "mixer_social_Toddler_Funny_Say_NonSense": {
        "pre_actions": [
            "{initiator}, an innocent toddler, babbles nonsense to {target}."
        ],
        "actions": [
            "The toddler looks at {target} and babbles excitedly, as if trying to engage in a conversation.",
            "{initiator} points at an object and tries to name it, giggling as {target} listens attentively.",
            "Out of nowhere, the toddler blurts out a string of gibberish to {target}, expecting a response.",
            "{initiator} looks up at {target} with big curious eyes and starts copying the sounds he/she makes.",
            "Seeing {target} nearby, the toddler decides to approach, babbling contently.",
            "The toddler reaches out to {target} with a toy and begins babbling incoherent words with a big smile.",
            "{initiator} contemplates {target} zealously, uttering a series of nonsensical sounds.",
            "The toddler tugs at {target}'s clothes, repetitively  mumbling buzzwords, seeking attention.",
            "Realizing {target} is paying attention, the toddler squeals happily and babbles animatedly.",
            "Attempting to figure out the basics of conversation, {initiator} babbles playfully to {target}."
        ]
    },
    "mixer_social_Toddler_Funny_Tell_Knock_Knock_Joke": {
        "pre_actions": [
            "{initiator}, an innocent toddler, tells a knock knock joke to {target}."
        ],
        "actions": [
            "{initiator} toddles up to {target} with a mischievous smile on their face.",
            "\"Knock, knock,\" {initiator} says, giggling.",
        ]
    },
    "mixer_social_Toddler_Mean_Yell_At": {
        "pre_actions": [
            "{initiator}, a cranky toddler, yells at {target}."
        ],
        "actions": [
            "\"No, {target}, no! I don't like you!\" {initiator} yells with crossed arms.",
            "\"Go away, {target}! I don't want to play with you!\" {initiator} shouts, stomping their feet in frustration.",
            "\"Leave me alone, {target}! I'm busy and I don't want to talk to you!\" {initiator} screams, scowling.",
            "\"{target}! Stop it! I don't want to listen to you!\" {initiator} yells, covering their ears.",
            "\"I hate you, {target}! Go away and never come back!\" {initiator} shouts angrily, face turning red.",
            "\"{target}, stop it! I want my mommy, not you!\" {initiator} screams, tears streaming down their face.",
            "\"Get out of my face, {target}! I don't want to see you anymore!\" {initiator} yells, pushing {target} away.",
            "\"{target}, you're mean! I don't want to be friends with you!\" {initiator} yells, sticking out their tongue.",
            "\"{target}! You ruined everything! Now I'm mad at you!\" {initiator} shouts, pouting with crossed arms.",
            "\"I'm telling! {target} is being mean to me!\" {initiator} yells, running to find an adult."
        ]
    },
    "mixer_social_Toddler_TalkAbout_Art": {
        "pre_actions": [
            "{initiator}, a babbling toddler, talks about art with {target}."
        ],
        "actions": [
            "\"{target}, look at this paint I made! Colors everywhere!\" the toddler says excitedly, showing off their finger-painted masterpiece. ",
            "\"I'm trying to create a [specific animal] out of clay. What do you think, {target}?\" the toddler asks, molding the clay passionately. ",
            "\"Can you teach me how to draw, {target}? I want to make pretty pictures like you,\" the toddler asks with wide eyes. ",
            "\"{target}, do you like my picture? I put hearts and stars because they're pretty,\" the toddler says, hands covered in paint. ",
            "\"{target}! Look at this funny sculpture I made. It's like a bumpy monster,\" the toddler giggles, holding their work up for {initiator} to see. ",
            "\"I have so many colors of crayons. Which do you like best, {target}?\" the toddler asks, holding out a box of crayons. ",
            "\"{target}, guess what! I learned how to scribble today. Look at my beautiful masterpiece,\" the toddler says proudly, showing off their scrawled lines. ",
            "\"{target}, will you help me finger paint? I promise I won't make a mess... well, not too much of a mess,\" the toddler pleads, eyes sparkling. ",
            "\"{target}, did you know that blue and yellow make green? I'm an artist, I know these things,\" the toddler says confidently, holding up a crayon. ",
            "\"Drawing is so much fun, {target}! Will you draw with me and make magical worlds come to life?\" the toddler asks, holding a sketchpad."
        ]
    },
    "mixer_social_Toddler_TalkAbout_Day": {
        "pre_actions": [
            "{initiator}, a babbling toddler, talks about their day with {target}."
        ],
        "actions": [
            "\"{target}, guess what?! I painted a picture today! It was so fun!\" {initiator} exclaims, beaming with excitement.",
            "\"Somebody pushed me on the swings at the park, {target}, and I went really high!\" {initiator} says, their voice filled with excitement.",
            "\"I found a bug outside and I showed it to Miss Johnson, {target}. She said it was a ladybug!\" {initiator} says, their eyes wide with wonder.",
            "\"I saw a doggy today, {target}, and I asked it if I could pet it. It was so fluffy!\" {initiator} says, giggling.",
            "\"{target}, I went to story time at the library today, and I made a new friend! Her name is Emily and we read so many books!\" {initiator} says, enthusiasm lacing their words.",
            "\"Guess what, {target}! I ate the biggest ice cream cone today, and it had sprinkles! It was the best thing ever!\" {initiator} says, their face lighting up.",
            "\"Mommy took me to the zoo, {target}, and I saw a lion! It was so big and roar-y!\" {initiator} says, mimicking a lion's roar with enthusiasm.",
            "\"{target}, I played in the sandbox at the playground today! I built a castle and it was so tall!\" {initiator} says, their voice filled with pride.",
            "\"I fell down and got a 'boo-boo' on my knee today, {target}, but mommy kissed it and it feels better now!\" {initiator} says, pouting slightly.",
            "\"{target}, I played dress-up with my big sister today, and we pretended to be princesses! I had a sparkly crown!\" {initiator} says, twirling around with joy."
        ]
    },
    "mixer_social_Toddler_TalkAbout_Dinosaurs": {
        "pre_actions": [
            "{initiator}, a babbling toddler, talks about dinosaurs with {target}."
        ],
        "actions": [
            "\"{target}, do you know dinosaurs? They're big and scary!\" {initiator} babbles excitedly.",
            "\"I saw a dinosaur on TV, {target}! It had big, sharp teeth and a long neck!\" {initiator} exclaims, pointing at the screen.",
            "\"Hey, {target}! Did you know dinosaurs lived a long, long time ago, even before our moms and dads were born?\" {initiator} asks, looking up at {target}.",
            "\"I have a toy dinosaur, {target}! Wanna see it? It roars and moves its tail!\" {initiator} says, eager to show off their toy.",
            "\"Rawwr! I'm a dinosaur, {target}!\" {initiator} giggles, imitating a dinosaur walking.",
            "\"Look, {target}! This book has lots of pictures of dinosaurs. Can we read it together?\" {initiator} asks, holding up a book with colorful illustrations.",
            "\"Did you know, {target}, dinosaurs were really big? Some were even bigger than our house!\" {initiator} exclaims, attempting to spread their arms as wide as possible to demonstrate.",
            "\"{target}, I love dinosaurs! I can name so many kinds: T-rex, Triceratops, and Stegosaurus!\" {initiator} declares proudly.",
            "\"I want to be a paleontologist when I grow up, {target}! That's someone who knows all about dinosaurs!\" {initiator} shares their future ambition with excitement.",
            "\"I wish I could see a real dinosaur, {target}! That would be so cool!\" {initiator} says wistfully, looking up at the sky as if expecting a dinosaur to appear."
        ]
    },
    "mixer_social_Toddler_TalkAbout_Favorite_Color": {
        "pre_actions": [
            "{initiator}, a babbling toddler, talks about their favorite color with {target}."
        ],
        "actions": [
            "\"{target}, guess what? My favorite color is \"",
            "\"You won't believe it, {target}, but my favorite color is \"",
            "\"Oh, oh, oh! I have something to tell you, {target}! My favorite color, it's \"",
            "\"I have a super-duper special favorite color, {target}, and it's \"",
            "\"Do you want to know my top secret, {target}? My favorite color is \"",
            "\"Hey, {target}, I have a secret! My favorite color is \"",
            "\"Do you want to hear about my most favorite color ever, {target}? It's \""
        ]
    },
    "mixer_social_Toddler_TalkAbout_Princesses": {
        "pre_actions": [
            "{initiator}, a babbling toddler, talks about princesses with {target}."
        ],
        "actions": [
            "\"{target}, guess what? I saw a princess today, and she had the sparkliest dress ever!\" {initiator} babbles excitedly.",
            "\"I have a princess crown at home, {target}, and I wear it every day. Do you want to see it?\"",
            "\"Princesses are magical, {target}. I wish I could be a princess and have a castle with a pink unicorn!\"",
            "\"{target}, did you know princesses always have pretty hair? I want my hair to be long and beautiful like theirs.\"",
            "\"I have a book about princesses, {target}, and I want to read it to you. Can we sit and read it together?\"",
            "\"{target}, if I was a princess, I would have a pet dragon to protect me. What would you have as a princess?\"",
            "\"Do you think there are ladybug princesses, {target}? I love ladybugs, and I want to be their princess!\"",
            "\"I saw a princess movie yesterday, {target}, and there was a big, magical ballroom. I want to dance like that!\"",
            "\"{target}, I want to dress up as a princess today. Will you be my prince or princess too?\"",
            "\"{target}, princesses always go on adventures. Let's find a big castle and go on an adventure together!\""
        ]
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
    "tv_ChannelSurf": {
        "observations": [
            "{initiator} surfs the channels on tv.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "watch-passive": {
        "ignored": True,
    },
    "tv-watch-sports": {
        "observations": [
            "{initiator} watches sports on tv.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "watch-passive-withphone": {
        "observations": [
            "{initiator} watches tv while on their phone.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "TV_WatchRandomChannel": {
        "observations": [
            "{initiator} watches a random channel on tv.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "terrain-gohere": {
        "ignored": True,
    },
    "NPCLeaveLotNow_NPC_MustRun_WaveGoodBye": {
        "ignored": True,
    },
    "put_down_anywhere": {
        "ignored": True,
    },
    "si_moveAwayCircle": {
        "ignored": True,
    },
    "bar_NonCrafting_BottleStack": {
        "ignored": True,
    },
    "object_Insane_TalkToObjects": {
        "observations": [
            "{initiator} is insane and talks to the inanimate objects.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "generic_JungleGym": {
        "ignored": True,
    },
    "toilet_preFlush": {
        "ignored": True,
    },
    "jungleGymBoat_Play": {
        "observations": [
            "{initiator} plays around on the jungle gym boat that has cannons and a pirate flag.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "jungleGymBoat_Active": {
        "observations": [
            "{initiator} plays around on the jungle gym boat that has cannons and a pirate flag.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "jungleGymBoat_Passive": {
        "observations": [
            "{initiator} plays around on the jungle gym boat that has cannons and a pirate flag.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "bar_PracticeTricks_DestroyShaker": {
        "ignored": True,
    },
    "Bar_Juggle_Basic": {
        "observations": [
            "{initiator} juggles the cocktail shaker as a bar trick.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "bar_Tendbar": {
        "ignored": True,
    },
    "bar_Clean": {
        "observations": [
            "{initiator} cleans up the bar and wipes it down.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "terrain_putdown": {
        "ignored": True,
    },
    # TODO: How do we figure out which object was picked up?
    "carry_holdobject": {
        "ignored": True,
    },
    # TODO: How do we figure out which object was put down?
    "putdownchooser": {
        "ignored": True,
    },
    "bar_PracticeTricks": {
        "ignored": True,
    },
    "reaction_AnnoyedByMess": {
        "observations": [
            "{initiator} looks around at the mess and feels annoyed.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "[Join]stereo_Dance": {
        "observations": [
            "{initiator} walks up to the stereo and starts dancing.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "bar_MakeDrink_Staging_basic": {
        "ignored": True,
    },
    "Push_Leave_Lot": {
        "ignored": True,
    },
    "Bar_Shake_Basic": {
        "observations": [
            "{initiator} shakes the drink shaker at the bar.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "bar_DestroyShaker": {
        "observations": [
            "{initiator} puts the bar shaker away.",
        ],
        "filters": [
            HasNotHappened(memory_depth=10),
            InitiatorIsActiveSim(),
        ],
    },
    "Bar_BehindTheBack_Basic": {
        "observations": [
            "{initiator} does a bar trick throwing the shaker behind their back.",
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
