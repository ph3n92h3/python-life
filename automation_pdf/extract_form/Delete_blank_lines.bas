Attribute VB_Name = "Ä£¿é1"
Sub Delete_blank_lines()
For Each ws In Sheets
    ws.Range("A1").EntireColumn.Delete
    
    lngFirstRow = ws.UsedRange.Row
    lngLastRow = lngFirstRow + ws.UsedRange.Rows.Count - 1
    For a = lngLastRow To lngFirstRow Step -1
        If Application.WorksheetFunction.CountA(ws.Rows(a)) = 0 Then
            ws.Rows(a).Delete
        End If
    Next
Next
End Sub
