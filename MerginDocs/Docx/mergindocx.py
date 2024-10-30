from docx import Document
import os

def merge_documents(documents, output_file):
    # Cria um novo documento para a mesclagem
    merged_document = Document()

    for document in documents:
        if os.path.exists(document):  # Verifica se o documento existe
            # Carrega o documento
            sub_document = Document(document)
            
            # Adiciona o conteúdo do documento ao documento mesclado
            for element in sub_document.element.body:
                merged_document.element.body.append(element)
        else:
            print(f"Arquivo não encontrado: {document}")
    
    # Salva o documento mesclado
    merged_document.save(output_file)
    print(f'Mesclado em: {output_file}')

# Exemplo de uso
if __name__ == "__main__":
    # Caminho dos arquivos
	#base_path = r"H:\Meu Drive\Doc´s\XLS\Processos Seletivos\ATUAIS - a partir de 09-08-23\JUNHO-24 - Depois\FUNCAMP\1232024\Questões"
    base_path = r"C:\Docs\Docx"

    # Lista dos documentos que você deseja mesclar
    documents = [
        os.path.join(base_path, '1-Perguntas_Arquitetura_Computadores.docx'),
        os.path.join(base_path, '2-Perguntas_Backup_Recuperacao_Dados.docx'),
        os.path.join(base_path, '3-Redes_Perguntas_Respostas.docx'),
        os.path.join(base_path, '4-Comandos_Linux_DOS.docx'),
        os.path.join(base_path, '5-Configuracao_Redes_Cabeadas_Sem_Fio.docx'),
        os.path.join(base_path, '6-Instalacao_e_Configuracao_de_Access_Pointse_Perifericos.docx'),
        os.path.join(base_path, '7-Manutencao_de_Computadores_e_Configuracao_do_Setup_BIOS.docx'),
        os.path.join(base_path, '8-Diagnstico_de_Conectividade_e_Problemas_de_Computadores.docx'),
        os.path.join(base_path, '9-Seguranca_de_Redes_e_Sistemas_Operacionais_Windows_e_Linux.docx'),
        os.path.join(base_path, '10-Instalacao_de_Softwares_e_Pacotes_no_Windows.docx')
    ]
    
    # Nome do arquivo de saída
    output_file = os.path.join(base_path, 'documento_mesclado.docx')
    
    merge_documents(documents, output_file)
