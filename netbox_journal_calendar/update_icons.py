import requests
import json
import os


def update_mdi_icons():
    # URL del meta.json ufficiale di MDI
    URL = "https://raw.githubusercontent.com/Templarian/MaterialDesign-JS/master/meta.json"

    try:
        print("Scaricamento icone in corso...")
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Trasformiamo i dati in una lista di tuple (codice_css, nome_leggibile)
        # Esempio: ("mdi mdi-account", "Account")
        icon_list = [
            (f"mdi mdi-{icon['name']}", icon['name'].replace('-', ' ').title())
            for icon in data
        ]

        # Salviamo il risultato in un file JSON locale
        file_path = os.path.join(os.path.dirname(__file__), 'mdi_icons.json')
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(icon_list, f, indent=4)

        print(f"Successo! {len(icon_list)} icone salvate in mdi_icons.json")

    except Exception as e:
        print(f"Errore durante l'aggiornamento: {e}")


if __name__ == "__main__":
    update_mdi_icons()