# encoding: utf-8

from wordcloud import WordCloud
import jieba
import PIL
import matplotlib.pyplot as plt
import numpy as np
import json
import sys
import jieba.posseg as pseg

def  WordCount(wordList):
	wordDict = {}
	wordSet = set(wordList)
	for word in wordSet:
		wordDict[word] = wordList.count(word)
	# del wordDict["\r\n"]
	wordDict = sorted(wordDict.iteritems(), key=lambda d:d[1], reverse = True)
	#print wordDict
	file = open('./output/WordCount.txt','w')
	for word in wordDict:
		#print(json.dumps(word[0], ensure_ascii=False, encoding='UTF-8')) ,word[1]
		file.write(word[0])
		file.write(" ")
		file.write(str(word[1]))
		file.write("\n")
	file.close()

def WordCloudSquere(txt):
	wordcloud = WordCloud(font_path='./ttf/manhua.ttf', 
		background_color="black", 
		margin=5, width=1600, height=900) 
	wordcloud = wordcloud.generate(txt)
	wordcloud.to_file('./output/Squere.jpg')
	# plt.imshow(wordcloud)
	# plt.axis("off")
	# plt.show()

def WordCloudPlot(txt):
	path='./ttf/manhua.ttf'
	path=unicode(path, 'utf8').encode('gb18030')
	Mask = np.array(PIL.Image.open('./input/xiedu.png'))
	wordcloud = WordCloud(font_path=path, 
		background_color="black",   
		margin=5, width=1600, height=900,mask=Mask,max_words=100,max_font_size=500,random_state=200) 
	wordcloud = wordcloud.generate(txt)
	wordcloud.to_file('./output/Mask.jpg')
	# plt.imshow(wordcloud)
	# plt.axis("off")
	# plt.show()

def main():
	reload(sys)
	sys.setdefaultencoding( "utf-8" )
	wordList = []
	file = open(r'./input/xiedu.txt' , 'r').read()
	words = list(pseg.cut(file))
	cixing=["x","zg","uj","ul","e","d","uz","y","r","m"]
	# for w in words:
	# 	print("%s %s" %(w.word, w.flag))
	# for w in words:
	# 	f = 1;
	# 	for ci in cixing:
	# 		if w.flag == ci:
	# 			f = 0;
	# 			break;
	# 	if f == 1:
	# 		print("%s %s" %(w.word, w.flag))
	# 		wordList.append(w.word)
	for w in words:
		if w.flag == "n":
			wordList.append(w.word)
		# if w.flag == "v":
		# 	wordList.append(w.word)
	# print wordList
	WordCount(wordList)
	txt = r' '.join(wordList)
	#print wordList
	WordCloudSquere(txt)
	WordCloudPlot(txt)
	# print txt

if __name__ == '__main__':
	main()
