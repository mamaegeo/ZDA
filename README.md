# ZDA

## Téma semestrálního projektu: Analýza faktorů stresu u studentů

## Situace (Situation)

V rámci tohoto projektu jsem analyzoval faktory přispívající ke stresu mezi studenty. Využil jsem k tomu výsledky průzkumu Student Stress Factors z portalu kaggle.com (https://www.kaggle.com/datasets/rxnach/student-stress-factors-a-comprehensive-analysis/data), které obsahují různé typy faktorů jako:

- Psychologické faktory: 'anxiety_level', 'self_esteem', 'mental_health_history', 'depression'

- Fyziologické faktory: 'headache', 'blood_pressure', 'sleep_quality', 'breathing_problem'

- Environmentální faktory: 'noise_level', 'living_conditions', 'safety', 'basic_needs',

- Akademické faktory: 'academic_performance', 'study_load', 'teacher_student_relationship', 'future_career_concerns'

- Sociální faktor: 'social_support', 'peer_pressure', 'extracurricular_activities', 'bullying'

## Zadání (Task)

Cílem tohoto projektu je provést detailní analýzu faktorů, které ovlivňují úroveň stresu mezi studenty. Na základě získaných dat zkusím identifikovat hlavní faktory přispívající ke stresu a navrhnout opatření na jeho snížení.

Klíčové otázky:

1) Kolik studentů v minulosti uvedlo problémy s duševním zdravím?
2) Mají studenti, kteří zažívají šikanu, větší pravděpodobnost, že budou mít v minulosti problémy s duševním zdravím?
3) Uvádějí studenti se špatnou kvalitou spánku také vyšší míru deprese?
4) Existuje korelace mezi mírou úzkosti a akademickým výkonem?
5) U kterého faktoru (psychologického, fyziologického, environmentálního, akademického, sociálního) nejvíce studentů uvádí nejvyšší míru stresu?
6) Jaké jsou nejvýznamnější faktory vyvolávající stres u studentů?


## Akce (Action)

### Příprava dat

Data, která jsem dostal, byla v dobrém stavu. Po provedení kontroly správnosti formátu všech datových prvků a také kontroly chybějících hodnot, dospěl jsem k závěru, že data jsou relativně konzistentní.

Problém, na který jsem narazil, spočíval v rozmezích pro určité parametry:

anxiety_level: range from 0 to 21

self_esteem: range from 0 to 30

mental_health_history: range from 0 to 1

depression: range from 0 to 27

stress_level: range from 0 to 2

blood_pressure: range from 1 to 3

ostatní: range from 0 to 5

Po provedení vyšetření ohledně těchto parametrů jsem narazil na několik různých škálovacích systému, které se využívají k měření daných hodnot:

anxiety_level: Generalized Anxiety Disorder 7-item (GAD-7)

self_esteem: Rosenberg's Self-Esteem Scale

mental_health_history: 0 pravděpodobně znamená, že student nemá žádnou historii mentálního zdraví, 1 - že ji má

depression: Patient Health Questionnaire (PHQ-9)

ostatní: 0,1 - nizká úroveň, 2,3 - průměrná úroveň, 4,5 - vysoká úroveň


### Deskriptivní statistika
Základní deskriptivní analýza byla provedena v Pythonu s využitím knihovny Pandas a za pomoci PowerBI.

#### Psychické zdraví:

Úroveň úzkosti: Průměrná úroveň úzkosti byla kolem 11, s rozsahem od 0 do 21.

Sebeúcta: Průměrná úroveň sebeúcty byla asi 17.8, s rozsahem od 0 do 30.

Historie duševního zdraví: Téměř polovina respondentů (49.3%) uvádí historii duševních problémů.

#### Fyzické zdraví:

Deprese: Průměrná úroveň deprese byla přibližně 12.6, s rozsahem od 0 do 27.

Bolesti hlavy: Průměrná úroveň bolesti hlavy byla kolem 2.5, s rozsahem od 0 do 5.

Krevní tlak: Průměrná hodnota krevního tlaku nebyla zmíněna.

#### Životní podmínky:

Kvalita spánku: Průměrná kvalita spánku byla mírně nadprůměrná s hodnotou kolem 2.7, s rozsahem od 0 do 5.

Problémy s dýcháním: Průměrná úroveň problémů s dýcháním byla 2.7, s rozsahem od 0 do 5.

Hlučnost: Průměrná hlučnost byla kolem 2.6, s rozsahem od 0 do 5.

Životní podmínky: Nejčastěji jsou podmínky označeny jako průměrné.

#### Akademické prostředí:

Výkon ve škole: Průměrný výkon ve škole byl 2.8, s rozsahem od 0 do 5.

Zátěž studiem: Průměrná zátěž studiem byla 2.7, s rozsahem od 0 do 5.

Vztah učitel-žák: Vztahy mezi učiteli a studenty byly průměrně hodnoceny na 2.8.

#### Sociální faktory:

Obavy o budoucí kariéru: Průměrná úroveň obav o budoucí kariéru byla 2.8, s rozsahem od 0 do 5.

Sociální podpora: Průměrná úroveň sociální podpory byla 2.6, s rozsahem od 0 do 5.

Nátlak vrstevníků: Průměrný nátlak vrstevníků byl 1.0, s rozsahem od 0 do 2.

#### Další faktory:

Mimoškolní aktivity: Průměrně se mimoškolní aktivity hodnotily na 2.6.

Obtěžování: Průměrná úroveň obtěžování byla 2.6.

Úroveň stresu: Průměrná úroveň stresu byla 1.0, s rozsahem od 0 do 2.

Tyto výsledky poskytují přehled o tom, jak se studenti cítí a jaké faktory ovlivňují jejich životní situaci a akademický výkon.
![image](https://github.com/mamaegeo/ZDA/assets/135848732/8d829aa5-fc14-40b2-91f3-06501ab67bab)
![image](https://github.com/mamaegeo/ZDA/assets/135848732/f4eae43c-0e71-4bac-9ed4-e98b3c71a972)

Data s výsledky v textovém formátu a ve formátu csv jsou uloženy v souborech descriptive_statistics.csv a descriptive_statistics.txt.

### Korelační analýza

#### Korelační matice
Matice se nacházi v souboru correlation_matrix.txt

#### Nejvyšší korelace: 

Bullying a stress_level: 0.75

#### Nejnižší korelace: 

Self_esteem a stress_level: -0.76

#### Pozitivní korelace:

Anxiety_level a depression: 0.69

Anxiety_level a future_career_concerns: 0.72

Depression a headache: 0.66

Self_esteem a social_support: 0.68


#### Negativní korelace:

Anxiety_level a sleep_quality: -0.71

Self_esteem a future_career_concerns: -0.71

Sleep_quality a social_support: -0.68

Bullying a self_esteem: -0.76

### Otázky - Odpovědi:

1) Kolik studentů trpí stresem?

Celkový počet respondentů je 1100, ze kterých zhruba ⅔ (727) trpí stresem.

2) Kolik studentů v minulosti uvedlo problémy s duševním zdravím?
   
Z deskriptivní analýzy vyplývá, že téměř polovina respondentů (49.3%) uvádí historii duševních problémů.

3) Mají studenti, kteří zažívají šikanu, větší pravděpodobnost, že měli v minulosti problémy s duševním zdravím?
   
Téměř polovina respondentů (559 nebo 50.82%) zažila šikanu.

76.36% studentů, kteří zažili šikanu, mělo v minulosti problémy s duševním zdravím.

4) Uvádějí studenti se špatnou kvalitou spánku také vyšší míru deprese?
   
Z celkových 550 studentů, kteří mají nízkou kvalitu spánku jenom 10% má nízkou úroveň deprese, ostatní 90% mají vyšší míru deprese.

5) Existuje korelace mezi mírou úzkosti a akademickým výkonem?
   
Z korelační matice se dá odhalit, že korelace mezi úzkosti a akademickým výkonem je -0.65.

Negativní korelace mezi mírou úzkosti a akademickým výkonem naznačuje, že vyšší úroveň úzkosti souvisí s nižším akademickým výkonem, ale je důležité zmínit, že neříká nám, co přesně způsobuje tento vztah.

## Výsledek (Result)

### Obecně

V rámci semestrálního projektu jsem zkusil najít data, udělat jejich přípravu pro další zpracování, provést deskriptivní a korelační analýzy dat a odpovědět na některé zajímavé otázky ohledně faktorů stresu u studentů.

### Korelace vs kauzalita

Byl jsem upozorněn na problém korelace vs kauzalita a na problém s vyjadřováním v čj. V rámci své analýzy jsem provedl korelační analyzu, tzn. snažil jsem se zkoumat, jak parametry jsou spolu spojené. 

Korelace říká, jak moc se jeden parametr mění ve srovnání s druhým parametrem. Nicméně korelace neznamená nutně příčinný vztah mezi parametry.

Kauzalita označuje skutečný příčinný vztah mezi dvěma parametry, kde změny v jednom parametru skutečně způsobují změny v druhém.

Ikdyž některé závěry z grafů a popisné analýzy neobsahují kompletní důkaz k prokázání kauzality, myslím si, že zkoumání korelací mezi různými faktory přináší užitečný pohled na data.
Např. když se podíváme na korelační koeficient mezi mírou úzkosti a akademickým výkonem z 5. otázky, tak, podle mého názoru, to, že při zvýšení úrovně úzkosti může se očekávat, že akademický výkon klesne, a naopak, by mohlo naprosto odpovídat realitě, přestože kauzalita není prokázána. Ale je přece vhodné provést další analýzu pro zjištění příčinného vztahu.

### Analýza dat

Při analýze dat se odhalili některé zajímavé informace: 

- skoro ⅔ studentů trpí stresem 

- je velký počet studentů, kteří měli problémy s duševním zdravím a šikanou (skoro polovina). 

- úroveň deprese u studentů může být ve značné míře ovlivněn nedostatkem spánku

- existuje určitá korelace mezi úzkosti a akademickým výkonem

Návrh opatření na snížení stresu

je třeba věnovat zvýšenou pozornost duševnímu zdraví studentů a zlepšení podpůrných mechanismů

je důležité poskytnout prostředky a podporu pro studenty, kteří se potýkají s šikanou a které narazili na mentální problémy v minulosti

zvýšení povědomí u studentů o důležitosti spánku

Review

V rámci review zkusím porovnat svoje závěrečné myšlenky se statistiky z veřejných zdrojů na internetu.

Úroveň stresu

Podle zprávy Americké psychologické asociace z roku 2022 „Stres v Americe“ 46 % dospělých ve věku 18 až 35 let uvedlo, že „jsou většinu dní tak vystresovaní, že nemohou fungovat“. „ 46 % se liší od výsledku 66,6, který jsem získal já. Skupina respondentů zahrnuje studenty, ale mám podezření, že údaje o dospělých ve věku 23-26 až 35 let mohly zkreslit skutečnou úroveň stresu. 
V průzkumu agentury Gallup z března 2023, kterého se zúčastnilo více než 2 400 vysokoškolských studentů, 66 % z nich uvedlo, že zažívají stres, a 51 % uvedlo, že se cítí úzkostně „většinu dne“. Vzhledem k tomu, že tento průzkum byl zaměřen na vysokoškolské studenty a výsledek lépe odpovídá výsledku, ke kterému jsem dospěl já, řekl bych, že je docela velká šance, že údaje o úrovni stresu odpovídají realitě.

Šikana

Z dotazovaných studentů Texas A&M University-Commerce bylo 63,35 % od svého příchodu na vysokou školu svědky šikany a 27,15 % uvedlo, že se stali jejími oběťmi. Výsledky z průzkumu výše uvedené univerzity se v porovnání s mými výsledky (zhruba polovina studentů zažila šikanu) moc neshodují. Možnou příčinou může být absence podrobnějších popisů parametru v datech, se kterými jsem pracoval. V nich totiž nebyl žádný rozdíl mezi být oběti šikany anebo její svědkem, značilo se to obecně bullying.
 
Kvalita spánku a deprese

Konkrétní statistiku ohledně vztahu mezi depresi a kvalitou spánku tady neuvedu. Ale na webových stránkách National Library of Medicine jsem našel informace, že současná literatura stále podporuje obousměrný vztah mezi spánkem a depresí, nicméně význam kvality spánku se však stává velmi relevantní proměnnou.

Co se týká opatření, tak z článku www.usnews.com vyplývá, že nejlepší způsoby prevence a mitigace stresu jsou:

Budování a udržování sociálních vazeb

Spánek, dobrá strava a cvičení - “Healthy lifestyle”

Vyhledávání pomoci

Myslím si, že můj návrh zcela odpovídá výše zmíněným “opatřením”. Jenom asi je třeba zmínit, že “Budování a udržování sociálních vazeb” bylo v daném článku na prvním místě pravděpodobně kvůli čerstvým datům z doby covidu, který měla velký vliv na lidstvo včetně studentů. Ovšem v datasetu, který byl mnou použit, důraz byl na jiné sociální faktory. Ale samozřejmě uznávám, že budování a udržování sociálních vazeb může mít pozitivní vliv při zmírnění úrovně stresu.
 
