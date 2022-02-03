from a_scrape import Amazon_Scrape
from messaging import Messaging


text = '\u20b9'
amazon_scrape = Amazon_Scrape()

data = f'''Book : {amazon_scrape.bookname}
Author : {amazon_scrape.author}
Price : Rs.{amazon_scrape.price.split(text)[1]}'''
print(data)


msg = Messaging()
msg.send(msg_stuff = data)

msg.email(body_text=data)








