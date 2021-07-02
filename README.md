# HypeMonitors

Above is a collection of monitors I've made for tracking drops and restocks of hard to find, rare, or in-demand products.

Please note, I am releasing these because they're almost all defunct and no longer work. And I am no longer maintaining them.

If you plan on forking these to rebuild and use, be sure to run them with a proxy and/or VPN

### Supreme Restock Monitor
> This monitor tracks stocks and restocks of all products under the "New" category then drops a notification to an assigned Discord channel.

### Supreme Community Monitor
> Twice a week, Wednesday and again Thursday morning (this time with updated prices), the monitor fetches the upcoming Supreme drop and unloads it to a designated Discord channel. It also posts the Top 5 voted items for the week to a second Discord channel.

### SNKRS Monitor
> This monitor does not track restocks but instead tracks announcements of upcoming drops and sends the annoucement to an assigned Discord channel. 
> - Discord Webhooks are managed through **vmonitorsSNKRSUsers.json**
> - Proxies are managed through **proxies.txt**
> - Useragents are managed through **useragents.txt**

### Shopify Monitor
> This monitor takes a list of Shopify stores and creates a thread for each one. It then pulls the products.json file on each store and looks for changes. There are also filters put in place to designate certain items or brands to their own Discord channels. 
> - Discord Webhooks are managed through **vmonitorsShopifyUsers.json** 
> - Stores are managed through **ShopifyShops.txt**
> - Proxies are managed through **proxies.txt**
> - Useragents are managed through **useragents.txt**

### Micro Center Monitor
> This is the simplest of the monitors. Edit the code with your Webhooks for Discord and then drop in a full product page URL from Micro Center's website and run it. You can take it upon yourself to introduce Threading and things like that with the code laid out in the Shopify Monitor. Also, it only tracks if the product is in stock or not, but doesn't track the store. Feel free to add that too, you can find a breakdown of each store's availablility by outputting **Line 90's getPage.content** to a txt file and searching for:
> - <span class="storeInStock">
