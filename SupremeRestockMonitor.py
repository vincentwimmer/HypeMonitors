#Feel Free to use/sell/republish this code!
import requests
import re
import time
import threading
import gc
from dhooks import Webhook, Embed


headers = {
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", 
	"Accept-Encoding": "gzip, deflate, br",
	"Accept-Language": "en-US,en;q=0.5",
	"Connection": "keep-alive",
	"TE" : "Trailers",
	"Upgrade-Insecure-Requests": "1", 
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
	}

url = "https://www.supremenewyork.com/shop/new"

dCordLogsWebhook = "url to webhook"
dCordWebhook = "url to webhook"

def getItemInfo(newDropURL):
	try:
		try:
			ProductPage = requests.get(newDropURL,headers=headers, timeout=(6))
		except:
			ProductPage = requests.get(newDropURL,headers=headers, timeout=(6))

		ProductPageHTML = ProductPage.text
		AllSizes = []
		Stock = True

		try:
			#Get Product Name
			try:
				if ProductPageHTML.find('itemprop="name">') != -1:
					getProductName = ProductPageHTML.find('itemprop="name">')
					ProductNameParse = (ProductPageHTML[(getProductName+16) : (getProductName+200)])
					ProductNameFixed = re.split(r'<|\"', ProductNameParse )
			except:
				post_log(f'{url} Cant find name',url)
				pass

			#Check Sizes/Stock
			pos = -1
			while True:
				if ProductPageHTML.find('<option value="') != -1:
					pos = ProductPageHTML.find('<option value="', pos + 1)
					ProductSizeParse = (ProductPageHTML[(pos+15) : (pos+150)])
					ProductSizeFixed = re.split(r'<|\"|>', ProductSizeParse)
					AllSizes.append(ProductSizeFixed[2])
					if pos == -1:
						break
				else:
					break
				
			try:
				del AllSizes[-1]
			except:
				pass

			try:
				if (len(AllSizes)) == 0:
					AllSizes.append("Out of Stock")	
					Stock = False
			except:
				post_log(f'{url} Cant set OOS',url)
				pass

			#Get Color
			try:
				if ProductPageHTML.find('<p class="style protect" itemprop="model">') != -1:
					getProductColor = ProductPageHTML.find('<p class="style protect" itemprop="model">')
					ProductColorParse = (ProductPageHTML[(getProductColor+42) : (getProductColor+200)])
					ProductColorFixed = re.split(r'<|\"|>', ProductColorParse )
			except:
				post_log(f'{url} Cant find color',url)
				pass

			#Get Image
			try:
				if ProductPageHTML.find('<img itemprop="image" id="img-main" alt="') != -1:
					getProductImage = ProductPageHTML.find('<img itemprop="image" id="img-main" alt="')
					ProductImageParse = (ProductPageHTML[(getProductImage+41) : (getProductImage+400)])
					ProductImageFixed = re.split(r'<|\"|>|src=', ProductImageParse)
			except:
				post_log(f'{url} Cant find image',url)
				pass


			return [ProductNameFixed[0], Stock, AllSizes,ProductColorFixed[0],"https:"+ProductImageFixed[3]]

		except:
			post_log(f'{url} Get product failed',url)
	except:
		getItemInfo(newDropURL)
	

def loadNew(url):
	AllCatUrls = []

	try:
		getLatestDrop = requests.get(url, headers=headers, timeout=(6))

		if getLatestDrop.ok:

			LatestDrop = getLatestDrop.text

			try:
				pos = -1
				while True:
					if LatestDrop.find('<a style="height:81px;" href="') != -1:
						pos = LatestDrop.find('<a style="height:81px;" href="', pos + 1)
						URLParse = (LatestDrop[(pos+30) : (pos+150)])
						URLFixed = re.split(r'<|\"|>', URLParse)
						AllCatUrls.append("https://www.supremenewyork.com"+URLFixed[0])
						if pos == -1:
							break
					else:
						break
					
				del AllCatUrls[-1]

				return AllCatUrls
			except:
				return AllCatUrls
		else:
			print("Connection Error")
			post_log(f'{url} CONNECTION ERROR! Check VPN.',url)
			return None
	except:
		return None

def post_log(message,Name):    
	hook = Webhook(dCordLogsWebhook)
	embed = Embed(title=Name,url='https://www.supremenewyork.com/shop/new', description='', timestamp='now', color=0x11b668)
	embed.add_field(name='Message', value=message)
	embed.set_author(name='vMonitors Supreme')
	embed.set_footer(text='vMonitors')

	#Attempts 2 sends JUST in case
	try:
		hook.send(embed=embed)
	except:
		try:
			hook.send(embed=embed)
		except:
			print("Err on log send")


def PostDiscord(itemName,itemStock,itemSizes,itemColor,itemImage,itemStatus,itemLink):

	hook = Webhook(dCordWebhook)
	
	embed = Embed(title="Supreme-US", url=itemLink, color=0x11b668, timestamp='now')	

	if(itemStatus == "RESTOCK"):
		embed.add_field(name="RESTOCK", value=itemName,inline=False)
	elif(itemStatus == "NEW"):
		embed.add_field(name="NEW", value=itemName,inline=False)

	embed.add_field(name='Sizes', value='\n'.join(itemSizes))
	embed.add_field(name="Link", value=itemLink,inline=False)
	#embed.set_thumbnail(itemImage)
	embed.set_image(itemImage)
	embed.set_author(name='vMonitors Supreme')
	embed.set_footer(text='vMonitors')
	
	try:
		#Try sending twice JUST in case.
		try:
			hook.send(embed=embed)
		except:
			hook.send(embed=embed)
	except Exception as e:
		try:
			post_log(e, itemName)
		except:
			post_log(e, "Error")

def Main(url):
	oldItemDict = {}
	newItemDict = {}
	swapItemDict = {}
	oldItems = None

	while oldItems == None:
		oldItems = loadNew(url)
		try:
			for x in range(len(oldItems)):
				item = getItemInfo(oldItems[x])
				itemUpdate = {oldItems[x]:item}
				oldItemDict.update(itemUpdate)
		except:
			pass

	print(oldItemDict)

	print("SupMon Online.")
	post_log(f'{url} Monitor has started.',url)

	while True:
		newItems = loadNew(url)
		
		swapItemDict.clear()

		if newItems != None:
			for x in range(len(newItems)):
				item = getItemInfo(newItems[x])
				itemUpdate = {newItems[x]:item}
				newItemDict.update(itemUpdate)

				NewInfo = (newItemDict.get(newItems[x]))

				try:
					OldInfo = (oldItemDict.get(newItems[x]))
				except:
					OldInfo = []

				if OldInfo == []:
					OldInfo = [None, False, ['Out of Stock'], None, None]

				try:
					if NewInfo[1] == True and (NewInfo[1] != OldInfo[1]):
						print("Restock!", NewInfo[0])
						itemName = NewInfo[0]
						itemStock = NewInfo[1]
						itemSizesPre = NewInfo[2]
						itemSizes = itemSizesPre[:len(itemSizesPre)//2]
						itemColor = NewInfo[3]
						itemImage = NewInfo[4]
						itemStatus = "RESTOCK"
						itemLink = newItems[x]

						PostDiscord(itemName,itemStock,itemSizes,itemColor,itemImage,itemStatus,itemLink)
				except Exception as e:
					try:
						post_log(e, NewInfo[0])
					except:
						post_log(e, "Error")

				try:
					if len(NewInfo[2]) > len(OldInfo[2]):
						print("Restock!", NewInfo[0])
						itemName = NewInfo[0]
						itemStock = NewInfo[1]
						itemSizesPre = NewInfo[2]
						itemSizes = itemSizesPre[:len(itemSizesPre)//2]
						itemColor = NewInfo[3]
						itemImage = NewInfo[4]
						itemStatus = "RESTOCK"
						itemLink = newItems[x]

						PostDiscord(itemName,itemStock,itemSizes,itemColor,itemImage,itemStatus,itemLink)
				except Exception as e:
					try:
						post_log(e, NewInfo[0])
					except:
						post_log(e, "Error")

				try:
					if ((NewInfo[0] and NewInfo[1]) != OldInfo):
						print("New Item", NewInfo[0])
						itemName = NewInfo[0]
						itemStock = NewInfo[1]
						itemSizesPre = NewInfo[2]
						itemSizes = itemSizesPre[:len(itemSizesPre)//2]
						itemColor = NewInfo[3]
						itemImage = NewInfo[4]
						itemStatus = "NEW"
						itemLink = newItems[x]

						PostDiscord(itemName,itemStock,itemSizes,itemColor,itemImage,itemStatus,itemLink)
				except Exception as e:
					try:
						post_log(e, NewInfo[0])
					except:
						post_log(e, "Who knows")

				swapItemDict.update(itemUpdate)

			oldItemDict.clear
			gc.collect()
			oldItemDict.update(swapItemDict)
			time.sleep(25)
		else:
			print("newItems Returned [None]")
			time.sleep(10)

main_thread = threading.Thread(target=Main, name='Main Thread {}'.format(0), args=(url,))

main_thread.start()

print("SupMon Starting.")
