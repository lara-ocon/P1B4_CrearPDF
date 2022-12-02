
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
   
        <div style="text-align:center">
            <br/>
            <h1 style="font-size: 40px; font-weight: bold;">Reporte ejecutivo</h1>
            <h2 style="font-size: 25px; font-weight: bold;">"Maven Pizzas"</h2>
            <img src="imagenes/log.png" alt="Comparación de ingredientes" width="600" height="600">
            <p style="font-size: 20px; font-weight: bold;">Autor: Lara Ocón Madrid </p>
    
        <div style="page-break-after: always;"></div>

        <div style="text-align:center">
            <br/>
            <h1 style="font-size: 40px; font-weight: bold;">Índice</h1>
            <br/>
            <p style="font-size: 20px; font-weight: bold;">1. Predicción Ingredientes</p>
            <p style="font-size: 20px; font-weight: bold;">2. Predicción vs Realidad</p>
            <p style="font-size: 20px; font-weight: bold;">3. Análisis de las ganancias</p>
       
        <div style="page-break-after: always;"></div>

        <div style="text-align:left">
            <h1 style="font-size: 30px; font-weight: bold;">1. Predicción de ingredientes</h1>
            <p>Este es un reporte ejecutivo de la pizzería Maven Pizzas</p>
            <p>El reporte contiene información sobre las ventas de la pizzería, las pizzas pedidas por semana, los ingredientes necesitados a la semana, la predicción de ingredientes propuesto para la semana, y la comparación entre dicha predicción y los ingredientes finalmente necesitados.</p>
            <p>En primer lugar, mostramos la predicción propuesta de ingredientes necesitados a la semana. Para calcular dicha predicción, hemos calculado la cantidad utilizada de cada ingrediente para cada semana y hemos calculado la media de todas las semanas. Después, hemos multiplicado la media para cada ingrediente por 1.2, factor que hemos elegido para evitar que pueda llegar a haber escasez de un ingrdiente una semana concreta.</p>
            <p>A continuación se muestra la predicción de ingredientes propuesta:</p>
            <img src="imagenes/prediccion_ingredientes.png" alt="Predicción de ingredientes">
        <div style="page-break-after: always;"></div>

        <div style="text-align:left">
            <p style="font-size: 15px; font-weight: bold;">2. Predicción  vs Realidad</p>
            <div style="text-align:center">
                <img src="imagenes/diferencia_prediccion_realidad_ingredientes.png" alt="Comparación de ingredientes" width="450" height="450">
            </div>
            <div style="text-align:left">
                <p>Vease el caso del ingrediente "Garlic", el mas usado en la pizzería, la diferencia entre la cantidad necesaria propuesta y la cantidad que se ha necesitado de dicho ingrediente en la pizzería a lo largo de las semanas.</p>
            </div>
            <div style="text-align:center">
                <img src="imagenes/diferencia_prediccion_realidad_Garlic.png" alt="Comparación de Garlic" width="450" height="450">
            </div>
        <div style="page-break-after: always;"></div>

        <div style="text-align:left">
            <p style="font-size: 15px; font-weight: bold;">3. Análisis de las ganancias</p>
            <div style="text-align:center">
                <img src="imagenes/ganancias_semana.png" alt="Ganancias por semana" width="500" height="500">
            </div>
            <div style="text-align:center">
                <img src="imagenes/ganancias_mes.png" alt="Ganancias por mes" width="500" height="500">
            </div>

    </body>

    </html>
    """

    # pasamos el html a pdf
    convert_html_to_pdf(html, "reporte_ejecutivo.pdf")
