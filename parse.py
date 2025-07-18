import fitz  # PyMuPDF
import os

# Path where your PDFs are downloaded
pdf_folder = r"D:\AvishkarAI\PDFs"

# Output folder to save extracted text
output_folder = os.path.join(pdf_folder, "parsed_text")
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(pdf_folder):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, filename)
        doc = fitz.open(pdf_path)

        print(f"Extracting from: {filename}")
        full_text = ""

        for page in doc:
            full_text += page.get_text()

        # Save to .txt file
        txt_filename = filename.replace(".pdf", ".txt")
        with open(os.path.join(output_folder, txt_filename), "w", encoding="utf-8") as f:
            f.write(full_text)

        doc.close()
