import time
import sys

lyrics = [
    "I saw her in the rightest way",
    "Looking like Anne Hathaway",
    "Laughing while she hit her pen",
    "And coughed, and coughed",
    "And then, she came up to my knees",
    "Begging, 'Baby, would you please?",
    "Do the things you said you'd do to me, to me?'"
]

def typewriter_lyrics(lines, char_speed=0.07, line_pause=0.8):
    for line in lines:
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(char_speed)
        
        print()  # Переход на новую строку
        time.sleep(line_pause)  # Пауза между строчками

typewriter_lyrics(lyrics)
