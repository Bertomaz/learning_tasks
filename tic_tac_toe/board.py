from constants import PLAYER_O, PLAYER_X

# === Module internal constants ===
# They are only needed for the internal workings of the module
_COLUMNS_PER_ROW = 3
_BITS_PER_QUARTER_BYTE = 2
_ENCODING = {  # How to map a cell state to a quarter-byte
    PLAYER_X: 0b01,
    PLAYER_O: 0b10
}
_DECODING = {  # The reverse mapping for the ENCODING
    value: key for key, value in _ENCODING.items()
}

# === Module internal functions ===
# They are only here as helpers
# for the internal working of the module
def _offset(row, column):
    quarter_bytes = row * _COLUMNS_PER_ROW + column
    return quarter_bytes * _BITS_PER_QUARTER_BYTE

def _print_state(board_state):
    print(f"{board_state:032b}")

def _clear_cell(board_state, row, colum):
    bitmask = ~(0b11 << _offset(row, column))
    return board_state & bitmask

# === Module public functions ===
# You may import/ use them as you see fit.
def create_empty_board():
    """Create an empty 3×3 board.

    Returns:
        The state of an empty board encoded as an integer
    """
    return 0

def set_player(board_state, row, column, player):
    """Set a cell of a board to be occupied by a player.

    This does not check if the cell is already occupied.
    Providing incorrect values for any of the arguments may have unexpected results.

    Args:
        board_state: An integer encoding the board state before the change.
        row: The row of the cell to be set. Must be in the interval (0…2).
        column: The column of the cell to be set. Must be in the interval (0…2).
        player: The player which occupies the cell, either `PLAYER_X`, `PLAYER_O` or `None`.
    Returns:
        The board state encoded as integer after the change was made.
    """
    if player is None:
        return _clear_cell(board_state, row, column)

    bitmask = _ENCODING[player] << _offset(row, column)
    return board_state | bitmask

def get_player(board_state, row, column):
    """Get the player who occupies a given cell.

    Providing incorrect values for any of the arguments may have unexpected results.

    Args:
        board_state: An integer encoding the board state from which to extract the player.
        row: The row of the cell to be gotten. Must be in the interval (0…2).
        column: The column of the cell to be gotten. Must be in the interval (0…2).
    Returns:
        The player which occupies the cell, either `PLAYER_X`, `PLAYER_O` or `None`.
    """
    flags = (board_state >> _offset(row, column)) & 0b11
    return _DECODING.get(flags, None)

def is_occupied(board_state, row, column):
    """Checks if a cell is occuoied by a player.

    Providing incorrect values for any of the arguments may have unexpected results.

    Args:
        board_state: An integer encoding the board state which to check.
        row: The row of the cell to be checked. Must be in the interval (0…2).
        column: The column of the cell to be checked. Must be in the interval (0…2).
    Returns:
        `True` if a player occupies the field, `False` otherwise.
    """
    return bool(get_player(board_state, row, column))
