# Script para instalar Python, Git, GitHub Desktop e Visual Studio Code via winget e configurar PATH

# Função para adicionar um diretório ao PATH do sistema
function Add-ToPath {
    param (
        [string]$PathToAdd
    )
    $currentPath = [System.Environment]::GetEnvironmentVariable("PATH", [System.EnvironmentVariableTarget]::Machine)
    if (-not $currentPath.Split(';') -contains $PathToAdd) {
        [System.Environment]::SetEnvironmentVariable("PATH", "$currentPath;$PathToAdd", [System.EnvironmentVariableTarget]::Machine)
        Write-Output "Adicionado ao PATH: $PathToAdd"
    } else {
        Write-Output "O caminho já está no PATH: $PathToAdd"
    }
}

# Instalando Git
Write-Output "Instalando Git..."
winget install --id Git.Git -e

# Instalando GitHub Desktop
Write-Output "Instalando GitHub Desktop..."
winget install --id GitHub.GitHubDesktop -e

# Instalando Visual Studio Code
Write-Output "Instalando Visual Studio Code..."
winget install --id Microsoft.VisualStudioCode -e


# Instalando Python
Write-Output "Instalando Python..."
winget install --id Python.Python.3.11 -e


# Espera para garantir que os programas sejam instalados
Start-Sleep -Seconds 10

# Adicionando os diretórios dos executáveis ao PATH
# Nota: As versões e locais de instalação podem variar, ajuste se necessário
Write-Output "Configurando variáveis de ambiente..."


# Git
$gitPath = "${env:PROGRAMFILES}\Git\bin"
Add-ToPath $gitPath

# GitHub Desktop
$githubDesktopPath = "${env:LOCALAPPDATA}\GitHubDesktop\GitHubDesktop.exe"
Add-ToPath $githubDesktopPath

# Visual Studio Code
$vsCodePath = "${env:LOCALAPPDATA}\Programs\Microsoft VS Code\bin"
Add-ToPath $vsCodePath

# Python
$pythonPath = "${env:LOCALAPPDATA}\Programs\Python\Python311"
Add-ToPath $pythonPath


Write-Output "Instalação e configuração concluídas!"
