from datetime import datetime
from pydantic import BaseModel

class WebNews(BaseModel):
    date:str 
    name:str 
    link:str 
    labels:list 
    content: str 

class News():
    '''News - class that holds properties for each one of the news.'''
    def __init__(self, date:str, name:str, link:str, labels:list, content:str ) -> None:
       print(f'In HERE!!!{date};{name};{link};{labels};{content}')
       self.set_date(date)
       self.set_name(name) 
       self.set_link(link)
       self.labels = list()
       self.set_labels(labels)
       self.set_content(content) 

    def set_date(self, date: str) -> None:
        self.date = date    

    def get_date(self) -> str:
        return self.date 

    def set_name(self, name: str) -> None:
        self.name = name    

    def get_name(self) -> str:
        return self.name 

    def set_link(self, link: str) -> None:
        self.link = link    

    def get_link(self) -> str:
        return self.link 

    def set_labels(self, labels: list) -> None:
        self.labels = labels    

    def get_labels(self) -> list:
        return self.labels 

    def set_content(self, content: str) -> None:
        self.content = content    

    def get_content(self) -> str:
        return self.content

    def get_news_info(self) -> str:
        '''Returns string of all properties of News instance'''
        res = ''
        res += f'\tDate - {self.get_date()}\n'
        res += f'\tName - {self.get_name()}\n'
        res += f'\tLink - {self.get_link()}\n'
        res += f'\tLabels - {self.get_labels()}\n'
        res += f'\tContent - {self.get_content()}\n'   
        return res 

    def get_news_dict(self) -> str:
        res = dict()
        res['date'] = self.get_date()
        res['name'] = (self.get_name())
        res['link'] = (self.get_link())
        res['labels'] = str(self.get_labels())
        res['content'] = (self.get_content())   
        return res        