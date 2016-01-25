#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on Jan 14, 2016

@author: "Pengyi Pan"
'''
import io, os

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
    <link rel="shortcut icon" href="image/siteIcon.ico">

    <!-- Bootstrap -->
    <link href='css/bootstrap.min.css' rel='stylesheet'>

    <!-- CSS -->
    <link href='css/index.css' rel='stylesheet'>
    <link rel="stylesheet" href="css/animate.min.css">
    <!-- //CSS -->
    
    <script src="js/wow.min.js"></script>
    <script>
        setTimeout(function() {
          new WOW().init();
        },2000);      
    </script>

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src='https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js'></script>
      <script src='https://oss.maxcdn.com/respond/1.4.2/respond.min.js'></script>
    <![endif]-->
  </head>
  <body>
    <!-- whole page container -->
    <div class='container-fluid' id='whole-page-container'>

      
      <!-- title bar row -->
      <div class='col-md-12'>

        <nav class="navbar navbar-default navbar-fixed-top">
          <div class="container-fluid">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
              <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
              </button>
              <a class="navbar-brand" href="#"><img id= 'navbar-logo' alt='Logo' src="image/siteIcon.ico"/></a>
              <a class="navbar-brand" href="#">看完豆瓣250没</a>
            </div>            

            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
              <ul class="nav navbar-nav navbar-right">
                  <form class="navbar-form navbar-left" role="search">
                    <button type="button" class="btn btn-default login-btn" data-toggle="modal" data-target="#myModal">登录</button>
                  </form>
                <li class="dropdown">
                  <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false"> <span class="glyphicon glyphicon-user" aria-hidden="true"><span class="caret"></span></a>
                  <ul class="dropdown-menu">
                    <li><a href="#">帐号设置</a></li>
                    <li role="separator" class="divider"></li>
                    <li><a href="#">登出</a></li>
                  </ul>
                </li>
              </ul>
            </div><!-- /.navbar-collapse -->

          </div>
        </nav>

      </div>
      <!-- //title bar row -->
      <!-- movies section -->
      <div class='col-md-12 movies-container' id='movies-container'>
        
      </div>
      <!-- movies section -->
      <div id='loading'></div>
        
        <!-- Modal -->
        <div id="myModal" class="modal fade" role="dialog">
          <div class="modal-dialog modal-lg">

            <!-- Modal content-->
            <div class="modal-content">
              <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal">&times;</button>
                <h4 class="modal-title">登录</h4>
              </div>
              <div class="modal-body">
                <p>用cookie登录</p>
                <p>用cookie登录</p>
                <p>用cookie登录</p>
                <p>用cookie登录</p>
                <p>用cookie登录</p>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
              </div>
            </div>

          </div>
        </div>      
      


    </div>
    <!-- //whole page container -->


    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src='js/jquery.min.js'></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src='js/bootstrap.min.js'></script>
    <script type="text/javascript" src="js/index.js"></script>
  </body>
</html>"""



#end of header

def readFiles():
    
    global html
    
    #read all crawler result files
    tdir = "../crawlerResult/"
    fileList = [ n for n in os.listdir(tdir) if n.endswith(".txt") ] 
    
    fileBuffer = ""
    
    for fileName in fileList:
        with io.open('../crawlerResult/' + fileName,'r',encoding='utf8') as f:
            
            lines = [line.rstrip('\n') for line in f]
            for line in lines:
                fileBuffer+= line + "\n"        
            f.close() 
    
    
    #generate html
    
    num_lines = sum(1 for line in fileBuffer.splitlines())
        
    lineCounter = 0
    for line in fileBuffer.splitlines():
        
        if lineCounter % (7*6) == 0: #start of one row - 6 items
            html += "<!-- movies row -->\n<div class='col-md-12 movie-row '>\n<div class='row-container'>\n"
        
        if lineCounter % 7 == 0: #start of one item
            html += "<div class='col-md-2 darken animated zoomIn wow' id='" + line + "'>\n\t"
        
        if lineCounter % 7 ==1: #img url
            html += "<img src='" + line + "' class='movie-cover-img img-responsive' alt='movie cover'/>\n\t"
            
        if lineCounter % 7 ==2: #title
            html += "<span class='movie-title-main'>" + line + "</span>\n\t"
            
#         if lineCounter % 7 ==3: #director and genre
#             html += "<span class='directors'><h4><small>" + line + "</small></h4></span>\n\t"
            
        if lineCounter % 7 ==4: #rating
            
            good = "progress-bar-success"
            mid = "progress-bar-warning"
            bad = "progress-bar-danger"
                        
            rating = float(line)
            
            barStyle = ""
            
            if rating >= 9.0:
                barStyle = good
            elif rating >= 8.5:
                barStyle = mid
            else:
                barStyle = bad
                       
            percentage = (10-3.5*(10 - rating))*10
            
            html += "<span class='rating-bar-block'>\n\t\t<div class='progress rating-bar'>\n\t\t\t<div class='progress-bar progress-bar-striped active " 
            html += barStyle + "' role='progressbar' aria-valuenow='40' aria-valuemin='0' aria-valuemax='100' style='width:" + str(percentage) +"%' >\n\t\t\t\t"
            html += str(rating) + "\t\t\n"
            html += "\t\t\t</div>\n\t\t</div>\n\t</span>\n\t"
#             
#         if lineCounter % 7 ==5: #num of comments
#             html += "<span class='commentNum'>" + line + '</span>\n\t'
            
        if lineCounter % 7 ==6: # description
            html += "<span class='description'>" + line + '</span>\n\t' 
            
        lineCounter += 1
        
        if lineCounter % 7 == 0: #end of one item
            html += "<span class='rank-num'><div class='badge'>" + str(lineCounter/7) + "</div></span>\n\t"
            html += "<span class='add-img-container'><img src='image/add-png.png' class='add-img'></img></span>\n\t"
            html += "<span class='delete-img-container'><img src='image/delete-png.png' class='delete-img'></img></span>\n"
            html += '</div>\n' 

        if lineCounter % (7*6) == 0: #finished one row - 6 items
            html += "</div>\n</div>\n<!-- //movies row -->\n" 
            
        if lineCounter == num_lines: #last line of buffer
            if lineCounter % (7*6) == 0: #finished one row - 6 items
                pass                            
            else:
                html += "</div>\n</div>\n<!-- //movies row -->\n" 
                

def mergeTwohtml(fileHandle):
    searchLine = "<div class='col-md-12 movies-container' id='movies-container'>\n"
    
    i = otherHtml.index(searchLine) + len(searchLine) # Make sure searchline is actually in the file
    
#     result = otherHtml[:i] + html + otherHtml[i:]
     
    fileHandle.write(otherHtml[:i].decode('utf-8')); 
    fileHandle.write(html);
    fileHandle.write(otherHtml[i:].decode('utf-8'));
    
def generateWebsite():
    
    with io.open('../website/index.html','w+',encoding='utf8') as f:
        
        readFiles()
        mergeTwohtml(f)
    
        
    f.close()      

if __name__ == '__main__':
    
    generateWebsite()
    
    print "Finished!"
    

