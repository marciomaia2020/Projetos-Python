'Módulo III

'MACRO - FORMULAS
'InserirFormulasPontos
'B4 deve ter a fórmula =PROG_CARTELAS!A3
'B5 deve ter a fórmula =PROG_CARTELAS!A4
'B6 deve ter a fórmula =PROG_CARTELAS!A5
'---------------------
'InserirFormulaFrequencia
'C4 deve ter a fórmula =(B3/$K$1)*1
'C5 deve ter a fórmula =(B4/$K$1)*1
'C6 deve ter a fórmula =(B5/$K$1)*1
'---------------------
'InserirFormulaCOUNTIF1
'D4 deve ter a fórmula =COUNTIF(PROG_CARTELAS!B2:XFD2,1)
'D5 deve ter a fórmula =COUNTIF(PROG_CARTELAS!B3:XFD3,1)
'D6 deve ter a fórmula =COUNTIF(PROG_CARTELAS!B4:XFD4,1)
'---------------------
'InserirFormulaCOUNTIF2
'E4 terá =COUNTIF(PROG_CARTELAS!B2:XFD2,2),
'E5 terá =COUNTIF(PROG_CARTELAS!B3:XFD3,2)
'---------------------
'InserirFormulaCOUNTIF3
'F4 conterá =COUNTIF(PROG_CARTELAS!B2:XFD2,3)
'F5 conterá =COUNTIF(PROG_CARTELAS!B3:XFD3,3)
'---------------------
'InserirFormulaCOUNTIF4
'G4 conterá =COUNTIF(PROG_CARTELAS!B2:XFD2,4)
'G5 conterá =COUNTIF(PROG_CARTELAS!B3:XFD3,4)
'---------------------
'InserirFormulaCOUNTIF5
'H4 conterá =COUNTIF(PROG_CARTELAS!B2:XFD2,5)
'H5 conterá =COUNTIF(PROG_CARTELAS!B3:XFD3,5)
'---------------------
'InserirFormulaCOUNTIF6
'I4 conterá =COUNTIF(PROG_CARTELAS!B2:XFD2,6)
'I5 conterá =COUNTIF(PROG_CARTELAS!B3:XFD3,6)
'---------------------
'InserirFormulaCOUNTIF7
'J4 conterá =COUNTIF(PROG_CARTELAS!B1:XFD1,7)
'J5 conterá =COUNTIF(PROG_CARTELAS!B2:XFD2,7)
'---------------------

'InserirFormulasPontos
'InserirFormulaFrequencia
'InserirFormulaCOUNTIF1
'InserirFormulaCOUNTIF2
'InserirFormulaCOUNTIF3
'InserirFormulaCOUNTIF4
'InserirFormulaCOUNTIF5
'InserirFormulaCOUNTIF6
'InserirFormulaCOUNTIF7


Sub InserirFormulasPontos()
    Dim wsResultadoFinal As Worksheet
    Dim i As Long
    Dim ultimaLinha As Long

    ' Definir a planilha "RESULTADO FINAL"
    Set wsResultadoFinal = ThisWorkbook.Sheets("RESULTADO FINAL")

    ' Definir a última linha que deve ser preenchida com a fórmula
    ultimaLinha = 1048576 ' Última linha do Excel

    ' Inserir a fórmula a partir da célula B4 até a última linha
    For i = 4 To ultimaLinha
        wsResultadoFinal.Cells(i, 2).Formula = "=PROG_CARTELAS!A" & (i - 1)
    Next i
    
    'B4 deve ter a fórmula =PROG_CARTELAS!A3
    'B5 deve ter a fórmula =PROG_CARTELAS!A4
    'B6 deve ter a fórmula =PROG_CARTELAS!A5
End Sub

Sub InserirFormulaFrequencia()
    Dim wsResultadoFinal As Worksheet
    Dim i As Long
    Dim ultimaLinha As Long

    ' Definir a planilha "RESULTADO FINAL"
    Set wsResultadoFinal = ThisWorkbook.Sheets("RESULTADO FINAL")

    ' Definir a última linha que deve ser preenchida com a fórmula
    ultimaLinha = 1048576 ' Última linha do Excel

    ' Inserir a fórmula a partir da célula C4 até a última linha
    For i = 4 To ultimaLinha
        wsResultadoFinal.Cells(i, 3).Formula = "=(B" & (i - 1) & "/$K$1)*1"
    Next i
    
    'C4 deve ter a fórmula =(B3/$K$1)*1
    'C5 deve ter a fórmula =(B4/$K$1)*1
    'C6 deve ter a fórmula =(B5/$K$1)*1
End Sub
Sub InserirFormulaCOUNTIF1()
    Dim wsResultadoFinal As Worksheet
    Dim i As Long
    Dim ultimaLinha As Long

    ' Definir a planilha "RESULTADO FINAL"
    Set wsResultadoFinal = ThisWorkbook.Sheets("RESULTADO FINAL")

    ' Definir a última linha que deve ser preenchida com a fórmula
    ultimaLinha = 1048576 ' Última linha do Excel

    ' Inserir a fórmula a partir da célula D4 até a última linha
    For i = 4 To ultimaLinha
        wsResultadoFinal.Cells(i, 4).Formula = "=COUNTIF(PROG_CARTELAS!B" & (i - 2) & ":XFD" & (i - 2) & ",1)"
    Next i
	
	'D4 deve ter a fórmula =COUNTIF(PROG_CARTELAS!B2:XFD2,1)
	'D5 deve ter a fórmula =COUNTIF(PROG_CARTELAS!B3:XFD3,1)
	'D6 deve ter a fórmula =COUNTIF(PROG_CARTELAS!B4:XFD4,1)
End Sub
Sub InserirFormulaCOUNTIF2()
    Dim wsResultadoFinal As Worksheet
    Dim i As Long
    Dim ultimaLinha As Long

    ' Definir a planilha "RESULTADO FINAL"
    Set wsResultadoFinal = ThisWorkbook.Sheets("RESULTADO FINAL")

    ' Definir a última linha que deve ser preenchida com a fórmula (D1048576)
    ultimaLinha = 1048576

    ' Inserir a fórmula a partir da célula E4 até D1048576
    For i = 4 To ultimaLinha
        wsResultadoFinal.Cells(i, 5).Formula = "=COUNTIF(PROG_CARTELAS!B" & (i - 2) & ":XFD" & (i - 2) & ",2)"
    Next i
	'E4 terá =COUNTIF(PROG_CARTELAS!B2:XFD2,2),
	'E5 terá =COUNTIF(PROG_CARTELAS!B3:XFD3,2)
		
End Sub
Sub InserirFormulaCOUNTIF3()
    Dim wsResultadoFinal As Worksheet
    Dim i As Long
    Dim ultimaLinha As Long

    ' Definir a planilha "RESULTADO FINAL"
    Set wsResultadoFinal = ThisWorkbook.Sheets("RESULTADO FINAL")

    ' Definir a última linha que deve ser preenchida com a fórmula (F1048576)
    ultimaLinha = 1048576

    ' Inserir a fórmula a partir da célula F4 até F1048576
    For i = 4 To ultimaLinha
        wsResultadoFinal.Cells(i, 6).Formula = "=COUNTIF(PROG_CARTELAS!B" & (i - 2) & ":XFD" & (i - 2) & ",3)"
    Next i
	'F4 conterá =COUNTIF(PROG_CARTELAS!B2:XFD2,3)
	'F5 conterá =COUNTIF(PROG_CARTELAS!B3:XFD3,3)
End Sub

Sub InserirFormulaCOUNTIF4()
    Dim wsResultadoFinal As Worksheet
    Dim i As Long
    Dim ultimaLinha As Long

    ' Definir a planilha "RESULTADO FINAL"
    Set wsResultadoFinal = ThisWorkbook.Sheets("RESULTADO FINAL")

    ' Definir a última linha que deve ser preenchida com a fórmula (G1048576)
    ultimaLinha = 1048576

    ' Inserir a fórmula a partir da célula G4 até G1048576
    For i = 4 To ultimaLinha
        wsResultadoFinal.Cells(i, 7).Formula = "=COUNTIF(PROG_CARTELAS!B" & (i - 2) & ":XFD" & (i - 2) & ",4)"
    Next i
	'G4 conterá =COUNTIF(PROG_CARTELAS!B2:XFD2,4)
	'G5 conterá =COUNTIF(PROG_CARTELAS!B3:XFD3,4)
End Sub

Sub InserirFormulaCOUNTIF5()
    Dim wsResultadoFinal As Worksheet
    Dim i As Long
    Dim ultimaLinha As Long

    ' Definir a planilha "RESULTADO FINAL"
    Set wsResultadoFinal = ThisWorkbook.Sheets("RESULTADO FINAL")

    ' Definir a última linha que deve ser preenchida com a fórmula (H1048576)
    ultimaLinha = 1048576

    ' Inserir a fórmula a partir da célula H4 até H1048576
    For i = 4 To ultimaLinha
        wsResultadoFinal.Cells(i, 8).Formula = "=COUNTIF(PROG_CARTELAS!B" & (i - 2) & ":XFD" & (i - 2) & ",5)"
    Next i
	'H4 conterá =COUNTIF(PROG_CARTELAS!B2:XFD2,5)
	'H5 conterá =COUNTIF(PROG_CARTELAS!B3:XFD3,5)
	
End Sub
Sub InserirFormulaCOUNTIF6()
    Dim wsResultadoFinal As Worksheet
    Dim i As Long
    Dim ultimaLinha As Long

    ' Definir a planilha "RESULTADO FINAL"
    Set wsResultadoFinal = ThisWorkbook.Sheets("RESULTADO FINAL")

    ' Definir a última linha que deve ser preenchida com a fórmula (I1048576)
    ultimaLinha = 1048576

    ' Inserir a fórmula a partir da célula I4 até I1048576
    For i = 4 To ultimaLinha
        wsResultadoFinal.Cells(i, 9).Formula = "=COUNTIF(PROG_CARTELAS!B" & (i - 2) & ":XFD" & (i - 2) & ",6)"
    Next i
	'I4 conterá =COUNTIF(PROG_CARTELAS!B2:XFD2,6)
	'I5 conterá =COUNTIF(PROG_CARTELAS!B3:XFD3,6)
End Sub

Sub InserirFormulaCOUNTIF7()
    Dim wsResultadoFinal As Worksheet
    Dim i As Long
    Dim ultimaLinha As Long

    ' Definir a planilha "RESULTADO FINAL"
    Set wsResultadoFinal = ThisWorkbook.Sheets("RESULTADO FINAL")

    ' Definir a última linha que deve ser preenchida com a fórmula (J1048576)
    ultimaLinha = 1048576

    ' Inserir a fórmula a partir da célula J4 até J1048576
    For i = 4 To ultimaLinha
        wsResultadoFinal.Cells(i, 10).Formula = "=COUNTIF(PROG_CARTELAS!B" & (i - 3) & ":XFD" & (i - 3) & ",7)"
    Next i
	'J4 conterá =COUNTIF(PROG_CARTELAS!B1:XFD1,7)
	'J5 conterá =COUNTIF(PROG_CARTELAS!B2:XFD2,7)
End Sub
