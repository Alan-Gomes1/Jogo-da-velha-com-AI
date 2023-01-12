import time
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
  def __init__(self):
    self.board = [' ' for _ in range(9)]
    self.current_winner = None
    
  def print_board(self):
    # Exibindo cada linha dos 3 blocos
    for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
      print('| ' + ' | '.join(row) + ' |')
      
  @staticmethod
  def print_board_nums():
    # number_board informa qual número corresponde a qual bloco
    number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)] # o J como parâmetro do range assume valores dinâmico ex: 0 a 3, 3 a 6 e 6 a 9
    for row in number_board:
      print('| ' + ' | '.join(row) + ' |')
    print()
  """resultado:
    | 0 | 1 | 2 |
    | 3 | 4 | 5 |
    | 6 | 7 | 8 |"""
    
  def available_moves(self):
    """Pega a posição das jogadas e retorna as posições vazias
      ex: ['x', 'o', ' '] --> [(0, x), (1, o), (2, ' ')]"""
    return [i for i, spot in enumerate(self.board) if spot == ' '] 
  
  def empty_squares(self):
    return ' ' in self.board
  
  def num_empty_squares(self):
    return self.board.count(' ')
  
  def make_move(self, square, letter):
    if self.board[square] == ' ':
      self.board[square] = letter
      if self.winner(square, letter):
        self.current_winner = letter
      return True
    return False
  
  def winner(self, square, letter):
    # verificação da linha
    row_index = square // 3
    row = self.board[row_index*3 : (row_index+1)*3]
    if all([spot == letter for spot in row]):
      return True
    
    # Verificação da coluna
    column_index = square % 3
    column = [self.board[column_index+i*3] for i in range(3)]
    if all([spot == letter for spot in column]):
      return True
    
    # Verificação da diagonal
    # as posições de números pares são os únicos campos possivéis para se vencer na diagonal [0, 4, 8] ou [2, 4, 6]
    if square % 2 == 0:
      diagonal1 = [self.board[i] for i in [0, 4, 8]]
      if all([spot == letter for spot in diagonal1]):
        return True
      
      diagonal2 = [self.board[i] for i in [2, 4, 6]]
      if all([spot == letter for spot in diagonal2]):
        return True
      
    return False # Caso não haja vencedor
  

def play(game, x_player, o_player, print_game=True):
  # Retorna o vencedor do jogo ou empate.
  if print_game:
    game.print_board_nums()
    
  letter = 'X' # Símbolo inicial
  while game.empty_squares():
    # Verifica se ainda há campos vazios, caso não haja é porque o jogo chegou ao fim.
    if letter == 'O':
      square = o_player.get_move(game)
    else:
      square = x_player.get_move(game)
      
    if game.make_move(square, letter):
      if print_game:
        print(letter + f' fez um movimento no campo {square}')
        game.print_board()
        print('')
        
      if game.current_winner:
        if print_game:
          print(letter + ' Vencedor!')
        return letter
        
      letter = 'O' if letter == 'X' else 'X' # Trocando jogadores
      
    time.sleep(0.8)
  if print_game:
    print('Empate!')

      
if __name__ == '__main__':
  x_player = HumanPlayer('X')
  o_player = RandomComputerPlayer('O')
  jogo_da_velha = TicTacToe()
  play(jogo_da_velha, x_player, o_player, print_game=True)