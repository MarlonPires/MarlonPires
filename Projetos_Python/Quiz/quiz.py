from questions import list_questions

print("\nSeja muito bem vindo(a) ao quiz do Marlon!")

answer_user = input("Vamos começar? (S/N)\n")
if answer_user.upper() != 'S':
    quit()
score = 0
print("\nComeçando... \n");
for item in list_questions:
    answer_user = input(f"{item['Question']}\n{item['Alternatives']} \n")
    if answer_user.lower() == item['Answer']:
        print("Resposta Certa!\n")
        score+=1
    else:
        print("Resposta Errada!\n")
        print(f"A resposta correta é '{item['Answer']}'.\n")

    print(f"{item['Explanation']}\n")
if(score==0):
    print("Estude mais um pouco.")
else:
    print("Muito bem!")
print(f"Você acertou {score}/{len(list_questions)} \n")
print("Finalizando...\n")