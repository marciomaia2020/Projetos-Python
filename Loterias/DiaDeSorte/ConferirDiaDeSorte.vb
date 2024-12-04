Sub Conferir()
    ' Definir as planilhas
    Dim wsTestes As Worksheet
    Dim wsDiaDeSorte As Worksheet
    Dim numero As Variant
    Dim listaSuspensa As Range
    Dim valor As Range

    Set wsTestes = ThisWorkbook.Sheets("Testes")
    Set wsDiaDeSorte = ThisWorkbook.Sheets("DIA DE SORTE")

    ' Solicitar ao usuário para inserir o número
    numero = Application.InputBox("Digite o número para iniciar a conferência:", "Iniciar Conferência", Type:=1)

    ' Verificar se o usuário cancelou a caixa de diálogo ou não inseriu um número
    If numero = False Then
        MsgBox "Você não inseriu um número. A conferência foi cancelada.", vbExclamation
        Exit Sub
    End If
    
    ' Chama a macro InserirMesNaColunaI_ para o mês
    'MsgBox "Chamando a macro para inserir o mês"
    InserirMesNaColunaI_
    
    MsgBox "A macro só será executada quando o valor de A1 for 1 - POR FAVOR - Selecione o valor 1 na lista suspensa.", vbExclamation

	
        'MsgBox "Chamando a macro AcumularValores_"
        AcumularValores_
        'MsgBox "Chamando a macro SomarValoresSeA1MaiorQue2_"
        'SomarValoresSeA1MaiorQue2_

    ' Definir a lista suspensa na coluna A da planilha DIA DE SORTE a partir da célula A2
    Set listaSuspensa = wsDiaDeSorte.Range("A2", wsDiaDeSorte.Cells(wsDiaDeSorte.Rows.Count, "A").End(xlUp))

    ' Iniciar a conferência a partir do número digitado pelo usuário
    For Each valor In listaSuspensa
        ' Verifica se o valor atual é maior ou igual ao número informado
        If valor.Value >= numero Then
            ' Debug para verificar o valor
            Debug.Print "Valor atual da lista suspensa: " & valor.Value

            ' Atualiza a célula A1 da planilha Testes com o valor atual
            wsTestes.Range("A1").Value = valor.Value
            Debug.Print "Valor atualizado na célula A1: " & wsTestes.Range("A1").Value

            ' Aguardar 1 segundo antes de avançar para o próximo item
            Application.Wait Now + TimeValue("00:00:01")
            DoEvents ' Permite que o Excel processe outros eventos
            
            
            'MsgBox "Chamando a macro AcumularValores_"
            'AcumularValores_
            'MsgBox "Chamando a macro SomarValoresSeA1MaiorQue2_"
            SomarValoresSeA1MaiorQue2_
            
            
            
            
        End If
    Next valor

    ' Mensagem de conclusão da conferência
    MsgBox "A conferência foi concluída!", vbInformation
End Sub

Sub TransferirDados_()
    Dim wsTestes As Worksheet
    Dim intervaloOrigem As Range
    Dim ultimaColuna As Long
    Dim proximaColuna As Long

    ' Definir as planilhas
    Set wsTestes = ThisWorkbook.Sheets("Testes")

    ' Definir o intervalo de origem
    Set intervaloOrigem = wsTestes.Range("J4:J1048575")


    ' Definir a próxima coluna vazia
    proximaColuna = ultimaColuna + 1


    'MsgBox "Valores copiados com sucesso!", vbInformation
End Sub

Sub InserirMesNaColunaI_()
    Dim ws As Worksheet
    Dim valorEscolhido As Integer
    Dim lastRow As Long
    Dim i As Long
    Dim rng As Range
    Dim valores() As Variant
    
    ' Definir a planilha "Testes"
    Set ws = ThisWorkbook.Sheets("Testes")
    
    ' Solicitar que o usuário escolha um número de 1 a 12
    valorEscolhido = Application.InputBox("Escolha um número entre 1 e 12:", Type:=1)
    
    ' Verificar se o valor está dentro do intervalo permitido
    If valorEscolhido < 1 Or valorEscolhido > 12 Then
        MsgBox "Por favor, escolha um número entre 1 e 12.", vbExclamation
        Exit Sub
    End If
    
    ' Definir a última linha para o intervalo (I4 até a última linha)
    lastRow = 1048576
    
    ' Definir o intervalo de I4 até I1048576
    Set rng = ws.Range("I4:I" & lastRow)
    
    ' Criar uma matriz para preencher a coluna rapidamente
    ReDim valores(1 To lastRow - 3, 1 To 1)
    
    ' Preencher a matriz com o valor escolhido
    For i = 1 To lastRow - 3
        valores(i, 1) = valorEscolhido
    Next i
    
    ' Inserir a matriz no intervalo de uma só vez
    rng.Value = valores
    
    'MsgBox "O valor " & valorEscolhido & " foi inserido na coluna I rapidamente.", vbInformation
End Sub

Sub AcumularValores_()
    Dim wsTestes As Worksheet
    Dim rngTestes As Range
    Dim arrJ As Variant
    Dim arrN As Variant
    Dim i As Long

    ' Definir a planilha "Testes"
    Set wsTestes = ThisWorkbook.Sheets("Testes")

    ' Verificar se o valor de A1 é 1
    If wsTestes.Range("A1").Value <> 1 Then
        MsgBox "A macro só será executada quando o valor de A1 for 1 - POR FAVOR - Selecione o valor 1 na lista suspensa.", vbExclamation
        Exit Sub
    End If

    ' Desativar a atualização da tela e o cálculo automático para aumentar a performance
    Application.ScreenUpdating = False
    Application.Calculation = xlCalculationManual

    ' Definir o intervalo a ser monitorado na coluna J
    Set rngTestes = wsTestes.Range("J4:J1048575")

    ' Copiar os valores da coluna J para um array
    arrJ = rngTestes.Value

    ' Limpar o intervalo N4:N1048575
    wsTestes.Range("N4:N1048575").ClearContents

    ' Copiar os valores de J para N (usando array)
    wsTestes.Range("N4:N1048575").Value = arrJ

    ' Reativar a atualização da tela e o cálculo automático
    Application.ScreenUpdating = True
    Application.Calculation = xlCalculationAutomatic

    ' Notificação de sucesso
    'MsgBox "Valores copiados para N com sucesso!", vbInformation
End Sub

Sub SomarValoresSeA1MaiorQue2_()
    Dim wsTestes As Worksheet
    Dim rngTestes As Range
    Dim arrJ As Variant
    Dim arrN As Variant
    Dim i As Long

    ' Definir a planilha "Testes"
    Set wsTestes = ThisWorkbook.Sheets("Testes")

    ' Verificar se o valor de A1 é maior ou igual a 2
    If wsTestes.Range("A1").Value >= 2 Then
        ' Desativar a atualização da tela e o cálculo automático para aumentar a performance
        Application.ScreenUpdating = False
        Application.Calculation = xlCalculationManual

        ' Definir o intervalo a ser monitorado na coluna J
        Set rngTestes = wsTestes.Range("J4:J1048575")

        ' Copiar os valores de J e N para arrays
        arrJ = rngTestes.Value
        arrN = wsTestes.Range("N4:N1048575").Value

        ' Percorrer os arrays para somar os valores
        For i = 1 To UBound(arrJ, 1)
            If Not IsEmpty(arrJ(i, 1)) Then
                arrN(i, 1) = arrN(i, 1) + arrJ(i, 1)
            End If
        Next i

        ' Copiar o array de volta para a coluna N
        wsTestes.Range("N4:N1048575").Value = arrN

        ' Reativar a atualização da tela e o cálculo automático
        Application.ScreenUpdating = True
        Application.Calculation = xlCalculationAutomatic

        'MsgBox "Valores somados com sucesso!", vbInformation
    Else
        'MsgBox "O valor em A1 precisa ser maior que 2 para a soma ser realizada.", vbExclamation
    End If
End Sub



