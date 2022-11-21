
# Práctica 1 - Bloque 4
# Lara Ocón Madrid - 202115710

from xhtml2pdf import pisa

def convert_html_to_pdf(source_html, output_filename):
    # open output file for writing (truncated binary)
    result_file = open(output_filename, "w+b")

    # convert HTML to PDF
    pisa_status = pisa.CreatePDF(
        source_html,                # the HTML to convert
        dest=result_file)           # file handle to recieve result

    # close output file
    result_file.close()                 # close output file

    # return True on success and False on errors
    return pisa_status.err


if __name__ == "__main__":

    # creamos el html
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Reporte ejecutivo</title>
    </head>
    <body>
        <h1>Práctica 1 Bloque 4 - Adquisición de Datos</h1>
        <h2>Lara Ocón Madrid - 202115710</h2>
        <h3>Reporte ejecutivo pizzería "Maven Pizzas"</h3>
        <p>Este es un reporte ejecutivo de la pizzería Maven Pizzas</p>
        <p>El reporte contiene información sobre las ventas de la pizzería, las pizzas pedidas por semana, los ingredientes necesitados a la semana, la predicción de ingredientes propuesto para la semana, y la comparación entre dicha predicción y los ingredientes finalmente necesitados.</p>
        <p>En primer lugar, mostramos la predicción propuesta de ingredientes necesitados a la semana. Para calcular dicha predicción, hemos calculado la cantidad utilizada de cada ingrediente para cada semana y hemos calculado la media de todas las semanas. Después, hemos multiplicado la media para cada ingrediente por 1.2, factor que hemos elegido para evitar que pueda llegar a haber escasez de un ingrdiente una semana concreta.</p>
        <p>A continuación se muestra la predicción de ingredientes propuesta:</p>
        <img src="imagenes/prediccion_ingredientes.png" alt="Predicción de ingredientes">
        <div style="page-break-after: always;"></div>
        <p>A continuación se muestra la comparación entre la predicción de ingredientes y los ingredientes finalmente necesitados:</p>
        <img src="imagenes/diferencia_prediccion_realidad_ingredientes.png" alt="Comparación de ingredientes">
        <p>Vease el caso del ingrediente "Garlic", el mas usado en la pizzería, la diferencia entre la cantidad necesaria propuesta y la cantidad que se ha necesitado de dicho ingrediente en la pizzería a lo largo de las semanas.</p>
        <img src="imagenes/diferencia_prediccion_realidad_Garlic.png" alt="Comparación de Garlic">
        <div style="page-break-after: always;"></div>
        <p>A continuación se muestran las ganancias para cada semana del año:</p>
        <img src="imagenes/ganancias_semana.png" alt="Ganancias por semana">
        <p>Vease también las ganancias por mes:</p>
        <img src="imagenes/ganancias_mes.png" alt="Ganancias por mes">
        <div style="page-break-after: always;"></div>
    </body>
    </html>
    """

    # pasamos el html a pdf
    convert_html_to_pdf(html, "reporte_ejecutivo.pdf")
