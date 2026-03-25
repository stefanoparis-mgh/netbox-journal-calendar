# 📅 NetBox Journal Calendar Plugin

[![License](https://img.shields.io)](https://opensource.org)
[![NetBox Compatibility](https://img.shields.io)](https://github.com)

Un plugin per **NetBox** che trasforma le tue Journal Entries in un calendario interattivo e filtrabile. Visualizza cronologicamente gli interventi, i guasti e le attività di manutenzione direttamente sulla griglia temporale.

---

## 📸 Screenshots

### Vista Mensile del Calendario
![Vista Calendario](https://raw.githubusercontent.com)
*Esempio della griglia mensile con eventi colorati per tipo.*

### Filtri Avanzati
![Filtri](https://raw.githubusercontent.com)
*Filtra per Sito, Device o Custom Fields per isolare gli interventi specifici.*

---

## ✨ Funzionalità

- **Visualizzazione Intuitiva**: Griglia mensile completa basata sul modulo `calendar` di Python.
- **Color-Coding Automatico**:
  - 🔵 **Info**: Note informative.
  - 🟢 **Success**: Interventi risolti.
  - 🟡 **Warning**: Avvisi o manutenzioni programmate.
  - 🔴 **Danger**: Guasti critici o errori.
- **Integrazione Nativa**: Utilizza i componenti UI di NetBox e Bootstrap per un look coerente.
- **Filtri Potenti**: Supporta il filtraggio per `Site`, `Device`, `User` e perfino **Custom Fields** (es. ID Ticket).

---

## 🛠 Installazione

### 1. Scarica e Installa il Pacchetto
Puoi installarlo direttamente da GitHub tramite `pip`:

```bash
pip install git+https://github.com/stefanoparis-mgh/netbox-journal-calendar
