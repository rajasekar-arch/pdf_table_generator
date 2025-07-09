from pdf_table_generator import TablePDF

headers = ["Stage", "Topic", "Goals", "Tools"]
data = [
    ["1", "Programming", "Automation", "Python, Git"],
    ["2", "Databases", "Querying", "PostgreSQL, MongoDB"],
    ["3", "Cloud", "Scalability", "AWS, Azure"],
]
col_widths = [15, 40, 60, 75]

pdf = TablePDF(
    title="Data Engineer Roadmap (2025 Edition)",
    font_family="Arial",
    header_font_size=16,
    section_font_size=12,
    body_font_size=9
)

pdf.section_title("Learning Path")
pdf.draw_table(headers, data, col_widths)
pdf.save_pdf("custom_roadmap.pdf")
