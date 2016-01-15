#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on Jan 14, 2016

@author: "Pengyi Pan"
'''
import codecs

def createNumTag(stri):
    


    return 

if __name__ == '__main__':
    

    with codecs.open('../crawlerResult/douban250.txt','r','utf-8') as f:
        lines = f.read().splitlines()
        for line in lines:
            if line == "":
                print "haha"
            
            
            print line
            
            if 'AllFinished' in line:
                break
            
    f.close()