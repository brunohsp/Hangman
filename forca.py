# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
	def __init__(self, word):
		self.word = word.upper()
		self.secret = ''
		self.lifes = 0
		
	# Método para adivinhar a letra
	def guess(self, letter):
		if letter in self.word:
			index = 0
			for l in self.word:
				if letter.upper() == l.upper():
					self.secret[index] = letter
				index += 1
		else:
			self.lifes += 1

	# Método para verificar se o jogo terminou
	def hangman_over(self):
		if self.lifes <= 5 and '_' in self.secret:
			return 0
		else:
			return 1

	# Método para verificar se o jogador venceu
	def hangman_won(self):
		if '_' in self.secret and self.lifes >= 5:
			return 0
		else:
			return 1

	# Método para não mostrar a letra no board
	def hide_word(self):
		self.secret = ["_" for l in self.word]
		
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		print(board[self.lifes])
		print('\n\n', self.secret)

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
	with open("palavras.txt", "rt") as f:
		bank = f.readlines()
	return bank[random.randint(0,len(bank))].strip().upper()


# Função Main - Execução do Programa
def main():

	# Objeto
	game = Hangman(rand_word())
	game.hide_word()

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while not game.hangman_over():
		game.print_game_status()
		kick = input("Informe uma letra\n").strip().upper()
		game.guess(kick)

	game.print_game_status()

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		print('\nParabéns! Você venceu!!')

	else:
		print('\nGame over! Você perdeu.')
		print('A palavra era ' + game.word)
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()

