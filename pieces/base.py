from config import BLACK, WHITE


class Piece:
    """Базовый класс для всех шахматных фигур."""

    white_symbol = "?"
    black_symbol = "?"
    is_king = False

    def __init__(self, color: str):
        if color not in [WHITE, BLACK]:
            raise ValueError("Некорректный цвет!")
        self.color = color  # WHITE или BLACK

        if self.white_symbol == "?" or self.black_symbol == "?":
            raise NotImplementedError(
                f"Для класса {self.__class__} не прописал символ!"
            )

    def get_moves(self, row: int, col: int, board) -> list[tuple[int, int]]:
        """
        Возвращает список клеток [(r, c), ...], куда фигура может пойти с клетки (row, col).
        ВАЖНО: Здесь не нужно проверять, окажется ли свой король под шахом (это работа Движка).
        Нужно учитывать только границы доски, другие фигуры и особые правила самой фигуры.
        """
        raise NotImplementedError(
            "Не реализован метод get_moves() в классе", self.__class__
        )

    def on_move(
        self, from_pos: tuple[int, int], to_pos: tuple[int, int], board
    ) -> None:
        """
        Вызывается доской СРАЗУ ПОСЛЕ того, как фигуру переставили с from_pos на to_pos.
        Позволяет фигуре самой выполнить особые действия (рокировка, взятие на проходе, превращение).
        """
        raise NotImplementedError(
            "Не реализован метод on_move() в классе", self.__class__
        )

    def copy(self):
        """Создает копию фигуры для симуляции ходов в движке."""
        new_piece = self.__class__(self.color)
        return new_piece

    def __str__(self) -> str:
        return self.white_symbol if self.color == WHITE else self.black_symbol
