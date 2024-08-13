import mysql.connector


def get_student_total_fees(student_name, semester):
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="gamepro@123",
            database="bowen_ai_db"
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Prepare the SQL query
        query = "SELECT total_fees FROM fees WHERE student_name = %s AND semester = %s"

        # Execute the SQL query with the provided parameters
        cursor.execute(query, (student_name, semester))

        # Fetch the result
        result = cursor.fetchone()

        # Check if the result is not empty
        if result:
            total_fees = result[0]  # Fetching the first column value
            return total_fees
        else:
            # If no matching record found, return None
            return None

    except mysql.connector.Error as error:
        print("Error while fetching data from database:", error)
        return None

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()


# Example usage:
student_name = "peter pandey"
semester = 1
total_fees = int(get_student_total_fees(student_name, semester))
if total_fees is not None:
    print(f"Total fees for {student_name} in semester {semester} is {total_fees} naira")
else:
    print(f"No information found for {student_name} in semester {semester}.")


def get_pending_fees(student_name, semester):
    connection = None
    cursor = None
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="gamepro@123",
            database="bowen_ai_db"
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Prepare the SQL query
        query = "SELECT pending FROM fees WHERE student_name = %s AND semester = %s"

        # Execute the SQL query with the provided parameters
        cursor.execute(query, (student_name, semester))

        # Fetch the result
        result = cursor.fetchone()

        # Check if the result is not empty
        if result:
            pending_fees = result[0]
            return pending_fees
        else:
            # If no matching record found, return None
            return None

    except mysql.connector.Error as error:
        print("Error while fetching data from database:", error)
        return None

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()


# Example usage:
student_name = "bill gates"
semester = 2
pending_fees = int(get_pending_fees(student_name, semester))
if pending_fees is not None:
    print(f"Pending fees for {student_name} in semester {semester} is {pending_fees} naira")
elif pending_fees == 0.00:
    print(f"Pending fees for {student_name} in semester {semester} is {pending_fees} naira")
else:
    print(f"No information found for {student_name} in semester {semester}.")


def get_paid_fees(student_name, semester):
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="gamepro@123",
            database="bowen_ai_db"
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Prepare the SQL query
        query = "SELECT paid FROM fees WHERE student_name = %s AND semester = %s"

        # Execute the SQL query with the provided parameters
        cursor.execute(query, (student_name, semester))

        # Fetch the result
        result = cursor.fetchone()

        # Check if the result is not empty
        if result:
            paid_fees = result[0]
            return paid_fees

        else:
            # If no matching record found, return None
            return None

    except mysql.connector.Error as error:
        print("Error while fetching data from database:", error)
        return None

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()


# Example usage:
student_name = "peter pandey"
semester = 1
paid_info = int(get_paid_fees(student_name, semester))
if paid_info is not None:
    print(f"{student_name} has paid {paid_info} naira for semester {semester}")
elif paid_info == 0.00:
    print(f"{student_name} has paid {paid_info} naira for semester {semester}")
else:
    print("No information found for the student.")


def get_pending_students(semester):
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="gamepro@123",
            database="bowen_ai_db"
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Prepare the SQL query to select students with pending fees for the given semester
        query = "SELECT student_name FROM fees WHERE semester = %s AND pending > 0"

        # Execute the SQL query with the provided semester parameter
        cursor.execute(query, (semester,))

        # Fetch all the results
        pending_students = cursor.fetchall()

        # Return the list of pending students
        return [student[0] for student in pending_students]

    except mysql.connector.Error as error:
        print("Error while fetching data from database:", error)
        return []

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()


# Example usage:
semester = 2
pending_students = get_pending_students(semester)
if pending_students:
    print(f"Students with pending fees for semester {semester} are:")
    for student in pending_students:
        print(student)
else:
    print("No students found with pending fees for the specified semester.")


def get_paid_students(semester):
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="gamepro@123",
            database="bowen_ai_db"
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Prepare the SQL query to retrieve students who have fully paid their fees for the specified semester
        query = "SELECT student_name FROM fees WHERE semester = %s AND pending = 0"

        # Execute the SQL query with the provided semester
        cursor.execute(query, (semester,))

        # Fetch all the results
        students_paid_fees = cursor.fetchall()

        # Return the list of students who have fully paid their fees for the specified semester
        return [student[0] for student in students_paid_fees]

    except mysql.connector.Error as error:
        print("Error while fetching data from database:", error)
        return []

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()


# Example usage:
semester = 2
fully_paid_students = get_paid_students(semester)
if fully_paid_students:
    print("Students who have fully paid their fees for semester", semester, ":")
    for student in fully_paid_students:
        print(student)
else:
    print("No student have fully paid their fees for semester", semester)


def get_pending_sum(semester):
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="gamepro@123",
            database="bowen_ai_db"
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Prepare the SQL query to get the sum of pending fees for the given semester
        query = "SELECT SUM(pending) FROM fees WHERE semester = %s"

        # Execute the SQL query with the provided semester
        cursor.execute(query, (semester,))

        # Fetch the result
        result = cursor.fetchone()[0]

        # Check if the result is not empty
        if result is not None:
            return result
        else:
            # If no matching record found, return 0
            return 0

    except mysql.connector.Error as error:
        print("Error while fetching data from database:", error)
        return None

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()


# Example usage:
semester = 1
pending_sum = int(get_pending_sum(semester))
if pending_sum is not None:
    print(f"Sum of pending fees for semester {semester} is {pending_sum} naira")
else:
    print("Error: Unable to retrieve pending sum.")


def get_student_gpa(student_name, semester):
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="gamepro@123",
            database="bowen_ai_db"
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Prepare the SQL query to get the GPA for the given student and semester
        query = "SELECT gpa FROM marks WHERE student_name = %s AND semester = %s"

        # Execute the SQL query with the provided student name and semester
        cursor.execute(query, (student_name, semester))

        # Fetch the result
        result = cursor.fetchone()

        # Check if the result is not empty
        if result is not None:
            return result[0]  # Return the GPA
        else:
            # If no matching record found, return None
            return None

    except mysql.connector.Error as error:
        print("Error while fetching data from database:", error)
        return None

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()


# Example usage:
student_name = "peter pandey"
semester = 1
gpa = get_student_gpa(student_name, semester)
if gpa is not None:
    print(f"{student_name}'s GPA for semester {semester} is {gpa}")
else:
    print(f"No GPA information found for {student_name} in semester {semester}.")


def get_highest_gpa(semester):
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="gamepro@123",
            database="bowen_ai_db"
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Call the stored procedure
        cursor.callproc('GetMaxGPAForSemester', [semester])

        # Fetch the result
        result = None
        for res in cursor.stored_results():
            result = res.fetchone()

        # Check if the result is not empty
        if result is not None:
            student_name, gpa = result
            return student_name, gpa
        else:
            # If no matching record found, return None
            return None, None

    except mysql.connector.Error as error:
        print("Error while fetching data from database:", error)
        return None, None

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()


# Example usage:
semester = 1
student_name, gpa = get_highest_gpa(semester)
name = student_name[0:50]
if student_name is not None and gpa is not None:
    print(f"The student with the highest GPA for {semester} is {name} with a GPA of {gpa}.")
else:
    print(f"No information found for {semester} or database error occurred.")


def get_student_with_lowest_gpa(semester):
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="gamepro@123",
            database="bowen_ai_db"
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Call the stored procedure
        cursor.callproc('GetStudentWithLowestGPA', [semester])

        # Fetch the result
        for result in cursor.stored_results():
            data = result.fetchone()
            if data:
                student_name, gpa = data
                return student_name, gpa
            else:
                return None, None

    except mysql.connector.Error as error:
        print("Error while fetching data from database:", error)
        return None, None

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()


# Example usage:
semester = 1
student_name, gpa = get_student_with_lowest_gpa(semester)
if student_name is not None and gpa is not None:
    print(f"The student with the lowest GPA for {semester} is {student_name} with a GPA of {gpa}.")
else:
    print(f"No information found for {semester} or database error occurred.")


def get_average_gpa(semester):
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="gamepro@123",
            database="bowen_ai_db"
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Prepare the SQL query to get the average GPA for the given semester
        query = "SELECT AVG(gpa) FROM marks WHERE semester = %s"

        # Execute the SQL query with the provided semester
        cursor.execute(query, (semester,))

        # Fetch the result
        result = cursor.fetchone()[0]

        # Check if the result is not empty
        if result is not None:
            return result
        else:
            # If no matching record found, return 0
            return 0

    except mysql.connector.Error as error:
        print("Error while fetching data from database:", error)
        return None

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()


# Example usage:
semester = 1
average_gpa = f"{get_average_gpa(semester):.2f}"
if average_gpa is not None:
    print(f"Average GPA for {semester}: {average_gpa}")
else:
    print("Error: Unable to retrieve average GPA.")


def get_admin_posts():
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="gamepro@123",
            database="bowen_ai_db"
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Prepare the SQL query to get all posts and their corresponding names
        query = "SELECT post, name FROM administration"

        # Execute the SQL query
        cursor.execute(query)

        # Fetch all the results
        results = cursor.fetchall()

        # Format the results as a string
        response = ""
        for post, name in results:
            response += f" (({post}))  ===>> {name}"

        return response.strip()

    except mysql.connector.Error as error:
        print("Error while fetching data from database:", error)
        return None

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()


# Example usage:
admin_posts = get_admin_posts()
if admin_posts:
    print("Executives Posts:")
    print(admin_posts)
else:
    print("Error: Unable to retrieve administrator posts.")


def get_exco_posts():
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="gamepro@123",
            database="bowen_ai_db"
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Prepare the SQL query to get all posts and their corresponding names
        query = "SELECT post, name FROM excos"

        # Execute the SQL query
        cursor.execute(query)

        # Fetch all the results
        results = cursor.fetchall()

        # Format the results as a string
        response = ""
        for post, name in results:
            response += f" (({post}))  ===>> {name}"

        return response.strip()

    except mysql.connector.Error as error:
        print("Error while fetching data from database:", error)
        return None

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()


# Example usage:
exco_posts = get_exco_posts()
if exco_posts:
    print("Administrator Posts:")
    print(exco_posts)
else:
    print("Error: Unable to retrieve administrator posts.")


def get_exco_info(post):
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="gamepro@123",
            database="bowen_ai_db"
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Prepare the SQL query to get the name and number for the given post
        query = "SELECT name, number FROM excos WHERE post = %s"

        # Execute the SQL query with the provided post
        cursor.execute(query, (post,))

        # Fetch the result
        result = cursor.fetchone()

        # Check if the result is not empty
        if result:
            name, number = result
            return f"Name: {name}, Phone Number: 0{number}"
        else:
            # If no matching record found, return a message indicating so
            return "No information found for the given post."

    except mysql.connector.Error as error:
        print("Error while fetching data from database:", error)
        return "Error: Unable to retrieve information."

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()


# Example usage:
post = "public relations officer"
exco_info = get_exco_info(post)
print(exco_info)


def get_punishment_info(offence):
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="gamepro@123",
            database="bowen_ai_db"
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Prepare the SQL query to get the name and number for the given post
        query = "SELECT punishment FROM conduct WHERE offence = %s"

        # Execute the SQL query with the provided post
        cursor.execute(query, (offence,))

        # Fetch the result
        result = cursor.fetchone()

        # Check if the result is not empty
        if result:
            punishment = result
            punishment_string = punishment[0]
            return f"the punishment is {punishment_string}"
        else:
            # If no matching record found, return a message indicating so
            return "No information found for the given offence."

    except mysql.connector.Error as error:
        print("Error while fetching data from database:", error)
        return "Error: Unable to retrieve information."

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()


# Example usage:
offence = "improper dressing"
punishment_info = get_punishment_info(offence)
print(punishment_info)


def get_courses_and_colleges():
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="gamepro@123",
            database="bowen_ai_db"
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Prepare the SQL query to get all courses and their respective colleges and acronyms
        query = "SELECT courses, college, college_acrn FROM degree"

        # Execute the SQL query
        cursor.execute(query)

        # Fetch all the results
        results = cursor.fetchall()

        # Construct the response string
        response = []
        for row in results:
            course, college, college_acrn = row
            response.append(f"{course}, {college}({college_acrn}) ----- ")

        # Join the list into a single string
        response_string = "\n".join(response)
        return response_string

    except mysql.connector.Error as error:
        print("Error while fetching data from database:", error)
        return None

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()


# Example usage:
courses_and_colleges = get_courses_and_colleges()
if courses_and_colleges:
    print("Courses and Colleges:")
    print(courses_and_colleges)
else:
    print("Error: Unable to retrieve courses and colleges.")


def get_provost(college_acrn):
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="gamepro@123",
            database="bowen_ai_db"
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Prepare the SQL query to get the provost for the given college_acrn
        query = "SELECT provost FROM degree WHERE college_acrn = %s"

        # Execute the SQL query with the provided college_acrn
        cursor.execute(query, (college_acrn,))

        # Fetch the result
        result = cursor.fetchone()

        # Check if the result is not empty
        if result:
            provost = result[0]
            return provost
        else:
            # If no matching record found, return a message
            return "No provost found for the given college acronym."

    except mysql.connector.Error as error:
        print("Error while fetching data from database:", error)
        return "An error occurred while retrieving the provost."

    finally:
        # Close the cursor and connection
        if cursor:# cursor.close()
            if connection:
                connection.close()


# Example usage:
college_acrn = "COCCS"
provost = get_provost(college_acrn)
print(f"The provost for the college, {college_acrn} is {provost}")
