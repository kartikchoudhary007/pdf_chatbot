import fitz  # PyMuPDF
import os

def pdf_to_markdown(pdf_path, markdown_path):
    doc = fitz.open(pdf_path)

    markdown_content = ""

    for page_number in range(doc.page_count):
        page = doc[page_number]
        text = page.get_text("text")
        markdown_content += f"# Page {page_number + 1}\n\n{text}\n\n"

    doc.close()

    with open(markdown_path, "w", encoding="utf-8") as markdown_file:
        markdown_file.write(markdown_content)

    return markdown_content  # Added this line to return content

if __name__ == "__main__":
    pdf_path = "data/48lawsofpower.pdf"
    markdown_path = "text.md"

    pdf_to_markdown(pdf_path, markdown_path)
