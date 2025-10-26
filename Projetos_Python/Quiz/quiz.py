from questions import list_questions

print("Seja muito bem vindo(a) ao quiz do Marlon!")

answer_user = input("Vamos começar? (S/N)\n")
if answer_user != 'S':
    quit();
else:
    print("Começando...");
    for item in list_questions:
        answer_user = input(f"{item['Question']}{item['Alternatives']}")
        if answer_user == item['Answer']:
            print("Resposta Certa!\n")
        else:
            print("Resposta Errada!\n")