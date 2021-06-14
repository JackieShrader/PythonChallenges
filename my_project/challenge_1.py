import pandas as pd


def main() -> int:
    # prompts user for the file location
    # filename = input("Please input the filename or directory route: ")

    # Just exists so I don't have to keep typing filename while testing
    filename = "my_project/2010-2011_Class_Size_-_Borough_Summary.csv"

    # reads in the data from the file
    in_csv = pd.read_csv(filename)

    print("Column names in alphabetical order: ")
    print(sorted(in_csv.columns))

    # This is including data rows plus the header rows
    print("Total number of rows in the file is: ", len(in_csv.index) + 1)

    # Sums together the number of students and class sections
    studentsAndSections = in_csv["NUMBER OF STUDENTS / SEATS FILLED"] + in_csv["NUMBER OF SECTIONS"]

    # Assigns the sum to a new column
    in_csv["New Total Students + Sections"] = studentsAndSections

    # Outputs the dataframe including the new column to a CSV
    in_csv.to_csv(r'NewCSVFile.csv', index=False)
    return 0


if __name__ == '__main__':
    exit(main())

