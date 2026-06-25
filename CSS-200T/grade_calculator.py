def calculate_final_grades():
    print("==================================================")
    print("🎓 CSS-200T: STUDENT ACADEMIC PERFORMANCE TRACKER")
    print("==================================================\n")
    
    # List of assignment scores out of 100
    scores = [88, 92, 79, 95, 64, 100, 81]
    
    total_points = sum(scores)
    total_assignments = len(scores)
    average = total_points / total_assignments
    
    print(f"📊 Total Assignments Processed: {total_assignments}")
    print(f"📊 Numeric Class Average: {average:.2f}%")
    
    # Conditional logic branch to determine letter grade
    if average >= 90:
        letter_grade = 'A'
    elif average >= 80:
        letter_grade = 'B'
    elif average >= 70:
        letter_grade = 'C'
    elif average >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
        
    print(f"🎯 Final Calculated Letter Grade: [{letter_grade}]")
    
    # Check for any performance outliers (failing grades)
    print("\n--- Flagging Assignments Needing Review ---")
    flagged = 0
    for idx, score in enumerate(scores, 1):
        if score < 70:
            print(f"⚠️ Review Needed: Assignment #{idx} scored low ({score}%)")
            flagged += 1
            
    if flagged == 0:
        print("✅ All assignments meet minimum passing standards.")
    print("\n==================================================")

if __name__ == "__main__":
    calculate_final_grades()
