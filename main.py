from bs4 import BeautifulSoup
import requests

url = 'https://www.airbnb.com.co/s/Bogot%C3%A1--Colombia/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=5&query=Bogot%C3%A1%2C%20Colombia&place_id=ChIJKcumLf2bP44RFDmjIFVjnSM&date_picker_type=calendar&checkin=2023-01-14&checkout=2023-01-18&source=structured_search_input_header&search_type=autocomplete_click'
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')

elements = soup.select('.gh7uyir.giajdwt.g14v8520.dir.dir-ltr div')
print(len(elements))
