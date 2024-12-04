import os
import pdfkit
from PyPDF2 import PdfReader

def convert_html_to_pdf(html_file, pdf_file):
    if not os.path.exists(html_file):
        raise FileNotFoundError(f'Arquivo HTML não encontrado: {html_file}')
    
    path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # Ajuste o caminho conforme necessário
    config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
    
    pdfkit.from_file(html_file, pdf_file, configuration=config)

def count_pages(pdf_file):
    try:
        with open(pdf_file, 'rb') as f:
            reader = PdfReader(f)
            return len(reader.pages)
    except Exception as e:
        raise RuntimeError(f'Erro ao ler o arquivo PDF {pdf_file}: {e}')

# Listas de arquivos HTML e PDF
html_files = [
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\html\PrintYet\tutorial_manipulacao_python.html',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\html\PrintYet\Lista_de_Dependencias_Python.html',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\html\PrintYet\Extracao_de_Dados_em_Python.html',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\html\PrintYet\guia_extracao_de_dados_python.html',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\html\PrintYet\Conceitos_de_Classes_em_Python.html',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\html\PrintYet\python_project_structure_with_explanation.html',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\html\PrintYet\downloadArquivosNet.html',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\html\PrintYet\Exemplos_de_Caminho_de_Arquivos_em_Python.html',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\html\PrintYet\macetes_em_python.html',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\html\PrintYet\provedoresPython.html',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\html\PrintYet\requirementsxrailway.json.html',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\html\PrintYet\recusrosAprenderPraticarPython.html',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\html\PrintYet\Conceitos_Avançados_em_Python.html',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\html\PrintYet\conceitosDeStrings.html',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\html\PrintYet\conceitosDeListas.html',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\html\PrintYet\conceitoDeDicionarios.html',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\html\PrintYet\conceitosDeTuplas.html',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\html\PrintYet\conceitosDeSets.html',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\html\PrintYet\conceitosDeVariaveis.html',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\html\PrintYet\conceitosDeFuncoes.html',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\html\PrintYet\conceitosDeEntradaSaida.html',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\html\PrintYet\conceitosDeSaida.html',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\html\PrintYet\conceitosDeMatplotlib.html',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\html\PrintYet\conceitosDeModulos.html',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\html\PrintYet\manipulacaoDeArquivos.html',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\html\PrintYet\termosFuncamentais.html',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\html\PrintYet\conceiosDeMSQL.html',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\html\PrintYet\conceitosDeInsercaoDadosMSQL.html',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\html\PrintYet\conceitosGlossarios.html',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\html\PrintYet\apostila_de_paythonI.html',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\html\PrintYet\Atribuicao_de_Multiplos_Valores.html',
    # Adicione outros caminhos de arquivos HTML aqui
    
]

pdf_files = [
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\tutorial_manipulacao_python.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Lista_de_Dependencias_Python.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Extracao_de_Dados_em_Python.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\guia_extracao_de_dados_python.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Conceitos_de_Classes_em_Python.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\python_project_structure_with_explanation.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\downloadArquivosNet.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Exemplos_de_Caminho_de_Arquivos_em_Python.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\macetes_em_python.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\provedoresPython.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\requirementsxrailway.json.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\recusrosAprenderPraticarPython.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Conceitos_Avançados_em_Python.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\conceitosDeStrings.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\conceitosDeListas.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\conceitoDeDicionarios.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\conceitosDeTuplas.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\conceitosDeSets.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\conceitosDeVariaveis.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\conceitosDeFuncoes.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\conceitosDeEntradaSaida.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\conceitosDeSaida.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\conceitosDeMatplotlib.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\conceitosDeModulos.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\manipulacaoDeArquivos.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\termosFuncamentais.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\conceiosDeMSQL.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\conceitosDeInsercaoDadosMSQL.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\conceitosGlossarios.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\apostila_de_paythonI..pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Atribuicao_de_Multiplos_Valores.pdf',
    # Adicione outros caminhos de arquivos PDF aqui
    
]

# Verifique se as listas têm o mesmo comprimento
if len(html_files) != len(pdf_files):
    raise ValueError("As listas html_files e pdf_files devem ter o mesmo comprimento.")

for html_file, pdf_file in zip(html_files, pdf_files):
    try:
        convert_html_to_pdf(html_file, pdf_file)
        num_pages = count_pages(pdf_file)
        print(f'{pdf_file} tem {num_pages} páginas.')
    except Exception as e:
        print(f'Erro ao converter {html_file}: {e}')
