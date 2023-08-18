import pandas as pd
import requests
from bs4 import BeautifulSoup
Mobile_name = []
Prices= []
Description = []
Reviews = []

for i in range(2,12):
    url ="https://www.flipkart.com/search?q=mobile+phone+5g+under+50000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_22_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_22_na_na_na&as-pos=2&as-type=RECENT&suggestionId=mobile+phone+5g+under+50000%7CMobiles&requestId=49b90fc2-08cf-498d-bf33-818ddcfcab06&as-searchtext=mobile+phone+5g+under+50000&page="+str(i)
    r = requests.get(url)
    #print(r)
    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div",class_="_1YokD2 _3Mn1Gg")

    names = box.find_all("div",class_="_4rR01T")
    for i in names:
        name = i.text
        Mobile_name.append(name)
    #print(Mobile_name)

    prices = box.find_all("div",class_="_30jeq3 _1_WHN1")
    for i in prices:
        name = i.text
        Prices.append(name)
    #print(Prices) 

    desc = box.find_all("ul",class_="_1xgFaf")
    for i in desc:
        name =i.text
        Description.append(name)
    #print(Description)    

    reviews = box.find_all("div",class_="_3LWZlK")
    for i in reviews:
        name = i.text
        Reviews.append(name)
    #print(Reviews)
df = pd.DataFrame({"Mobile Name": Mobile_name,"Prices":Prices,"Description":Description,"Reviews":Reviews})
#print(df)
df.to_csv("flipkart_mobiles_5g_under_50000.csv")
















    
    #print(soup)
    #np = soup.find("a",class_="_1LKTO3").get("href") #np = next page
    #cnp ="https://www.flipkart.com"+np               #cnp = complete next page
    #print(cnp)

