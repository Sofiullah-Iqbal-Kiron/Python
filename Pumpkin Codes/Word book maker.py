def print_in_TeX_mode(words):
    for w in sorted(words):
        print(f"\t{w} & {words[w]} \\\\ \n\t\\hline")


words = {
    "Throughout": "জুড়ে",
    "Phenomena": "ঘটনা",
    "Exhibit": "প্রদর্শন",
    "Often": "প্রায়শই",
    "Notion": "ভাব, ধারণা",
    "Aspect": "রূপ, মুখাবয়ব",
    "Singleton": "একক বস্তু",
    "Perhaps": "সম্ভবত",
    "Substitution": "প্রতিস্থাপন",
    "Elaborate": "বিস্তৃত",
    "Up to this point": "এখন পর্যন্ত",
    "Chasing": "তাড়া করা",
    "Shelter": "আশ্রয়",
    "Could one of you move my cup closer to my mouth?": "",
    "Disrupt": "বা্যাহত করা",
    "Chaos": "বিস্শৃঙ্খলা",
    # "": "",
    # "": "",
    # "": "",
    # "": "",
    # "": "",
    # "": "",
    # "": "",
    # "": "",
    # "": "",
    # "": "",
    # "": "",
    # "": "",
}

print_in_TeX_mode(words)
