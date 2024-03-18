while True:
    print("\n1. Atspausdinti įvestį atbulai"
          "\n2. Atspausdinti įvestį ir simbolių įvestyje kiekį"
          "\nq  - išeiti")
    pasirinkimas = input(">>> ")

#####################################
# pasirinkimo patikrinimas
    if pasirinkimas not in ("q", "1", "2"):
        print("Tokio pasirinkimo nėra")
        continue
