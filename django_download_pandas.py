def pandas2response(df):
    sio = BytesIO()
    sheetname = "test"
    PandasWriter = pandas.ExcelWriter(
        sio, engine='xlsxwriter', options={'remove_timezone': True})
    df.to_excel(PandasWriter, sheet_name=sheetname)
    PandasWriter.save()
    sio.seek(0)
    response = HttpResponse(
        sio.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    # set up  file datetime
    filename = datetime.now().strftime("%Y-%m-%d-%H-%M")
    response['Content-Disposition'] = 'attachment; filename={filename}.xlsx'.format(
        filename=filename)
    return response

