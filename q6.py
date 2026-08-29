import pandas as pd
import matplotlib.pyplot as plt

# Load the processed dataset from Q5
df = pd.read_csv('data/processed_student_performance.csv')

# 1. Bar chart: Student names vs final scores
# Using a wide figure size (18, 6) and rotating x-labels so all 80 names are readable
plt.figure(figsize=(18, 6))
plt.bar(df['Student'], df['Final_Score'], color='skyblue')
plt.title('Final Scores by Student')
plt.xlabel('Student Name')
plt.ylabel('Final Score')
plt.xticks(rotation=90, fontsize=8) 
plt.tight_layout() # Ensures labels are not cut off
plt.savefig('plots/final_scores.png')
plt.close()

# 2. Scatter plot: Hours studied vs final score
plt.figure(figsize=(8, 5))
plt.scatter(df['Hours_Studied'], df['Final_Score'], color='coral', alpha=0.7)
plt.title('Relationship Between Hours Studied and Final Score')
plt.xlabel('Hours Studied')
plt.ylabel('Final Score')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('plots/study_vs_score.png')
plt.close()

# 3. Histogram: Distribution of final scores
plt.figure(figsize=(8, 5))
plt.hist(df['Final_Score'], bins=10, color='lightgreen', edgecolor='black')
plt.title('Distribution of Final Scores')
plt.xlabel('Final Score Range')
plt.ylabel('Number of Students')
plt.tight_layout()
plt.savefig('plots/score_distribution.png')
plt.close()

# 4. Custom Plot: Attendance vs Final Score
plt.figure(figsize=(8, 5))
plt.scatter(df['Attendance'], df['Final_Score'], color='purple', alpha=0.7)
plt.title('Impact of Attendance on Final Score')
plt.xlabel('Attendance (%)')
plt.ylabel('Final Score')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('plots/custom_plot.png')
plt.close()

print("All visualzations have been successfully generated and saved.")
