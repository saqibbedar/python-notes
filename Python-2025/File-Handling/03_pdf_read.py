import os
import PyPDF2

def read_pdf(pdf_path):
    # Create a PDF file object
    with open(pdf_path, 'rb') as file:
        # Create PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Get number of pages
        num_pages = len(pdf_reader.pages)
        
        # Initialize string to store text
        text = ""
        
        # Extract text from each page
        for page_num in range(num_pages):
            # Get page object
            page = pdf_reader.pages[page_num]
            # Extract text from page
            text += page.extract_text()
            
        return text

# Example usage
pdf_path = os.path.join(".", "example.pdf")
try:
    content = read_pdf(pdf_path)
    
    # Save extracted text to file
    output_dir = os.path.join(".", "00_generated_files")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    with open(os.path.join(output_dir, "pdf_content.txt"), "w", encoding="utf-8") as file:
        file.write(content)
        
except FileNotFoundError:
    print(f"PDF file not found at: {pdf_path}")
except Exception as e:
    print(f"An error occurred: {str(e)}")