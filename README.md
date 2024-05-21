# ZDA

## Téma semestrální práce: Analyza faktorů stresu u studentů

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

![image](https://github.com/mamaegeo/ZDA/assets/135848732/9e619b53-c9ee-47c4-a0e2-9d4057504fe5)



## Výsledek (Result)

## Shrnutí (Review)
