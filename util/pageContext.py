# coding:utf-8

from util.doubleLinkList import Node,DoublyLinkedList


class PageContext(object):
    def __init__(self,val):
        self.pageDic = {}
        self.doubleLink = DoublyLinkedList()
        self.doubleLink.clear()
        
        for i in val:
            
            self.pageDic[i.id] = i
            self.doubleLink.append(i.id)

    
    def getPageContext(self,i):
        
        # print(self.pageDic.get(i))
        a = self.doubleLink.getByData(i)
        # print(a)
        prev = ""
        next = ""
        if(type(a) == Node):
                
            prevId = a.pre.data

            nextId = a.next.data
            
            if (prevId != None and prevId != i):
                artPrev = self.pageDic.get(prevId)
                prev = '<p> \
                <a href="/gen/news_'+str(artPrev.id)+'.html">上一篇：\
                    '+artPrev.title+'</a> \
                </p>'
                print(prev)
            if (nextId != None and nextId != i):
                artPrev = self.pageDic.get(nextId)
                next = '<p> \
                <a href="/gen/news_'+str(artPrev.id)+'.html">下一篇：\
                    '+artPrev.title+'</a> \
                </p>'
                print(next) 
        return prev + next
            

