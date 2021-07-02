import requests
import re
import time
import datetime
import threading
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

url = "https://www.supremecommunity.com/season/fall-winter2020/droplists/"

#This allows you to drop the Top5 voted items of the week into their own channel.
dCordWebhook = "url to webhook"
dCordTop5Webhook = "url to webhook"

def getInfo(newDropURL):
	itemData = []

	getDropInfo = requests.get(newDropURL, headers=headers)
	dropInfo = getDropInfo.text

	itemImgSrc = None
	itemTitle = None
	itemPrice = None
	itemUpvotes = None
	itemDownvotes = None
	itemWeek = None

	if dropInfo.find('<div class="col-sm-10 col-md-8">') != -1:
		getItemWeek = dropInfo.find('<div class="col-sm-10 col-md-8">')
		itemWeekParse = (dropInfo[(getItemWeek+32) : (getItemWeek+165)])
		itemWeekFixed = re.split(r'<|\"|Droplist ', itemWeekParse)
		itemWeekGB = itemWeekFixed[2]
		itemWeekGB = re.split(r' ', itemWeekGB)
		itemWeek = str(itemWeekGB[1] + " " + itemWeekGB[0] + " " + "20"+itemWeekGB[2])

	pos = -1
	while True:
		if dropInfo.find('<div class="card card-2">') != -1:
			pos = dropInfo.find('<div class="card card-2">', pos + 1)
			itemHTML = (dropInfo[(pos+25) : (pos+6000)])

			if itemHTML.find('<img class="prefill-img" alt=') != -1:
				getItemImg = itemHTML.find('<img class="prefill-img" alt=')
				itemImgParse = (itemHTML[(getItemImg+30) : (getItemImg+500)])
				itemImgFixed = re.split(r'<|\"|src=', itemImgParse)
				itemImgSrc = "https://www.supremecommunity.com"+itemImgFixed[3]

			if itemHTML.find('<h2 class="name item-details item-details-title">') != -1:
				getItemTitle = itemHTML.find('<h2 class="name item-details item-details-title">')
				itemTitleParse = (itemHTML[(getItemTitle+49) : (getItemTitle+200)])
				itemTitleFixed = re.split(r'<|\"', itemTitleParse)
				itemTitle = itemTitleFixed[0]

			if itemHTML.find('<span class="label-price">') != -1:
				getItemPrice = itemHTML.find('<span class="label-price">')
				itemPriceParse = (itemHTML[(getItemPrice+26) : (getItemPrice+400)]).replace(" ", "")
				itemPriceFixed = re.split(r'<|\"|\n', itemPriceParse)
				itemPrice = itemPriceFixed[1]

			if itemHTML.find('<p class="upvotes hidden">') != -1:
				getItemUpvotes = itemHTML.find('<p class="upvotes hidden">')
				itemUpvotesParse = (itemHTML[(getItemUpvotes+26) : (getItemUpvotes+34)])
				itemUpvotesFixed = re.split(r'<|\"', itemUpvotesParse)
				itemUpvotes = itemUpvotesFixed[0]

			if itemHTML.find('<p class="downvotes hidden">') != -1:
				getItemDownvotes = itemHTML.find('<p class="downvotes hidden">')
				itemDownvotesParse = (itemHTML[(getItemDownvotes+28) : (getItemDownvotes+35)])
				itemDownvotesFixed = re.split(r'<|\"', itemDownvotesParse)
				itemDownvotes = itemDownvotesFixed[0]			

			itemData.append([itemImgSrc, itemTitle, itemPrice, itemUpvotes, itemDownvotes, itemWeek])

			if pos == -1:
				break
		else:
			break
	
	return itemData
	

def loadDrop(url):
	DropURLFixed = []

	getLatestDrop = requests.get(url, headers=headers)
	LatestDrop = getLatestDrop.text
	try:
		if LatestDrop.find('<div class="col-sm-4 col-xs-12 app-lr-pad-2" id="box-latest">\n                                        <a href=') != -1:
			getDropURL = LatestDrop.find('<div class="col-sm-4 col-xs-12 app-lr-pad-2" id="box-latest">\n                                        <a href=')
			DropURLParse = (LatestDrop[(getDropURL+111) : (getDropURL+250)])
			DropURLFixed = re.split(r'<|\"', DropURLParse )
	except:
		pass

	newDropURL = "https://www.supremecommunity.com" + DropURLFixed[0]

	print(newDropURL)

	dropInfo = getInfo(newDropURL)

	return dropInfo


def PostDiscord(dropItem,itype):
	embed = Embed(title="SupremeCommunity", url="https://www.supremecommunity.com/", description=f'Week: **{dropItem[5]}**', color=0x11b668, timestamp='now')

	embed.add_field(name=dropItem[1], value=f'🟢 Upvotes: **{dropItem[3]}** \n \n🔴 Downvotes: **{dropItem[4]}** \n ')

	keyword = re.split(r" ", dropItem[1])
	keyword1 = ",+"
	keyword2 = " +"
	keyword3 = ", "
	keywordT1 = "+"+keyword1.join(keyword)
	keywordT2 = "+"+keyword2.join(keyword)
	keywordT3 = " "+keyword3.join(keyword)
	
	embed.add_field(name="Keywords", value=f'{keywordT1}\n{keywordT2}\n{keywordT3}\n',inline=False)

	embed.add_field(name="Price", value=f'**`{dropItem[2]}`**',inline=False)

	#embed.set_thumbnail(itemImage)
	embed.set_image(dropItem[0])

	embed.set_author(name='vMonitors SupremeCommunity')
	embed.set_footer(text='vMonitors')

	if itype == "Reg":
		hook = Webhook(dCordWebhook)
		hook.send(embed=embed)

	if itype == "Top5":
		hook = Webhook(dCordTop5Webhook)
		hook.send(embed=embed)

def Main(url):
	waitWeek = datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

	while True:
		todayDate = datetime.datetime.today()
		currentWeekday = datetime.datetime.today().weekday()

		if todayDate > waitWeek and (currentWeekday == 2 or currentWeekday == 3):
			dropItems = loadDrop(url)

			dropItems.reverse()

			for x in range(len(dropItems)):
				dropItem = dropItems[x]
				itype = "Reg"
				PostDiscord(dropItem,itype)

			top5 = dropItems[-5:]

			for x in range(len(top5)):
				#print("Drake's Top5Top5")
				dropItem = top5[x]
				itype = "Top5"
				PostDiscord(dropItem,itype)

			waitWeek = datetime.datetime.today() + datetime.timedelta(days=1)

			print("SC Droplist Posted. - See ya next week! -", waitWeek)
		time.sleep(2)

main_thread = threading.Thread(target=Main, name='Main Thread {}'.format(0), args=(url,))

main_thread.start()

print("SupComDropMon Online.")
