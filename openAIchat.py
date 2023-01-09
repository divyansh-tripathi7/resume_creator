import openai
import api 
import pprint
from dictFill import *

def chat1(prompt):
    openai.api_key = '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'
    completions = openai.Completion.create(model = "text-davinci-003", prompt= prompt ,max_tokens=1000)
    message = completions.choices[0].text
    # print(completions)
    return message

filled_resume = fill_resume_dict()
# filled_resume = {'contact_info': {'name': 'Jane Doe',
#   'address': '123 Main Street, Anytown, USA',
#   'phone': '123-456-7890',
#   'email': 'jane.doe@gmail.com',
#   'github': 'jane-doe',
#   'linkedin': 'jane-doe',
#   'gmail': 'jane.doe@gmail.com'},
#  'summary': 'Motivated and detail-oriented software engineer with 5 years of experience in full-stack development. Skilled in Python, JavaScript, and Java. Experience with agile development methodologies and a strong passion for delivering high-quality products.',
#  'work_experience': [{'job_title': 'Software Engineer',
#    'company': 'ACME Corp',
#    'dates': 'January 2018 - Present',
#    'responsibilities': ['Developed and maintained a web application using Python, Django, and PostgreSQL', 'Implemented new features and functionality using JavaScript and React', 'Collaborated with cross-functional teams to plan and deliver projects on time and on budget'],
#    'achievements': ['Spearheaded the development of a new feature that increased user engagement by 30%', 'Refactored legacy code, improving application performance by 15%']}],
#  'education': [{'degree': 'Bachelor of Science in Computer Science', 'school': 'University of Technology', 'dates': 'September 2014 - June 2018'}],
#  'projects': [{'name': 'Personal Blog', 'description': 'A blog platform built with Python, Flask, and MySQL. Implements user authentication and authorization, and allows users to create and publish their own posts.', 'url': 'https://github.com/jane-doe/personal-blog'},
#              {'name': 'Online Marketplace', 'description': 'A platform for buying and selling handmade and vintage items. Built with Ruby on Rails and PostgreSQL. Implements Stripe integration for handling payments.', 'url': 'https://github.com/jane-doe/online-marketplace'}],
#  'achievements': ['Received the Outstanding Graduate Award at University of Technology', 'Presented a research paper at the International Conference on Computer Science'],
#  'certifications': [{'name': 'Certified ScrumMaster', 'authority': 'Scrum Alliance', 'date': 'August 2020'}],
#  'skills': ['Python', 'JavaScript', 'Java', 'Django', 'React', 'Flask', 'Ruby on Rails', 'MySQL', 'PostgreSQL', 'Agile development'],
#  'additional_info': ['Fluent in English and Spanish', 'Experience working remotely']}

# list parameters daalo 

filled_dict = pprint.pformat(filled_resume)



reqMssg = 'Please create an overleaf resume for me from details provided in the dictionary above'


print(chat1(filled_dict))

# print(chat1(reqMssg))

codeOverLeaf = chat1(reqMssg)
print(codeOverLeaf)


