import pdfkit
from PyPDF2 import PdfReader

# Defina o caminho completo do seu arquivo HTML
html_file = r"D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\html\ambientes_virtuais_python.html"
# Defina o nome do arquivo PDF temporário
pdf_file = r"D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\html\output.pdf"

# Converter o arquivo HTML para PDF
pdfkit.from_file(html_file, pdf_file)

# Ler o PDF e contar as páginas
with open(pdf_file, "rb") as f:
    reader = PdfReader(f)
    num_pages = len(reader.pages)

print(f"O número de páginas no arquivo HTML é: {num_pages}")
