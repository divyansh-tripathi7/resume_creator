from openAIchat import codeOverLeaf

with open('resume.tex' , 'w') as file:
    file.write(codeOverLeaf)

print("enter pdftex")

from latex import build_pdf
f = open("./resume.tex", "rt")
data = f.read()
pdf = build_pdf(data)
pdf.save_to("./resume.pdf")

print("exit pdftex")
