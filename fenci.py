# encoding: utf-8

from wordcloud import WordCloud
import jieba
import PIL
import matplotlib.pyplot as plt
import numpy as np
import json
import sys

def  WordCount(wordList):
	wordDict = {}
	wordSet = set(wordList)
	for word in wordSet:
		wordDict[word] = wordList.count(word)
	del wordDict["\r\n"]
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
	wordcloud.to_file('./output/Squere(all).jpg')
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
	wordcloud.to_file('./output/Mask(all).jpg')
	# plt.imshow(wordcloud)
	# plt.axis("off")
	# plt.show()

def main():
	reload(sys)
	sys.setdefaultencoding( "utf-8" )
	wordList = []
	file = open(r'./input/xiedu(all).txt' , 'r').read()
	words = list(jieba.cut(file))
	for word in words:
		if len(word) > 1:
			wordList.append(word)
	WordCount(wordList)
	txt = r' '.join(wordList)
	#print wordList
	WordCloudSquere(txt)
	WordCloudPlot(txt)
	# print txt

if __name__ == '__main__':
	main()
