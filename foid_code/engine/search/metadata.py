import json
import numpy as np

class DocumentDTO():
    def __init__(self, id, size,totalPages, creator, keywords, producer, title, creationDate): 
        self.id = id
        self.size = size
        self.totalPages = totalPages
        self.creator = creator
        self.keywords = keywords
        self.producer = producer
        self.title = title
        self.creationDate = creationDate
        self.pages=[]

    def addPage(self,page):
        self.pages.append(page)

    def convert_to_json(self,obj):
        if isinstance(obj,PageDTO):
            return {
                "id":obj.id,
                "size":obj.size,
                "totalPages":obj.totalPages,
                "creator":obj.creator,
                "keywords":obj.keywords,
                "producer":obj.producer,
                "title":obj.title,
                "creationDate":obj.creationDate,
                "pages":obj.pages,
            }
        raise TypeError(f"Object of type {type(obj)} is not JSON serializable")


    def reprJSON(self):
        return dict(id=self.id, size = self.size, totalPages = self.totalPages, creator = self.creator, keywords = self.keywords, producer = self.producer, title = self.title, creationDate = self.creationDate, pages= self.pages) 

class PageDTO():
    def __init__(self, id,pageNumber):
        self.id=id
        self.pageNumber=pageNumber
        self.images=[]
       
    def addImage(self,image):
        self.images.append(image)
  

    def reprJSON(self):
        return dict(id=self.id, pageNumber = self.pageNumber,images=self.images)


class ImageDTO():
    def __init__(self, id,position,score,width,height):
        self.id=id
        self.position=position
        self.score=score
        self.width=width
        self.height=height
        self.objects=[]
        self.texts= []
        self.tables=[]
        self.texts=[]
        self.lists=[]
        self.titles=[]
        self.figures=[]
    def addObject(self,object):
        self.objects.append(object)
    def addTexts(self,text):
        self.texts.append(text)
    def addTables(self, image):
        self.tables.append(image)
    def addText(self, image):
        self.texts.append(image)
    def addLists(self, image):
        self.lists.append(image)
    def addTitles(self, image):
        self.titles.append(image)
    def addFigure(self, image):
        self.figures.append(image)

    def reprJSON(self):
        return dict(id=self.id, position=self.position, score=self.score, width=self.width,objects=self.objects,height=self.height, texts=self.texts,tables=self.tables,lists=self.lists,titles=self.titles,figures=self.figures)

class ObjectDTO():
    def __init__(self, id,name,position,score):
        self.id=id
        self.name=name
        self.position=position
        self.score=score
    
    def reprJSON(self):
        return dict(id=self.id, name=self.name, position=self.position, score=self.score)

class FigureDTO():
    def __init__(self, id, name, position, score,objects):
        self.id = id
        self.name = name
        self.position = position
        self.score = score
        self.objects=objects

    def reprJSON(self):
        return dict(id=self.id, name=self.name, position=self.position, score=self.score,objects=self.objects)

class  TextDTO():
    def __init__(self, id, name, position, score,content=""):
        self.id = id
        self.name = name
        self.position = position
        self.score = score
        self.content = content

    def reprJSON(self):
        return dict(id=self.id, name=self.name, position=self.position, score=self.score,content=self.content)

class  ListDTO():
    def __init__(self, id, name, position, score,content=""):
        self.id = id
        self.name = name
        self.position = position
        self.score = score
        self.content = content

    def reprJSON(self):
        return dict(id=self.id, name=self.name, position=self.position, score=self.score,content=self.content)


class  TableDTO():
    def __init__(self, id, name, position, score,content=""):
        self.id = id
        self.name = name
        self.position = position
        self.score = score
        self.content = content

    def reprJSON(self):
        return dict(id=self.id, name=self.name, position=self.position, score=self.score,content=self.content)


class Position():
    def __init__(self, x1,x2,y1,y2):
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2

    def reprJSON(self):
        return dict(x1=self.x1, x2=self.x2, y1=self.y1, y2=self.y2)

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.reprJSON()


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (np.int_, np.intc, np.intp, np.int8,
                            np.int16, np.int32, np.int64, np.uint8,
                            np.uint16, np.uint32, np.uint64)):
            return int(obj)
        elif isinstance(obj, (np.float_, np.float16, np.float32,
                              np.float64)):
            return float(obj)
        elif isinstance(obj, (np.ndarray,)):
            return obj.tolist()
        return obj.reprJSON()
