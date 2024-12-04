const uploadArea = document.getElementById('upload-area');
const fileInput = document.getElementById('file-input');
const originalImageDiv = document.getElementById('original-image');
const processedImageDiv = document.getElementById('processed-image');
const downloadBtn = document.getElementById('download-btn');

// Abrir explorador de arquivos ao clicar na área de upload
uploadArea.addEventListener('click', () => {
    fileInput.click();
});

// Mostrar pré-visualização da imagem original
fileInput.addEventListener('change', (event) => {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            originalImageDiv.innerHTML = `<h2>Imagem Original</h2><img src="${e.target.result}" alt="Imagem Original">`;
        };
        reader.readAsDataURL(file);

        const formData = new FormData();
        formData.append('image', file);

        // Enviar imagem para o backend
        fetch('/remove-bg', {
            method: 'POST',
            body: formData
        })
        .then(response => response.blob())
        .then(blob => {
            // Gerar o URL da imagem processada
            const imgURL = URL.createObjectURL(blob);
            processedImageDiv.innerHTML = `<h2>Imagem Processada</h2><img src="${imgURL}" alt="Imagem com fundo removido">`;
            downloadBtn.href = imgURL;
            downloadBtn.download = 'imagem-processada.jpg'; // Definindo o nome do arquivo como .jpg
            downloadBtn.style.display = 'inline'; // Exibir o botão de download
        })
        .catch(error => {
            processedImageDiv.innerHTML = `<p style="color: red;">Erro ao processar imagem: ${error}</p>`;
        });
    }
});
