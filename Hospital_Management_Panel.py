from datetime import date
import sqlite3

class Doctor:
    def __init__(self, name, surname, age, specialty, salary):
        self.name = name
        self.surname = surname
        self.age = age
        self.specialty = specialty
        self.salary = salary

    def show_info(self):
        print(f"""
            Name: {self.name}
            Surname: {self.surname}
            Age: {self.age}
            Specialty: {self.specialty}
            Salary: {self.salary}
        """)
class Nurse:
    def __init__(self, name, surname, age, unit, salary):
        self.name = name
        self.surname = surname
        self.age = age
        self.unit = unit
        self.salary = salary

    def show_info(self):
        print(f"""
            Name: {self.name}
            Surname: {self.surname}
            Age: {self.age}
            Unit: {self.unit}
            Salary: {self.salary}
        """)

class Patient:

    def __init__(self, name, surname, id, date_of_birth, sickness):
        self.name = name
        self.surname = surname
        self.id = id
        self.date_of_birth = date_of_birth
        self.sickness = sickness
        self.bill = 0


    def show_info(self):
        print("Patient İnfo:")
        print(f"""
            Name: {self.name}
            Surname: {self.surname}
            ID: {self.id}
            Date Of Birth: {self.date_of_birth}
        """)



class HospitalControlPanel:
    def __init__(self):
        self.db = "HospitalControlPanel.db"
        self.conn = sqlite3.connect(self.db)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS PATIENT(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NAME VARCHAR(50),
                SURNAME VARCHAR(50),
                IDENTITY_ VARCHAR(11),
                DATEOFBIRTH DATE,
                SICKNESS VARCHAR(50)
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS NURSE(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NAME VARCHAR(50),
                SURNAME VARCHAR(50),
                AGE VARCHAR(3),
                UNIT VARCHAR(30),
                SALARY INTEGER
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS DOCTOR(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NAME VARCHAR(50),
                SURNAME VARCHAR(50),
                AGE VARCHAR(3),
                SPECIALTY VARCHAR(40),
                SALARY INTEGER
            )
        """)

    def add_doctor(self):
        try:
            print("Add Doctor:")
            name = input("Name: ")
            surname = input("Surname: ")
            age = input("Age: ")
            specialty = input("Specialty: ")
            salary = int(input("Salary: "))
            doctor = Doctor(name, surname, age, specialty, salary)
            self.cursor.execute("INSERT INTO DOCTOR (NAME, SURNAME, AGE, SPECIALTY, SALARY) VALUES (?,?,?,?,?)",
                                (doctor.name, doctor.surname, doctor.age, doctor.specialty, doctor.salary))
            self.conn.commit()
            print(f"{doctor.name} {doctor.surname} added the system")
        except ValueError:
            print("Please write a numerical data to salary part and try again.")


    def add_nurse(self):
        try:
            name = input("Name: ")
            surname = input("Surname: ")
            age = input("Age: ")
            unit = input("Unit: ")
            salary = int(input("Salary: "))
            nurse = Nurse(name, surname, age, unit, salary)
            self.cursor.execute("INSERT INTO NURSE (NAME, SURNAME, AGE, UNIT, SALARY) VALUES (?,?,?,?,?)",
                                (nurse.name, nurse.surname, nurse.age, nurse.unit, nurse.salary))
            self.conn.commit()
            print(f"{nurse.name} {nurse.surname} added the system.")
        except ValueError:
            print("Please write a numerical data to salary part and try again.")

    def add_patient(self):
        name = input("Name: ")
        surname = input("Surname: ")
        id = input("Identıty number(with 11 number): ")
        date_of_birth = input("Date Of Birth(YYYY-MM-DD): ")
        sickness = input("Sickness: ")
        patient = Patient(name, surname, id, date_of_birth, sickness)
        self.cursor.execute("INSERT INTO PATIENT (NAME, SURNAME, IDENTITY_,DATEOFBIRTH, SICKNESS) VALUES(?,?,?,?,?)", (patient.name, patient.surname, patient.id, patient.date_of_birth, patient.sickness))
        self.conn.commit()
        print(f"{patient.name} {patient.surname} added the system.")

    def delete_doc(self):
        print("Delete Doctor: \n")
        id = input("Please write id: ")
        d = self.cursor.execute("DELETE FROM DOCTOR WHERE ID = ?", (id, ))
        self.conn.commit()
        if d:
            print(f"{id} deleted system")
        else:
            print(f"{id} not found.")

    def delete_nurse(self):
        print("Delete Nurse: ")
        id = input("Please write id: ")
        d = self.cursor.execute("DELETE FROM NURSE WHERE ID = ?", (id,))
        self.conn.commit()
        if d:
            print(f"{id} deleted system")
        else:
            print(f"{id} not found.")

    def delete_patient(self):
        print("Delete Patient: ")
        id = input("Please write id: ")
        d = self.cursor.execute("DELETE FROM PATIENT WHERE ID = ?", (id,))
        self.conn.commit()
        if d:
            print(f"{id} deleted system")
        else:
            print(f"{id} not found.")

    def get_patient_id(self):
        name = input("Please write the name of a patient: ")
        self.cursor.execute("SELECT ID FROM PATIENT WHERE NAME = ?", (name, ))
        result = self.cursor.fetchone()
        print(result[0])
        return result[0] if result else None

    def get_nurse_id(self):
        name = input("Please write the name of a nurse: ")
        self.cursor.execute("SELECT ID FROM NURSE WHERE NAME = ?", (name, ))
        result = self.cursor.fetchone()
        print(result[0])
        return result[0] if result else None

    def get_doctor_id(self):
        name = input("Please write the name of a doctor: ")
        self.cursor.execute("SELECT ID FROM DOCTOR WHERE NAME = ?", (name, ))
        result = self.cursor.fetchone()
        print(result[0])
        return result[0] if result else None



    def patient_exit(self):
        print("Patient Exit: ")
        id = input("Please write id: ")
        s = self.cursor.execute("SELECT * FROM PATIENT WHERE ID = ?", (id, )).fetchone()
        print(s)
        patient = Patient(s[1], s[2], s[3], s[4], s[5])
        patient.is_here = True
        patient.out()

    def show_all_patient(self):
        self.cursor.execute("SELECT * FROM PATIENT")
        patients = self.cursor.fetchall()
        if not patients:
            print("There is no patients in the hospital now.")
        else:
            print("\nPatients:")
            for patient in patients:
                patient_obj = Patient(*patient[1:])
                patient_obj.show_info()

    def show_all_nurse(self):
        self.cursor.execute("SELECT * FROM NURSE")
        nurses = self.cursor.fetchall()
        if not nurses:
            print("There is no nurses in the hospital now.")
        else:
            print("\nNurses:")
            for nurse in nurses:
                nurse_obj = Nurse(*nurse[1:])
                nurse_obj.show_info()


    def show_all_doctor(self):
        self.cursor.execute("SELECT * FROM DOCTOR")
        doctors = self.cursor.fetchall()
        if not doctors:
            print("There is no doctors in the hospital now.")
        else:
            print("\nDoctors:")
            for doctor in doctors:
                doctor_obj = Doctor(*doctor[1:])
                doctor_obj.show_info()


    def close_connection(self):
        self.conn.close()


hospital = HospitalControlPanel()
while True:
    hospital.create_tables()
    print(20*"*", "Hospital Management Panel", 20*"*")
    print("""
        1. Add Patient
        2. Add Nurse
        3. Add Doctor
        4. Delete Nurse
        5. Delete Doctor
        6. Delete Patient
        7. Get Patient id
        8. Get Nurse id
        9. Get Doctor id
        10. Show All Patients
        11. Show All Nurses
        12. Show All Doctors
        13. Close Program
    """)
    proc = input("Process: ")
    if proc == "1":
        hospital.add_patient()
    elif proc == "2":
        hospital.add_nurse()
    elif proc == "3":
        hospital.add_doctor()
    elif proc == "4":
        hospital.delete_nurse()
    elif proc == "5":
        hospital.delete_doc()
    elif proc == "6":
        hospital.delete_patient()
    elif proc == "7":
        hospital.get_patient_id()
    elif proc == "8":
        hospital.get_nurse_id()
    elif proc == "9":
        hospital.get_doctor_id()
    elif proc == "10":
        hospital.show_all_patient()
    elif proc == "11":
        hospital.show_all_nurse()
    elif proc == "12":
        hospital.show_all_doctor()
    elif proc == "13":
        print("Exiting system...")
    else:
        print("You write something wrong.")
        break


























