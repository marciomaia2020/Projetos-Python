// Função para permitir arrastar e soltar os arquivos
const dropArea = document.getElementById('drop-area');
const fileList = document.getElementById('file-list');
const mergeBtn = document.getElementById('merge-btn');
let files = [];

// Função para lidar com o evento de "arrastar e soltar"
dropArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropArea.style.backgroundColor = '#add8e6'; // Cor ao arrastar
});

dropArea.addEventListener('dragleave', () => {
    dropArea.style.backgroundColor = '#f0f8ff'; // Cor original
});

dropArea.addEventListener('drop', (e) => {
    e.preventDefault();
    dropArea.style.backgroundColor = '#f0f8ff'; // Cor original

    const droppedFiles = e.dataTransfer.files;
    
    for (let i = 0; i < droppedFiles.length; i++) {
        if (droppedFiles[i].type === 'application/pdf') {
            files.push(droppedFiles[i]);
            updateFileList();
        }
    }

    if (files.length > 0) {
        mergeBtn.disabled = false;
    }
});

// Função para exibir a lista de arquivos
function updateFileList() {
    fileList.innerHTML = '';
    files.forEach((file, index) => {
        const listItem = document.createElement('li');
        listItem.textContent = file.name;
        
        // Adicionando botão de excluir
        const deleteBtn = document.createElement('button');
        deleteBtn.textContent = 'Excluir';
        deleteBtn.onclick = () => removeFile(index);

        listItem.appendChild(deleteBtn);
        fileList.appendChild(listItem);
    });
}

// Função para remover arquivo da lista
function removeFile(index) {
    files.splice(index, 1);
    updateFileList();

    if (files.length === 0) {
        mergeBtn.disabled = true;
    }
}

// Função para enviar os arquivos e mesclar no servidor
mergeBtn.addEventListener('click', () => {
    if (files.length < 2) {
        alert('Selecione pelo menos 2 arquivos PDF para mesclar.');
        return;
    }

    const formData = new FormData();
    files.forEach((file) => {
        formData.append('pdf_files', file);
    });

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then((response) => response.blob())
    .then((blob) => {
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = 'merged.pdf';
        link.click();
    })
    .catch((error) => {
        console.error('Erro ao enviar os arquivos:', error);
    });
});
