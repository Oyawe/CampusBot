from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse

import db_helper

app = FastAPI()


@app.post("/")
async def handle_request(request: Request):
    # Retrieve the JSON data from the request
    payload = await request.json()

    # Extract the necessary information from the payload
    # Based on the structure of the WebhookRequest from DialogFlow
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']

    if intent == "get.total.fees":
        return get_fees(parameters)
    elif intent == "get.pending.fees":
        return get_pending_fees(parameters)
    elif intent == "get.paid.fees":
        return get_paid_fees(parameters)
    elif intent == "get.pending.students":
        return get_pending_students(parameters)
    elif intent == "get.paid.students":
        return get_paid_students(parameters)
    elif intent == "total.pending.fees":
        return get_total_pending_fees(parameters)
    elif intent == "get.student.gpa":
        return get_student_gpa(parameters)
    elif intent == "get.min.gpa":
        return get_min_gpa(parameters)
    elif intent == "get.max.gpa":
        return get_max_gpa(parameters)
    elif intent == "get.average.gpa":
        return get_avg_gpa(parameters)
    elif intent == "get.admin.and.governing.council":
        return get_admin(parameters)
    elif intent == "get.bbsf.executives":
        return get_excos(parameters)
    elif intent == "get.bbsf.individuals":
        return get_excos_post(parameters)
    elif intent == "get.punishment.info":
        return get_punishment_information(parameters)
    elif intent == "get.courses":
        return get_courses(parameters)
    elif intent == "get.provost":
        return get_provost(parameters)


def get_fees(parameters: dict):
    person = parameters["person"]["name"]
    semester = int(parameters["number"])
    fees = db_helper.get_student_total_fees(person, semester)

    if fees:
        fulfillment_text = f"The total fees for {person} in semester {semester} is {fees} naira"
    else:
        fulfillment_text = f"No information found for {person} in semester {semester}."

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })


def get_pending_fees(parameters: dict):
    person = parameters["person"]["name"]
    semester = int(parameters["number"])
    fees = db_helper.get_pending_fees(person, semester)

    if fees:
        fulfillment_text = f"{person} still has {fees} naira to balance up for semester {semester} fees"
    elif fees == 0.00:
        fulfillment_text = f"{person} has completed his school fees payment for semester {semester}"
    else:
        fulfillment_text = f"No information found for {person} in semester {semester}."

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })


def get_paid_fees(parameters: dict):
    person = parameters["person"]["name"]
    semester = int(parameters["number"])
    fees = db_helper.get_paid_fees(person, semester)

    if fees:
        fulfillment_text = f"{person} has paid {fees} naira for semester {semester}"
    elif fees == 0.00:
        fulfillment_text = f"{person} has paid nothing for semester {semester}"
    else:
        fulfillment_text = f"No information found for {person} in semester {semester}."

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })


def get_pending_students(parameters: dict):
    semester = int(parameters["number"])
    students = db_helper.get_pending_students(semester)

    if students:
        student_names = ", ".join(students)
        fulfillment_text = f"'{student_names}' are the students with pending fees for semester {semester}"
    else:
        fulfillment_text = f"No students found with pending fees for semester {semester}."

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })


def get_paid_students(parameters: dict):
    semester = int(parameters["number"])
    students = db_helper.get_paid_students(semester)

    if students:
        student_names = ", ".join(students)
        fulfillment_text = f"'{student_names}' has paid fully their fees for semester {semester}"
    else:
        fulfillment_text = f"No student have fully paid their fees for semester {semester}"

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })


def get_total_pending_fees(parameters: dict):
    semester = int(parameters["number"])
    fees = db_helper.get_pending_sum(semester)

    if fees:
        fulfillment_text = f"The total pending fees during semester {semester} is {fees} naira"
    else:
        fulfillment_text = "Error: Unable to retrieve pending sum."

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })


def get_student_gpa(parameters: dict):
    person = parameters["person"]["name"]
    semester = int(parameters["number"])
    gpa = db_helper.get_student_gpa(person, semester)

    if gpa:
        fulfillment_text = f"{person}'s GPA during semester {semester} is {gpa}"
    else:
        fulfillment_text = f"No GPA information found for {person} in semester {semester}."

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })


def get_min_gpa(parameters: dict):
    semester = int(parameters["number"])
    gpa = db_helper.get_student_with_lowest_gpa(semester)
    name = gpa[0]
    grade = gpa[1]

    if gpa:
        fulfillment_text = f"The lowest GPA during semester {semester} is {grade} which was attained by {name}."
    else:
        fulfillment_text = f"Error: Unable to retrieve minimum GPA for semester {semester}"

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })


def get_max_gpa(parameters: dict):
    semester = int(parameters["number"])
    gpa = db_helper.get_highest_gpa(semester)
    name = gpa[0]
    grade = gpa[1]

    if gpa:
        fulfillment_text = f"The highest GPA during semester {semester} is {grade} which was attained by {name}."
    else:
        fulfillment_text = f"Error: Unable to retrieve highest GPA for semester {semester}"

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })


def get_avg_gpa(parameters: dict):
    semester = int(parameters["number"])
    gpa = f"{db_helper.get_average_gpa(semester):.2f}"

    if gpa:
        fulfillment_text = f"The average GPA for semester {semester} is {gpa}"
    else:
        fulfillment_text = f"Error: Unable to retrieve average GPA for semester {semester}."

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })


def get_admin(parameters: dict):
    administrator = parameters["administrators"]
    admin_posts = db_helper.get_admin_posts()
    if admin_posts:
        fulfillment_text = f"These are the administrators:==>>  {admin_posts}"
    else:
        print("Error: Unable to retrieve administrator posts.")

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })


def get_excos(parameters: dict):
    bbsf = parameters["bbsf"]
    exco_posts = db_helper.get_exco_posts()
    if exco_posts:
        # fulfillment_text = "Administrator Posts:"
        fulfillment_text = f"These are the BBSF executives:==>>  {exco_posts}"
    else:
        print("Error: Unable to retrieve administrator posts.")

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })


def get_excos_post(parameters: dict):
    post = parameters["bbsfpost"]
    get_post = f"{db_helper.get_exco_info(post)}"

    if get_post:
        fulfillment_text = f"Here's information about the bbsf {post} --> {get_post}"
    else:
        fulfillment_text = "No information found for the given post."

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })


def get_punishment_information(parameters: dict):
    offence = parameters["offences"]
    get_punishment = f"{db_helper.get_punishment_info(offence)}"

    if get_punishment:
        fulfillment_text = f"For {offence} {get_punishment}"
    else:
        fulfillment_text = "No information found for the given offence"

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })


def get_courses(parameters: dict):
    courses = parameters["courses"]
    courses = db_helper.get_courses_and_colleges()
    if courses:
        fulfillment_text = f"These are the courses we offer with their respective colleges ==========>> {courses}"
    else:
        print("Error: Unable to retrieve courses and colleges.")

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })


def get_provost(parameters: dict):
    college = parameters["college"]
    college_upper = college.upper()
    provost = f"{db_helper.get_provost(college)}"

    if provost:
        fulfillment_text = f"The provost for the college, {college_upper} is {provost}"
    else:
        fulfillment_text = "No information found for the given college"

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })
