Attribute VB_Name = "Module111"
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

Sub AllStockAnalysisRefactored()
    
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
    Dim totalvolume(11) As Long
    Dim starting_price(11) As Single
    Dim closing_price(11) As Single
    Dim tickerindex As Integer
    
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
    tickerindex = 0
    'Sort Data by ticker and date
    
    Range("A1:H" & rowend).Sort Key1:=Range("A1"), Key2:=Range("B1"), Order1:=xlAscending, Order2:=xlAscending, Header:=xlYes
        
    'set volumes to 0
            For k = 0 To 11
                totalvolume(k) = 0
            Next k
    
    'start for loop cycling through all rows
    
            For i = rowstart To rowend
            
    'increase total volume if equal to ticker
                
                If Cells(i, 1).Value = ticker(tickerindex) Then
                    totalvolume(tickerindex) = totalvolume(tickerindex) + Cells(i, 8).Value
                End If
                
    'set starting price
                
                If Cells(i, 1).Value = ticker(tickerindex) And Cells(i - 1, 1).Value <> ticker(tickerindex) Then
                    starting_price(tickerindex) = Cells(i, 6).Value
                End If
                
    'set closing price
                    
                If Cells(i, 1) = ticker(tickerindex) And Cells(i + 1, 1) <> ticker(tickerindex) Then
                    closing_price(tickerindex) = Cells(i, 6).Value
                End If
                
    'increase ticker if at the end of its grouping
    
                If Cells(i, 1) = ticker(tickerindex) And Cells(i + 1, 1) <> ticker(tickerindex) Then
                    tickerindex = tickerindex + 1
                End If
                
            Next i
            
    'output ticker values
            
          Worksheets("All_Stock_Analysis").Activate
    
    'input data into table from arrays
    
    Cells(4, 1).Value = ticker(0)
    Cells(4, 2).Value = totalvolume(0)
    Cells(4, 3).Value = (closing_price(0) / starting_price(0)) - 1
    Cells(5, 1).Value = ticker(1)
    Cells(5, 2).Value = totalvolume(1)
    Cells(5, 3).Value = (closing_price(1) / starting_price(1)) - 1
    Cells(6, 1).Value = ticker(2)
    Cells(6, 2).Value = totalvolume(2)
    Cells(6, 3).Value = (closing_price(2) / starting_price(2)) - 1
    Cells(7, 1).Value = ticker(3)
    Cells(7, 2).Value = totalvolume(3)
    Cells(7, 3).Value = (closing_price(3) / starting_price(3)) - 1
    Cells(8, 1).Value = ticker(4)
    Cells(8, 2).Value = totalvolume(4)
    Cells(8, 3).Value = (closing_price(4) / starting_price(4)) - 1
    Cells(9, 1).Value = ticker(5)
    Cells(9, 2).Value = totalvolume(5)
    Cells(9, 3).Value = (closing_price(5) / starting_price(5)) - 1
    Cells(10, 1).Value = ticker(6)
    Cells(10, 2).Value = totalvolume(6)
    Cells(10, 3).Value = (closing_price(6) / starting_price(6)) - 1
    Cells(11, 1).Value = ticker(7)
    Cells(11, 2).Value = totalvolume(7)
    Cells(11, 3).Value = (closing_price(7) / starting_price(7)) - 1
    Cells(12, 1).Value = ticker(8)
    Cells(12, 2).Value = totalvolume(8)
    Cells(12, 3).Value = (closing_price(8) / starting_price(8)) - 1
    Cells(13, 1).Value = ticker(9)
    Cells(13, 2).Value = totalvolume(9)
    Cells(13, 3).Value = (closing_price(9) / starting_price(9)) - 1
    Cells(14, 1).Value = ticker(10)
    Cells(14, 2).Value = totalvolume(10)
    Cells(14, 3).Value = (closing_price(10) / starting_price(10)) - 1
    Cells(15, 1).Value = ticker(11)
    Cells(15, 2).Value = totalvolume(11)
    Cells(15, 3).Value = (closing_price(11) / starting_price(11)) - 1
    'Format Ticker return output
    
    For Each Cell In Range("C4:C15")
    
        If Cell.Value > 0.75 Then
            Cell.Interior.Color = RGB(0, 128, 0)
        ElseIf Cell.Value > 0.5 Then
            Cell.Interior.Color = RGB(50, 205, 50)
        ElseIf Cell.Value > 0.25 Then
            Cell.Interior.Color = RGB(0, 255, 0)
        ElseIf Cell.Value > 0 Then
            Cell.Interior.Color = RGB(152, 251, 152)
        ElseIf Cell.Value < -0.75 Then
            Cell.Interior.Color = RGB(230, 0, 0)
        ElseIf Cell.Value < -0.5 Then
            Cell.Interior.Color = RGB(255, 91, 91)
        ElseIf Cell.Value < -0.25 Then
            Cell.Interior.Color = RGB(255, 137, 137)
        ElseIf Cell.Value < 0 Then
            Cell.Interior.Color = RGB(255, 201, 201)
        Else
            Cell.Interior.Color = xlNone
                
        End If
        
    Next Cell
    
    'format data post-output
    
    Range("B3:B15").NumberFormat = "#,##0"
    Range("C3:C15").NumberFormat = "0.0%"
    Columns("A:C").AutoFit
    
    timerend = Timer
    
    MsgBox ("This refactored code ran for " & (timerend - timerstart) & " seconds for the " & yearValue & " analysis")
        
End Sub

Sub ClearWorksheet()

    Worksheets("All_Stock_Analysis").Activate
    Range("A:C").Clear
    Range("A:C").Interior.Color = xlNone
    
    
End Sub
