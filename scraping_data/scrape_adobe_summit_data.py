import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL of the Adobe Summit event page
url = "https://summit.adobe.com"
response = requests.get(url)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')
# Extracting information
event_name = "Adobe Summit"
event_dates = "March 25-28, 2024"
location = "Las Vegas, NV & Virtual"
website_url = url
description_tag = soup.find('meta', attrs={'name': 'description'})
description = description_tag['content'] if description_tag else "N/A"

# Since the website might use different classes or structures, we have to identify those correctly
# Key Speakers
key_speakers = []
speakers_section = soup.find('section', id='speakers')
if speakers_section:
    speaker_tags = speakers_section.find_all('div', class_='speaker-name')
    key_speakers = [speaker.get_text(strip=True) for speaker in speaker_tags]

# Agenda/Schedule - This part would typically be a link to a detailed agenda
agenda_schedule = "Refer to the website for detailed agenda and schedule."
# Registration Details
registration_details = "Refer to the website for registration details."
# Pricing - As prices can change, refer directly to the website for current pricing
pricing = "Refer to the website for current pricing details."
# Categories
categories = ["Digital marketing", "Customer experience", "Technology"]
# Audience Type
audience_type = ["Marketers", "Advertisers", "IT professionals"]
# Compile data into a dictionary
event_data = {
    "Event Name": [event_name],
    "Event Date(s)": [event_dates],
    "Location": [location],
    "Website URL": [website_url],
    "Description": [description],
    "Key Speakers": [', '.join(key_speakers)],
    "Agenda/Schedule": [agenda_schedule],
    "Registration Details": [registration_details],
    "Pricing": [pricing],
    "Categories": [', '.join(categories)],
    "Audience type": [', '.join(audience_type)]
}


df = pd.DataFrame(event_data)
# Save the DataFrame to a CSV file
df.to_csv('adobe_summit_2024.csv', index=False)
print(df)
