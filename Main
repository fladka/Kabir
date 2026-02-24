import requests
from feedgen.feed import FeedGenerator

def generate_kabir_feed():
    # 1. Fetch data from the Kabir Dohe API
    url = "https://kabir-ke-dohe-api.vercel.app/api/couplets?popular=true"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to fetch data")
        return
        
    data = response.json()
    
    # 2. Initialize the RSS Feed
    fg = FeedGenerator()
    fg.title('Daily Kabir Das Dohas')
    fg.link(href='https://github.com/fladka/Kabir', rel='alternate')
    fg.description('Timeless wisdom and couplets by Sant Kabir Das')
    fg.language('hi')
    
    # 3. Add entries (pulling the top 5 popular dohas)
    for doha in data[:5]:
        fe = fg.add_entry()
        fe.title(doha.get('couplet_hindi', 'Kabir Doha'))
        
        meaning = doha.get('explanation', 'No meaning provided.')
        translation = doha.get('translation', 'No translation provided.')
        
        content = f"<p><strong>Meaning:</strong> {meaning}</p><p><strong>Translation:</strong> {translation}</p>"
        fe.description(content)
        fe.id(str(doha.get('_id', doha.get('couplet_hindi'))))
        fe.link(href="https://github.com/fladka/Kabir")
        
    # 4. Save the file
    fg.rss_file('rss.xml')
    print("RSS feed generated successfully!")

if __name__ == '__main__':
    generate_kabir_feed()
