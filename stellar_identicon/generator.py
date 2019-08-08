import hashlib
import math
import randomcolor

from pydenticon import Generator


class ExtendedPydenticonGenerator(Generator):
    SCHEME_RAW = 'raw'
    SCHEME_STANDART = 'standart'
    SCHEME_BRIGHT = 'bright'
    SCHEME_LIGHT = 'light'
    SCHEME_DARK = 'dark'

    SCHEME_CHOICES = (
        SCHEME_RAW,
        SCHEME_STANDART,
        SCHEME_BRIGHT,
        SCHEME_LIGHT,
        SCHEME_DARK,
    )

    def __init__(self, rows, columns, digest=hashlib.md5, foreground=['#000000'], background="#ffffff", color_scheme=SCHEME_RAW):
        self.color_scheme = color_scheme
        super(ExtendedGenerator, self).__init__(rows, columns, digest, foreground, background)

    def _generate_matrix(self, hash_bytes, symmetry):
        cells = self.rows * self.columns

        matrix = [[False] * self.columns for row in range(self.rows)]

        if symmetry:
            columns_for_calculation = math.ceil(self.columns / 2.)
        else:
            columns_for_calculation = self.columns

        for column in range(columns_for_calculation):
            for row in range(self.rows):
                if self._get_bit(column + row * columns_for_calculation, hash_bytes[1:]):
                    matrix[row][column] = True

                    if symmetry:
                        matrix[row][self.columns - column - 1] = True

        return matrix

    def _get_color(self, data):
        if self.color_scheme == self.SCHEME_RAW:
            return '#' + data

        rand_color = randomcolor.RandomColor(seed=data)
        return rand_color.generate(luminosity=self.color_scheme)[0]

    def generate(self, data, width, height, padding=(0, 0, 0, 0), symmetry=False, output_format="png", inverted=False):
        digest_byte_list = self._data_to_digest_byte_list(data)

        # Create the matrix describing which block should be filled-in.
        matrix = self._generate_matrix(digest_byte_list, symmetry=symmetry)

        # Determine the background and foreground colours.
        if output_format == "ascii":
            foreground = "+"
            background = "-"
        else:
            background = self.background

            if self.foreground:
                foreground = self.foreground[digest_byte_list[0] % len(self.foreground)]
            else:
                foreground = self._get_color(digest_byte_list[0])

        # Swtich the colours if inverted image was requested.
        if inverted:
            foreground, background = background, foreground

        # Generate the identicon in requested format.
        if output_format == "ascii":
            return self._generate_ascii(matrix, foreground, background)
        else:
            return self._generate_image(matrix, width, height, padding, foreground, background, output_format)
