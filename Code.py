from colorama import Fore,Style,init
from time import sleep
from random import choice

init(autoreset=True)

word_3 = ['aba','abs','ace','act','add','ado','aft','age','ago','aha','aid','aim','air','ala','ale','all','alt','amp','ana','and','ant','any','ape','app','apt','arc','are','ark','arm','art','ash','ask','asp','ass','ate','ave','awe','axe','aye','BAA','bad','bag','ban','bar','bat','bay','bed','bee','beg','bel','ben','bet','bid','big','bin','bio','bis','bit','biz','bob','bog','boo','bow','box','boy','bra','bud','Bug','bum','bun','bus','but','buy','bye','cab','cad','cam','can','cap','car','cat','chi','cob','cod','col','con','coo','cop','cor','cos','cot','cow','cox','coy','cry','cub','cue','cup','cut','dab','dad','dal','dam','day','Dee','def','del','den','dew','did','die','dig','dim','din','dip','dis','doc','doe','dog','don','dot','dry','dub','due','dug','dun','duo','dye','ear','eat','ebb','ecu','eft','egg','ego','elf','elm','emu','end','era','eta','eve','eye','fab','fad','fan','far','fat','fax','fay','fed','fee','fen','few','fig','fin','fir','fit','fix','flu','fly','foe','fog','for','fox','fry','fun','fur','gag','gal','gap','gas','gay','gee','gel','gem','get','gig','gin','god','got','gum','gun','gut','guy','gym','had','ham','has','hat','hay','hem','hen','her','hey','hid','him','hip','his','hit','hog','hon','hop','hot','how','hub','hue','hug','huh','hum','hut','ice','icy','igg','ill','imp','ink','inn','ion','its','ivy','jam','jar','jaw','jay','jet','job','joe','jog','joy','jug','jun','kay','ken','key','kid','kin','kit','lab','lac','lad','lag','lam','lap','law','lax','lay','lea','led','Lee','leg','let','lib','lid','lie','lip','lit','log','lot','low','mac','mad','mag','man','map','mar','mas','mat','max','may','med','meg','men','Met','mid','mil','mix','mob','mod','mol','mom','mon','mop','mot','mud','mug','mum','nab','nah','nan','nap','nay','neb','net','new','nil','nip','nod','nor','nos','not','now','nun','nut','oak','odd','off','oft','oil','old','ole','one','ooh','opt','orb','ore','our','out','owe','owl','own','pac','pad','pal','pam','pan','pap','par','pas','pat','paw','pay','pea','peg','pen','pep','per','pet','pew','phi','pic','pie','pig','pin','pip','pit','ply','pod','pol','pop','pot','pro','psi','pub','pup','put','rad','rag','raj','ram','ran','rap','rat','raw','ray','red','ref','reg','rem','rep','rev','rib','rid','rig','rim','rip','rob','rod','roe','rot','row','rub','rue','rug','rum','run','rye','sab','sac','sad','sae','sag','sal','sap','sat','saw','say','sea','sec','see','sen','set','sew','sex','she','shy','sic','sim','sin','sip','sir','sis','sit','six','ski','sky','sly','sod','sol','son','sow','soy','spa','spy','sub','sue','sum','sun','sup','tab','tad','tag','tam','tan','tap','tar','tat','tax','tea','ted','tee','ten','the','thy','tie','tin','tip','tod','toe','tom','ton','too','top','tor','tot','tow','toy','try','tub','tug','two','use','van','vat','vet','via','vie','vow','wan','war','was','wax','way','web','wed','wee','wet','who','why','wig','win','wis','wit','won','woo','wow','wry','wye','yen','yep','yes','yet','you','zip','zoo']
word_4 = ['able','acid','aged','also','area','army','away','baby','back','ball','band','bank','base','bath','bear','beat','been','beer','bell','belt','best','bill','bird','blow','blue','boat','body','bomb','bond','bone','book','boom','born','boss','both','bowl','bulk','burn','bush','busy','call','calm','came','camp','card','care','case','cash','cast','cell','chat','chip','city','club','coal','coat','code','cold','come','cook','cool','cope','copy','CORE','cost','crew','crop','dark','data','date','dawn','days','dead','deal','dean','dear','debt','deep','deny','desk','dial','dick','diet','disc','disk','does','done','door','dose','down','draw','drew','drop','drug','dual','duke','dust','duty','each','earn','ease','east','easy','edge','else','even','ever','evil','exit','face','fact','fail','fair','fall','farm','fast','fate','fear','feed','feel','feet','fell','felt','file','fill','film','find','fine','fire','firm','fish','five','flat','flow','food','foot','ford','form','fort','four','free','from','fuel','full','fund','gain','game','gate','gave','gear','gene','gift','girl','give','glad','goal','goes','gold','Golf','gone','good','gray','grew','grey','grow','gulf','hair','half','hall','hand','hang','hard','harm','hate','have','head','hear','heat','held','hell','help','here','hero','high','hill','hire','hold','hole','holy','home','hope','host','hour','huge','hung','hunt','hurt','idea','inch','into','iron','item','jack','jane','jean','john','join','jump','jury','just','keen','keep','kent','kept','kick','kill','kind','king','knee','knew','know','lack','lady','laid','lake','land','lane','last','late','lead','left','less','life','lift','like','line','link','list','live','load','loan','lock','logo','long','look','lord','lose','loss','lost','love','luck','made','mail','main','make','male','many','Mark','mass','matt','meal','mean','meat','meet','menu','mere','mike','mile','milk','mill','mind','mine','miss','mode','mood','moon','more','most','move','much','must','name','navy','near','neck','need','news','next','nice','nick','nine','none','nose','note','okay','once','only','onto','open','oral','over','pace','pack','page','paid','pain','pair','palm','park','part','pass','past','path','peak','pick','pink','pipe','plan','play','plot','plug','plus','poll','pool','poor','port','post','pull','pure','push','race','rail','rain','rank','rare','rate','read','real','rear','rely','rent','rest','rice','rich','ride','ring','rise','risk','road','rock','role','roll','roof','room','root','rose','rule','rush','ruth','safe','said','sake','sale','salt','same','sand','save','seat','seed','seek','seem','seen','self','sell','send','sent','sept','ship','shop','shot','show','shut','sick','side','sign','site','size','skin','slip','slow','snow','soft','soil','sold','sole','some','song','soon','sort','soul','spot','star','stay','step','stop','such','suit','sure','take','tale','talk','tall','tank','tape','task','team','tech','tell','tend','term','test','text','than','that','them','then','they','thin','this','thus','till','time','tiny','told','toll','tone','tony','took','tool','tour','town','tree','trip','true','tune','turn','twin','type','unit','upon','used','user','vary','vast','very','vice','view','vote','wage','wait','wake','walk','wall','want','ward','warm','wash','wave','ways','weak','wear','week','well','went','were','west','what','when','whom','wide','wife','wild','will','wind','wine','wing','wire','wise','wish','with','wood','word','wore','work','yard','yeah','year','your','zero','zone']
word_5 = ['ABOUT', 'ABOVE', 'ABUSE', 'ACTOR', 'ACUTE', 'ADMIT', 'ADOPT', 'ADULT', 'AFTER', 'AGAIN', 'AGENT', 'AGREE', 'AHEAD', 'ALARM', 'ALBUM', 'ALERT', 'ALIKE', 'ALIVE', 'ALLOW', 'ALONE', 'ALONG', 'ALTER', 'AMONG', 'ANGER', 'ANGLE', 'ANGRY', 'APART', 'APPLE', 'APPLY', 'ARENA', 'ARGUE', 'ARISE', 'ARRAY', 'ASIDE', 'ASSET', 'AUDIO', 'AUDIT', 'AVOID', 'AWARD', 'AWARE', 'BADLY', 'BAKER', 'BASES', 'BASIC', 'BASIS', 'BEACH', 'BEGAN', 'BEGIN', 'BEGUN', 'BEING', 'BELOW', 'BENCH', 'BILLY', 'BIRTH', 'BLACK', 'BLAME', 'BLIND', 'BLOCK', 'BLOOD', 'BOARD', 'BOOST', 'BOOTH', 'BOUND', 'BRAIN', 'BRAND', 'BREAD', 'BREAK', 'BREED', 'BRIEF', 'BRING', 'BROAD', 'BROKE', 'BROWN', 'BUILD', 'BUILT', 'BUYER', 'CABLE', 'CALIF', 'CARRY', 'CATCH', 'CAUSE', 'CHAIN', 'CHAIR', 'CHART', 'CHASE', 'CHEAP', 'CHECK', 'CHEST', 'CHIEF', 'CHILD', 'CHINA', 'CHOSE', 'CIVIL', 'CLAIM', 'CLASS', 'CLEAN', 'CLEAR', 'CLICK', 'CLOCK', 'CLOSE', 'COACH', 'COAST', 'COULD', 'COUNT', 'COURT', 'COVER', 'CRAFT', 'CRASH', 'CREAM', 'CRIME', 'CROSS', 'CROWD', 'CROWN', 'CURVE', 'CYCLE', 'DAILY', 'DANCE', 'DATED', 'DEALT', 'DEATH', 'DEBUT', 'DELAY', 'DEPTH', 'DOING', 'DOUBT', 'DOZEN', 'DRAFT', 'DRAMA', 'DRAWN', 'DREAM', 'DRESS', 'DRILL', 'DRINK', 'DRIVE', 'DROVE', 'DYING', 'EAGER', 'EARLY', 'EARTH', 'EIGHT', 'ELITE', 'EMPTY', 'ENEMY', 'ENJOY', 'ENTER', 'ENTRY', 'EQUAL', 'ERROR', 'EVENT', 'EVERY', 'EXACT', 'EXIST', 'EXTRA', 'FAITH', 'FALSE', 'FAULT', 'FIBER', 'FIELD', 'FIFTH', 'FIFTY', 'FIGHT', 'FINAL', 'FIRST', 'FIXED', 'FLASH', 'FLEET', 'FLOOR', 'FLUID', 'FOCUS', 'FORCE', 'FORTH', 'FORTY', 'FORUM', 'FOUND', 'FRAME', 'FRANK', 'FRAUD', 'FRESH', 'FRONT', 'FRUIT', 'FULLY', 'FUNNY', 'GIANT', 'GIVEN', 'GLASS', 'GLOBE', 'GOING', 'GRACE', 'GRADE', 'GRAND', 'GRANT', 'GRASS', 'GREAT', 'GREEN', 'GROSS', 'GROUP', 'GROWN', 'GUARD', 'GUESS', 'GUEST', 'GUIDE', 'HAPPY', 'HARRY', 'HEART', 'HEAVY', 'HENCE', 'HENRY', 'HORSE', 'HOTEL', 'HOUSE', 'HUMAN', 'IDEAL', 'IMAGE', 'INDEX', 'INNER', 'INPUT', 'ISSUE', 'JAPAN', 'JIMMY', 'JOINT', 'JONES', 'JUDGE', 'KNOWN', 'LABEL', 'LARGE', 'LASER', 'LATER', 'LAUGH', 'LAYER', 'LEARN', 'LEASE', 'LEAST', 'LEAVE', 'LEGAL', 'LEVEL', 'LEWIS', 'LIGHT', 'LIMIT', 'LINKS', 'LIVES', 'LOCAL', 'LOGIC', 'LOOSE', 'LOWER', 'LUCKY', 'LUNCH', 'LYING', 'MAGIC', 'MAJOR', 'MAKER', 'MARCH', 'MARIA', 'MATCH', 'MAYBE', 'MAYOR', 'MEANT', 'MEDIA', 'METAL', 'MIGHT', 'MINOR', 'MINUS', 'MIXED', 'MODEL', 'MONEY', 'MONTH', 'MORAL', 'MOTOR', 'MOUNT', 'MOUSE', 'MOUTH', 'MOVIE', 'MUSIC', 'NEEDS', 'NEVER', 'NEWLY', 'NIGHT', 'NOISE', 'NORTH', 'NOTED', 'NOVEL', 'NURSE', 'OCCUR', 'OCEAN', 'OFFER', 'OFTEN', 'ORDER', 'OTHER', 'OUGHT', 'PAINT', 'PANEL', 'PAPER', 'PARTY', 'PEACE', 'PETER', 'PHASE', 'PHONE', 'PHOTO', 'PIECE', 'PILOT', 'PITCH', 'PLACE', 'PLAIN', 'PLANE', 'PLANT', 'PLATE', 'POINT', 'POUND', 'POWER', 'PRESS', 'PRICE', 'PRIDE', 'PRIME', 'PRINT', 'PRIOR', 'PRIZE', 'PROOF', 'PROUD', 'PROVE', 'QUEEN', 'QUICK', 'QUIET', 'QUITE', 'RADIO', 'RAISE', 'RANGE', 'RAPID', 'RATIO', 'REACH', 'READY', 'REFER', 'RIGHT', 'RIVAL', 'RIVER', 'ROBIN', 'ROGER', 'ROMAN', 'ROUGH', 'ROUND', 'ROUTE', 'ROYAL', 'RURAL', 'SCALE', 'SCENE', 'SCOPE', 'SCORE', 'SENSE', 'SERVE', 'SEVEN', 'SHALL', 'SHAPE', 'SHARE', 'SHARP', 'SHEET', 'SHELF', 'SHELL', 'SHIFT', 'SHIRT', 'SHOCK', 'SHOOT', 'SHORT', 'SHOWN', 'SIGHT', 'SINCE', 'SIXTH', 'SIXTY', 'SIZED', 'SKILL', 'SLEEP', 'SLIDE', 'SMALL', 'SMART', 'SMILE', 'SMITH', 'SMOKE', 'SOLID', 'SOLVE', 'SORRY', 'SOUND', 'SOUTH', 'SPACE', 'SPARE', 'SPEAK', 'SPEED', 'SPEND', 'SPENT', 'SPLIT', 'SPOKE', 'SPORT', 'STAFF', 'STAGE', 'STAKE', 'STAND', 'START', 'STATE', 'STEAM', 'STEEL', 'STICK', 'STILL', 'STOCK', 'STONE', 'STOOD', 'STORE', 'STORM', 'STORY', 'STRIP', 'STUCK', 'STUDY', 'STUFF', 'STYLE', 'SUGAR', 'SUITE', 'SUPER', 'SWEET', 'TABLE', 'TAKEN', 'TASTE', 'TAXES', 'TEACH', 'TEETH', 'TERRY', 'TEXAS', 'THANK', 'THEFT', 'THEIR', 'THEME', 'THERE', 'THESE', 'THICK', 'THING', 'THINK', 'THIRD', 'THOSE', 'THREE', 'THREW', 'THROW', 'TIGHT', 'TIMES', 'TIRED', 'TITLE', 'TODAY', 'TOPIC', 'TOTAL', 'TOUCH', 'TOUGH', 'TOWER', 'TRACK', 'TRADE', 'TRAIN', 'TREAT', 'TREND', 'TRIAL', 'TRIED', 'TRIES', 'TRUCK', 'TRULY', 'TRUST', 'TRUTH', 'TWICE', 'UNDER', 'UNDUE', 'UNION', 'UNITY', 'UNTIL', 'UPPER', 'UPSET', 'URBAN', 'USAGE', 'USUAL', 'VALID', 'VALUE', 'VIDEO', 'VIRUS', 'VISIT', 'VITAL', 'VOICE', 'WASTE', 'WATCH', 'WATER', 'WHEEL', 'WHERE', 'WHICH', 'WHILE', 'WHITE', 'WHOLE', 'WHOSE', 'WOMAN', 'WOMEN', 'WORLD', 'WORRY', 'WORSE', 'WORST', 'WORTH', 'WOULD', 'WOUND', 'WRITE', 'WRONG', 'WROTE', 'YIELD', 'YOUNG', 'YOUTH']
word_6 = ['abroad','accept','access','across','acting','action','active','actual','advice','advise','affect','afford','afraid','agency','agenda','almost','always','amount','animal','annual','answer','anyone','anyway','appeal','appear','around','arrive','artist','aspect','assess','assist','assume','attack','attend','august','author','avenue','backed','barely','battle','beauty','became','become','before','behalf','behind','belief','belong','berlin','better','beyond','bishop','border','bottle','bottom','bought','branch','breath','bridge','bright','broken','budget','burden','bureau','button','camera','cancer','cannot','carbon','career','castle','casual','caught','center','centre','chance','change','charge','choice','choose','chosen','church','circle','client','closed','closer','coffee','column','combat','coming','common','comply','copper','corner','costly','county','couple','course','covers','create','credit','crisis','custom','damage','danger','dealer','debate','decade','decide','defeat','defend','define','degree','demand','depend','deputy','desert','design','desire','detail','detect','device','differ','dinner','direct','doctor','dollar','domain','double','driven','driver','during','easily','eating','editor','effect','effort','eighth','either','eleven','emerge','empire','employ','enable','ending','energy','engage','engine','enough','ensure','entire','entity','equity','escape','estate','ethnic','exceed','except','excess','expand','expect','expert','export','extend','extent','fabric','facing','factor','failed','fairly','fallen','family','famous','father','fellow','female','figure','filing','finger','finish','fiscal','flight','flying','follow','forced','forest','forget','formal','format','former','foster','fought','fourth','French','friend','future','garden','gather','gender','german','global','golden','ground','growth','guilty','handed','handle','happen','hardly','headed','health','height','hidden','holder','honest','impact','import','income','indeed','injury','inside','intend','intent','invest','island','itself','jersey','joseph','junior','killed','labour','latest','latter','launch','lawyer','leader','league','leaves','legacy','length','lesson','letter','lights','likely','linked','liquid','listen','little','living','losing','lucent','luxury','mainly','making','manage','manner','manual','margin','marine','marked','market','martin','master','matter','mature','medium','member','memory','mental','merely','merger','method','middle','miller','mining','minute','mirror','mobile','modern','modest','module','moment','morris','mostly','mother','motion','moving','murder','museum','mutual','myself','narrow','nation','native','nature','nearby','nearly','nights','nobody','normal','notice','notion','number','object','obtain','office','offset','online','option','orange','origin','output','oxford','packed','palace','parent','partly','patent','people','period','permit','person','phrase','picked','planet','player','please','plenty','pocket','police','policy','prefer','pretty','prince','prison','profit','proper','proven','public','pursue','raised','random','rarely','rather','rating','reader','really','reason','recall','recent','record','reduce','reform','regard','regime','region','relate','relief','remain','remote','remove','repair','repeat','replay','report','rescue','resort','result','retail','retain','return','reveal','review','reward','riding','rising','robust','ruling','safety','salary','sample','saving','saying','scheme','school','screen','search','season','second','secret','sector','secure','seeing','select','seller','senior','series','server','settle','severe','sexual','should','signal','signed','silent','silver','simple','simply','single','sister','slight','smooth','social','solely','sought','source','soviet','speech','spirit','spoken','spread','spring','square','stable','status','steady','stolen','strain','stream','street','stress','strict','strike','string','strong','struck','studio','submit','sudden','suffer','summer','summit','supply','surely','survey','switch','symbol','system','taking','talent','target','taught','tenant','tender','tennis','thanks','theory','thirty','though','threat','thrown','ticket','timely','timing','tissue','toward','travel','treaty','trying','twelve','twenty','unable','unique','united','unless','unlike','update','useful','valley','varied','vendor','versus','victim','vision','visual','volume','walker','wealth','weekly','weight','wholly','window','winner','winter','within','wonder','worker','wright','writer','yellow']

print('''
               HOW TO PLAY
Computer chooses a random word and you have to guess it. 
The word appearing in GREEN is IN the hidden word and is at the CORRECT place.
The word appearing in BLUE is IN the hidden word but is at INCORRECT place.
The word appearing in RED is NOT IN the hidden word anywhere.

Number of chances according to the length of word:
3 letter word -> 5 chances
4 letter word -> 6 chances
5 letter word -> 7 chances
6 letter word -> 9 chances 
      ''')

num=int(input("Word length (Currently available -> 3 - 6)\n"))

if num in [3,4,5,6]:
    pass
else:
    sleep(0.75)
    print('Please type a valid word length')
    sleep(0.75)
    num=int(input("Word length (Currently available -> 4 - 6)\n"))
    
if num==3:
    word=choice(word_3).upper()
    allowed=5
elif num==4:
    word=choice(word_4).upper() 
    allowed=6
elif num==5:
    word=choice(word_5).upper()
    allowed=7
elif num==6:
    word=choice(word_6).upper()
    allowed=9

guess=1

check=(input("(Chance {}) Your Guess?\n".format(guess))).upper()

if len(check)==num:
    pass
else:
    check=input("(Chance {0})Please enter a {1} letter word\n".format(guess,num)).upper()

cpu=list(word)
user=list(check)

while cpu!=user and guess!=allowed+1:
    for i in range(len(cpu)):
        if user[i]==cpu[i]:
           print(Fore.GREEN + Style.BRIGHT + user[i],end='')
        elif user[i] in cpu:
           print(Fore.BLUE + Style.BRIGHT + user[i],end='')
        else:
           print(Fore.RED + Style.BRIGHT + user[i],end='')
        
        sleep(0.1)
    
    print()
    guess+=1
    
    if guess<allowed+1:
        check=(input("(Chance {}) Your Guess?\n".format(guess))).upper()
           
        if len(check)==num:
            pass
        else:
            check=input("(Chance {0}) Please enter a {1} letter word\n".format(guess,num)).upper()
        
        user=list(check)
    else:
        pass
     
if cpu==user:
    for i in user:
        print(Fore.GREEN + Style.BRIGHT + i,end='')
        sleep(0.15)
    
    sleep(1)
    print('\nCongratulations! You found the word\n')
    
    sleep(1)
    print('Chances taken = {}'.format(guess))
else:
    print('\nSorry, you failed to find the word!\nThe word was {}'.format(word))
