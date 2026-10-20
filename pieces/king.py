from config import ALL_DIRS
from pieces.base import Piece
from pieces.rook import Rook


class King(Piece):
    white_symbol = "♔"
    black_symbol = "♚"
    is_king = True

    # === ЗОНА ИГРОКА А (__init__ и get_moves) ===

    # === ЗОНА ИГРОКА Б (on_move) ===
    pass
