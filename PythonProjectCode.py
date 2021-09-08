import serial
import time
import sqlite3
from datetime import date

conn = sqlite3.connect('database1.db')
conn.isolation_level = None
cursor = conn.cursor()

# *** ----------------------------------------------------------
z1baudrate = 9600  # Set the Baudrate before running it
z1port = 'COM3'  # set the correct port before run it
# *** ----------------------------------------------------------

z1serial = serial.Serial(port=z1port, baudrate=z1baudrate)

try:
    z1serial = serial.Serial('COM3', 9600, timeout=1)
    z1serial.timeout = 2  # set read timeout
    print("******************************************")
    print(" Opening the Serial port - Success")
    print("******************************************")
except:
    print("\n")
    print("******************************************")
    print(" Opening the Serial port - Failed")
    print("******************************************")

if z1serial.is_open:
    while True:

        # -- Read the data from the Serial port
        # -- Sample data looks like : "TXN0A-0D93B3DD-37DE3963"
        # -- Data received in the serial port needs to be parsed based on the '-'
        # -- First part is the Transaction type : "TXN0A"
        # -  Second part is the Student_id       : "0D93B3DD"
        # -- Third part is the book id          : "37DE3963"
        data = z1serial.readline().decode('ascii')
        data1 = data.strip()
        if (data1 > ""):
            if (data1[0:3] == "TXN"):
                pass
            else:
                print(data)

        InParms = data.split('-')
        if (InParms[0] == "TXN00:"):
            print("* ************************************************************** *")
            print("*                                                                *")
            print("*           Supported Menu                                       *")
            print("*           --------------                                       *")
            print("*           Key [A]    : Issue Book                              *")
            print("*           Key [B]    : Return Book                             *")
            print("*           Key [C]    : Student Info                            *")
            print("*           Key [D]    : Book Info                               *")
            print("*           Key [*]    : Project Details                         *")
            print("*           Key [0]    : Display Menu                            *")
            print("*           Key [1 - 9]: Currently not used                      *")
            print("*                                                                *")
            print("* ************************************************************** *")
        else:
            pass

        if (InParms[0] == "TXN01:"):
            print("* ************************************************************** *")
            print("*                                                                *")
            print("* Selected key [1] is not currently used                         *")
            print("* Please press [0] for supported keys                            *")
            print("*                                                                *")
            print("* ************************************************************** *")
        else:
            pass

        if (InParms[0] == "TXN02:"):
            print("* ************************************************************** *")
            print("*                                                                *")
            print("* Selected key [2] is not currently used                         *")
            print("* Please press [0] for supported keys                            *")
            print("*                                                                *")
            print("* ************************************************************** *")
        else:
            pass

        if (InParms[0] == "TXN03:"):
            print("* ************************************************************** *")
            print("*                                                                *")
            print("* Selected key [3] is not currently used                         *")
            print("* Please press [0] for supported keys                            *")
            print("*                                                                *")
            print("* ************************************************************** *")
        else:
            pass

        if (InParms[0] == "TXN04:"):
            print("* ************************************************************** *")
            print("*                                                                *")
            print("* Selected key [4] is not currently used                         *")
            print("* Please press [0] for supported keys                            *")
            print("*                                                                *")
            print("* ************************************************************** *")
        else:
            pass
        if (InParms[0] == "TXN05:"):
            print("* ************************************************************** *")
            print("*                                                                *")
            print("* Selected key [5] is not currently used                         *")
            print("* Please press [0] for supported keys                            *")
            print("*                                                                *")
            print("* ************************************************************** *")
        else:
            pass
        if (InParms[0] == "TXN06:"):
            print("* ************************************************************** *")
            print("*                                                                *")
            print("* Selected key [6] is not currently used                         *")
            print("* Please press [0] for supported keys                            *")
            print("*                                                                *")
            print("* ************************************************************** *")
        else:
            pass

        if (InParms[0] == "TXN07:"):
            print("* ************************************************************** *")
            print("*                                                                *")
            print("* Selected key [7] is not currently used                         *")
            print("* Please press [0] for supported keys                            *")
            print("*                                                                *")
            print("* ************************************************************** *")
        else:
            pass

        if (InParms[0] == "TXN08:"):
            print("* ************************************************************** *")
            print("*                                                                *")
            print("* Selected key [8] is not currently used                         *")
            print("* Please press [0] for supported keys                            *")
            print("*                                                                *")
            print("* ************************************************************** *")
        else:
            pass

        if (InParms[0] == "TXN09:"):
            print("* ************************************************************** *")
            print("*                                                                *")
            print("* Selected key [9] is not currently used                         *")
            print("* Please press [0] for supported keys                            *")
            print("*                                                                *")
            print("* ************************************************************** *")
        else:
            pass

        if (InParms[0] == "TXN0*:"):
            print("* ************************************************************** *")
            print("*                                                                *")
            print("* Project name : Arduino based Library management system         *")
            print("* Profressor   :                                                 *")
            print("* Project by   : Rohit (19BCE1493)                               *")
            print("*                                                                *")
            print("*                                                                *")
            print("*                                                                *")
            print("* Hardware used: Arduino UNO                                     *")
            print("*                RFID Scanner                                    *")
            print("*                KeyPad                                          *")
            print("*                Active Buzzer                                   *")
            print("* Software used: Arduino Sketch                                  *")
            print("*                Python 3.6                                      *")
            print("*                SQLITE database                                 *")
            print("* Development tools used : Python IDLE                           *")
            print("*                          Aruino Studio                         *")
            print("*                                                                *")
            print("* ************************************************************** *")
        else:
            pass

            # -- -----------------------------------------------------
            # -- Following code is for Issue Book transaction
            # -- -----------------------------------------------------
        if (InParms[0] == "TXN0A:"):
            curr_txn_id = InParms[0].strip()
            curr_patron_id = InParms[1].strip()
            curr_book_id = InParms[2].strip()

            print("--------------------------------------------")
            print("Selected transaction is : ", curr_txn_id)
            print("Student id is            : ", curr_patron_id)
            print("Book id is              : ", curr_book_id)
            print("Retrieving data from DB ...")
            print("--------------------------------------------")
            sql101 = "SELECT * FROM Student WHERE student_id = ?"
            try:
                cursor = conn.cursor()
                cursor.execute(sql101, [curr_patron_id])
                rows = cursor.fetchall()
                for row in rows:
                    print("Student id      : ", row[0])
                    print("First name     : ", row[1])
                    print("Last name      : ", row[2])
                    print("Enroll date    : ", row[3])
                    print("Address-01     : ", row[4])
                    print("Address-02     : ", row[5])
                    print("Address-03     : ", row[6])
                    print("\n")
            except sqlite3.Error as e:
                print("An error occurred in SQL_101:", e.args[0])

            sql102 = "SELECT * FROM Book WHERE book_id = ?"
            try:
                cursor = conn.cursor()
                cursor.execute(sql102, [curr_book_id])
                rows = cursor.fetchall()
                for row in rows:
                    print("Book id        : ", row[0])
                    print("ISBN           : ", row[1])
                    print("Title          : ", row[2])
                    print("Enroll date    : ", row[3])
                    print("Author         : ", row[4])
                    print("Publisher      : ", row[5])
                    print("\n")


            except sqlite3.Error as e:
                print("An error occurred in SQL_102:", e.args[0])

            sql103 = """SELECT DISTINCT 'Y' FROM StudentBook
            			             WHERE book_id = ? AND RETURN_FLAG = 'N'"""
            try:
                print("Checking if the book is already issued ...")
                cursor = conn.cursor()
                cursor.execute(sql103, [curr_book_id])
                rows = cursor.fetchall()
                Error_Flag = 'N'
                for row in rows:
                    if (row[0] == 'Y'):
                        Error_Flag = 'Y'
                        break
                    else:
                        pass
                if (Error_Flag == 'N'):
                    sql104 = """INSERT INTO StudentBook (student_id,
            					            book_id,issue_date,RETURN_FLAG)
            								VALUES(?,?,?,'N')"""
                    try:
                        today = date.today()
                        d1 = today.strftime("%d-%m-%Y")
                        cursor = conn.cursor()
                        parms = (curr_patron_id, curr_book_id, d1)
                        cursor.execute(sql104, parms)
                        print("Book Issued successfully")
                        conn.commit()
                    except sqlite3.Error as e:
                        print("An error occurred in SQL_104:", e.args[0])
                    sql105 = """UPDATE StudentBook
            				    SET fname = (SELECT first_name FROM Student
            				    WHERE Student.student_id = StudentBook.student_id)"""
                    try:
                        today = date.today()
                        d1 = today.strftime("%d-%m-%Y")
                        cursor = conn.cursor()
                        cursor.execute(sql105)
                        conn.commit()
                    except sqlite3.Error as e:
                        print("An error occurred in SQL_105:", e.args[0])
                    sql106 = """UPDATE StudentBook SET lname =
            				 (SELECT last_name FROM Student
            				WHERE Student.student_id = StudentBook.student_id)"""
                    try:
                        today = date.today()
                        d1 = today.strftime("%d-%m-%Y")
                        cursor = conn.cursor()
                        cursor.execute(sql106)
                        conn.commit()
                    except sqlite3.Error as e:
                        print("An error occurred in SQL_106:", e.args[0])
                    sql107 = """UPDATE StudentBook SET b_title = (
            				SELECT title FROM BOOK WHERE
            				BOOK.book_id = StudentBook.book_id)"""
                    try:
                        today = date.today()
                        d1 = today.strftime("%d-%m-%Y")
                        cursor = conn.cursor()
                        cursor.execute(sql107)
                        conn.commit()
                    except sqlite3.Error as e:
                        print("An error occurred in SQL_107:", e.args[0])
                else:
                    print("???????????????????????????????????????????????????")
                    print(" Error : This book is already Issued, please check ")
                    print("???????????????????????????????????????????????????")
            except sqlite3.Error as e:
                print("An error occurred in SQL_103:", e.args[0])
        else:
            pass

            # -- -----------------------------------------------------
            # -- Following code is for Issue Book transaction
            # -- -----------------------------------------------------
        if (InParms[0] == "TXN0B:"):
            curr_txn_id = InParms[0].strip()
            curr_book_id = InParms[1].strip()
            print("--------------------------------------------")
            print("Selected transaction is : ", curr_txn_id)
            print("Book id is              : ", curr_book_id)
            print("Retrieving data from DB ...")
            print("--------------------------------------------")

            sql101 = """SELECT * FROM StudentBook
            			            WHERE book_id = ? AND RETURN_FLAG = 'N'"""
            try:
                cursor = conn.cursor()
                cursor.execute(sql101, [curr_book_id])
                rows = cursor.fetchall()
                for row in rows:
                    print("Student id       : ", row[0])
                    print("Book id        : ", row[1])
                    print("Issue date     : ", row[2])
                    curr_patron_id = row[0].strip()
                    print("\n")
            except sqlite3.Error as e:
                print("An error occurred in SQL_001:", e.args[0])
            sql102 = "SELECT * FROM Student WHERE student_id = ?"
            try:
                cursor = conn.cursor()
                cursor.execute(sql102, [curr_patron_id])
                rows = cursor.fetchall()
                for row in rows:
                    print("Student id      : ", row[0])
                    print("First name     : ", row[1])
                    print("Last name      : ", row[2])
                    print("Enroll date    : ", row[3])
                    print("Address-01     : ", row[4])
                    print("Address-02     : ", row[5])
                    print("Address-03     : ", row[6])
                    print("\n")
            except sqlite3.Error as e:
                print("An error occurred in SQL_001:", e.args[0])
            sql103 = "SELECT * FROM BOOK WHERE book_id = ?"
            try:
                cursor = conn.cursor()
                cursor.execute(sql103, [curr_book_id])
                rows = cursor.fetchall()
                for row in rows:
                    print("Book id        : ", row[0])
                    print("ISBN           : ", row[1])
                    print("Title          : ", row[2])
                    print("Enroll date    : ", row[3])
                    print("Author         : ", row[4])
                    print("Publisher      : ", row[5])
                    print("\n")
            except sqlite3.Error as e:
                print("An error occurred in SQL_001:", e.args[0])
            sql103 = """SELECT DISTINCT 'Y' FROM StudentBook
            			             WHERE book_id = ? AND RETURN_FLAG = 'N'"""
            try:
                cursor = conn.cursor()
                cursor.execute(sql103, [curr_book_id])
                rows = cursor.fetchall()
                Found_Flag = 'N'
                for row in rows:
                    if (row[0] == 'Y'):
                        Found_Flag = 'Y'
                        break
                    else:
                        pass
                if (Found_Flag == 'Y'):
                    today = date.today()
                    d1 = today.strftime("%d-%m-%Y")
                    sql104 = '''UPDATE StudentBook SET RETURN_FLAG = ?
                                            WHERE student_id = ? AND book_id = ?
                                            AND RETURN_FLAG = 'N' '''
                    try:
                        today = date.today()
                        d1 = today.strftime("%d-%m-%Y")
                        cursor = conn.cursor()
                        parms = ("Y", curr_patron_id, curr_book_id)
                        print("parms     : ", parms)
                        cursor.execute(sql104, parms)
                        print("Book returned successfully")
                        conn.commit()
                    except sqlite3.Error as e:
                        print("An error occurred in SQL_001:", e.args[0])
                else:
                    print("???????????????????????????????????????????????????")
                    print(" Error : This book is already returned, please check ")
                    print("???????????????????????????????????????????????????")
            except sqlite3.Error as e:
                print("An error occurred in SQL_103:", e.args[0])
        else:
            pass

            # -- -----------------------------------------------------
            # -- Following code is for Issue Book transaction
            # -- -----------------------------------------------------
        if (InParms[0] == "TXN0C:"):
            curr_txn_id = InParms[0].strip()
            curr_patron_id = InParms[1].strip()
            print("--------------------------------------------")
            print("Selected transaction is : ", curr_txn_id)
            print("Student id is            : ", curr_patron_id)
            print("Retrieving data from DB ...")
            print("--------------------------------------------")

            sql101 = "SELECT * FROM Student WHERE student_id = ?"
            try:
                cursor = conn.cursor()
                cursor.execute(sql101, [curr_patron_id])
                rows = cursor.fetchall()
                for row in rows:
                    print("Student id      : ", row[0])
                    print("First name     : ", row[1])
                    print("Last name      : ", row[2])
                    print("Enroll date    : ", row[3])
                    print("Address-01     : ", row[4])
                    print("Address-02     : ", row[5])
                    print("Address-03     : ", row[6])
                    print("\n")
            except sqlite3.Error as e:
                print("An error occurred in SQL_001:", e.args[0])
        else:
            pass

            # -- -----------------------------------------------------
            # -- Following code is for Issue Book transaction
            # -- -----------------------------------------------------
        if (InParms[0] == "TXN0D:"):
            curr_txn_id = InParms[0].strip()
            curr_book_id = InParms[1].strip()
            print("--------------------------------------------")
            print("Selected transaction is : ", curr_txn_id)
            print("Book id is              : ", curr_book_id)
            print("Retrieving data from DB ...")
            print("--------------------------------------------")

            sql102 = "SELECT * FROM BOOK WHERE book_id = ?"
            try:
                cursor = conn.cursor()
                cursor.execute(sql102, [curr_book_id])
                rows = cursor.fetchall()
                for row in rows:
                    print("Book id        : ", row[0])
                    print("ISBN           : ", row[1])
                    print("Title          : ", row[2])
                    print("Enroll date    : ", row[3])
                    print("Author         : ", row[4])
                    print("Publisher      : ", row[5])
                    print("\n")
            except sqlite3.Error as e:
                print("An error occurred in SQL_001:", e.args[0])
        else:
            pass

else:
    print('z1serial not open')

# z1serial.close()  # close z1serial if z1serial is open.
