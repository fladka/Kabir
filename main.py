import datetime
from feedgen.feed import FeedGenerator

def generate_kabir_feed():
    # THE DOHA LIBRARY
    couplets = [
        {"couplet_hindi": "काल करे सो आज कर, आज करे सो अब । पल में प्रलय होएगी, बहुरि करेगा कब ॥", "explanation": "Do tomorrow's work today, and today's work right now.", "translation": "Tomorrow's work do today, today's work now. If the moment is lost, how will the work be done?"},
        {"couplet_hindi": "बुरा जो देखन मैं चला, बुरा न मिलिया कोय । जो दिल खोजा आपना, मुझसे बुरा न कोय ॥", "explanation": "I searched the world for bad people but found none. When I looked inside my own heart, I realized I am the worst of all.", "translation": "I went searching for the wicked, but found no one. When I searched my own heart, I found no one worse than me."},
        {"couplet_hindi": "दुख में सुमिरन सब करे, सुख में करै न कोय । जो सुख में सुमिरन करे, दुख काहे को होय ॥", "explanation": "Everyone remembers God in sorrow, no one remembers in joy. If one remembers God in joy, why would sorrow ever come?", "translation": "In sorrow everyone remembers Him, in joy no one does. If one remembers Him in joy, why would sorrow come?"},
        {"couplet_hindi": "गुरु गोविंद दोऊ खड़े, काके लागूं पाँय । बलिहारी गुरु आपने, गोविंद दियो बताय ॥", "explanation": "Both Guru and God are standing before me, whose feet should I touch first? I bow to my Guru.", "translation": "Guru and God both are standing, whose feet should I touch? I surrender to my Guru who introduced me to God."},
        {"couplet_hindi": "माटी कहे कुम्हार से, तु क्या रौंदे मोय । एक दिन ऐसा आएगा, मैं रौंदूगी तोय ॥", "explanation": "The clay says to the potter, 'Why do you trample me? A day will come when I will trample you.'", "translation": "Clay says to the potter, why do you knead me? A day will come when I will knead you."},
        {"couplet_hindi": "ऐसी बानी बोलिए, मन का आपा खोय । औरन को शीतल करे, आपहुं शीतल होय ॥", "explanation": "Speak such words that you lose your ego. Words that cool the listener and cool yourself.", "translation": "Speak such words that you lose your ego. It cools others and cools yourself too."},
        {"couplet_hindi": "पोथी पढ़ि पढ़ि जग मुआ, पंडित भया न कोय । ढाई आखर प्रेम का, पढ़े सो पंडित होय ॥", "explanation": "Reading books, the world died, no one became wise. One who reads the two and a half letters of 'Love' becomes wise.", "translation": "Reading books the world died, none became a scholar. He who reads the two and a half letters of Love, becomes a scholar."},
        {"couplet_hindi": "बड़ा हुआ तो क्या हुआ, जैसे पेड़ खजूर । पंथी को छाया नहीं, फल लागे अति दूर ॥", "explanation": "What is the use of being big like a date tree? It gives no shade to travelers and its fruits are too high to reach.", "translation": "What if you are big, like the date palm tree. No shade for the traveler, and fruit grows too far."},
        {"couplet_hindi": "धीरे-धीरे रे मना, धीरे सब कुछ होय । माली सींचे सौ घड़ा, ॠतु आए फल होय ॥", "explanation": "Slowly, oh mind, everything happens slowly. The gardener may water with a hundred pots, but fruit only comes in its season.", "translation": "Slowly my mind, slowly everything happens. The gardener waters a hundred pots, but fruit arrives only in its season."},
        {"couplet_hindi": "सांईं इतना दीजिये, जा मे कुटुम समाय । मैं भी भूखा न रहूँ, साधु ना भूखा जाय ॥", "explanation": "Oh God, give me only enough to feed my family. So I do not go hungry, and no guest goes hungry from my door.", "translation": "Lord, give me only this much, that my family is sustained. I shouldn't remain hungry, nor should a saint go hungry."},
        {"couplet_hindi": "निंदक नियरे राखिए, ऑंगन कुटी छवाय । बिन पानी, साबुन बिना, निर्मल करे सुभाय ॥", "explanation": "Keep your critics close, give them a hut in your yard. Without soap or water, they cleanse your character.", "translation": "Keep the critic close to you, build him a hut in your courtyard. Without water or soap, he cleanses your nature."},
        {"couplet_hindi": "कबीरा सूता क्या करे, जागी न जपे मुरार । एक दिन ऐसा सोवना, लंबे पाँव पसार ॥", "explanation": "Kabir, why do you sleep? Wake up and remember God. One day you will sleep a long sleep with your legs stretched out (death).", "translation": "Kabir, what do you do sleeping? Wake up and chant God's name. One day you must sleep like this, legs stretched far."},
        {"couplet_hindi": "जैसे तिल में तेल है, ज्यों चकमक में आग । तेरा साईं तुझ में है, तू जाग सके तो जाग ॥", "explanation": "Just as oil is inside the sesame seed, and fire is in the flint stone. Your God is inside you, wake up if you can.", "translation": "Like oil in sesame, like fire in flint. Your Lord is within you, awake if you can awake."},
        {"couplet_hindi": "जिन खोजा तिन पाइया, गहरे पानी पैठ । मैं बपुरा बूडन डरा, रहा किनारे बैठ ॥", "explanation": "Those who searched, found it by diving into deep water. I, the poor one, was afraid of drowning and sat on the shore.", "translation": "Those who searched, found it by diving deep. I, poor fellow, feared drowning, and sat on the shore."},
        {"couplet_hindi": "कबीरा खड़ा बाज़ार में, मांगे सबकी खैर । ना काहू से दोस्ती,न काहू से बैर ॥", "explanation": "Kabir stands in the market, wishing well for everyone. He has friendship with no one, and enmity with no one.", "translation": "Kabir stands in the market, praying for everyone's welfare. Neither friendship with anyone, nor enmity with anyone."}
    ]

    current_time = datetime.datetime.now(datetime.timezone.utc)
    hours_since_epoch = int(current_time.timestamp() // 3600)
    index = hours_since_epoch % len(couplets)
    doha = couplets[index]
    
    # 1. NEW: T-UI PLAIN TEXT EXPORT
    text_output = f"""
====================================
           KABIR DOHA            
====================================
{doha['couplet_hindi']}

MEANING:
{doha['explanation']}

TRANSLATION:
{doha['translation']}
====================================
"""
    with open('doha.txt', 'w', encoding='utf-8') as f:
        f.write(text_output)

    # 2. EXISTING: RSS EXPORT
    fg = FeedGenerator()
    fg.title('Hourly Kabir Das Dohas')
    fg.link(href='https://github.com/fladka/Kabir', rel='alternate')
    fg.description('Timeless wisdom by Sant Kabir Das')
    fg.language('hi')

    for i in range(3):
        idx = (hours_since_epoch - i) % len(couplets)
        d = couplets[idx]
        fe = fg.add_entry()
        title = d.get('couplet_hindi', 'Kabir Doha')
        fe.title(title)
        fe.description(f"<p>Meaning: {d.get('explanation', '')}</p><p>Translation: {d.get('translation', '')}</p>")
        fe.id(title + str(hours_since_epoch - i))
        fe.link(href="https://github.com/fladka/Kabir")
        item_time = current_time.replace(minute=0, second=0, microsecond=0) - datetime.timedelta(hours=i)
        fe.pubDate(item_time)

    fg.rss_file('rss.xml')
    print("Hourly Text and RSS feeds generated successfully!")

if __name__ == '__main__':
    generate_kabir_feed()
        
