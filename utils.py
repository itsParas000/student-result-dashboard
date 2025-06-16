import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    return pd.read_csv('data/students.csv')

def clean_data(df):
    df.fillna(df.mean(numeric_only=True), inplace=True)
    return df

def calculate_scores(df):
    df["Total"] = df[['Maths', 'Science', 'English']].sum(axis=1)
    df["Percentage"] = df["Total"] / 3
    return df

def get_topper(df):
    index = df['Total'].idxmax()
    return df.loc[index], index

def subject_averages(df):
    return df[['Maths', 'Science', 'English']].mean()

def plot_total_marks(df):
    plt.figure(figsize=(10, 5))
    plt.bar(df['Name'][:20], df['Total'][:20], color='skyblue')
    plt.xticks(rotation=45)
    plt.title("Total Marks of Students")
    plt.xlabel("Student")
    plt.ylabel("Total Marks")
    plt.tight_layout()
    plt.show()

def plot_student_pie(df, index):
    student = df.loc[index]
    subjects = ['Maths', 'Science', 'English']
    scores = student[subjects]
    plt.figure(figsize=(6, 6))
    plt.pie(scores, labels=subjects, autopct='%1.1f%%')
    plt.title(f"{student['Name']}'s Subject Performance")
    plt.show()

def save_single_student(df, index, filename="student_report.csv"):
    if 0 <= index < len(df):
        df.iloc[[index]].to_csv(filename, index=False)
        print(f"\n Report of {df.iloc[index]['Name']} saved as '{filename}'")
    else:
        print(" Invalid student index.")
