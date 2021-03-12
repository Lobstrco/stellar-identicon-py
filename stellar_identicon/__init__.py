from stellar_sdk.keypair import Keypair
from stellar_sdk.exceptions import Ed25519PublicKeyInvalidError

from .exceptions import InvalidStellarAddressException
from .generator import ExtendedPydenticonGenerator


DEFAULT_IDENTICON_SIZE = 7


class StellarIdenticonGenerator(object):
    def __init__(self, *args, **kwargs):
        self.generator = ExtendedPydenticonGenerator(
            DEFAULT_IDENTICON_SIZE, DEFAULT_IDENTICON_SIZE, foreground=None
        )

    def _is_valid_key(self, public_key):
        try:
            Keypair.from_public_key(public_key=public_key)
            return True
        except Ed25519PublicKeyInvalidError:
            raise InvalidStellarAddressException("Invalid stellar address")

    def generate(
        self, public_key, icon_width=210, icon_height=210, output_format="png"
    ):
        if self._is_valid_key(public_key):
            return self.generator.generate(
                public_key,
                icon_width,
                icon_height,
                output_format=output_format,
                symmetry=True,
            )
