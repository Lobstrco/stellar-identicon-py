from .generator import ExtendedPydenticonGenerator


DEFAULT_IDENTICON_SIZE = 7


class StellarIdenticonGenerator(object):
    def __init__(self, *args, **kwargs):
        self.generator = ExtendedPydenticonGenerator(
            DEFAULT_IDENTICON_SIZE, DEFAULT_IDENTICON_SIZE, color_scheme=ExtendedGenerator.SCHEME_DARK, foreground=None
        )

    def generate(self, public_key, icon_width=210, icon_height=210, output_format="png"):
        return self.generator.generate(
            public_key, icon_width, icon_height, output_format=output_format, symmetry=True
        )
