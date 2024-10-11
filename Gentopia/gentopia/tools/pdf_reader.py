from typing import Any, Optional, Type
from PyPDF2 import PdfReader
from gentopia.tools.basetool import *
from transformers import pipeline  # For summarization

class PDFSummarizerArgs(BaseModel):
    file_path: str = Field(..., description="Path to the PDF file")

class PDFSummarizer(BaseTool):
    """Tool that reads and summarizes a PDF file."""

    name = "pdf_summarizer"
    description = ("Reads and summarizes a PDF file. Input should be the path to the PDF file.")

    args_schema: Optional[Type[BaseModel]] = PDFSummarizerArgs

    def _run(self, file_path: str) -> str:
        # Step 1: Read the PDF content
        text = self.read_pdf(file_path)

        # Step 2: Summarize the text using a summarization model
        summary = self.summarize_text(text)
        
        return summary

    def read_pdf(self, file_path: str) -> str:
        """Extracts text from a PDF file."""
        reader = PdfReader(file_path)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text

    def summarize_text(self, text: str) -> str:
        """Summarizes the extracted text using a language model."""
        # Using Huggingface's transformers pipeline for summarization
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

        # Split text into smaller chunks to avoid token limit errors
        max_chunk_size = 1000  # This can be adjusted based on the model's input size limit
        text_chunks = [text[i:i+max_chunk_size] for i in range(0, len(text), max_chunk_size)]

        summary = ""
        for chunk in text_chunks:
            summary_chunk = summarizer(chunk, max_length=150, min_length=50, do_sample=False)
            summary += summary_chunk[0]['summary_text'] + "\n\n"

        return summary

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError

if __name__ == "__main__":
    # Test the PDF summarizer
    summarizer = PDFSummarizer()
    summary = summarizer._run("path/to/your/pdf_file.pdf")  # Provide the path to the PDF file
    print(summary)

