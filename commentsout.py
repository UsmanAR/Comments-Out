import sys
import requests
from bs4 import BeautifulSoup 
banner="""
:'######:::'#######::'##::::'##:'##::::'##:'########:'##::: ##:'########::'######::::::'#######::'##::::'##:'########:
'##... ##:'##.... ##: ###::'###: ###::'###: ##.....:: ###:: ##:... ##..::'##... ##::::'##.... ##: ##:::: ##:... ##..::
 ##:::..:: ##:::: ##: ####'####: ####'####: ##::::::: ####: ##:::: ##:::: ##:::..::::: ##:::: ##: ##:::: ##:::: ##::::
 ##::::::: ##:::: ##: ## ### ##: ## ### ##: ######::: ## ## ##:::: ##::::. ######::::: ##:::: ##: ##:::: ##:::: ##::::
 ##::::::: ##:::: ##: ##. #: ##: ##. #: ##: ##...:::: ##. ####:::: ##:::::..... ##:::: ##:::: ##: ##:::: ##:::: ##::::
 ##::: ##: ##:::: ##: ##:.:: ##: ##:.:: ##: ##::::::: ##:. ###:::: ##::::'##::: ##:::: ##:::: ##: ##:::: ##:::: ##::::
. ######::. #######:: ##:::: ##: ##:::: ##: ########: ##::. ##:::: ##::::. ######:::::. #######::. #######::::: ##::::
:......::::.......:::..:::::..::..:::::..::........::..::::..:::::..::::::......:::::::.......::::.......::::::..::::: 
======================================================================================================================
  Made by @UsmanAR \n  Github - https://github.com/UsmanAR 
======================================================================================================================"""
print(banner)
n=len(sys.argv)
if(n!=2):
	print("\nUSAGE :  python3 commentout.py <hostname>\n")
	exit()
host=sys.argv[1]
if(host=="-h"):
	print("\nUSAGE : python3 commentout.py <hostname>\n        python3 commentout.py [-h] : print this\n")
	exit()
response= requests.get("http://"+host)
print("\033[92m"  + "\n\nEXTRACTING COMMENTS [+]\n\n" + "\033[00m")
html=response.text
n=len(sys.argv)
soup = BeautifulSoup(html,features="html.parser")
content=soup.prettify
i=0
j=0
group= ""
comment=""
finder=True
ender=False
final=""
end_group=""
writer = False
counter = 0
for text in str(content): 
	if (text=="<"):
		finder=True
	if(finder):
		if(i<=3):
			group= group + text
			if(group=="<!--"):
				writer = True
			i=i+1
		else: 
			finder= False
			group=""
			i=0
	if(writer):
		comment=comment + text
	if(text=="-"):
		ender=True
	if(ender):
		if(j<=2):
			end_group=end_group+text
			if(end_group=="-->"):
				final =  final + comment 
				final=final+ "\n\n" + "<!-" 
				group=""
				end_group=""
				comment=""
				writer =False
				counter+=1
				ender=False
			j=j+1
		else: 
			ender=False
			end_group=""
			j=0
if(counter==0):
	print('\033[31m' + 'NO COMMENTS FOUND\n' + '\033[0m') 
else:
	print("\033[92m" + "**********  COMMENTS FOUND ************* \n \n" + "\033[00m")
	print("<!-" + final + "->")
	print(f"\nTotal number of comments found : {counter}.")
	print("\n")

