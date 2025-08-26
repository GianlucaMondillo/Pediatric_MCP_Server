"""
Calcoli medici per la pediatria
BSA - Body Surface Area
Fluidi di mantenimento secondo Holiday-Segar
"""
import mcp.types as types
from utils.medical_formulas import (
    calculate_bsa_dubois,
    calculate_bsa_mosteller,
    calculate_holiday_segar_fluids,
    calculate_schwartz_creatinine_clearance,
    calculate_bmi_pediatric,
    calculate_daily_calories_pediatric,
    calculate_normal_bp_pediatric,
    calculate_predicted_height,
    calculate_burned_surface_area,
    calculate_pnfs,
    calculate_pnfs_interpretation,
    calculate_calcium_corrected,
    calculate_bone_mineral_density_zscore_interpretation
)

def get_calculation_tools():
    """Restituisce tutti i tool per i calcoli medici"""
    return [
        types.Tool(
            name="calculate_bsa",
            description="Calcola la superficie corporea (BSA) usando formule di DuBois e Mosteller",
            inputSchema={
                "type": "object",
                "properties": {
                    "weight_kg": {
                        "type": "number",
                        "minimum": 0.1,
                        "maximum": 200,
                        "description": "Peso del paziente in kg"
                    },
                    "height_cm": {
                        "type": "number", 
                        "minimum": 10,
                        "maximum": 250,
                        "description": "Altezza del paziente in cm"
                    }
                },
                "required": ["weight_kg", "height_cm"]
            }
        ),
        
        types.Tool(
            name="calculate_maintenance_fluids",
            description="Calcola i fluidi di mantenimento secondo il metodo Holiday-Segar",
            inputSchema={
                "type": "object",
                "properties": {
                    "weight_kg": {
                        "type": "number",
                        "minimum": 0.5,
                        "maximum": 150,
                        "description": "Peso del paziente in kg"
                    }
                },
                "required": ["weight_kg"]
            }
        ),
        
        types.Tool(
            name="calculate_creatinine_clearance",
            description="Calcola clearance della creatinina pediatrica usando formula di Schwartz",
            inputSchema={
                "type": "object",
                "properties": {
                    "creatinine_mg_dl": {
                        "type": "number",
                        "minimum": 0.1,
                        "maximum": 10,
                        "description": "Creatinina sierica in mg/dL"
                    },
                    "height_cm": {
                        "type": "number",
                        "minimum": 30,
                        "maximum": 200,
                        "description": "Altezza in cm"
                    },
                    "age_years": {
                        "type": "number",
                        "minimum": 0,
                        "maximum": 18,
                        "description": "Età in anni"
                    }
                },
                "required": ["creatinine_mg_dl", "height_cm", "age_years"]
            }
        ),
        
        types.Tool(
            name="calculate_bmi_pediatric",
            description="Calcola BMI pediatrico e valutazione nutrizionale",
            inputSchema={
                "type": "object",
                "properties": {
                    "weight_kg": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 150,
                        "description": "Peso in kg"
                    },
                    "height_cm": {
                        "type": "number",
                        "minimum": 40,
                        "maximum": 200,
                        "description": "Altezza in cm"
                    },
                    "age_months": {
                        "type": "integer",
                        "minimum": 24,
                        "maximum": 216,
                        "description": "Età in mesi (≥24 mesi per BMI)"
                    }
                },
                "required": ["weight_kg", "height_cm", "age_months"]
            }
        ),
        
        types.Tool(
            name="calculate_daily_calories",
            description="Calcola fabbisogno calorico giornaliero pediatrico",
            inputSchema={
                "type": "object",
                "properties": {
                    "weight_kg": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 100,
                        "description": "Peso in kg"
                    },
                    "age_months": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 216,
                        "description": "Età in mesi"
                    }
                },
                "required": ["weight_kg", "age_months"]
            }
        ),
        
        types.Tool(
            name="calculate_normal_blood_pressure",
            description="Calcola valori normali di pressione arteriosa per età pediatrica",
            inputSchema={
                "type": "object",
                "properties": {
                    "age_years": {
                        "type": "number",
                        "minimum": 0,
                        "maximum": 18,
                        "description": "Età in anni"
                    },
                    "height_percentile": {
                        "type": "integer",
                        "minimum": 5,
                        "maximum": 95,
                        "description": "Percentile di altezza (default 50°)"
                    }
                },
                "required": ["age_years"]
            }
        ),
        
        # NUOVI STRUMENTI AGGIUNTI
        
        types.Tool(
            name="calculate_predicted_height",
            description="Calcola l'altezza predetta finale basata sull'altezza dei genitori",
            inputSchema={
                "type": "object",
                "properties": {
                    "father_height_cm": {
                        "type": "number",
                        "minimum": 140,
                        "maximum": 220,
                        "description": "Altezza del padre in cm"
                    },
                    "mother_height_cm": {
                        "type": "number",
                        "minimum": 140,
                        "maximum": 200,
                        "description": "Altezza della madre in cm"
                    },
                    "is_male": {
                        "type": "boolean",
                        "description": "Sesso del bambino: True=maschio, False=femmina"
                    }
                },
                "required": ["father_height_cm", "mother_height_cm", "is_male"]
            }
        ),
        
        types.Tool(
            name="calculate_burned_surface_area",
            description="Calcola la superficie corporea ustionata secondo Lund-Browder modificata per età pediatrica",
            inputSchema={
                "type": "object",
                "properties": {
                    "age_years": {
                        "type": "number",
                        "minimum": 0,
                        "maximum": 18,
                        "description": "Età in anni"
                    },
                    "weight_kg": {
                        "type": "number",
                        "minimum": 0,
                        "maximum": 100,
                        "description": "Peso in kg (opzionale, per calcolo fluidi)"
                    },
                    "head_percent": {
                        "type": "number",
                        "minimum": 0,
                        "maximum": 100,
                        "description": "Percentuale di ustione della testa/collo (0-100%)"
                    },
                    "trunk_percent": {
                        "type": "number",
                        "minimum": 0,
                        "maximum": 100,
                        "description": "Percentuale di ustione del tronco (0-100%)"
                    },
                    "arms_percent": {
                        "type": "number",
                        "minimum": 0,
                        "maximum": 100,
                        "description": "Percentuale di ustione delle braccia (0-100%)"
                    },
                    "hands_percent": {
                        "type": "number",
                        "minimum": 0,
                        "maximum": 100,
                        "description": "Percentuale di ustione delle mani (0-100%)"
                    },
                    "legs_percent": {
                        "type": "number",
                        "minimum": 0,
                        "maximum": 100,
                        "description": "Percentuale di ustione delle gambe (0-100%)"
                    },
                    "feet_percent": {
                        "type": "number",
                        "minimum": 0,
                        "maximum": 100,
                        "description": "Percentuale di ustione dei piedi (0-100%)"
                    },
                    "genitals_percent": {
                        "type": "number",
                        "minimum": 0,
                        "maximum": 100,
                        "description": "Percentuale di ustione dei genitali (0-100%)"
                    }
                },
                "required": ["age_years"]
            }
        ),
        types.Tool(
            name="calculate_anc",
            description="Calcola l'Absolute Neutrophil Count (ANC) da WBC e percentuali neutrofili/bande",
            inputSchema={
                "type": "object",
                "properties": {
                    "wbc_count": {
                        "type": "number",
                        "minimum": 0.1,
                        "description": "Globuli bianchi totali (x10^3/μL)"
                    },
                    "neutrophil_percent": {
                        "type": "number",
                        "minimum": 0,
                        "maximum": 100,
                        "description": "Percentuale di neutrofili segmentati"
                    },
                    "bands_percent": {
                        "type": "number",
                        "minimum": 0,
                        "maximum": 100,
                        "default": 0,
                        "description": "Percentuale di bande (opzionale)"
                    }
                },
                "required": ["wbc_count", "neutrophil_percent"]
            }
        ),
        types.Tool(
            name="calculate_pnfs",
            description="Calcola il Pediatric NAFLD Fibrosis Score (PNFS) per predire il rischio di fibrosi avanzata in steatosi epatica non alcolica pediatrica",
            inputSchema={
                "type": "object",
                "properties": {
                    "alt_iu_l": {
                        "type": "number",
                        "minimum": 5,
                        "maximum": 1000,
                        "description": "ALT in IU/L"
                    },
                    "alkaline_phosphatase_iu_l": {
                        "type": "number",
                        "minimum": 50,
                        "maximum": 1500,
                        "description": "Fosfatasi alcalina in IU/L"
                    },
                    "platelets_k_ul": {
                        "type": "number",
                        "minimum": 20,
                        "maximum": 999,
                        "description": "Piastrine in K/μL"
                    },
                    "ggt_iu_l": {
                        "type": "number",
                        "minimum": 5,
                        "maximum": 1000,
                        "description": "GGT in IU/L"
                    }
                },
                "required": ["alt_iu_l", "alkaline_phosphatase_iu_l", "platelets_k_ul", "ggt_iu_l"]
            }
        ),
        types.Tool(
            name="calculate_pediatric_bone_health",
            description="Calcola parametri di salute ossea pediatrica (calcio corretto, interpretazione DXA)",
            inputSchema={
                "type": "object",
                "properties": {
                    "calcium_total_mg_dl": {
                        "type": "number",
                        "minimum": 5,
                        "maximum": 15,
                        "description": "Calcio sierico totale in mg/dL"
                    },
                    "albumin_g_dl": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 6,
                        "description": "Albumina sierica in g/dL"
                    },
                    "bmd_zscore": {
                        "type": "number",
                        "minimum": -5,
                        "maximum": 5,
                        "description": "Z-score della densità minerale ossea (DXA)"
                    },
                    "age_years": {
                        "type": "number",
                        "minimum": 0,
                        "maximum": 18,
                        "description": "Età in anni"
                    },
                    "vitamin_d_ng_ml": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 100,
                        "description": "Livello di vitamina D (25-OH) in ng/mL"
                    }
                },
                "required": ["calcium_total_mg_dl", "albumin_g_dl", "age_years"]
            }
        )
    ]


def handle_calculation_tools(name: str, arguments: dict):
    """Gestisce i calcoli medici"""
    try:
        if name == "calculate_bsa":
            return _calculate_bsa(arguments)
        elif name == "calculate_maintenance_fluids":
            return _calculate_maintenance_fluids(arguments)
        elif name == "calculate_creatinine_clearance":
            return _calculate_creatinine_clearance(arguments)
        elif name == "calculate_bmi_pediatric":
            return _calculate_bmi_pediatric(arguments)
        elif name == "calculate_daily_calories":
            return _calculate_daily_calories(arguments)
        elif name == "calculate_normal_blood_pressure":
            return _calculate_normal_blood_pressure(arguments)
        elif name == "calculate_predicted_height":
            return _calculate_predicted_height(arguments)
        elif name == "calculate_burned_surface_area":
            return _calculate_burned_surface_area(arguments)
        elif name == "calculate_anc":
            return _calculate_anc(arguments)
        # Nuovi strumenti aggiunti
        elif name == "calculate_pnfs":
            return _calculate_pnfs(arguments)
        elif name == "calculate_pediatric_bone_health":
            return _calculate_pediatric_bone_health(arguments)
        else:
            raise ValueError(f"Calcolo non implementato: {name}")
    except Exception as e:
        return [types.TextContent(type="text", text=f"Errore nel calcolo: {str(e)}")]
def _calculate_bsa(args):
    """Calcola la superficie corporea"""
    weight_kg = args.get('weight_kg')
    height_cm = args.get('height_cm')
    
    # Validazione input
    if weight_kg <= 0 or height_cm <= 0:
        raise ValueError("Peso e altezza devono essere maggiori di 0")
    
    # Calcolo con entrambe le formule
    bsa_dubois = calculate_bsa_dubois(weight_kg, height_cm)
    bsa_mosteller = calculate_bsa_mosteller(weight_kg, height_cm)
    
    # Determinazione quale formula è più appropriata
    if weight_kg < 10:
        recommended = "Mosteller"
        recommended_value = bsa_mosteller
    else:
        recommended = "DuBois" 
        recommended_value = bsa_dubois
    
    result = f"""Calcolo Superficie Corporea (BSA)
==================================
Parametri inseriti:
- Peso: {weight_kg} kg
- Altezza: {height_cm} cm

Risultati:
- Formula DuBois: {bsa_dubois} m²
- Formula Mosteller: {bsa_mosteller} m²

Formula raccomandata: {recommended}
BSA raccomandata: {recommended_value} m²

Note cliniche:
• DuBois: Più accurata per bambini >10 kg
• Mosteller: Più semplice, adatta per tutti i pesi
• Normale BSA pediatrica: 0.25-1.8 m²

Utilizzi clinici:
- Calcolo dosaggi chemioterapici
- Valutazione funzione renale
- Parametri emodinamici (IC, GC)
"""
    return [types.TextContent(type="text", text=result)]

def _calculate_maintenance_fluids(args):
    """Calcola i fluidi di mantenimento Holiday-Segar"""
    weight_kg = args.get('weight_kg')
    
    if weight_kg <= 0:
        raise ValueError("Il peso deve essere maggiore di 0")
    
    fluids = calculate_holiday_segar_fluids(weight_kg)
    
    # Calcolo componenti elettrolitiche standard
    daily_na = round(fluids['daily_ml'] * 0.002)  # ~2 mEq/L
    daily_k = round(fluids['daily_ml'] * 0.002)   # ~2 mEq/L
    
    result = f"""Fluidi di Mantenimento (Holiday-Segar)
=====================================
Peso paziente: {weight_kg} kg

Fluidi di mantenimento:
- Volume giornaliero: {fluids['daily_ml']} ml/24h
- Rate orario: {fluids['hourly_ml']} ml/h
- Rate infusionale: {fluids['rate_ml_h']} ml/h

Elettroliti giornalieri (approssimativi):
- Sodio: {daily_na} mEq/die (~2 mEq/kg/die)
- Potassio: {daily_k} mEq/die (~2 mEq/kg/die)

Metodo Holiday-Segar:
• Primi 10 kg: 100 ml/kg/die
• Kg 11-20: 50 ml/kg/die aggiuntivi
• Oltre 20 kg: 20 ml/kg/die aggiuntivi

Note cliniche:
- Valido per bambini sani senza perdite patologiche
- Aumentare del 10-15% per ogni grado di febbre >38°C
- Ridurre del 20% in caso di oliguria/anuria
- Monitorare bilancio idrico e elettroliti

Soluzione standard: Glucosata 5% + NaCl 0.45% + KCl 20 mEq/L
"""
    return [types.TextContent(type="text", text=result)]

def _calculate_creatinine_clearance(args):
    """Calcola clearance creatinina con formula di Schwartz"""
    creatinine_mg_dl = args.get('creatinine_mg_dl')
    height_cm = args.get('height_cm')
    age_years = args.get('age_years')
    
    clearance = calculate_schwartz_creatinine_clearance(creatinine_mg_dl, height_cm, age_years)
    
    # Valori normali per età
    if age_years < 2:
        normal_range = "50-80 ml/min/1.73m²"
    elif age_years < 13:
        normal_range = "70-120 ml/min/1.73m²"
    else:
        normal_range = "90-130 ml/min/1.73m²"
    
    # Interpretazione
    if clearance < 60:
        interpretation = "RIDOTTA - Insufficienza renale cronica"
    elif clearance < 90:
        interpretation = "LIEVEMENTE RIDOTTA"
    else:
        interpretation = "NORMALE"
    
    result = f"""Clearance Creatinina Pediatrica (Schwartz)
=========================================
Parametri:
- Creatinina sierica: {creatinine_mg_dl} mg/dL
- Altezza: {height_cm} cm  
- Età: {age_years} anni

Clearance calcolata: {clearance} ml/min/1.73m²
Range normale: {normal_range}
Interpretazione: {interpretation}

Formula utilizzata:
- Lattanti (<1 anno): k = 0.45
- Bambini (1-12 anni): k = 0.55  
- Adolescenti maschi (>12 anni): k = 0.7
- CrCl = (k × Altezza) / Creatinina

Classificazione IRC pediatrica:
• Stadio 1: ≥90 ml/min/1.73m² (normale)
• Stadio 2: 60-89 ml/min/1.73m² (lieve riduzione)
• Stadio 3: 30-59 ml/min/1.73m² (moderata riduzione)
• Stadio 4: 15-29 ml/min/1.73m² (severa riduzione)
• Stadio 5: <15 ml/min/1.73m² (insufficienza terminale)
"""
    return [types.TextContent(type="text", text=result)]

def _calculate_bmi_pediatric(args):
    """Calcola BMI pediatrico"""
    weight_kg = args.get('weight_kg')
    height_cm = args.get('height_cm')
    age_months = args.get('age_months')
    
    bmi = calculate_bmi_pediatric(weight_kg, height_cm)
    age_years = age_months / 12
    
    # Classificazione approssimativa (senza curve di crescita precise)
    if age_years < 5:
        if bmi < 14: status = "SOTTOPESO"
        elif bmi < 17: status = "NORMALE"
        elif bmi < 18: status = "SOVRAPPESO"
        else: status = "OBESITÀ"
    else:
        if bmi < 16: status = "SOTTOPESO"
        elif bmi < 22: status = "NORMALE"
        elif bmi < 25: status = "SOVRAPPESO"
        else: status = "OBESITÀ"
    
    result = f"""BMI Pediatrico
==============
Età: {age_years:.1f} anni ({age_months} mesi)
Peso: {weight_kg} kg
Altezza: {height_cm} cm

BMI calcolato: {bmi} kg/m²
Stato nutrizionale: {status} (approssimativo)

Note importanti:
• BMI pediatrico varia con età e sesso
• Utilizzare curve di crescita CDC/WHO per percentili
• Valutazione accurata richiede percentili specifici
• BMI valido da 2 anni in poi

Raccomandazioni per valutazione completa:
- Curve di crescita peso/altezza
- Velocità di crescita
- Valutazione nutrizionale qualitativa
- Anamnesi alimentare

Limiti di questa valutazione:
- Non considera percentili specifici per età/sesso
- Classificazione semplificata
- Richiede interpretazione clinica contestuale
"""
    return [types.TextContent(type="text", text=result)]

def _calculate_daily_calories(args):
    """Calcola fabbisogno calorico giornaliero"""
    weight_kg = args.get('weight_kg')
    age_months = args.get('age_months')
    
    calories_data = calculate_daily_calories_pediatric(weight_kg, age_months)
    age_years = age_months / 12
    
    # Distribuzione macronutrienti
    protein_g = round(weight_kg * 1.2)  # 1.2g/kg proteine
    fat_percent = 30  # 30% grassi
    carb_percent = 50  # 50% carboidrati
    
    result = f"""Fabbisogno Calorico Pediatrico
==============================
Età: {age_years:.1f} anni ({age_months} mesi)
Peso: {weight_kg} kg

Fabbisogno calorico:
- Totale giornaliero: {calories_data['daily_calories']} kcal/die
- Per kg di peso: {calories_data['calories_per_kg']} kcal/kg/die

Distribuzione raccomandata:
- Proteine: {protein_g}g/die (~15% delle calorie)
- Grassi: ~{fat_percent}% delle calorie
- Carboidrati: ~{carb_percent}% delle calorie

Fabbisogno per età:
• 0-12 mesi: 100-120 kcal/kg/die
• 1-3 anni: 100 kcal/kg/die
• 3-10 anni: 70-80 kcal/kg/die
• >10 anni: 50-60 kcal/kg/die

Note cliniche:
- Aumentare del 10-15% in caso di febbre
- Aumentare del 20-50% in malattie acute
- Ridurre in caso di sedentarietà
- Personalizzare per attività fisica e crescita

Monitoraggio:
- Curva di crescita peso/altezza
- Apporti alimentari effettivi
- Attività fisica e sviluppo
"""
    return [types.TextContent(type="text", text=result)]

def _calculate_normal_blood_pressure(args):
    """Calcola pressione arteriosa normale per età"""
    age_years = args.get('age_years')
    height_percentile = args.get('height_percentile', 50)
    
    bp_data = calculate_normal_bp_pediatric(age_years, height_percentile)
    
    result = f"""Pressione Arteriosa Normale Pediatrica
====================================
Età: {age_years} anni
Percentile altezza: {height_percentile}°

Valori normali (approssimativi):
- Sistolica normale: {bp_data['systolic_normal']} mmHg
- Diastolica normale: {bp_data['diastolic_normal']} mmHg

Soglie ipertensione:
- Sistolica 90° percentile: {bp_data['systolic_90th']} mmHg
- Diastolica 90° percentile: {bp_data['diastolic_90th']} mmHg

Classificazione ipertensione pediatrica:
• Normale: <90° percentile per età, sesso, altezza
• Prehipertensione: 90-95° percentile
• Ipertensione stadio 1: 95-99° percentile + 5mmHg
• Ipertensione stadio 2: >99° percentile + 5mmHg

Note importanti:
- Utilizzare bracciale appropriato (40% circonferenza braccio)
- Misurare dopo 5 min riposo, seduti
- Confermare su 3 visite separate
- Considerare variazioni circadiane

Formula semplificata utilizzata:
- Sistolica: 90 + (2 × età in anni)
- Diastolica: 50 + (1.5 × età in anni)

Per valutazione accurata utilizzare:
- Tabelle specifiche per sesso, età, altezza
- Curve di riferimento pediatriche validate
- Monitoraggio pressorio 24h se indicato
"""
    return [types.TextContent(type="text", text=result)]
def _calculate_predicted_height(args):
    """Calcola altezza predetta finale"""
    father_height_cm = args.get('father_height_cm', 0)
    mother_height_cm = args.get('mother_height_cm', 0)
    is_male = args.get('is_male', True)
    
    # Validazione input
    if father_height_cm <= 0 or mother_height_cm <= 0:
        raise ValueError("Altezze dei genitori devono essere maggiori di 0")
    
    # Calcolo altezza predetta
    predicted = calculate_predicted_height(father_height_cm, mother_height_cm, is_male)
    
    # Intervallo di confidenza (±8.5 cm)
    lower_range = round(predicted - 8.5, 1)
    upper_range = round(predicted + 8.5, 1)
    
    result = f"""Altezza Predetta Finale
=====================
Dati genitori:
- Altezza padre: {father_height_cm} cm
- Altezza madre: {mother_height_cm} cm
- Sesso bambino: {'Maschio' if is_male else 'Femmina'}

Risultati:
- Altezza predetta: {predicted} cm
- Range di confidenza: {lower_range} - {upper_range} cm

Formula utilizzata:
- Maschi: [(altezza padre + altezza madre + 13) / 2] ± 8.5 cm
- Femmine: [(altezza padre + altezza madre - 13) / 2] ± 8.5 cm

Note cliniche:
- Predizione basata sul potenziale genetico
- Accuratezza ±8.5 cm nel 95% dei casi
- Non considera fattori ambientali o patologie
- Utile per valutare crescita in relazione al target genetico
- Non utilizzare in presenza di patologie endocrine

Fattori che possono influenzare:
- Stato nutrizionale
- Malattie croniche
- Pubertà precoce o ritardata
- Fattori ormonali
"""
    return [types.TextContent(type="text", text=result)]

def _calculate_burned_surface_area(args):
    """Calcola superficie corporea ustionata"""
    age_years = args.get('age_years', 0)
    areas = {
        'head': args.get('head_percent', 0),
        'trunk': args.get('trunk_percent', 0),
        'arms': args.get('arms_percent', 0),
        'hands': args.get('hands_percent', 0),
        'legs': args.get('legs_percent', 0),
        'feet': args.get('feet_percent', 0),
        'genitals': args.get('genitals_percent', 0)
    }
    
    # Calcolo superficie ustionata
    total_bsa = calculate_burned_surface_area(age_years, areas)
    
    # Fabbisogno idrico (formula di Parkland modificata per pediatria)
    weight_kg = args.get('weight_kg', 0)
    fluid_requirement = 0
    fluid_text = "Non calcolabile (peso non fornito)"
    
    if weight_kg > 0:
        if total_bsa > 10:  # Considerare fluidi solo se >10% TBSA
            fluid_requirement = 3 * weight_kg * total_bsa
            first_8h = round(fluid_requirement / 2)
            second_8h = round(first_8h / 2)
            third_8h = round(first_8h / 2)
            fluid_text = f"• Totale 24h: {fluid_requirement} ml\n• Prime 8h: {first_8h} ml\n• Seconde 8h: {second_8h} ml\n• Terze 8h: {third_8h} ml"
    
    result = f"""Valutazione Superficie Corporea Ustionata
======================================
Età: {age_years} anni
TBSA totale: {total_bsa}% della superficie corporea

Aree ustionate:
- Testa/collo: {areas['head']}%
- Tronco: {areas['trunk']}%
- Braccia: {areas['arms']}%
- Mani: {areas['hands']}%
- Gambe: {areas['legs']}%
- Piedi: {areas['feet']}%
- Genitali: {areas['genitals']}%

Fabbisogno idrico (Parkland modificato):
{fluid_text}

Considerazioni cliniche:
- Ustioni >10% TBSA richiedono reidratazione IV
- Ustioni >15% richiedono ricovero
- Formula Parkland pediatrica: 3 ml × kg × %TBSA
- Ustioni >20% aumentano rischio di shock
- Ustioni >30% possono richiedere escarotomie

Criteri di trasferimento a centro ustioni:
- TBSA >10% in età <10 anni
- TBSA >15% in età >10 anni
- Ustioni III grado >5%
- Ustioni a mani, viso, genitali, articolazioni
- Ustioni da corrente elettrica
"""
    return [types.TextContent(type="text", text=result)]
def _calculate_pnfs(args):
    """Calcola Pediatric NAFLD Fibrosis Score (PNFS)"""
    alt_iu_l = args.get('alt_iu_l', 0)
    alkaline_phosphatase_iu_l = args.get('alkaline_phosphatase_iu_l', 0)
    platelets_k_ul = args.get('platelets_k_ul', 0)
    ggt_iu_l = args.get('ggt_iu_l', 0)
    
    # Calcolo PNFS
    pnfs_score = calculate_pnfs(alt_iu_l, alkaline_phosphatase_iu_l, platelets_k_ul, ggt_iu_l)
    interpretation = calculate_pnfs_interpretation(pnfs_score)
    
    result = f"""Pediatric NAFLD Fibrosis Score (PNFS)
====================================
Probabilità di fibrosi avanzata: {pnfs_score}%

Rischio: {interpretation['interpretation']}
Raccomandazione: {interpretation['recommendation']}

Parametri utilizzati:
- ALT: {alt_iu_l} IU/L
- Fosfatasi alcalina: {alkaline_phosphatase_iu_l} IU/L
- Piastrine: {platelets_k_ul} K/μL
- GGT: {ggt_iu_l} IU/L

Interpretazione:
- <30%: Basso rischio di fibrosi avanzata
- 30-60%: Rischio intermedio
- >60%: Alto rischio di fibrosi avanzata

Note cliniche:
- Score validato in popolazione pediatrica con NAFLD confermata da biopsia
- AUROC di 0.74 (95% CI: 0.66, 0.82) per predire fibrosi avanzata
- Significativamente migliore di APRI, NAFLD Fibrosis Score e FIB-4 Index
- Non sostituisce la biopsia epatica che rimane il gold standard
- Utile per identificare pazienti ad alto rischio da candidare a biopsia

NAFLD vs NASH:
- NAFLD (steatosi semplice): Accumulo di grasso epatico senza infiammazione significativa
- NASH (steatoepatite): Steatosi con infiammazione e danno epatocellulare
- La fibrosi avanzata è associata a maggior rischio di progressione a cirrosi
Fonte: Alkhouri et al., 2014
"""
    return [types.TextContent(type="text", text=result)]


def _calculate_pediatric_bone_health(args):
    """Calcola parametri di salute ossea pediatrica"""
    calcium_total_mg_dl = args.get('calcium_total_mg_dl', 0)
    albumin_g_dl = args.get('albumin_g_dl', 0)
    bmd_zscore = args.get('bmd_zscore', None)
    age_years = args.get('age_years', 0)
    vitamin_d_ng_ml = args.get('vitamin_d_ng_ml', None)
    
    # Calcolo calcio corretto
    calcium_corrected = calculate_calcium_corrected(calcium_total_mg_dl, albumin_g_dl)
    
    # Interpretazione calcio
    if calcium_corrected < 8.5:
        calcium_status = "IPOCALCEMIA"
        calcium_note = "Valori bassi, valutare sintomi e cause"
    elif calcium_corrected <= 10.5:
        calcium_status = "NORMOCALCEMIA"
        calcium_note = "Valori nella norma"
    else:
        calcium_status = "IPERCALCEMIA"
        calcium_note = "Valori elevati, valutare cause"
    
    # Interpretazione vitamina D
    vitamin_d_status = ""
    vitamin_d_recommendation = ""
    
    if vitamin_d_ng_ml is not None:
        if vitamin_d_ng_ml < 12:
            vitamin_d_status = "CARENZA SEVERA"
            vitamin_d_recommendation = "Terapia con colecalciferolo 2000-4000 UI/die per 6-8 settimane, poi mantenimento"
        elif vitamin_d_ng_ml < 20:
            vitamin_d_status = "CARENZA"
            vitamin_d_recommendation = "Terapia con colecalciferolo 1000-2000 UI/die per 6-8 settimane"
        elif vitamin_d_ng_ml < 30:
            vitamin_d_status = "INSUFFICIENZA"
            vitamin_d_recommendation = "Supplementazione 600-1000 UI/die"
        else:
            vitamin_d_status = "SUFFICIENZA"
            vitamin_d_recommendation = "Adeguato apporto dietetico, esposizione solare"
    
    # Interpretazione BMD
    bmd_interpretation = ""
    if bmd_zscore is not None:
        bmd_result = calculate_bone_mineral_density_zscore_interpretation(bmd_zscore)
        bmd_interpretation = f"""
BMD Z-score: {bmd_zscore}
Interpretazione: {bmd_result['interpretation']}
Raccomandazione: {bmd_result['recommendation']}

Nota: In età pediatrica, si utilizza il Z-score (non il T-score)
- Z-score ≥ -1: Normale
- Z-score tra -1 e -2: Bassa densità minerale ossea
- Z-score ≤ -2: Densità minerale ossea molto bassa
"""
    
    # Fabbisogno giornaliero di calcio per età
    calcium_rda = 0
    if age_years < 1:
        calcium_rda = 200
    elif age_years < 4:
        calcium_rda = 700
    elif age_years < 9:
        calcium_rda = 1000
    elif age_years < 19:
        calcium_rda = 1300
    
    # Fabbisogno giornaliero di vitamina D per età
    vitamin_d_rda = 0
    if age_years < 1:
        vitamin_d_rda = 400
    else:
        vitamin_d_rda = 600
    
    result = f"""Valutazione Salute Ossea Pediatrica
================================
Età: {age_years} anni

CALCIO:
- Calcio totale: {calcium_total_mg_dl} mg/dL
- Albumina: {albumin_g_dl} g/dL
- Calcio corretto: {calcium_corrected} mg/dL
- Stato calcio: {calcium_status}
- Note: {calcium_note}
- Fabbisogno giornaliero: {calcium_rda} mg/die

{'VITAMINA D:' if vitamin_d_ng_ml is not None else ''}
{f'- Livello: {vitamin_d_ng_ml} ng/mL' if vitamin_d_ng_ml is not None else ''}
{f'- Stato: {vitamin_d_status}' if vitamin_d_ng_ml is not None else ''}
{f'- Raccomandazione: {vitamin_d_recommendation}' if vitamin_d_ng_ml is not None else ''}
- Fabbisogno giornaliero: {vitamin_d_rda} UI/die

{bmd_interpretation if bmd_zscore is not None else ''}

Note cliniche:
- Valori di riferimento calcio corretto: 8.5-10.5 mg/dL
- Correzione calcio per albumina: Calcio totale + 0.8 × (4 - Albumina)
- Valori di riferimento vitamina D (25-OH):
  * <12 ng/mL: Carenza severa
  * 12-20 ng/mL: Carenza
  * 20-30 ng/mL: Insufficienza
  * >30 ng/mL: Sufficienza

Raccomandazioni generali:
- Dieta ricca di calcio (latticini, verdure a foglia verde, legumi)
- Attività fisica regolare con carico (corsa, salto)
- Adeguata esposizione solare
- Evitare fumo passivo e attivo
- Limitare bevande gassate e caffeina

Screening in bambini a rischio:
- Malassorbimento intestinale
- Terapia steroidea cronica
- Malattie infiammatorie croniche
- Disordini endocrini
- Immobilizzazione prolungata
"""
    return [types.TextContent(type="text", text=result)]
    
