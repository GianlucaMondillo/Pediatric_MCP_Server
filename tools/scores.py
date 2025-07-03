"""
Score medici per la pediatria
PEWS - Pediatric Early Warning Score
PAS - Pediatric Appendicitis Score  
APGAR - Score neonatale
"""
import mcp.types as types
from utils.medical_formulas import (
    calculate_pews_interpretation,
    calculate_pas_interpretation, 
    calculate_apgar_interpretation,
    calculate_gcs_pediatric_interpretation,
    calculate_pediatric_trauma_score,
    calculate_catch_score,
    calculate_westley_croup_score,
    calculate_centor_score_pediatric,
    calculate_wells_score_pediatric,
    # Nuove funzioni importate
    calculate_pas_asthma_interpretation,
    calculate_pass_asthma_interpretation,
    calculate_bacterial_meningitis_score_interpretation,
    calculate_kocher_criteria_interpretation,
    calculate_kawasaki_criteria_interpretation,
    calculate_bops_interpretation
)

def get_score_tools():
    """Restituisce tutti i tool per i score medici"""
    return [
        types.Tool(
            name="calculate_pews",
            description="Calcola il PEWS (Pediatric Early Warning Score) versione italiana validata per identificare bambini a rischio di deterioramento clinico",
            inputSchema={
                "type": "object",
                "properties": {
                    "behavior": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 3,
                        "description": "Comportamento: 0=Gioca/appropriato, 1=Dorme, 2=Irritabile/Preoccupazione genitori, 3=Letargico/confuso/Ridotta risposta al dolore"
                    },
                    "cardiovascular": {
                        "type": "integer", 
                        "minimum": 0,
                        "maximum": 3,
                        "description": "Apparato cardiovascolare: 0=Roseo/refill 1-2sec, 1=Pallido/refill 3sec, 2=Grigio/refill 4sec/tachicardia +20bpm, 3=Grigio marezzato/refill ≥5sec/tachicardia +30bpm/BRADICARDIA"
                    },
                    "respiratory": {
                        "type": "integer",
                        "minimum": 0, 
                        "maximum": 3,
                        "description": "Apparato respiratorio: 0=Parametri normali/no rientramenti, 1=Lievi alterazioni/rientramenti intercostali, 2=Moderate alterazioni/rientramenti sottosternali, 3=Gravi alterazioni/rientramenti globali"
                    },
                    "age_months": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 216,
                        "description": "Età in mesi per interpretazione parametri vitali"
                    }
                },
                "required": ["behavior", "cardiovascular", "respiratory", "age_months"]
            }
        ),
        
        types.Tool(
            name="calculate_pas",
            description="Calcola il PAS (Pediatric Appendicitis Score) per valutare la probabilità di appendicite acuta",
            inputSchema={
                "type": "object",
                "properties": {
                    "fever": {
                        "type": "boolean",
                        "description": "Febbre ≥38°C (1 punto se presente)"
                    },
                    "anorexia": {
                        "type": "boolean", 
                        "description": "Anoressia (1 punto se presente)"
                    },
                    "nausea_vomiting": {
                        "type": "boolean",
                        "description": "Nausea o vomito (1 punto se presente)" 
                    },
                    "cough_percussion_hopping": {
                        "type": "boolean",
                        "description": "Dolore con colpo di tosse, percussione o saltellamento (2 punti se presente)"
                    },
                    "rlq_tenderness": {
                        "type": "boolean",
                        "description": "Dolorabilità in fossa iliaca destra (2 punti se presente)"
                    },
                    "pain_migration": {
                        "type": "boolean", 
                        "description": "Migrazione del dolore da regione periombelicale a fossa iliaca destra (1 punto se presente)"
                    },
                    "leukocytosis": {
                        "type": "boolean",
                        "description": "Leucocitosi >10.000/μL (1 punto se presente)"
                    },
                    "neutrophilia": {
                        "type": "boolean",
                        "description": "Neutrofilia >7.500/μL (1 punto se presente)"
                    }
                },
                "required": ["fever", "anorexia", "nausea_vomiting", "cough_percussion_hopping", "rlq_tenderness", "pain_migration", "leukocytosis", "neutrophilia"]
            }
        ),
        
        types.Tool(
            name="calculate_apgar",
            description="Calcola il punteggio APGAR per valutare le condizioni del neonato",
            inputSchema={
                "type": "object",
                "properties": {
                    "heart_rate": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 2,
                        "description": "Frequenza cardiaca: 0=Assente, 1=<100 bpm, 2=≥100 bpm"
                    },
                    "respiratory_effort": {
                        "type": "integer",
                        "minimum": 0, 
                        "maximum": 2,
                        "description": "Sforzo respiratorio: 0=Assente, 1=Debole/irregolare, 2=Buono/pianto vigoroso"
                    },
                    "muscle_tone": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 2, 
                        "description": "Tono muscolare: 0=Flaccido, 1=Flessione degli arti, 2=Movimento attivo"
                    },
                    "reflex_irritability": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 2,
                        "description": "Riflessi/irritabilità: 0=Nessuna risposta, 1=Smorfie, 2=Pianto vigoroso"
                    },
                    "color": {
                        "type": "integer", 
                        "minimum": 0,
                        "maximum": 2,
                        "description": "Colorito: 0=Blu/pallido, 1=Rosa con estremità blu, 2=Completamente rosa"
                    }
                },
                "required": ["heart_rate", "respiratory_effort", "muscle_tone", "reflex_irritability", "color"]
            }
        ),
        
        types.Tool(
            name="calculate_gcs_pediatric",
            description="Calcola Glasgow Coma Scale pediatrica per valutazione neurologica",
            inputSchema={
                "type": "object",
                "properties": {
                    "eye_opening": {
                        "type": "integer",
                        "minimum": 1,
                        "maximum": 4,
                        "description": "Apertura occhi: 1=Nessuna, 2=Al dolore, 3=Al richiamo, 4=Spontanea"
                    },
                    "verbal_response": {
                        "type": "integer",
                        "minimum": 1,
                        "maximum": 5,
                        "description": "Risposta verbale: 1=Nessuna, 2=Suoni incomprensibili, 3=Parole inappropriate, 4=Confuso, 5=Orientato"
                    },
                    "motor_response": {
                        "type": "integer",
                        "minimum": 1, 
                        "maximum": 6,
                        "description": "Risposta motoria: 1=Nessuna, 2=Estensione, 3=Flessione abnorme, 4=Retrazione, 5=Localizza, 6=Obbedisce"
                    },
                    "age_months": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 216,
                        "description": "Età in mesi per adattamento scala"
                    }
                },
                "required": ["eye_opening", "verbal_response", "motor_response", "age_months"]
            }
        ),
        
        types.Tool(
            name="calculate_mchat",
            description="Valuta M-CHAT (Modified Checklist for Autism in Toddlers) per screening autismo",
            inputSchema={
                "type": "object",
                "properties": {
                    "enjoys_swinging": {"type": "boolean", "description": "Il bambino ama dondolarsi/essere fatto saltare sulle ginocchia?"},
                    "interest_other_children": {"type": "boolean", "description": "Il bambino mostra interesse per altri bambini?"},
                    "enjoys_climbing": {"type": "boolean", "description": "Il bambino ama arrampicarsi?"},
                    "enjoys_peekaboo": {"type": "boolean", "description": "Il bambino ama giocare a cu-cu/nascondino?"},
                    "pretend_play": {"type": "boolean", "description": "Il bambino fa giochi di finzione (es. bere da tazza vuota)?"},
                    "points_to_request": {"type": "boolean", "description": "Il bambino usa l'indice per chiedere qualcosa?"},
                    "points_to_show_interest": {"type": "boolean", "description": "Il bambino punta per mostrare interesse?"},
                    "plays_appropriately_toys": {"type": "boolean", "description": "Il bambino gioca appropriatamente con giocattoli piccoli?"},
                    "brings_objects_to_show": {"type": "boolean", "description": "Il bambino porta oggetti per mostrarli?"},
                    "looks_in_eyes": {"type": "boolean", "description": "Il bambino guarda negli occhi per più di 1-2 secondi?"},
                    "oversensitive_noise": {"type": "boolean", "description": "Il bambino sembra ipersensibile ai rumori?"},
                    "smiles_in_response": {"type": "boolean", "description": "Il bambino sorride in risposta al vostro viso/sorriso?"},
                    "imitates_actions": {"type": "boolean", "description": "Il bambino imita le vostre azioni?"},
                    "responds_to_name": {"type": "boolean", "description": "Il bambino risponde quando chiamato per nome?"},
                    "points_at_airplane": {"type": "boolean", "description": "Se puntate un aeroplano nel cielo, il bambino lo guarda?"},
                    "walks_independently": {"type": "boolean", "description": "Il bambino cammina da solo?"},
                    "looks_at_pointed_objects": {"type": "boolean", "description": "Il bambino guarda cose che voi puntate?"},
                    "unusual_finger_movements": {"type": "boolean", "description": "Il bambino fa movimenti strani con le dita vicino agli occhi?"},
                    "tries_to_attract_attention": {"type": "boolean", "description": "Il bambino cerca di attirare la vostra attenzione sulla sua attività?"},
                    "suspected_hearing_problem": {"type": "boolean", "description": "Vi siete mai chiesti se il bambino ha problemi di udito?"}
                },
                "required": ["enjoys_swinging", "interest_other_children", "enjoys_climbing", "enjoys_peekaboo", "pretend_play", "points_to_request", "points_to_show_interest", "plays_appropriately_toys", "brings_objects_to_show", "looks_in_eyes", "oversensitive_noise", "smiles_in_response", "imitates_actions", "responds_to_name", "points_at_airplane", "walks_independently", "looks_at_pointed_objects", "unusual_finger_movements", "tries_to_attract_attention", "suspected_hearing_problem"]
            }
        ),
        
        # NUOVI STRUMENTI AGGIUNTI
        
        types.Tool(
            name="calculate_pediatric_trauma_score",
            description="Calcola Pediatric Trauma Score (PTS) per valutare la gravità dei traumi pediatrici",
            inputSchema={
                "type": "object",
                "properties": {
                    "weight_kg": {
                        "type": "number",
                        "minimum": 0,
                        "maximum": 100,
                        "description": "Peso in kg"
                    },
                    "systolic_bp": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 200,
                        "description": "Pressione arteriosa sistolica in mmHg"
                    },
                    "conscious": {
                        "type": "boolean",
                        "description": "Stato di coscienza: True=sveglio, False=obnubilato/coma"
                    },
                    "open_wound": {
                        "type": "boolean",
                        "description": "Ferita aperta/penetrante: True=presente, False=assente"
                    },
                    "fracture": {
                        "type": "boolean",
                        "description": "Frattura aperta/multipla: True=presente, False=assente"
                    },
                    "cutaneous": {
                        "type": "boolean",
                        "description": "Cute intatta: True=intatta, False=compromessa"
                    }
                },
                "required": ["weight_kg", "systolic_bp", "conscious", "open_wound", "fracture", "cutaneous"]
            }
        ),
        
        types.Tool(
            name="calculate_catch_score",
            description="Calcola CATCH (Canadian Assessment of Tomography for Childhood Head injury) per valutare necessità di TC in trauma cranico pediatrico",
            inputSchema={
                "type": "object",
                "properties": {
                    "vomiting": {
                        "type": "boolean",
                        "description": "Vomito ≥3 episodi dopo il trauma"
                    },
                    "headache": {
                        "type": "boolean",
                        "description": "Cefalea severa persistente"
                    },
                    "gcsscore": {
                        "type": "integer",
                        "minimum": 13,
                        "maximum": 15,
                        "description": "GCS a 2 ore dal trauma (13-15)"
                    },
                    "suspected_skull_fracture": {
                        "type": "boolean",
                        "description": "Segni clinici di frattura cranica"
                    },
                    "dangerous_mechanism": {
                        "type": "boolean",
                        "description": "Meccanismo traumatico pericoloso (caduta >1m, incidente auto)"
                    }
                },
                "required": ["vomiting", "headache", "gcsscore", "suspected_skull_fracture", "dangerous_mechanism"]
            }
        ),
        
        types.Tool(
            name="calculate_westley_croup_score",
            description="Calcola Westley Croup Score per valutare la gravità del croup pediatrico",
            inputSchema={
                "type": "object",
                "properties": {
                    "stridor": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 2,
                        "description": "Stridore inspiratorio: 0=Nessuno, 1=Con agitazione, 2=A riposo"
                    },
                    "retraction": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 3,
                        "description": "Retrazioni: 0=Nessuna, 1=Lievi, 2=Moderate, 3=Severe"
                    },
                    "air_entry": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 2,
                        "description": "Ingresso d'aria: 0=Normale, 1=Diminuito, 2=Marcatamente diminuito"
                    },
                    "cyanosis": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 5,
                        "description": "Cianosi: 0=Nessuna, 4=Con agitazione, 5=A riposo"
                    },
                    "consciousness": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 5,
                        "description": "Livello di coscienza: 0=Normale, 5=Alterato"
                    }
                },
                "required": ["stridor", "retraction", "air_entry", "cyanosis", "consciousness"]
            }
        ),
        
        types.Tool(
            name="calculate_centor_score_pediatric",
            description="Calcola Centor Score modificato per faringite streptococcica in età pediatrica",
            inputSchema={
                "type": "object",
                "properties": {
                    "age_years": {
                        "type": "number",
                        "minimum": 0,
                        "maximum": 18,
                        "description": "Età in anni"
                    },
                    "exudate": {
                        "type": "boolean",
                        "description": "Essudato tonsillare presente"
                    },
                    "tender_nodes": {
                        "type": "boolean",
                        "description": "Linfoadenopatia cervicale anteriore dolente"
                    },
                    "fever": {
                        "type": "boolean",
                        "description": "Febbre >38°C"
                    },
                    "cough": {
                        "type": "boolean",
                        "description": "Presenza di tosse"
                    }
                },
                "required": ["age_years", "exudate", "tender_nodes", "fever", "cough"]
            }
        ),
        
        types.Tool(
            name="calculate_wells_score_pediatric",
            description="Calcola Wells Score pediatrico per valutare probabilità di trombosi venosa profonda",
            inputSchema={
                "type": "object",
                "properties": {
                    "provoked_dvt": {
                        "type": "boolean",
                        "description": "TVP provocata da traumi, chirurgia recente, immobilizzazione"
                    },
                    "alternative_diagnosis": {
                        "type": "boolean",
                        "description": "Diagnosi alternativa possibile"
                    },
                    "swelling": {
                        "type": "boolean",
                        "description": "Gonfiore dell'intero arto"
                    },
                    "unilateral_tenderness": {
                        "type": "boolean",
                        "description": "Dolorabilità unilaterale lungo sistema venoso profondo"
                    },
                    "swelling_thigh_calf": {
                        "type": "boolean",
                        "description": "Gonfiore polpaccio >3cm rispetto controlaterale"
                    },
                    "unilateral_pitting": {
                        "type": "boolean",
                        "description": "Edema improntabile monolaterale"
                    },
                    "bedridden": {
                        "type": "boolean",
                        "description": "Allettamento recente >3 giorni"
                    },
                    "active_cancer": {
                        "type": "boolean",
                        "description": "Cancro attivo"
                    },
                    "previous_dvt": {
                        "type": "boolean",
                        "description": "Precedente TVP"
                    }
                },
                "required": ["provoked_dvt", "alternative_diagnosis", "swelling", "unilateral_tenderness", "swelling_thigh_calf", "unilateral_pitting", "bedridden", "active_cancer", "previous_dvt"]
            }
        ),
        types.Tool(
            name="calculate_pas_asthma",
            description="Calcola il Pediatric Asthma Score (PAS) per valutare la gravità di un'esacerbazione asmatica",
            inputSchema={
                "type": "object",
                "properties": {
                    "respiratory_rate": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 3,
                        "description": "Frequenza respiratoria: 0=normale, 1=aumentata, 2=molto aumentata, 3=grave tachipnea"
                    },
                    "oxygen_requirement": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 3,
                        "description": "Richiesta di ossigeno: 0=nessuna (SatO2≥96%), 1=bassa (SatO2 94-95%), 2=moderata (SatO2 90-93%), 3=alta (SatO2<90%)"
                    },
                    "auscultation": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 3,
                        "description": "Auscultazione: 0=normale, 1=wheezing fine/localizzato, 2=wheezing durante tutta l'espirazione, 3=wheezing in ins/esp o silenzio"
                    },
                    "retractions": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 3,
                        "description": "Retrazioni: 0=nessuna, 1=lievi intercostali, 2=moderate intercostali/sottosternali, 3=gravi con uso muscoli accessori"
                    },
                    "dyspnea": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 3,
                        "description": "Dispnea: 0=nessuna, 1=lieve, 2=moderata, 3=grave con difficoltà a parlare/alimentarsi"
                    }
                },
                "required": ["respiratory_rate", "oxygen_requirement", "auscultation", "retractions", "dyspnea"]
            }
        ),

        types.Tool(
            name="calculate_pass_asthma",
            description="Calcola il Pediatric Asthma Severity Score (PASS) per valutare la gravità di un'esacerbazione asmatica",
            inputSchema={
                "type": "object",
                "properties": {
                    "wheezing": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 2,
                        "description": "Wheezing: 0=assente, 1=fine/localizzato, 2=diffuso"
                    },
                    "work_of_breathing": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 2,
                        "description": "Lavoro respiratorio: 0=normale, 1=aumentato, 2=massimale"
                    },
                    "prolonged_expiration": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 2,
                        "description": "Espirazione prolungata: 0=assente, 1=moderata, 2=marcata"
                    }
                },
                "required": ["wheezing", "work_of_breathing", "prolonged_expiration"]
            }
        ),
        types.Tool(
            name="calculate_pas_asthma",
            description="Calcola il Pediatric Asthma Score (PAS) per valutare la gravità di un'esacerbazione asmatica",
            inputSchema={
                "type": "object",
                "properties": {
                    "respiratory_rate": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 3,
                        "description": "Frequenza respiratoria: 0=normale, 1=aumentata, 2=molto aumentata, 3=grave tachipnea"
                    },
                    "oxygen_requirement": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 3,
                        "description": "Richiesta di ossigeno: 0=nessuna (SatO2≥96%), 1=bassa (SatO2 94-95%), 2=moderata (SatO2 90-93%), 3=alta (SatO2<90%)"
                    },
                    "auscultation": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 3,
                        "description": "Auscultazione: 0=normale, 1=wheezing fine/localizzato, 2=wheezing durante tutta l'espirazione, 3=wheezing in ins/esp o silenzio"
                    },
                    "retractions": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 3,
                        "description": "Retrazioni: 0=nessuna, 1=lievi intercostali, 2=moderate intercostali/sottosternali, 3=gravi con uso muscoli accessori"
                    },
                    "dyspnea": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 3,
                        "description": "Dispnea: 0=nessuna, 1=lieve, 2=moderata, 3=grave con difficoltà a parlare/alimentarsi"
                    }
                },
                "required": ["respiratory_rate", "oxygen_requirement", "auscultation", "retractions", "dyspnea"]
            }
        ),

        types.Tool(
            name="calculate_pass_asthma",
            description="Calcola il Pediatric Asthma Severity Score (PASS) per valutare la gravità di un'esacerbazione asmatica",
            inputSchema={
                "type": "object",
                "properties": {
                    "wheezing": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 2,
                        "description": "Wheezing: 0=assente, 1=fine/localizzato, 2=diffuso"
                    },
                    "work_of_breathing": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 2,
                        "description": "Lavoro respiratorio: 0=normale, 1=aumentato, 2=massimale"
                    },
                    "prolonged_expiration": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 2,
                        "description": "Espirazione prolungata: 0=assente, 1=moderata, 2=marcata"
                    }
                },
                "required": ["wheezing", "work_of_breathing", "prolonged_expiration"]
            }
        ),
        types.Tool(
            name="calculate_bacterial_meningitis_score",
            description="Calcola il Bacterial Meningitis Score for Children per predire il rischio di meningite batterica",
            inputSchema={
                "type": "object",
                "properties": {
                    "csf_gram_stain_positive": {
                        "type": "boolean",
                        "description": "Colorazione di Gram positiva nel liquor"
                    },
                    "csf_anc_geq_1000": {
                        "type": "boolean",
                        "description": "Conta neutrofili nel liquor ≥1000 cell/μL"
                    },
                    "csf_protein_geq_80": {
                        "type": "boolean",
                        "description": "Proteine liquorali ≥80 mg/dL"
                    },
                    "peripheral_anc_geq_10000": {
                        "type": "boolean",
                        "description": "Conta neutrofili periferici ≥10000 cell/μL"
                    },
                    "seizure_at_onset": {
                        "type": "boolean",
                        "description": "Convulsioni all'esordio"
                    }
                },
                "required": ["csf_gram_stain_positive", "csf_anc_geq_1000", "csf_protein_geq_80", "peripheral_anc_geq_10000", "seizure_at_onset"]
            }
        ),
        types.Tool(
            name="calculate_kocher_criteria",
            description="Calcola i Kocher Criteria per la diagnosi di artrite settica dell'anca in età pediatrica",
            inputSchema={
                "type": "object",
                "properties": {
                    "fever": {
                        "type": "boolean",
                        "description": "Febbre >38.5°C"
                    },
                    "weight_bearing": {
                        "type": "boolean",
                        "description": "Incapacità/rifiuto di carico sull'arto interessato"
                    },
                    "esr_elevated": {
                        "type": "boolean",
                        "description": "VES >40 mm/h"
                    },
                    "wbc_elevated": {
                        "type": "boolean",
                        "description": "Leucociti >12,000/μL"
                    }
                },
                "required": ["fever", "weight_bearing", "esr_elevated", "wbc_elevated"]
            }
        ),
        types.Tool(
            name="calculate_kawasaki_criteria",
            description="Valuta i criteri diagnostici per la malattia di Kawasaki in età pediatrica",
            inputSchema={
                "type": "object",
                "properties": {
                    "fever_5_days": {
                        "type": "boolean",
                        "description": "Febbre persistente per ≥5 giorni"
                    },
                    "conjunctival_injection": {
                        "type": "boolean",
                        "description": "Iniezione congiuntivale bilaterale non essudativa"
                    },
                    "oral_changes": {
                        "type": "boolean",
                        "description": "Alterazioni del cavo orale (labbra screpolate, eritema orofaringeo, lingua a fragola)"
                    },
                    "extremity_changes": {
                        "type": "boolean",
                        "description": "Alterazioni delle estremità (eritema palmo-plantare, edema, desquamazione)"
                    },
                    "polymorphous_rash": {
                        "type": "boolean",
                        "description": "Esantema polimorfo"
                    },
                    "cervical_lymphadenopathy": {
                        "type": "boolean",
                        "description": "Linfoadenopatia cervicale (>1.5 cm di diametro)"
                    },
                    "laboratory_findings": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": ["elevated_crp", "elevated_esr", "anemia", "hypoalbuminemia", "elevated_alt", "leukocytosis", "thrombocytosis", "pyuria"]
                        },
                        "description": "Esami di laboratorio anormali"
                    },
                    "echocardiogram_findings": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": ["coronary_artery_abnormality", "mitral_regurgitation", "pericardial_effusion", "decreased_lv_function", "z_score_gt_2"]
                        },
                        "description": "Reperti ecocardiografici"
                    }
                },
                "required": ["fever_5_days", "conjunctival_injection", "oral_changes", "extremity_changes", "polymorphous_rash", "cervical_lymphadenopathy"]
            }
        ),
        types.Tool(
            name="calculate_hsp_criteria",
            description="Valuta i criteri EULAR/PRINTO/PRES per la diagnosi di Porpora di Henoch-Schönlein (HSP)",
            inputSchema={
                "type": "object",
                "properties": {
                    "palpable_purpura": {
                        "type": "boolean",
                        "description": "Porpora palpabile (criterio obbligatorio)"
                    },
                    "abdominal_pain": {
                        "type": "boolean",
                        "description": "Dolore addominale"
                    },
                    "histopathology": {
                        "type": "boolean",
                        "description": "Depositi di IgA alla biopsia"
                    },
                    "arthritis_arthralgia": {
                        "type": "boolean",
                        "description": "Artrite o artralgia"
                    },
                    "renal_involvement": {
                        "type": "boolean",
                        "description": "Coinvolgimento renale (ematuria e/o proteinuria)"
                    }
                },
                "required": ["palpable_purpura", "abdominal_pain", "histopathology", "arthritis_arthralgia", "renal_involvement"]
            }
        ),
        types.Tool(
            name="calculate_jones_criteria",
            description="Valuta i criteri di Jones aggiornati (2015) per la diagnosi di febbre reumatica acuta",
            inputSchema={
                "type": "object",
                "properties": {
                    "prior_rheumatic_heart_disease": {
                        "type": "boolean",
                        "description": "Precedente cardiopatia reumatica"
                    },
                    "high_risk_population": {
                        "type": "boolean",
                        "description": "Popolazione ad alto rischio (endemicità elevata)"
                    },
                    "confirmed_strep_infection": {
                        "type": "boolean",
                        "description": "Infezione streptococcica recente confermata"
                    },
                    "major_criteria": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": [
                                "carditis", "arthritis", "chorea", "erythema_marginatum", "subcutaneous_nodules",
                                "subclinical_carditis", "polyarthralgia"
                            ]
                        },
                        "description": "Criteri maggiori (cardite, artrite, corea, eritema marginato, noduli sottocutanei, cardite subclinica, poliartralgia)"
                    },
                    "minor_criteria": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": [
                                "fever", "elevated_esr_crp", "prolonged_pr_interval", "polyarthralgia", "monoarthralgia"
                            ]
                        },
                        "description": "Criteri minori (febbre, VES/PCR elevata, PR prolungato, poliartralgia, monoartralgia)"
                    }
                },
                "required": ["prior_rheumatic_heart_disease", "high_risk_population", "confirmed_strep_infection", "major_criteria", "minor_criteria"]
            }
        ),

        types.Tool(
            name="calculate_bops",
            description="Calcola il Behavioral Observational Pain Scale (BOPS) per dolore post-operatorio pediatrico (1-7 anni)",
            inputSchema={
                "type": "object",
                "properties": {
                    "facial_expression": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 2,
                        "description": "Espressione facciale: 0=Neutra/sorridente/calma, 1=Occasionale fronte corrugata/labbra serrate, 2=Frequenti/costanti espressioni dolore"
                    },
                    "verbalization": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 2,
                        "description": "Verbalizzazione: 0=Normale/dorme silenziosamente, 1=Occasionali lamenti/piagnucola, 2=Pianto intenso/grida/singhiozzi"
                    },
                    "body_position": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 2,
                        "description": "Posizione corporea: 0=Inattiva/rilassata/movimento normale, 1=Tesa/irrequieta/si contorce, 2=Rigida/flessa/calci/tocca la ferita"
                    },
                    "age_months": {
                        "type": "integer",
                        "minimum": 12,
                        "maximum": 84,
                        "description": "Età in mesi (12-84 mesi = 1-7 anni)"
                    }
                },
                "required": ["facial_expression", "verbalization", "body_position", "age_months"]
            }
        ),
        types.Tool(
            name="calculate_lansky_score",
            description="Calcola il Lansky Play-Performance Scale per la valutazione funzionale pediatrica (0-16 anni)",
            inputSchema={
                "type": "object",
                "properties": {
                    "performance_level": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 100,
                        "multipleOf": 10,
                        "description": "Livello funzionale: 100=attività normale, 0=non responsivo (a intervalli di 10)"
                    },
                    "age_months": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 192,
                        "description": "Età in mesi (0-192 mesi = 0-16 anni)"
                    }
                },
                "required": ["performance_level", "age_months"]
            }
        ),
        types.Tool(
            name="calculate_sickle_cell_complication_risk",
            description="Calcola il rischio di complicanze severe in bambini con anemia falciforme (Miller et al.)",
            inputSchema={
                "type": "object",
                "properties": {
                    "hemoglobin_level": {
                        "type": "number",
                        "minimum": 3,
                        "maximum": 15,
                        "description": "Livello di emoglobina basale in g/dL"
                    },
                    "wbc_count": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 50,
                        "description": "Conta leucocitaria basale in x10^3/μL"
                    },
                    "history_of_acs": {
                        "type": "boolean",
                        "description": "Storia di sindrome toracica acuta"
                    },
                    "pain_events_per_year": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 20,
                        "description": "Numero di eventi dolorosi che richiedono assistenza medica all'anno"
                    },
                    "dactylitis_under_1_year": {
                        "type": "boolean",
                        "description": "Storia di dattilite prima dell'anno di età"
                    },
                    "hemoglobin_f_level": {
                        "type": "number",
                        "minimum": 0,
                        "maximum": 100,
                        "description": "Livello di emoglobina fetale (%)"
                    },
                    "genotype": {
                        "type": "string",
                        "enum": ["ss", "sbeta0", "sc", "sbeta+"],
                        "description": "Genotipo: SS, Sβ0, SC o Sβ+"
                    }
                },
                "required": ["hemoglobin_level", "wbc_count", "history_of_acs", "pain_events_per_year", "genotype"]
            }
        ),
        types.Tool(
            name="calculate_pnhs",
            description="Calcola il Pediatric NAFLD Histological Score (PNHS) per distinguere NASH (steatoepatite) da semplice steatosi",
            inputSchema={
                "type": "object",
                "properties": {
                    "bmi_zscore": {
                        "type": "number",
                        "minimum": -3,
                        "maximum": 5,
                        "description": "BMI z-score"
                    },
                    "ast_iu_l": {
                        "type": "number",
                        "minimum": 5,
                        "maximum": 1000,
                        "description": "AST in IU/L"
                    },
                    "alt_iu_l": {
                        "type": "number",
                        "minimum": 5,
                        "maximum": 1000,
                        "description": "ALT in IU/L"
                    },
                    "insulin_resistance": {
                        "type": "boolean",
                        "description": "Presenza di resistenza insulinica (HOMA-IR >2.5 o diagnosi clinica)"
                    },
                    "apnea_obstructive_sleep": {
                        "type": "boolean",
                        "description": "Diagnosi di apnea ostruttiva del sonno"
                    }
                },
                "required": ["bmi_zscore", "ast_iu_l", "alt_iu_l", "insulin_resistance"]
            }
        )
    ]

def handle_score_tools(name: str, arguments: dict):
    """Gestisce i calcoli dei score"""
    try:
        if name == "calculate_pews":
            return _calculate_pews(arguments)
        elif name == "calculate_pas":
            return _calculate_pas(arguments)
        elif name == "calculate_apgar":
            return _calculate_apgar(arguments)
        elif name == "calculate_gcs_pediatric":
            return _calculate_gcs_pediatric(arguments)
        elif name == "calculate_mchat":
            return _calculate_mchat(arguments)
        elif name == "calculate_pediatric_trauma_score":
            return _calculate_pediatric_trauma_score(arguments)
        elif name == "calculate_catch_score":
            return _calculate_catch_score(arguments)
        elif name == "calculate_westley_croup_score":
            return _calculate_westley_croup_score(arguments)
        elif name == "calculate_centor_score_pediatric":
            return _calculate_centor_score_pediatric(arguments)
        elif name == "calculate_wells_score_pediatric":
            return _calculate_wells_score_pediatric(arguments)
        # Nuovi strumenti aggiunti
        elif name == "calculate_pas_asthma":
            return _calculate_pas_asthma(arguments)
        elif name == "calculate_pass_asthma":
            return _calculate_pass_asthma(arguments)
        elif name == "calculate_bacterial_meningitis_score":
            return _calculate_bacterial_meningitis_score(arguments)
        elif name == "calculate_kocher_criteria":
            return _calculate_kocher_criteria(arguments)
        elif name == "calculate_kawasaki_criteria":
            return _calculate_kawasaki_criteria(arguments)
        elif name == "calculate_jones_criteria":
            return _calculate_jones_criteria(arguments)
        elif name == "calculate_bops":
            return _calculate_bops(arguments)
        elif name == "calculate_lansky_score":
            return _calculate_lansky_score(arguments)
        elif name == "calculate_sickle_cell_complication_risk":
            return _calculate_sickle_cell_complication_risk(arguments)
        elif name == "calculate_pnhs":
            return _calculate_pnhs(arguments)
        else:
            raise ValueError(f"Score non implementato: {name}")
    except Exception as e:
        return [types.TextContent(type="text", text=f"Errore nel calcolo: {str(e)}")]
def _calculate_pews(args):
    """Calcola PEWS Score"""
    behavior = args.get('behavior', 0)
    cardiovascular = args.get('cardiovascular', 0)
    respiratory = args.get('respiratory', 0) 
    nebulizer_use = args.get('nebulizer_use', 0)
    persistent_vomiting = args.get('persistent_vomiting', 0)
    
    total = behavior + cardiovascular + respiratory + nebulizer_use + persistent_vomiting
    interpretation = calculate_pews_interpretation(total)
    
    result = f"""PEWS (Pediatric Early Warning Score)
=====================================
Punteggio totale: {total}/13
Livello di rischio: {interpretation['risk_level']}
Azione raccomandata: {interpretation['action']}

Dettaglio punteggi:
- Comportamento: {behavior}/3
- Cardiovascolare: {cardiovascular}/3  
- Respiratorio: {respiratory}/3
- Uso nebulizzatore: {nebulizer_use}/2
- Vomito persistente: {persistent_vomiting}/1

Interpretazione clinica:
• Score 0-2: Monitoraggio di routine
• Score 3-4: Aumentare sorveglianza
• Score 5-6: Considerare terapia intensiva
• Score ≥7: Intervento immediato
"""
    return [types.TextContent(type="text", text=result)]

def _calculate_pas(args):
    """Calcola PAS Score"""
    # Calcolo punteggio
    score = 0
    details = []
    
    if args.get('fever', False):
        score += 1
        details.append("• Febbre ≥38°C: +1")
    if args.get('anorexia', False):
        score += 1
        details.append("• Anoressia: +1")
    if args.get('nausea_vomiting', False):
        score += 1
        details.append("• Nausea/vomito: +1")
    if args.get('cough_percussion_hopping', False):
        score += 2
        details.append("• Dolore con tosse/percussione/saltellamento: +2")
    if args.get('rlq_tenderness', False):
        score += 2
        details.append("• Dolorabilità fossa iliaca destra: +2")
    if args.get('pain_migration', False):
        score += 1
        details.append("• Migrazione del dolore: +1")
    if args.get('leukocytosis', False):
        score += 1
        details.append("• Leucocitosi >10.000/μL: +1")
    if args.get('neutrophilia', False):
        score += 1
        details.append("• Neutrofilia >7.500/μL: +1")
    
    interpretation = calculate_pas_interpretation(score)
    
    result = f"""PAS (Pediatric Appendicitis Score)
===================================
Punteggio totale: {score}/10
Probabilità appendicite: {interpretation['probability']}
Raccomandazione: {interpretation['recommendation']}

Elementi presenti:
{chr(10).join(details) if details else "• Nessun elemento presente"}

Interpretazione clinica:
• Score 0-2: Appendicite improbabile (2%)
• Score 3-5: Probabilità intermedia (15-25%) 
• Score 6-7: Alta probabilità (70-80%)
• Score 8-10: Appendicite molto probabile (95%+)
"""
    return [types.TextContent(type="text", text=result)]

def _calculate_apgar(args):
    """Calcola APGAR Score"""
    heart_rate = args.get('heart_rate', 0)
    respiratory_effort = args.get('respiratory_effort', 0)
    muscle_tone = args.get('muscle_tone', 0)
    reflex_irritability = args.get('reflex_irritability', 0)
    color = args.get('color', 0)
    
    total = heart_rate + respiratory_effort + muscle_tone + reflex_irritability + color
    interpretation = calculate_apgar_interpretation(total)
    
    result = f"""APGAR Score
===========
Punteggio totale: {total}/10
Condizione: {interpretation['condition']}
Azione: {interpretation['action']}

Dettaglio punteggi:
- Frequenza cardiaca: {heart_rate}/2
- Sforzo respiratorio: {respiratory_effort}/2
- Tono muscolare: {muscle_tone}/2
- Riflessi/irritabilità: {reflex_irritability}/2
- Colorito: {color}/2

Interpretazione clinica:
• Score 8-10: Neonato normale
• Score 4-7: Moderatamente depresso
• Score 0-3: Severamente depresso

Note: Valutazione a 1 e 5 minuti dalla nascita
"""
    return [types.TextContent(type="text", text=result)]

def _calculate_gcs_pediatric(args):
    """Calcola Glasgow Coma Scale pediatrica"""
    eye_opening = args.get('eye_opening', 1)
    verbal_response = args.get('verbal_response', 1) 
    motor_response = args.get('motor_response', 1)
    age_months = args.get('age_months', 12)
    
    total = eye_opening + verbal_response + motor_response
    interpretation = calculate_gcs_pediatric_interpretation(total)
    
    # Adattamenti per età
    age_note = ""
    if age_months < 24:
        age_note = "\nNota: Scala adattata per età <2 anni - Valutazione più complessa"
    
    result = f"""Glasgow Coma Scale Pediatrica
==============================
Età paziente: {age_months} mesi
Punteggio totale: {total}/15

Severità: {interpretation['severity']}
Prognosi: {interpretation['prognosis']}
Azione: {interpretation['action']}

Dettaglio punteggi:
- Apertura occhi: {eye_opening}/4
- Risposta verbale: {verbal_response}/5
- Risposta motoria: {motor_response}/6

Interpretazione:
• 13-15: Trauma cranico lieve
• 9-12: Trauma cranico moderato  
• 3-8: Trauma cranico severo

{age_note}

Indicazioni per monitoraggio:
- GCS <9: Intubazione e ventilazione
- GCS 9-12: Osservazione intensiva
- GCS >12: Monitoraggio standard
"""
    return [types.TextContent(type="text", text=result)]

def _calculate_mchat(args):
    """Calcola M-CHAT Score"""
    
    # Domande critiche (punteggio doppio se negative)
    critical_items = ['points_to_show_interest', 'brings_objects_to_show', 'looks_in_eyes', 
                     'responds_to_name', 'looks_at_pointed_objects', 'tries_to_attract_attention']
    
    failed_items = []
    critical_failed = 0
    total_failed = 0
    
    # Controllo risposte (False = fallimento)
    question_map = {
        'enjoys_swinging': 'Godere del dondolo',
        'interest_other_children': 'Interesse per altri bambini',
        'enjoys_climbing': 'Godere dell\'arrampicata',
        'enjoys_peekaboo': 'Godere del cu-cu',
        'pretend_play': 'Gioco simbolico',
        'points_to_request': 'Indicare per richiedere',
        'points_to_show_interest': 'Indicare per interesse (*)',
        'plays_appropriately_toys': 'Gioco appropriato con giocattoli',
        'brings_objects_to_show': 'Portare oggetti per mostrare (*)',
        'looks_in_eyes': 'Contatto oculare (*)',
        'oversensitive_noise': 'Ipersensibilità ai rumori (inverso)',
        'smiles_in_response': 'Sorriso responsivo',
        'imitates_actions': 'Imitazione',
        'responds_to_name': 'Risposta al nome (*)',
        'points_at_airplane': 'Seguire indicazione (aeroplano)',
        'walks_independently': 'Cammino indipendente',
        'looks_at_pointed_objects': 'Seguire pointing (*)',
        'unusual_finger_movements': 'Movimenti strani dita (inverso)',
        'tries_to_attract_attention': 'Ricerca attenzione (*)',
        'suspected_hearing_problem': 'Sospetto problema udito (inverso)'
    }
    
    # Items che se presenti indicano rischio (inversi)
    reverse_items = ['oversensitive_noise', 'unusual_finger_movements', 'suspected_hearing_problem']
    
    for item, value in args.items():
        expected = False if item in reverse_items else True
        
        if value != expected:
            total_failed += 1
            failed_items.append(question_map[item])
            
            if item in critical_items:
                critical_failed += 1
    
    # Interpretazione
    if critical_failed >= 2 or total_failed >= 3:
        risk_level = "ALTO RISCHIO"
        recommendation = "Riferimento immediato per valutazione specialistica autismo"
        follow_up = "Valutazione diagnostica approfondita entro 1 mese"
    elif total_failed >= 2:
        risk_level = "RISCHIO MODERATO"
        recommendation = "Follow-up M-CHAT a 24 mesi, osservazione clinica"
        follow_up = "Rivalutazione tra 1-3 mesi"
    else:
        risk_level = "BASSO RISCHIO"
        recommendation = "Sviluppo nella norma, screening di routine"
        follow_up = "Screening standard ai controlli programmati"
    
    result = f"""M-CHAT (Modified Checklist for Autism in Toddlers)
=================================================
Items falliti totali: {total_failed}/20
Items critici falliti: {critical_failed}/6

Livello di rischio: {risk_level}
Raccomandazione: {recommendation}
Follow-up: {follow_up}

Items falliti:
{chr(10).join(['• ' + item for item in failed_items]) if failed_items else '• Nessun item fallito'}

Interpretazione:
• ≥2 item critici falliti O ≥3 item totali: Alto rischio autismo
• 2 item totali falliti: Rischio moderato, follow-up
• 0-1 item falliti: Basso rischio

Note importanti:
- Età target: 16-30 mesi
- (*) = Item critico
- Sensibilità 95%, Specificità 95%
- Follow-up M-CHAT raccomandato se rischio moderato
- Valutazione specialistica se alto rischio
"""
    return [types.TextContent(type="text", text=result)]

def _calculate_pediatric_trauma_score(args):
    """Calcola Pediatric Trauma Score (PTS)"""
    weight_kg = args.get('weight_kg', 0)
    systolic_bp = args.get('systolic_bp', 0)
    conscious = args.get('conscious', False)
    open_wound = args.get('open_wound', False)
    fracture = args.get('fracture', False)
    cutaneous = args.get('cutaneous', False)
    
    # Calcolo punteggio PTS
    score = 0
    details = []
    
    # Peso
    if weight_kg > 20:
        score += 2
        details.append("• Peso >20kg: +2")
    elif weight_kg >= 10:
        score += 1
        details.append("• Peso 10-20kg: +1")
    else:
        score -= 1
        details.append("• Peso <10kg: -1")
    
    # Pressione sistolica
    if systolic_bp > 90:
        score += 2
        details.append("• PA >90mmHg: +2")
    elif systolic_bp >= 50:
        score += 1
        details.append("• PA 50-90mmHg: +1")
    else:
        score -= 1
        details.append("• PA <50mmHg: -1")
    
    # Stato di coscienza
    if conscious:
        score += 2
        details.append("• Paziente sveglio: +2")
    else:
        score -= 1
        details.append("• Paziente in coma: -1")
    
    # Ferita
    if not open_wound:
        score += 2
        details.append("• Nessuna ferita aperta: +2")
    else:
        score -= 1
        details.append("• Ferita maggiore/penetrante: -1")
    
    # Frattura
    if not fracture:
        score += 2
        details.append("• Nessuna frattura: +2")
    else:
        score -= 1
        details.append("• Frattura aperta/multipla: -1")
    
    # Cute
    if cutaneous:
        score += 2
        details.append("• Cute intatta: +2")
    else:
        score -= 1
        details.append("• Perdita sostanza cutanea: -1")
    
    # Interpretazione
    if score > 8:
        risk_level = "MINIMO"
        management = "Valutazione standard - Trauma lieve"
    elif score >= 6:
        risk_level = "MODERATO"
        management = "Valutazione trauma team - Potenziale pericolo"
    elif score >= 0:
        risk_level = "SEVERO"
        management = "Trauma team - Stabilizzazione prioritaria"
    else:
        risk_level = "CRITICO"
        management = "Rianimazione immediata - Estremo pericolo"
    
    result = f"""Pediatric Trauma Score (PTS)
========================
Punteggio totale: {score}/12

Livello di rischio: {risk_level}
Gestione: {management}

Criteri valutati:
{chr(10).join(details)}

Interpretazione clinica:
- >8: Trauma minore - Basso rischio
- 6-8: Trauma moderato - Potenziale pericolo per la vita
- 0-5: Trauma severo - Pericolo per la vita
- <0: Trauma critico - Estremo pericolo

Note:
- Score più utilizzato in pediatria per triage traumatologico
- Forte correlatore di mortalità e necessità di cure intensive
- PTS <8 richiede centro traumatologico pediatrico
- PTS <6 associato a mortalità >25%
"""
    return [types.TextContent(type="text", text=result)]

def _calculate_catch_score(args):
    """Calcola CATCH (Canadian Assessment of Tomography for Childhood Head injury)"""
    vomiting = args.get('vomiting', False)
    headache = args.get('headache', False)
    gcsscore = args.get('gcsscore', 15)
    suspected_skull_fracture = args.get('suspected_skull_fracture', False)
    dangerous_mechanism = args.get('dangerous_mechanism', False)
    
    # Calcolo punteggio
    score = 0
    risk_factors = []
    
    if gcsscore < 15:
        score += 1
        risk_factors.append("• GCS <15 a 2h dal trauma")
    if suspected_skull_fracture:
        score += 1
        risk_factors.append("• Sospetta frattura cranica")
    if vomiting:
        score += 1
        risk_factors.append("• Vomito ≥3 episodi")
    if dangerous_mechanism:
        score += 1
        risk_factors.append("• Meccanismo traumatico pericoloso")
    if headache:
        score += 1
        risk_factors.append("• Cefalea severa")
    
    # Interpretazione
    if score >= 1:
        risk_level = "ALTO"
        recommendation = "TC encefalo raccomandata"
    else:
        risk_level = "BASSO"
        recommendation = "TC encefalo non necessaria - Osservazione"
    
    result = f"""CATCH Score (Canadian Assessment of Tomography for Childhood Head injury)
========================================================================
Punteggio totale: {score}/5

Livello di rischio: {risk_level}
Raccomandazione: {recommendation}

Fattori di rischio presenti:
{chr(10).join(risk_factors) if risk_factors else '• Nessun fattore di rischio presente'}

Criteri CATCH:
- GCS <15 a 2 ore dal trauma
- Sospetta frattura cranica aperta/depressa
- Storia di vomito ≥3 episodi
- Segni di frattura della base cranica
- Meccanismo traumatico pericoloso
- Cefalea severa

Nota clinica: 
- Applicabile per traumi cranici con GCS 13-15
- Età 0-16 anni
- La presenza di ANCHE UN SOLO criterio indica necessità di TC
- Sensibilità 98%, Specificità 50%
- Se tutti negativi, rischio lesioni cerebrali <1%
"""
    return [types.TextContent(type="text", text=result)]

def _calculate_westley_croup_score(args):
    """Calcola Westley Croup Score"""
    stridor = args.get('stridor', 0)
    retraction = args.get('retraction', 0)
    air_entry = args.get('air_entry', 0)
    cyanosis = args.get('cyanosis', 0)
    consciousness = args.get('consciousness', 0)
    
    total_score = stridor + retraction + air_entry + cyanosis + consciousness
    
    # Interpretazione
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
    
    result = f"""Westley Croup Score
==================
Punteggio totale: {total_score}/17

Severità: {severity}
Gestione: {management}

Dettaglio punteggi:
- Stridore inspiratorio: {stridor}/2
- Retrazioni: {retraction}/3
- Ingresso d'aria: {air_entry}/2
- Cianosi: {cyanosis}/4
- Livello di coscienza: {consciousness}/5

Interpretazione:
- 0-2: Croup lieve - Steroidi e osservazione domiciliare
- 3-5: Croup moderato - Osservazione ospedaliera
- 6-11: Croup severo - Trattamento intensivo
- ≥12: Croup critico - Insufficienza respiratoria imminente

Criteri di score:
1. Stridore inspiratorio: 0=nessuno, 1=con agitazione, 2=a riposo
2. Retrazioni: 0=nessuna, 1=lievi, 2=moderate, 3=severe
3. Ingresso d'aria: 0=normale, 1=diminuito, 2=marcatamente diminuito
4. Cianosi: 0=nessuna, 4=con agitazione, 5=a riposo
5. Coscienza: 0=normale, 5=alterata
"""
    return [types.TextContent(type="text", text=result)]

def _calculate_centor_score_pediatric(args):
    """Calcola Centor Score modificato per faringite streptococcica pediatrica"""
    age_years = args.get('age_years', 0)
    exudate = args.get('exudate', False)
    tender_nodes = args.get('tender_nodes', False)
    fever = args.get('fever', False)
    cough = args.get('cough', False)
    
    # Calcolo punteggio
    score = 0
    criteria = []
    
    if exudate:
        score += 1
        criteria.append("• Essudato tonsillare: +1")
    if tender_nodes:
        score += 1
        criteria.append("• Linfoadenopatia cervicale dolente: +1")
    if fever:
        score += 1
        criteria.append("• Febbre >38°C: +1")
    if not cough:
        score += 1
        criteria.append("• Assenza di tosse: +1")
    if 3 <= age_years <= 14:
        score += 1
        criteria.append("• Età 3-14 anni: +1")
    
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
    
    result = f"""Centor Score Pediatrico (Faringite Streptococcica)
============================================
Età paziente: {age_years} anni
Punteggio totale: {score}/5

Probabilità infezione streptococcica: {probability}
Raccomandazione: {recommendation}

Criteri presenti:
{chr(10).join(criteria) if criteria else '• Nessun criterio presente'}

Interpretazione:
- 0-1: Probabilità <10% - No test/antibiotici
- 2: Probabilità 10-17% - Test rapido
- 3: Probabilità 30-35% - Test rapido
- 4-5: Probabilità >50% - Test rapido o terapia empirica

Note cliniche:
- Score modificato per pediatria (aggiunge età 3-14 anni)
- Utile in contesti ambulatoriali per razionalizzare test/antibiotici
- Valore predittivo migliorato associando test rapido (Strep A)
- Considerare fattori epidemiologici (contatti familiari, stagionalità)
"""
    return [types.TextContent(type="text", text=result)]

def _calculate_wells_score_pediatric(args):
    """Calcola Wells Score pediatrico per TVP"""
    provoked_dvt = args.get('provoked_dvt', False)
    alternative_diagnosis = args.get('alternative_diagnosis', False)
    swelling = args.get('swelling', False)
    unilateral_tenderness = args.get('unilateral_tenderness', False)
    swelling_thigh_calf = args.get('swelling_thigh_calf', False)
    unilateral_pitting = args.get('unilateral_pitting', False)
    bedridden = args.get('bedridden', False)
    active_cancer = args.get('active_cancer', False)
    previous_dvt = args.get('previous_dvt', False)
    
    # Calcolo punteggio
    score = 0
    details = []
    
    if provoked_dvt:
        score += 1
        details.append("• TVP provocata: +1")
    if alternative_diagnosis:
        score -= 2
        details.append("• Diagnosi alternativa possibile: -2")
    if swelling:
        score += 1
        details.append("• Gonfiore intero arto: +1")
    if unilateral_tenderness:
        score += 1
        details.append("• Dolorabilità vene profonde: +1")
    if swelling_thigh_calf:
        score += 1
        details.append("• Gonfiore polpaccio >3cm: +1")
    if unilateral_pitting:
        score += 1
        details.append("• Edema improntabile monolaterale: +1")
    if bedridden:
        score += 1
        details.append("• Allettamento recente >3 giorni: +1")
    if active_cancer:
        score += 1
        details.append("• Cancro attivo: +1")
    if previous_dvt:
        score += 1
        details.append("• Precedente TVP: +1")
    
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
    
    result = f"""Wells Score Pediatrico per TVP
==========================
Punteggio totale: {score}

Probabilità TVP: {probability}
Raccomandazione: {recommendation}

Criteri presenti:
{chr(10).join(details) if details else '• Nessun criterio presente'}

Interpretazione:
- ≥2: Alta probabilità TVP - Ecografia urgente
- 1: Moderata probabilità - Ecografia + D-dimero
- ≤0: Bassa probabilità - D-dimero

Note:
- Validato in popolazione pediatrica
- D-dimero falsi positivi frequenti in bambini
- Combinare con ecografia per decisioni cliniche
- Soglie adattate per bambini (differenti da adulti)
- Considerare fattori di rischio aggiuntivi (CVC, immobilità)
"""
    return [types.TextContent(type="text", text=result)]
def _calculate_pas_asthma(args):
    """Calcola Pediatric Asthma Score"""
    respiratory_rate = args.get('respiratory_rate', 0)
    oxygen_requirement = args.get('oxygen_requirement', 0)
    auscultation = args.get('auscultation', 0)
    retractions = args.get('retractions', 0)
    dyspnea = args.get('dyspnea', 0)
    
    total = respiratory_rate + oxygen_requirement + auscultation + retractions + dyspnea
    interpretation = calculate_pas_asthma_interpretation(total)
    
    result = f"""Pediatric Asthma Score (PAS)
=========================
Punteggio totale: {total}/15
Severità: {interpretation['severity']}
Raccomandazione: {interpretation['recommendation']}

Dettaglio punteggi:
- Frequenza respiratoria: {respiratory_rate}/3
- Richiesta di ossigeno: {oxygen_requirement}/3
- Auscultazione: {auscultation}/3
- Retrazioni: {retractions}/3
- Dispnea: {dyspnea}/3

Interpretazione clinica:
- Score 0-4: Asma lieve
- Score 5-7: Asma moderata
- Score 8-11: Asma severa
- Score 12-15: Asma critica/potenziale arresto respiratorio

Nota: Il PAS è uno strumento di valutazione oggettiva della gravità dell'asma
utilizzato nei contesti di emergenza e per monitorare la risposta al trattamento.
"""
    return [types.TextContent(type="text", text=result)]

def _calculate_pass_asthma(args):
    """Calcola Pediatric Asthma Severity Score (PASS)"""
    wheezing = args.get('wheezing', 0)
    work_of_breathing = args.get('work_of_breathing', 0)
    prolonged_expiration = args.get('prolonged_expiration', 0)
    
    total = wheezing + work_of_breathing + prolonged_expiration
    interpretation = calculate_pass_asthma_interpretation(total)
    
    result = f"""Pediatric Asthma Severity Score (PASS)
==================================
Punteggio totale: {total}/6
Severità: {interpretation['severity']}
Raccomandazione: {interpretation['recommendation']}

Dettaglio punteggi:
- Wheezing: {wheezing}/2
- Lavoro respiratorio: {work_of_breathing}/2
- Espirazione prolungata: {prolonged_expiration}/2

Interpretazione clinica:
- Score 0-2: Asma lieve
- Score 3-4: Asma moderata
- Score 5-6: Asma severa

Nota: Il PASS è uno score validato e semplificato a 3 parametri,
utile per la valutazione rapida dell'esacerbazione asmatica
in contesti di emergenza pediatrica.
"""
    return [types.TextContent(type="text", text=result)]

def _calculate_bacterial_meningitis_score(args):
    """Calcola Bacterial Meningitis Score for Children"""
    total_score = 0
    criteria = []
    
    if args.get('csf_gram_stain_positive', False):
        total_score += 2
        criteria.append("• Colorazione di Gram positiva nel liquor: +2")
    
    if args.get('csf_anc_geq_1000', False):
        total_score += 1
        criteria.append("• Neutrofili liquorali ≥1000 cell/μL: +1")
    
    if args.get('csf_protein_geq_80', False):
        total_score += 1
        criteria.append("• Proteine liquorali ≥80 mg/dL: +1")
    
    if args.get('peripheral_anc_geq_10000', False):
        total_score += 1
        criteria.append("• Neutrofili periferici ≥10000 cell/μL: +1")
    
    if args.get('seizure_at_onset', False):
        total_score += 1
        criteria.append("• Convulsioni all'esordio: +1")
    
    interpretation = calculate_bacterial_meningitis_score_interpretation(total_score)
    
    result = f"""Bacterial Meningitis Score for Children
====================================
Punteggio totale: {total_score}/6

Rischio di meningite batterica: {interpretation['risk']}
Raccomandazione: {interpretation['recommendation']}

Criteri presenti:
{chr(10).join(criteria) if criteria else "• Nessun criterio presente"}

Interpretazione clinica:
- Score 0: Rischio molto basso (<0.1%)
- Score 1: Rischio basso (0.4-2.5%)
- Score ≥2: Rischio alto (>8%)

Note cliniche:
- Applicabile a bambini ≥2 mesi con meningite a liquor limpido
- Non applicabile in caso di antibioticoterapia nelle 72h precedenti
- Non applicabile in caso di comorbilità o immunodepressione
- Score validato in diversi contesti clinici con elevato valore predittivo negativo
- Un punteggio ≥2 ha sensibilità 99-100% per meningite batterica

Criteri di esclusione originali dello studio:
- Condizioni critiche/immunocompromissione
- Presenza di shunt/dispositivi neurochirurgici
- Trauma cranico recente o neurochirurgia
- Convulsioni epilettiche note
"""
    return [types.TextContent(type="text", text=result)]

def _calculate_kocher_criteria(args):
    """Calcola Kocher Criteria per artrite settica dell'anca"""
    total_score = 0
    criteria = []
    
    if args.get('fever', False):
        total_score += 1
        criteria.append("• Febbre >38.5°C")
    
    if args.get('weight_bearing', False):
        total_score += 1
        criteria.append("• Incapacità/rifiuto di carico sull'arto")
    
    if args.get('esr_elevated', False):
        total_score += 1
        criteria.append("• VES >40 mm/h")
    
    if args.get('wbc_elevated', False):
        total_score += 1
        criteria.append("• Leucociti >12,000/μL")
    
    interpretation = calculate_kocher_criteria_interpretation(total_score)
    
    result = f"""Kocher Criteria per Artrite Settica dell'Anca
=========================================
Criteri positivi: {total_score}/4

Probabilità di artrite settica: {interpretation['probability']}
Raccomandazione: {interpretation['recommendation']}

Criteri presenti:
{chr(10).join(criteria) if criteria else "• Nessun criterio presente"}

Interpretazione clinica:
- 0 criteri: <0.2% probabilità di artrite settica
- 1 criterio: ~3% probabilità
- 2 criteri: ~40% probabilità
- 3 criteri: ~93% probabilità
- 4 criteri: ~99% probabilità

Note cliniche:
- Criteri validati per bambini con dolore o limitazione articolare dell'anca
- La PCR elevata (>2.0 mg/dL) è stata aggiunta successivamente come quinto criterio
- Strumento di screening, non sostituisce il giudizio clinico
- Un'ecografia dell'anca con versamento è compatibile ma non specifica
- L'aspirazione articolare rimane il gold standard diagnostico

Diagnosi differenziali da considerare:
- Sinovite transitoria dell'anca
- Osteomielite
- Artrite reumatoide giovanile
- Malattia di Legg-Calvé-Perthes
- Epifisiolisi della testa femorale
"""
    return [types.TextContent(type="text", text=result)]

def _calculate_kawasaki_criteria(args):
    """Valuta criteri diagnostici per malattia di Kawasaki"""
    has_fever = args.get('fever_5_days', False)
    
    # Conteggio criteri clinici principali
    clinical_criteria = [
        'conjunctival_injection', 
        'oral_changes', 
        'extremity_changes',
        'polymorphous_rash', 
        'cervical_lymphadenopathy'
    ]
    
    criteria_count = 0
    criteria_present = []
    
    for criterion in clinical_criteria:
        if args.get(criterion, False):
            criteria_count += 1
            criteria_present.append(f"• {criterion.replace('_', ' ').title()}")
    
    # Valutazione laboratorio ed ecocardiografia
    lab_findings = args.get('laboratory_findings', [])
    echo_findings = args.get('echocardiogram_findings', [])
    
    lab_findings_text = ""
    if lab_findings:
        lab_findings_text = "Alterazioni di laboratorio:\n" + "\n".join([f"• {item.replace('_', ' ').title()}" for item in lab_findings])
    
    echo_findings_text = ""
    if echo_findings:
        echo_findings_text = "Reperti ecocardiografici:\n" + "\n".join([f"• {item.replace('_', ' ').replace('gt', '>').title()}" for item in echo_findings])
    
    # Interpretazione
    interpretation = calculate_kawasaki_criteria_interpretation(has_fever, criteria_count)
    
    result = f"""Criteri Diagnostici per Malattia di Kawasaki
=========================================
Diagnosi: {interpretation['diagnosis']}
Raccomandazione: {interpretation['recommendation']}

Febbre ≥5 giorni: {'Presente' if has_fever else 'Assente'}
Criteri clinici principali presenti: {criteria_count}/5

Criteri clinici:
{chr(10).join(criteria_present) if criteria_present else "• Nessun criterio presente"}

{lab_findings_text if lab_findings_text else ""}

{echo_findings_text if echo_findings_text else ""}

Interpretazione:
- Kawasaki classico: Febbre ≥5 giorni + ≥4 criteri clinici principali
- Kawasaki incompleto: Febbre ≥5 giorni + 2-3 criteri clinici + anomalie laboratorio/ecocardiografia
- Kawasaki atipico: Presentazione clinica insolita con febbre e anomalie coronariche

Note cliniche:
- Il trattamento tempestivo (entro 10 giorni) riduce il rischio di anomalie coronariche
- Trattamento standard: IVIG 2g/kg in singola dose + ASA (80-100mg/kg/die)
- Monitoraggio ecocardiografico: alla diagnosi, a 2 settimane e a 6-8 settimane
- Fino al 25% dei pazienti non trattati sviluppa anomalie coronariche
- Per Kawasaki incompleto: valutare algoritmo AHA per supporto diagnostico

Criteri di laboratorio supplementari per Kawasaki incompleto:
- Albumina ≤3.0 g/dL
- Anemia per età
- Elevazione ALT
- Piastrine ≥450,000/mm³ dopo 7 giorni
- GB ≥15,000/mm³
- Piuria sterile
"""
    return [types.TextContent(type="text", text=result)]

def _calculate_hsp_criteria(args):
    """Valuta criteri EULAR/PRINTO/PRES per diagnosi di Porpora di Henoch-Schönlein"""
    palpable_purpura = args.get('palpable_purpura', False)
    
    # Conteggio criteri aggiuntivi
    additional_criteria = [
        'abdominal_pain', 
        'histopathology', 
        'arthritis_arthralgia',
        'renal_involvement'
    ]
    
    criteria_count = 0
    criteria_present = []
    
    if palpable_purpura:
        criteria_present.append("• Porpora palpabile (criterio obbligatorio)")
    
    for criterion in additional_criteria:
        if args.get(criterion, False):
            criteria_count += 1
            criteria_present.append(f"• {criterion.replace('_', ' ').title()}")
    
    # Diagnosi
    if palpable_purpura and criteria_count >= 1:
        diagnosis = "CRITERI HSP SODDISFATTI"
        recommendation = "Diagnosi di Porpora di Henoch-Schönlein (HSP) confermata."
    else:
        diagnosis = "CRITERI HSP NON SODDISFATTI"
        if not palpable_purpura:
            recommendation = "Criterio obbligatorio (porpora palpabile) non presente. Considerare diagnosi alternative."
        else:
            recommendation = "Necessario almeno un criterio aggiuntivo oltre alla porpora palpabile."
    
    result = f"""Criteri EULAR/PRINTO/PRES per Porpora di Henoch-Schönlein (HSP)
===========================================================
Diagnosi: {diagnosis}
Raccomandazione: {recommendation}

Criteri presenti:
{chr(10).join(criteria_present) if criteria_present else "• Nessun criterio presente"}

Criteri aggiuntivi presenti: {criteria_count}/4

Interpretazione:
- Criterio obbligatorio: Porpora palpabile non piastrinopenica
- Diagnosi HSP: Criterio obbligatorio + almeno 1 dei seguenti:
  - Dolore addominale
  - Istologia con depositi di IgA
  - Artrite/artralgia
  - Coinvolgimento renale (ematuria/proteinuria)

Note cliniche:
- HSP è la vasculite più comune in età pediatrica
- Età tipica: 3-10 anni, più comune in maschi
- Porpora tipicamente localizzata a arti inferiori e glutei
- Monitoraggio renale per 6 mesi è raccomandato
- Prognosi generalmente buona, complicanze renali nel 20-30%
- Trattamento: supportivo nella maggior parte dei casi
- Steroidi indicati in caso di grave coinvolgimento gastrointestinale/articolare

Fonte: Criteri EULAR/PRINTO/PRES 2010
"""
    return [types.TextContent(type="text", text=result)]
def _calculate_jones_criteria(args):
    """Valuta criteri di Jones per diagnosi di febbre reumatica acuta"""
    prior_rheumatic_heart_disease = args.get('prior_rheumatic_heart_disease', False)
    high_risk_population = args.get('high_risk_population', False)
    confirmed_strep_infection = args.get('confirmed_strep_infection', False)
    major_criteria = args.get('major_criteria', [])
    minor_criteria = args.get('minor_criteria', [])
    
    # Validazione della poliartralgia nei criteri maggiori per popolazione ad alto rischio
    if "polyarthralgia" in major_criteria and not high_risk_population:
        major_criteria.remove("polyarthralgia")
    
    # Validazione della monoartralgia nei criteri minori per popolazione ad alto rischio
    if "monoarthralgia" in minor_criteria and not high_risk_population:
        minor_criteria.remove("monoarthralgia")
    
    # Verifica della cardite subclinica (solo con ecocardiografia)
    has_subclinical_carditis = "subclinical_carditis" in major_criteria
    
    # Conteggio criteri
    major_count = len(major_criteria)
    minor_count = len(minor_criteria)
    
    # Diagnosi in caso di primo episodio
    if not prior_rheumatic_heart_disease:
        if major_count >= 2:
            diagnosis = "FEBBRE REUMATICA ACUTA CONFERMATA"
            details = "Primo episodio con ≥2 criteri maggiori"
        elif major_count == 1 and minor_count >= 2:
            diagnosis = "FEBBRE REUMATICA ACUTA CONFERMATA"
            details = "Primo episodio con 1 criterio maggiore + ≥2 criteri minori"
        else:
            diagnosis = "CRITERI NON SODDISFATTI"
            details = "Insufficienti criteri per febbre reumatica acuta"
    
    # Diagnosi in caso di recidiva
    else:
        if major_count >= 2:
            diagnosis = "RECIDIVA DI FEBBRE REUMATICA CONFERMATA"
            details = "Recidiva con ≥2 criteri maggiori"
        elif major_count == 1 and minor_count >= 2:
            diagnosis = "RECIDIVA DI FEBBRE REUMATICA CONFERMATA"
            details = "Recidiva con 1 criterio maggiore + ≥2 criteri minori"
        elif major_count == 0 and minor_count >= 3:
            diagnosis = "RECIDIVA DI FEBBRE REUMATICA CONFERMATA"
            details = "Recidiva con ≥3 criteri minori"
        else:
            diagnosis = "CRITERI NON SODDISFATTI PER RECIDIVA"
            details = "Insufficienti criteri per recidiva di febbre reumatica"
    
    # Raccomandazione
    if not confirmed_strep_infection:
        recommendation = "ATTENZIONE: Evidenza di infezione streptococcica precedente è essenziale per la diagnosi."
        diagnosis = "DIAGNOSI INCERTA"
    elif diagnosis.startswith("FEBBRE") or diagnosis.startswith("RECIDIVA"):
        recommendation = "Iniziare trattamento appropriato e profilassi secondaria."
    else:
        recommendation = "Considerare diagnosi alternative."
    
    result = f"""Criteri di Jones (2015) per Febbre Reumatica Acuta
===========================================
Diagnosi: {diagnosis}
Dettagli: {details}
Raccomandazione: {recommendation}

{'Popolazione ad alto rischio: SÌ' if high_risk_population else 'Popolazione ad alto rischio: NO'}
{'Precedente cardiopatia reumatica: SÌ' if prior_rheumatic_heart_disease else 'Precedente cardiopatia reumatica: NO'}
{'Infezione streptococcica confermata: SÌ' if confirmed_strep_infection else 'Infezione streptococcica confermata: NO (RICHIESTA)'}

Criteri maggiori presenti ({major_count}):
{chr(10).join(['• ' + c.replace('_', ' ').title() for c in major_criteria]) if major_criteria else '• Nessuno'}

Criteri minori presenti ({minor_count}):
{chr(10).join(['• ' + c.replace('_', ' ').title() for c in minor_criteria]) if minor_criteria else '• Nessuno'}

Interpretazione:
- Primo episodio: 
  - ≥2 criteri maggiori, o
  - 1 criterio maggiore + ≥2 criteri minori
- Recidiva:
  - ≥2 criteri maggiori, o
  - 1 criterio maggiore + ≥2 criteri minori, o
  - ≥3 criteri minori

Note:
- La poliartralgia è criterio maggiore SOLO in popolazioni ad alto rischio
- La cardite subclinica (anomalie ecocardiografiche senza soffi) è criterio maggiore
- Evidenza di infezione streptococcica recente è necessaria per la diagnosi
- In caso di corea o cardite indolente, l'evidenza di infezione streptococcica può non essere richiesta
- La profilassi secondaria è essenziale per prevenire recidive

Fonte: Criteri di Jones aggiornati (AHA 2015)
"""
    return [types.TextContent(type="text", text=result)]

def _calculate_bops(args):
    """Calcola Behavioral Observational Pain Scale (BOPS)"""
    facial_expression = args.get('facial_expression', 0)
    verbalization = args.get('verbalization', 0)
    body_position = args.get('body_position', 0)
    
    total = facial_expression + verbalization + body_position
    interpretation = calculate_bops_interpretation(total)
    
    result = f"""Behavioral Observational Pain Scale (BOPS)
=======================================
Punteggio totale: {total}/6
Livello di dolore: {interpretation['pain_level']}
Raccomandazione: {interpretation['recommendation']}

Dettaglio punteggi:
- Espressione facciale: {facial_expression}/2
- Verbalizzazione: {verbalization}/2
- Posizione corporea: {body_position}/2

Interpretazione:
- 0-1: Nessun dolore
- 2-3: Dolore lieve
- 4: Dolore moderato
- 5-6: Dolore severo

Note cliniche:
- Scala validata per bambini di 1-7 anni nel postoperatorio
- Monitoraggio semplice e rapido (< 1 minuto)
- Particolarmente utile nel setting di recovery room
- Alta affidabilità inter-osservatore
- Complementare alla valutazione dell'intensità dolore con altre scale
- Rivalutare dopo ogni intervento analgesico

Fonte: Behavioural Observational Pain Scale di Hesselgard et al.
"""
    return [types.TextContent(type="text", text=result)]

def _calculate_lansky_score(args):
    """Calcola Lansky Play-Performance Scale"""
    performance_level = args.get('performance_level', 0)
    age_months = args.get('age_months', 0)
    age_years = age_months / 12
    
    # Definizione dei livelli funzionali
    levels = {
        100: "Attività normale, nessuna limitazione",
        90: "Limitazioni minori nelle attività fisiche intense",
        80: "Attivo, ma si stanca più facilmente",
        70: "Restrizioni maggiori nel gioco e minore tempo di attività",
        60: "In piedi, attivo, ma gioco minimo; mantiene se stesso occupato con attività più tranquille",
        50: "Vestito, nessun gioco attivo, sedentario, in grado di partecipare a tutte le attività calme",
        40: "Maggior parte del tempo a letto; partecipa ad attività calme",
        30: "A letto; bisogno di assistenza anche per gioco calmo",
        20: "Spesso addormentato; gioco limitato ad attività molto passive",
        10: "Nessun gioco; non si alza dal letto; mantiene attività passive",
        0: "Non responsivo"
    }
    
    current_level = levels.get(performance_level, "Livello non definito")
    
    # Interpretazione funzionale
    if performance_level >= 90:
        functional_status = "OTTIMO"
        recommendation = "Nessuna restrizione significativa, monitoraggio di routine"
    elif performance_level >= 70:
        functional_status = "BUONO"
        recommendation = "Limitazioni minime, considerare supporto per attività intense"
    elif performance_level >= 50:
        functional_status = "MODERATO"
        recommendation = "Significative limitazioni nel gioco attivo, valutare supporto domiciliare"
    elif performance_level >= 30:
        functional_status = "SCARSO"
        recommendation = "Prevalentemente a letto, valutare necessità di assistenza sanitaria"
    else:
        functional_status = "GRAVE"
        recommendation = "Necessaria assistenza continua, considerare cure palliative/intensive"
    
    result = f"""Lansky Play-Performance Scale
==========================
Età: {age_years:.1f} anni ({age_months} mesi)
Punteggio: {performance_level}/100

Stato funzionale: {functional_status}
Descrizione: {current_level}
Raccomandazione: {recommendation}

Interpretazione clinica:
- 100-90: Attività normale o con limitazioni minime
- 80-70: Attivo ma con affaticabilità aumentata
- 60-50: In piedi, gioco ridotto, prevalenza attività calme
- 40-30: Maggior parte del tempo a letto, bisogno di assistenza
- 20-10: Allettato, attività molto limitate
- 0: Non responsivo

Note:
- Scala validata per bambini di 0-16 anni
- Utilizzata principalmente in oncologia pediatrica e cure palliative
- Utile per:
  * Valutazione baseline e follow-up
  * Decisioni terapeutiche
  * Criteri di ammissione a studi clinici
  * Quantificazione risultati terapeutici
- Punteggio <50 indica necessità di assistenza importante
- Punteggio <30 indica compromissione severa della qualità di vita

Fonte: Lansky Play-Performance Scale, Lansky et al. 1987
"""
    return [types.TextContent(type="text", text=result)]
def _calculate_sickle_cell_complication_risk(args):
    """Calcola rischio di complicanze severe in anemia falciforme pediatrica"""
    hemoglobin_level = args.get('hemoglobin_level', 0)
    wbc_count = args.get('wbc_count', 0)
    history_of_acs = args.get('history_of_acs', False)
    pain_events_per_year = args.get('pain_events_per_year', 0)
    dactylitis_under_1_year = args.get('dactylitis_under_1_year', False)
    hemoglobin_f_level = args.get('hemoglobin_f_level', 0)
    genotype = args.get('genotype', "").lower()
    
    # Fattori di rischio
    risk_factors = []
    
    if hemoglobin_level < 7:
        risk_factors.append(f"• Emoglobina basale bassa: {hemoglobin_level} g/dL (<7 g/dL)")
    
    if wbc_count > 15:
        risk_factors.append(f"• Leucocitosi: {wbc_count} x10^3/μL (>15 x10^3/μL)")
    
    if history_of_acs:
        risk_factors.append("• Storia di sindrome toracica acuta")
    
    if pain_events_per_year >= 3:
        risk_factors.append(f"• Eventi dolorosi frequenti: {pain_events_per_year}/anno (≥3/anno)")
    
    if dactylitis_under_1_year:
        risk_factors.append("• Dattilite prima dell'anno di età")
    
    if hemoglobin_f_level < 10:
        risk_factors.append(f"• Emoglobina fetale bassa: {hemoglobin_f_level}% (<10%)")
    
    if genotype in ["ss", "sbeta0"]:
        risk_factors.append(f"• Genotipo a rischio elevato: {genotype.upper()}")
    
    # Determinazione del rischio
    risk_count = len(risk_factors)
    
    if risk_count == 0:
        risk_level = "BASSO"
        recommendation = "Monitoraggio standard, profilassi infezioni, screening complicanze"
    elif risk_count <= 2:
        risk_level = "INTERMEDIO"
        recommendation = "Monitoraggio più frequente, considerare idrossiurea"
    else:
        risk_level = "ALTO"
        recommendation = "Idrossiurea fortemente raccomandata, monitoraggio intensivo"
    
    # Raccomandazioni per idrossiurea
    hydroxyurea_indication = "NO"
    if (history_of_acs or pain_events_per_year >= 3) and genotype in ["ss", "sbeta0"]:
        hydroxyurea_indication = "SÌ"
    
    result = f"""Valutazione Rischio Complicanze in Anemia Falciforme
=================================================
Livello di rischio: {risk_level}
Raccomandazione: {recommendation}
Indicazione a idrossiurea: {hydroxyurea_indication}

Fattori di rischio identificati:
{chr(10).join(risk_factors) if risk_factors else "• Nessun fattore di rischio significativo identificato"}

Dati del paziente:
- Emoglobina: {hemoglobin_level} g/dL
- Leucociti: {wbc_count} x10^3/μL
- Genotipo: {genotype.upper()}
- Eventi dolorosi/anno: {pain_events_per_year}
- Storia di sindrome toracica acuta: {'Sì' if history_of_acs else 'No'}
- Dattilite <1 anno: {'Sì' if dactylitis_under_1_year else 'No'}
- Emoglobina fetale: {hemoglobin_f_level if hemoglobin_f_level > 0 else 'Non specificata'}%

Fattori di rischio per complicanze severe:
- Emoglobina basale <7 g/dL
- Leucocitosi >15 x10^3/μL
- Storia di sindrome toracica acuta
- ≥3 eventi dolorosi/anno
- Dattilite <1 anno di età
- Emoglobina fetale <10%
- Genotipo SS o Sβ0

Indicazioni a idrossiurea (NHLBI):
- Bambini ≥9 mesi con genotipo SS o Sβ0 e:
  * ≥3 crisi dolorose moderate-severe nell'ultimo anno
  * Storia di sindrome toracica acuta
  * Altre complicanze severe legate alla vasoocclusione

Fonte: Miller et al., NEJM 2000 e Linee Guida NHLBI 2014
"""
    return [types.TextContent(type="text", text=result)]
def _calculate_pnhs(args):
    """Calcola Pediatric NAFLD Histological Score (PNHS)"""
    bmi_zscore = args.get('bmi_zscore', 0)
    ast_iu_l = args.get('ast_iu_l', 0)
    alt_iu_l = args.get('alt_iu_l', 0)
    insulin_resistance = args.get('insulin_resistance', False)
    apnea_obstructive_sleep = args.get('apnea_obstructive_sleep', False)
    
    # Calcolo punteggio
    score = 0
    criteria = []
    
    if bmi_zscore > 2.0:
        score += 1
        criteria.append(f"• BMI z-score elevato: {bmi_zscore} (>2.0)")
    
    ast_alt_ratio = ast_iu_l / alt_iu_l if alt_iu_l > 0 else 0
    if ast_alt_ratio > 0.8:
        score += 1
        criteria.append(f"• Rapporto AST/ALT elevato: {ast_alt_ratio:.2f} (>0.8)")
    
    if insulin_resistance:
        score += 1
        criteria.append("• Resistenza insulinica presente")
    
    if apnea_obstructive_sleep:
        score += 1
        criteria.append("• Apnea ostruttiva del sonno presente")
    
    # Interpretazione
    if score <= 1:
        interpretation = "BASSA PROBABILITÀ DI NASH"
        recommendation = "Monitoraggio standard, modifiche stile di vita, controllo ogni 6-12 mesi"
    elif score == 2:
        interpretation = "PROBABILITÀ INTERMEDIA DI NASH"
        recommendation = "Monitoraggio più frequente, considerare valutazione specialistica"
    else:
        interpretation = "ALTA PROBABILITÀ DI NASH"
        recommendation = "Valutazione specialistica epatologica, considerare biopsia epatica"
    
    result = f"""Pediatric NAFLD Histological Score (PNHS)
==========================================
Punteggio: {score}/4

Interpretazione: {interpretation}
Raccomandazione: {recommendation}

Criteri presenti:
{chr(10).join(criteria) if criteria else "• Nessun criterio presente"}

Parametri utilizzati:
- BMI z-score: {bmi_zscore}
- AST: {ast_iu_l} IU/L
- ALT: {alt_iu_l} IU/L
- AST/ALT ratio: {ast_alt_ratio:.2f}
- Resistenza insulinica: {'Sì' if insulin_resistance else 'No'}
- Apnea ostruttiva del sonno: {'Sì' if apnea_obstructive_sleep else 'No'}

Interpretazione:
- 0-1: Bassa probabilità di NASH
- 2: Probabilità intermedia di NASH
- 3-4: Alta probabilità di NASH

Note cliniche:
- Score validato per distinguere NASH da semplice steatosi in popolazione pediatrica
- Non sostituisce la biopsia epatica che rimane il gold standard
- Utile per identificare pazienti ad alto rischio da candidare a biopsia
- Sensibilità 74% e specificità 71% per NASH con cutoff ≥2

NAFLD vs NASH:
- NAFLD (steatosi semplice): Accumulo di grasso epatico senza infiammazione significativa
- NASH (steatoepatite): Steatosi con infiammazione e danno epatocellulare
- NASH è associata a maggior rischio di progressione a fibrosi e cirrosi

Fonte: Nobili et al., 2019
"""
    return [types.TextContent(type="text", text=result)]