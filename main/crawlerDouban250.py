#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on Jan 14, 2016

@author: "Pengyi Pan"
'''
import urllib2
from bs4 import BeautifulSoup
import io

#number of movies to crawl

_startRank = 51      #inclusive (can pick 1,26,51,76...201,226)

_endRank = 75       #inclusive


def crawlAndGenerateRow(startRank,endRank,resultFile):
    
    print "crawling " + str(startRank) + "-" + str(endRank)
     
    output = ""
    
    rankNum = startRank - 1
     
    while 1:
                   
        url = "http://movie.douban.com/top250?start=" + str(rankNum) + "&filter="

        htm = urllib2.urlopen(url)
        soup = BeautifulSoup(htm,"html.parser")  
        itemSet = soup.findAll('div',attrs = {"class":"item"})
        
        #each loop produce a movie
        for item in itemSet:
#             print item

            rankNum += 1
            output += str(rankNum) + "\n"
            
            #Fetch img urls
            
            #get img result from youku
            
            ultNameToUse = item.find('span',attrs = {"class":"title"}).string
            
            youkuUrl = "http://www.soku.com/v?keyword=" + ultNameToUse.encode(encoding='UTF-8',errors='strict')
            youkuUrl = youkuUrl.replace(' ','%')

            youkuHtm = urllib2.urlopen(youkuUrl)          
            imgSoup = BeautifulSoup(youkuHtm,"html.parser")
            
            imgClass = imgSoup.find('div',attrs = {"class":"s_target"})
            
            if imgClass is not None: #movie exists
                
                                
                tempStr = imgClass.find('img')['src']
                if tempStr == "http://g1.ykimg.com/0900641F464A7BBE7400000000000000000000-0000-0000-0000-00005B2F7B0E": #“无预览图”
                    imgName = item.find('img')
                    output += imgName['src']
                else:
                    output += tempStr
                        
            #//get img result from youku
            else:

                imgName = item.find('img')
                output += imgName['src']
                            
            output += '\n' 
             
            #Fetch Titles
            nameSet = item.findAll('span',attrs = {"class":"title"})
            otherNameSet = item.findAll('span',attrs = {"class":"other"})
            allNames = ""
            for name in nameSet:
                nameStr = name.string
                allNames += nameStr
                break

#             for otherName in otherNameSet:
#                 otherNameStr = otherName.string              
#                 allNames += otherNameStr

            allNames = allNames.replace('  ', ' ')
            
            output += allNames + '\n'
            
            #Fetch director and genre
            directorSpans = item.find('div',attrs = {"class":"bd"}).find('p')
            dirStr = ""
            for dirSpan in directorSpans:
                dirStr += dirSpan.string
            resultStr="" 
            dirStr.splitlines() 

            for line in dirStr:
                resultStr += line  
            resultStr = resultStr.replace('\n','')
            resultStr = resultStr.replace('                            ','')
            resultStr = resultStr.replace('...',' ')
            resultStr = resultStr.replace('                        ','')
            
            output += resultStr + '\n'  
            
            #Fetch rating (out of 10)
            rating = item.find('span',attrs = {"class":"rating_num"})
            output += rating.string + '\n'
            
            #Fetch comment number short description
            comResult=""
            commentSpan = item.findAll('span')
            for span in commentSpan[-2]:
                spanStr = span.string
                if spanStr is None:
                    continue
                comResult += spanStr + '\n'
            output += comResult

            #Fetch short description
            desResult = ""
            for span in commentSpan[-1]:
                spanStr = span.string
                if spanStr is None:
                    continue
                desResult += spanStr + '\n'            
            output += desResult
            
            
            print "Finished #" + str(rankNum)  
            
            if rankNum == endRank:
                break    
              
        if rankNum == endRank:
            break
    
    resultFile.write(output)
        

     


def crawl(startRank,endRank):
    
#     #clear result directory
#     cdir = os.getcwd()
#     tdir = "../crawlerResult/"
#     os.chdir(tdir)
#     filelist = [ f for f in os.listdir(".") if f.endswith(".txt") ]   
#     for f in filelist:
#         os.remove(f)
#     
#     os.chdir(cdir)
#     #//clear result directory
    
    
    
    numOfResultFile = (endRank-startRank)/25 + 1
     
    for fileNum in range(numOfResultFile):
         
        fileName = "result_" + str(startRank/25 + fileNum) + ".txt"
     
        with io.open('../crawlerResult/' + fileName,'w+',encoding='utf8') as f:
             
            tempStart = startRank + fileNum * 25
            tempEnd = tempStart + 25 - 1
             
            if _endRank - tempStart < 25:
                tempEnd = _endRank              
                        
            crawlAndGenerateRow(tempStart,tempEnd,f)
      
          
              
        f.close()    
    
                            
    

if __name__ == '__main__':
    
    crawl(_startRank,_endRank)
                 
    print "===================="
    print "     All done"
    print "===================="
