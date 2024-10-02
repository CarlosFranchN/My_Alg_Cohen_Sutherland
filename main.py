from Sutherland import Vetor
import flet as ft
import flet.canvas as cv
import math


def main(page: ft.Page):
    page.title = "Calculadora de Vetores"
    page.padding = 20
    
    
    VIEWPORT_SIZE = 300


    ponto1_x = ft.TextField(label="Ponto 1 - X", width=100)
    ponto1_y = ft.TextField(label="Ponto 1 - Y", width=100)


    ponto2_x = ft.TextField(label="Ponto 2 - X", width=100)
    ponto2_y = ft.TextField(label="Ponto 2 - Y", width=100)


    result_label = ft.Text(value="Resultado aparecerá aqui")


    canvas = cv.Canvas(
        width=VIEWPORT_SIZE,
        height=VIEWPORT_SIZE,
        shapes=[],  
    )

    def desenhar_vetor(ponto1, ponto2):

        canvas.shapes.clear()

        canvas.shapes.append(
            cv.Rect(
                x=0,
                y=0,
                width=VIEWPORT_SIZE,
                height=VIEWPORT_SIZE,
                paint=ft.Paint(
                    style=ft.PaintingStyle.STROKE,
                    stroke_width=2,
                    color=ft.colors.BLACK,
                )
            )
        )


        escala = VIEWPORT_SIZE / 50

        ponto1_canvas = (ponto1[0] * escala, VIEWPORT_SIZE - ponto1[1] * escala)
        ponto2_canvas = (ponto2[0] * escala, VIEWPORT_SIZE - ponto2[1] * escala)


        dx = ponto2_canvas[0] - ponto1_canvas[0]
        dy = ponto2_canvas[1] - ponto1_canvas[1]
        comprimento = math.sqrt(dx**2 + dy**2)
        
        if comprimento > 0:

            dx /= comprimento
            dy /= comprimento


            ponta_tamanho = 10
            ponta1_x = ponto2_canvas[0] - ponta_tamanho * (dx + dy)
            ponta1_y = ponto2_canvas[1] - ponta_tamanho * (dy - dx)
            ponta2_x = ponto2_canvas[0] - ponta_tamanho * (dx - dy)
            ponta2_y = ponto2_canvas[1] - ponta_tamanho * (dy + dx)


            canvas.shapes.append(
                cv.Line(
                    x1=ponto1_canvas[0],
                    y1=ponto1_canvas[1],
                    x2=ponto2_canvas[0],
                    y2=ponto2_canvas[1],
                    paint=ft.Paint(stroke_width=2, color=ft.colors.BLUE)
                )
            )


            canvas.shapes.append(
                cv.Path(
                    [
                        cv.Path.MoveTo(ponto2_canvas[0], ponto2_canvas[1]),
                        cv.Path.LineTo(ponta1_x, ponta1_y),
                        cv.Path.LineTo(ponta2_x, ponta2_y),
                        cv.Path.Close()
                    ],
                    paint=ft.Paint(style=ft.PaintingStyle.FILL, color=ft.colors.BLUE)
                )
            )


        for ponto in [ponto1_canvas, ponto2_canvas]:
            canvas.shapes.append(
                cv.Circle(
                    x=ponto[0],
                    y=ponto[1],
                    radius=3,
                    paint=ft.Paint(color=ft.colors.RED, style=ft.PaintingStyle.FILL)
                )
            )


        canvas.update()


    def calcular_vetor(e):
        try:

            ponto1 = (int(ponto1_x.value), int(ponto1_y.value))
            ponto2 = (int(ponto2_x.value), int(ponto2_y.value))


            vetor = Vetor(ponto1, ponto2)


            result_label.value = f"Vetor: {vetor.vetor}\nBits do vetor: {vetor.bits_vetor}\n{vetor.contido()}"


            desenhar_vetor(ponto1, ponto2)

        except ValueError:
            result_label.value = "Insira valores numéricos válidos para as coordenadas."


        page.update()

    calcular_button = ft.ElevatedButton(text="Calcular Vetor", on_click=calcular_vetor)


    page.add(
        ft.Row([ponto1_x, ponto1_y]),
        ft.Row([ponto2_x, ponto2_y]),
        calcular_button,
        result_label,
        ft.Text("Viewport (50x50)"),
        canvas,
    )


ft.app(target=main)