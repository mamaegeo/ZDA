# ZDA

## Téma semestrálního projektu: Analyza faktorů stresu u studentů

## Situace (Situation)

V rámci tohoto projektu jsem analyzoval faktory přispívající ke stresu mezi studenty. Využil jsem k tomu výsledky průzkumu Student Stress Factors z portalu kaggle.com (https://www.kaggle.com/datasets/rxnach/student-stress-factors-a-comprehensive-analysis/data), které obsahují různé typy faktorů jako:

- Psychologické faktory: 'anxiety_level', 'self_esteem', 'mental_health_history', 'depression'

- Fyziologické faktory: 'headache', 'blood_pressure', 'sleep_quality', 'breathing_problem'

- Environmentální faktory: 'noise_level', 'living_conditions', 'safety', 'basic_needs',

- Akademické faktory: 'academic_performance', 'study_load', 'teacher_student_relationship', 'future_career_concerns'

- Sociální faktor: 'social_support', 'peer_pressure', 'extracurricular_activities', 'bullying'

## Zadání (Task)

Cílem bylo identifikovat, které faktory mají největší dopad na úroveň stresu studentů. Bylo potřeba provést komplexní analýzu dat k odhalení trendů/silných korelací/vzorců, které by mohly pomoci při pochopení a zmírnění stresu u studentů.

## Akce (Action)

### Příprava dat

Data, která jsem dostal, byla v dobrém stavu. Po provedení kontroly správnosti formátu všech datových prvků a také kontroly chybějících hodnot, dospěl jsem k závěru, že data jsou relativně konzistentní.

Jedniný problém, na který jsem narazil, spočíval v rozmezích pro určité parametry:

anxiety_level: range from 0 to 21

self_esteem: range from 0 to 30

mental_health_history: range from 0 to 1

depression: range from 0 to 27

ostatní více méně: range from 0 to 5

Po provedení vyšetření ohledně těchto parametrů jsem narazil na několik různých škalovacích systému, které se využívají k měření daných hodnot:

anxiety_level: Generalized Anxiety Disorder 7-item (GAD-7)

self_esteem: Rosenberg's Self-Esteem Scale

mental_health_history: 0 pravděpodobně znamená, že student nemá žádnou historii mentalního zdraví, 1 - že ji má

depression: Patient Health Questionnaire (PHQ-9)

ostatní: 0,1 - nizká úroveň, 2,3 - průměrná úroveň, 4,5 - vysoká úroveň

### Deskriptivní statistika
Základní diskreptivní analýza byla provedena v Pythonu s využitím knihovny Pandas a za pomoci PowerBI.

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

Data s výsledky jsou uloženy v souborech descriptive_statistics.csv a descriptive_statistics.txt.

### Korelační analýza

#### Korelační matice
Matice se nacházi v souboru correlation_matrix.txt a 

#### Nejvyšší korelace:

Future_career_concerns a stress_level: 0.74

#### Nejnižší korelace:

Self_esteem a blood_pressure: -0.76

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

## Výsledek (Result)

Existuje silný pozitivní vztah mezi úrovní úzkosti a obavami o budoucí kariéru (0.72), což naznačuje, že vyšší úroveň úzkosti může být spojena s většími obavami o budoucnost.

Podobně silný pozitivní vztah je i mezi obavami o budoucí kariéru a úrovní stresu (0.74), což naznačuje, že lidé se silnými obavami o budoucí kariéru často prožívají také vyšší úroveň stresu.

Také existuje silný negativní vztah mezi sebeúctou a zážitkem šikanování (-0.76), což naznačuje, že nižší úroveň sebeúcty může být spojena s vyšší pravděpodobností zkušenosti se šikanováním.

Mezi úzkostí a kvalitou spánku je silná negativní korelace (-0.71), což naznačuje, že vyšší úroveň úzkosti může vést k horší kvalitě spánku.

Také mezi sebeúctou a sociální podporou existuje silná pozitivní korelace (0.68), což znamená, že lidé s vyšší úrovní sebeúcty mají tendenci mít také větší sociální podporu.

## Shrnutí (Review)

V rámci semestrálního projektu jsem zkisil najít data, udělat jejích přípravu pro další zpracování, provést diskriptivní a korelační analýzy dat a definovat zavěry, které vyplývají z analýzy.
