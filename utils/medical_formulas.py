"""
Formule mediche reali utilizzate nella pratica clinica pediatrica
"""
import math
def calculate_pas_asthma_interpretation(total_score: int) -> dict:
    """
    Interpreta il Pediatric Asthma Score
    
    Args:
        total_score: Punteggio PAS totale (0-15)
        
    Returns:
        Dict con severità e raccomandazione
    """
    if total_score <= 4:
        return {
            'severity': 'LIEVE',
            'recommendation': 'Beta-agonisti a breve durata d\'azione (SABA), considerare dimissione'
        }
    elif total_score <= 7:
        return {
            'severity': 'MODERATA',
            'recommendation': 'SABA ogni 1-2 ore, considerare steroidi, monitoraggio per 2-4 ore'
        }
    elif total_score <= 11:
        return {
            'severity': 'SEVERA',
            'recommendation': 'SABA continui, steroidi sistemici, considerare Mg solfato, valutare ricovero'
        }
    else:
        return {
            'severity': 'CRITICA',
            'recommendation': 'Trattamento intensivo, SABA+anticolinergici continui, steroidi IV, possibile intubazione'
        }

def calculate_pass_asthma_interpretation(total_score: int) -> dict:
    """
    Interpreta il Pediatric Asthma Severity Score (PASS)
    
    Args:
        total_score: Punteggio PASS totale (0-6)
        
    Returns:
        Dict con severità e raccomandazione
    """
    if total_score <= 2:
        return {
            'severity': 'LIEVE',
            'recommendation': 'Considerare dimissione con follow-up, SABA al bisogno'
        }
    elif total_score <= 4:
        return {
            'severity': 'MODERATA',
            'recommendation': 'Continuare trattamento in PS, rivalutare dopo 1-2 ore'
        }
    else:
        return {
            'severity': 'SEVERA',
            'recommendation': 'Trattamento intensivo, possibile ricovero in terapia intensiva'
        }

def calculate_bacterial_meningitis_score_interpretation(total_score: int) -> dict:
    """
    Interpreta il Bacterial Meningitis Score for Children
    
    Args:
        total_score: Punteggio totale (0-6)
        
    Returns:
        Dict con rischio e raccomandazione
    """
    if total_score == 0:
        return {
            'risk': 'MOLTO BASSO (<0.1%)',
            'recommendation': 'Considerare dimissione con follow-up, basso rischio di meningite batterica'
        }
    elif total_score == 1:
        return {
            'risk': 'BASSO (0.4-2.5%)',
            'recommendation': 'Valutare attentamente, considerare osservazione o ulteriori indagini'
        }
    else:
        return {
            'risk': 'ALTO (>8%)',
            'recommendation': 'Ricovero e terapia antibiotica empirica raccomandata'
        }

def calculate_kocher_criteria_interpretation(total_score: int) -> dict:
    """
    Interpreta i Kocher Criteria per artrite settica dell'anca
    
    Args:
        total_score: Numero di criteri positivi (0-4)
        
    Returns:
        Dict con probabilità e raccomandazione
    """
    if total_score == 0:
        return {
            'probability': '<0.2%',
            'recommendation': 'Artrite settica estremamente improbabile. Considerare altre diagnosi.'
        }
    elif total_score == 1:
        return {
            'probability': '3%',
            'recommendation': 'Bassa probabilità. Considerare osservazione o ulteriori indagini.'
        }
    elif total_score == 2:
        return {
            'probability': '40%',
            'recommendation': 'Probabilità intermedia. Considerare aspirazione articolare.'
        }
    elif total_score == 3:
        return {
            'probability': '93%',
            'recommendation': 'Alta probabilità. Aspirazione articolare raccomandata.'
        }
    else:  # total_score == 4
        return {
            'probability': '99%',
            'recommendation': 'Probabilità molto alta. Aspirazione articolare e intervento fortemente raccomandati.'
        }

def calculate_kawasaki_criteria_interpretation(has_fever: bool, criteria_count: int) -> dict:
    """
    Interpreta i criteri diagnostici per la malattia di Kawasaki
    
    Args:
        has_fever: Presenza di febbre per ≥5 giorni
        criteria_count: Numero di criteri clinici positivi (0-5)
        
    Returns:
        Dict con diagnosi e raccomandazione
    """
    if not has_fever:
        return {
            'diagnosis': 'CRITERI NON SODDISFATTI',
            'recommendation': 'Malattia di Kawasaki improbabile. La febbre per ≥5 giorni è un criterio essenziale.'
        }
    elif criteria_count >= 4:
        return {
            'diagnosis': 'KAWASAKI CLASSICO',
            'recommendation': 'Diagnosi di Kawasaki classico. Iniziare IVIG e ASA ad alte dosi entro 10 giorni dall\'esordio.'
        }
    elif 2 <= criteria_count <= 3:
        return {
            'diagnosis': 'POSSIBILE KAWASAKI INCOMPLETO',
            'recommendation': 'Sospetto Kawasaki incompleto. Valutare criteri di laboratorio e ecocardiografia.'
        }
    else:
        return {
            'diagnosis': 'CRITERI NON SODDISFATTI',
            'recommendation': 'Malattia di Kawasaki improbabile. Considerare diagnosi alternative.'
        }

def calculate_bops_interpretation(total_score: int) -> dict:
    """
    Interpreta il Behavioral Observational Pain Scale (BOPS)
    
    Args:
        total_score: Punteggio BOPS totale (0-6)
        
    Returns:
        Dict con intensità dolore e raccomandazione
    """
    if total_score <= 1:
        return {
            'pain_level': 'NESSUN DOLORE',
            'recommendation': 'Nessun intervento analgesico richiesto'
        }
    elif total_score <= 3:
        return {
            'pain_level': 'DOLORE LIEVE',
            'recommendation': 'Considerare analgesia non farmacologica o paracetamolo'
        }
    elif total_score <= 4:
        return {
            'pain_level': 'DOLORE MODERATO',
            'recommendation': 'Somministrare analgesici non oppioidi'
        }
    else:
        return {
            'pain_level': 'DOLORE SEVERO',
            'recommendation': 'Somministrare analgesici oppioidi, valutare cause del dolore'
        }

def calculate_pnfs(alt_iu_l: float, alkaline_phosphatase_iu_l: float, platelets_k_ul: float, ggt_iu_l: float) -> float:
    """
    Calcola il Pediatric NAFLD Fibrosis Score (PNFS)
    Formula: z = 1.1 + (0.34 × sqrt(ALT)) + (0.002 × alkaline phosphatase) - (1.1 × log(platelets)) - (0.02 × GGT)
    Convertito in probabilità: p = 100 × exp(z) / [1 + exp(z)]
    
    Args:
        alt_iu_l: ALT in IU/L
        alkaline_phosphatase_iu_l: Fosfatasi alcalina in IU/L
        platelets_k_ul: Piastrine in K/μL
        ggt_iu_l: GGT in IU/L
    
    Returns:
        Probabilità di fibrosi avanzata (0-100%)
    """
    import math
    
    # Calcolo del valore z
    z = (1.1 + (0.34 * math.sqrt(alt_iu_l)) + (0.002 * alkaline_phosphatase_iu_l) - 
         (1.1 * math.log10(platelets_k_ul)) - (0.02 * ggt_iu_l))
    
    # Conversione in probabilità (0-100%)
    probability = 100 * math.exp(z) / (1 + math.exp(z))
    
    return round(probability, 1)

def calculate_pnfs_interpretation(pnfs_score: float) -> dict:
    """
    Interpreta il Pediatric NAFLD Fibrosis Score (PNFS)
    
    Args:
        pnfs_score: Probabilità PNFS (0-100%)
        
    Returns:
        Dict con interpretazione e raccomandazione
    """
    if pnfs_score < 30.0:
        return {
            'interpretation': 'BASSO RISCHIO FIBROSI AVANZATA',
            'recommendation': 'Monitoraggio standard, modifiche stile di vita, controllo ogni 6-12 mesi'
        }
    elif pnfs_score <= 60.0:
        return {
            'interpretation': 'RISCHIO INTERMEDIO',
            'recommendation': 'Monitoraggio più frequente, elastografia, controllo ogni 3-6 mesi'
        }
    else:
        return {
            'interpretation': 'ALTO RISCHIO FIBROSI AVANZATA',
            'recommendation': 'Considerare biopsia epatica, valutazione specialistica epatologica'
        }
def calculate_calcium_corrected(calcium_total_mg_dl: float, albumin_g_dl: float) -> float:
    """
    Calcola il calcio corretto per albumina
    Formula: Calcio totale + 0.8 × (4 - Albumina)
    
    Args:
        calcium_total_mg_dl: Calcio totale in mg/dL
        albumin_g_dl: Albumina in g/dL
    
    Returns:
        Calcio corretto in mg/dL
    """
    if albumin_g_dl >= 4.0:
        return calcium_total_mg_dl
    
    calcium_corrected = calcium_total_mg_dl + 0.8 * (4.0 - albumin_g_dl)
    return round(calcium_corrected, 2)

def calculate_bone_mineral_density_zscore_interpretation(bmd_zscore: float) -> dict:
    """
    Interpreta Z-score della densità minerale ossea in età pediatrica
    
    Args:
        bmd_zscore: Z-score della densità minerale ossea
        
    Returns:
        Dict con interpretazione e raccomandazione
    """
    if bmd_zscore >= -1.0:
        return {
            'interpretation': 'NORMALE',
            'recommendation': 'Nessuna azione specifica richiesta. Mantenere adeguato apporto di calcio e vitamina D.'
        }
    elif bmd_zscore >= -2.0:
        return {
            'interpretation': 'BASSA DENSITÀ MINERALE OSSEA',
            'recommendation': 'Ottimizzare apporto di calcio, vitamina D, attività fisica. Rivalutare in 12 mesi.'
        }
    else:
        return {
            'interpretation': 'DENSITÀ MINERALE OSSEA MOLTO BASSA',
            'recommendation': 'Valutazione endocrinologica, considerare intervento farmacologico, ricerca cause secondarie.'
        }
def calculate_bsa_dubois(weight_kg: float, height_cm: float) -> float:
    """
    Calcola la superficie corporea usando la formula di DuBois
    Formula: BSA (m²) = 0.007184 × Weight(kg)^0.425 × Height(cm)^0.725
    
    Args:
        weight_kg: Peso in kg
        height_cm: Altezza in cm
    
    Returns:
        BSA in m²
    """
    if weight_kg <= 0 or height_cm <= 0:
        raise ValueError("Peso e altezza devono essere maggiori di 0")
    
    bsa = 0.007184 * (weight_kg ** 0.425) * (height_cm ** 0.725)
    return round(bsa, 2)

def calculate_bsa_mosteller(weight_kg: float, height_cm: float) -> float:
    """
    Calcola la superficie corporea usando la formula di Mosteller
    Formula: BSA (m²) = √(Weight(kg) × Height(cm) / 3600)
    
    Args:
        weight_kg: Peso in kg
        height_cm: Altezza in cm
    
    Returns:
        BSA in m²
    """
    if weight_kg <= 0 or height_cm <= 0:
        raise ValueError("Peso e altezza devono essere maggiori di 0")
    
    bsa = math.sqrt((weight_kg * height_cm) / 3600)
    return round(bsa, 2)

def calculate_holiday_segar_fluids(weight_kg: float) -> dict:
    """
    Calcola i fluidi di mantenimento secondo Holiday-Segar
    
    Regole:
    - Primi 10 kg: 100 ml/kg/die
    - Successivi 10 kg (11-20 kg): 50 ml/kg/die  
    - Oltre 20 kg: 20 ml/kg/die
    
    Args:
        weight_kg: Peso in kg
    
    Returns:
        Dict con ml/die, ml/ora e rate infusionale
    """
    if weight_kg <= 0:
        raise ValueError("Il peso deve essere maggiore di 0")
    
    # Calcolo fluidi giornalieri
    if weight_kg <= 10:
        daily_ml = weight_kg * 100
    elif weight_kg <= 20:
        daily_ml = (10 * 100) + ((weight_kg - 10) * 50)
    else:
        daily_ml = (10 * 100) + (10 * 50) + ((weight_kg - 20) * 20)
    
    # Calcolo rate orario
    hourly_ml = daily_ml / 24
    
    return {
        'daily_ml': round(daily_ml),
        'hourly_ml': round(hourly_ml, 1),
        'rate_ml_h': round(hourly_ml, 1)
    }

def calculate_pews_interpretation(total_score: int, has_bradycardia: bool = False) -> dict:
    """Interpreta PEWS con considerazione specifica per bradicardia"""
    if has_bradycardia or total_score >= 7:
        return {
            'risk_level': 'CRITICO',
            'action': 'Intervento immediato - Contattare rianimazione/MET team'
        }
    elif total_score >= 5:
        return {
            'risk_level': 'ALTO',
            'action': 'Considerare terapia intensiva - Monitoraggio continuo - Consulenza medica urgente'
        }
    elif total_score >= 3:
        return {
            'risk_level': 'MODERATO',
            'action': 'Aumentare frequenza monitoraggio ogni 2 ore - Consulenza medica'
        }
    else:
        return {
            'risk_level': 'BASSO',
            'action': 'Monitoraggio standard ogni 4-6 ore'
        }
def calculate_pas_interpretation(total_score: int) -> dict:
    """
    Interpreta il punteggio PAS (Pediatric Appendicitis Score)
    
    Args:
        total_score: Punteggio PAS totale (0-10)
        
    Returns:
        Dict con probabilità di appendicite e raccomandazione
    """
    if total_score <= 2:
        return {
            'probability': 'BASSA (2%)',
            'recommendation': 'Appendicite improbabile - Considerare diagnosi alternative'
        }
    elif total_score <= 5:
        return {
            'probability': 'INTERMEDIA (15-25%)',
            'recommendation': 'Osservazione clinica - Rivalutazione in 6-12 ore'
        }
    elif total_score <= 7:
        return {
            'probability': 'ALTA (70-80%)',
            'recommendation': 'Forte sospetto appendicite - Consultazione chirurgica'
        }
    else:
        return {
            'probability': 'MOLTO ALTA (95%+)',
            'recommendation': 'Appendicite molto probabile - Preparazione per intervento'
        }

def calculate_apgar_interpretation(total_score: int) -> dict:
    """
    Interpreta il punteggio APGAR
    
    Args:
        total_score: Punteggio APGAR totale (0-10)
        
    Returns:
        Dict con condizione del neonato e azioni
    """
    if total_score >= 8:
        return {
            'condition': 'NORMALE',
            'action': 'Nessun intervento necessario - Cure di routine'
        }
    elif total_score >= 4:
        return {
            'condition': 'MODERATAMENTE DEPRESSO',
            'action': 'Stimolazione, aspirazione, ossigeno se necessario'
        }
    else:
        return {
            'condition': 'SEVERAMENTE DEPRESSO',
            'action': 'Rianimazione immediata - Intubazione e ventilazione'
        }

def calculate_gcs_pediatric_interpretation(total_score: int) -> dict:
    """
    Interpreta Glasgow Coma Scale pediatrica
    """
    if total_score >= 13:
        return {'severity': 'LIEVE', 'prognosis': 'Buona', 'action': 'Osservazione clinica'}
    elif total_score >= 9:
        return {'severity': 'MODERATA', 'prognosis': 'Riservata', 'action': 'Monitoraggio intensivo'}
    else:
        return {'severity': 'SEVERA', 'prognosis': 'Grave', 'action': 'Terapia intensiva immediata'}

def calculate_schwartz_creatinine_clearance(creatinine_mg_dl: float, height_cm: float, age_years: float) -> float:
    """
    Calcola clearance creatinina pediatrica con formula di Schwartz
    Formula: CrCl = (k × Height) / Creatinina sierica
    k = 0.45 per lattanti, 0.55 per bambini, 0.7 per adolescenti maschi
    """
    if age_years < 1:
        k = 0.45
    elif age_years < 13:
        k = 0.55
    else:
        k = 0.7
    
    clearance = (k * height_cm) / creatinine_mg_dl
    return round(clearance, 1)

def calculate_bmi_pediatric(weight_kg: float, height_cm: float) -> float:
    """
    Calcola BMI pediatrico
    """
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)

def calculate_daily_calories_pediatric(weight_kg: float, age_months: int) -> dict:
    """
    Calcola fabbisogno calorico giornaliero pediatrico
    """
    if age_months < 12:
        # Lattanti: 100-120 kcal/kg/die
        calories = weight_kg * 110
    elif age_months < 36:
        # 1-3 anni: 100 kcal/kg/die
        calories = weight_kg * 100
    elif age_months < 120:
        # 3-10 anni: 70-80 kcal/kg/die
        calories = weight_kg * 75
    else:
        # >10 anni: 50-60 kcal/kg/die
        calories = weight_kg * 55
    
    return {
        'daily_calories': round(calories),
        'calories_per_kg': round(calories/weight_kg, 1)
    }

def calculate_normal_bp_pediatric(age_years: float, height_percentile: int = 50) -> dict:
    """
    Calcola pressione arteriosa normale per età (semplificata)
    """
    if age_years < 1:
        systolic = 70 + (2 * age_years * 12)  # mesi
        diastolic = 40
    else:
        systolic = 90 + (2 * age_years)
        diastolic = 50 + (1.5 * age_years)
    
    return {
        'systolic_normal': round(systolic),
        'diastolic_normal': round(diastolic),
        'systolic_90th': round(systolic + 10),
        'diastolic_90th': round(diastolic + 10)
    }
def calculate_pediatric_trauma_score(weight_kg: float, systolic_bp: int, conscious: bool, 
                            open_wound: bool, fracture: bool, cutaneous: bool) -> int:
    """
    Calcola Pediatric Trauma Score (PTS)
    
    Parametri (ciascuno +2, +1 o -1):
    - Peso: >20kg (+2), 10-20kg (+1), <10kg (-1)
    - Pressione sistolica: >90mmHg (+2), 50-90mmHg (+1), <50mmHg (-1)
    - Stato di coscienza: Sveglio (+2), Obnubilato (+1), Coma (-1)
    - Ferita: Nessuna (+2), Minore (+1), Maggiore o penetrante (-1)
    - Frattura: Nessuna (+2), Chiusa (+1), Aperta o multipla (-1)
    - Cute: Intatta (+2), Contusione (+1), Perdita di sostanza (-1)
    
    Interpretazione:
    >8: Rischio minimo
    6-8: Potenzialmente pericoloso per la vita
    0-5: Pericoloso per la vita
    <0: Estremo pericolo per la vita
    """
    score = 0
    
    # Peso
    if weight_kg > 20:
        score += 2
    elif weight_kg >= 10:
        score += 1
    else:
        score -= 1
    
    # Pressione sistolica
    if systolic_bp > 90:
        score += 2
    elif systolic_bp >= 50:
        score += 1
    else:
        score -= 1
    
    # Stato di coscienza
    if conscious:
        score += 2
    else:
        score -= 1
    
    # Ferita
    if not open_wound:
        score += 2
    else:
        score -= 1
    
    # Frattura
    if not fracture:
        score += 2
    else:
        score -= 1
    
    # Cute
    if cutaneous:
        score += 2
    else:
        score -= 1
    
    return score

def calculate_catch_score(vomiting: bool, headache: bool, gcsscore: int, 
                         suspected_skull_fracture: bool, dangerous_mechanism: bool) -> int:
    """
    Calcola CATCH (Canadian Assessment of Tomography for Childhood Head injury)
    
    Parametri (1 punto ciascuno):
    - GCS < 15 a 2 ore dal trauma
    - Sospetta frattura cranica aperta/depressa
    - Storia di vomito ≥ 3 episodi
    - Segni di frattura della base cranica
    - Meccanismo traumatico grave
    - Cefalea grave

    Score ≥ 1 indica alto rischio, raccomandata TC encefalo
    """
    score = 0
    
    if gcsscore < 15:
        score += 1
    
    if suspected_skull_fracture:
        score += 1
    
    if vomiting:
        score += 1
    
    if dangerous_mechanism:
        score += 1
    
    if headache:
        score += 1
    
    return score

def calculate_westley_croup_score(stridor: int, retraction: int, air_entry: int, 
                               cyanosis: int, consciousness: int) -> dict:
    """
    Calcola Westley Croup Score
    
    Parametri:
    - Stridore inspiratorio (0-2)
    - Retrazioni (0-3)
    - Ingresso d'aria (0-2)
    - Cianosi (0-4)
    - Livello di coscienza (0-5)
    
    Interpretazione:
    ≤2: Croup lieve
    3-5: Croup moderato
    6-11: Croup severo
    ≥12: Imminente insufficienza respiratoria
    """
    total_score = stridor + retraction + air_entry + cyanosis + consciousness
    
    if total_score <= 2:
        severity = "LIEVE"
        management = "Gestione domiciliare - Steroidi singola dose"
    elif total_score <= 5:
        severity = "MODERATO"
        management = "Osservazione ospedaliera - Steroidi e adrenalina"
    elif total_score <= 11:
        severity = "SEVERO"
        management = "Ricovero urgente - Trattamento intensivo"
    else:
        severity = "CRITICO"
        management = "Potenziale intubazione - Terapia intensiva"
    
    return {
        'severity': severity,
        'management': management
    }

def calculate_predicted_height(father_height_cm: float, mother_height_cm: float, 
                             is_male: bool) -> float:
    """
    Calcola l'altezza predetta finale basata sull'altezza dei genitori
    
    Formula:
    - Maschi: [(altezza padre + altezza madre + 13) / 2] ± 8.5 cm
    - Femmine: [(altezza padre + altezza madre - 13) / 2] ± 8.5 cm
    
    Args:
        father_height_cm: Altezza del padre in cm
        mother_height_cm: Altezza della madre in cm
        is_male: True se il bambino è maschio, False se femmina
    
    Returns:
        Altezza predetta in cm
    """
    if is_male:
        predicted = (father_height_cm + mother_height_cm + 13) / 2
    else:
        predicted = (father_height_cm + mother_height_cm - 13) / 2
    
    return round(predicted, 1)

def calculate_burned_surface_area(age_years: float, areas: dict) -> float:
    """
    Calcola la superficie corporea ustionata usando la tabella di Lund-Browder
    
    Args:
        age_years: Età in anni
        areas: Dict con percentuali di ustione per area corporea
            Chiavi: 'head', 'trunk', 'arms', 'hands', 'legs', 'feet', 'genitals'
    
    Returns:
        Percentuale totale di superficie corporea ustionata
    """
    # Coefficienti per età
    if age_years <= 1:
        head_coef = 0.19
        legs_coef = 0.13
    elif age_years <= 4:
        head_coef = 0.17
        legs_coef = 0.15
    elif age_years <= 9:
        head_coef = 0.13
        legs_coef = 0.16
    else:
        head_coef = 0.07
        legs_coef = 0.18
    
    # Percentuali standard
    trunk_coef = 0.32  # anteriore (13%) + posteriore (13%) + collo (2%) + glutei (2.5%) + genitali (1%)
    arms_coef = 0.14   # 2 braccia
    hands_coef = 0.05  # 2 mani
    feet_coef = 0.07   # 2 piedi
    
    # Calcolo superficie ustionata
    total_bsa = 0
    
    if 'head' in areas and areas['head']:
        total_bsa += head_coef * (areas['head'] / 100)
    if 'trunk' in areas and areas['trunk']:
        total_bsa += trunk_coef * (areas['trunk'] / 100)
    if 'arms' in areas and areas['arms']:
        total_bsa += arms_coef * (areas['arms'] / 100)
    if 'hands' in areas and areas['hands']:
        total_bsa += hands_coef * (areas['hands'] / 100)
    if 'legs' in areas and areas['legs']:
        total_bsa += legs_coef * (areas['legs'] / 100)
    if 'feet' in areas and areas['feet']:
        total_bsa += feet_coef * (areas['feet'] / 100)
    if 'genitals' in areas and areas['genitals']:
        total_bsa += 0.01 * (areas['genitals'] / 100)
    
    return round(total_bsa * 100, 1)

def calculate_centor_score_pediatric(age_years: float, exudate: bool, tender_nodes: bool,
                               fever: bool, cough: bool) -> dict:
    """
    Calcola Centor Score modificato per faringite streptococcica in età pediatrica
    
    Criteri:
    - Essudato tonsillare: +1
    - Linfoadenopatia cervicale anteriore dolente: +1
    - Febbre >38°C: +1
    - Assenza di tosse: +1
    - Età 3-14 anni: +1 (fattore aggiuntivo per pediatria)
    
    Returns:
        Dict con punteggio, probabilità e raccomandazione
    """
    score = 0
    
    if exudate:
        score += 1
    if tender_nodes:
        score += 1
    if fever:
        score += 1
    if not cough:
        score += 1
    if 3 <= age_years <= 14:
        score += 1
    
    # Interpretazione
    if score <= 1:
        probability = "BASSA (<10%)"
        recommendation = "No test rapido, no antibiotici"
    elif score == 2:
        probability = "INTERMEDIA-BASSA (10-17%)"
        recommendation = "Considerare test rapido, antibiotici solo se positivo"
    elif score == 3:
        probability = "INTERMEDIA-ALTA (30-35%)"
        recommendation = "Test rapido, antibiotici se positivo"
    else:
        probability = "ALTA (>50%)"
        recommendation = "Test rapido o trattamento empirico se test non disponibile"
    
    return {
        'score': score,
        'probability': probability,
        'recommendation': recommendation
    }

def calculate_wells_score_pediatric(provoked_dvt: bool, alternative_diagnosis: bool, 
                           swelling: bool, unilateral_tenderness: bool, 
                           swelling_thigh_calf: bool, unilateral_pitting: bool,
                           bedridden: bool, active_cancer: bool, previous_dvt: bool) -> dict:
    """
    Calcola Wells Score pediatrico per TVP (Trombosi Venosa Profonda)
    
    Criteri:
    - TVP provocata: +1
    - Diagnosi alternativa possibile: -2
    - Gonfiore dell'intero arto: +1
    - Dolorabilità localizzata lungo sistema venoso profondo: +1
    - Gonfiore polpaccio >3cm rispetto controlaterale: +1
    - Edema improntabile monolaterale: +1
    - Allettamento recente >3 giorni: +1
    - Cancro attivo: +1
    - Precedente TVP: +1
    
    Returns:
        Dict con punteggio, probabilità e raccomandazione
    """
    score = 0
    
    if provoked_dvt:
        score += 1
    if alternative_diagnosis:
        score -= 2
    if swelling:
        score += 1
    if unilateral_tenderness:
        score += 1
    if swelling_thigh_calf:
        score += 1
    if unilateral_pitting:
        score += 1
    if bedridden:
        score += 1
    if active_cancer:
        score += 1
    if previous_dvt:
        score += 1
    
    # Interpretazione
    if score >= 2:
        probability = "ALTA (>75%)"
        recommendation = "Ecografia + anticoagulante mentre si attende"
    elif score == 1:
        probability = "MODERATA (~17%)"
        recommendation = "Ecografia, considerare D-dimero"
    else:
        probability = "BASSA (<5%)"
        recommendation = "D-dimero, considerare stop se negativo"
    
    return {
        'score': score,
        'probability': probability,
        'recommendation': recommendation
    }
def calculate_anc(wbc_count: float, neutrophil_percent: float, bands_percent: float = 0.0) -> int:
    """
    Calcola il conteggio assoluto dei neutrofili (ANC) in cellule/μL.
    
    Args:
        wbc_count: Conteggio globuli bianchi in migliaia/μL
        neutrophil_percent: Percentuale di neutrofili segmentati (0-100)
        bands_percent: Percentuale di bande (opzionale, 0-100)
    
    Returns:
        ANC: Conteggio assoluto dei neutrofili in cellule/μL
    """
    if not (0 <= neutrophil_percent <= 100 and 0 <= bands_percent <= 100):
        raise ValueError("Le percentuali devono essere tra 0 e 100")
    anc = wbc_count * (neutrophil_percent + bands_percent) / 100 * 1000
    return int(round(anc))

def calculate_pas_asthma_interpretation(total_score: int) -> dict:
    """
    Interpreta il Pediatric Asthma Score
    
    Args:
        total_score: Punteggio PAS totale (0-15)
        
    Returns:
        Dict con severità e raccomandazione
    """
    if total_score <= 4:
        return {
            'severity': 'LIEVE',
            'recommendation': 'Beta-agonisti a breve durata d\'azione (SABA), considerare dimissione'
        }
    elif total_score <= 7:
        return {
            'severity': 'MODERATA',
            'recommendation': 'SABA ogni 1-2 ore, considerare steroidi, monitoraggio per 2-4 ore'
        }
    elif total_score <= 11:
        return {
            'severity': 'SEVERA',
            'recommendation': 'SABA continui, steroidi sistemici, considerare Mg solfato, valutare ricovero'
        }
    else:
        return {
            'severity': 'CRITICA',
            'recommendation': 'Trattamento intensivo, SABA+anticolinergici continui, steroidi IV, possibile intubazione'
        }

def calculate_pass_asthma_interpretation(total_score: int) -> dict:
    """
    Interpreta il Pediatric Asthma Severity Score (PASS)
    
    Args:
        total_score: Punteggio PASS totale (0-6)
        
    Returns:
        Dict con severità e raccomandazione
    """
    if total_score <= 2:
        return {
            'severity': 'LIEVE',
            'recommendation': 'Considerare dimissione con follow-up, SABA al bisogno'
        }
    elif total_score <= 4:
        return {
            'severity': 'MODERATA',
            'recommendation': 'Continuare trattamento in PS, rivalutare dopo 1-2 ore'
        }
    else:
        return {
            'severity': 'SEVERA',
            'recommendation': 'Trattamento intensivo, possibile ricovero in terapia intensiva'
        }
    
def calculate_bacterial_meningitis_score_interpretation(total_score: int) -> dict:
    """
    Interpreta il Bacterial Meningitis Score for Children
    
    Args:
        total_score: Punteggio totale (0-6)
        
    Returns:
        Dict con rischio e raccomandazione
    """
    if total_score == 0:
        return {
            'risk': 'MOLTO BASSO (<0.1%)',
            'recommendation': 'Considerare dimissione con follow-up, basso rischio di meningite batterica'
        }
    elif total_score == 1:
        return {
            'risk': 'BASSO (0.4-2.5%)',
            'recommendation': 'Valutare attentamente, considerare osservazione o ulteriori indagini'
        }
    else:
        return {
            'risk': 'ALTO (>8%)',
            'recommendation': 'Ricovero e terapia antibiotica empirica raccomandata'
        }
    
def calculate_kocher_criteria_interpretation(total_score: int) -> dict:
    """
    Interpreta i Kocher Criteria per artrite settica dell'anca
    
    Args:
        total_score: Numero di criteri positivi (0-4)
        
    Returns:
        Dict con probabilità e raccomandazione
    """
    if total_score == 0:
        return {
            'probability': '<0.2%',
            'recommendation': 'Artrite settica estremamente improbabile. Considerare altre diagnosi.'
        }
    elif total_score == 1:
        return {
            'probability': '3%',
            'recommendation': 'Bassa probabilità. Considerare osservazione o ulteriori indagini.'
        }
    elif total_score == 2:
        return {
            'probability': '40%',
            'recommendation': 'Probabilità intermedia. Considerare aspirazione articolare.'
        }
    elif total_score == 3:
        return {
            'probability': '93%',
            'recommendation': 'Alta probabilità. Aspirazione articolare raccomandata.'
        }
    else:  # total_score == 4
        return {
            'probability': '99%',
            'recommendation': 'Probabilità molto alta. Aspirazione articolare e intervento fortemente raccomandati.'
        }
def calculate_kawasaki_criteria_interpretation(has_fever: bool, criteria_count: int) -> dict:
    """
    Interpreta i criteri diagnostici per la malattia di Kawasaki
    
    Args:
        has_fever: Presenza di febbre per ≥5 giorni
        criteria_count: Numero di criteri clinici positivi (0-5)
        
    Returns:
        Dict con diagnosi e raccomandazione
    """
    if not has_fever:
        return {
            'diagnosis': 'CRITERI NON SODDISFATTI',
            'recommendation': 'Malattia di Kawasaki improbabile. La febbre per ≥5 giorni è un criterio essenziale.'
        }
    elif criteria_count >= 4:
        return {
            'diagnosis': 'KAWASAKI CLASSICO',
            'recommendation': 'Diagnosi di Kawasaki classico. Iniziare IVIG e ASA ad alte dosi entro 10 giorni dall\'esordio.'
        }
    elif 2 <= criteria_count <= 3:
        return {
            'diagnosis': 'POSSIBILE KAWASAKI INCOMPLETO',
            'recommendation': 'Sospetto Kawasaki incompleto. Valutare criteri di laboratorio e ecocardiografia.'
        }
    else:
        return {
            'diagnosis': 'CRITERI NON SODDISFATTI',
            'recommendation': 'Malattia di Kawasaki improbabile. Considerare diagnosi alternative.'
        }
    
def calculate_bops_interpretation(total_score: int) -> dict:
    """Interpreta il Behavioral Observational Pain Scale (BOPS)"""
    if total_score <= 1:
        return {
            'pain_level': 'NESSUN DOLORE',
            'recommendation': 'Nessun intervento analgesico richiesto'
        }
    elif total_score <= 3:
        return {
            'pain_level': 'DOLORE LIEVE',
            'recommendation': 'Considerare analgesia non farmacologica o paracetamolo'
        }
    elif total_score <= 4:
        return {
            'pain_level': 'DOLORE MODERATO',
            'recommendation': 'Somministrare analgesici non oppioidi'
        }
    else:
        return {
            'pain_level': 'DOLORE SEVERO',
            'recommendation': 'Somministrare analgesici oppioidi, valutare cause del dolore'
        }
    
def calculate_pnfs(age_years: float, waist_circumference_cm: float, triglycerides_mg_dl: float, alt_iu_l: float) -> float:
    """
    Calcola il Pediatric NAFLD Fibrosis Score (PNFS)
    Formula: 1.1 + (0.34 × sqrt(ALT)) + (0.002 × Trigliceridi) - (1.1 × Log(età in anni)) 
             + (0.02 × Circonferenza vita)
    
    Args:
        age_years: Età in anni
        waist_circumference_cm: Circonferenza vita in cm
        triglycerides_mg_dl: Trigliceridi in mg/dL
        alt_iu_l: ALT in IU/L
    
    Returns:
        PNFS score
    """
    import math
    
    pnfs = (1.1 + (0.34 * math.sqrt(alt_iu_l)) + (0.002 * triglycerides_mg_dl) - 
            (1.1 * math.log10(age_years)) + (0.02 * waist_circumference_cm))
    
    return round(pnfs, 2)

def calculate_pnfs_interpretation(pnfs_score: float) -> dict:
    """
    Interpreta il Pediatric NAFLD Fibrosis Score (PNFS)
    
    Args:
        pnfs_score: PNFS calcolato
        
    Returns:
        Dict con interpretazione e raccomandazione
    """
    if pnfs_score < 8.0:
        return {
            'interpretation': 'BASSO RISCHIO FIBROSI',
            'recommendation': 'Monitoraggio standard, modifiche stile di vita, controllo ogni 6-12 mesi'
        }
    elif pnfs_score <= 9.0:
        return {
            'interpretation': 'RISCHIO INTERMEDIO',
            'recommendation': 'Monitoraggio più frequente, elastografia, controllo ogni 3-6 mesi'
        }
    else:
        return {
            'interpretation': 'ALTO RISCHIO FIBROSI',
            'recommendation': 'Considerare biopsia epatica, valutazione specialistica epatologica'
        }
    
def calculate_calcium_corrected(calcium_total_mg_dl: float, albumin_g_dl: float) -> float:
    """
    Calcola il calcio corretto per albumina
    Formula: Calcio totale + 0.8 × (4 - Albumina)
    
    Args:
        calcium_total_mg_dl: Calcio totale in mg/dL
        albumin_g_dl: Albumina in g/dL
    
    Returns:
        Calcio corretto in mg/dL
    """
    if albumin_g_dl >= 4.0:
        return calcium_total_mg_dl
    
    calcium_corrected = calcium_total_mg_dl + 0.8 * (4.0 - albumin_g_dl)
    return round(calcium_corrected, 2)

def calculate_bone_mineral_density_zscore_interpretation(bmd_zscore: float) -> dict:
    """
    Interpreta Z-score della densità minerale ossea in età pediatrica
    
    Args:
        bmd_zscore: Z-score della densità minerale ossea
        
    Returns:
        Dict con interpretazione e raccomandazione
    """
    if bmd_zscore >= -1.0:
        return {
            'interpretation': 'NORMALE',
            'recommendation': 'Nessuna azione specifica richiesta. Mantenere adeguato apporto di calcio e vitamina D.'
        }
    elif bmd_zscore >= -2.0:
        return {
            'interpretation': 'BASSA DENSITÀ MINERALE OSSEA',
            'recommendation': 'Ottimizzare apporto di calcio, vitamina D, attività fisica. Rivalutare in 12 mesi.'
        }
    else:
        return {
            'interpretation': 'DENSITÀ MINERALE OSSEA MOLTO BASSA',
            'recommendation': 'Valutazione endocrinologica, considerare intervento farmacologico, ricerca cause secondarie.'
        }