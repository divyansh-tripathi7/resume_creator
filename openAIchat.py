import openai
# import api 
import pprint
from dictFill import filled_resume

print("in open ai py")

def chat1(prompt):
    openai.api_key = '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'
    completions = openai.Completion.create(model = "text-davinci-003", prompt= prompt ,max_tokens=1000)
    message = completions.choices[0].text
    # print(completions)
    return message

filled_dict = pprint.pformat(filled_resume)
print("filled dictino**********************************")
print(filled_dict)
reqMssg = 'Please give a latex code to create resume for me from details provided in the dictionary above'

print(chat1(filled_dict))


print("in codeleaf banaying")

codeOverLeaf = chat1(reqMssg)
print(codeOverLeaf)

print("write pdftex")

with open('resume.tex' , 'w') as file:
    file.write(codeOverLeaf)

print("exit open ai py")
