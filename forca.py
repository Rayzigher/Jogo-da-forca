# Jogo da Forca
import random

def escolher_palavra():
    palavras = ["python", "desenvolvimento", "programacao", "computador", "jogo", "forca"]
    return random.choice(palavras)

def exibir_forca(erros):
    estados = [
        '''
          -----
          |   |
              |
              |
              |
              |
        =========
        ''',
        '''
          -----
          |   |
          O   |
              |
              |
              |
        =========
        ''',
        '''
          -----
          |   |
          O   |
          |   |
              |
              |
        =========
        ''',
        '''
          -----
          |   |
          O   |
         /|   |
              |
              |
        =========
        ''',
        '''
          -----
          |   |
          O   |
         /|\\  |
              |
              |
        =========
        ''',
        '''
          -----
          |   |
          O   |
         /|\\  |
         /    |
              |
        =========
        ''',
        '''
          -----
          |   |
          O   |
         /|\\  |
         / \\  |
              |
        =========
        '''
    ]
    print(estados[erros])


def jogar():
    palavra = escolher_palavra()
    palavra_oculta = ["_"] * len(palavra)
    tentativas = 6
    letras_erradas = []
    letras_certas = []

    print("Seja bem vindo ao jogo da forca")

    while tentativas > 0 and "".join(palavra_oculta) != palavra:
        print("\nPalavra: ", " ".join(palavra_oculta))
        print(f"Tentivas restantes: {tentativas}")
        print("Letras erradas ", " ".join(letras_erradas))

        letra = input("Digite uma letra: ").lower()

        if letra in letras_certas or letra in letras_erradas:
            print("Você ja tentou essa letra.")
            continue

        if letra in palavra:
            letras_certas.append(letra)
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_oculta[i] = letra
        else:
            letras_erradas.append(letra)
            tentativas -= 1
            exibir_forca(6 - tentativas)
    
    if "".join(palavra_oculta) == palavra:
        print(f"\nParabéns! Você adivinhou a palavra: {palavra}")
    else:
        print(f"\nVocê perdeu! A palavra era: {palavra}")
    
if __name__ == "__main__":
    jogar()
        
    

    




