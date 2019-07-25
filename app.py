

  
#Python libraries that we need to import for our bot
import random
from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)
ACCESS_TOKEN = 'EAAFLBvAmOd0BAKVKAF3df5Sghin1OmB73pAMiQz0Hb8731vsFEg2Xz1xCIa7QECQ9r49gzAVTUXVjTXSNb11Sqft5X2TNf4VSvL60MTLD337ZBZBR95kxtZCzQcZA3kSL6W3lTB31g3mNrZAq8vej7YaeUNFGPOKIORcYo478A94XyxMLnMT2'
VERIFY_TOKEN = 'TESTINGTOKEN'
bot = Bot(ACCESS_TOKEN)




















#We will receive messages that Facebook sends our bot at this endpoint 
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook.""" 
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    #if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
       output = request.get_json()
       for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                #Facebook Messenger ID for user so we know where to send response back to
                recipient_id = message['sender']['id']
                if message['message'].get('text') == '9':
                    response_sent_text = get_message()
                    send_message(recipient_id, response_sent_text[0])
		    send_message(recipient_id, response_sent_text[1])
                #if user sends us a GIF, photo,video, or any other non-text item
                #if message['message'].get('attachments'):
                #    response_sent_nontext = get_message()
                #    send_message(recipient_id, response_sent_nontext)
    return "Message Processed"


def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


#chooses a random message to send to the user
def get_message():
    txtArray = [
'''( diclac 150 قرص بعد الفطار ) 
  ( omepak 20 قرص بعد الفطار ) 
  (indotopic cream دهان 3 مرات) 
  (epinosin b عضل يوم بعد يوم) 
  (sirdalud 2 mg قرص قبل النوم )''', 

''' (Mobic) 
  (Napizole)
   (Cymbatex 60)
    (Thiotacid 600)
     (Biovit)''', 

'''(Tecnovula)
(Nolvadex)
(Chromax )
(Solupred 5)
(Vibromycin)
(Villamoral vaginal was)''',

'''(Augmentin 1 gm tab)
 (After meals tab )
 (Dexilant 30 mg tab) 
 (Maalox) 
 (Gastromotil) 
 (Etaphylline)
  (Midodrine tab)
   (Librax tab)''',

'''(NEXIUM40)
 (MOTILLUM TAB )
  (DOGMATIL 200 FORT )
   (DANSET 8MG)'''
   ,
   '''
   ديرماميد
دايفوبيت
زيرتك
   '''
   ,
   '''
   ميكوفللين شراب
فينآدون شـرآب
ابيمـول اكسـترا اقراص
سبكتراسيفكيور٣٠٠
   '''
   ,
   '''
   ارثروفاست 
   باكلوفين 25
   ايريني باثيك 
   ازورا كريم 
   روكسيكام حقن  
   '''
   ,
   '''
   ارتيكوسيف
فولتارين
 emazad كريم
ميديكسافلام
Zalance ا
   '''
   ,
   '''
   روتون
ديبوفيت
كالسيتريكس
   '''
   ,
   '''
   فلوتاك 
نورجيسك
نيروفيت
   '''
   ,
   '''
   جوينتاتيك
دانتيريلاكس
ادلور
امبيزيم
ثرومبكس
   '''
   ,
   '''
   زيثروماكس
الفيولين بي
بانادول
   '''
   ,
   '''
   رومارين 
   روبيفامين 
   ديبروكورتين حقن 
   موبيك 15مجم اقراص 
   اسيلوك 300اقراص 
   موديورتيك اقراص 
   '''
   ,
   '''
   ولبيترين
ديبوفيت
اوكسيتريليبازين
سيبرالكس
تيبوفورتين
   '''
   ,
   '''
   ديباكين شراب
تيراتام شراب
فى دروب نقط
فروتال شراب
اعشاب سيكم مهدئة
   '''
   ,
   '''
   افيروزوليد
   فولتارين
   كيتولاك
   كليندام300
   الفينتيرن 
   '''
   ,
   '''
   Mondo مرة صباحا
Perderm مرة مساءا
Fernilar شريط 
قرص قبل النوم
   '''
   ,
   '''
   ليبراكس
سيستون
يوفامين
تامسولين
   '''
   ,
   '''
   تريتوفلامين
ستارلين كريم
سينوبار 
بريتير كريم
   '''
   ,
   '''
   امبزيم 
   والفاكيموتريبسين حقن
    وكيورام 1جم
   ريباريل جيل 
   '''
   ,
   '''
   Cefotax
Curam 
ketolac
Pedicort
Tantum
   '''
   ,
   '''
   ارستابكس بلاس
تورسيورتك أقراص
كوندومانيا١٠
اسبويبد
تريبتزول 25 أقراص
انكونت 
سيرفيتام
ميلجا
   '''
   ,
   '''
   Folic acid
Ezacard
Utrocare
Prontogest 400
   '''
   ,
   '''
   ميكوفليين ٢سم كل ٨ساعه بعد 
الحقنة ٢سم ع البودره وياخد 1سم يوميا
   '''
   ,
   '''
   دولفين امبول
ديكساميثازون امبول
   '''
   ,
   '''
   بلاتينور ٧٥
بيجاكسين كبسول
الداكتون ٢٥ مج
فلاميبرو كبسول
ازجوفانس كبسول
كومفولكس جيل
نيوروتون امبول
   '''
   ,
   '''
   كيلاجون 3مرات لمدة اسبوع
يوريفين3مرات لمدة 5ايام
بيبون بلس كل 24ساعة لمدة اسبوعين
انوفا قرص يذوب ع نصف كوب ماء
كل 12ساعة لمدة يومين
   '''
   ,
   '''
   كلارتين اقراص
كوديلار شراب
باكتبرو شراب
كيناكورت اقراص
   '''
   ,
   '''
   فيروجلوبين 
فاسكولار
بي كوم
برونتو جيست لبوس تركيز ٢٠٠
زاندروس
   '''
   ,
   '''
   توفرانيل ١٢٥
فيلوسيف 1جرام
ديكساميثازون
   '''
   ,
   '''
   راني امبول
كيتولاك امبول
المودوكساسين 500mg اقراص
   '''
   ,
   '''
   ابيدون شرب
ايبكوفلين شرب
ديكساميثازون حقن
يونيكتام حقن 
امبريكسول
   '''
   ,
   '''
   لازيلاكتون100
 Aspocid 75 
 nitromak 2.5
Ator
Exanide 20
   '''
   ,
   '''
   ديكلوفين امبول 
كومتركس
   ''',
   '''
   Unipridol fort  syp
Herbacaf  syp
Fernilar
   ''',
   '''
   زوراكسون 
ادويفلام
بارامول
زيثروكان
   ''',
   '''
   هيدروكين 200 اقراص
اندوميثازين لبوس
انتي كوكس 15مجم كبسول
ايه اي جي ايزموبرازول40مجم اقراص
موتيفال اقراص
   ''',
   '''
   كيورسيف نقط
نيزابكس شامبو
تيكساكورت على دكتاكورت خليط
وفي برمنجات 1/8000
فنستيل نقط
   ''',
   '''
   بنداكس
فلوكورال
نيورتون
باترافين
لاميفين
   ''',
   '''
   زوفيراكس
ميجاليز
   ''',
   '''
   كلوفرين
يوفامين
كيتوبريك
جينوكونازول
باندرمال
   ''',
   '''
   يور ايد
دونيفوكسات
نابروفين
   ''',
   '''
   Hiderm soap 
Delarex
   ''',
   '''
   
ليبانتيل ٣٠٠ 
موديريتك 
اندوجابلين
انتودين 
فولتارين لبوس 
كالسيمات
   ''',
   '''
   Vomistop
folicap 0.5
   ''',
   '''
   دافلون ٥٠٠ اقراص
سافييبليد 
ميجابيو ٧٥ اقراص 
رابيدوس ٥٠ اقراص
اكسترا كريم
   ''',
   '''
   
Duphaston tap
Aspocid 75 tap
Omega 3 cap
Folic acid
   ''',
   '''
   Bon care ,25
Calcitron 
Daflon
   ''',
   '''
   
Rosuvast 10
Zandros
Nebasco 5
Examide 10
No migraine
   ''',
   '''
   سيفوتاكس
نيوزيلكس حقن
موتليم
ستربتوكين
سبازموفين
   ''',
   '''
   itopride و
دايجينورم شراب
وpantoloc 20
   ''',
   '''
   سوبراكس 30مل
 سيتال نقط 
امبركسول نقط
   ''',
   '''
   سولوكورتيف
 امبيزيم 
اوجمنتين 
فلازكور
فلاموسيل ادول
   ''',
   '''
   زوراكسوان
فورتيكورتين
افيبكت
فاركوسولفين
   ''',
   '''
   
Mucotec 300 
Norhinose spray
   ''',
   '''
   
 سليب ايز
 كوجينتول
 كونفيجران٢٥
   ''',
   '''
   
يونيتون 4 كريم 
زنك بلس اقراص 
نيونيل كريم
   ''',
   '''
   
Ambezim g tab
Anox tab
   ''',
   '''
   
فروت كال
كلوسبامين فورت
ايتاترون 
ديبوفيت امبول
   ''',
   '''
   
دولفين ك حقن عضل يوميا
اريثركس 200 كبسول مرة بعد الفطار 
 يوريفين فوار  مرتين يوميا
   ''',
   '''
   
Flazacor30
Gincobiloba
Ezogast40
Betolvex amp
Escita
   ''',
   '''
   
كيفورك
توسيكان
كيتوبريك
كيتولاك
   ''',
   '''
   
Lantopep 60
Ganaton 50
Neurimax amp
Digenorm syp
   ''',
   '''
   
ناترى صابون
فيبراميسين
زيرتك
ديرماتوب
اليجون كريم للعين
   ''',
   '''
   
سيفاكسون
اسماكاست
فوراديل
ميفلونيذ
   ''',
   '''
   
جلوكوز
سكروفير
ابيدرون
بيكوزيم
تريكتين قرص
موتيليوم شراب
بيرفتكس امبول
   ''',
   '''
   
جلوكوز 5 فى الميه
ادولور 30
فيسيرالجين
دانسيت4
رايسك 40
بيمفاست1جم
جاست ريج امبول
   ''',
   '''
   
اوبتيرد
باتانول
   ''',
   '''
   
ديلاركس
تكساكورت
جنتازون
توب فلام 
بريد سول
هاي ديرم صابونة
   ''',
   '''
   لونجاسيف
ميكوفللين
فنتولين
   ''',
   '''
   
برازر كير كريم
كليروفات
   ''',
   '''
   
محلول جلوكوز ملحي 
فيسرالجين 
زانتاك
برمبران
ليوسيفورت
هيباتوكسيم ١ جم 
نو تريبل او ( ميمورال ) 
كل دول مع المحلول كل ١٢ ساعه 
ايميتريكس قرص 
سيرڤيتام ك
   ''',
   '''
   
تيكانيز اسبراي
فيناكسان
بارامول أقراص
كيتولاك امبول
فاموتين اقراص
   ''',
   '''
   
رواتينكس 
ك١ ايبكس اقراص
ديكسلانت30ملي 
جاناتون50ملي
   ''',
   '''
   
ريلاكس كريم
كلوبكس اقراص
بريستفلام أقراص
ليفابيون امبول 
اوستيوكير اقراص
   ''',
   '''
   
ليوميتاسين أمبول
نورفلكس
فلكسيلاكس
سيلبريج
 اوميز 20
   ''',
   '''
   
دلتازون
رويال فيت جى
   ''',
   '''
   
دلتا فيت ب ١٢ اقراص استحلاب تحت اللسان
فيا كال شيكولاته اقراص
   ''',
   '''
   
سيتال نقط 
انتينال شرب 
فلاجيل 
جاست ريج
   ''',
   '''
   
محلول ملح 
فيسرالجين امبول
سيفازون اجرام فيال
ابيدرون امبول
رآني امبول
بيرمبيران امبول 
ديبوفيت لبوس 
رواكول قراص
   ''',
   '''
   
اندرال40
كونتراليبسي
سيتالو
ميوفين
ناريدركس2.5
   ''',
   '''
   
اكني مايسن
بيوتاكسيمارك
يوني فنجاي أو كانديوازول
فاشكو
فروموز اي كريم
   ''',
   '''
   
فاركوتيليام
فيدروب
فنستيل
أكوا بلس
دينتونكس
   ''',
   '''
   
Stimulan amp
Ginkobiloba caps
Jueprin 81mg
Ator 10mg
   ''',
   '''
   
درموفيرين أقراص منع الحمل
امريزول ان لبوس
اوكافا تشطيف
   ''',
   '''
   
Duphaston tab  
folicap 0.5 cap 
neurobion amp 
ezacard ca
   ''',
   '''
   
موون فيس 
كوزموديرم
فوتكس كريم
سيليكي لايف
اندوفيل
اكت زينك
   ''',
   '''
   
كيروفيت كبسول 
دلتافيت
هيما كبسول
فوليك اسيد اقراص 
كوناديون اقراص
   ''',
   '''
   
هيدروكينون 
اسكربيك
بانثينول
موميسون 
اكرتين 
انفنتي صابونه
كابرون500
   ''',
   '''
   
سولبيريد20
ازاثيوبرين50
بنتاسا
جاسترلوك40
كلوفيرين اس ار
   ''',
   '''
   
ترايتون٢٠٠
سيبرديازول
فيرم1
   ''',
   '''
   
ميديفيت شراب
نيكسبرو اكياس
   ''',
   '''
   
ارسوجلوب كبسول
ارتكيوسيف كبسول
موبي ايز  جيل
انوكسيكام 20 مجم
   ''',
   '''
   
مكسيماش40
سبازمودايجستين
رانى  
فيسرالجين امبول
موتيليوم شراب
   ''',
   '''
   
ديبروفوس امبول 
ليفست ق
كيناكورت
ديرموفيت كريم
جلسرين صابونه
كبيرون
   ''',
   '''
   
كوردارون
اوميز
   ''',
   '''
   
يونيكتام 1.5 
دولفين 75 
سيبترين اقراص
 الليرجكس اقراص
 بنادول العادي
   ''',
   '''
   
اسيتيل ستاتين فوار
زيتوكسونال
مالوكس بلس
بروبريك
فاركولين
ميفلونيد
فوراديل
   ''',
   '''
   
Silymarin plus Sach 
Conadione 
Lactulose 
rentol حقنه شرجيه 
Calmag
   ''',
   '''
   
فيروترون
بيوفيت امبول
   ''',
   '''
   
الفاكيموتريبسن
ميلوفلام
كالسيدول
   ''',
   '''
   
ليفابيون
فولتارين
مالتي ريلاكس
رانيتاك
   ''',
   '''
   
R M soap.  
butaximark cream
   ''',
   '''
   
زيرتك
موكسفلوكساسين
باى الكوفان
   ''',
   '''
   
naphcon A
hyfresh
brimonacond
corner gel
   ''',
   '''
   
Mobitil supp
Esomuim 40
Vidrop drops
Uri aed eff
   ''',
   '''
   
Haemostop amp
Kapron
Dioced c
Bruffen400
   ''',
   '''
   
Bioglimet plus
Pregdin apex
Power b complex
   ''',
   '''
   
Levoflixacin
Syston 
Rowatinex.
Epimag. 
Flector
curepro
   ''',
   '''
   
فلاجيل
بيدياشور
هاىبيوتك ٤٦٠
   ''',
   '''
   
Vapozole
Quinabiotic
All vent
   ''',
   '''
   
كلاريثرو 
فلاجيل 
اموكسيل ٥٠٠
 استوهالت
   ''',
   '''
   
اندرال 40
كاربيمازول 5
زوراكال40 
توبرامات 25
جاستروموتيل
   ''',
   '''
   
موتيفال
كاربابكس١٠٠
   ''',
   '''
   
كيتوفان امبول
كتافلاي
هايبيوتيك ٦٠٠
بروفين
   ''',
   '''
   
بسكوبان 
فولتارين 
رينجر محلول
جاست ريج 
سبازموبينافير
   ''',
   '''
   
كيمبوبيم
فينتالير فورت
فياساليمول
بيتاليرج
ازماكاست
   ''',
   '''
   
كونتراكتيبيكس 
ديرموفيت 
ماربالين
كولشيسين
   ''',
   '''
   
Incont la 4mg
Urginafact
Arcalion fort
Omega3
Uripan
   ''',
   '''
   
يوناسين750
دولفن25
اوترفين
ستريم
فينادون
   ''',
   '''
   
كانيولا20
محلول ملح
فيروساك
سوبرسيز
   ''',
   '''
   
برونكوتيك
جى سى مول
كلافيموكس
   ''',
   '''
   
فلومكس 0.5 امبول
بيبي ريليف 12.5 لبوس
   ''',
   '''
   
يورينكس
سبازموسين
   ''',
   '''
   
سيردالود
ديفيدو
ميلوكسيكام
فولتارين
بروفينيد لبوس
   ''',
   '''
   
Anthzon 
Doxycost
Dalacin-c
Meglase
   ''',
   '''
   
زنتاك امبول
كورتيبلكس امبول 
فيسرالجين امبول
   ''',
   '''
   
سليمارين بلس 
دايجينورم 
ابيكوزيم
جيمافيتا
   ''',
   '''
   
سبارا 200
سيتروسيد فوار
سوليد لبوس
   ''',
   '''
   
سيربروليسن
تيبونينا
كيمريكا75
تريبتزول10
اميوران
سولوبريد20
انوفا
   ''',
   '''
   
فيناكسان٥٠٠
ايه جى ايزوميبرازول
موتيليم
   ''',
   '''
   
كولشيسن
اميوران
تينتا فير بخاخ
فلوتيفورم ١٢٥ 
بيتاليرج اقراص 
نيكسيكيور
   ''',
   '''
   
Urivin sach.
Etodin300.
Adwimove gel.
xanthubex80
   ''',
   '''
   
Uricorinal eff
Celebrex 200 tab
Diacerin caps
Goutyless tab
   ''',
   '''
   
هيماتكس
لاكتوكال
   ''',
   '''
   
فوراديل
ميفلونايد
سوليوبريد
كولشيسين
استيل سيستاتين
لازيلاكتون
   ''',
   '''
   
رانجير
بروتولانز
   ''',
   '''
   
ايزميوم
ديكلوتزين فوار
انتى كوكس
دروفين
ماجنابيوتك٦٢٥
ميدريست كريم
   ''',
   '''
   
جلسرين صابونة
درموفيت 
افيل امبول
فاستل ١٨٠ اقراص
solo  lotion و
وkeflex 500 tab
   ''',
   '''
   Valigen sach
Aceclecopa
Depovit
   ''',
   '''
   
سولوكورتيف
امبيزيم
اوجمنتين
فلاموسيل
فلازكور
ادول
   ''',
   '''
   
Ciprodiazol 500 
Ambezim 
Fusi cream
   ''',
   '''
   
زيتوكسانال 
يورينكس
   ''',
   '''
   
Amaryl 4 mg 
Galvus met 50/1000
Milga
Erastapex plus 40/12.5
   ''',
   '''
   
امريزول
زيثروسين
ويست بريث
فوراديل
مفلونيد
دكتارين
   ''',
   '''
   
جاروبرايد
ايزوميلودان40
جاستروبيوتيك200
   ''',
   '''
   nexium
mucosta
motillium
eucarbon
flagyl
nystatin
   ''',
   '''
   
تيبوفورتين ٨٠
ديسبركام ٢٠
   ''',
   '''
   
نيكسكيور ٤٠ 
ليبراكس 
دايجنورم شراب 
موتيفال اقراص شريط 
بى كوم
   ''',
   '''
   Diclac
Rubivamin
Diprocortin 
Naproxen
Ranitac
   ''',
   '''
   
فلوتاك كابسول
كولمدتين اقراص
فورتكورتين امبول
نيوروبين امبول
   ''',
   '''
   نورفلكس
Actozoneا
دولفين ك
كيردالود
ديكلاك
   ''',
   '''
   
بيتافوس امبول
استيل سيستايين 600 أكياس 
ادول أقراص
ميجاموكس 
فينتوكف شرب
   ''',
   '''
   دان دوف 
   فاست كير 
   سترونج فيل
   فيتامونت
   ''',
   '''
   
فولتارين امبول
يوفامين ريتارد
يورينكس اقراص
ابيكوتيل حقن
انداسين
فسرالجين
بوسكوبان كومب
كاتافاست
   ''',
   '''
   
Gone shampoo 
dodge spray 
Pro out hair tonic
Hair globe spray
irospect cap
   ''',
   '''
   
تابسين 100
زينا تشطيف
اميرزول ان لبوس
 برستافلام
   ''',
   '''
   
Megamox457 
zovrax400 
telefast 
otrovin child
acyclovir5% 
catafly
   ''',
   '''
   
فاركوتليم
درينك
كالم كينج
   ''',
   '''
   
Ciprofar 500
Renal s sachet
Zyrtec tap
   ''',
   '''
   
فسرالجين حقن
كولونا اقراص 
لبراكس كابسول
   ''',
   '''
   
ايمرست امبول 
دياسمكت
كتافلاى شراب 
اورس
انتى ديازوكس شراب 
سييفزون
   ''',
   '''
   
رانسيف 
يوريبان تقريبا
 يوروسولفين
 رواتنكس
   ''',
   '''
   
Oxitropil
Ornidaz
Flumox 500
Delarex
   ''',
   '''
   
Natralex
betacor 80
isopten 240
   ''',
   '''
   
نيوكلاف 
فينادون 
اوتريفين اطفال
   ''',
   '''
   
Unictam 375 vial.
Cefaclor 125 syp.
Amrizol syp.
Nitazode syp. 
Ors sach.
Dolphin 12.5 supp
   ''',
   '''
   
لانوكسين
كلاتكس
جوسبرين
اتور٤٠
   ''',
   '''
   
Flavicef syrup
Cetal  d 
Oxymet d
Calm cough
Coughseed
   ''',
   '''
   
ليوميتاسين
هيكساجابالين
ارتيكوسيف
دولاجين
   ''',
   '''
   محلولة غلط معلش
ليوميتاسين
هيكساجابالين
ارتيكوسيف
   ''',
   '''
   
Duricef 500
Methergin
Malva
   ''',
   '''
   
ميراميريكس
التراسولف
كيبرون
دايجستين
بيكوزيم
   ''',
   '''
   
Primrose plus 1000
Alphentern 
Voltaren 100sr
Voltaren gel
   ''',
   '''
   
Minirin melt 120
Imipramine tab
   ''',
   '''
   
مالتي ريلاكس 5
مايوفين
فلكتور
نايت كالم
رواتنكس 
كيتولاك اقراص
نيوروتون امبول
   ''',
   '''
   
فينوتك اقراص
كابرون
فيرترون
سبازمو فين
   ''',
   '''
   
Downoprazol 40
One alpha 1 m
Cal preg tab
Biovit amp
Optaminus tab
   ''',
   '''
   
ليبوسنس
تريفلوكان
فيمينا
نافيبروكسين
   ''',
   '''
   
spiraquet
sulfax
hermapro
vilaphorea
   ''',
   '''
   
Zanders
Aspren81
Hems caps 
Marcal
   ''',
   '''
   
Tobracoid E.O
Lacritears
   ''',
   '''
   
prontogest 400
cobal f 
octatron
   ''',
   '''
   
ترايكتين
فيروترون
برومكس
   ''',
   '''
   
نيرسو شامبو
مينوكسولوك
بانتوجار
   ''',
   '''
   
فلاجيلات فورت
ديجينورم
نازاكورت
الزنتال
   ''',
   '''
   
Clovatil tab
Novistoric 10
   ''',
   '''
   
كابرون
ميثرجين
امريزول
ديسفلاتيل
كولوسبازمين فورت
   ''',
   '''
   
Spirazole
Betadine m.w
cevamole eff
   ''',
   '''
   
سيدوجين
جيونترا
فيردول
   ''',
   '''
   
تكساكورت
ايفاستين
بريد سول
   ''',
   '''
   
تراياكتين
فيرموزول
برونتو
تريترون
   ''',
   '''
   
فلاجيل250
فلوموكس 250
بروفين200
   ''',
   '''
   
Motilium syrp
noerosive syrp
   ''',
   '''
   
زيثروماكس كبسول
ماء اكسجين
   ''',
   '''
   
ستيرونات اقراص
ايمتركس اقراص
رواتينكس كبسول
   ''',
   '''
   
اندرال 10
ليبراكس
ايزومبكس
نيوريماكس
   ''',
   '''
   
ابيدرون ١/٢ سم
فورتام
ادولور
فيسيرالجين
ابيكوتيل فيال جلوكوز ٥٪
   ''',
   '''
   
Medixaflam amp امبول عضل يوميا لمدة 5 ايام
Multirelax ق مرتين
Rx gel 3 مرات
   ''',
   '''
   
vanzapro 
ventolin
predsol 
lyse drop
   ''',
   '''
   
Long acting penicillin
Plaquenil
Biovit
Arthfree
Voltatrn supp
   ''',
   '''
   
كيونوستارماكس
فيسيرالجين
بروفينيد
يوروسولفين
   ''',
   '''
   
فيبراميسين
ديكسا ترول
نقط للاذن 4مرات
   ''',
   '''
   
ديلزوسين
اكتوفنت
ابيدرون
   ''',
   '''
   
Colchicine
Dantirelax
Srilane cream
   ''',
   '''
   
انتي كوكس 
ادولور 30
بريجافالكس 50
سالفاكس
   ''',
   '''
   
بروتوجيست ٢٠٠
يتروكير
دكتاكورت
فوليكاب ٢.٥
   ''',
   '''
   
floxamo 
pandaol
depovet
neobronchofen
   ''',
   '''
   
الليرتام
سبرو ٥٠٠
بيبتون شراب
بنادول
   ''',
   '''
   
اوكساليبتال
sycosetam
ميلجا 
هوستاكورتين
لازكس
بوتاسيوم
اركاليون
   ''',
   '''
   
نيوروتون
ثيوتاسيد
امبيزيم
تريتوالس
دوروفين
كيتولاك
موبيتيل
   ''',
   '''
   
elivit
cobal f
omegafit 1000
once time daily
neuroton
osteocare
   ''',
   '''
   
انفلاكام
لونجاسيف
سيدالاك
بروكاسوفت
منثولاكس
   ''',
   '''
   
سيمبكورت320 
فلوروفلوكس 400
ترايمدفلو
برونكوبرو
   ''',
   '''
   
Genophil 
Sullfax cmf 
Recoxibright 90
   ''',
   '''
   
ابكوتيل امبول 
سبازموفين امبول 
سيميثكون ق 
رانتيدين ١٥٠ ق
ليبراكس ق
   ''',
   '''
   
محلول ملح
ديرمازين كريم
فيوسيدرم كريم
ميجاموكس شراب
ابيدون شراب
   ''',
   '''
   
جينيرا
امريفلوكان
يورينكس
جينودكتارين
كلنسو
   ''',
   '''
   
سيفوران
ميجاموكس
أورازون
بيبي ريليف 25
   ''',
   '''
   
فاستيل
ليفست
ليفوديل
   ''',
   '''
   
Ambezim
Mobitl amp
Conventin 100
Relax
   ''',
   '''
   
Olfen
Avil
Dexamethazone
Spasmo digestin
Theragran
   ''',
   '''
   
فيوتيك نقط
ميجاموكس
ميوكتك
رينكس نقط
ديكسافين شراب
   ''',
   '''
   
جاستروموتيل
ديكسيلانت
انتودين
اميبرايد
   ''',
   '''
   
Spirex 3
Ivypront
Cal heparin
   ''',
   '''
   
انريتش شراب
اوستوكير  شراب
فيدروب  نقط
   ''',
   '''
   
زيسورسين
اوسبكت
ميوكوتيك
مينوفيللين
   ''',
   '''
   
جينوفيل 
كولشيسين
وNeuropatex 
وVronogabic 75
   ''',
   '''
   
Orchinohist
Co-avazir
Tobrin
   ''',
   '''
   
كلوميد
روز فيم اقراص
مارفيجلون
سيكلوبرجنوفا
   ''',
   '''
   
ديسبركام امبول 
موفيزي ١٠ مجم ق
ارثروفاست ق
   ''',
   '''
   
جينورين 
سوفيناسين 5ملي
   ''',
   '''
   
كيناكومب
جولد
   ''',
   '''
   
Controloc 40 
Gastro motil
   ''',
   '''
   
اولرنتاز
بيكولاكس
بيترو
اوروفار اقراص استحلاب
   ''',
   '''
   
كلوبكس 
اسبوسيد
اتور10
تارج160
ممكسا 10
كارنتول
   ''',
   '''
   
فلاجيل محلول.
ليبراكس. 
ستوب سبازم.
بانتولوك
   ''',
   '''
   
سيدبروكت
سبازموديجستين
لاكتيلوز
تامسولين
   ''',
   '''
   
سينومارين
فلوموكس٢٥٠شراب
دولفين ٥٠
   ''',
   '''
   
فلاجنيل كريم
ديفلوكان 150
فاستولات
   ''',
   '''
   
محلول ملح  
فورتاكورتين
 دانست8
 فولتارين
 سيفوترياكسون 
فلاجيل 500 
بوتافين 50 
ستربتوكين
   ''',
   '''
   
هيدروكينون 
اسكوربيك
بانثينول 
موميزون 
اكرتين
انفنتى spf 50 
كابرون اقراص
   ''',
   '''
   
دولفين k
فينادون شراب 
كيناكومب كريم
   ''',
   '''
   
درموفيت
امريزول ان لبوس
 اوكافا تشطيف
   ''',
   '''
   
دوفاديلان
سيدولوت ديبوت
اندوميثازين
زيثروكان
   ''',
   '''
   
انتودين امبول
بانتولوك ٤٠
كولوڤيرين 
كولوسبازمين
 فيتايامي
   ''',
   '''
   
هيباتيكم شراب
ايبكوزيم شراب
Falconasea شراب
   ''',
   '''
   
Bendax 
Egy gastrase
Cefathird
   ''',
'''

Ciprofar 500 tab
Alka masr sach
Flexonaze spray 
Megalase tab 
Solvymist syrp
'''


]

    sample_responses = ['https://druggo-app.github.io/rosheta/imgs/{}.jpg'.format(i) for i in range(1,251)]
    # return selected item to the user
    i = random.choice(range(1,255))
    img = sample_responses[i]
    txt = txtArray[i]
    return (img, txt)

#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

if __name__ == "__main__":
    app.run()


