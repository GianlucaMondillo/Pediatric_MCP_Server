 # Pediatric MCP Server

Server MCP per calcoli medici pediatrici, score clinici e assessment.

## 🚀 Installazione


https://github.com/user-attachments/assets/280aa1d5-6ab5-461e-a9dd-ccbd3fd467be


```bash
git clone https://github.com/tuousername/pediatric-mcp-server.git
cd pediatric-mcp-server
pip install -r requirements.txt
```

## ⚙️ Configurazione Claude Desktop

**Questo server funziona solo con Claude Desktop (app desktop di Anthropic).**

### Passo 1: Trova il file di configurazione

Il file `claude_desktop_config.json` si trova in:

- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Mac**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

### Passo 2: Modifica il file di configurazione

Apri `claude_desktop_config.json` e aggiungi:

```json
{
  "mcpServers": {
    "pediatric-tools": {
      "command": "python",
      "args": ["PERCORSO_COMPLETO/pediatric-mcp-server/server.py"],
      "env": {}
    }
  }
}
```

**Sostituisci `PERCORSO_COMPLETO` con il path reale della cartella.**

### Passo 3: Riavvia Claude Desktop

Chiudi e riapri l'app Claude Desktop per caricare i nuovi strumenti.

## 🔧 Avvio Manuale

```bash
python server.py
```

## 📋 Strumenti Disponibili

### Score Medici
- PEWS (Pediatric Early Warning Score)
- PAS (Pediatric Appendicitis Score)
- APGAR Score
- GCS Pediatrico
- M-CHAT (Screening Autismo)
- Pediatric Trauma Score
- CATCH Score
- Westley Croup Score
- Centor Score Pediatrico
- Wells Score Pediatrico

### Calcoli Medici
- BSA (Superficie Corporea)
- Fluidi di Mantenimento (Holiday-Segar)
- Clearance Creatinina (Schwartz)
- BMI Pediatrico
- Fabbisogno Calorico
- Pressione Arteriosa Normale
- Altezza Predetta
- Superficie Ustionata
- ANC (Absolute Neutrophil Count)

### Assessment Clinici
- Valutazione Disidratazione
- Scale del Dolore
- Stato Nutrizionale
- Tappe Sviluppo
- Controllo Asma
- HEADS-ED (Salute Mentale)
- BEARS (Disturbi Sonno)
- Criteri Rome IV

## ⚠️ Disclaimer

Solo per scopi educativi. Non sostituisce il giudizio medico professionale.

## 📞 Supporto

Apri un Issue su GitHub per problemi o richieste.
