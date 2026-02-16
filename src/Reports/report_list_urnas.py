"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  07/01/2026
Comentarios:
    Crea el informe del listado de urnas.
"""
import datetime

from fpdf import FPDF, FPDFException, FontFace
from fpdf.enums import TableCellFillMode

from Model.DAO.urna_dao import UrnaDAO
from Services.Result.result import Result


class ReportListUrnasPDF(FPDF):
    def __init__(self, titulo: str):
        """ Constructor de clase """

        # Constructor base
        super().__init__(orientation="L", format="A4")

        # Inicializa las propiedades
        self._titulo = titulo
        self._data = self._get_data()
        self.set_auto_page_break(auto=True, margin=15)

    def footer(self):
        """ Genera el pie de página. """

        # Posiciona el cursor a 15 mm del borde inferior
        self.set_y(-10)

        # Estilo de encabezado
        footer_style = FontFace(emphasis="NONE", color=255,
                                fill_color=(2, 15, 158), family="Helvetica",
                                size_pt=10)

        # Creamos el pie de página
        with self.table(
                borders_layout="NONE",
                cell_fill_mode=TableCellFillMode.ROWS,
                # col_widths=(100, 100, 100),
                headings_style=footer_style,
                line_height=6,
                text_align=("LEFT", "CENTER", "RIGHT"),
                # width=287,
        ) as pie:
            row = pie.row()
            row.cell(datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))
            row.cell(self._titulo)
            row.cell(f"Page {self.page_no()}/{{nb}}")

    def build_body(self):
        """ Construye el cuerpo del reporte. """
        # Encabezado de tabla
        ## Crear encabezado de tabla
        self.set_fill_color(2, 15, 158)
        self.rect(5, 5, 287, 16, style="F")

        ## Imagen
        self.image("../Resources/Images/Icon.png", x=7, y=7, w=12, h=12)

        ## Título
        self.set_xy(25, 8)
        self.set_font("Helvetica", size=18)
        self.set_text_color(255)
        self.cell(0, 10, self._titulo, align="C")

        # Establece la fuente del cuerpo
        self.set_font("Times", size=10)

        # Color de las líneas
        pdf.set_draw_color(2, 15, 158)

        # Salto de línea
        self.ln(15)

        # Color del texte de la tabla
        self.set_text_color(0)
        self.set_fill_color(255, 255, 255)
        self.cell(0, 10, self._titulo, align="C")

        # Estilo del encabezado de tabla
        header_style = FontFace(
            emphasis="BOLD",
            color=255,
            fill_color=(2, 15, 158),
            family="Helvetica",
            size_pt=10,
        )

        # Se crea la tabla
        with self.table(
                # col_widths=(40, 40, 40, 40, 40, 40),
                borders_layout="NONE",
                cell_fill_color=(224, 235, 255),
                cell_fill_mode=TableCellFillMode.ROWS,
                line_height=6,
                headings_style=header_style,
        ) as table:
            # Encabezados
            header = table.row()
            header.cell("MARCA")
            header.cell("MODELO")
            header.cell("DIMS. (An x Pr x Al cm)")
            header.cell("GROSOR (mm)")
            header.cell("VOLUMNEN (L)")
            header.cell("MATERIAL")

            # Datos
            for urna in self._data:
                row = table.row()
                row.cell(str(urna.id_marca))
                row.cell(str(urna.modelo))
                row.cell(f"{urna.anchura} x {urna.profundidad} x"
                         f" {urna.altura}")
                row.cell(str(urna.grosor_cristal))
                row.cell(str(urna.volumen_tanque))
                row.cell(str(urna.id_material))

    def create_report(self) -> Result:
        """ Genera el reporte. """

        self.alias_nb_pages()
        self.add_page()
        self.set_margins(5, 5, 5)
        self.build_body()
        return self.save()

    def save(self) -> Result:
        """ Guarda el reporte en formato PDF. """
        try:
            self.output(f"{self._titulo}.pdf")
            return Result.success(1)
        except FPDFException as e:
            return Result.failure(f"Error interno de FPDF:\n {e}")
        except OSError as e:
            return Result.failure(f"Error del sistema de archivos:\n {e}")
        except Exception as e:
            return Result.failure(f"Error inesperado:\n {e}")

    def _get_data(self) -> Result:
        """ Obtiene los datos para el reporte"""

        dao = UrnaDAO()
        res = dao.get_list()
        if not res.is_success:
            return res
        self._data = res.value
        return self._data


if __name__ == "__main__":
    pdf = ReportListUrnasPDF("LISTADO DE URNAS")
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_margins(5, 5, 5)
    pdf.build_body()
    pdf.output("urnas.pdf")
