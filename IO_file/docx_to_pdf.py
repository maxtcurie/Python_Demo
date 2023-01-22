import aspose.words as aw

doc = aw.Document("./Input/Input.docx")
doc.save("./Output/Output.pdf")