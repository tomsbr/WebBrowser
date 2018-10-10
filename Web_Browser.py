import webbrowser
import time
techUrls = ["https://outlook.office.com/owa/?realm=dukes.jmu.edu&exsvurl=1&ll-cc=1033&modurl=0&path=/mail/inbox", "https://canvas.jmu.edu/", 
"https://accounts.qryptos.com/?continue=https://home.qryptos.com/fund", "https://gist.github.com/mrliptontea/4c793ebdf72ed145bcbf"]

socialMediaUrls = ["www.netflix.com", "www.coinbase.com", 
"https://www.binance.com/trade.html?symbol=VEN_BTC", "", ""]

def open_tabs(url_list):
	for element in url_list:
		webbrowser.open_new_tab(element)

def main():
	webbrowser.open("www.youtube.com", new=2, autoraise=False)
	time.sleep(1)
	open_tabs(techUrls)
	open_tabs(socialMediaUrls)

main()