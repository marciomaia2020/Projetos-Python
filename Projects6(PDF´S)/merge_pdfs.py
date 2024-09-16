import os
from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output_pdf):
    # Cria o diretório de saída se não existir
    output_dir = os.path.dirname(output_pdf)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    merger = PdfMerger()

    for pdf in pdf_list:
        merger.append(pdf)
    
    merger.write(output_pdf)
    merger.close()

# Lista de arquivos PDF que você deseja mesclar
pdf_files = [
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Ambientes_Virtuais_no_Python.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Aplicacao_de_Integracao_de_APIs_com_Flask.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Ambientes_Virtuais_no_Python.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Aplicacao_de_Integracao_de_APIs_com_Flask.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Apostila_do_Desenvolvedor_Python.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\conceiosDeMSQL.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\conceitoDeDicionarios.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\conceitosDeEntradaSaida.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\conceitosDeFuncoes.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\conceitosDeInsercaoDadosMSQL.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\conceitosDeListas.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\conceitosDeMatplotlib.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\conceitosDeModulos.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\conceitosDeSaida.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\conceitosDeSets.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\conceitosDeStrings.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\conceitosDeTuplas.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\conceitosDeVariaveis.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\conceitosGlossarios.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Conceitos_Avancados_em_Python.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Conceitos_Avançados_em_Python.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Conceitos_Basicos_de_Python.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Conceitos_de_Classes_em_Python.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Conceitos_de_POO_em_Python.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Cronograma_de_Estudo.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\downloadArquivosNet.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Exemplos_de_Caminho_de_Arquivoscem_Python.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Exemplos_de_Caminho_de_Arquivos_em_Python.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Exemplo_de_requirements.txt_e_Explicacao_sobre_railway.json.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Extensoes_Populares_do_Flask.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Extracao_de_Dados_com_Python.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Extracao_de_Dados_em_Python.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Funcoes_Especiais_em_Python.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\guia_extracao_de_dados_python.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Lista_de_Dependencias_Python.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Macetes_em_Python.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Manipulacao_de_Planilhas_Excel_e_HTML_com_Python.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Mapa_do_Python.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\menipulacaoDeArquivos.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Principais_Provedores_de_Hospedagem_para_Python.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Problemas_Resolvidos_em_Python.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\provedoresPython.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Python_Project_Structure.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\python_project_structure_with_explanation.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Recursos_para_Aprender_e _raticar_Python.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\recusrosAprenderPraticarPython.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\requirementsxrailway.json.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Resumo_de_Assuntos_Avancados_em_Desenvolvimento_Web_com_Python_Codigos.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Resumo_de_Assuntos_Avançados_em_Desenvolvimento_Webcom_Python_Explicacao.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Resumo_de_Assuntos_Avançados_em_Desenvolvimento_Web_com_Python.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Sites_para_Deployment.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\termosFundamentais.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\tutorial_manipulacao_python.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Apostila_de_Python.pdf',
    r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\separados\Atribuicao_de_Multiplos_Valores.pdf',


]

# Nome do arquivo de saída
output_pdf = r'D:\MEUSSITESEPROJETOS\Sites\portifolioDoMaia\docs\python\pdf\merged\documento_unificado.pdf'

# Mesclar os PDFs
merge_pdfs(pdf_files, output_pdf)

print(f'PDFs mesclados com sucesso em {output_pdf}')
