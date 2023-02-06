Attribute VB_Name = "Module11"
Sub Stock_Analysis()
    Worksheets("DQ Analysis").Activate
    Range("A1").Value = "DAQ0 (Ticker: DQ)"
    
    'Create Header Row
    
    Cells(3, 1).Value = "Year"
    Cells(3, 2).Value = "Total Daily Volume"
    Cells(3, 3).Value = "Return"
    
    'Set initial conditions data type
    
    Dim closing_price As Double
    Dim starting_price As Double
    Dim totalvolume As Long
    
    'Create initial conditions
    
    rowstart = 2
    rowend = Cells(Rows.Count, 1).End(xlDown).Row
    totalvolume = 0
    starting_price = 0
    closing_price = 0
    
    Worksheets("2018").Activate
    
    Range("A1:H" & rowend).Sort Key1:=Range("A1"), Key2:=Range("B1"), Order1:=xlAscending, Order2:=xlAscending, Header:=xlYes
    
    For i = rowstart To rowend
    
        'increase total volume if ticker is "DQ"
        
        If (Cells(i, 1).Value = "DQ") Then
            totalvolume = totalvolume + Cells(i, 8).Value
        End If
        
        'set starting price
        
        If Cells(i, 1).Value = "DQ" And Cells(i - 1, 1).Value <> "DQ" Then
            starting_price = Cells(i, 3).Value
        End If
        
        'set closing price
        
        If Cells(i, 1).Value <> "DQ" And Cells(i - 1, 1).Value = "DQ" Then
            closing_price = Cells(i, 6).Value
            
        End If
        
    Next i
    
    'MsgBox(totalvolume)
    
    Worksheets("DQ Analysis").Activate
    Cells(4, 1).Value = 2018
    Cells(4, 2).Value = totalvolume
    Cells(4, 3).Value = (closing_price / starting_price) - 1
    
End Sub

Sub AllStockAnalysis()
    
    'Initialize the worksheet and headers
    
    yearValue = InputBox("What year would you like the analysis to run?")
    
    Dim timerstart As Single
    Dim timerend As Single
    
    timerstart = Timer
    Worksheets("All_Stock_Analysis").Activate
    Range("A1").Value = "All Stocks" & " " & yearValue
    
    Cells(3, 1).Value = "Ticker"
    Cells(3, 2).Value = "Total Daily Volume"
    Cells(3, 3).Value = "Return"
    
    'input variables and data types
    
    Dim ticker(11) As String
    Dim rowend As Long
    Dim rowstart As Integer
    Dim arraystart As Integer
    Dim arrayend As Integer
    Dim totalvolume As Long
    Dim starting_price As Double
    Dim closing_price As Double
    
    ticker(0) = "AY"
    ticker(1) = "CSIQ"
    ticker(2) = "DQ"
    ticker(3) = "ENPH"
    ticker(4) = "FSLR"
    ticker(5) = "HASI"
    ticker(6) = "JKS"
    ticker(7) = "RUN"
    ticker(8) = "SEDG"
    ticker(9) = "SPWR"
    ticker(10) = "TERP"
    ticker(11) = "VSLR"
    
    Worksheets(yearValue).Activate
    
    rowstart = 2
    rowend = Cells(Rows.Count, 1).End(xlUp).Row
    arraystart = 0
    arrayend = 11
    
    'Sort Data by ticker and date
    
    Range("A1:H" & rowend).Sort Key1:=Range("A1"), Key2:=Range("B1"), Order1:=xlAscending, Order2:=xlAscending, Header:=xlYes
        
    'run through all tickers in array
        
        For j = arraystart To arrayend
        
    'reset for new ticker
            
            totalvolume = 0
            starting_price = 0
            closing_price = 0
            
            For i = rowstart To rowend
            
    'increase total volume if ticker is equal to ticker
                
                If Cells(i, 1).Value = ticker(j) Then
                    totalvolume = totalvolume + Cells(i, 8).Value
                End If
                
    'set starting price
                
                If Cells(i, 1).Value = ticker(j) And Cells(i - 1, 1).Value <> ticker(j) Then
                    starting_price = Cells(i, 6).Value
                End If
                
    'set closing price
                    
                If Cells(i, 1) = ticker(j) And Cells(i + 1, 1) <> ticker(j) Then
                    closing_price = Cells(i, 6).Value
                End If
            
            Next i
            
    'output ticker values
            
            Sheets("All_Stock_Analysis").Cells(4 + j, 1).Value = ticker(j)
            Sheets("All_Stock_Analysis").Cells(4 + j, 2).Value = totalvolume
            Sheets("All_Stock_Analysis").Cells(4 + j, 3).Value = (closing_price / starting_price) - 1
    
    'Format Ticker return output
    
            If Sheets("All_Stock_Analysis").Cells(4 + j, 3) > 0.75 Then
                Sheets("All_Stock_Analysis").Cells(4 + j, 3).Interior.Color = RGB(0, 128, 0)
            ElseIf Sheets("All_Stock_Analysis").Cells(4 + j, 3) > 0.5 Then
                Sheets("All_Stock_Analysis").Cells(4 + j, 3).Interior.Color = RGB(50, 205, 50)
            ElseIf Sheets("All_Stock_Analysis").Cells(4 + j, 3) > 0.25 Then
                Sheets("All_Stock_Analysis").Cells(4 + j, 3).Interior.Color = RGB(0, 255, 0)
            ElseIf Sheets("All_Stock_Analysis").Cells(4 + j, 3) > 0 Then
                Sheets("All_Stock_Analysis").Cells(4 + j, 3).Interior.Color = RGB(152, 251, 152)
            ElseIf Sheets("All_Stock_Analysis").Cells(4 + j, 3) < -0.75 Then
                Sheets("All_Stock_Analysis").Cells(4 + j, 3).Interior.Color = RGB(230, 0, 0)
            ElseIf Sheets("All_Stock_Analysis").Cells(4 + j, 3) < -0.5 Then
                Sheets("All_Stock_Analysis").Cells(4 + j, 3).Interior.Color = RGB(255, 91, 91)
            ElseIf Sheets("All_Stock_Analysis").Cells(4 + j, 3) < -0.25 Then
                Sheets("All_Stock_Analysis").Cells(4 + j, 3).Interior.Color = RGB(255, 137, 137)
            ElseIf Sheets("All_Stock_Analysis").Cells(4 + j, 3) < 0 Then
                Sheets("All_Stock_Analysis").Cells(4 + j, 3).Interior.Color = RGB(255, 201, 201)
            Else
                Sheets("All_Stock_Analysis").Cells(4 + j, 3).Interior.Color = xlNone
            
            End If
            
        Next j
        
    Worksheets("All_Stock_Analysis").Activate
    
    'format data post-output
    
    Range("B3:B15").NumberFormat = "#,##0"
    Range("C3:C15").NumberFormat = "0.0%"
    Columns("A:C").AutoFit
    
    timerend = Timer
    
    MsgBox ("This original code ran for " & (timerend - timerstart) & " seconds for the " & yearValue & " analysis")
        
End Sub

Sub ClearWorksheet()

    Worksheets("All_Stock_Analysis").Activate
    Range("A:C").Clear
    Range("A:C").Interior.Color = xlNone
    
    
End Sub
