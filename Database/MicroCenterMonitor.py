import requests
import re
import time
from dhooks import Webhook, Embed

url = 'Product Page URL'
dCordWebhook = 'Webhook URL'
dCordLogsWebhook = 'Webhook URL'

def PostDiscord(itemTitle,itemImage,itemStock,itemPrice):

	hook = Webhook(dCordWebhook)
	embed = Embed(title=f'{itemTitle}',url=f'{url}', timestamp='now', color=0x11b668)
	print(itemImage)
	embed.set_image(itemImage)
	embed.add_field(name='Stock', value=f'**{itemStock.upper()}**')
	embed.add_field(name='Price', value=f'**{itemPrice}**')
	embed.set_author(name='vMonitors MicroCenter Monitor')
	embed.set_footer(text='vMonitors')
	hook.send(embed=embed)

def PostDiscordLog(err):

	hook = Webhook(dCordLogsWebhook)
	embed = Embed(title=f'vMonitors MicroCenter Monitor',url=f'{url}', timestamp='now', color=0x11b668)

	embed.add_field(name='Status', value=f'**Online**')
	embed.add_field(name='Issues', value=f'**{err}**')

	embed.set_author(name='vMonitors MicroCenter Monitor')
	embed.set_footer(text='vMonitors')
	hook.send(embed=embed)

def TitleOut(getPage):
	titleParse = ""

	if getPage.text.find('og:title" content="') != -1:
		getTitle = getPage.text.find('og:title" content="')
		titleParse = (getPage.text[(getTitle+19) : (getTitle+200)])

	titleFixed = re.split(r'<|/|>| - Micro Center|\"', titleParse)
	return titleFixed[0]

def ImageOut(getPage):
	imageParse = ""

	if getPage.text.find('<img class= "productImageZoom" src="') != -1:
		getImage = getPage.text.find('<img class= "productImageZoom" src="')
		imageParse = (getPage.text[(getImage+36) : (getImage+250)])

	imageFixed = re.split(r'>|\"', imageParse)
	return imageFixed[0]

def PriceOut(getPage):
	priceParse = ""

	if getPage.text.find('<span><span id=\'pricing2\' content="') != -1:
		getPrice = getPage.text.find('<span><span id=\'pricing2\' content="')
		priceParse = (getPage.text[(getPrice+35) : (getPrice+90)])

	priceFixed = re.split(r'<|/|>|\"', priceParse)
	return priceFixed[0]


def StockOut(getPage):
	StockParse = ""

	if getPage.text.find('<span class="storeInStock">(') != -1:
		getStock = getPage.text.find('<span class="storeInStock">(')
		StockParse = (getPage.text[(getStock+28) : (getStock+58)])

	StockFixed = re.split(r"<|/|>|\)|\"", StockParse)
	return StockFixed[0]

def Main():
	print("MicroCenter Monitor Online")
	err = "None"
	PostDiscordLog(err)
	while True:
		try:
			headers = {
			   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", 
			   "Accept-Encoding": "gzip, deflate, br",
			   "Accept-Language": "en-US,en;q=0.5",
			   "Connection": "keep-alive",
			   "TE" : "Trailers",
			   "Upgrade-Insecure-Requests": "1", 
			   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
			   }
			getPage = requests.get(url, headers=headers, timeout=(60))

			item_dict = {
				"Title" : TitleOut(getPage),
				"ImageURL" : ImageOut(getPage),
				"Stock" : StockOut(getPage),
				"Price" : "$"+PriceOut(getPage),
			}
			if item_dict['Stock'] != "Sold Out":
				PostDiscord(item_dict['Title'],item_dict['ImageURL'],item_dict['Stock'],item_dict['Price'])
				print(item_dict['Title'],item_dict['ImageURL'],item_dict['Stock'],item_dict['Price'])

		except:
			err = "Server IP POSSIBLY BANNED"
			PostDiscordLog(err)
		
		time.sleep(30)

Main()
