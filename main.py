from dto.news import News
from backend.sqlite_db import DBConnection
import web_services

# test creating of records in table 
cont = 'Národná banka Slovenska (NBS) warns the public about the activities of AXE Capital Group SE, which offers investment opportunities at the following websites: https://www.instagram.com/axe.capital.group/ and https://www.facebook.com/AxeCapitalGroup/. Please note that this company is currently not subject to supervision by NBS. It is not authorised by NBS to conduct any activity in the Slovak financial market, nor is it recorded in any register maintained by NBS. Funds invested through this company are not covered by Slovakia’s Deposit Protection Fund1 or Investment Guarantee Fund.2 We continue to warn consumers interested in investing in the financial market to consider carefully before concluding a contract with a financial services provider and to check the provider against the list of authorised providers listed on the NBS website. AXE Capital Group SE has its registered office at Štúrova 27, 040 01 Košice (Staré Mesto district) and its company registration number (IČO) is 52 005 666. 1  In accordance with Act No 118/1996 on the protection of deposits (and amending certain laws), as amended. 2  In accordance with Act No 566/2001 on securities and investment services (and amending certain laws), as amended.'
crnt_news = News('2022-05-01','test_name', 'http://test.com', ['test', 'app'], cont.encode('utf8')) 

db_con = DBConnection('test.db')
db_con.insert(crnt_news.get_news_dict())
print(db_con.select_all_records())


