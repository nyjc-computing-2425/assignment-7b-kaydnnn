# Built-in imports
import math

GRADE = {}
for i in range(1, 40):
    GRADE[i] = "U"
for i in range(40, 45):
    GRADE[i] = "S"
for i in range(45, 50):
    GRADE[i] = "E"
for i in range(50, 55):
    GRADE[i] = "D"
for i in range(55, 60):
    GRADE[i] = "C"
for i in range(60, 70):
    GRADE[i] = "B"
for i in range(70, 101):
    GRADE[i] = "A"

def read_testscores(filename):
    """
    reads testscores from a csv file and puts it in a list

    Parameters
    ---------
    filename : string
        a string for the csv file to read from

    Returns
    ---------
    list
        a list of data read from the csv
    """
    data_list = []
    with open (filename) as file:
        data = file.readlines()[1:]
        for row in data:
            row = row.replace("\n", "").split(",")
            data_dict = {}
            overall = math.ceil((int(row[2])/30 * 15) + (int(row[3])/40 * 30) + (int(row[4])/80 * 35) + (int(row[5])/30 * 20))
            data_dict["class"] = row[0]
            data_dict["name"] = row[1]
            data_dict["overall"] = overall
            data_dict["grade"] = GRADE.get(overall)
            data_list.append(data_dict)
        
        #f.close() is called automatically
    
    return data_list


def analyze_grades(student_data):
    """
    analyze results from students from each class

    Parameters
    ---------
    student_data : list
        list of data acquired from reading csv

    Returns
    ---------
    nested dictionary
        a dictionary of dictionaries containing class, grade and the         grade count
    """
    data = {
        # "Classes" : {"Grade" : "Count"}
    }
    grades = []
    for each in range(len(student_data)):
        if each + 1 in range(len(student_data)) and student_data[each].get("class") == student_data[each + 1].get("class"):
            grades.append(student_data[each].get("grade"))
        elif(each + 1 not in range(len(student_data))):
            grades.append(student_data[each].get("grade"))
            data[student_data[each].get("class")] = {
                "A" : grades.count("A"),
                "B" : grades.count("B"),
                "C" : grades.count("C"),
                "D" : grades.count("D"),
                "E" : grades.count("E"),
                "S" : grades.count("S"),
                "U" : grades.count("U")
            }
        else:
            grades.append(student_data[each].get("grade"))
            data[student_data[each].get("class")] = {
                "A" : grades.count("A"),
                "B" : grades.count("B"),
                "C" : grades.count("C"),
                "D" : grades.count("D"),
                "E" : grades.count("E"),
                "S" : grades.count("S"),
                "U" : grades.count("U")
            }
            grades = []

    return data

studentdata = read_testscores("testscores.csv")
analysis = analyze_grades(studentdata)