from pdf2image import convert_from_path

pages = convert_from_path('main.pdf', dpi=300)
for i, page in enumerate(pages):
    page.save(f'resume_page_{i+1}.jpg', 'JPEG', quality=90)