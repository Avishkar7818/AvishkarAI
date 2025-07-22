import arxiv
import os
import re
import fitz  # PyMuPDF
import os

query = "deep learning transformers"
results = arxiv.Search(
    query=query,
    max_results=15,
    sort_by=arxiv.SortCriterion.Relevance
)

output_dir = r"D:\AvishkarAI\PDFs"
os.makedirs(output_dir, exist_ok=True)

def senitize_filename(title):
    return re.sub(r'[\\/*?:"<>|]', '', title)

for result in results.results():
    safe_title = senitize_filename(result.title)

    pdf_path = os.path.join(output_dir, f"{safe_title}.pdf")
    print(f"Downloading: {result.title}")
    result.download_pdf(filename=pdf_path)



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

