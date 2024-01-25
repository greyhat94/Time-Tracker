import time

def log_attivita(attivita, tempo):
    with open('log_attivita.txt', 'a') as file_log:
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f'{timestamp} - Attività: {attivita}, Tempo: {tempo} secondi\n'
        file_log.write(log_entry)

def main():
    print("Benvenuto! Questo script tiene traccia del tempo trascorso su diverse attività.")
    
    while True:
        attivita = input("Inserisci l'attività corrente (o 'fine' per uscire): ")
        
        if attivita.lower() == 'fine':
            print("Arrivederci!")
            break
        
        inizio_attivita = time.time()
        input("Premi INVIO quando hai finito con l'attività.")
        fine_attivita = time.time()
        
        tempo_trascorso = int(fine_attivita - inizio_attivita)
        log_attivita(attivita, tempo_trascorso)
        
        print(f"Hai trascorso {tempo_trascorso} secondi su '{attivita}'.")

if __name__ == "__main__":
    main()
