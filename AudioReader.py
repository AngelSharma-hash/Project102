import pyttsx3,PyPDF2

#Replace file.pdf' with path to your PDF file (i.e. /Desktop/Contracts/file.pdf)

pdfreader = PyPDF2.PdfReader(open(r'C:\Users\Angel Sharma\Downloads\Classroom of the Elite_ Year 2 Vol. 5.pdf','rb'))

reader = pyttsx3.init()
total_pages = len(pdfreader .pages)

for page in range(0,total_pages):   

    text = pdfreader.getPage(page).extractText()

    legible_text = text.strip().replace('\n',' ')

    print(legible_text)

    reader.say(legible_text)

    reader.save_to_file(legible_text,'file.mp3')

    reader.runAndWait()

reader.stop()