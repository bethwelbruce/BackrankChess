def find_back_rank_mate_moves(board):
  """Finds all back-rank mate moves in the given board."""

  # Get the positions of all the pieces on the back rank.
  back_rank_pieces = []
  for row in range(7):
    for col in range(8):
      if board[row][col] is not None and board[row][col].color == board.turn:
        back_rank_pieces.append((row, col))

  # Find all pairs of pieces that can deliver a back-rank mate.
  back_rank_mate_moves = []
  for i in range(len(back_rank_pieces)):
    for j in range(i + 1, len(back_rank_pieces)):
      if back_rank_pieces[i][0] == back_rank_pieces[j][0]:
        back_rank_mate_moves.append((back_rank_pieces[i][1], back_rank_pieces[j][1]))

  return back_rank_mate_moves
