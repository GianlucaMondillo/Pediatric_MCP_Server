#!/usr/bin/env python3
import asyncio
import sys
from mcp.server import Server
from mcp.server.stdio import stdio_server
import mcp.types as types

# Import dei moduli tools
from tools.scores import get_score_tools, handle_score_tools
from tools.calculations import get_calculation_tools, handle_calculation_tools
from tools.assessments import get_assessment_tools, handle_assessment_tools

# Fix per Windows
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

app = Server("NOME_SERVER")

@app.list_tools()
async def list_tools() -> list[types.Tool]:
    """Combina tutti i tool dai moduli"""
    tools = []
    tools.extend(get_score_tools())        # PEWS, PAS, etc
    tools.extend(get_calculation_tools())  # BSA, fluidi
    tools.extend(get_assessment_tools())   # Altri assessment
    return tools

@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[types.TextContent]:
    """Routing delle chiamate ai moduli appropriati"""
    
    # Score medici
    if name in ['calculate_pews', 'calculate_pas', 'calculate_apgar', 'calculate_gcs_pediatric', 'calculate_mchat',
               'calculate_pediatric_trauma_score', 'calculate_catch_score', 'calculate_westley_croup_score',
               'calculate_centor_score_pediatric', 'calculate_wells_score_pediatric',
               'calculate_pas_asthma', 'calculate_pass_asthma', 'calculate_bacterial_meningitis_score',
               'calculate_kocher_criteria', 'calculate_kawasaki_criteria', 'calculate_jones_criteria',
               'calculate_bops', 'calculate_lansky_score', 'calculate_sickle_cell_complication_risk',
               'calculate_pnhs']:
        return handle_score_tools(name, arguments)
    
    # Calcoli medici
    elif name in ['calculate_bsa', 'calculate_maintenance_fluids', 'calculate_creatinine_clearance', 
                 'calculate_bmi_pediatric', 'calculate_daily_calories', 'calculate_normal_blood_pressure',
                 'calculate_predicted_height', 'calculate_burned_surface_area', 'calculate_anc',
                 'calculate_pnfs', 'calculate_pediatric_bone_health']:
        return handle_calculation_tools(name, arguments)
    
    # Assessment clinici
    elif name in ['assess_dehydration', 'assess_pain_scale', 'assess_nutritional_status', 
                 'assess_developmental_milestones', 'assess_asthma_control',
                 'assess_heads_ed', 'assess_pediatric_sleep',
                 'assess_rome4_abdominal_migraine', 'assess_rome4_aerophagia', 'assess_rome4_constipation',
                 'assess_rome4_cyclic_vomiting', 'assess_rome4_functional_abdominal_pain',
                 'assess_rome4_functional_dyspepsia', 'assess_rome4_functional_nausea_vomiting',
                 'assess_rome4_ibs', 'assess_rome4_nonretentive_fecal_incontinence',
                 'assess_rome4_rumination_syndrome', 'assess_brue_criteria']:
        return handle_assessment_tools(name, arguments)
    
    else:
        raise ValueError(f"Strumento sconosciuto: {name}")

async def main():
    """Main entry point per il server"""
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream, 
            write_stream,
            app.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())