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

## Akce (Action)

## Výsledek (Result)

## Shrnutí (Review)
