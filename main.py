
import pandas as pd
import requests
from bs4 import BeautifulSoup

page=requests.get('https://www.airbnb.com.co/s/Bogot%C3%A1--Colombia/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=5&query=Bogot%C3%A1%2C%20Colombia&place_id=ChIJKcumLf2bP44RFDmjIFVjnSM&date_picker_type=calendar&source=structured_search_input_header&search_type=autocomplete_click')
soup=BeautifulSoup(page.content,'lxml')

#GET URLS
uls=[]
for i in range(0,15):
    URL='https://www.airbnb.com.co/s/Bogot%C3%A1--Colombia/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=5&query=Bogot%C3%A1%2C%20Colombia&place_id=ChIJKcumLf2bP44RFDmjIFVjnSM&date_picker_type=calendar&checkin=2023-01-04&checkout=2023-02-01&source=structured_search_input_header&search_type=autocomplete_click'
    page=requests.get(URL)
    soup=BeautifulSoup(page.text,'lxml')
    next_page=soup.find('a', {'aria-label':'Siguiente'}).get('href')
    next_page_full='https://www.airbnb.com.co/'+next_page
    uls.append(next_page_full)
    URL=next_page_full
    
#MADE THE FUNCTION
URLS=[]
titles=[]
beds=[]
prices=[]
ranting=[]
def airbnb(url):
    page=requests.get(url)
    soup=BeautifulSoup(page.content,'lxml')
    boxes=soup.find_all('div', 'c4mnd7m dir dir-ltr')
    for i in boxes:
        #to get url
        url=i.find('a','bn2bl2p dir dir-ltr').get('href')
        urls_full='https://www.airbnb.com.co/'+url
        URLS.append(urls_full)
        #to Get the titles
        title=i.find('div', 't1jojoys dir dir-ltr').text
        titles.append(title)
        # getting beds
        try:
            bed=i.find('span', 'dir dir-ltr').text
            beds.append(bed)
        except:
            beds.append('n/a')
        #getting prices
        try:
            price=i.find('div', '_1jo4hgw').text
            prices.append(price)
        except:
            prices.append('n/a')
        #getting rating
        try:
            rati=i.find('span','r1dxllyb dir dir-ltr').text
            ranting.append(rati)
        except:
            ranting.append('n/a')
            
#NOW CALLING THE FUNCION
for each in uls:
    airbnb(each)
    
#DATAFRAME
dic={'URL':URLS, 'titles':titles,'beds':beds,'prices':prices,'rating':ranting}
dt=pd.DataFrame(dic)
dt.to_excel('airbnb.xlsx')
