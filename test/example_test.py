import os
from pdf_table_generator import TablePDF  # Adjust if your file is named differently

def test_pdf_generation():
    # Sample table data
    headers = ["Stage", "Topic", "Goals", "Tools"]
    data = [
        ["1", "Programming", "Automation", "Python, Git"],
        ["2", "Databases", "Querying", "PostgreSQL, MongoDB"],
        ["3", "Cloud", "Scalability", "AWS, Azure"],
    ]
    col_widths = [15, 40, 60, 75]

    # Output file
    filename = "test_output.pdf"

    # Create PDF
    pdf = TablePDF(
        title="Test PDF Generation",
        font_family="Arial",
        header_font_size=14,
        section_font_size=12,
        body_font_size=9
    )

    pdf.section_title("Testing Table Section")
    pdf.draw_table(headers, data, col_widths)
    pdf.save_pdf(filename)

    # Validate file exists
    if os.path.exists(filename):
        print(f"Test passed: {filename} was created successfully.")
    else:
        print("Test failed: PDF file was not created.")

if __name__ == "__main__":
    test_pdf_generation()
