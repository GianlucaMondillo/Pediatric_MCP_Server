"""
Strumenti clinici aggiuntivi per pediatria di base.
Formule e calcoli pratici utilizzati quotidianamente dai pediatri di libera scelta.
"""
import mcp.types as types
from utils.medical_formulas import (
    calculate_bsa_mosteller, 
    calculate_bsa_dubois, 
    holiday_segar_fluids,
    calculate_weight_percentile_who
)

def get_clinical_tools():
    """Restituisce tutti gli strumenti clinici aggiuntivi"""
    return [
        types.Tool(
            name="calculate_fever_fluid_requirements",
            description="Calcola aumento fabbisogno idrico in caso di febbre secondo regola clinica 10-15%/°C",
            inputSchema={
                "type": "object",
                "properties": {
                    "weight_kg": {
                        "type": "number", 
                        "minimum": 2, 
                        "maximum": 100,
                        "description": "Peso in chilogrammi"
                    },
                    "temperature_celsius": {
                        "type": "number", 
                        "minimum": 37.5, 
                        "maximum": 42,
                        "description": "Temperatura corporea in gradi Celsius"
                    },
                    "baseline_fluids_ml": {
                        "type": "number",
                        "minimum": 100,
                        "maximum": 5000,
                        "description": "Fluidi di base giornalieri (ml/24h) - può essere calcolato con Holiday-Segar"
                    }
                },
                "required": ["weight_kg", "temperature_celsius", "baseline_fluids_ml"]
            }
        ),
        
        types.Tool(
            name="assess_growth_velocity",
            description="Valuta velocità di crescita pediatrica secondo curve standard WHO/CDC",
            inputSchema={
                "type": "object",
                "properties": {
                    "age_months": {
                        "type": "integer", 
                        "minimum": 1, 
                        "maximum": 240,
                        "description": "Età in mesi"
                    },
                    "current_weight_kg": {
                        "type": "number", 
                        "minimum": 1, 
                        "maximum": 150,
                        "description": "Peso attuale in kg"
                    },
                    "previous_weight_kg": {
                        "type": "number", 
                        "minimum": 1, 
                        "maximum": 150,
                        "description": "Peso precedente in kg"
                    },
                    "months_interval": {
                        "type": "integer",
                        "minimum": 1,
                        "maximum": 24,
                        "description": "Intervallo tra le misurazioni in mesi"
                    }
                },
                "required": ["age_months", "current_weight_kg", "previous_weight_kg", "months_interval"]
            }
        ),
        
        types.Tool(
            name="calculate_head_circumference_growth",
            description="Valuta crescita circonferenza cranica secondo norme pediatriche",
            inputSchema={
                "type": "object",
                "properties": {
                    "age_months": {
                        "type": "integer", 
                        "minimum": 0, 
                        "maximum": 60,
                        "description": "Età in mesi (0-60 mesi)"
                    },
                    "head_circumference_cm": {
                        "type": "number", 
                        "minimum": 25, 
                        "maximum": 65,
                        "description": "Circonferenza cranica in cm"
                    },
                    "gender": {
                        "type": "string",
                        "enum": ["m", "f", "male", "female"],
                        "description": "Sesso: m/male o f/female"
                    }
                },
                "required": ["age_months", "head_circumference_cm", "gender"]
            }
        ),
        
        types.Tool(
            name="assess_developmental_milestones",
            description="Verifica tappe dello sviluppo neuromotorio secondo linee guida AAP",
            inputSchema={
                "type": "object",
                "properties": {
                    "age_months": {
                        "type": "integer", 
                        "minimum": 1, 
                        "maximum": 60,
                        "description": "Età in mesi"
                    },
                    "motor_skills": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": ["sits_without_support", "crawls", "walks_alone", "runs", "jumps", "rides_tricycle", "hops_one_foot"]
                        },
                        "description": "Competenze motorie presenti"
                    },
                    "language_skills": {
                        "type": "array",
                        "items": {
                            "type": "string", 
                            "enum": ["babbling", "first_words", "two_word_phrases", "simple_sentences", "complex_sentences", "storytelling"]
                        },
                        "description": "Competenze linguistiche presenti"
                    },
                    "social_skills": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": ["social_smile", "stranger_anxiety", "separation_anxiety", "parallel_play", "cooperative_play", "empathy"]
                        },
                        "description": "Competenze sociali presenti"
                    }
                },
                "required": ["age_months"]
            }
        )
    ]

def handle_clinical_tools(name: str, arguments: dict):
    """Gestisce gli strumenti clinici aggiuntivi"""
    if name == "calculate_fever_fluid_requirements":
        return _calculate_fever_fluid_requirements(arguments)
    elif name == "assess_growth_velocity":
        return _assess_growth_velocity(arguments)
    elif name == "calculate_head_circumference_growth":
        return _calculate_head_circumference_growth(arguments)
    elif name == "assess_developmental_milestones":
        return _assess_developmental_milestones(arguments)
    else:
        raise ValueError(f"Strumento clinico non implementato: {name}")

def _calculate_fever_fluid_requirements(args):
    """
    Calcola aumento fabbisogno idrico per febbre
    Regola clinica: +10-15% per ogni grado sopra 37°C
    """
    try:
        weight = args.get('weight_kg')
        temp = args.get('temperature_celsius')
        baseline = args.get('baseline_fluids_ml')
        
        degrees_above_normal = temp - 37.0
        
        # Incremento 12.5% (media tra 10-15%) per grado
        fever_increase_percent = degrees_above_normal * 12.5
        additional_fluids = baseline * (fever_increase_percent / 100)
        total_fluids = baseline + additional_fluids
        
        # Calcoli per diversi intervalli
        per_hour = total_fluids / 24
        per_6h = total_fluids / 4
        per_8h = total_fluids / 3
        
        result = f"""Fabbisogno Idrico in Febbre
==========================
👶 Paziente: {weight} kg, T° {temp}°C
Temperatura sopra normale: +{degrees_above_normal:.1f}°C

💧 FABBISOGNI IDRICI:
- Baseline (normotermia): {baseline} ml/24h
- Incremento per febbre: +{additional_fluids:.0f} ml/24h ({fever_increase_percent:.1f}%)
- Totale necessario: {total_fluids:.0f} ml/24h

⏰ FRAZIONAMENTI:
- Per ora: {per_hour:.1f} ml/h
- Ogni 6 ore: {per_6h:.0f} ml
- Ogni 8 ore: {per_8h:.0f} ml

📋 REGOLA CLINICA:
- +10-15% fabbisogno per ogni °C >37°C
- Perdite insensibili aumentate per:
  - Sudorazione
  - Tachipnea
  - Vasodilatazione

⚠️ CONSIDERAZIONI:
- Monitorare segni disidratazione
- Valutare tolleranza orale
- Considerare vie alternative se vomito
- Aumentare ulteriormente se diarrea presente

🧪 ELETTROLITI:
- Mantenere Na+ 135-145 mEq/L
- Aggiungere KCl se intake normale
- Monitorare se febbre >48h

Riferimento: Nelson Textbook of Pediatrics
Principi di gestione fluidi in febbre
"""
        return [types.TextContent(type="text", text=result)]
        
    except Exception as e:
        return [types.TextContent(type="text", text=f"Errore nel calcolo fluidi febbre: {str(e)}")]

def _assess_growth_velocity(args):
    """
    Valuta velocità di crescita secondo parametri pediatrici standard
    """
    try:
        age_months = args.get('age_months')
        current_weight = args.get('current_weight_kg')
        previous_weight = args.get('previous_weight_kg')
        interval_months = args.get('months_interval')
        
        # Calcolo velocità di crescita
        weight_gain = current_weight - previous_weight
        weight_gain_per_month = weight_gain / interval_months
        weight_gain_grams_per_day = (weight_gain * 1000) / (interval_months * 30.4)
        
        # Velocità attese per età (approssimazioni cliniche)
        if age_months <= 3:
            expected_gain_per_day = "25-30 g/die"
            expected_monthly = "750-900 g/mese"
        elif age_months <= 6:
            expected_gain_per_day = "20-25 g/die"
            expected_monthly = "600-750 g/mese"
        elif age_months <= 12:
            expected_gain_per_day = "10-15 g/die"
            expected_monthly = "300-450 g/mese"
        elif age_months <= 24:
            expected_gain_per_day = "5-10 g/die"
            expected_monthly = "150-300 g/mese"
        else:
            expected_gain_per_day = "3-8 g/die"
            expected_monthly = "100-250 g/mese"
        
        # Valutazione crescita
        if weight_gain_grams_per_day < 0:
            assessment = "PERDITA DI PESO - Valutazione urgente"
            color = "🔴"
        elif age_months <= 6 and weight_gain_grams_per_day < 15:
            assessment = "CRESCITA INADEGUATA - Monitoraggio stretto"
            color = "🟠"
        elif age_months > 6 and age_months <= 24 and weight_gain_grams_per_day < 5:
            assessment = "CRESCITA LENTA - Valutazione nutrizionale"
            color = "🟡"
        elif age_months > 24 and weight_gain_grams_per_day < 3:
            assessment = "POSSIBILE RALLENTAMENTO - Monitoraggio"
            color = "🟡"
        else:
            assessment = "CRESCITA ADEGUATA"
            color = "🟢"
        
        age_years = age_months // 12
        age_remaining = age_months % 12
        age_display = f"{age_years}a {age_remaining}m" if age_remaining > 0 else f"{age_years} anni"
        
        result = f"""Velocità di Crescita Ponderale
=============================
{color} Paziente: {age_display}
Periodo: {interval_months} mesi

📊 CRESCITA OSSERVATA:
- Peso precedente: {previous_weight} kg
- Peso attuale: {current_weight} kg
- Incremento totale: {weight_gain:+.2f} kg
- Velocità: {weight_gain_grams_per_day:.1f} g/die
- Mensile: {weight_gain_per_month*1000:.0f} g/mese

📈 CRESCITA ATTESA PER ETÀ:
- Giornaliera: {expected_gain_per_day}
- Mensile: {expected_monthly}

💡 VALUTAZIONE: {assessment}

📋 VELOCITÀ NORMALI PER ETÀ:
- 0-3 mesi: 25-30 g/die (750-900 g/mese)
- 3-6 mesi: 20-25 g/die (600-750 g/mese)
- 6-12 mesi: 10-15 g/die (300-450 g/mese)
- 1-2 anni: 5-10 g/die (150-300 g/mese)
- >2 anni: 3-8 g/die (100-250 g/mese)

⚠️ RED FLAGS:
- Perdita di peso a qualsiasi età
- <15 g/die nei primi 6 mesi
- <5 g/die tra 6-24 mesi
- Attraversamento >2 linee percentili verso il basso

🔍 SE CRESCITA INADEGUATA:
- Valutare intake calorico
- Escludere malassorbimento
- Valutare patologie organiche
- Considerare fattori psicosociali

Riferimento: WHO Growth Standards
AAP Bright Futures Guidelines
"""
        return [types.TextContent(type="text", text=result)]
        
    except Exception as e:
        return [types.TextContent(type="text", text=f"Errore nella valutazione crescita: {str(e)}")]

def _calculate_head_circumference_growth(args):
    """
    Valuta crescita circonferenza cranica secondo norme WHO
    """
    try:
        age_months = args.get('age_months')
        hc_cm = args.get('head_circumference_cm')
        gender = args.get('gender')
        
        is_male = gender.lower() in ['m', 'male']
        
        # Valori medi approssimativi WHO (semplificati)
        if age_months == 0:  # Nascita
            mean_hc = 34.5 if is_male else 34.0
        elif age_months == 1:
            mean_hc = 37.0 if is_male else 36.5
        elif age_months == 3:
            mean_hc = 40.0 if is_male else 39.5
        elif age_months == 6:
            mean_hc = 43.0 if is_male else 42.5
        elif age_months == 12:
            mean_hc = 46.0 if is_male else 45.5
        elif age_months == 24:
            mean_hc = 48.5 if is_male else 48.0
        elif age_months == 36:
            mean_hc = 50.0 if is_male else 49.5
        else:
            # Interpolazione approssimativa per altre età
            if age_months < 12:
                # Crescita rapida primo anno
                mean_hc = 34.5 + (age_months * 0.95) if is_male else 34.0 + (age_months * 0.95)
            else:
                # Crescita più lenta dopo primo anno
                mean_hc = 46.0 + ((age_months - 12) * 0.21) if is_male else 45.5 + ((age_months - 12) * 0.21)
        
        # Deviazione dalla media (approssimazione)
        deviation = hc_cm - mean_hc
        
        # Valutazione (approssimativa - DS ≈ 1.5 cm)
        if abs(deviation) <= 1.5:
            assessment = "NORMALE"
            color = "🟢"
        elif abs(deviation) <= 3.0:
            if deviation > 0:
                assessment = "LIEVEMENTE AUMENTATA - Monitoraggio"
            else:
                assessment = "LIEVEMENTE RIDOTTA - Monitoraggio"
            color = "🟡"
        else:
            if deviation > 0:
                assessment = "MACROCEFALIA - Valutazione specialistica"
            else:
                assessment = "MICROCEFALIA - Valutazione urgente"
            color = "🔴"
        
        # Velocità di crescita attesa
        if age_months <= 3:
            expected_growth = "2.0 cm/mese"
        elif age_months <= 6:
            expected_growth = "1.0 cm/mese"
        elif age_months <= 12:
            expected_growth = "0.5 cm/mese"
        else:
            expected_growth = "0.25 cm/mese"
        
        result = f"""Circonferenza Cranica
====================
{color} Paziente: {gender.upper()}, {age_months} mesi
CC attuale: {hc_cm} cm

📊 VALUTAZIONE:
- Media per età/sesso: {mean_hc:.1f} cm
- Deviazione: {deviation:+.1f} cm
- Stato: {assessment}

📈 CRESCITA NORMALE CC:
- Nascita: 34-35 cm
- 1 mese: 37 cm
- 3 mesi: 40 cm  
- 6 mesi: 43 cm
- 12 mesi: 46 cm
- 24 mesi: 48.5 cm

⏱️ VELOCITÀ CRESCITA ATTESA:
- Per questa età: {expected_growth}

📋 VELOCITÀ NORMALI:
- 0-3 mesi: 2.0 cm/mese
- 3-6 mesi: 1.0 cm/mese
- 6-12 mesi: 0.5 cm/mese
- >12 mesi: 0.25 cm/mese

⚠️ SEGNALI DI ALLARME:
- Macrocefalia (>97° percentile)
- Microcefalia (<3° percentile) 
- Crescita troppo rapida
- Crossing percentiles

🔍 SE ANOMALA:
- Macrocefalia: Ecografia/TC, valutare familiarità
- Microcefalia: Valutazione genetica/neurologica
- Monitoraggio seriato essenziale

📏 MISURAZIONE CORRETTA:
- Nastro sopra sopracciglia
- Passaggio per occipite
- Circonferenza massima
- 3 misurazioni, prendere la maggiore

Riferimento: WHO Head Circumference Charts
AAP Bright Futures Guidelines
"""
        return [types.TextContent(type="text", text=result)]
        
    except Exception as e:
        return [types.TextContent(type="text", text=f"Errore valutazione circonferenza cranica: {str(e)}")]

def _assess_developmental_milestones(args):
    """
    Valuta tappe sviluppo neuromotorio secondo linee guida AAP
    """
    try:
        age_months = args.get('age_months')
        motor_skills = args.get('motor_skills', [])
        language_skills = args.get('language_skills', [])
        social_skills = args.get('social_skills', [])
        
        # Tappe attese per età (semplificato)
        milestones_by_age = {
            6: {
                'motor': ['sits_without_support'],
                'language': ['babbling'],
                'social': ['social_smile']
            },
            9: {
                'motor': ['crawls'],
                'language': ['babbling'],
                'social': ['stranger_anxiety']
            },
            12: {
                'motor': ['walks_alone'],
                'language': ['first_words'],
                'social': ['separation_anxiety']
            },
            18: {
                'motor': ['runs'],
                'language': ['two_word_phrases'],
                'social': ['parallel_play']
            },
            24: {
                'motor': ['jumps'],
                'language': ['simple_sentences'],
                'social': ['parallel_play']
            },
            36: {
                'motor': ['rides_tricycle'],
                'language': ['complex_sentences'],
                'social': ['cooperative_play']
            },
            48: {
                'motor': ['hops_one_foot'],
                'language': ['storytelling'],
                'social': ['empathy']
            }
        }
        
        # Trova tappe attese per l'età più vicina
        expected_age = min(milestones_by_age.keys(), key=lambda x: abs(x - age_months))
        expected = milestones_by_age.get(expected_age, {'motor': [], 'language': [], 'social': []})
        
        # Valutazione sviluppo
        motor_ok = all(skill in motor_skills for skill in expected['motor'])
        language_ok = all(skill in language_skills for skill in expected['language'])
        social_ok = all(skill in social_skills for skill in expected['social'])
        
        overall_assessment = "NORMALE" if motor_ok and language_ok and social_ok else "RITARDO POSSIBILE"
        color = "🟢" if overall_assessment == "NORMALE" else "🟡"
        
        # Red flags per età
        red_flags = []
        if age_months >= 6 and 'social_smile' not in social_skills:
            red_flags.append("Assenza sorriso sociale")
        if age_months >= 12 and 'first_words' not in language_skills:
            red_flags.append("Assenza prime parole")
        if age_months >= 18 and 'walks_alone' not in motor_skills:
            red_flags.append("Non cammina autonomamente")
        if age_months >= 24 and 'two_word_phrases' not in language_skills:
            red_flags.append("Non combina parole")
            
        result = f"""Sviluppo Neuromotorio
=====================
{color} Età: {age_months} mesi
Valutazione: {overall_assessment}

🏃 SVILUPPO MOTORIO:
Presente: {', '.join(motor_skills) if motor_skills else 'Nessuna competenza inserita'}
Atteso per età: {', '.join(expected['motor'])}
Status: {'✓ OK' if motor_ok else '⚠ Valutare'}

🗣️ SVILUPPO LINGUAGGIO:
Presente: {', '.join(language_skills) if language_skills else 'Nessuna competenza inserita'}
Atteso per età: {', '.join(expected['language'])}
Status: {'✓ OK' if language_ok else '⚠ Valutare'}

👥 SVILUPPO SOCIALE:
Presente: {', '.join(social_skills) if social_skills else 'Nessuna competenza inserita'}
Atteso per età: {', '.join(expected['social'])}
Status: {'✓ OK' if social_ok else '⚠ Valutare'}

📅 TAPPE PRINCIPALI:
- 6 mesi: Siede, babbling, sorriso sociale
- 9 mesi: Gattona, ansia estranei
- 12 mesi: Cammina, prime parole, ansia separazione
- 18 mesi: Corre, frasi 2 parole, gioco parallelo
- 24 mesi: Salta, frasi semplici
- 36 mesi: Triciclo, frasi complesse, gioco cooperativo
- 48 mesi: Salta su un piede, racconta storie

🚩 RED FLAGS PRESENTI:
{chr(10).join(['• ' + flag for flag in red_flags]) if red_flags else "Nessun red flag identificato"}

⚠️ QUANDO RIFERIRE:
- Perdita competenze acquisite
- Ritardo >25% tappe per età
- Red flags presenti
- Preoccupazioni genitori persistenti

🔍 STRUMENTI SCREENING:
- Ages & Stages Questionnaire (ASQ)
- Modified Checklist for Autism (M-CHAT)
- Parents' Evaluation Developmental Status (PEDS)

Riferimento: AAP Bright Futures
CDC Developmental Milestones
"""
        return [types.TextContent(type="text", text=result)]
        
    except Exception as e:
        return [types.TextContent(type="text", text=f"Errore valutazione sviluppo: {str(e)}")] 
