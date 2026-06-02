#!/usr/bin/env python3
"""
Script: indexar_e_mover.py
Objetivo: Mapear arquivos baixados em BAIXADOS_PAYWALL para entradas do catálogo,
          mover PDFs para as pastas de eixo corretas com nomes padronizados,
          e atualizar o catalogo_artigos.csv com status BAIXADO.
"""

import os, shutil, csv, re

# ── Caminhos ────────────────────────────────────────────────────────────────
BASE        = "/Users/joaopedrobarbosa/Cowork/Msc_BMT/msc_GE_20261"
SRC_DIR     = os.path.join(BASE, "BAIXADOS_PAYWALL")
PDFS_DIR    = os.path.join(BASE, "artigos_materiais/01_PDFs")
CATALOG     = os.path.join(BASE, "artigos_materiais/02_Catalogo/catalogo_artigos.csv")
CATALOG_BAK = CATALOG + ".bak"

# ── Mapeamento: nome-do-arquivo-original → (id_catalogo, nome_destino, eixo) ─
MAPPING = {
    # Emerald
    "jkm-04-2018-0228.pdf":
        ("S1A01","Chen_2019_km-functions-corporate-university-evolution.pdf","eixo1_corporate_university"),
    "k-03-2021-0218.pdf":
        ("S1A02","Chen_2022_influencing-factors-knowledge-enhancement-corporate-universities.pdf","eixo1_corporate_university"),
    "vjikms-12-2016-0074.pdf":
        ("S1A03","Scarso_2017_corporate-universities-knowledge-management-tools.pdf","eixo1_corporate_university"),
    "tlo-10-2023-0193en.pdf":
        ("S1A05","Mora-Mora_2025_corporate-university-model-emerging-economies.pdf","eixo1_corporate_university"),
    "jic-12-2022-0238.pdf":
        ("S1A09","Chen_2023_knowledge-network-intellectual-capital-corporate-university.pdf","eixo1_corporate_university"),
    "tlo-01-2021-0011.pdf":
        ("S2A01","Lissillour_2022_ambidexterity-learning-organization-corporate-university.pdf","eixo1_corporate_university"),
    "jkm-10-2024-1198en.pdf":
        ("S3A02","Zhang_2025_impact-genai-enterprise-innovation-km-perspective.pdf","eixo2_ia_generativa_gc"),
    "jkm-09-2025-1398en.pdf":
        ("S3A03","Brusco-Pletsch_2026_digital-transformation-genai-km-systems.pdf","eixo2_ia_generativa_gc"),
    "jkm-01-2025-0102en.pdf":
        ("S3A04","Rai_2026_generative-ai-management-education-km.pdf","eixo2_ia_generativa_gc"),
    "jkm-03-2025-0418en.pdf":
        ("S3A05","He_2025_genai-km-manufacturing-five-stage-framework.pdf","eixo2_ia_generativa_gc"),
    "md-09-2025-2615en.pdf":
        ("S7A10","Romeo_2026_navigating-ai-frontier-holistic-framework.pdf","eixo4_governanca_ia"),
    "shr-01-2025-0008en.pdf":
        ("S8A02","Asiedu_2025_future-proofing-workforce-upskilling-reskilling.pdf","eixo5_reconfiguracao_trabalho"),
    "ijilt-02-2020-0022.pdf":
        ("S6A08","Wilkens_2020_ai-workplace-double-edged-sword.pdf","eixo3_learning_flow_work"),

    # IEEE / outros publishers com nome longo
    "Popular_LLM-Large_Language_Models_in_Enterprise_Applications.pdf":
        ("S4A06","Pasupuleti_2024_popular-llm-enterprise-applications.pdf","eixo2_ia_generativa_gc"),
    "Popular_LLM-Large_Language_Models_in_Enterprise_Applications-2.pdf":
        None,  # duplicata — descartar
    "Large_Language_Models_and_Applications_The_Rebirth_of_Enterprise_Knowledge_Management_and_the_Rise_of_Prompt_Libraries.pdf":
        ("S4A10","OLeary_2024_llm-prompt-libraries-rebirth-enterprise-km.pdf","eixo2_ia_generativa_gc"),
    "Intelligent Sys in Account - 2023 - O%27Leary - Enterprise large language models  Knowledge characteristics  risks  and.pdf":
        ("S4A01","OLeary_2023_enterprise-llm-knowledge-risks-activities.pdf","eixo2_ia_generativa_gc"),
    "Transmuting_Information_to_Knowledge_with_an_Enterprise_Knowledge_Graph.pdf":
        ("S9A05","Aasman_2017_transmuting-information-knowledge-enterprise-kg.pdf","eixo6_knowledge_graphs_rag"),
    "Integrating_Retrieval-Augmented_Generation_RAG_and_Knowledge_Augmented_Generation_KAG_Frameworks_to_Build_Accurate_Enterprise_Question_Answering_Systems.pdf":
        ("S10A01","Guo_2025_integrating-rag-kag-enterprise-qa.pdf","eixo6_knowledge_graphs_rag"),
    "Secure_Retrieval-Augmented_Generation_Framework_for_Automated_Knowledge_Access_in_Enterprise_Git_Repositories.pdf":
        ("S10A06","Shaikh_2026_secure-rag-framework-enterprise-git.pdf","eixo6_knowledge_graphs_rag"),
    "Survey_and_Benchmarking_of_Retrieval_Methods_for_Enterprise_Retrieval-Augmented_Generation.pdf":
        ("S10A03","Ruparel_2025_survey-benchmarking-retrieval-enterprise-rag.pdf","eixo6_knowledge_graphs_rag"),
    "A_Comparative_Analysis_of_Retrieval-Augmented_Generation_Architectures_with_Semantic_Hashing_for_Enterprise_Knowledge_Systems.pdf":
        ("S10A04","Altinok_2026_comparative-rag-architectures-semantic-hashing.pdf","eixo6_knowledge_graphs_rag"),

    # Springer
    "s11192-019-03328-0.pdf":
        ("S2A04","Singh_2019_mapping-themes-corporate-university-scientometrics.pdf","eixo1_corporate_university"),

    # MDPI (OA)
    "applsci-16-00368-v2.pdf":
        ("S4A05","Karakurt_2025_rag-llm-enterprise-km-slr.pdf","eixo2_ia_generativa_gc"),

    # EDUPIJ
    "files_1_articles_article_981_EDUPIJ_981_article_693c93b5ca21d.pdf":
        ("S6A03","Yabanova_2025_ai-workplace-education-systematic-review.pdf","eixo3_learning_flow_work"),

    # Elsevier (por número S2.0)
    "1-s2.0-S266665962500023X-main.pdf":
        ("S7A09","Liao_2025_navigating-ai-digital-governance-5w1h.pdf","eixo4_governanca_ia"),
    "1-s2.0-S0160791X23001987-main.pdf":
        ("S8A09","Leon_2023_employees-reskilling-upskilling-industry5.pdf","eixo5_reconfiguracao_trabalho"),
    "1-s2.0-S0268401225001343-main.pdf":
        ("S8A07","Yang_2026_deskilling-reskilling-upskilling-genai-students.pdf","eixo5_reconfiguracao_trabalho"),
    "1-s2.0-S095070512401044X-main.pdf":
        ("S10A05","Siddharth_2024_rag-engineering-design-knowledge.pdf","eixo6_knowledge_graphs_rag"),

    # TechRxiv
    "37932.pdf":
        ("S6A10","Joskowicz_2023_engineers-perspectives-genai-workplace.pdf","eixo3_learning_flow_work"),

    # Wiley
    "Job Performance in the Learning Organization: The Mediating Impacts of Self\u2010Efficacy and Work Engagement.pdf":
        ("S5A07","Song_2018_job-performance-learning-organization-mediating.pdf","eixo3_learning_flow_work"),

    # SSRN
    "ssrn-6002294.pdf":
        ("S7A01","Zentner_2026_ai-workforce-coverage-maturity-framework.pdf","eixo4_governanca_ia"),
    "ssrn-4817726.pdf":
        ("S7A02","Ligot_2024_ai-governance-framework-responsible-development.pdf","eixo4_governanca_ia"),
    "ssrn-6639519.pdf":
        ("S7A03","Kiran_2026_responsible-ai-governance-framework-enterprises.pdf","eixo4_governanca_ia"),
    "ssrn-6466703.pdf":
        ("S7A04","AlFawareh_2026_human-centric-ai-governance-digital-hrm.pdf","eixo4_governanca_ia"),
    "ssrn-5372870.pdf":
        ("S7A05","Sprongl_2025_ai-integration-framework-responsible-adoption.pdf","eixo4_governanca_ia"),
    "ssrn-6672905.pdf":
        ("S7A07","Shaikh_2026_bounded-design-donut-model-ai-governance.pdf","eixo4_governanca_ia"),
    "ssrn-4924672.pdf":
        ("S9A08","Li_2024_hierarchical-matching-kg-retrieval-rag.pdf","eixo6_knowledge_graphs_rag"),
    "ssrn-5198936.pdf":
        ("S9A10","Kumarasinghe_2025_automated-ds-kg-construction-rag-pipeline.pdf","eixo6_knowledge_graphs_rag"),

    # preprints.org
    "preprints202504.1707.v1.pdf":
        ("S7A06","Joshi_2025_ai-governance-design-agentic-systems.pdf","eixo4_governanca_ia"),
}

# IDs que NÃO foram baixados (permaneceram inacessíveis) → remover do catálogo
# (todos os que ainda são PAYWALL/OA_INACESSÍVEL não presentes no mapping)
SUCCESSFULLY_DOWNLOADED_IDS = {v[0] for v in MAPPING.values() if v is not None}

# Adicionar os que foram baixados automaticamente antes desta sessão
AUTO_DOWNLOADED = {
    "S3A01": ("Pimentel_2024_genai-solutions-km-literature-review-roadmap.pdf", "eixo2_ia_generativa_gc"),
    "S9A01": ("Duan_2020_cold-start-enterprise-knowledge-graph.pdf", "eixo6_knowledge_graphs_rag"),
    "S9A06": ("Galkin_2017_enterprise-kg-semantic-approach.pdf", "eixo6_knowledge_graphs_rag"),
    "S9A07": ("Pires_2024_enhancing-llms-kg-literature-retrieval.pdf", "eixo6_knowledge_graphs_rag"),
}
SUCCESSFULLY_DOWNLOADED_IDS.update(AUTO_DOWNLOADED.keys())

# ── Ler catálogo ────────────────────────────────────────────────────────────
with open(CATALOG, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter='|')
    rows = list(reader)
    fieldnames = reader.fieldnames

print(f"Catálogo lido: {len(rows)} linhas\n")

# ── Backup ──────────────────────────────────────────────────────────────────
shutil.copy2(CATALOG, CATALOG_BAK)
print(f"Backup salvo em: {CATALOG_BAK}\n")

# ── FASE 1: Mover PDFs ──────────────────────────────────────────────────────
moved = []
discarded = []
not_found = []

print("=" * 60)
print("FASE 1: MOVENDO PDFs")
print("=" * 60)

for src_name, mapping in MAPPING.items():
    src_path = os.path.join(SRC_DIR, src_name)
    if not os.path.exists(src_path):
        not_found.append(src_name)
        print(f"  ⚠️  NÃO ENCONTRADO: {src_name}")
        continue

    if mapping is None:
        discarded.append(src_name)
        os.remove(src_path)
        print(f"  🗑️  DESCARTADO (duplicata): {src_name}")
        continue

    catalog_id, dest_name, eixo = mapping
    dest_dir  = os.path.join(PDFS_DIR, eixo)
    dest_path = os.path.join(dest_dir, dest_name)
    os.makedirs(dest_dir, exist_ok=True)
    shutil.move(src_path, dest_path)
    moved.append((catalog_id, dest_name, eixo))
    print(f"  ✅ {catalog_id} → {eixo}/{dest_name}")

print(f"\nMovidos: {len(moved)} | Descartados: {len(discarded)} | Não encontrados: {len(not_found)}\n")

# ── FASE 2: Atualizar catálogo ───────────────────────────────────────────────
print("=" * 60)
print("FASE 2: ATUALIZANDO CATÁLOGO")
print("=" * 60)

# Build lookup de catalog_id → (dest_name, eixo)
id_to_file = {v[0]: (v[1], v[2]) for v in MAPPING.values() if v is not None}
id_to_file.update({k: v for k, v in AUTO_DOWNLOADED.items()})

# IDs que devem ser REMOVIDOS (ainda PAYWALL/OA_INACESSÍVEL)
ids_to_remove = set()
updated_rows = []
removed_rows = []

for row in rows:
    rid = row['id']
    status = row['acesso']

    # Se já estava BAIXADO, DUPLICATA, etc. — manter
    if status not in ('PAYWALL', 'OA_INACESSÍVEL'):
        updated_rows.append(row)
        continue

    # Se está na lista de baixados → atualizar para BAIXADO
    if rid in id_to_file:
        dest_name, eixo = id_to_file[rid]
        row['acesso'] = 'BAIXADO'
        row['arquivo_local'] = f"01_PDFs/{eixo}/{dest_name}"
        updated_rows.append(row)
        print(f"  ✅ {rid} → BAIXADO | {row['arquivo_local']}")
    else:
        # Não foi baixado → remover do catálogo
        removed_rows.append(row)
        print(f"  ❌ {rid} → REMOVIDO (não baixado) | {row['titulo'][:60]}")

print(f"\nAtualizados: {len(id_to_file)} | Removidos: {len(removed_rows)}\n")

# ── FASE 3: Salvar catálogo atualizado ──────────────────────────────────────
with open(CATALOG, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='|')
    writer.writeheader()
    writer.writerows(updated_rows)

print(f"✅ Catálogo salvo: {len(updated_rows)} linhas restantes")
print(f"   Removidas: {len(removed_rows)} entradas inacessíveis\n")

# ── FASE 4: Relatório Final ──────────────────────────────────────────────────
print("=" * 60)
print("RELATÓRIO FINAL")
print("=" * 60)

status_counts = {}
for row in updated_rows:
    s = row['acesso']
    status_counts[s] = status_counts.get(s, 0) + 1

for status, count in sorted(status_counts.items()):
    print(f"  {status}: {count}")

print(f"\nIDs removidos do catálogo:")
for row in removed_rows:
    print(f"  - {row['id']} | {row['titulo'][:70]}")

print("\n✅ CONCLUÍDO!")
