class Vetor:
    def __init__(self, ponto1, ponto2):
        self.vetor = [ponto1, ponto2]
        self.bits_vetor = []
        self.definir_bits()

    def bits_Sutherland(self, ponto):
        bits = [0, 0, 0, 0]
        if ponto[1] > 50:
            bits[0] = 1
        elif ponto[1] < 0:
            bits[1] = 1

        if ponto[0] > 50:
            bits[2] = 1
        elif ponto[0] < 0:
            bits[3] = 1

        return bits

    def definir_bits(self):
        for ponto in self.vetor:
            self.bits_vetor.append(self.bits_Sutherland(ponto))

    def in_viewport(self):
        VIEWPORT: list = [0, 0, 0, 0]
        saida = list(
            map(lambda ponto: True if ponto == VIEWPORT else False, self.bits_vetor)
        )
        return saida

    def contido(self):
        saida = self.in_viewport()
        if sum(saida) == 2:
            return f"O vetor {self.vetor} está Contido"
        elif sum(saida) == 1:
            return f"O vetor {self.vetor} está Parcialmente Contido"

        elif sum(saida) == 0:
            return f" O vetor {self.vetor} está Não Contido"


# a = [0,0]
# b = [0,0]
# print("Sabendo que a VIEWPORT tem o tamanho (50,50):")
# print("Digite as coordenadas dos pontos do vetor: ")
# a[0] = int(input("Digite a coordenada X do primeiro ponto: "))
# a[1] = int(input("Digite a coordenada Y do primeiro ponto: "))
# b[0] = int(input("Digite a coordenada X do segundo ponto: "))
# b[1] = int(input("Digite a coordenada Y do segundo ponto: "))

# vetor = Vetor(a,b)
# print(vetor.vetor)
# print(vetor.bits_vetor)
# print(vetor.in_viewport())
# print(vetor.contido())
import flet as ft
import flet.canvas as cv


def main(page: ft.Page):
    page.title = "Calculadora de Vetores"
    page.padding = 20
    
    # Tamanho do viewport (quadrado)
    VIEWPORT_SIZE = 300

    # Inputs para coordenadas do primeiro ponto
    ponto1_x = ft.TextField(label="Ponto 1 - X", width=100)
    ponto1_y = ft.TextField(label="Ponto 1 - Y", width=100)

    # Inputs para coordenadas do segundo ponto
    ponto2_x = ft.TextField(label="Ponto 2 - X", width=100)
    ponto2_y = ft.TextField(label="Ponto 2 - Y", width=100)

    # Label para mostrar o resultado
    result_label = ft.Text(value="Resultado aparecerá aqui")

    # Canvas para desenhar o viewport e o vetor
    canvas = cv.Canvas(
        width=VIEWPORT_SIZE,
        height=VIEWPORT_SIZE,
        content=cv.Gr,
    )

    def desenhar_vetor(ponto1, ponto2):
        # Limpa o canvas
        canvas.content.shapes.clear()

        # Desenha o quadrado representando o viewport
        canvas.content.shapes.append(
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

        # Converte as coordenadas dos pontos para a escala do canvas
        # Assumimos que o viewport vai de (0, 0) até (50, 50) (coordenadas do mundo)
        escala = VIEWPORT_SIZE / 50

        ponto1_canvas = (ponto1[0] * escala, VIEWPORT_SIZE - ponto1[1] * escala)
        ponto2_canvas = (ponto2[0] * escala, VIEWPORT_SIZE - ponto2[1] * escala)

        # Desenha a linha que representa o vetor
        canvas.content.shapes.append(
            cv.Line(
                x1=ponto1_canvas[0],
                y1=ponto1_canvas[1],
                x2=ponto2_canvas[0],
                y2=ponto2_canvas[1],
                paint=ft.Paint(
                    stroke_width=2,
                    color=ft.colors.BLUE,
                )
            )
        )

        # Atualiza o canvas
        canvas.update()

    # Função chamada ao clicar no botão
    def calcular_vetor(e):
        try:
            # Converte as entradas para inteiros
            ponto1 = (int(ponto1_x.value), int(ponto1_y.value))
            ponto2 = (int(ponto2_x.value), int(ponto2_y.value))

            # Cria o objeto Vetor e define os bits
            vetor = Vetor(ponto1, ponto2)

            # Mostra o vetor e bits calculados
            result_label.value = f"Vetor: {vetor.vetor}\nBits do vetor: {vetor.bits_vetor}\n{vetor.contido()}"

            # Chama a função para desenhar o vetor no canvas
            desenhar_vetor(ponto1, ponto2)

        except ValueError:
            result_label.value = "Insira valores numéricos válidos para as coordenadas."

        # Atualiza a página para exibir o resultado
        page.update()

    # Botão para calcular o vetor
    calcular_button = ft.ElevatedButton(text="Calcular Vetor", on_click=calcular_vetor)

    # Adiciona os widgets à página
    page.add(
        ft.Row([ponto1_x, ponto1_y]),
        ft.Row([ponto2_x, ponto2_y]),
        calcular_button,
        result_label,
        ft.Text("Viewport (50x50)"),
        canvas,
    )

# Executa o aplicativo
ft.app(target=main)