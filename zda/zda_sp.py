import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv

# df = pd.read_csv('Student_Stress_Factors.csv')

data = {
    "anxiety_level": [],
    "self_esteem": [],
    "mental_health_history": [],
    "depression": [],
    "headache": [],
    "blood_pressure": [],
    "sleep_quality": [],
    "breathing_problem": [],
    "noise_level": [],
    "living_conditions": [],
    "safety": [],
    "basic_needs": [],
    "academic_performance": [],
    "study_load": [],
    "teacher_student_relationship": [],
    "future_career_concerns": [],
    "social_support": [],
    "peer_pressure": [],
    "extracurricular_activities": [],
    "bullying": [],
    "stress_level": []
}

with open('StressLevelDataset.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        data["anxiety_level"].append(int(row[0]))
        data["self_esteem"].append(int(row[1]))
        data["mental_health_history"].append(int(row[2]))
        data["depression"].append(int(row[3]))
        data["headache"].append(int(row[4]))
        data["blood_pressure"].append(int(row[5]))
        data["sleep_quality"].append(int(row[6]))
        data["breathing_problem"].append(int(row[7]))
        data["noise_level"].append(int(row[8]))
        data["living_conditions"].append(int(row[9]))
        data["safety"].append(int(row[10]))
        data["basic_needs"].append(int(row[11]))
        data["academic_performance"].append(int(row[12]))
        data["study_load"].append(int(row[13]))
        data["teacher_student_relationship"].append(int(row[14]))
        data["future_career_concerns"].append(int(row[15]))
        data["social_support"].append(int(row[16]))
        data["peer_pressure"].append(int(row[17]))
        data["extracurricular_activities"].append(int(row[18]))
        data["bullying"].append(int(row[19]))
        data["stress_level"].append(int(row[20]))

# Creating DataFrame
df = pd.DataFrame(data)

# Descriptive Statistics
desc_stats = df.describe()
desc_stats.to_csv('descriptive_statistics.csv')
with open('descriptive_statistics.txt', 'w') as file:
    file.write(desc_stats.to_string())

# Correlation Matrix
corr_matrix = df.corr()
corr_matrix.to_csv('correlation_matrix.txt', sep='\t', float_format='%.2f')

# Visualization
plt.figure(figsize=(16, 10))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

# Scatter Plot Matrix
sns.pairplot(df)
plt.suptitle("Scatter Plot Matrix", y=1.02)
plt.show()

plt.show()
