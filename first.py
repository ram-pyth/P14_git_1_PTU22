while True:
    print("\n1. Atspausdinti įvestį atbulai"
          "\nq  - išeiti")
    pasirinkimas = input(">>> ")

#####################################
# pasirinkimo patikrinimas
    if pasirinkimas not in ("q", "1"):
        print("--------------------")
        print("Tokio pasirinkimo nėra")
        continue

# pauzė realizuota su input, input laukia Enter paspaudimo
    print("\n-----------")
    input("Tęsti - Enter")
