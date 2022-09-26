from pvleopard import *
import moviepy.editor
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest


# Replace the parameter with the location of the video
video = moviepy.editor.VideoFileClip("C:\\Users\\param\\Downloads\\y2mate.com - How to Practice English Speaking at Home By Yourself_360p.mp4")

audio = video.audio

# Replace the parameter with the location along with filename
audio.write_audiofile("C:\\Users\\param\\Downloads\\audio.mp3")
o = create(access_key='Ff28G+gaWSYeGP8/O4gLaW04+eiem4N7cew7xCp+6Ucn5/iY3KHdig==')
transcript, words = o.process_file("C:\\Users\\param\\Downloads\\audio.mp3")
print(transcript)

stopwords = list(STOP_WORDS)
nlp = spacy.load("C:\\Users\\param\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\en_core_web_sm"
                 "\\en_core_web_sm-3.4.0")
doc = nlp(transcript)
tokens = [token.text for token in doc]
punctuation = punctuation + '\n'
word_freq = {}
for word in doc:
    if word.text.lower() not in stopwords:
        if word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text] = 1
            else:
                word_freq[word.text] += 1

max_freq = max(word_freq.values())
for word in word_freq.keys():
    word_freq[word] = word_freq[word] / max_freq
sentence_tokens = [sent for sent in doc.sents]
sentence_scores = {}
for sent in sentence_tokens:
    for word in sent:
        if word.text.lower() in word_freq.keys():
            if sent not in sentence_scores.keys():
                sentence_scores[sent] = word_freq[word.text.lower()]
            else:
                sentence_scores[sent] += word_freq[word.text.lower()]

select_length = int(len(sentence_tokens) * 0.3)
summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)
final_summary = [word.text for word in summary]
summary = ''.join(final_summary)
print(summary)
