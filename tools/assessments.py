"""
Assessment clinici per la pediatria
Valutazione disidratazione e scale del dolore
"""
import mcp.types as types
def get_assessment_tools():
    """Restituisce tutti i tool per gli assessment clinici"""
    return [
        types.Tool(
            name="assess_dehydration",
            description="Valuta il grado di disidratazione nel bambino usando parametri clinici",
            inputSchema={
                "type": "object",
                "properties": {
                    "general_appearance": {
                        "type": "string",
                        "enum": ["normal", "restless_thirsty", "lethargic_unconscious"],
                        "description": "Aspetto generale: normal, restless_thirsty, lethargic_unconscious"
                    },
                    "eyes": {
                        "type": "string", 
                        "enum": ["normal", "slightly_sunken", "very_sunken"],
                        "description": "Occhi: normal, slightly_sunken, very_sunken"
                    },
                    "tears": {
                        "type": "string",
                        "enum": ["present", "decreased", "absent"], 
                        "description": "Lacrime: present, decreased, absent"
                    },
                    "mouth_tongue": {
                        "type": "string",
                        "enum": ["moist", "sticky", "dry"],
                        "description": "Bocca e lingua: moist, sticky, dry"
                    },
                    "thirst": {
                        "type": "string",
                        "enum": ["drinks_normal", "eager_to_drink", "unable_to_drink"],
                        "description": "Sete: drinks_normal, eager_to_drink, unable_to_drink"
                    },
                    "skin_pinch": {
                        "type": "string", 
                        "enum": ["normal", "slow", "very_slow"],
                        "description": "Pinch test: normal (<2sec), slow (2-3sec), very_slow (>3sec)"
                    },
                    "age_months": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 216,
                        "description": "Età in mesi (0-216 mesi = 0-18 anni)"
                    }
                },
                "required": ["general_appearance", "eyes", "tears", "mouth_tongue", "thirst", "skin_pinch", "age_months"]
            }
        ),
        
        types.Tool(
            name="assess_pain_scale",
            description="Raccomanda la scala del dolore più appropriata basata su età e capacità comunicative",
            inputSchema={
                "type": "object",
                "properties": {
                    "age_months": {
                        "type": "integer", 
                        "minimum": 0,
                        "maximum": 216,
                        "description": "Età in mesi (0-216 mesi = 0-18 anni)"
                    },
                    "cognitive_ability": {
                        "type": "string",
                        "enum": ["normal", "delayed", "unable_to_communicate"],
                        "description": "Capacità cognitive: normal, delayed, unable_to_communicate"
                    },
                    "pain_type": {
                        "type": "string",
                        "enum": ["acute", "chronic", "postoperative"],
                        "description": "Tipo di dolore: acute, chronic, postoperative"
                    },
                    "current_pain_indicators": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": ["crying", "facial_expression", "body_posture", "movement", "verbal_complaint", "sleep_disturbance", "feeding_difficulty"]
                        },
                        "description": "Indicatori di dolore presenti"
                    }
                },
                "required": ["age_months", "cognitive_ability", "pain_type"]
            }
        ),
        
        types.Tool(
            name="assess_nutritional_status",
            description="Valuta lo stato nutrizionale pediatrico con parametri clinici",
            inputSchema={
                "type": "object",
                "properties": {
                    "age_months": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 216,
                        "description": "Età in mesi"
                    },
                    "recent_weight_loss": {
                        "type": "boolean",
                        "description": "Perdita di peso recente (ultimo mese)"
                    },
                    "poor_appetite": {
                        "type": "boolean", 
                        "description": "Appetito ridotto persistente"
                    },
                    "feeding_difficulties": {
                        "type": "boolean",
                        "description": "Difficoltà alimentari (suzione, deglutizione)"
                    },
                    "growth_faltering": {
                        "type": "boolean",
                        "description": "Faltering di crescita (crossing percentili)"
                    },
                    "muscle_wasting": {
                        "type": "boolean",
                        "description": "Perdita massa muscolare visibile"
                    },
                    "subcutaneous_fat_loss": {
                        "type": "boolean",
                        "description": "Perdita grasso sottocutaneo"
                    },
                    "edema_present": {
                        "type": "boolean",
                        "description": "Edema presente"
                    },
                    "chronic_disease": {
                        "type": "boolean",
                        "description": "Malattia cronica presente"
                    }
                },
                "required": ["age_months", "recent_weight_loss", "poor_appetite", "feeding_difficulties", "growth_faltering", "muscle_wasting", "subcutaneous_fat_loss", "edema_present", "chronic_disease"]
            }
        ),
        
        types.Tool(
            name="assess_developmental_milestones",
            description="Valuta raggiungimento tappe sviluppo psicomotorio per età",
            inputSchema={
                "type": "object",
                "properties": {
                    "age_months": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 72,
                        "description": "Età in mesi (0-72 mesi)"
                    },
                    "motor_skills": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": ["head_control", "sits_unsupported", "crawls", "walks_independently", "runs", "jumps", "climbs_stairs", "rides_tricycle"]
                        },
                        "description": "Abilità motorie raggiunte"
                    },
                    "language_skills": {
                        "type": "array",
                        "items": {
                            "type": "string", 
                            "enum": ["responds_to_name", "babbles", "first_words", "two_words", "simple_sentences", "follows_commands", "tells_stories"]
                        },
                        "description": "Abilità linguistiche raggiunte"
                    },
                    "social_skills": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": ["smiles_socially", "stranger_anxiety", "parallel_play", "cooperative_play", "empathy", "shares_toys", "follows_rules"]
                        },
                        "description": "Abilità sociali raggiunte"
                    },
                    "cognitive_skills": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": ["object_permanence", "cause_effect", "symbolic_play", "sorting_shapes", "counts_to_ten", "draws_person", "understands_time"]
                        },
                        "description": "Abilità cognitive raggiunte"
                    }
                },
                "required": ["age_months", "motor_skills", "language_skills", "social_skills", "cognitive_skills"]
            }
        ),
        
        types.Tool(
            name="assess_asthma_control",
            description="Valuta controllo asma pediatrico usando parametri clinici",
            inputSchema={
                "type": "object",
                "properties": {
                    "daytime_symptoms_per_week": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 7,
                        "description": "Giorni con sintomi diurni nell'ultima settimana"
                    },
                    "nighttime_awakenings_per_month": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 30,
                        "description": "Risvegli notturni per asma nell'ultimo mese"
                    },
                    "rescue_inhaler_use_per_week": {
                        "type": "integer", 
                        "minimum": 0,
                        "maximum": 50,
                        "description": "Utilizzi broncodilatatore al bisogno per settimana"
                    },
                    "activity_limitation": {
                        "type": "string",
                        "enum": ["none", "minor", "moderate", "severe"],
                        "description": "Limitazione attività: none, minor, moderate, severe"
                    },
                    "school_absences_asthma": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 30,
                        "description": "Giorni assenza scuola per asma (ultimo mese)"
                    },
                    "recent_exacerbations": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 10,
                        "description": "Riacutizzazioni ultime 4 settimane"
                    }
                },
                "required": ["daytime_symptoms_per_week", "nighttime_awakenings_per_month", "rescue_inhaler_use_per_week", "activity_limitation", "school_absences_asthma", "recent_exacerbations"]
            }
        ),
        
        # NUOVI STRUMENTI AGGIUNTI
        
        types.Tool(
            name="assess_heads_ed",
            description="Valuta HEADS-ED per screening rapido salute mentale pediatrica in pronto soccorso",
            inputSchema={
                "type": "object",
                "properties": {
                    "home": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 2,
                        "description": "Home (ambiente familiare): 0=Supportivo/appropriato, 1=Alcune/lievi preoccupazioni, 2=Caos/conflitti maggiori/unsafe"
                    },
                    "education": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 2,
                        "description": "Education (scuola): 0=Andamento bene/supportiva, 1=Alcuni problemi/assenteismo, 2=Fallimento/sospensioni/non frequenta"
                    },
                    "activities_peers": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 2,
                        "description": "Activities/Peers (attività/pari): 0=Buone amicizie/attività, 1=Qualche preoccupazione sociale, 2=Isolamento/peer negativi/nessuna attività"
                    },
                    "drugs_alcohol": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 2,
                        "description": "Drugs/Alcohol (sostanze): 0=Nessun uso, 1=Sperimentazione/uso occasionale, 2=Uso regolare/problematico"
                    },
                    "suicidality": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 2,
                        "description": "Suicidality (suicidalità): 0=Negata, 1=Ideazione senza piano/intento, 2=Ideazione con piano/intento/comportamenti"
                    },
                    "emotions_behavior": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 2,
                        "description": "Emotions/Behavior (emozioni/comportamento): 0=Appropriate/stable, 1=Mood/anxiety lievi, 2=Depressione/ansia severe/psicosi/aggressività"
                    },
                    "discharge_resources": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 2,
                        "description": "Discharge Resources (risorse dimissione): 0=Supporto familiare adeguato/follow-up, 1=Risorse limitate, 2=Nessun supporto/follow-up"
                    },
                    "age_years": {
                        "type": "number",
                        "minimum": 8,
                        "maximum": 18,
                        "description": "Età in anni (validato per 8-18 anni)"
                    }
                },
                "required": ["home", "education", "activities_peers", "drugs_alcohol", "suicidality", "emotions_behavior", "discharge_resources", "age_years"]
            }
        ),
        
        types.Tool(
            name="assess_pediatric_sleep",
            description="Valuta BEARS per screening disturbi del sonno pediatrico",
            inputSchema={
                "type": "object",
                "properties": {
                    "age_years": {
                        "type": "number",
                        "minimum": 0,
                        "maximum": 18,
                        "description": "Età in anni"
                    },
                    "bedtime_problems": {
                        "type": "boolean",
                        "description": "Problemi di addormentamento"
                    },
                    "excessive_daytime_sleepiness": {
                        "type": "boolean",
                        "description": "Sonnolenza diurna eccessiva"
                    },
                    "awakenings": {
                        "type": "boolean",
                        "description": "Risvegli notturni frequenti"
                    },
                    "regularity": {
                        "type": "boolean",
                        "description": "Regolarità del ciclo sonno-veglia"
                    },
                    "snoring": {
                        "type": "boolean",
                        "description": "Russamento/problemi respiratori"
                    }
                },
                "required": ["age_years", "bedtime_problems", "excessive_daytime_sleepiness", "awakenings", "regularity", "snoring"]
            }
        ),
        
        # CRITERI ROME IV AGGIUNTI
        
        types.Tool(
            name="assess_rome4_abdominal_migraine",
            description="Valuta criteri Rome IV per emicrania addominale pediatrica",
            inputSchema={
                "type": "object",
                "properties": {
                    "episodes_abdominal_pain": {
                        "type": "boolean",
                        "description": "Episodi stereotipati di dolore addominale acuto periombelicale"
                    },
                    "episodes_duration_hours": {
                        "type": "integer",
                        "minimum": 1,
                        "maximum": 72,
                        "description": "Durata tipica degli episodi in ore (1-72)"
                    },
                    "normal_between_episodes": {
                        "type": "boolean",
                        "description": "Ritorno allo stato di salute normale tra gli episodi"
                    },
                    "interferes_activities": {
                        "type": "boolean",
                        "description": "Dolore interferisce con attività quotidiane"
                    },
                    "associated_symptoms": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": ["anorexia", "nausea", "vomiting", "headache", "photophobia", "pallor"]
                        },
                        "description": "Sintomi associati: anoressia, nausea, vomito, mal di testa, fotofobia, pallore"
                    },
                    "symptoms_duration_months": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 60,
                        "description": "Durata dei sintomi in mesi"
                    },
                    "episodes_count": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 100,
                        "description": "Numero di episodi negli ultimi 6 mesi"
                    }
                },
                "required": ["episodes_abdominal_pain", "episodes_duration_hours", "normal_between_episodes", "interferes_activities", "associated_symptoms", "symptoms_duration_months", "episodes_count"]
            }
        ),
        
        types.Tool(
            name="assess_rome4_aerophagia",
            description="Valuta criteri Rome IV per aerofagia pediatrica",
            inputSchema={
                "type": "object",
                "properties": {
                    "air_swallowing": {
                        "type": "boolean",
                        "description": "Deglutizione eccessiva di aria"
                    },
                    "abdominal_distension": {
                        "type": "boolean",
                        "description": "Distensione addominale dovuta all'aria"
                    },
                    "repetitive_belching": {
                        "type": "boolean",
                        "description": "Eruttazione ripetuta"
                    },
                    "repetitive_flatulence": {
                        "type": "boolean",
                        "description": "Flatulenza ripetuta"
                    },
                    "symptoms_duration_months": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 60,
                        "description": "Durata dei sintomi in mesi"
                    },
                    "symptoms_frequency_weekly": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 7,
                        "description": "Frequenza dei sintomi (giorni/settimana)"
                    },
                    "other_gi_conditions": {
                        "type": "boolean",
                        "description": "Presenza di altre condizioni gastrointestinali che spiegano i sintomi"
                    }
                },
                "required": ["air_swallowing", "abdominal_distension", "repetitive_belching", "repetitive_flatulence", "symptoms_duration_months", "symptoms_frequency_weekly", "other_gi_conditions"]
            }
        ),
        
        types.Tool(
            name="assess_rome4_constipation",
            description="Valuta criteri Rome IV per stipsi funzionale pediatrica",
            inputSchema={
                "type": "object",
                "properties": {
                    "bowel_movements_weekly": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 21,
                        "description": "Numero di evacuazioni settimanali"
                    },
                    "fecal_incontinence": {
                        "type": "boolean",
                        "description": "Almeno 1 episodio di incontinenza fecale settimanale (in bambini continenti)"
                    },
                    "stool_retention": {
                        "type": "boolean",
                        "description": "Storia di posture o comportamenti di ritenzione fecale"
                    },
                    "painful_defecation": {
                        "type": "boolean",
                        "description": "Storia di defecazione dolorosa o difficoltosa"
                    },
                    "large_fecal_mass": {
                        "type": "boolean",
                        "description": "Presenza di grande massa fecale nel retto"
                    },
                    "large_diameter_stools": {
                        "type": "boolean",
                        "description": "Storia di feci di grande diametro"
                    },
                    "symptoms_duration_months": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 60,
                        "description": "Durata dei sintomi in mesi"
                    },
                    "toilet_trained": {
                        "type": "boolean",
                        "description": "Bambino ha completato training toilette"
                    }
                },
                "required": ["bowel_movements_weekly", "fecal_incontinence", "stool_retention", "painful_defecation", "large_fecal_mass", "large_diameter_stools", "symptoms_duration_months"]
            }
        ),
        
        types.Tool(
            name="assess_rome4_cyclic_vomiting",
            description="Valuta criteri Rome IV per sindrome del vomito ciclico pediatrica",
            inputSchema={
                "type": "object",
                "properties": {
                    "stereotypical_episodes": {
                        "type": "boolean",
                        "description": "Episodi stereotipati di vomito intenso"
                    },
                    "episodes_duration_hours": {
                        "type": "integer",
                        "minimum": 1,
                        "maximum": 168,
                        "description": "Durata tipica degli episodi in ore (1-168)"
                    },
                    "episodes_count": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 100,
                        "description": "Numero di episodi negli ultimi 12 mesi"
                    },
                    "return_to_baseline": {
                        "type": "boolean",
                        "description": "Ritorno allo stato di salute normale tra gli episodi"
                    },
                    "symptoms_duration_months": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 60,
                        "description": "Durata dei sintomi in mesi"
                    },
                    "vomiting_frequency": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 100,
                        "description": "Frequenza del vomito durante gli episodi (numero episodi/ora)"
                    },
                    "other_gi_conditions": {
                        "type": "boolean",
                        "description": "Presenza di altre condizioni gastrointestinali che spiegano i sintomi"
                    }
                },
                "required": ["stereotypical_episodes", "episodes_duration_hours", "episodes_count", "return_to_baseline", "symptoms_duration_months", "vomiting_frequency", "other_gi_conditions"]
            }
        ),
        
        types.Tool(
            name="assess_rome4_functional_abdominal_pain",
            description="Valuta criteri Rome IV per dolore addominale funzionale pediatrico - non altrimenti specificato",
            inputSchema={
                "type": "object",
                "properties": {
                    "abdominal_pain_frequency": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 7,
                        "description": "Frequenza del dolore addominale (giorni/settimana)"
                    },
                    "continuous_pain": {
                        "type": "boolean",
                        "description": "Dolore addominale continuo"
                    },
                    "meets_ibs_criteria": {
                        "type": "boolean",
                        "description": "Soddisfa criteri per sindrome intestino irritabile"
                    },
                    "meets_dyspepsia_criteria": {
                        "type": "boolean",
                        "description": "Soddisfa criteri per dispepsia funzionale"
                    },
                    "meets_abdominal_migraine_criteria": {
                        "type": "boolean",
                        "description": "Soddisfa criteri per emicrania addominale"
                    },
                    "symptoms_duration_months": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 60,
                        "description": "Durata dei sintomi in mesi"
                    },
                    "inflammatory_condition": {
                        "type": "boolean",
                        "description": "Evidenza di processo infiammatorio, anatomico, metabolico o neoplastico"
                    }
                },
                "required": ["abdominal_pain_frequency", "continuous_pain", "meets_ibs_criteria", "meets_dyspepsia_criteria", "meets_abdominal_migraine_criteria", "symptoms_duration_months", "inflammatory_condition"]
            }
        ),
        
        types.Tool(
            name="assess_rome4_functional_dyspepsia",
            description="Valuta criteri Rome IV per dispepsia funzionale pediatrica",
            inputSchema={
                "type": "object",
                "properties": {
                    "bothersome_postprandial_fullness": {
                        "type": "boolean",
                        "description": "Sensazione fastidiosa di pienezza postprandiale"
                    },
                    "early_satiety": {
                        "type": "boolean",
                        "description": "Sazietà precoce che impedisce di terminare un pasto normale"
                    },
                    "epigastric_pain": {
                        "type": "boolean",
                        "description": "Dolore epigastrico"
                    },
                    "epigastric_burning": {
                        "type": "boolean",
                        "description": "Bruciore epigastrico"
                    },
                    "symptoms_duration_months": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 60,
                        "description": "Durata dei sintomi in mesi"
                    },
                    "symptoms_frequency_weekly": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 7,
                        "description": "Frequenza dei sintomi (giorni/settimana)"
                    },
                    "organic_disease": {
                        "type": "boolean",
                        "description": "Evidenza di malattia organica che spiega i sintomi"
                    }
                },
                "required": ["bothersome_postprandial_fullness", "early_satiety", "epigastric_pain", "epigastric_burning", "symptoms_duration_months", "symptoms_frequency_weekly", "organic_disease"]
            }
        ),
        
        types.Tool(
            name="assess_rome4_functional_nausea_vomiting",
            description="Valuta criteri Rome IV per nausea e vomito funzionali pediatrici",
            inputSchema={
                "type": "object",
                "properties": {
                    "bothersome_nausea": {
                        "type": "boolean",
                        "description": "Nausea fastidiosa come sintomo predominante"
                    },
                    "weekly_vomiting_episodes": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 50,
                        "description": "Episodi di vomito settimanali"
                    },
                    "meal_related": {
                        "type": "boolean",
                        "description": "Sintomi regolarmente associati ai pasti"
                    },
                    "induced_vomiting": {
                        "type": "boolean",
                        "description": "Vomito autoindotto"
                    },
                    "meets_eating_disorder_criteria": {
                        "type": "boolean",
                        "description": "Soddisfa criteri per disturbo alimentare"
                    },
                    "meets_rumination_criteria": {
                        "type": "boolean",
                        "description": "Soddisfa criteri per sindrome di ruminazione"
                    },
                    "meets_cyclic_vomiting_criteria": {
                        "type": "boolean",
                        "description": "Soddisfa criteri per sindrome del vomito ciclico"
                    },
                    "symptoms_duration_months": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 60,
                        "description": "Durata dei sintomi in mesi"
                    },
                    "organic_disease": {
                        "type": "boolean",
                        "description": "Evidenza di malattia organica che spiega i sintomi"
                    }
                },
                "required": ["bothersome_nausea", "weekly_vomiting_episodes", "meal_related", "induced_vomiting", "meets_eating_disorder_criteria", "meets_rumination_criteria", "meets_cyclic_vomiting_criteria", "symptoms_duration_months", "organic_disease"]
            }
        ),
        
        types.Tool(
            name="assess_rome4_ibs",
            description="Valuta criteri Rome IV per sindrome dell'intestino irritabile pediatrica",
            inputSchema={
                "type": "object",
                "properties": {
                    "abdominal_pain_days_monthly": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 30,
                        "description": "Giorni con dolore addominale al mese"
                    },
                    "pain_related_to_defecation": {
                        "type": "boolean",
                        "description": "Dolore addominale associato alla defecazione"
                    },
                    "stool_frequency_change": {
                        "type": "boolean",
                        "description": "Dolore associato a cambio nella frequenza delle feci"
                    },
                    "stool_form_change": {
                        "type": "boolean",
                        "description": "Dolore associato a cambio nella forma/consistenza delle feci"
                    },
                    "symptoms_duration_months": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 60,
                        "description": "Durata dei sintomi in mesi"
                    },
                    "predominant_stool_pattern": {
                        "type": "string",
                        "enum": ["constipation", "diarrhea", "mixed", "unspecified"],
                        "description": "Pattern predominante delle feci: constipation, diarrhea, mixed, unspecified"
                    },
                    "organic_disease": {
                        "type": "boolean",
                        "description": "Evidenza di malattia organica che spiega i sintomi"
                    }
                },
                "required": ["abdominal_pain_days_monthly", "pain_related_to_defecation", "stool_frequency_change", "stool_form_change", "symptoms_duration_months", "predominant_stool_pattern", "organic_disease"]
            }
        ),
        
        types.Tool(
            name="assess_rome4_nonretentive_fecal_incontinence",
            description="Valuta criteri Rome IV per incontinenza fecale non ritentiva pediatrica",
            inputSchema={
                "type": "object",
                "properties": {
                    "defecation_inappropriate_places": {
                        "type": "boolean",
                        "description": "Defecazione in luoghi inappropriati"
                    },
                    "fecal_incontinence_frequency": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 30,
                        "description": "Frequenza incontinenza fecale (giorni/mese)"
                    },
                    "developmental_age_at_least_4": {
                        "type": "boolean",
                        "description": "Età di sviluppo di almeno 4 anni"
                    },
                    "toilet_trained": {
                        "type": "boolean",
                        "description": "Bambino ha completato training toilette"
                    },
                    "fecal_retention": {
                        "type": "boolean",
                        "description": "Evidenza di ritenzione fecale"
                    },
                    "symptoms_duration_months": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 60,
                        "description": "Durata dei sintomi in mesi"
                    },
                    "organic_disease": {
                        "type": "boolean",
                        "description": "Evidenza di malattia organica che spiega i sintomi"
                    }
                },
                "required": ["defecation_inappropriate_places", "fecal_incontinence_frequency", "developmental_age_at_least_4", "toilet_trained", "fecal_retention", "symptoms_duration_months", "organic_disease"]
            }
        ),
        
        types.Tool(
            name="assess_rome4_rumination_syndrome",
            description="Valuta criteri Rome IV per sindrome di ruminazione pediatrica",
            inputSchema={
                "type": "object",
                "properties": {
                    "repeated_regurgitation": {
                        "type": "boolean",
                        "description": "Rigurgito ripetuto e senza sforzo di cibo parzialmente digerito"
                    },
                    "regurgitation_not_preceded_by_retching": {
                        "type": "boolean",
                        "description": "Rigurgito non preceduto da nausea o conati"
                    },
                    "regurgitation_within_30min_after_meal": {
                        "type": "boolean",
                        "description": "Inizio entro 30 minuti dal pasto"
                    },
                    "regurgitation_not_improved_with_acid_suppression": {
                        "type": "boolean",
                        "description": "Non migliora con terapie standard per reflusso"
                    },
                    "symptoms_duration_months": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 60,
                        "description": "Durata dei sintomi in mesi"
                    },
                    "symptoms_frequency_weekly": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 7,
                        "description": "Frequenza dei sintomi (giorni/settimana)"
                    },
                    "organic_disease": {
                        "type": "boolean",
                        "description": "Evidenza di malattia organica che spiega i sintomi"
                    }
                },
                "required": ["repeated_regurgitation", "regurgitation_not_preceded_by_retching", "regurgitation_within_30min_after_meal", "regurgitation_not_improved_with_acid_suppression", "symptoms_duration_months", "symptoms_frequency_weekly", "organic_disease"]
            }
        ),
        types.Tool(
            name="assess_brue_criteria",
            description="Valuta i criteri per Brief Resolved Unexplained Events (BRUE) nei lattanti e classifica il rischio",
            inputSchema={
                "type": "object",
                "properties": {
                    "age_less_than_1_year": {
                        "type": "boolean",
                        "description": "Età <1 anno"
                    },
                    "event_brief": {
                        "type": "boolean",
                        "description": "Evento breve (<1 minuto) e risolto completamente"
                    },
                    "no_explanation": {
                        "type": "boolean",
                        "description": "Nessuna spiegazione identificabile dopo valutazione"
                    },
                    "event_features": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": [
                                "cyanosis", "pallor", "absent_breathing", "marked_change_in_tone", 
                                "altered_responsiveness"
                            ]
                        },
                        "description": "Caratteristiche dell'evento (cianosi, pallore, respiro assente, alterato tono, alterata responsività)"
                    },
                    "age_less_than_2_months": {
                        "type": "boolean",
                        "description": "Età <2 mesi"
                    },
                    "prematurity": {
                        "type": "boolean",
                        "description": "Prematurità <32 settimane o età <45 settimane post-concezionali"
                    },
                    "event_duration_gt_1_min": {
                        "type": "boolean",
                        "description": "Durata evento >1 minuto"
                    },
                    "multiple_events": {
                        "type": "boolean",
                        "description": "Eventi multipli"
                    },
                    "cpr_required": {
                        "type": "boolean",
                        "description": "RCP richiesta da personale sanitario"
                    }
                },
                "required": ["age_less_than_1_year", "event_brief", "no_explanation", "event_features"]
            }
        )
    
    ]
def handle_assessment_tools(name: str, arguments: dict):
    """Gestisce gli assessment clinici"""
    try:
        if name == "assess_dehydration":
            return _assess_dehydration(arguments)
        elif name == "assess_pain_scale":
            return _assess_pain_scale(arguments)
        elif name == "assess_nutritional_status":
            return _assess_nutritional_status(arguments)
        elif name == "assess_developmental_milestones":
            return _assess_developmental_milestones(arguments)
        elif name == "assess_asthma_control":
            return _assess_asthma_control(arguments)
        elif name == "assess_heads_ed":
            return _assess_heads_ed(arguments)
        elif name == "assess_pediatric_sleep":
            return _assess_pediatric_sleep(arguments)
        elif name == "assess_rome4_abdominal_migraine":
            return _assess_rome4_abdominal_migraine(arguments)
        elif name == "assess_rome4_aerophagia":
            return _assess_rome4_aerophagia(arguments)
        elif name == "assess_rome4_constipation":
            return _assess_rome4_constipation(arguments)
        elif name == "assess_rome4_cyclic_vomiting":
            return _assess_rome4_cyclic_vomiting(arguments)
        elif name == "assess_rome4_functional_abdominal_pain":
            return _assess_rome4_functional_abdominal_pain(arguments)
        elif name == "assess_rome4_functional_dyspepsia":
            return _assess_rome4_functional_dyspepsia(arguments)
        elif name == "assess_rome4_functional_nausea_vomiting":
            return _assess_rome4_functional_nausea_vomiting(arguments)
        elif name == "assess_rome4_ibs":
            return _assess_rome4_ibs(arguments)
        elif name == "assess_rome4_nonretentive_fecal_incontinence":
            return _assess_rome4_nonretentive_fecal_incontinence(arguments)
        elif name == "assess_rome4_rumination_syndrome":
            return _assess_rome4_rumination_syndrome(arguments)
        # Nuovi strumenti aggiunti
        elif name == "assess_brue_criteria":
            return _assess_brue_criteria(arguments)
        else:
            raise ValueError(f"Assessment non implementato: {name}")
    except Exception as e:
        return [types.TextContent(type="text", text=f"Errore nell'assessment: {str(e)}")]
def _assess_dehydration(args):
    """Valuta il grado di disidratazione secondo WHO/UNICEF"""
    
    # Punteggio per ogni parametro
    scores = {
        'general_appearance': {
            'normal': 0,
            'restless_thirsty': 1, 
            'lethargic_unconscious': 2
        },
        'eyes': {
            'normal': 0,
            'slightly_sunken': 1,
            'very_sunken': 2
        },
        'tears': {
            'present': 0,
            'decreased': 1,
            'absent': 2
        },
        'mouth_tongue': {
            'moist': 0,
            'sticky': 1,
            'dry': 2
        },
        'thirst': {
            'drinks_normal': 0,
            'eager_to_drink': 1,
            'unable_to_drink': 2
        },
        'skin_pinch': {
            'normal': 0,
            'slow': 1,
            'very_slow': 2
        }
    }
    
    # Calcolo punteggio totale
    total_score = 0
    details = []
    
    for param, value in args.items():
        if param == 'age_months':
            continue
        if param in scores and value in scores[param]:
            score = scores[param][value]
            total_score += score
            details.append(f"• {param.replace('_', ' ').title()}: {value.replace('_', ' ')} ({score} punti)")
    
    # Determinazione grado disidratazione
    age_months = args.get('age_months', 12)
    
    if total_score <= 2:
        dehydration_grade = "NESSUNA o LIEVE"
        fluid_loss = "<3%"
        management = "Soluzioni orali, allattamento al seno, alimentazione normale"
        who_plan = "Piano A - Trattamento domiciliare"
    elif total_score <= 6:
        dehydration_grade = "MODERATA"
        fluid_loss = "3-9%"
        management = "SRO (Sali di Reidratazione Orale) 75ml/kg in 4 ore"
        who_plan = "Piano B - Reidratazione orale"
    else:
        dehydration_grade = "SEVERA"
        fluid_loss = ">9%"
        management = "Reidratazione endovenosa immediata - Ricovero ospedaliero"
        who_plan = "Piano C - Reidratazione endovenosa"
    
    # Calcolo SRO se indicato
    weight_estimate = "Non specificato"
    sro_volume = "Non calcolabile senza peso"
    
    result = f"""Valutazione Disidratazione (WHO/UNICEF)
========================================
Età paziente: {age_months} mesi
Punteggio totale: {total_score}/12

Grado di disidratazione: {dehydration_grade}
Perdita di fluidi stimata: {fluid_loss} del peso corporeo
Piano WHO: {who_plan}

Parametri valutati:
{chr(10).join(details)}

Trattamento raccomandato:
{management}

Note cliniche:
- Controllare peso se disponibile per calcoli precisi
- Nei lattanti <6 mesi la disidratazione può essere più severa
- Monitorare diuresi, sete, comportamento
- Rivalutare ogni 2-4 ore durante trattamento

Segni di allarme per ospedalizzazione:
- Vomito persistente (non tollera SRO)
- Diarrea profusa (>10 scariche/die)
- Febbre alta persistente
- Segni di shock (ipotensione, tachicardia)
"""
    return [types.TextContent(type="text", text=result)]

def _assess_pain_scale(args):
    """Raccomanda la scala del dolore più appropriata"""
    
    age_months = args.get('age_months')
    cognitive_ability = args.get('cognitive_ability')
    pain_type = args.get('pain_type')
    pain_indicators = args.get('current_pain_indicators', [])
    
    age_years = age_months / 12
    
    # Determinazione scala più appropriata
    if age_months < 12:  # 0-12 mesi
        if pain_type == "postoperative":
            recommended_scale = "COMFORT-B Scale"
            description = "Scala comportamentale per neonati post-operatori"
        else:
            recommended_scale = "NIPS (Neonatal Infant Pain Scale)"
            description = "Scala per dolore neonatale/infantile"
    
    elif age_months < 36:  # 1-3 anni
        if cognitive_ability == "unable_to_communicate":
            recommended_scale = "FLACC Scale"
            description = "Scala comportamentale (Face, Legs, Activity, Cry, Consolability)"
        else:
            recommended_scale = "FLACC Scale o Wong-Baker FACES"
            description = "FLACC per osservazione, FACES se collaborativo"
    
    elif age_months < 84:  # 3-7 anni
        if cognitive_ability in ["normal", "delayed"]:
            recommended_scale = "Wong-Baker FACES Pain Scale"
            description = "Scala con faccine adatta per bambini"
        else:
            recommended_scale = "FLACC Scale"
            description = "Scala comportamentale per bambini non comunicativi"
    
    else:  # >7 anni
        if cognitive_ability == "normal":
            recommended_scale = "NRS (Numeric Rating Scale) 0-10"
            description = "Scala numerica per bambini e adolescenti"
        elif cognitive_ability == "delayed":
            recommended_scale = "Wong-Baker FACES Pain Scale"
            description = "Scala con faccine, più comprensibile"
        else:
            recommended_scale = "FLACC Scale modificata"
            description = "Scala comportamentale per non comunicativi"
    
    # Indicatori di dolore presenti
    pain_indicators_text = ""
    if pain_indicators:
        pain_indicators_text = f"\nIndicatori di dolore presenti:\n" + "\n".join([f"• {indicator.replace('_', ' ').title()}" for indicator in pain_indicators])
    
    # Scale alternative e considerazioni speciali
    alternatives = []
    special_considerations = []
    
    if pain_type == "chronic":
        alternatives.append("• Consider PedsQL for quality of life assessment")
        special_considerations.append("• Valutazione multidimensionale per dolore cronico")
    
    if pain_type == "postoperative":
        special_considerations.append("• Valutazione frequente nelle prime 24-48h")
        special_considerations.append("• Considerare dolore a riposo e durante movimento")
    
    if age_months < 6:
        special_considerations.append("• Nei neonati pretermine usare scale specifiche (PIPP)")
    
    result = f"""Raccomandazione Scala del Dolore
=================================
Paziente: {age_years:.1f} anni ({age_months} mesi)
Capacità cognitive: {cognitive_ability.replace('_', ' ')}
Tipo di dolore: {pain_type}

SCALA RACCOMANDATA: {recommended_scale}
Descrizione: {description}

{pain_indicators_text}

Scale alternative per età:
- 0-12 mesi: NIPS, COMFORT-B, PIPP (pretermine)
- 1-3 anni: FLACC, Wong-Baker FACES
- 3-7 anni: Wong-Baker FACES, OUCHER 
- 7+ anni: NRS 0-10, VAS, Wong-Baker FACES

Considerazioni speciali:
{chr(10).join(special_considerations) if special_considerations else "• Nessuna particolare"}

Note per la valutazione:
- Valutare dolore a riposo e durante attività
- Documentare intensità prima e dopo interventi
- Considerare fattori culturali e familiari
- Coinvolgere i genitori nella valutazione
- Rivalutare regolarmente l'efficacia degli interventi

Targets terapeutici:
- Dolore acuto: <4/10 o assenza pianto/distress
- Dolore procedurale: <6/10 con interventi appropriati
- Dolore cronico: funzionalità e qualità di vita
"""
    return [types.TextContent(type="text", text=result)]

def _assess_nutritional_status(args):
    """Valuta stato nutrizionale pediatrico"""
    age_months = args.get('age_months')
    
    # Conteggio fattori di rischio
    risk_factors = 0
    risk_details = []
    
    risk_items = {
        'recent_weight_loss': 'Perdita di peso recente',
        'poor_appetite': 'Appetito ridotto', 
        'feeding_difficulties': 'Difficoltà alimentari',
        'growth_faltering': 'Faltering di crescita',
        'muscle_wasting': 'Perdita massa muscolare',
        'subcutaneous_fat_loss': 'Perdita grasso sottocutaneo',
        'edema_present': 'Edema presente',
        'chronic_disease': 'Malattia cronica'
    }
    
    for item, value in args.items():
        if item != 'age_months' and value:
            risk_factors += 1
            risk_details.append(f"• {risk_items[item]}")
    
    # Valutazione rischio nutrizionale
    if risk_factors == 0:
        risk_level = "BASSO RISCHIO"
        recommendation = "Stato nutrizionale apparentemente adeguato"
        monitoring = "Controlli di routine secondo calendario"
    elif risk_factors <= 2:
        risk_level = "RISCHIO MODERATO"
        recommendation = "Valutazione nutrizionale dettagliata raccomandata"
        monitoring = "Follow-up nutrizionale entro 1 mese"
    elif risk_factors <= 4:
        risk_level = "ALTO RISCHIO"
        recommendation = "Intervento nutrizionale necessario"
        monitoring = "Valutazione specialistica nutrizionale urgente"
    else:
        risk_level = "RISCHIO MOLTO ALTO"
        recommendation = "Malnutrizione probabile - Intervento immediato"
        monitoring = "Ricovero per stabilizzazione nutrizionale"
    
    age_years = age_months / 12
    
    result = f"""Valutazione Stato Nutrizionale Pediatrico
=========================================
Età: {age_years:.1f} anni ({age_months} mesi)
Fattori di rischio presenti: {risk_factors}/8

Livello di rischio: {risk_level}
Raccomandazione: {recommendation}
Monitoraggio: {monitoring}

Fattori di rischio identificati:
{chr(10).join(risk_details) if risk_details else '• Nessun fattore di rischio identificato'}

Valutazione completa dovrebbe includere:
- Antropometria (peso, altezza, BMI, circonferenze)
- Curve di crescita e velocità crescita
- Anamnesi alimentare (diario alimentare 3-7 giorni)
- Esame obiettivo (segni carenza specifiche)
- Laboratorio se indicato (albumina, prealbumina, transferrina)

Indicatori antropometrici chiave:
- Peso per età (sottopeso se <3° percentile)
- Altezza per età (stunting se <3° percentile)  
- Peso per altezza o BMI (wasting se <3° percentile)
- Velocità di crescita (crossing percentili)

Red flags per malnutrizione:
- Perdita >5% peso in 1 mese
- Crossing >2 percentili in 6 mesi
- Segni clinici carenze vitaminiche/minerali
- Ritardo sviluppo psicomotorio
"""
    return [types.TextContent(type="text", text=result)]

def _assess_developmental_milestones(args):
    """Valuta tappe sviluppo psicomotorio"""
    age_months = args.get('age_months')
    motor_skills = args.get('motor_skills', [])
    language_skills = args.get('language_skills', [])
    social_skills = args.get('social_skills', [])
    cognitive_skills = args.get('cognitive_skills', [])
    
    # Tappe attese per età (semplificato)
    expected_milestones = {}
    
    if age_months >= 6:
        expected_milestones['motor'] = ['head_control']
    if age_months >= 8:
        expected_milestones['motor'].append('sits_unsupported')
    if age_months >= 12:
        expected_milestones['motor'].extend(['crawls', 'walks_independently'])
        expected_milestones['language'] = ['responds_to_name', 'babbles', 'first_words']
        expected_milestones['social'] = ['smiles_socially', 'stranger_anxiety']
        expected_milestones['cognitive'] = ['object_permanence']
    if age_months >= 24:
        expected_milestones['motor'].extend(['runs', 'jumps'])
        expected_milestones['language'].extend(['two_words', 'follows_commands'])
        expected_milestones['social'].append('parallel_play')
        expected_milestones['cognitive'].extend(['cause_effect', 'symbolic_play'])
    if age_months >= 36:
        expected_milestones['motor'].extend(['climbs_stairs', 'rides_tricycle'])
        expected_milestones['language'].extend(['simple_sentences', 'tells_stories'])
        expected_milestones['social'].extend(['cooperative_play', 'empathy'])
        expected_milestones['cognitive'].extend(['sorting_shapes', 'draws_person'])
    if age_months >= 60:
        expected_milestones['language'].append('tells_stories')
        expected_milestones['social'].extend(['shares_toys', 'follows_rules'])
        expected_milestones['cognitive'].extend(['counts_to_ten', 'understands_time'])
    
    # Valutazione per dominio
    areas_concern = []
    areas_normal = []
    
    domains = {
        'Motorio': (motor_skills, expected_milestones.get('motor', [])),
        'Linguaggio': (language_skills, expected_milestones.get('language', [])),
        'Sociale': (social_skills, expected_milestones.get('social', [])),
        'Cognitivo': (cognitive_skills, expected_milestones.get('cognitive', []))
    }
    
    for domain_name, (achieved, expected) in domains.items():
        if expected:
            achieved_count = len([skill for skill in expected if skill in achieved])
            expected_count = len(expected)
            percentage = (achieved_count / expected_count) * 100 if expected_count > 0 else 100
            
            if percentage < 70:
                areas_concern.append(f"• {domain_name}: {achieved_count}/{expected_count} tappe ({percentage:.0f}%)")
            else:
                areas_normal.append(f"• {domain_name}: {achieved_count}/{expected_count} tappe ({percentage:.0f}%)")
    
    # Valutazione globale
    if len(areas_concern) == 0:
        overall_assessment = "SVILUPPO APPROPRIATO"
        recommendation = "Sviluppo in linea con età cronologica"
        follow_up = "Controlli di routine"
    elif len(areas_concern) == 1:
        overall_assessment = "POSSIBILE RITARDO SPECIFICO"
        recommendation = "Approfondimento specialistico consigliato"
        follow_up = "Valutazione specifica entro 2-3 mesi"
    else:
        overall_assessment = "POSSIBILE RITARDO GLOBALE"
        recommendation = "Valutazione neuropsichiatrica urgente"
        follow_up = "Riferimento immediato per early intervention"
    
    age_years = age_months / 12
    
    result = f"""Valutazione Sviluppo Psicomotorio
=================================
Età: {age_years:.1f} anni ({age_months} mesi)

Valutazione globale: {overall_assessment}
Raccomandazione: {recommendation}
Follow-up: {follow_up}

Domini valutati:

Aree di preoccupazione:
{chr(10).join(areas_concern) if areas_concern else '• Nessuna area di preoccupazione'}

Aree nella norma:
{chr(10).join(areas_normal) if areas_normal else '• Nessuna area valutata come normale'}

Abilità raggiunte per dominio:
- Motorie: {', '.join(motor_skills) if motor_skills else 'Nessuna specificata'}
- Linguistiche: {', '.join(language_skills) if language_skills else 'Nessuna specificata'}  
- Sociali: {', '.join(social_skills) if social_skills else 'Nessuna specificata'}
- Cognitive: {', '.join(cognitive_skills) if cognitive_skills else 'Nessuna specificata'}

Note importanti:
- Valutazione basata su milestone semplificati
- Variabilità individuale normale
- Considerare fattori ambientali e culturali
- Screening formale raccomandato se preoccupazioni
- Early intervention efficace se avviato precocemente

Red flags per riferimento urgente:
- Perdita abilità già acquisite
- Ritardo significativo in 2+ domini
- Assenza linguaggio a 2 anni
- Comportamenti ripetitivi/stereotipati
- Mancanza interesse sociale
"""
    return [types.TextContent(type="text", text=result)]

def _assess_asthma_control(args):
    """Valuta controllo dell'asma pediatrico"""
    daytime_symptoms = args.get('daytime_symptoms_per_week', 0)
    nighttime_awakenings = args.get('nighttime_awakenings_per_month', 0)
    rescue_inhaler_use = args.get('rescue_inhaler_use_per_week', 0)
    activity_limitation = args.get('activity_limitation', 'none')
    school_absences = args.get('school_absences_asthma', 0)
    recent_exacerbations = args.get('recent_exacerbations', 0)
    
    # Punteggio controllo asma
    control_score = 0
    
    # Sintomi diurni
    if daytime_symptoms == 0:
        control_score += 0
    elif daytime_symptoms <= 2:
        control_score += 1
    else:
        control_score += 2
    
    # Risvegli notturni
    if nighttime_awakenings == 0:
        control_score += 0
    elif nighttime_awakenings <= 2:
        control_score += 1
    else:
        control_score += 2
    
    # Uso broncodilatatore
    if rescue_inhaler_use == 0:
        control_score += 0
    elif rescue_inhaler_use <= 2:
        control_score += 1
    else:
        control_score += 2
    
    # Limitazione attività
    limitation_scores = {'none': 0, 'minor': 1, 'moderate': 2, 'severe': 3}
    control_score += limitation_scores.get(activity_limitation, 0)
    
    # Assenze scolastiche
    if school_absences == 0:
        control_score += 0
    elif school_absences <= 2:
        control_score += 1
    else:
        control_score += 2
    
    # Riacutizzazioni
    if recent_exacerbations == 0:
        control_score += 0
    elif recent_exacerbations == 1:
        control_score += 1
    else:
        control_score += 2
    
    # Classificazione controllo
    if control_score <= 2:
        control_level = "BEN CONTROLLATO"
        action = "Mantenere terapia attuale"
        follow_up = "Controllo tra 3-6 mesi"
        color = "Verde"
    elif control_score <= 6:
        control_level = "PARZIALMENTE CONTROLLATO"
        action = "Considerare step-up terapeutico"
        follow_up = "Rivalutazione entro 1-2 mesi"
        color = "Giallo"
    else:
        control_level = "NON CONTROLLATO"
        action = "Step-up terapeutico necessario"
        follow_up = "Controllo entro 2-4 settimane"
        color = "Rosso"
    
    result = f"""Valutazione Controllo Asma Pediatrico
====================================
Punteggio controllo: {control_score}/13

Livello di controllo: {control_level}
Zona semaforo: {color}
Azione raccomandata: {action}
Follow-up: {follow_up}

Parametri valutati:
- Sintomi diurni: {daytime_symptoms}/7 giorni per settimana
- Risvegli notturni: {nighttime_awakenings}/mese
- Uso broncodilatatore: {rescue_inhaler_use}/settimana
- Limitazione attività: {activity_limitation}
- Assenze scolastiche: {school_absences}/mese
- Riacutizzazioni recenti: {recent_exacerbations}/mese

Criteri controllo ottimale (tutti presenti):
- Sintomi diurni ≤2 giorni/settimana
- Risvegli notturni ≤2/mese
- Broncodilatatore ≤2 giorni/settimana
- Nessuna limitazione attività
- Nessuna riacutizzazione

Red flags per controllo insufficiente:
- Sintomi quotidiani
- Risvegli notturni frequenti (>1/settimana)
- Uso frequente broncodilatatore (>2/settimana)
- Limitazione significativa attività
- Riacutizzazioni multiple

Prossimi passi:
- Verificare tecnica inalatoria
- Valutare aderenza terapeutica
- Identificare trigger ambientali
- Considerare comorbidità (rinite, MRGE)
- Educazione paziente/famiglia
- Piano d'azione scritto personalizzato
"""
    return [types.TextContent(type="text", text=result)]

def _assess_heads_ed(args):
    """Valuta HEADS-ED per screening salute mentale pediatrica in pronto soccorso"""
    home = args.get('home', 0)
    education = args.get('education', 0)
    activities_peers = args.get('activities_peers', 0)
    drug_use = args.get('drug_use', 0)
    suicide = args.get('suicide', 0)
    emotions_behaviors = args.get('emotions_behaviors', 0)
    discharge_resources = args.get('discharge_resources', 0)
    
    # Calcolo punteggio totale
    total_score = home + education + activities_peers + drug_use + suicide + emotions_behaviors + discharge_resources
    
    # Valutazione delle componenti
    components = [
        f"• Home (ambiente familiare): {home}/2",
        f"• Education (scuola): {education}/2",
        f"• Activities/Peers (attività/pari): {activities_peers}/2",
        f"• Drug use (uso sostanze): {drug_use}/2",
        f"• Suicidality (suicidalità): {suicide}/2",
        f"• Emotions/Behaviors (emozioni/comportamenti): {emotions_behaviors}/2",
        f"• Discharge resources (risorse alla dimissione): {discharge_resources}/2"
    ]
    
    # Interpretazione
    if total_score <= 4:
        risk_level = "BASSO"
        disposition = "Dimissione con follow-up ambulatoriale"
    elif total_score <= 8:
        risk_level = "MODERATO"
        disposition = "Consulenza psichiatrica raccomandata, considerare ricovero"
    else:
        risk_level = "ALTO"
        disposition = "Consulenza psichiatrica urgente, probabile ricovero"
    
    # Flag per rischio suicidario
    suicide_alert = ""
    if suicide >= 1:
        suicide_alert = "\n⚠️ ATTENZIONE: Rischio suicidario presente - Valutazione urgente richiesta"
    
    result = f"""HEADS-ED (Screening Salute Mentale Pediatrica PS)
===============================================
Punteggio totale: {total_score}/14
Livello di rischio: {risk_level}
Disposizione: {disposition}{suicide_alert}

Componenti valutate:
{chr(10).join(components)}

Interpretazione punteggi:
- 0-4: Rischio basso - Follow-up ambulatoriale
- 5-8: Rischio moderato - Consulenza psichiatrica raccomandata
- >8: Rischio alto - Consulenza psichiatrica urgente

Note di utilizzo:
- Validato in pronto soccorso pediatrico
- Punteggio di ogni item: 0=nessun problema, 1=lieve, 2=moderato/severo
- Qualsiasi punteggio ≥1 per suicidalità richiede valutazione immediata
- Prioritizzare items con punteggio 2 per intervento immediato
- Non sostituisce valutazione clinica completa
"""
    return [types.TextContent(type="text", text=result)]

def _assess_pediatric_sleep(args):
    """Valuta BEARS per screening disturbi del sonno pediatrico"""
    age_years = args.get('age_years', 0)
    bedtime_problems = args.get('bedtime_problems', False)
    excessive_daytime_sleepiness = args.get('excessive_daytime_sleepiness', False)
    awakenings = args.get('awakenings', False)
    regularity = args.get('regularity', False)
    snoring = args.get('snoring', False)
    
    # Conteggio problemi del sonno
    problems_count = 0
    problems = []
    
    if bedtime_problems:
        problems_count += 1
        problems.append("• Problemi di addormentamento")
    if excessive_daytime_sleepiness:
        problems_count += 1
        problems.append("• Sonnolenza diurna eccessiva")
    if awakenings:
        problems_count += 1
        problems.append("• Risvegli notturni")
    if not regularity:
        problems_count += 1
        problems.append("• Irregolarità del sonno")
    if snoring:
        problems_count += 1
        problems.append("• Russamento/problemi respiratori")
    
    # Valori normali per età
    if age_years < 1:
        sleep_hours = "14-15 ore (inclusi sonnellini)"
        normal_pattern = "Sonnellini multipli, consolidamento notturno in sviluppo"
    elif age_years < 3:
        sleep_hours = "12-14 ore (incluso sonnellino)"
        normal_pattern = "1 sonnellino diurno, 10-12 ore notturne"
    elif age_years < 6:
        sleep_hours = "11-13 ore (alcuni sonnellino)"
        normal_pattern = "Sonnellino opzionale, sonno notturno consolidato"
    elif age_years < 12:
        sleep_hours = "10-11 ore"
        normal_pattern = "No sonnellini, sonno notturno consolidato"
    else:
        sleep_hours = "8-10 ore"
        normal_pattern = "Pattern sonno-veglia irregolare comune"
    
    # Interpretazione
    if problems_count == 0:
        assessment = "NORMALE"
        recommendation = "Nessun intervento necessario"
    elif problems_count == 1:
        assessment = "DISTURBO LIEVE"
        recommendation = "Igiene del sonno, rivalutazione al prossimo controllo"
    elif problems_count == 2:
        assessment = "DISTURBO MODERATO"
        recommendation = "Intervento su igiene del sonno, diario del sonno, follow-up"
    else:
        assessment = "DISTURBO SIGNIFICATIVO"
        recommendation = "Valutazione approfondita, considerare referral specialistico"
    
    result = f"""Screening Disturbi del Sonno Pediatrico (BEARS)
==========================================
Età: {age_years} anni
Problemi identificati: {problems_count}/5

Valutazione: {assessment}
Raccomandazione: {recommendation}

Problemi del sonno:
{chr(10).join(problems) if problems else '• Nessun problema identificato'}

Pattern normale per età:
- Ore di sonno raccomandate: {sleep_hours}
- Pattern tipico: {normal_pattern}

Aree valutate (BEARS):
B = Bedtime problems (problemi addormentamento)
E = Excessive daytime sleepiness (sonnolenza diurna)
A = Awakenings (risvegli notturni)
R = Regularity (regolarità sonno-veglia)
S = Snoring (russamento/disturbi respiratori)

Note cliniche:
- Screening semplice per setting ambulatoriale
- Se ≥3 problemi, valutare impatto su funzionamento
- Russamento persistente richiede valutazione OSAS
- Disturbi del sonno spesso correlati a problemi comportamentali
- Interventi educativi efficaci nella maggior parte dei casi
"""
    return [types.TextContent(type="text", text=result)]

# IMPLEMENTAZIONE DEI CRITERI ROME IV

def _assess_rome4_abdominal_migraine(args):
    """Valuta criteri Rome IV per emicrania addominale pediatrica"""
    episodes_abdominal_pain = args.get('episodes_abdominal_pain', False)
    episodes_duration_hours = args.get('episodes_duration_hours', 0)
    normal_between_episodes = args.get('normal_between_episodes', False)
    interferes_activities = args.get('interferes_activities', False)
    associated_symptoms = args.get('associated_symptoms', [])
    symptoms_duration_months = args.get('symptoms_duration_months', 0)
    episodes_count = args.get('episodes_count', 0)
    
    # Verifica criteri essenziali
    criteria_met = []
    criteria_not_met = []
    
    if episodes_abdominal_pain:
        criteria_met.append("• Episodi stereotipati di dolore addominale acuto periombelicale")
    else:
        criteria_not_met.append("• Episodi stereotipati di dolore addominale acuto periombelicale")
    
    if episodes_duration_hours >= 1:
        criteria_met.append(f"• Durata episodi: {episodes_duration_hours} ore")
    else:
        criteria_not_met.append("• Durata episodi ≥1 ora")
    
    if normal_between_episodes:
        criteria_met.append("• Ritorno allo stato di salute normale tra gli episodi")
    else:
        criteria_not_met.append("• Ritorno allo stato di salute normale tra gli episodi")
    
    if interferes_activities:
        criteria_met.append("• Dolore interferisce con attività quotidiane")
    else:
        criteria_not_met.append("• Dolore interferisce con attività quotidiane")
    
    # Verifica sintomi associati (almeno 2 richiesti)
    associated_symptoms_count = len(associated_symptoms)
    
    if associated_symptoms_count >= 2:
        criteria_met.append(f"• Presenza di {associated_symptoms_count} sintomi associati: {', '.join([s.replace('_', ' ') for s in associated_symptoms])}")
    else:
        criteria_not_met.append(f"• Presenza di almeno 2 sintomi associati (attualmente: {associated_symptoms_count})")
    
    # Verifica durata
    if symptoms_duration_months >= 6:
        criteria_met.append(f"• Durata dei sintomi: {symptoms_duration_months} mesi (≥6 mesi richiesti)")
    else:
        criteria_not_met.append(f"• Durata dei sintomi: {symptoms_duration_months} mesi (<6 mesi, richiesti ≥6 mesi)")
    
    # Verifica numero episodi
    if episodes_count >= 2:
        criteria_met.append(f"• Numero di episodi: {episodes_count} (≥2 richiesti)")
    else:
        criteria_not_met.append(f"• Numero di episodi: {episodes_count} (<2, richiesti ≥2)")
    
    # Valutazione criteri Rome IV
    rome_criteria_met = (
        episodes_abdominal_pain and 
        episodes_duration_hours >= 1 and 
        normal_between_episodes and 
        interferes_activities and 
        associated_symptoms_count >= 2 and 
        symptoms_duration_months >= 6 and 
        episodes_count >= 2
    )
    
    if rome_criteria_met:
        diagnosis = "CRITERI ROME IV SODDISFATTI"
        recommendation = "Diagnosi di emicrania addominale secondo Rome IV"
    else:
        diagnosis = "CRITERI ROME IV NON SODDISFATTI"
        if len(criteria_not_met) <= 2 and symptoms_duration_months >= 2:
            recommendation = "Possibile emicrania addominale in evoluzione, rivalutare"
        else:
            recommendation = "Considerare diagnosi alternative"
    
    result = f"""Criteri Rome IV per Emicrania Addominale Pediatrica
=================================================
Diagnosi: {diagnosis}
Raccomandazione: {recommendation}

Criteri soddisfatti:
{chr(10).join(criteria_met) if criteria_met else '• Nessun criterio soddisfatto'}

Criteri non soddisfatti:
{chr(10).join(criteria_not_met) if criteria_not_met else '• Tutti i criteri soddisfatti'}

Criteri Rome IV completi per l'emicrania addominale:
1. Episodi stereotipati di dolore addominale acuto periombelicale
2. Episodi separati da settimane/mesi di normalità
3. Dolore interferisce con attività quotidiane
4. Almeno 2 dei seguenti sintomi: anoressia, nausea, vomito, mal di testa, fotofobia, pallore
5. Sintomi presenti per almeno 6 mesi
6. Almeno 2 episodi di dolore

Diagnosi differenziali da considerare:
- Malattia infiammatoria intestinale
- Patologia delle vie biliari
- Patologia urinaria
- Dolore addominale funzionale
- Sindrome intestino irritabile

Note cliniche:
- Più comune in età scolare (7-12 anni)
- Spesso familiarità per emicrania
- Risposta a terapie antiemicraniche
- Possibile evoluzione in emicrania tipica in adolescenza
"""
    return [types.TextContent(type="text", text=result)]

def _assess_rome4_aerophagia(args):
    """Valuta criteri Rome IV per aerofagia pediatrica"""
    air_swallowing = args.get('air_swallowing', False)
    abdominal_distension = args.get('abdominal_distension', False)
    repetitive_belching = args.get('repetitive_belching', False)
    repetitive_flatulence = args.get('repetitive_flatulence', False)
    symptoms_duration_months = args.get('symptoms_duration_months', 0)
    symptoms_frequency_weekly = args.get('symptoms_frequency_weekly', 0)
    other_gi_conditions = args.get('other_gi_conditions', False)
    
    # Verifica criteri essenziali
    criteria_met = []
    criteria_not_met = []
    
    if air_swallowing:
        criteria_met.append("• Deglutizione eccessiva di aria")
    else:
        criteria_not_met.append("• Deglutizione eccessiva di aria")
    
    if abdominal_distension:
        criteria_met.append("• Distensione addominale dovuta all'aria")
    else:
        criteria_not_met.append("• Distensione addominale dovuta all'aria")
    
    if repetitive_belching or repetitive_flatulence:
        criteria_met.append("• Eruttazione e/o flatulenza ripetuta")
    else:
        criteria_not_met.append("• Eruttazione e/o flatulenza ripetuta")
    
    # Verifica frequenza
    if symptoms_frequency_weekly >= 2:
        criteria_met.append(f"• Frequenza dei sintomi: {symptoms_frequency_weekly} giorni/settimana (≥2 richiesti)")
    else:
        criteria_not_met.append(f"• Frequenza dei sintomi: {symptoms_frequency_weekly} giorni/settimana (<2, richiesti ≥2)")
    
    # Verifica durata
    if symptoms_duration_months >= 2:
        criteria_met.append(f"• Durata dei sintomi: {symptoms_duration_months} mesi (≥2 mesi richiesti)")
    else:
        criteria_not_met.append(f"• Durata dei sintomi: {symptoms_duration_months} mesi (<2, richiesti ≥2 mesi)")
    
    # Verifica esclusione altre condizioni
    if not other_gi_conditions:
        criteria_met.append("• Assenza di altre condizioni GI che spiegano i sintomi")
    else:
        criteria_not_met.append("• Presenza di altre condizioni GI che spiegano i sintomi")
    
    # Valutazione criteri Rome IV
    rome_criteria_met = (
        air_swallowing and 
        abdominal_distension and 
        (repetitive_belching or repetitive_flatulence) and 
        symptoms_frequency_weekly >= 2 and 
        symptoms_duration_months >= 2 and 
        not other_gi_conditions
    )
    
    if rome_criteria_met:
        diagnosis = "CRITERI ROME IV SODDISFATTI"
        recommendation = "Diagnosi di aerofagia secondo Rome IV"
    else:
        diagnosis = "CRITERI ROME IV NON SODDISFATTI"
        if len(criteria_not_met) <= 2 and symptoms_duration_months >= 1:
            recommendation = "Possibile aerofagia in evoluzione, rivalutare"
        else:
            recommendation = "Considerare diagnosi alternative"
    
    result = f"""Criteri Rome IV per Aerofagia Pediatrica
=======================================
Diagnosi: {diagnosis}
Raccomandazione: {recommendation}

Criteri soddisfatti:
{chr(10).join(criteria_met) if criteria_met else '• Nessun criterio soddisfatto'}

Criteri non soddisfatti:
{chr(10).join(criteria_not_met) if criteria_not_met else '• Tutti i criteri soddisfatti'}

Criteri Rome IV completi per l'aerofagia:
1. Deglutizione eccessiva di aria
2. Distensione addominale dovuta all'aria
3. Eruttazione e/o flatulenza ripetuta
4. Sintomi presenti almeno 2 giorni a settimana
5. Sintomi presenti per almeno 2 mesi
6. Sintomi non spiegati da altre condizioni mediche

Diagnosi differenziali da considerare:
- Disturbi funzionali GI (IBS, dispepsia)
- Malattia da reflusso gastroesofageo
- Intolleranze alimentari
- Patologie organiche GI

Note cliniche:
- Spesso associata a situazioni di stress/ansia
- Può essere inconsapevole o inconscia
- Più comune in bambini con disturbi del neurosviluppo
- Approccio terapeutico:
  * Educazione e rassicurazione
  * Tecniche comportamentali
  * Riduzione stress
  * Considerare supporto psicologico
"""
    return [types.TextContent(type="text", text=result)]

def _assess_rome4_constipation(args):
    """Valuta criteri Rome IV per stipsi funzionale pediatrica"""
    bowel_movements_weekly = args.get('bowel_movements_weekly', 0)
    fecal_incontinence = args.get('fecal_incontinence', False)
    stool_retention = args.get('stool_retention', False)
    painful_defecation = args.get('painful_defecation', False)
    large_fecal_mass = args.get('large_fecal_mass', False)
    large_diameter_stools = args.get('large_diameter_stools', False)
    symptoms_duration_months = args.get('symptoms_duration_months', 0)
    toilet_trained = args.get('toilet_trained', True)
    
    # Verifica numero criteri (richiesti almeno 2)
    criteria_count = 0
    criteria_present = []
    
    if bowel_movements_weekly < 2:
        criteria_count += 1
        criteria_present.append(f"• Meno di 2 defecazioni alla settimana (attuale: {bowel_movements_weekly})")
    
    if fecal_incontinence and toilet_trained:
        criteria_count += 1
        criteria_present.append("• Almeno 1 episodio di incontinenza fecale alla settimana")
    
    if stool_retention:
        criteria_count += 1
        criteria_present.append("• Storia di ritenzione fecale")
    
    if painful_defecation:
        criteria_count += 1
        criteria_present.append("• Storia di defecazione dolorosa o difficile")
    
    if large_fecal_mass:
        criteria_count += 1
        criteria_present.append("• Presenza di grande massa fecale nel retto")
    
    if large_diameter_stools:
        criteria_count += 1
        criteria_present.append("• Storia di feci di grande diametro")
    
    # Verifica durata
    duration_met = symptoms_duration_months >= 1
    
    # Valutazione criteri Rome IV
    rome_criteria_met = (criteria_count >= 2 and duration_met)
    
    if rome_criteria_met:
        diagnosis = "CRITERI ROME IV SODDISFATTI"
        recommendation = "Diagnosi di stipsi funzionale secondo Rome IV"
    else:
        diagnosis = "CRITERI ROME IV NON SODDISFATTI"
        if criteria_count >= 1 and symptoms_duration_months < 1:
            recommendation = "Possibile stipsi funzionale in evoluzione, rivalutare"
        else:
            recommendation = "Considerare diagnosi alternative"
    
    # Criteri non soddisfatti
    criteria_not_met = []
    if criteria_count < 2:
        criteria_not_met.append(f"• Presenti solo {criteria_count} criteri (richiesti almeno 2)")
    
    if not duration_met:
        criteria_not_met.append(f"• Durata dei sintomi: {symptoms_duration_months} mesi (<1, richiesto ≥1 mese)")
    
    result = f"""Criteri Rome IV per Stipsi Funzionale Pediatrica
=============================================
Diagnosi: {diagnosis}
Raccomandazione: {recommendation}

Criteri presenti ({criteria_count}/6):
{chr(10).join(criteria_present) if criteria_present else '• Nessun criterio presente'}

{'Criteri non soddisfatti:' if criteria_not_met else ''}
{chr(10).join(criteria_not_met) if criteria_not_met else ''}

Durata dei sintomi: {symptoms_duration_months} mesi (richiesto ≥1 mese)

Criteri Rome IV completi per la stipsi funzionale:
Almeno 2 dei seguenti criteri, presenti per almeno 1 mese:
1. Meno di 2 defecazioni alla settimana
2. Almeno 1 episodio di incontinenza fecale alla settimana (dopo acquisizione continenza)
3. Storia di posture o comportamenti di ritenzione fecale
4. Storia di defecazione dolorosa o difficile
5. Presenza di grande massa fecale nel retto
6. Storia di feci di grande diametro

Note cliniche:
- Nei bambini con continenza, l'incontinenza è quasi sempre secondaria a ritenzione
- Importante escludere cause organiche, specialmente nei lattanti
- Anamnesi perinatale e familiare importanti
- Elementi diagnostici aggiuntivi: DRE, diario evacuativo
- Trattamento: educazione, dieta, disimpatto se necessario, lassativi

Red flags per cause organiche:
- Ritardo di crescita
- Insorgenza molto precoce (<1 mese di vita)
- Sangue nelle feci senza ragade
- Febbre o vomito
- Alterazioni neurologiche
- Alterazioni alla regione sacrale
"""
    return [types.TextContent(type="text", text=result)]

def _assess_rome4_cyclic_vomiting(args):
    """Valuta criteri Rome IV per sindrome del vomito ciclico pediatrica"""
    stereotypical_episodes = args.get('stereotypical_episodes', False)
    episodes_duration_hours = args.get('episodes_duration_hours', 0)
    episodes_count = args.get('episodes_count', 0)
    return_to_baseline = args.get('return_to_baseline', False)
    symptoms_duration_months = args.get('symptoms_duration_months', 0)
    vomiting_frequency = args.get('vomiting_frequency', 0)
    other_gi_conditions = args.get('other_gi_conditions', False)
    
    # Verifica criteri essenziali
    criteria_met = []
    criteria_not_met = []
    
    if stereotypical_episodes:
        criteria_met.append("• Episodi stereotipati di vomito intenso")
    else:
        criteria_not_met.append("• Episodi stereotipati di vomito intenso")
    
    if episodes_duration_hours >= 1:
        criteria_met.append(f"• Durata episodi: {episodes_duration_hours} ore")
    else:
        criteria_not_met.append("• Durata episodi ≥1 ora")
    
    if episodes_count >= 2:
        criteria_met.append(f"• Numero di episodi: {episodes_count} (≥2 richiesti)")
    else:
        criteria_not_met.append(f"• Numero di episodi: {episodes_count} (<2, richiesti ≥2)")
    
    if return_to_baseline:
        criteria_met.append("• Ritorno allo stato di salute normale tra gli episodi")
    else:
        criteria_not_met.append("• Ritorno allo stato di salute normale tra gli episodi")
    
    # Verifica durata
    if symptoms_duration_months >= 6:
        criteria_met.append(f"• Durata dei sintomi: {symptoms_duration_months} mesi (≥6 mesi richiesti)")
    else:
        criteria_not_met.append(f"• Durata dei sintomi: {symptoms_duration_months} mesi (<6, richiesti ≥6 mesi)")
    
    # Verifica frequenza vomito
    if vomiting_frequency >= 4:
        criteria_met.append(f"• Frequenza vomito durante episodi: {vomiting_frequency} episodi/ora (≥4 richiesti)")
    else:
        criteria_not_met.append(f"• Frequenza vomito durante episodi: {vomiting_frequency} episodi/ora (<4, richiesti ≥4)")
    
    # Verifica esclusione altre condizioni
    if not other_gi_conditions:
        criteria_met.append("• Assenza di altre condizioni GI che spiegano i sintomi")
    else:
        criteria_not_met.append("• Presenza di altre condizioni GI che spiegano i sintomi")
    
    # Valutazione criteri Rome IV
    rome_criteria_met = (
        stereotypical_episodes and 
        episodes_duration_hours >= 1 and 
        episodes_count >= 2 and 
        return_to_baseline and 
        symptoms_duration_months >= 6 and 
        vomiting_frequency >= 4 and 
        not other_gi_conditions
    )
    
    if rome_criteria_met:
        diagnosis = "CRITERI ROME IV SODDISFATTI"
        recommendation = "Diagnosi di sindrome del vomito ciclico secondo Rome IV"
    else:
        diagnosis = "CRITERI ROME IV NON SODDISFATTI"
        if len(criteria_not_met) <= 2 and symptoms_duration_months >= 2:
            recommendation = "Possibile sindrome del vomito ciclico in evoluzione, rivalutare"
        else:
            recommendation = "Considerare diagnosi alternative"
    
    result = f"""Criteri Rome IV per Sindrome del Vomito Ciclico Pediatrica
======================================================
Diagnosi: {diagnosis}
Raccomandazione: {recommendation}

Criteri soddisfatti:
{chr(10).join(criteria_met) if criteria_met else '• Nessun criterio soddisfatto'}

Criteri non soddisfatti:
{chr(10).join(criteria_not_met) if criteria_not_met else '• Tutti i criteri soddisfatti'}

Criteri Rome IV completi per la sindrome del vomito ciclico:
1. Episodi stereotipati di vomito intenso e acuto
2. Durata episodi 1 ora - 10 giorni
3. Almeno 2 episodi in un periodo di 6 mesi
4. Ritorno allo stato di salute normale tra gli episodi
5. Sintomi presenti per almeno 6 mesi
6. Frequenza del vomito durante gli episodi ≥4 volte/ora
7. Sintomi non spiegati da altre condizioni mediche

Diagnosi differenziali da considerare:
- Patologia del SNC (tumori, ipertensione endocranica)
- Patologie metaboliche/endocrine
- Patologie ostruttive gastrointestinali
- Disturbi alimentari
- Malrotazione intestinale/volvolo intermittente

Note cliniche:
- Spesso esordio stereotipato (stessi orari, stessi sintomi)
- Tipici prodromi: pallore, letargia, nausea, anoressia
- Associata a disturbi del movimento (mal d'auto)
- Spesso familiarità per emicrania
- Possibili trigger: stress, infezioni, mestruazioni, alimenti
- Considerare consulenza neurologica
"""
    return [types.TextContent(type="text", text=result)]

def _assess_rome4_functional_abdominal_pain(args):
    """Valuta criteri Rome IV per dolore addominale funzionale pediatrico - non altrimenti specificato"""
    abdominal_pain_frequency = args.get('abdominal_pain_frequency', 0)
    continuous_pain = args.get('continuous_pain', False)
    meets_ibs_criteria = args.get('meets_ibs_criteria', False)
    meets_dyspepsia_criteria = args.get('meets_dyspepsia_criteria', False)
    meets_abdominal_migraine_criteria = args.get('meets_abdominal_migraine_criteria', False)
    symptoms_duration_months = args.get('symptoms_duration_months', 0)
    inflammatory_condition = args.get('inflammatory_condition', False)
    
    # Verifica criteri essenziali
    criteria_met = []
    criteria_not_met = []
    
    # Frequenza del dolore
    pain_frequency_met = abdominal_pain_frequency >= 4 or continuous_pain
    if pain_frequency_met:
        if continuous_pain:
            criteria_met.append("• Dolore addominale continuo")
        else:
            criteria_met.append(f"• Dolore addominale almeno 4 giorni/settimana (attuale: {abdominal_pain_frequency})")
    else:
        criteria_not_met.append(f"• Dolore addominale <4 giorni/settimana (attuale: {abdominal_pain_frequency}) e non continuo")
    
    # Non soddisfa criteri per altre condizioni
    other_conditions_met = not (meets_ibs_criteria or meets_dyspepsia_criteria or meets_abdominal_migraine_criteria)
    if other_conditions_met:
        criteria_met.append("• Non soddisfa criteri per IBS, dispepsia funzionale o emicrania addominale")
    else:
        criteria_not_met.append("• Soddisfa criteri per IBS, dispepsia funzionale o emicrania addominale")
    
    # Verifica durata
    duration_met = symptoms_duration_months >= 2
    if duration_met:
        criteria_met.append(f"• Durata dei sintomi: {symptoms_duration_months} mesi (≥2 mesi richiesti)")
    else:
        criteria_not_met.append(f"• Durata dei sintomi: {symptoms_duration_months} mesi (<2, richiesti ≥2 mesi)")
    
    # Verifica esclusione processi infiammatori
    if not inflammatory_condition:
        criteria_met.append("• Assenza di processi infiammatori, anatomici, metabolici o neoplastici")
    else:
        criteria_not_met.append("• Presenza di processi infiammatori, anatomici, metabolici o neoplastici")
    
    # Valutazione criteri Rome IV
    rome_criteria_met = (
        pain_frequency_met and 
        other_conditions_met and 
        duration_met and 
        not inflammatory_condition
    )
    
    if rome_criteria_met:
        diagnosis = "CRITERI ROME IV SODDISFATTI"
        recommendation = "Diagnosi di dolore addominale funzionale - NOS secondo Rome IV"
    else:
        diagnosis = "CRITERI ROME IV NON SODDISFATTI"
        if pain_frequency_met and other_conditions_met and not inflammatory_condition and symptoms_duration_months >= 1:
            recommendation = "Possibile dolore addominale funzionale in evoluzione, rivalutare"
        else:
            recommendation = "Considerare diagnosi alternative"
    
    result = f"""Criteri Rome IV per Dolore Addominale Funzionale - NOS
======================================================
Diagnosi: {diagnosis}
Raccomandazione: {recommendation}

Criteri soddisfatti:
{chr(10).join(criteria_met) if criteria_met else '• Nessun criterio soddisfatto'}

Criteri non soddisfatti:
{chr(10).join(criteria_not_met) if criteria_not_met else '• Tutti i criteri soddisfatti'}

Criteri Rome IV completi per dolore addominale funzionale - NOS:
1. Dolore addominale almeno 4 giorni/settimana o continuo
2. Non soddisfa criteri per IBS, dispepsia funzionale o emicrania addominale
3. Sintomi presenti per almeno 2 mesi
4. Assenza di processi infiammatori, anatomici, metabolici o neoplastici

Diagnosi differenziali da considerare:
- Sindrome dell'intestino irritabile
- Dispepsia funzionale
- Emicrania addominale
- Malattia infiammatoria intestinale
- Malattia celiaca
- Patologie delle vie biliari
- Patologie urinarie
- Intolleranze alimentari

Note cliniche:
- Diagnosi di esclusione dopo valutazione appropriata
- Importanza di una buona anamnesi ed esame obiettivo
- Considerare red flags per patologie organiche
- Approccio biopsicosociale al trattamento
- Educazione del paziente e della famiglia
- Terapia cognitivo-comportamentale spesso efficace
"""
    return [types.TextContent(type="text", text=result)]

def _assess_rome4_functional_dyspepsia(args):
    """Valuta criteri Rome IV per dispepsia funzionale pediatrica"""
    bothersome_postprandial_fullness = args.get('bothersome_postprandial_fullness', False)
    early_satiety = args.get('early_satiety', False)
    epigastric_pain = args.get('epigastric_pain', False)
    epigastric_burning = args.get('epigastric_burning', False)
    symptoms_duration_months = args.get('symptoms_duration_months', 0)
    symptoms_frequency_weekly = args.get('symptoms_frequency_weekly', 0)
    organic_disease = args.get('organic_disease', False)
    
    # Verifica presenza di almeno un sintomo
    has_symptoms = bothersome_postprandial_fullness or early_satiety or epigastric_pain or epigastric_burning
    
    # Verifica criteri essenziali
    criteria_met = []
    criteria_not_met = []
    
    symptoms_list = []
    if bothersome_postprandial_fullness:
        symptoms_list.append("pienezza postprandiale fastidiosa")
    if early_satiety:
        symptoms_list.append("sazietà precoce")
    if epigastric_pain:
        symptoms_list.append("dolore epigastrico")
    if epigastric_burning:
        symptoms_list.append("bruciore epigastrico")
    
    if has_symptoms:
        criteria_met.append(f"• Presenza di almeno un sintomo: {', '.join(symptoms_list)}")
    else:
        criteria_not_met.append("• Mancanza di sintomi dispeptici (pienezza postprandiale, sazietà precoce, dolore/bruciore epigastrico)")
    
    # Verifica frequenza
    if symptoms_frequency_weekly >= 4:
        criteria_met.append(f"• Frequenza dei sintomi: {symptoms_frequency_weekly} giorni/settimana (≥4 richiesti)")
    else:
        criteria_not_met.append(f"• Frequenza dei sintomi: {symptoms_frequency_weekly} giorni/settimana (<4, richiesti ≥4)")
    
    # Verifica durata
    if symptoms_duration_months >= 2:
        criteria_met.append(f"• Durata dei sintomi: {symptoms_duration_months} mesi (≥2 mesi richiesti)")
    else:
        criteria_not_met.append(f"• Durata dei sintomi: {symptoms_duration_months} mesi (<2, richiesti ≥2 mesi)")
    
    # Verifica esclusione malattie organiche
    if not organic_disease:
        criteria_met.append("• Assenza di malattie organiche che spiegano i sintomi")
    else:
        criteria_not_met.append("• Presenza di malattie organiche che spiegano i sintomi")
    
    # Valutazione criteri Rome IV
    rome_criteria_met = (
        has_symptoms and 
        symptoms_frequency_weekly >= 4 and 
        symptoms_duration_months >= 2 and 
        not organic_disease
    )
    
    # Sottotipi
    subtype = "Non classificabile"
    if rome_criteria_met:
        if bothersome_postprandial_fullness or early_satiety:
            if epigastric_pain or epigastric_burning:
                subtype = "Sindrome da distress postprandiale e sindrome da dolore epigastrico (Overlap)"
            else:
                subtype = "Sindrome da distress postprandiale"
        elif epigastric_pain or epigastric_burning:
            subtype = "Sindrome da dolore epigastrico"
    
    if rome_criteria_met:
        diagnosis = "CRITERI ROME IV SODDISFATTI"
        recommendation = f"Diagnosi di dispepsia funzionale ({subtype}) secondo Rome IV"
    else:
        diagnosis = "CRITERI ROME IV NON SODDISFATTI"
        if has_symptoms and not organic_disease and symptoms_duration_months >= 1:
            recommendation = "Possibile dispepsia funzionale in evoluzione, rivalutare"
        else:
            recommendation = "Considerare diagnosi alternative"
    
    result = f"""Criteri Rome IV per Dispepsia Funzionale Pediatrica
=================================================
Diagnosi: {diagnosis}
Raccomandazione: {recommendation}
Sottotipo: {subtype}

Criteri soddisfatti:
{chr(10).join(criteria_met) if criteria_met else '• Nessun criterio soddisfatto'}

Criteri non soddisfatti:
{chr(10).join(criteria_not_met) if criteria_not_met else '• Tutti i criteri soddisfatti'}

Criteri Rome IV completi per dispepsia funzionale:
1. Uno o più dei seguenti sintomi:
   - Pienezza postprandiale fastidiosa
   - Sazietà precoce
   - Dolore epigastrico
   - Bruciore epigastrico
2. Sintomi presenti almeno 4 giorni a settimana
3. Sintomi presenti per almeno 2 mesi
4. Assenza di malattie organiche che spiegano i sintomi

Sottotipi:
- Sindrome da distress postprandiale: pienezza postprandiale e/o sazietà precoce
- Sindrome da dolore epigastrico: dolore e/o bruciore epigastrico
- Overlap: caratteristiche di entrambi i sottotipi

Diagnosi differenziali da considerare:
- Malattia da reflusso gastroesofageo
- Gastroparesi
- Ulcera peptica
- Malattia celiaca
- Infezione da H. pylori
- Patologie biliari
- Pancreatite

Note cliniche:
- Considerare endoscopia in presenza di red flags
- Valutare test per H. pylori
- Approccio terapeutico basato sul sottotipo
- Considerare modifiche dietetiche e stile di vita
- Farmaci: IPP, procinetici, antiacidi
- Supporto psicologico se componente ansiosa
"""
    return [types.TextContent(type="text", text=result)]

def _assess_rome4_functional_nausea_vomiting(args):
    """Valuta criteri Rome IV per nausea e vomito funzionali pediatrici"""
    bothersome_nausea = args.get('bothersome_nausea', False)
    weekly_vomiting_episodes = args.get('weekly_vomiting_episodes', 0)
    meal_related = args.get('meal_related', False)
    induced_vomiting = args.get('induced_vomiting', False)
    meets_eating_disorder_criteria = args.get('meets_eating_disorder_criteria', False)
    meets_rumination_criteria = args.get('meets_rumination_criteria', False)
    meets_cyclic_vomiting_criteria = args.get('meets_cyclic_vomiting_criteria', False)
    symptoms_duration_months = args.get('symptoms_duration_months', 0)
    organic_disease = args.get('organic_disease', False)
    
    # Verifica criteri essenziali
    criteria_met = []
    criteria_not_met = []
    
    # Nausea o vomito
    has_nausea_or_vomiting = bothersome_nausea or weekly_vomiting_episodes > 0
    if has_nausea_or_vomiting:
        if bothersome_nausea:
            criteria_met.append("• Nausea fastidiosa come sintomo predominante")
        if weekly_vomiting_episodes > 0:
            criteria_met.append(f"• Episodi di vomito: {weekly_vomiting_episodes} a settimana")
    else:
        criteria_not_met.append("• Mancanza di nausea fastidiosa o vomito")
    
    # Frequenza dei sintomi
    frequency_met = bothersome_nausea or weekly_vomiting_episodes >= 1
    if not frequency_met:
        criteria_not_met.append("• Frequenza di nausea/vomito insufficiente")
    
    # Non soddisfa criteri per altre condizioni
    other_conditions_met = not (meets_eating_disorder_criteria or meets_rumination_criteria or meets_cyclic_vomiting_criteria or induced_vomiting)
    if other_conditions_met:
        criteria_met.append("• Non soddisfa criteri per disturbi alimentari, sindrome di ruminazione o vomito ciclico")
    else:
        if meets_eating_disorder_criteria:
            criteria_not_met.append("• Soddisfa criteri per disturbi alimentari")
        if meets_rumination_criteria:
            criteria_not_met.append("• Soddisfa criteri per sindrome di ruminazione")
        if meets_cyclic_vomiting_criteria:
            criteria_not_met.append("• Soddisfa criteri per sindrome del vomito ciclico")
        if induced_vomiting:
            criteria_not_met.append("• Vomito autoindotto")
    
    # Verifica durata
    if symptoms_duration_months >= 2:
        criteria_met.append(f"• Durata dei sintomi: {symptoms_duration_months} mesi (≥2 mesi richiesti)")
    else:
        criteria_not_met.append(f"• Durata dei sintomi: {symptoms_duration_months} mesi (<2, richiesti ≥2 mesi)")
    
    # Verifica esclusione malattie organiche
    if not organic_disease:
        criteria_met.append("• Assenza di malattie organiche che spiegano i sintomi")
    else:
        criteria_not_met.append("• Presenza di malattie organiche che spiegano i sintomi")
    
    # Sottotipo
    subtype = ""
    if bothersome_nausea and weekly_vomiting_episodes < 1:
        subtype = "Nausea funzionale"
    elif weekly_vomiting_episodes >= 1:
        subtype = "Vomito funzionale"
    
    # Valutazione criteri Rome IV
    rome_criteria_met = (
        has_nausea_or_vomiting and 
        frequency_met and 
        other_conditions_met and 
        symptoms_duration_months >= 2 and 
        not organic_disease
    )
    
    if rome_criteria_met:
        diagnosis = "CRITERI ROME IV SODDISFATTI"
        recommendation = f"Diagnosi di {subtype} secondo Rome IV"
    else:
        diagnosis = "CRITERI ROME IV NON SODDISFATTI"
        if has_nausea_or_vomiting and other_conditions_met and not organic_disease and symptoms_duration_months >= 1:
            recommendation = "Possibile nausea/vomito funzionale in evoluzione, rivalutare"
        else:
            recommendation = "Considerare diagnosi alternative"
    
    result = f"""Criteri Rome IV per Nausea e Vomito Funzionali Pediatrici
=====================================================
Diagnosi: {diagnosis}
Raccomandazione: {recommendation}
Sottotipo: {subtype}

Criteri soddisfatti:
{chr(10).join(criteria_met) if criteria_met else '• Nessun criterio soddisfatto'}

Criteri non soddisfatti:
{chr(10).join(criteria_not_met) if criteria_not_met else '• Tutti i criteri soddisfatti'}

Criteri Rome IV completi per nausea e vomito funzionali:
1. Nausea fastidiosa come sintomo predominante e/o episodi di vomito
2. Sintomi presenti almeno 2 volte a settimana (nausea) o almeno 1 volta a settimana (vomito)
3. Non soddisfa criteri per disturbi alimentari, sindrome di ruminazione o vomito ciclico
4. Vomito non autoindotto
5. Sintomi presenti per almeno 2 mesi
6. Assenza di malattie organiche che spiegano i sintomi

Sottotipi:
- Nausea funzionale: nausea come sintomo predominante, almeno 2 volte/settimana
- Vomito funzionale: almeno 1 episodio di vomito/settimana

Diagnosi differenziali da considerare:
- Malattia da reflusso gastroesofageo
- Patologie del SNC
- Patologie metaboliche/endocrine
- Disturbi alimentari
- Gastroparesi
- Patologie delle vie biliari
- Sindrome da vomito ciclico
- Sindrome di ruminazione

Note cliniche:
- Considerare relazione con stress/ansia
- Importante esame neurologico completo
- Valutare red flags per patologie organiche
- Approccio terapeutico: farmacologico e psicologico
- Considerare terapie complementari (agopuntura, biofeedback)
"""
    return [types.TextContent(type="text", text=result)]

def _assess_rome4_ibs(args):
    """Valuta criteri Rome IV per sindrome dell'intestino irritabile pediatrica"""
    abdominal_pain_days_monthly = args.get('abdominal_pain_days_monthly', 0)
    pain_related_to_defecation = args.get('pain_related_to_defecation', False)
    stool_frequency_change = args.get('stool_frequency_change', False)
    stool_form_change = args.get('stool_form_change', False)
    symptoms_duration_months = args.get('symptoms_duration_months', 0)
    predominant_stool_pattern = args.get('predominant_stool_pattern', 'unspecified')
    organic_disease = args.get('organic_disease', False)
    
    # Verifica criteri essenziali
    criteria_met = []
    criteria_not_met = []
    
    # Dolore addominale
    if abdominal_pain_days_monthly >= 4:
        criteria_met.append(f"• Dolore addominale almeno 4 giorni al mese (attuale: {abdominal_pain_days_monthly})")
    else:
        criteria_not_met.append(f"• Dolore addominale <4 giorni al mese (attuale: {abdominal_pain_days_monthly}, richiesto ≥4)")
    
    # Relazione con defecazione
    defecation_related = pain_related_to_defecation or stool_frequency_change or stool_form_change
    defecation_criteria = []
    
    if pain_related_to_defecation:
        defecation_criteria.append("dolore associato alla defecazione")
    if stool_frequency_change:
        defecation_criteria.append("cambio nella frequenza delle feci")
    if stool_form_change:
        defecation_criteria.append("cambio nella forma/consistenza delle feci")
    
    if defecation_related:
        criteria_met.append(f"• Dolore associato a: {', '.join(defecation_criteria)}")
    else:
        criteria_not_met.append("• Dolore non associato a defecazione, frequenza o consistenza delle feci")
    
    # Verifica durata
    if symptoms_duration_months >= 2:
        criteria_met.append(f"• Durata dei sintomi: {symptoms_duration_months} mesi (≥2 mesi richiesti)")
    else:
        criteria_not_met.append(f"• Durata dei sintomi: {symptoms_duration_months} mesi (<2, richiesti ≥2 mesi)")
    
    # Verifica esclusione malattie organiche
    if not organic_disease:
        criteria_met.append("• Assenza di malattie organiche che spiegano i sintomi")
    else:
        criteria_not_met.append("• Presenza di malattie organiche che spiegano i sintomi")
    
    # Valutazione criteri Rome IV
    rome_criteria_met = (
        abdominal_pain_days_monthly >= 4 and 
        defecation_related and 
        symptoms_duration_months >= 2 and 
        not organic_disease
    )
    
    # Sottotipo IBS
    subtype_display = {
        'constipation': "IBS con stipsi predominante (IBS-C)",
        'diarrhea': "IBS con diarrea predominante (IBS-D)",
        'mixed': "IBS con pattern misto (IBS-M)",
        'unspecified': "IBS non classificato (IBS-U)"
    }
    
    if rome_criteria_met:
        diagnosis = "CRITERI ROME IV SODDISFATTI"
        recommendation = f"Diagnosi di sindrome dell'intestino irritabile ({subtype_display[predominant_stool_pattern]}) secondo Rome IV"
    else:
        diagnosis = "CRITERI ROME IV NON SODDISFATTI"
        if abdominal_pain_days_monthly >= 2 and defecation_related and not organic_disease and symptoms_duration_months >= 1:
            recommendation = "Possibile IBS in evoluzione, rivalutare"
        else:
            recommendation = "Considerare diagnosi alternative"
    
    result = f"""Criteri Rome IV per Sindrome dell'Intestino Irritabile Pediatrica (IBS)
==================================================================
Diagnosi: {diagnosis}
Raccomandazione: {recommendation}
Sottotipo: {subtype_display[predominant_stool_pattern]}

Criteri soddisfatti:
{chr(10).join(criteria_met) if criteria_met else '• Nessun criterio soddisfatto'}

Criteri non soddisfatti:
{chr(10).join(criteria_not_met) if criteria_not_met else '• Tutti i criteri soddisfatti'}

Criteri Rome IV completi per IBS:
1. Dolore addominale almeno 4 giorni al mese
2. Dolore associato a uno o più dei seguenti:
   - Defecazione
   - Cambio nella frequenza delle feci
   - Cambio nella forma/consistenza delle feci
3. Sintomi presenti per almeno 2 mesi
4. Assenza di malattie organiche che spiegano i sintomi

Sottotipi di IBS:
- IBS-C: Stipsi predominante (>25% feci tipo 1-2 Bristol, <25% tipo 6-7)
- IBS-D: Diarrea predominante (>25% feci tipo 6-7 Bristol, <25% tipo 1-2)
- IBS-M: Pattern misto (>25% feci tipo 1-2 e >25% tipo 6-7)
- IBS-U: Non classificato (criteri IBS soddisfatti ma pattern fecale non classificabile)

Diagnosi differenziali da considerare:
- Malattia infiammatoria intestinale
- Malattia celiaca
- Intolleranza al lattosio/fruttosio
- Stipsi funzionale
- Allergie alimentari
- Infezioni gastrointestinali
- Dolore addominale funzionale

Note cliniche:
- Approccio terapeutico:
  * Educazione e rassicurazione
  * Modifiche dietetiche (FODMAP)
  * Gestione dello stress
  * Farmaci sintomatici specifici per sottotipo
- Considerare supporto psicologico
- Follow-up regolare
"""
    return [types.TextContent(type="text", text=result)]

def _assess_rome4_nonretentive_fecal_incontinence(args):
    """Valuta criteri Rome IV per incontinenza fecale non ritentiva pediatrica"""
    defecation_inappropriate_places = args.get('defecation_inappropriate_places', False)
    fecal_incontinence_frequency = args.get('fecal_incontinence_frequency', 0)
    developmental_age_at_least_4 = args.get('developmental_age_at_least_4', False)
    toilet_trained = args.get('toilet_trained', False)
    fecal_retention = args.get('fecal_retention', False)
    symptoms_duration_months = args.get('symptoms_duration_months', 0)
    organic_disease = args.get('organic_disease', False)
    
    # Verifica criteri essenziali
    criteria_met = []
    criteria_not_met = []
    
    # Evacuazione in luoghi inappropriati
    if defecation_inappropriate_places:
        criteria_met.append("• Defecazione in luoghi inappropriati")
    else:
        criteria_not_met.append("• Mancanza di defecazione in luoghi inappropriati")
    
    # Frequenza dell'incontinenza
    if fecal_incontinence_frequency >= 1:
        criteria_met.append(f"• Frequenza incontinenza fecale: {fecal_incontinence_frequency} giorni/mese (≥1 richiesto)")
    else:
        criteria_not_met.append(f"• Frequenza incontinenza fecale: {fecal_incontinence_frequency} giorni/mese (<1, richiesto ≥1)")
    
    # Età di sviluppo
    if developmental_age_at_least_4:
        criteria_met.append("• Età di sviluppo di almeno 4 anni")
    else:
        criteria_not_met.append("• Età di sviluppo <4 anni")
    
    # Training toilette
    if toilet_trained:
        criteria_met.append("• Training toilette completato")
    else:
        criteria_not_met.append("• Training toilette non completato")
    
    # Esclusione ritenzione fecale
    if not fecal_retention:
        criteria_met.append("• Assenza di ritenzione fecale")
    else:
        criteria_not_met.append("• Presenza di ritenzione fecale")
    
    # Verifica durata
    if symptoms_duration_months >= 1:
        criteria_met.append(f"• Durata dei sintomi: {symptoms_duration_months} mesi (≥1 mese richiesto)")
    else:
        criteria_not_met.append(f"• Durata dei sintomi: {symptoms_duration_months} mesi (<1, richiesto ≥1 mese)")
    
    # Verifica esclusione malattie organiche
    if not organic_disease:
        criteria_met.append("• Assenza di malattie organiche che spiegano i sintomi")
    else:
        criteria_not_met.append("• Presenza di malattie organiche che spiegano i sintomi")
    
    # Valutazione criteri Rome IV
    rome_criteria_met = (
        defecation_inappropriate_places and 
        fecal_incontinence_frequency >= 1 and 
        developmental_age_at_least_4 and 
        toilet_trained and 
        not fecal_retention and 
        symptoms_duration_months >= 1 and 
        not organic_disease
    )
    
    if rome_criteria_met:
        diagnosis = "CRITERI ROME IV SODDISFATTI"
        recommendation = "Diagnosi di incontinenza fecale non ritentiva secondo Rome IV"
    else:
        diagnosis = "CRITERI ROME IV NON SODDISFATTI"
        if fecal_retention:
            recommendation = "Considerare stipsi funzionale con incontinenza da overflow"
        elif not toilet_trained or not developmental_age_at_least_4:
            recommendation = "Completare training toilette, rivalutare"
        else:
            recommendation = "Considerare diagnosi alternative"
    
    result = f"""Criteri Rome IV per Incontinenza Fecale Non Ritentiva Pediatrica
==============================================================
Diagnosi: {diagnosis}
Raccomandazione: {recommendation}

Criteri soddisfatti:
{chr(10).join(criteria_met) if criteria_met else '• Nessun criterio soddisfatto'}

Criteri non soddisfatti:
{chr(10).join(criteria_not_met) if criteria_not_met else '• Tutti i criteri soddisfatti'}

Criteri Rome IV completi per incontinenza fecale non ritentiva:
1. Defecazione in luoghi inappropriati al contesto sociale
2. Almeno un episodio al mese
3. Età cronologica o di sviluppo di almeno 4 anni
4. Bambino ha completato training toilette
5. Assenza di evidenza di ritenzione fecale
6. Sintomi presenti per almeno 1 mese
7. Assenza di malattie organiche che spiegano i sintomi

Diagnosi differenziali da considerare:
- Stipsi funzionale con incontinenza da overflow
- Diarrea cronica
- Disturbi neurogenici dell'intestino
- Malattie infiammatorie intestinali
- Disturbi comportamentali
- Abuso sessuale

Note cliniche:
- Distinzione chiave da stipsi con overflow: assenza di ritenzione
- Importante valutazione psicologica e comportamentale
- Approccio terapeutico:
  * Educazione famiglia e bambino
  * Programma di allenamento intestinale
  * Rinforzo positivo
  * Terapia comportamentale
- Considerare stress psicosociale
- Prognosi generalmente favorevole con intervento precoce
"""
    return [types.TextContent(type="text", text=result)]

def _assess_rome4_rumination_syndrome(args):
    """Valuta criteri Rome IV per sindrome di ruminazione pediatrica"""
    repeated_regurgitation = args.get('repeated_regurgitation', False)
    regurgitation_not_preceded_by_retching = args.get('regurgitation_not_preceded_by_retching', False)
    regurgitation_within_30min_after_meal = args.get('regurgitation_within_30min_after_meal', False)
    regurgitation_not_improved_with_acid_suppression = args.get('regurgitation_not_improved_with_acid_suppression', False)
    symptoms_duration_months = args.get('symptoms_duration_months', 0)
    symptoms_frequency_weekly = args.get('symptoms_frequency_weekly', 0)
    organic_disease = args.get('organic_disease', False)
    
    # Verifica criteri essenziali
    criteria_met = []
    criteria_not_met = []
    
    # Rigurgito ripetuto
    if repeated_regurgitation:
        criteria_met.append("• Rigurgito ripetuto e senza sforzo di cibo parzialmente digerito")
    else:
        criteria_not_met.append("• Mancanza di rigurgito ripetuto di cibo")
    
    # Caratteristiche del rigurgito
    if regurgitation_not_preceded_by_retching:
        criteria_met.append("• Rigurgito non preceduto da nausea o conati")
    else:
        criteria_not_met.append("• Rigurgito preceduto da nausea o conati")
    
    if regurgitation_within_30min_after_meal:
        criteria_met.append("• Inizio entro 30 minuti dal pasto")
    else:
        criteria_not_met.append("• Inizio non entro 30 minuti dal pasto")
    
    if regurgitation_not_improved_with_acid_suppression:
        criteria_met.append("• Non migliora con terapie standard per reflusso")
    else:
        criteria_not_met.append("• Migliora con terapie standard per reflusso")
    
    # Verifica frequenza
    if symptoms_frequency_weekly >= 2:
        criteria_met.append(f"• Frequenza dei sintomi: {symptoms_frequency_weekly} giorni/settimana (≥2 richiesti)")
    else:
        criteria_not_met.append(f"• Frequenza dei sintomi: {symptoms_frequency_weekly} giorni/settimana (<2, richiesti ≥2)")
    
    # Verifica durata
    if symptoms_duration_months >= 2:
        criteria_met.append(f"• Durata dei sintomi: {symptoms_duration_months} mesi (≥2 mesi richiesti)")
    else:
        criteria_not_met.append(f"• Durata dei sintomi: {symptoms_duration_months} mesi (<2, richiesti ≥2 mesi)")
    
    # Verifica esclusione malattie organiche
    if not organic_disease:
        criteria_met.append("• Assenza di malattie organiche che spiegano i sintomi")
    else:
        criteria_not_met.append("• Presenza di malattie organiche che spiegano i sintomi")
    
    # Valutazione criteri Rome IV
    rome_criteria_met = (
        repeated_regurgitation and 
        regurgitation_not_preceded_by_retching and 
        regurgitation_within_30min_after_meal and 
        regurgitation_not_improved_with_acid_suppression and 
        symptoms_frequency_weekly >= 2 and 
        symptoms_duration_months >= 2 and 
        not organic_disease
    )
    
    if rome_criteria_met:
        diagnosis = "CRITERI ROME IV SODDISFATTI"
        recommendation = "Diagnosi di sindrome di ruminazione secondo Rome IV"
    else:
        diagnosis = "CRITERI ROME IV NON SODDISFATTI"
        if repeated_regurgitation and not organic_disease and symptoms_duration_months >= 1:
            recommendation = "Possibile sindrome di ruminazione in evoluzione, rivalutare"
        else:
            recommendation = "Considerare diagnosi alternative"
    
    result = f"""Criteri Rome IV per Sindrome di Ruminazione Pediatrica
===================================================
Diagnosi: {diagnosis}
Raccomandazione: {recommendation}

Criteri soddisfatti:
{chr(10).join(criteria_met) if criteria_met else '• Nessun criterio soddisfatto'}

Criteri non soddisfatti:
{chr(10).join(criteria_not_met) if criteria_not_met else '• Tutti i criteri soddisfatti'}

Criteri Rome IV completi per la sindrome di ruminazione:
1. Rigurgito ripetuto e senza sforzo di cibo parzialmente digerito
2. Rigurgito non preceduto da nausea o conati
3. Inizio entro 30 minuti dal pasto
4. Non migliora con terapie standard per reflusso
5. Sintomi presenti almeno 2 giorni a settimana
6. Sintomi presenti per almeno 2 mesi
7. Assenza di malattie organiche che spiegano i sintomi

Diagnosi differenziali da considerare:
- Malattia da reflusso gastroesofageo
- Disturbi della motilità esofagea
- Acalasia
- Ernia iatale
- Stenosi pilorica
- Gastroparesi
- Disturbi del comportamento alimentare
- Sindrome di Sandifer

Note cliniche:
- Osservazione diretta spesso necessaria per la diagnosi
- Caratteristica contrazione dei muscoli addominali
- Può verificarsi con o senza consapevolezza
- Più comune in lattanti e bambini con ritardo dello sviluppo
- Approccio terapeutico:
  * Riabilitazione diaframmatica
  * Tecniche di distrazione durante/dopo i pasti
  * Terapia comportamentale
  * Biofeedback
- Prognosi migliore con intervento multidisciplinare
"""
    return [types.TextContent(type="text", text=result)]

def _assess_brue_criteria(args):
    """Valuta criteri per Brief Resolved Unexplained Events (BRUE)"""
    age_less_than_1_year = args.get('age_less_than_1_year', False)
    event_brief = args.get('event_brief', False)
    no_explanation = args.get('no_explanation', False)
    event_features = args.get('event_features', [])
    
    # Criteri per rischio elevato
    age_less_than_2_months = args.get('age_less_than_2_months', False)
    prematurity = args.get('prematurity', False)
    event_duration_gt_1_min = args.get('event_duration_gt_1_min', False)
    multiple_events = args.get('multiple_events', False)
    cpr_required = args.get('cpr_required', False)
    
    # Verifica criteri BRUE
    is_brue = (
        age_less_than_1_year and 
        event_brief and 
        no_explanation and 
        len(event_features) > 0
    )
    
    # Criteri presenti
    criteria_present = []
    if age_less_than_1_year:
        criteria_present.append("• Età <1 anno")
    if event_brief:
        criteria_present.append("• Evento breve (<1 minuto) e risolto completamente")
    if no_explanation:
        criteria_present.append("• Nessuna spiegazione identificabile dopo valutazione")
    if event_features:
        features_text = ", ".join([f.replace("_", " ") for f in event_features])
        criteria_present.append(f"• Caratteristiche dell'evento: {features_text}")
    
    # Criteri rischio elevato
    high_risk_factors = []
    if age_less_than_2_months:
        high_risk_factors.append("• Età <2 mesi")
    if prematurity:
        high_risk_factors.append("• Prematurità <32 settimane o età <45 settimane post-concezionali")
    if event_duration_gt_1_min:
        high_risk_factors.append("• Durata evento >1 minuto")
    if multiple_events:
        high_risk_factors.append("• Eventi multipli")
    if cpr_required:
        high_risk_factors.append("• RCP richiesta da personale sanitario")
    
    # Determinazione rischio
    if not is_brue:
        diagnosis = "NON SODDISFA CRITERI BRUE"
        recommendation = "Non classificabile come BRUE. Valutare diagnosi alternative."
        risk = "N/A"
    elif len(high_risk_factors) > 0:
        diagnosis = "BRUE AD ALTO RISCHIO"
        recommendation = "Ricovero per monitoraggio e valutazione approfondita."
        risk = "ALTO"
    else:
        diagnosis = "BRUE A BASSO RISCHIO"
        recommendation = "Considerare dimissione dopo esame obiettivo normale ed educazione ai genitori."
        risk = "BASSO"
    
    result = f"""Valutazione Brief Resolved Unexplained Event (BRUE)
==================================================
Diagnosi: {diagnosis}
Rischio: {risk}
Raccomandazione: {recommendation}

Criteri BRUE:
{chr(10).join(criteria_present) if criteria_present else "• Nessun criterio presente"}

{'Fattori di rischio elevato:' if high_risk_factors else ''}
{chr(10).join(high_risk_factors) if high_risk_factors else ''}

Interpretazione:
- BRUE richiede tutti i seguenti criteri:
  - Età <1 anno
  - Evento breve (<1 minuto) e risolto completamente
  - Nessuna spiegazione dopo valutazione appropriata
  - ≥1 tra: cianosi/pallore, respiro assente/irregolare, alterato tono muscolare, alterata responsività

- Fattori di alto rischio:
  - Età <2 mesi
  - Prematurità
  - Durata evento >1 minuto
  - Eventi multipli
  - RCP richiesta da sanitari

Note cliniche:
- BRUE sostituisce il vecchio termine ALTE (Apparent Life-Threatening Event)
- BRUE a basso rischio: considerare dimissione senza indagini estese
- BRUE ad alto rischio: considerare ricovero, monitoraggio e indagini più approfondite
- Indagini da considerare in BRUE ad alto rischio: ECG, poligrafia, EEG, valutazione reflusso GE
- Educare sempre i genitori sulla gestione e monitoraggio del bambino

Fonte: Linee guida American Academy of Pediatrics 2016
"""
    return [types.TextContent(type="text", text=result)]