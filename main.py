import requests
import datetime
from feedgen.feed import FeedGenerator

def generate_kabir_feed():
    url = "https://kabir-ke-dohe-api.vercel.app/api/couplets?popular=true"
    
    fg = FeedGenerator()
    fg.title('Daily Kabir Das Dohas')
    fg.link(href='https://github.com/fladka/Kabir', rel='alternate')
    fg.description('Timeless wisdom and couplets by Sant Kabir Das')
    fg.language('hi')

    try:
        response = requests.get(url)
        data = response.json()
        
        couplets = []
        if isinstance(data, dict):
            for val in data.values():
                if isinstance(val, list):
                    couplets = val
                    break
        elif isinstance(data, list):
            couplets = data
            
    except Exception as e:
        print(f"Failed to fetch from API: {e}")
        couplets = []
        
    # Get the current time to satisfy T-UI's strict parser
    current_time = datetime.datetime.now(datetime.timezone.utc)
        
    if not couplets:
        fe = fg.add_entry()
        fe.title('Kabir Feed Setup Successful')
        fe.description('Your feed is active! Waiting for the API to provide the next doha.')
        fe.link(href='https://github.com/fladka/Kabir')
        fe.pubDate(current_time)
    else:
        for i, doha in enumerate(couplets[:5]):
            fe = fg.add_entry()
            fe.title(doha.get('couplet_hindi', 'Kabir Doha'))
            
            meaning = doha.get('explanation', 'No meaning provided.')
            translation = doha.get('translation', 'No translation provided.')
            
            content = f"<p><strong>Meaning:</strong> {meaning}</p><p><strong>Translation:</strong> {translation}</p>"
            fe.description(content)
            fe.id(str(doha.get('_id', doha.get('couplet_hindi'))))
            fe.link(href="https://github.com/fladka/Kabir")
            
            # Add the required timestamp, offset slightly for each doha
            item_time = current_time - datetime.timedelta(minutes=i)
            fe.pubDate(item_time)
            
    fg.rss_file('rss.xml')
    print("RSS feed generated successfully!")

if __name__ == '__main__':
    generate_kabir_feed()
        
