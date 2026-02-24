import requests
from feedgen.feed import FeedGenerator

def generate_kabir_feed():
    url = "https://kabir-ke-dohe-api.vercel.app/api/couplets?popular=true"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to fetch data")
        return
        
    data = response.json()
    
    # NEW FIX: Safely unwrap the dictionary to find the list of dohas
    couplets = []
    if isinstance(data, dict):
        # Look for common list keys the API might use
        for key in ['couplets', 'data', 'results']:
            if key in data and isinstance(data[key], list):
                couplets = data[key]
                break
    elif isinstance(data, list):
        couplets = data
        
    if not couplets:
        print("Could not find the couplets in the API response.")
        return
    
    fg = FeedGenerator()
    fg.title('Daily Kabir Das Dohas')
    fg.link(href='https://github.com/fladka/Kabir', rel='alternate')
    fg.description('Timeless wisdom and couplets by Sant Kabir Das')
    fg.language('hi')
    
    # We now slice 'couplets' instead of 'data'
    for doha in couplets[:5]:
        fe = fg.add_entry()
        fe.title(doha.get('couplet_hindi', 'Kabir Doha'))
        
        meaning = doha.get('explanation', 'No meaning provided.')
        translation = doha.get('translation', 'No translation provided.')
        
        content = f"<p><strong>Meaning:</strong> {meaning}</p><p><strong>Translation:</strong> {translation}</p>"
        fe.description(content)
        fe.id(str(doha.get('_id', doha.get('couplet_hindi'))))
        fe.link(href="https://github.com/fladka/Kabir")
        
    fg.rss_file('rss.xml')
    print("RSS feed generated successfully!")

if __name__ == '__main__':
    generate_kabir_feed()
