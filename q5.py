import pandas as pd

# 1. Load the CSV into a DataFrame.
df = pd.read_csv('data/student_performance.csv')

# 2. Print the first five rows.
print("2. First 5 rows:\n", df.head())

# 3. Print the number of rows and columns.
print("\n3. Rows and Columns (Shape):", df.shape)

# 4. Display the column names.
print("\n4. Column Names:", df.columns.tolist())

# 5. Check whether the dataset contains missing values.
print("\n5. Missing Values:\n", df.isnull().sum())

# 6. Calculate the average Final_Score.
print("\n6. Average Final_Score:", df['Final_Score'].mean())

# 7. Find the student with the highest Final_Score.
highest_scorer = df.loc[df['Final_Score'].idxmax(), 'Student']
print("\n7. Student with highest Final_Score:", highest_scorer)

# 8. Create a new column: Improvement = Final_Score - Previous_Score.
df['Improvement'] = df['Final_Score'] - df['Previous_Score']
print("\n8. Created 'Improvement' column.")

# 9. Display only students with attendance greater than or equal to 80.
print("\n9. Students with Attendance >= 80:\n", df[df['Attendance'] >= 80])

# 10. Sort the DataFrame by Final_Score in descending order.
df_sorted = df.sort_values(by='Final_Score', ascending=False)
print("\n10. Sorted by Final_Score (descending).\n", df_sorted.head())

# 11. Save the processed DataFrame as processed_student_performance.csv.
df_sorted.to_csv('data/processed_student_performance.csv', index=False)
print("\n11. Saved processed DataFrame to 'processed_student_performance.csv'")
