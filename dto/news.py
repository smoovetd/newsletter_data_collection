from datetime import datetime


class News:
    '''News - class that holds properties for each one of the news.'''
    def __init__(self, date:datetime, name:str, link:str, labels:list, content:str ) -> None:
       self.set_date(date)
       self.set_name(name) 
       self.set_link(link)
       self.labels = list()
       self.set_labels(labels)
       self.set_content(content) 

    def set_date(self, date: datetime) -> None:
        self.date = date    

    def get_date(self) -> datetime:
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
        print('test')
        res = ''
        res += f'\tDate - {self.get_date()}\n'
        res += f'\tName - {self.get_name()}\n'
        res += f'\tLink - {self.get_link()}\n'
        res += f'\tLabels - {self.get_labels()}\n'
        res += f'\tContent - {self.get_content()}\n'   
        return res 