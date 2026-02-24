import requests
from feedgen.feed import FeedGenerator

def generate_kabir_feed():
    url = "https://kabir-ke-dohe-api.vercel.app/api/couplets?popular=true"
    
    # 1. Initialize the feed first so it ALWAYS exists
    fg = FeedGenerator()
    fg.title('Daily Kabir Das Dohas')
    fg.link(href='https://github.com/fladka/Kabir', rel='alternate')
    fg.description('Timeless wisdom and couplets by Sant Kabir Das')
    fg.language('hi')

    try:
        response = requests.get(url)
        data = response.json()
        
        # 2. Aggressively hunt for the list of dohas
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
        
    # 3. If no dohas are found, create a fallback entry so the file is still generated
    if not couplets:
        print("Warning: Creating a placeholder because no dohas were found.")
        fe = fg.add_entry()
        fe.title('Kabir Feed Setup Successful')
        fe.description('Your feed is active! Waiting for the API to provide the next doha.')
        fe.link(href='https://github.com/fladka/Kabir')
    else:
        # 4. Add the actual dohas
        for doha in couplets[:5]:
            fe = fg.add_entry()
            fe.title(doha.get('couplet_hindi', 'Kabir Doha'))
            
            meaning = doha.get('explanation', 'No meaning provided.')
            translation = doha.get('translation', 'No translation provided.')
            
            content = f"<p><strong>Meaning:</strong> {meaning}</p><p><strong>Translation:</strong> {translation}</p>"
            fe.description(content)
            fe.id(str(doha.get('_id', doha.get('couplet_hindi'))))
            fe.link(href="https://github.com/fladka/Kabir")
            
    # 5. Save the file (This will now ALWAYS happen)
    fg.rss_file('rss.xml')
    print("RSS feed generated successfully!")

if __name__ == '__main__':
    generate_kabir_feed()
