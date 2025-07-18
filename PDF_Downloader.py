import arxiv
import os
import re

query = "deep learning transformers"
results = arxiv.Search(
    query=query,
    max_results=10,
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
