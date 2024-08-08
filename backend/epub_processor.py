from ebooklib import epub
from bs4 import BeautifulSoup

def extract_text_by_chapter(file_path):
    """
    Extract text from each chapter of the EPUB file.
    """
    book = epub.read_epub(file_path)
    chapters = []
    for item in book.get_items_of_type(epub.EpubHtml):
        soup = BeautifulSoup(item.get_body_content(), 'html.parser')
        text = soup.get_text()
        chapters.append(text)
    return chapters

def split_text(text, max_length=5000):
    """
    Split text into chunks not exceeding max_length characters.
    """
    sentences = text.split('. ')
    chunks = []
    current_chunk = ""
    
    for sentence in sentences:
        if len(current_chunk) + len(sentence) + 1 <= max_length:
            current_chunk += sentence + ". "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + ". "
    
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks

def process_epub(file_path):
    """
    Process the EPUB file: extract chapters and split them into manageable chunks.
    """
    chapters = extract_text_by_chapter(file_path)
    all_chunks = []
    for chapter in chapters:
        chunks = split_text(chapter)
        all_chunks.extend(chunks)
    return all_chunks

if __name__ == "__main__":
    file_path = "path_to_your_epub_file.epub"
    chunks = process_epub(file_path)
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1}: {chunk[:100]}...")  # Print the first 100 characters of each chunk
