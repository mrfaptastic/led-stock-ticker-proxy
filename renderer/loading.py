from rgbmatrix.graphics import DrawText
from version import __version__
from constants import LOGO_IMAGE
from utils import align_text_center, load_font, load_image, center_image
from data.color import Color


class Loading:
    """
    Render a splash screen while tickers' data is being fetched

    Arguments:
        matrix (rgbmatrix.RGBMatrix):           RGBMatrix instance
        config (data.Config):                   Config instance

    Attributes:
        canvas (rgbmatrix.Canvas):              Canvas associated with matrix
        logo (PIL.Image):                       Software logo image
        color (rgbmatrix.graphics.Color):       Color instance
        font (rgbmatrix.graphics.Font):         Font instance
        logo_x_offset (int):                    Logo image x-coord
        logo_y_offset (int):                    Logo image y-coord
        version_x (int):                        Version text x-coord
        version_y (int):                        Version text y-coord
    """

    def __init__(self, matrix, config):
        self.matrix = matrix
        self.config = config
        self.canvas = matrix.CreateFrameCanvas()

        # Load logo
        self.logo = load_image(LOGO_IMAGE, (28, 28))

        # Load color
        self.color = Color.ORANGE

        # Load font
        self.font = load_font(self.config.layout['fonts']['4x6'])

        self.logo_x_offset, self.logo_y_offset = center_image(self.canvas.width,
                                                              self.canvas.height,
                                                              self.logo.size[0],
                                                              self.logo.size[1])

        self.version_x = align_text_center(string=__version__,
                                           canvas_width=self.canvas.width,
                                           font_width=self.font.baseline - 1)[0]
        self.version_y = self.canvas.height

    def render(self):
        self.canvas.Clear()

        self.render_logo()
        self.render_version()

        self.canvas = self.matrix.SwapOnVSync(self.canvas)

    def render_version(self):
        return DrawText(self.canvas, self.font, self.version_x, self.version_y, self.color, __version__)

    def render_logo(self):
        return self.canvas.SetImage(self.logo, self.logo_x_offset, self.logo_y_offset - 3)
