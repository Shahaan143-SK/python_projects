import random
# Combined list of famous personalities (India, Pakistan, Worldwide)
subjects = [
    # 🇮🇳 Indian Personalities
    "Mahatma Gandhi", "Jawaharlal Nehru", "Narendra Modi", "Indira Gandhi", "Dr. B.R. Ambedkar",
    "Ratan Tata", "Mukesh Ambani", "Gautam Adani", "Azim Premji", "Narayana Murthy",
    "Sachin Tendulkar", "Virat Kohli", "P.V. Sindhu", "M.S. Dhoni", "Neeraj Chopra",
    "Amitabh Bachchan", "Shah Rukh Khan", "A.R. Rahman", "Deepika Padukone", "Priyanka Chopra",
    "Rabindranath Tagore", "Chetan Bhagat", "Arundhati Roy", "Dr. A.P.J. Abdul Kalam", "Swami Vivekananda",

    # 🇵🇰 Pakistani Personalities
    "Muhammad Ali Jinnah", "Benazir Bhutto", "Imran Khan", "Liaquat Ali Khan", "Malala Yousafzai",
    "Mian Muhammad Mansha", "Shahid Khan", "Abdul Razzak Dawood",
    "Wasim Akram", "Shahid Afridi", "Babar Azam", "Jahangir Khan", "Sania Mirza",
    "Nusrat Fateh Ali Khan", "Atif Aslam", "Mahira Khan", "Abida Parveen", "Ali Zafar",
    "Faiz Ahmed Faiz", "Allama Iqbal", "Bano Qudsia", "Saadat Hasan Manto", "Parveen Shakir",

    # 🌍 World Personalities
    "Barack Obama", "Nelson Mandela", "Winston Churchill", "Vladimir Putin", "Angela Merkel",
    "Elon Musk", "Jeff Bezos", "Bill Gates", "Steve Jobs", "Warren Buffett",
    "Albert Einstein", "Marie Curie", "Isaac Newton", "Nikola Tesla", "Stephen Hawking",
    "Taylor Swift", "Leonardo DiCaprio", "Beyoncé", "Tom Cruise", "Rihanna",
    "William Shakespeare", "Maya Angelou", "Jane Austen", "Rumi", "Paulo Coelho",
    "Martin Luther King Jr.", "Mother Teresa", "Greta Thunberg", "Dalai Lama", "Desmond Tutu"
]

# Extended list of actions with English verb forms
actions = [
    # Movement
    "run", "runs", "running", "ran",
    "walk", "walks", "walking", "walked",
    "jump", "jumps", "jumping", "jumped",
    "climb", "climbs", "climbing", "climbed",
    "swim", "swims", "swimming", "swam",
    "fly", "flies", "flying", "flew",
    "drive", "drives", "driving", "drove",
    "ride", "rides", "riding", "rode",
    "sit", "sits", "sitting", "sat",
    "stand", "stands", "standing", "stood",
    "crawl", "crawls", "crawling", "crawled",
    "run", "runs", "running", "ran",

    # Communication
    "talk", "talks", "talking", "talked",
    "speak", "speaks", "speaking", "spoke",
    "say", "says", "saying", "said",
    "tell", "tells", "telling", "told",
    "listen", "listens", "listening", "listened",
    "hear", "hears", "hearing", "heard",
    "shout", "shouts", "shouting", "shouted",
    "whisper", "whispers", "whispering", "whispered",
    "ask", "asks", "asking", "asked",
    "answer", "answers", "answering", "answered",
    "argue", "argues", "arguing", "argued",
    "explain", "explains", "explaining", "explained",

    # Work & Creation
    "work", "works", "working", "worked",
    "build", "builds", "building", "built",
    "create", "creates", "creating", "created",
    "design", "designs", "designing", "designed",
    "make", "makes", "making", "made",
    "fix", "fixes", "fixing", "fixed",
    "write", "writes", "writing", "wrote",
    "draw", "draws", "drawing", "drew",
    "paint", "paints", "painting", "painted",
    "clean", "cleans", "cleaning", "cleaned",
    "cook", "cooks", "cooking", "cooked",
    "bake", "bakes", "baking", "baked",

    # Learning & Thinking
    "study", "studies", "studying", "studied",
    "learn", "learns", "learning", "learned",
    "teach", "teaches", "teaching", "taught",
    "read", "reads", "reading", "read",
    "think", "thinks", "thinking", "thought",
    "understand", "understands", "understanding", "understood",
    "remember", "remembers", "remembering", "remembered",
    "forget", "forgets", "forgetting", "forgot",
    "plan", "plans", "planning", "planned",
    "decide", "decides", "deciding", "decided",
    "solve", "solves", "solving", "solved",
    "analyze", "analyzes", "analyzing", "analyzed",

    # Emotions
    "love", "loves", "loving", "loved",
    "like", "likes", "liking", "liked",
    "hate", "hates", "hating", "hated",
    "enjoy", "enjoys", "enjoying", "enjoyed",
    "smile", "smiles", "smiling", "smiled",
    "laugh", "laughs", "laughing", "laughed",
    "cry", "cries", "crying", "cried",
    "hope", "hopes", "hoping", "hoped",
    "fear", "fears", "fearing", "feared",

    # Daily life
    "eat", "eats", "eating", "ate",
    "drink", "drinks", "drinking", "drank",
    "sleep", "sleeps", "sleeping", "slept",
    "wake", "wakes", "waking", "woke",
    "wash", "washes", "washing", "washed",
    "brush", "brushes", "brushing", "brushed",
    "dress", "dresses", "dressing", "dressed",
    "shop", "shops", "shopping", "shopped",
    "open", "opens", "opening", "opened",
    "close", "closes", "closing", "closed",

    # Social & Helping
    "help", "helps", "helping", "helped",
    "support", "supports", "supporting", "supported",
    "give", "gives", "giving", "gave",
    "take", "takes", "taking", "took",
    "meet", "meets", "meeting", "met",
    "invite", "invites", "inviting", "invited",
    "thank", "thanks", "thanking", "thanked",
    "greet", "greets", "greeting", "greeted",
    "follow", "follows", "following", "followed",
    "lead", "leads", "leading", "led"
]

# 🌍 Combined list of famous PLACES + THINGS (religious sites removed)

places_things = [
    # --- Countries ---
    "India", "Pakistan", "United States", "China", "Japan", "United Kingdom", "France", "Germany", "Canada", "Australia",
    "Italy", "Brazil", "Russia", "South Africa", "Singapore", "Thailand", "UAE", "Spain", "Mexico", "Indonesia",
    
    # --- Cities ---
    "New York", "London", "Paris", "Tokyo", "Mumbai", "Karachi", "Beijing", "Dubai", "Rome", "Los Angeles",
    "Delhi", "Lahore", "Bangkok", "Istanbul", "Seoul", "Barcelona", "Toronto", "Sydney", "Berlin", "Moscow",
    "Cape Town", "Singapore City", "Chicago", "Kuala Lumpur", "Doha", "San Francisco", "Jakarta", "Melbourne",
    
    # --- Indian Landmarks (non-religious) ---
    "Taj Mahal", "Gateway of India", "India Gate", "Red Fort", "Qutub Minar", "Statue of Unity",
    "Charminar", "Hawa Mahal", "Marine Drive", "Mysore Palace", "Victoria Memorial", "Lotus Tower",
    "Jantar Mantar", "Ellora Caves", "Ajanta Caves", "Bandra-Worli Sea Link", "Howrah Bridge", "Rashtrapati Bhavan",
    
    # --- Pakistani Landmarks (non-religious) ---
    "Minar-e-Pakistan", "Badshahi Mosque", "Faisal Mosque", "Mazar-e-Quaid", "Pakistan Monument",
    "K2 Mountain", "Karakoram Highway", "Lake Saiful Muluk", "Neelum Valley", "Hunza Valley",
    "Fairy Meadows", "Gwadar Port", "Clifton Beach", "Baltit Fort", "Attabad Lake", "Derawar Fort",
    "Rohtas Fort", "Shalimar Gardens", "Hingol National Park", "Makran Coastal Highway",
    
    # --- World Famous Landmarks ---
    "Eiffel Tower", "Statue of Liberty", "Great Wall of China", "Colosseum", "Burj Khalifa",
    "Pyramids of Giza", "Sydney Opera House", "Big Ben", "Empire State Building", "Leaning Tower of Pisa",
    "Golden Gate Bridge", "Machu Picchu", "Christ the Redeemer", "Mount Everest", "Mount Fuji",
    "Niagara Falls", "Grand Canyon", "Great Barrier Reef", "Yellowstone National Park", "Serengeti National Park",
    "Victoria Falls", "Mount Kilimanjaro", "CN Tower", "Brooklyn Bridge", "Hollywood Sign",
    "London Bridge", "Stonehenge", "Versailles Palace", "Louvre Museum", "Petronas Towers",
    "Gardens by the Bay", "Space Needle", "Marina Bay Sands", "One World Trade Center", "Shanghai Tower",
    "Panama Canal", "Antelope Canyon", "Death Valley", "Ha Long Bay", "Banff National Park",
    "Salar de Uyuni", "Grand Palace Bangkok", "Table Mountain", "Iguazu Falls", "Mount Etna",
    "Lake Louise", "Dubai Mall", "The Palm Jumeirah", "Chichen Itza", "Times Square", "Central Park",
    
    # --- Things ---
    "chair", "table", "lamp", "book", "pen", "cup", "plate", "bottle", "mirror", "clock", "bed", "couch",
    "door", "window", "television", "fan", "remote", "curtain", "sofa", "shelf", "carpet",
    "computer", "laptop", "smartphone", "tablet", "headphones", "camera", "printer", "charger",
    "keyboard", "mouse", "speaker", "microphone", "monitor", "router", "drone", "smartwatch",
    "car", "bus", "train", "bicycle", "motorcycle", "truck", "airplane", "boat", "subway", "scooter", "helicopter", "tram",
    "tree", "flower", "mountain", "river", "stone", "leaf", "sun", "moon", "star", "cloud", "sand", "ocean", "rain", "snow",
    "notebook", "file", "pencil", "eraser", "scissors", "ruler", "paper", "stapler", "calculator", "folder", "highlighter",
    "marker", "envelope", "glue", "tape",
    "shirt", "pants", "dress", "hat", "shoes", "watch", "bag", "jacket", "tie", "scarf", "glasses", "belt", "wallet", "ring",
    "necklace", "bracelet", "umbrella",
    "bread", "rice", "apple", "banana", "milk", "coffee", "tea", "juice", "cake", "egg", "pizza", "sandwich",
    "chocolate", "ice cream", "noodles", "burger", "pasta", "salad", "cookie", "water bottle",
    "key", "coin", "toy", "ball", "helmet", "glove", "mask", "bookcase", "map"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_thing = random.choice(places_things)
    
    fake_news = f"Breaking News: {subject} was seen to {action} in {place_thing}."
    print(fake_news)
    
    user_input = input("Generate another fake news? (Yes/No): ").strip().lower()
    if user_input == 'y' or user_input == 'yes':
        continue
    elif user_input == 'n' or user_input == 'no':
        break
    else:
        print("Invalid input. Exiting the generator.")
        break
print("Thanks for using the Fake News Headline Generator! Have a fun day!")
"""For Preview Only:
https://funheadlines.preview.emergentagent.com/"""




