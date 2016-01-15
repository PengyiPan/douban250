#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on Jan 14, 2016

@author: "Pengyi Pan"
'''
import urllib2
from bs4 import BeautifulSoup
import codecs
import io

# result html file

html = """"""

#other website code
otherHtml = """
<!DOCTYPE html>
<html lang='en'>
  <head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <title>看完豆瓣250没</title>

    <!-- Bootstrap -->
    <link href='css/bootstrap.min.css' rel='stylesheet'>

    <!-- CSS -->
    <link href='css/index.css' rel='stylesheet'>
    <!-- //CSS -->

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src='https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js'></script>
      <script src='https://oss.maxcdn.com/respond/1.4.2/respond.min.js'></script>
    <![endif]-->
  </head>
  <body>
    <!-- whole page container -->
    <div class='container-fluid'>
      
      <!-- title bar row -->
      <div class='col-md-12'>

        <div class='col-md-4'>
          blank
        </div>

        <div class='col-md-4'>
          title and logo
        </div>

        <div class='col-md-4'>
          sign in
        </div>

      </div>
      <!-- //title bar row -->
      <!-- movies section -->
      <div class='col-md-12 movies-container'>
        
      </div>
      <!-- movies section -->
      


    </div>
    <!-- //whole page container -->


    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src='js/jquery.min.js'></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src='js/bootstrap.min.js'></script>
  </body>
</html>"""



#end of header

def crawlAndGenerateRow(topRank):
    global html
    
    rankNum = 0
     
    while 1:
           
        url = "http://movie.douban.com/top250?start=" + str(rankNum) + "&filter="
        htm = urllib2.urlopen(url)
        soup = BeautifulSoup(htm,"html.parser")   
        itemSet = soup.findAll('div',attrs = {"class":"item"})
        
        #each loop produce a movie
        for item in itemSet:
#             print item
            if rankNum % 6 == 0:
                html += "<!-- movies row -->\n<div class='col-md-12'>\n"

            rankNum += 1
            html += "<div class='col-md-2 darken' id='" + str(rankNum) + "'>\n\t"
            
            #Fetch img urls
            imgResult = "<img src='"
            imgName = item.find('img')
            imgResult += imgName['src']
            imgResult += "' class='movie-cover-img img-responsive' alt='movie cover'>"
            html += imgResult + '\n\t' 
             
            #Fetch Titles
            nameSet = item.findAll('span',attrs = {"class":"title"})
            otherNameSet = item.findAll('span',attrs = {"class":"other"})
            allNames = ""
            for name in nameSet:
                nameStr = name.string
                nameStr = "<h2><strong>" + nameStr + "</strong></h2>"
                allNames += nameStr
                break
            allNames += "<h3><small>";
            for otherName in otherNameSet:
                otherNameStr = otherName.string              
                allNames += otherNameStr

            allNames = allNames.replace('  ', ' ')
            allNames += "</small></h3>";
            
            allNames = "<span class='movie-title-main'>" + allNames + "</span>"

            html += allNames + '\n\t'
            
            #Fetch director and genre
            directorSpans = item.find('div',attrs = {"class":"bd"}).find('p')
            dirStr = ""
            for dirSpan in directorSpans:
                dirStr += dirSpan.string
            resultStr="" 
            dirStr.splitlines() 
            resultStr += "<span class='directors'><h4><small>"
            for line in dirStr:
                resultStr += line  
            resultStr = resultStr.replace('\n','')
            resultStr = resultStr.replace('                            ','')
            resultStr = resultStr.replace('...',' ')
            resultStr += "</small></h4></span>"
            resultStr = resultStr.replace('                        ','')
            
            html += resultStr + '\n\t'  
            
            #Fetch rating (out of 10)
            rating = item.find('span',attrs = {"class":"rating_num"})
            html += "<span class='rating'>"+rating.string + '</span>\n\t'
            
            #Fetch comment number short description
            comResult="<span class='commentNum'>"
            commentSpan = item.findAll('span')
            for span in commentSpan[-2]:
                spanStr = span.string
                if spanStr is None:
                    continue
                comResult += spanStr + '</span>\n\t'
            html += comResult

            #Fetch short description
            desResult = "<span class='description'>"
            for span in commentSpan[-1]:
                spanStr = span.string
                if spanStr is None:
                    continue
                desResult += spanStr + '</span>\n'            
            html += desResult
            
            html += '</div>\n' 
            print "Finished #" + str(rankNum)  
                
            if rankNum % 6 == 0:
                
                html += "</div>\n<!-- //movies row -->\n"    
            
            if rankNum == topRank:
                if topRank%6 == 0:
                    return
                else:
                    html += "</div>\n<!-- //movies row -->\n" 
                    return
    
        
def mergeTwohtml(fileHandle):
    searchLine = "<div class='col-md-12 movies-container'>"
    
    i = otherHtml.index(searchLine) + len(searchLine) # Make sure searchline is actually in the file
    
#     result = otherHtml[:i] + html + otherHtml[i:]
     
    fileHandle.write(otherHtml[:i].decode('utf-8')); 
    fileHandle.write(html);
    fileHandle.write(otherHtml[i:].decode('utf-8'));
     

    

if __name__ == '__main__':
    
    with io.open('../website/index.html','w+',encoding='utf8') as f:
        
        crawlAndGenerateRow(24)
        finalHtml = mergeTwohtml(f)
    
        
    f.close()
             
    
    print "===================="
    print "     All done"
    print "===================="
