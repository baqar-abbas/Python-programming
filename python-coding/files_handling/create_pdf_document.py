from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Create a PDF canvas
pdf = canvas.Canvas("my_pdf_document.pdf", pagesize=letter)

# Title
pdf.setTitle("My First PDF")
pdf.setFont("Helvetica-Bold", 20)
pdf.drawString(100, 750, "My First PDF Document")

# Content
pdf.setFont("Helvetica", 12)
pdf.drawString(100, 700, "Hello from Python!")
pdf.drawString(100, 680, "This PDF was created using the reportlab library.")
pdf.drawString(100, 660, "You can create real PDF files with Python.")

# Save the PDF
pdf.save()

print("PDF document created: my_pdf_document.pdf")