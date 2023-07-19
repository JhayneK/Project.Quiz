from base import questoes

score = 0
tam = len(questoes)

for i in range(1,tam+1):
    print(f"{questoes[i][0]}\n(A) - {questoes[i][1]}  (B) - {questoes[i][2]}  \
(C) - {questoes[i][3]}  (D) - {questoes[i][4]}\n")
    answer = input("Resposta: ")
    if answer.upper() == questoes[i][5]:
        print("Você acertou")
        score += 1
        print(score)
    else:
        print("Você errou.")

print("\nSeu score é: ", score)
