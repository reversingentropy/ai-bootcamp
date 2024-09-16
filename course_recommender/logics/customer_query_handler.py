# logics/customer_query_handler.py
import json
from helper_functions.llm import get_completion_by_messages

category_n_course_name = {
    'Programming and Development': ['Web Development Bootcamp',
                                     'Introduction to Cloud Computing',
                                     'Advanced Web Development',
                                     'Cloud Architecture Design'],
    'Data Science & AI': ['Data Science with Python',
                          'AI and Machine Learning for Beginners',
                          'Machine Learning with R',
                          'Deep Learning with TensorFlow'],
    'Marketing': ['Digital Marketing Masterclass',
                  'Social Media Marketing Strategy'],
    'Cybersecurity': ['Cybersecurity Fundamentals',
                      'Ethical Hacking for Beginners'],
    'Business and Management': ['Project Management Professional (PMP)® Certification Prep',
                                'Agile Project Management'],
    'Writing and Literature': ['Creative Writing Workshop',
                               'Advanced Creative Writing'],
    'Design': ['Graphic Design Essentials', 'UI/UX Design Fundamentals']
}

def identify_category_and_courses(user_message):
    delimiter = "####"

    system_message = f"""
    You will be provided with customer service queries. \
    The customer service query will be enclosed in
    the pair of {delimiter}.

    Decide if the query is relevant to any specific courses
    in the Python dictionary below, where each key is a `category`
    and the value is a list of `course_name`.

    If there are any relevant course(s) found, output the pair(s) of a) `course_name` and b) the associated `category` into a
    list of dictionary objects, where each item in the list is a relevant course
    and each course is a dictionary that contains two keys:
    1) category
    2) course_name

    {category_n_course_name}

    If there are no relevant courses found, output an empty list.

    Ensure your response contains only the list of dictionary objects or an empty list, \
    without any enclosing tags or delimiters.
    """

    messages = [
        {'role': 'system', 'content': system_message},
        {'role': 'user', 'content': f"{delimiter}{user_message}{delimiter}"},
    ]
    category_and_product_response_str = get_completion_by_messages(messages)
    category_and_product_response_str = category_and_product_response_str.replace("'", "\"")
    
    try:
        category_and_product_response = json.loads(category_and_product_response_str)
    except json.JSONDecodeError:
        print("Error decoding JSON response")
        category_and_product_response = []
    
    return category_and_product_response

# Load course data
filepath = './data/courses-full.json'

with open(filepath, 'r') as file:
    json_string = file.read()
    dict_of_courses = json.loads(json_string)

def get_course_details(list_of_category_n_course):
    course_names_list = [x.get('course_name') for x in list_of_category_n_course]
    list_of_course_details = [dict_of_courses.get(course_name) for course_name in course_names_list]
    return list_of_course_details

def generate_response_based_on_course_details(user_message, product_details):
    delimiter = "####"

    system_message = f"""
    Follow these steps to answer the customer queries.
    The customer query will be delimited with a pair {delimiter}.

    Step 1:{delimiter} If the user is asking about course, \
    understand the relevant course(s) from the following list.
    All available courses shown in the json data below:
    {product_details}

    Step 2:{delimiter} Use the information about the course to \
    generate the answer for the customer's query.
    You must only rely on the facts or information in the course information.
    Your response should be as detailed as possible and \
    include information that is useful for customer to better understand the course.

    Step 3:{delimiter}: Answer the customer in a friendly tone.
    Make sure the statements are factually accurate.
    Your response should be comprehensive and informative to help the \
    the customers to make their decision.
    Complete with details such as rating, pricing, and skills to be learned.
    Use Neural Linguistic Programming to construct your response.

    Use the following format:
    Step 1:{delimiter} <step 1 reasoning>
    Step 2:{delimiter} <step 2 reasoning>
    Step 3:{delimiter} <step 3 response to customer>

    Make sure to include {delimiter} to separate every step.
    """

    messages = [
        {'role': 'system', 'content': system_message},
        {'role': 'user', 'content': f"{delimiter}{user_message}{delimiter}"},
    ]

    response_to_customer = get_completion_by_messages(messages)
    response_to_customer = response_to_customer.split(delimiter)[-1]
    return response_to_customer

def process_user_message(user_input):
    category_n_course_name = identify_category_and_courses(user_input)
    print("category_n_course_name : ", category_n_course_name)

    course_details = get_course_details(category_n_course_name)

    reply = generate_response_based_on_course_details(user_input, course_details)

    return reply
