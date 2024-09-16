const uploadArea = document.getElementById('upload-area');
const fileInput = document.getElementById('file-input');
const output = document.getElementById('output');
const originalImageDiv = document.getElementById('original-image');
const processedImageDiv = document.getElementById('processed-image');
const downloadBtn = document.getElementById('download-btn');

// Evento de clique para abrir o explorador de arquivos
uploadArea.addEventListener('click', () => {
    fileInput.click();
});

// Evento de drag and drop
uploadArea.addEventListener('dragover', (event) => {
    event.preventDefault();
    uploadArea.style.backgroundColor = "#81c784";
});

uploadArea.addEventListener('dragleave', () => {
    uploadArea.style.backgroundColor = "#a5d6a7";
});

uploadArea.addEventListener('drop', (event) => {
    event.preventDefault();
    uploadArea.style.backgroundColor = "#a5d6a7";
    const file = event.dataTransfer.files[0];
    handleFileUpload(file);
});

// Evento de seleção de arquivo
fileInput.addEventListener('change', (event) => {
    const file = event.target.files[0];
    handleFileUpload(file);
});

// Função para enviar a imagem ao backend e exibir imagens
function handleFileUpload(file) {
    if (!file) return;

    const reader = new FileReader();
    reader.onload = function (e) {
        originalImageDiv.innerHTML = `<h2>Imagem Original</h2><img src="${e.target.result}" alt="Imagem Original">`;
    };
    reader.readAsDataURL(file);  // Carregar a imagem original

    const formData = new FormData();
    formData.append('image', file);

    // Enviar imagem para o backend
    fetch('/remove-bg', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        const contentType = response.headers.get("Content-Type");  // Obter o tipo de conteúdo (imagem)
        return response.blob().then(blob => ({ blob, contentType }));
    })
    .then(({ blob, contentType }) => {
        // Criar a URL da imagem retornada pelo backend
        const imgURL = URL.createObjectURL(blob);
        processedImageDiv.innerHTML = `<h2>Imagem Processada</h2><img src="${imgURL}" alt="Imagem com fundo removido">`;

        // Preparar o botão de download com o tipo de conteúdo correto
        downloadBtn.href = imgURL;  // URL da imagem para download
        const extension = contentType.split("/")[1];  // Pegar a extensão do arquivo (png, jpeg, etc.)
        downloadBtn.download = `imagem-processada.${extension}`;  // Definir o nome do arquivo com a extensão correta
        downloadBtn.style.display = 'inline';  // Mostrar o botão de download
    })
    .catch(error => {
        output.innerHTML = `<p style="color: red;">Erro ao remover o fundo: ${error}</p>`;
    });
}
