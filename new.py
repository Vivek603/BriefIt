# importing libraries
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Input text - to summarize
text = """Thank you thank you to the president for convening the global entrepreneurship summit. and to Stanford for 
hosting we at Google are proud to be supporting this summit and we are passionate about entrepreneurship this is such 
an important issue for our company but also for our country and for a community of entrepreneurs around the world at 
Google entrepreneurship is in our DNA Google was founded here at Stanford and the company's first home was in a 
garage just a couple miles from here like many of you in the audience our founders were two young people with a 
vision of a better future a better way and and they decided to follow their dreams. we now live on our own campus down 
the road and in dozens of countries but the spirit continues in fact our most popular products almost all began as 
big ideas that small entrepreneurial teams dreamed up and made happen Gmail started with one person's passion to 
reinvent email today it has over one billion monthly active uses are browser chrome a small teams obsession to bring 
a faster more secure web to everyone now has over a billion monthly active uses cardboard or virtual reality viewer 
to engineers in our Paris office had an idea of what's possible with a piece of cardboard and a phone now more than 
five million viewers are taking people to new worlds. using cardboard teachers can take their classes on virtual field 
trips from the great barrier reef to march picture first lady Michelle Obama made this part of her reach higher 
education initiative more than one million students from eleven countries have gone on virtual field trips and today 
we are making cardboard available to LGBTQ centers around the world so people who cannot physically attend pride 
parades and festivals this weekend can still have the prior experience all of this came from two engineers is in 
Paris is bright idea we don't know what's next or where it will come from but we know that the barriers to 
entrepreneurship and to bringing ideas to global audiences are tumbling people working anywhere in the world born 
anywhere in the world can create a product and make it available to anyone in the world the most used messaging app 
in southeast Asia was built by a young man born in Ukraine who moved to the us and the three most popular viral games 
in the us in recent years came from entrepreneurs in Finland Ireland and Vietnam you're the ones building the next 
Google the next fortify the next Tesla the next while we don't even know but what I know is that someone in this room 
will build it maybe someone even from the cast of silicon valley let me tell you a little bit about my personal 
journey to silicon valley from India twenty two years ago growing up in India like many of you I got my first 
telephone when I was twelve in my case it turned out to be a rotary phone so it wasn't that great for selfies but I 
still love to call my friends play with it and sometimes take it apart that telephone cemented my fascination with 
technology I remember in my parents' house in Chennai reading about the invention of the transistor at bell labs of 
course that initial invention help frowned what became known as silicon valley and out of that came companies like 
fascial semiconductor and intel and all the computers and software that we all used today you can draw a direct line 
from that invention to the technology that powers your Twitter feed or your reach at messages today I remember 
reading about that I'm thinking it's the idea that matters it didn't matter where you come from or what your 
background is one revolutionary idea one brilliant invention can unleash other entrepreneurs to revolutionize 
industries in ways you could never predict the people who built a transistor in many ways enable the entrepreneurs 
who are using incredible processing power to analyze data and diagnose cancer in the same way the invention of 
smartphones and GPS has enabled other companies to build abs that revolutionized the way we travel around cities 
that's why I came here I had a deep desire to be part of this exchange of ideas this community of entrepreneurs and 
coming to the global hub where this was all happening at Stanford I felt welcomed and embraced """

# Tokenizing the text
stopWords = set(stopwords.words("english"))
words = word_tokenize(text)

# Creating a frequency table to keep the
# score of each word

freqTable = dict()
for word in words:
	word = word.lower()
	if word in stopWords:
		continue
	if word in freqTable:
		freqTable[word] += 1
	else:
		freqTable[word] = 1

# Creating a dictionary to keep the score
# of each sentence
sentences = sent_tokenize(text)
sentenceValue = dict()

for sentence in sentences:
	for word, freq in freqTable.items():
		if word in sentence.lower():
			if sentence in sentenceValue:
				sentenceValue[sentence] += freq
			else:
				sentenceValue[sentence] = freq



sumValues = 0
for sentence in sentenceValue:
	sumValues += sentenceValue[sentence]

# Average value of a sentence from the original text

average = int(sumValues / len(sentenceValue))

# Storing sentences into our summary.
summary = ''
for sentence in sentences:
	if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
		summary += " " + sentence
print(summary)
