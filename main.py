import datetime
from feedgen.feed import FeedGenerator

def generate_kabir_feed():
    # THE DOHA LIBRARY (PART 1)
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
        {"couplet_hindi": "कबीरा गर्व ना कीजिये, काल गहे कर केश । ना जानों कहाँ मारिसी, क्या घर क्या परदेश ॥", "explanation": "Do not be proud; death has you by the hair. You know not where it will strike, whether at home or in a foreign land.", "translation": "Be not proud, death holds your hair. You know not where it strikes, at home or elsewhere."},
        {"couplet_hindi": "दुर्लभ मानुष जन्म है, देह न बारम्बार । तरुवर ज्यों पत्ती झड़े, बहुरि न लागे डार ॥", "explanation": "Human birth is rare; this body is not gained again and again. Like a leaf falls from a tree and never returns to the branch.", "translation": "Human life is rare, it comes not again. Like a fallen leaf that never returns to the branch."},
        {"couplet_hindi": "जग में बैरी कोई नहीं, जो मन शीतल होय । यह आपा तो डारि दे, दया करे सब कोय ॥", "explanation": "No one is your enemy if your mind is calm. If you drop your ego, everyone will show you compassion.", "translation": "No one is your foe if your mind is cool. Drop your ego, and the world will be kind to you."},
        {"couplet_hindi": "साईं से लगन लगाये रख, फल की इच्छा त्याग । जब समय आएगा तेरा, बदल जाएगा भाग ॥", "explanation": "Keep your devotion to the Lord and give up the desire for fruits. When your time comes, your fate will change.", "translation": "Stay devoted to the Lord, forget the reward. When the time is right, your luck will turn."},
        {"couplet_hindi": "सबै रसायन मैं किया, प्रेम समान न कोय । रंचक ही में तन तपे, कंचन सा तन होय ॥", "explanation": "I have tried all elixirs, but none is like Love. Even a little makes the body shine like pure gold.", "translation": "I tried all potions, but none like love. A tiny bit transforms the body into gold."},
        {"couplet_hindi": "कबीरा संगत साधु की, ज्यों गंधी की बास । जो कुछ गंधी दे नहीं, तो भी बास सुबास ॥", "explanation": "The company of a saint is like a perfume seller. Even if he gives you nothing, the fragrance stays with you.", "translation": "Company of a saint is like a perfumer. Even if he gives nothing, the scent remains."},
        {"couplet_hindi": "माली आवत देख के, कलियन करे पुकार । फूले-फूले चुन लिये, काल्हि हमारी बार ॥", "explanation": "Seeing the gardener coming, the buds cry out. He picked all the flowers today; tomorrow it will be our turn.", "translation": "Seeing the gardener, the buds cry: He picked the flowers today, tomorrow is our turn."},
        {"couplet_hindi": "चाह मिटी चिंता मिटी, मनवा बेपरवाह । जिसको कछू न चाहिए, वो साहन के साह ॥", "explanation": "Desire ended, worry ended, the mind became carefree. He who wants nothing is the king of kings.", "translation": "Desire and worry gone, the mind is free. He who wants nothing is the king of kings."},
        {"couplet_hindi": "जा घट प्रेम न संचरे, सो घट जान मसान । जैसे खाल लुहार की, सांस लेत बिनु प्रान ॥", "explanation": "A heart without love is like a cremation ground. Like the blacksmith's bellows, it breathes without life.", "translation": "A heart without love is a graveyard. It breathes like bellows, but has no life."},
        {"couplet_hindi": "कहता हूँ कहि जात हूँ, कहूँ जो ठोक बजाय । कुआँ पास है आपणे, तू क्यों प्यासा जाय ॥", "explanation": "I say it again and again, and I say it with certainty. The well is near you; why do you remain thirsty?", "translation": "I tell you truly, the well is right here. Why do you still wander with thirst?"},
        {"couplet_hindi": "साधु शब्द समुद्र है, जामें रत्न अपार । मूरख भेद न जानहीं, ढूँढत फिरे किनार ॥", "explanation": "The words of a saint are an ocean filled with gems. Fools don't know the secret and look only on the shore.", "translation": "A saint's word is an ocean of gems. Fools know not the secret and stay on the shore."},
        {"couplet_hindi": "चिंता ऐसी डाकिनी, काटि कलेजा खाय । बैद बिचारा क्या करे, कहाँ तक दवा लगाय ॥", "explanation": "Worry is such a witch that she eats the heart. What can the poor doctor do? How far can medicine reach?", "translation": "Worry is a witch that eats the heart. What can a doctor do? Medicine cannot reach it."},
        {"couplet_hindi": "तन को जोगी सब करें, मन को बिरला कोय । सहजै सब सिधि पाइए, जो मन जोगी होय ॥", "explanation": "Everyone makes the body a yogi, but rarely anyone makes the mind one. All success is easy if the mind becomes a yogi.", "translation": "Many discipline the body, few the mind. All is achieved if the mind is disciplined."},
        {"couplet_hindi": "हाड़ जलै ज्यों लाकड़ी, केस जलै ज्यों घास । सब जग जलता देखि करि, भये कबीर उदास ॥", "explanation": "Bones burn like wood, hair burns like grass. Seeing the whole world burning (in worldliness), Kabir became sad.", "translation": "Bones burn like wood, hair like grass. Seeing the world burn, Kabir is saddened."},
        {"couplet_hindi": "कबीर लहरि समंद की, मोती बिखरे आइ । बगुला भेद न जानई, हंसा चुनि-चुनि खाइ ॥", "explanation": "The waves of the ocean bring pearls to the shore. The crane doesn't know their value, but the swan picks them up.", "translation": "Waves bring pearls to the shore. The crane knows not, the swan picks them up."},
        {"couplet_hindi": "पाहन पूजे हरि मिले, तो मैं पूजूं पहार । ताते यह चाकी भली, पीस खाय संसार ॥", "explanation": "If worshipping a stone finds God, I'll worship a mountain. Better is the grinding stone that feeds the world.", "translation": "If stones find God, I'll worship a hill. Better is the millstone that feeds the world."},
        {"couplet_hindi": "कबीर आपा मेटि करि, हरि भजि तजि अभिमान । जिहि घट दया न संचरे, सो घट जान मसान ॥", "explanation": "Kabir, erase your ego and worship God, leaving pride. A heart without compassion is a cremation ground.", "translation": "Kabir, kill the ego and pray. A heart without mercy is a graveyard."},
        {"couplet_hindi": "जाको राखे साइयां, मारि सके न कोय । बाल न बांका करि सके, जो जग बैरी होय ॥", "explanation": "He whom God protects, no one can kill. Not a hair can be harmed, even if the whole world is an enemy.", "translation": "Whom God protects, none can slay. Not a hair is harmed if the world is a foe."},
        {"couplet_hindi": "कबीरा संगत साधु की, कदे न निरफल होय । लोहा कंचन होत है, जो पारस परसे कोय ॥", "explanation": "Company with a saint never goes in vain. Just as iron turns to gold when it touches the philosopher's stone.", "translation": "Company of a saint is never wasted. Iron turns to gold by the touch of the stone."},
        {"couplet_hindi": "लूटि सके तो लूट ले, राम नाम की लूट । पाछे ही पछताओगे, प्राण जाहिंगे छूटि ॥", "explanation": "Gather the name of God while you can. You will regret it later when life leaves your body.", "translation": "Gather God's name now. You will regret it when life departs."},
        {"couplet_hindi": "कबीर सोया क्या करे, उठि न भजे भगवान । जम जब घर में आइसी, तब नहिं जपे कमान ॥", "explanation": "Kabir, why do you sleep? Wake up and pray. When Death enters your house, you won't be able to pray.", "translation": "Kabir, why sleep? Wake up and pray. When Death arrives, you cannot pray."},
        {"couplet_hindi": "कबीरा गरब न कीजिये, ऊँचा देखि आवास । काल परों भुईं लेटना, ऊपर जमसी घास ॥", "explanation": "Do not be proud of your high mansion. Tomorrow you will lie in the dust, and grass will grow over you.", "translation": "Be not proud of your high home. Tomorrow you lie in dust, covered in grass."},
        {"couplet_hindi": "रात गंवाई सोय के, दिवस गंवाया खाय । हीरा जनम अमोल था, कौड़ी बदले जाय ॥", "explanation": "The night was lost in sleep, the day in eating. This diamond-like life was priceless, but it's going for a penny.", "translation": "Night lost to sleep, day to food. This priceless life is sold for a penny."},
        {"couplet_hindi": "कबीरा तेलिन के बैल को, घर ही कोस पचास । सवेरे उठा फिर वहीं, साँझ हुई तो पास ॥", "explanation": "The oilman's bull travels fifty miles but stays in the same place. He starts and ends in the same spot.", "translation": "The oilman's bull walks miles but stays put. He ends where he began."},
        {"couplet_hindi": "फल कारन सेवा करे, तजे न मन से काम । कह कबीर सेवक नहीं, चहै चोगुना दाम ॥", "explanation": "One who serves for reward and doesn't give up desire is not a servant; he wants four times the price.", "translation": "He who serves for reward is no servant; he only wants a higher price."},
        {"couplet_hindi": "जो तोको कांटा बुवै, ताहि बोय तू फूल । तोको फूल के फूल हैं, बाको है तिरशूल ॥", "explanation": "If someone sows thorns for you, sow flowers for them. You will get flowers, and they will get thorns.", "translation": "If one sows thorns, sow flowers. You get flowers, they get thorns."},
        {"couplet_hindi": "कबीर दर्शन साधु के, बड़े भाग से होय । जो कछु किया सोई मिला, अब कछु और न कोय ॥", "explanation": "Meeting a saint happens through great fortune. What you did is what you got; there is nothing else now.", "translation": "Meeting a saint is great luck. You get what you gave; nothing more remains."},
                {"couplet_hindi": "साधु ऐसा चाहिये, जैसा सूप सुभाय । सार-सार को गहि रहै, थोथा देइ उड़ाय ॥", "explanation": "A saint should be like a winnowing basket. It keeps the essence and blows away the hollow chaff.", "translation": "A saint should be like a winnowing fan. Keep the truth, blow away the false."},
        {"couplet_hindi": "माला फेरत जुग भया, फिरा न मन का फेर । कर का मनका डारि दे, मन का मनका फेर ॥", "explanation": "A whole age passed turning beads, but the mind didn't turn. Drop the wooden beads and turn the beads of the heart.", "translation": "Years passed turning beads, the mind didn't change. Drop the beads, turn the heart."},
        {"couplet_hindi": "कबीरा खड़ा बाज़ार में, मांगे सबकी खैर । ना काहू से दोस्ती, ना काहू से बैर ॥", "explanation": "Kabir stands in the market, wishing well for all. Neither friendship with anyone, nor enmity with any.", "translation": "Kabir stands in the market, wishing all well. No friends, no foes."},
        {"couplet_hindi": "कबीर मानुष जन्म दुर्लभ है, देह न बारम्बार । तरुवर से पत्ता झड़ गया, बहुरि न लागे डार ॥", "explanation": "Human life is rare; this body comes but once. Once a leaf falls from a tree, it never rejoins the branch.", "translation": "Life is rare, the body comes once. A fallen leaf never returns to the branch."},
        {"couplet_hindi": "निंदक नियरे राखिए, ऑंगन कुटी छवाय । बिन पानी, साबुन बिना, निर्मल करे सुभाय ॥", "explanation": "Keep your critics close. Without water or soap, they cleanse your character.", "translation": "Keep critics close. They clean your nature without soap or water."},
        {"couplet_hindi": "ज्यों नैनों में पुतली, त्यों मालिक घट माहिं । मूरख लोग न जानहीं, बाहर ढूँढन जाहिं ॥", "explanation": "As the pupil is in the eye, the Lord is within the body. Fools know it not and search outside.", "translation": "As the pupil is in the eye, God is within. Fools seek Him outside."},
        {"couplet_hindi": "प्रेम पियाला जो पिये, शीश दक्षिणा देय । लोभी शीश न दे सके, नाम प्रेम का लेय ॥", "explanation": "He who drinks the cup of love gives his head as a gift. The greedy cannot give their head but still speak of love.", "translation": "He who drinks love's cup gives his life. The greedy cannot, yet they speak of love."},
        {"couplet_hindi": "कबीर सोई पीर है, जो जाने पर पीर । जो पर पीर न जानई, सो काफिर बेपीर ॥", "explanation": "He is a true saint who knows others' pain. He who does not is heartless.", "translation": "A true saint feels others' pain. He who doesn't is without a soul."},
        {"couplet_hindi": "पोथी पढ़ि पढ़ि जग मुआ, पंडित भया न कोय । ढाई आखर प्रेम का, पढ़े सो पंडित होय ॥", "explanation": "Reading books the world died, no one became wise. He who reads 'Love' becomes wise.", "translation": "Books didn't make the world wise. He who reads 'Love' is truly wise."},
        {"couplet_hindi": "जब मैं था तब हरि नहीं, अब हरि हैं मैं नाहिं । प्रेम गली अति सांकरी, तामें दो न समाहिं ॥", "explanation": "When I was, God was not. Now God is, and I am not. Love's path is too narrow for two.", "translation": "When I was, God was not. Now God is, I am not. Love's path is too narrow for two."},
        {"couplet_hindi": "माटी कहे कुम्हार से, तु क्या रौंदे मोय । एक दिन ऐसा आएगा, मैं रौंदूगी तोय ॥", "explanation": "Clay says to the potter: Why do you trample me? One day I will trample you.", "translation": "Clay tells the potter: You trample me now, but one day I will trample you."},
        {"couplet_hindi": "जैसी प्रीति कुटुम्ब की, तैसी हरि सो होय । चला जाय वैकुण्ठ को, पल्ला न पकड़े कोय ॥", "explanation": "If your love for God was like your love for family, you would reach heaven easily.", "translation": "Love God like you love family, and heaven is yours."},
        {"couplet_hindi": "जाति न पूछो साधु की, पूछ लीजिये ज्ञान । मोल करो तलवार का, पड़ा रहन दो म्यान ॥", "explanation": "Don't ask a saint's caste, ask for his wisdom. Price the sword, leave the sheath.", "translation": "Ask wisdom, not caste. Value the sword, not the sheath."},
        {"couplet_hindi": "जैसा अन्न वैसा मन, जैसा पानी वैसी बानी ।", "explanation": "As is the food, so is the mind. As is the water, so is the speech.", "translation": "Your mind follows your food. Your speech follows your water."},
        {"couplet_hindi": "एक ही साधे सब सधे, सब साधे सब जाय । माली सींचे मूल को, फूले फले अघाय ॥", "explanation": "Master one and master all. Water the root to get fruit.", "translation": "Master one to gain all. Water the root to flourish."},
        {"couplet_hindi": "मन के हारे हार है, मन के जीते जीत । कह कबीर हरि पाइए, मन ही की परतीत ॥", "explanation": "Defeat is in the mind, victory is in the mind. God is found through faith.", "translation": "Victory and defeat are in the mind. God is found through faith."},
        {"couplet_hindi": "चिंता से चतुराई घटे, दुख से घटे शरीर । पाप से लक्ष्मी घटे, कह गए दास कबीर ॥", "explanation": "Worry reduces cleverness, sorrow weakens the body. Sin reduces wealth.", "translation": "Worry dulls the mind, sorrow hurts the body. Sin takes wealth away."},
        {"couplet_hindi": "बोली एक अनमोल है, जो कोई बोले जानि । हिये तराजू तौलि के, तब मुख बाहर आनि ॥", "explanation": "Words are priceless; weigh them in your heart.", "translation": "Weigh words in your heart before speaking."},
        {"couplet_hindi": "कहूँ तो कोउ न मानई, सहूँ तो जिया जाय ।", "explanation": "If I speak, no one believes. If I remain silent, my soul suffers.", "translation": "Speak and none believe. Silent, the soul suffers."},
        {"couplet_hindi": "गुरु बिन ज्ञान न उपजै, गुरु बिन मिलै न मोष ।", "explanation": "Without a Guru, there is no knowledge and no salvation.", "translation": "No Guru, no wisdom, no freedom."},
        {"couplet_hindi": "माया मरी न मन भरा, मर-मर गया शरीर ।", "explanation": "Illusion and mind didn't die; only the body died again and again.", "translation": "Illusion and mind live on; only the body dies repeatedly."},
        {"couplet_hindi": "कबीरा यहु घर प्रेम का, खाला का घर नाहिं । सीस उतारे हाथि करि, सो पैठे घर माहिं ॥", "explanation": "This is the house of love. Sacrifice ego to enter.", "translation": "This is the home of love. Sacrifice your ego to enter."},
        {"couplet_hindi": "बपु बपुरो बुड़न डरो, रहा किनारे बैठ । जिन खोजा तिन पाइया, गहरे पानी पैठ ॥", "explanation": "Timidity stays on the shore. Seekers find treasures in the deep.", "translation": "The timid stay on the bank. Seekers find treasures in the deep water."},
        {"couplet_hindi": "कबीर नौबत आपणी, दिन दस लेहु बजाय । यहु पुर पटन यहु गली, बहुरि न देखहु आय ॥", "explanation": "Live fully now. You won't return to these streets again.", "translation": "Live your life fully now. You won't see these streets again."},
        {"couplet_hindi": "पढ़ि पढ़ि के पत्थर भये, लिखि लिखि भये जु ईंट । कह कबीर वा प्रेम की, एको मिली न छींट ॥", "explanation": "Reading without love makes one like a stone.", "translation": "Endless reading without love makes one like a stone."},
        {"couplet_hindi": "कबीर तन पंछी भया, जहाँ मन तहाँ उडि जाय । जो जैसी संगति करै, सो तैसा फल खाय ॥", "explanation": "The body follows the mind. You reap the fruit of your company.", "translation": "The body follows the mind. You reap what you sow in company."},
        {"couplet_hindi": "माया दीपक नर पतंग, भ्रमि भ्रमि इवैं पड़ंत । कह कबीर गुरु ज्ञान थे, एक आध उबरंत ॥", "explanation": "Maya is the flame and man the moth. Guru's wisdom saves a few.", "translation": "Maya is the flame, man the moth. Guru's wisdom saves some."},
        {"couplet_hindi": "नहाये धोये क्या भया, जो मन का मैल न जाय । मीन सदा जल में रहै, धोये बास न जाय ॥", "explanation": "Bathing is useless if the mind remains dirty.", "translation": "Bathing is useless if the mind stays dirty."},
        {"couplet_hindi": "कबीर संगत साधु की, बेगि करीजै जाय । दुरमति दूरि गंवाइ सी, देशी सुमति बताय ॥", "explanation": "Seek a saint's company to remove bad thoughts and gain wisdom.", "translation": "Seek a saint's company to drive away evil thoughts."},
        {"couplet_hindi": "कबीरा यहु तन जात है, सकै तो लेहु बहोरि । जा घट प्रीति न राम की, सो घट गया अकारि ॥", "explanation": "This body is fading. Without devotion, life is wasted.", "translation": "This body is fading. Without devotion, life is in vain."},
        {"couplet_hindi": "कबीर सो धन संचिये, जो आगै को होय । सीस चढ़ाये पोटली, ले जात न देख्या कोय ॥", "explanation": "Save the wealth that lasts beyond death.", "translation": "Save the wealth that lasts beyond the grave."},
        {"couplet_hindi": "कामी क्रोधी लालची, इनसे भक्ति न होय । भक्ति करे कोइ सूरमा, जाति वरन कुल खोय ॥", "explanation": "The greedy and angry cannot truly devote themselves.", "translation": "The greedy and angry cannot truly devote."},
        {"couplet_hindi": "पाँच पहर धंधे गया, तीन पहर गया सोय । एको घड़ी न सिमिरया, तो जम की मार क्यूं न होय ॥", "explanation": "Work and sleep took your time. Forgetting God leads to death.", "translation": "Work and sleep took your time. Forgetting God leads to certain death."},
        {"couplet_hindi": "कबीर कलजुग आइया, करम कथै सब कोय । जेहि घट दया न संचरे, सो कलिहारी होय ॥", "explanation": "A heart without mercy is lost in this dark age.", "translation": "A heart without mercy is truly lost in this dark age."},
        {"couplet_hindi": "साधु सिष तो बहुत हैं, गुरु न मिलिया कोय । कबीर चेला क्या करे, गुरु बिन ज्ञान न होय ॥", "explanation": "Without a true Guru, there is no real wisdom.", "translation": "Without a true Guru, there is no real wisdom."},
        {"couplet_hindi": "प्रेम बिना जो जप तपै, सो सब निष्फल जाय । कबीर सोई भक्त है, जाके हिरदै प्रेम समाय ॥", "explanation": "Prayers and penance without love are fruitless.", "translation": "Prayers without love are in vain."},
                 {"couplet_hindi": "कबीर सोई सुरमा, जो मन सों खेलै जाय । पंच चपेटा मारि करि, मन को वश में लाय ॥", "explanation": "The true hero is one who conquers his own mind.", "translation": "The true hero conquers his own mind."},
        {"couplet_hindi": "जग में रहिबे को कछू, ठौर ठिकाना नाहिं । कबीर राम नाम बिन, जम के फंदे माहिं ॥", "explanation": "Nothing is permanent. Without devotion, death traps you.", "translation": "Nothing is permanent. Without devotion, you are trapped by death."},
        {"couplet_hindi": "कबीर कलि का रूप देखि, हंसा मन न धीर । जहाँ देखूं तहाँ पाप है, कैसे तिरै कबीर ॥", "explanation": "In this age, the soul finds no peace amidst sin.", "translation": "In this age, the soul finds no peace."},
        {"couplet_hindi": "सतगुरु हमसों रीझि करि, एक कह्या प्रसङ्ग । बरस्या बादल प्रेम का, भीजि गया सब अङ्ग ॥", "explanation": "The Guru's word rained love and soaked my soul.", "translation": "The Guru's word soaked my entire soul in love."},
        {"couplet_hindi": "कबीर दीवा तेल बिन, बाती बिनु जरि जाय । साँझ सकारे राम कहि, कदे न बुझि जाय ॥", "explanation": "Divine remembrance is a light that never goes out.", "translation": "Divine remembrance is a light that never dies."},
        {"couplet_hindi": "कस्तूरी कुंडली बसै, मृग ढूँढै बन माहिं । ज्यों घट-घट राम हैं, दुनिया देखै नाहिं ॥", "explanation": "God is within every heart, yet the world seeks Him outside.", "translation": "God is within, yet the world seeks Him outside."},
        {"couplet_hindi": "साँच बराबर ताप नहीं, झूठ बराबर पाप । जाके हिरदे साँच है, ताके हिरदे आप ॥", "explanation": "God resides where there is truth.", "translation": "God resides where truth lives."},
        {"couplet_hindi": "चलती चाकी देख के, दिया कबीरा रोय । दुइ पाटन के बीच में, साबुत बचा न कोय ॥", "explanation": "Nothing stays whole in the duality of the world.", "translation": "Nothing stays whole in this dual world."},
        {"couplet_hindi": "मंगन मरण समान है, मति कोउ मांगो भीख । मंगन से तो मरन भला, यह सतगुरु की सीख ॥", "explanation": "Begging is like death. It is better to die than to beg.", "translation": "Begging is like death. Better to die than beg."},
        {"couplet_hindi": "जब तू आया जगत में, लोग हंसे तू रोय । ऐसी करनी कर चलो, तुम हँसो जगत रोय ॥", "explanation": "Live so that at death, you laugh while others mourn.", "translation": "Live so that at death, you laugh while others mourn."},
        {"couplet_hindi": "सोना सज्जन साधु जन, टूटि जुरै सौ बार । दुर्जन कुम्भ कुम्हार के, एकै धका दरार ॥", "explanation": "Good people join even if broken. The wicked shatter forever.", "translation": "Good people join; the wicked shatter forever."},
        {"couplet_hindi": "उज्जल पहिरे कापड़ा, पान सुपारी खाय । एकै हरि के नाम बिन, बांधा जमपुर जाय ॥", "explanation": "Fine clothes and food mean nothing without devotion.", "translation": "Fine clothes are nothing without devotion."},
        {"couplet_hindi": "काया कांची कुंभ है, लिये फिरे था साथ । टपका लागा फूटि गया, कछू न आया हाथ ॥", "explanation": "The body is a fragile clay pot that shatters instantly.", "translation": "The body is a fragile clay pot."},
        {"couplet_hindi": "कबीरा तेरी झोंपड़ी, गलकटियन के पास । जो करेंगे सो भरेंगे, तुम क्यों भये उदास ॥", "explanation": "You reap what you sow; don't worry about others' actions.", "translation": "You reap what you sow; don't worry about others."},
        {"couplet_hindi": "साईं इतना दीजिये, जा मे कुटुम समाय । मैं भी भूखा न रहूँ, साधु ना भूखा जाय ॥", "explanation": "Lord, give me enough to sustain my family and guests.", "translation": "Lord, give me enough for family and guests."},
        {"couplet_hindi": "अति का भला न बोलना, अति की भली न चूप । अति का भला न बरसना, अति की भली न धूप ॥", "explanation": "Too much of anything is bad.", "translation": "Too much of anything is bad."},
        {"couplet_hindi": "कबीरा सूता क्या करे, जागी न जपे मुरार । एक दिन ऐसा सोवना, लंबे पाँव पसार ॥", "explanation": "Wake up and pray; eternal sleep is coming.", "translation": "Wake up and pray; eternal sleep comes."},
        {"couplet_hindi": "तिनका कबहुं ना निंदिये, जो पाँवन तर होय । कबहुं उड़ ऑंखिन पड़े, पीर घनेरी होय ॥", "explanation": "Never mock the small; it can cause great pain.", "translation": "Never mock the small; it causes great pain."},
        {"couplet_hindi": "हीरा वहाँ न खोलिये, जहाँ कुंजड़ी की हाट । सहजै गाँठि बाँधि के, लगिये अपनी बाट ॥", "explanation": "Show your wisdom only where it is valued.", "translation": "Show wisdom only where it is valued."},
        {"couplet_hindi": "मन के हारे हार है, मन के जीते जीत । कह कबीर हरि पाइए, मन ही की परतीत ॥", "explanation": "Victory and defeat are both in the mind.", "translation": "Victory and defeat are in the mind."},
        {"couplet_hindi": "चिंता से चतुराई घटे, दुख से घटे शरीर । पाप से लक्ष्मी घटे, कह गए दास कबीर ॥", "explanation": "Worry dulls the mind and weakens the body.", "translation": "Worry dulls the mind and body."},
        {"couplet_hindi": "कबीर कहता हूँ कहि जात हूँ, कहूँ जो ठोक बजाय । कुआँ पास है आपणे, तू क्यों प्यासा जाय ॥", "explanation": "The source of wisdom is near; don't remain thirsty.", "translation": "Wisdom is near; don't remain thirsty."},
        {"couplet_hindi": "तन को जोगी सब करें, मन को बिरला कोय । सहजै सब सिधि पाइए, जो मन जोगी होय ॥", "explanation": "Taming the mind brings true success.", "translation": "Taming the mind brings success."},
        {"couplet_hindi": "हाड़ जलै ज्यों लाकड़ी, केस जलै ज्यों घास । सब जग जलता देखि करि, भये कबीर उदास ॥", "explanation": "Everything burns; worldliness is temporary.", "translation": "Everything burns; worldliness is temporary."},
        {"couplet_hindi": "पाहन पूजे हरि मिले, तो मैं पूजूं पहार । ताते यह चाकी भली, पीस खाय संसार ॥", "explanation": "Service is better than empty rituals.", "translation": "Service is better than rituals."},
        {"couplet_hindi": "जाको राखे साइयां, मारि सके न कोय । बाल न बांका करि सके, जो जग बैरी होय ॥", "explanation": "Whom God protects, none can slay.", "translation": "Whom God protects, none can slay."},
        {"couplet_hindi": "कबीरा संगत साधु की, ज्यों गंधी की बास । जो कुछ गंधी दे नहीं, तो भी बास सुबास ॥", "explanation": "Good company leaves its scent even without words.", "translation": "Good company leaves its scent."},
        {"couplet_hindi": "माली आवत देख के, कलियन करे पुकार । फूले-फूले चुन लिये, काल्हि हमारी बार ॥", "explanation": "Time waits for no one; our turn is coming.", "translation": "Time waits for none; our turn comes."},
        {"couplet_hindi": "चाह मिटी चिंता मिटी, मनवा बेपरवाह । जिसको कछू न चाहिए, वो साहन के साह ॥", "explanation": "Ending desire makes you the king of kings.", "translation": "Ending desire makes you a king."},
        {"couplet_hindi": "जा घट प्रेम न संचरे, सो घट जान मसान । जैसे खाल लुहार की, सांस लेत बिनु प्रान ॥", "explanation": "A heart without love is a graveyard.", "translation": "A heart without love is a graveyard."},
        {"couplet_hindi": "साधु शब्द समुद्र है, जामें रत्न अपार । मूरख भेद न जानहीं, ढूँढत फिरे किनार ॥", "explanation": "Wise words are an ocean of gems.", "translation": "Wise words are an ocean of gems."},
        {"couplet_hindi": "चिंता ऐसी डाकिनी, काटि कलेजा खाय । बैद बिचारा क्या करे, कहाँ तक दवा लगाय ॥", "explanation": "Worry eats the heart; no medicine can reach it.", "translation": "Worry eats the heart; no medicine reaches it."},
        {"couplet_hindi": "कबीर लहरि समंद की, मोती बिखरे आइ । बगुला भेद न जानई, हंसा चुनि-चुनि खाइ ॥", "explanation": "Only the wise recognize true value.", "translation": "Only the wise recognize true value."},
        {"couplet_hindi": "कबीर दर्शन साधु के, बड़े भाग से होय । जो कछु किया सोई मिला, अब कछु और न कोय ॥", "explanation": "Fortune brings you to the wise.", "translation": "Fortune brings you to the wise."},
        {"couplet_hindi": "जैसा अन्न वैसा मन, जैसा पानी वैसी बानी ।", "explanation": "You are what you consume.", "translation": "You are what you consume."},
        {"couplet_hindi": "एक ही साधे सब सधे, सब साधे सब जाय । माली सींचे मूल को, फूले फले अघाय ॥", "explanation": "Master one essential thing to gain everything.", "translation": "Master one to gain all."}
    ]

    current_time = datetime.datetime.now(datetime.timezone.utc)
    hours_since_epoch = int(current_time.timestamp() // 3600)
    index = hours_since_epoch % len(couplets)
    doha = couplets[index]
    
    # 1. TEXT EXPORT (DOHA.TXT)
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

    # 2. RSS EXPORT (RSS.XML)
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
        
        # Correct timestamp for T-UI
        item_time = current_time.replace(minute=0, second=0, microsecond=0) - datetime.timedelta(hours=i)
        fe.pubDate(item_time)

    fg.rss_file('rss.xml')
    print("All 108 dohas updated successfully!")

if __name__ == '__main__':
    generate_kabir_feed()
        
