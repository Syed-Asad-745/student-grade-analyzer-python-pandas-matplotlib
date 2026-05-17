import pandas as pd
import matplotlib.pyplot as plt

#-----------------------------loads "students.csv" file-----------------------
def load_file(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        return None

#---------takes the pandas data frame and returns a readable dictionary---------
def analyze_data(df):
    highest = df["Grade"].max()
    lowest = df["Grade"].min()
    average = df["Grade"].mean().round(1)
    passed = len(df[df["Grade"] >= 50])

    formatted_data = {"Highest" : highest,
                      "Lowest" : lowest,
                      "Average" : average,
                      "Passed" : passed}
    return formatted_data

#------------------------displays statistics on console---------------------------
def display_stats(stats):
    print(f"The highest grade is: {stats['Highest']}")
    print(f"The lowest grade is: {stats['Lowest']}")
    print(f"The average grade is: {stats['Average']}")
    print(f"The number of students passed is: {stats['Passed']}")

#----------------------plots a bar chart using matplotlib---------------------------
def plot_grades(df,stats):
    colors = ["green" if grade >= stats["Average"] else "red" for grade in df["Grade"]]
    plt.bar(df["Name"], df["Grade"], color=colors)
    plt.xlabel("Students")
    plt.ylabel("Grades")
    plt.title("Class Grades")
    plt.axhline(y=stats["Average"], color="red", linestyle="--", label="Average")
    plt.legend()
    plt.tight_layout()
    plt.show()

#------------------------------------main function------------------------------------
def main():
    df = load_file("students.csv")
    if df is None:
        return
    
    required_columns = ["Name", "Grade"]
    for col in required_columns:
        if col not in df.columns:
            print(f"Missing column: {col}")
            return

    stats = analyze_data(df)
    display_stats(stats)
    plot_grades(df,stats)


if __name__ == "__main__":
    main()