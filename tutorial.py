import bs4                                         #am using bs4 for beautiful soap
import requests
#url='https://en.wikipedia.org/wiki/Amitabh_Bachchan'
url="https://beta.nseindia.com/"
data= requests.get(url)                            #extract all data from that url and saving it in data named element
soup=bs4.BeautifulSoup(data.text, 'html.parser')   #here am using html parsing only with bs4 libraries
print(soup.prettify())                             #it will take all the content of my url and put it on my browser window
for para in soup.find_all('p'):                    #to print all para<p>
    print(para.text)
#=============================================================================

# for links in soup.find_all('a'):                    #to extraxt all url links
#       link=links.get('href')
#       print(link)
#==============================================================================
    # if link[0:3]=="../" and link!="#":                     #to remove un nessasary links start fron #,/,None etc
    #     print("https://en.wikipedia.org"+ link[2:len(link)])
    # elif link[0]=="/" and link!="#":
    #     print("https://en.wikipedia.org" + link)
    # elif link!="#":
    #     print(link)
    # elif link!="None":
    #     print(link)
#============================================================================
# for links in soup.find_all("a"):           #logic to get links of youtube videos
#     link=links.get("href")
#     if (link[0:3]=="/wa"):
#        print("http://www.youtube.com"+link)

