import csv
import shutil
from tempfile import NamedTemporaryFile

class IT_Academy:
    def view_course(self, filename):
        with open(filename, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            len = 0
            for row in csv_reader:
                if len == 0:
                    len += 1
                    continue
                print(f'Course: {row[0]} Fee: {row[1]}')
        print(">>>You are allowed to pay in two installments with Rs. 10000 each!<<<")

    def all_student_info(self, filename):
        with open(filename, mode='r') as file:
            csv_reader = csv.reader(file, delimiter=',')
            len = 0
            for row in csv_reader:
                if len == 0:
                    len += 1
                    continue
                else:
                     print(f'Id: {row[0]} \t Name: {row[1]}\t Address: {row[2]}\t Course: {row[3]}\t Deposited Amount: {row[4]}'
                        f'\t Due Left: {row[5]}\t Is_Graduated: {row[6]}')

    def individual_student_info(self, filename, s_id):
        with open(filename, mode='r') as file:
            csv_reader = csv.DictReader(file, delimiter=',')
            for row in csv_reader:
                if int(row["Id"]) == s_id:
                    print(f'ID: {row["Id"]} \t Name: {row["Name"]}\t Address: {row["Address"]}\tCourse: {row["Course"]}'
                          f'\t Payment done: {row["Deposited Amount"]} \t Amount Due: {row["Due Left"]}. ')

    def add_student(self, filename):
        info_lst = []
        with open(filename, mode='r') as file:
            csv_reader = csv.reader(file, delimiter=',')
            Rows = list(csv_reader)
            new_id = len(Rows) + 1
        with open(filename, mode='a+') as add:
            csv_writer = csv.writer(add)
            info_lst.append(new_id)
            info_lst.append(input("Enter your Name:"))
            info_lst.append(input("Enter your Address:"))
            info_lst.append((input("Enter Course you want to Enroll:")))
            info_lst.append(int(input("Enter payment amount:")))
            info_lst.append(20000 - info_lst[-1])
            info_lst.append(False)
            csv_writer.writerow(info_lst)

    def deposit(self, filename, amount, s_id, ):
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        fieldnames = ['Id', 'Name', 'Address', 'Course', 'Deposited Amount', 'Due Left', 'Is_Graduated']
        with open(filename, 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            writer = csv.DictWriter(tempfile, fieldnames=fieldnames)
            for row in reader:
                if row['Id'] == str(s_id):
                    row['Deposited Amount'] = int(row['Deposited Amount']) + amount
                    row['Due Left'] = int(row['Due Left']) - amount
                    writer.writerow({'Id': row['Id'], 'Name': row['Name'], 'Address': row['Address'], 'Course': row['Course'],
                         'Deposited Amount': row['Deposited Amount'],'Due Left': int(row['Due Left']),'Is_Graduated': row['Is_Graduated']})
                else:
                    writer.writerow({'Id': row['Id'], 'Name': row['Name'], 'Address': row['Address'], 'Course': row['Course'],
                         'Deposited Amount': row['Deposited Amount'], 'Due Left': row['Due Left'],'Is_Graduated': row['Is_Graduated']})
            shutil.move(tempfile.name, filename)

    def update(self, filename, s_id, change_column, value):
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        fieldnames = ['Id', 'Name', 'Address', 'Course', 'Deposited Amount', 'Due Left', 'Is_Graduated']
        with open(filename, 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            writer = csv.DictWriter(tempfile, fieldnames=fieldnames)
            for row in reader:
                if str(s_id) == row['Id']:
                    for field in row:
                        if change_column == field:
                            row[field] = value
                    writer.writerow({'Id': row['Id'], 'Name': row['Name'],'Address': row['Address'], 'Course': row['Course'],
                                     'Deposited Amount': row['Deposited Amount'], 'Due Left': row['Due Left'],'Is_Graduated': row['Is_Graduated']})
                else:
                    writer.writerow({'Id': row['Id'], 'Name': row['Name'],'Address': row['Address'], 'Course': row['Course'],
                                     'Deposited Amount': row['Deposited Amount'], 'Due Left': row['Due Left'],'Is_Graduated': row['Is_Graduated']})
            shutil.move(tempfile.name, filename)
            print("Successfully Updated Information")

    def delete(self, filename, id):
        self.filename = filename
        lines = list()
        with open(filename, 'r') as readfile:
            reader = csv.DictReader(readfile)
            for row in reader:
                lines.append(row)
                if int(row["Id"]) == id:
                    lines.remove(row)
        keys = lines[0].keys()
        print(list(keys))
        with open(filename, 'w') as writeFile:
            writer = csv.DictWriter(writeFile, keys)
            writer.writeheader()
            writer.writerows(lines)

        print("Successfully Removed")

    def refund(self, filename, s_id):
        with open(filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if bool(row["Is_Graduated"]) is True and int(row["Due Left"]) == 0 and int(row["Id"]) == s_id:
                    print("You have successfully graduated from {} course and your refund amount is Rs.20000".format(row["Course"]))
                break

if __name__ == "__main__":
    with open("Course_Book.csv", "w", newline='') as file:
        fieldnames = ['Course', 'Amount']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'Course': 'Full Stack Development', 'Amount': 20000})
        writer.writerow({'Course': 'Web Designing',          'Amount': 20000})
        writer.writerow({'Course': 'Data Mining & warehouse','Amount': 20000})
        writer.writerow({'Course': 'Graphic Designing',      'Amount': 20000})
        writer.writerow({'Course': 'AI/ML',                  'Amount': 20000})
        writer.writerow({'Course': 'Digital Marketing',      'Amount': 20000})
    
    with open("Student_Info.csv", "w") as file:
        fieldnames = ['Id', 'Name', 'Address', 'Course', 'Deposited Amount', 'Due Left', 'Is_Graduated']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({"Id": 1, 'Name': 'Supriya Shahi', 'Address': 'Kalanki', 'Course': 'Full Stack Development',
                         'Deposited Amount': 20000, 'Due Left': 0, 'Is_Graduated': True})
        writer.writerow({"Id": 2, 'Name': 'Pratik Shrestha', 'Address': 'Chabahil', 'Course': 'Full Stack Development',
                         'Deposited Amount': 15000, 'Due Left': 5000, 'Is_Graduated': True})
        writer.writerow({"Id": 3, 'Name': 'Dibya Shakya', 'Address': 'Kalimati', 'Course': 'Data Mining & warehouse', 'Deposited Amount': 20000, 'Due Left': 0,
             'Is_Graduated': False})
        writer.writerow({"Id": 4, 'Name': 'Aditi Sharma', 'Address': 'New Road', 'Course': 'Graphic Designing', 'Deposited Amount': 20000,
             'Due Left': 0, 'Is_Graduated': True})
        writer.writerow({"Id": 5, 'Name': 'Sajal Sapkota', 'Address': 'Lazimpat', 'Course': 'Digital Marketing', 'Deposited Amount': 10000,
             'Due Left': 10000, 'Is_Graduated': True})
        writer.writerow({"Id": 6, 'Name': 'Saman Pradhan', 'Address': 'Satdobato', 'Course': 'AI/ML', 'Deposited Amount': 8000, 'Due Left': 12000,
             'Is_Graduated': False})

    while True:
        print("ENTER YOUR OWN CHOICE:")
        ch = int(input("1.View course information\n"
                       "2.View all student details\n"
                       "3.View your informations\n"
                       "4.Deposit fee amount\n"
                       "5.Update information\n"
                       "6.Delete information\n"
                       "7.Add student detail\n"
                       "8.Return fee to graduate student. \n"))
        
        operation = IT_Academy()
        if ch == 1:
            operation.view_course('Course_Book.csv')
        elif ch == 2:
            operation.all_student_info('Student_Info.csv')
        elif ch == 3:
            id = int(input("Enter your Id:"))
            operation.individual_student_info("Student_Info.csv", id)
        elif ch == 4:
            id = int(input("Enter your Id:"))
            amt = int(input("Enter amount to deposit: "))
            operation.deposit('Student_Info.csv', amt, id)
            operation.all_student_info('Student_Info.csv')
        elif ch == 5:
            id = int(input("Enter your Id: "))
            col = input("Enter column you want to change:")
            val = input("Enter value to change: ")
            operation.update("Student_Info.csv", id, col, val)
        elif ch == 6:
            id = int(input("Enter your Id: "))
            operation.delete('Student_Info.csv', id)
        elif ch == 7:
            operation.add_student('Student_Info.csv')
        elif ch == 8:
            id = int(input("Enter your Id: "))
            operation.refund('Student_Info.csv', id)
        else:
            print("Invalid choice")
