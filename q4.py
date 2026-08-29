import numpy as np

# Creating the arrays using sample data (and the example array provided for final_scores)
hours_studied = np.array([5.5, 8.0, 3.2, 7.5, 6.1])
attendance = np.array([85, 95, 70, 90, 88])
previous_scores = np.array([65, 88, 55, 82, 72])
final_scores = np.array([70, 91, 58, 87, 76])

# 1. Print the shape and data type of each array
print("1. Shapes and Data Types:")
print(f"Hours Studied: Shape {hours_studied.shape}, Type {hours_studied.dtype}")
print(f"Attendance:    Shape {attendance.shape}, Type {attendance.dtype}")
print(f"Previous:      Shape {previous_scores.shape}, Type {previous_scores.dtype}")
print(f"Final Scores:  Shape {final_scores.shape}, Type {final_scores.dtype}\n")

# 2. Find the mean final score
print("2. Mean final score:", np.mean(final_scores))

# 3. Find the maximum and minimum final score
print("3. Max final score:", np.max(final_scores))
print("   Min final score:", np.min(final_scores))

# 4. Find the standard deviation of final scores
print("4. Standard deviation:", np.std(final_scores))

# 5. Add 5 bonus marks to every final score using NumPy array operations
bonus_scores = final_scores + 5
print("5. Scores with bonus:", bonus_scores)

# 6. Create a Boolean array showing which students scored at least 75
passed = final_scores >= 75
print("6. Boolean array (>= 75):", passed)

# 7. Use Boolean indexing to print only the scores greater than or equal to 75
print("7. Scores >= 75:", final_scores[passed])
