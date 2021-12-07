import os
import fitz

#all the directories
pdf_dir = "./EMNLP/PDF"
txt_dir = "./EMNLP/TXT"
xml_dir = "./EMNLP/XML"

#convert all the pdfs to txt using fitz
def convert_pdf_to_txt(pdf_dir, txt_dir):
    for pdf_file in os.listdir(pdf_dir):
        pdf_file = pdf_dir + "/" + pdf_file
        print(pdf_file)
        text = ''
        with fitz.open(pdf_file) as doc:
            for page in doc:
                text += page.getText()
        #save the text to a txt file
        txt_file = txt_dir + "/" + pdf_file.split("/")[-1].split(".")[0] + ".txt"
        print(txt_file)
        #save the text file with utf-8 encoding
        with open(txt_file, "w", encoding="utf-8") as f:
            f.write(text)


#save all the pdf files as a xml file with tag tree
def convert_pdf_to_xml(pdf_dir, xml_dir):
    for pdf_file in os.listdir(pdf_dir):
        
        pdf_file = pdf_dir + "/" + pdf_file
        text = ''
        with fitz.open(pdf_file) as doc:
            for page in doc:
                text += page.getText("xhtml")
        #save the text to a xml file
        xml_file = xml_dir + "/" + pdf_file.split("/")[-1].split(".")[0] + ".xml"
        with open(xml_file, "w", encoding="utf-8") as f:
            f.write(text)
        
        print("converting"+ pdf_file+ "to xml")


        
        

if __name__ == "__main__":
    convert_pdf_to_txt(pdf_dir, txt_dir)
    convert_pdf_to_xml(pdf_dir, xml_dir)

   

    