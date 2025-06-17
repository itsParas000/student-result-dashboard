from utils import (
    load_data, clean_data, calculate_scores, get_topper,
    subject_averages, plot_total_marks, plot_student_pie, save_single_student
)

def show_menu():
    print("\n Student Marks Report System")
    print("1. Show Topper")
    print("2. Show Subject Averages")
    print("3. Plot Bar Chart of Total Marks")
    print("4. Plot Pie Chart of a Student")
    print("5. Save a Student's Report to CSV")
    print("6. Exit")

def main():
    df = load_data()
    df = clean_data(df)
    df = calculate_scores(df)

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            topper, topper_index = get_topper(df)
            print(f"\n Topper: {topper['Name']} with {topper['Total']} marks (Index: {topper_index})")

        elif choice == '2':
            print("\n Subject Averages:")
            print(subject_averages(df))

        elif choice == '3':
            print("\n Showing Total Marks Chart...")
            plot_total_marks(df)

        elif choice == '4':
            try:
                index = int(input("Enter student index (0 to N): "))
                if 0 <= index < len(df):
                    plot_student_pie(df, index)
                else:
                    print(" Invalid index.")
            except ValueError:
                print(" Please enter a valid number.")

        
        elif choice == '5':
            try:
                index = int(input("Enter student index to save: "))
                filename = input("Enter filename (default: student_report.csv): ").strip()
                if filename == "":
                    filename = "student_report.csv"
                save_single_student(df, index, filename)
            except ValueError:
                print(" Please enter a valid number.")

        
        elif choice == '6':
            print("\n Exiting... Goodbye!")
            break

        else:
            print(" Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
