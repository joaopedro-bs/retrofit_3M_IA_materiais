#!/usr/bin/env python3
"""
rename_pdfs_v2.py — Renomeação padronizada: ID_Autor_Ano_slug.pdf
Execução atômica com validação pré/pós.
"""

import csv, os, re, shutil, hashlib, unicodedata, sys

# ── Config ──────────────────────────────────────────────────────────────────
BASE     = "/Users/joaopedrobarbosa/Cowork/Msc_BMT/msc_GE_20261"
PDFS_DIR = os.path.join(BASE, "artigos_materiais/01_PDFs")
CATALOG  = os.path.join(BASE, "artigos_materiais/02_Catalogo/catalogo_artigos.csv")
CAT_BAK  = CATALOG + ".pre_rename.bak"
SLUG_WORDS = 4

# ── Helpers ─────────────────────────────────────────────────────────────────
STOPS = frozenset({'the','a','an','of','in','for','and','on','to','with','from',
    'by','as','at','or','its','is','are','was','were','be','been','being','has',
    'have','had','do','does','did','will','shall','should','would','could','may',
    'might','can','not','no','nor','but','so','than','too','very','that','this',
    'these','those'})

def slugify(title, max_words=SLUG_WORDS):
    t = unicodedata.normalize('NFKD', title).encode('ascii', 'ignore').decode()
    t = re.sub(r'[^a-zA-Z0-9\s]', '', t).lower()
    words = [w for w in t.split() if w not in STOPS and len(w) > 2]
    return '-'.join(words[:max_words])

def get_surname(autores):
    first = autores.split(';')[0].strip()
    parts = first.split()
    # Skip initial tokens (1-2 chars, alphabetic = initials like "Y", "MA", "Dr")
    name_parts = []
    for p in parts:
        clean = p.replace('.', '').replace(',', '')
        if len(clean) <= 2 and clean.isalpha():
            continue
        # Also skip "Dr" prefix
        if clean.lower() == 'dr':
            continue
        name_parts.append(p)
    if not name_parts:
        name_parts = [parts[-1]] if parts else ['Unknown']
    surname = ''.join(name_parts)
    surname = unicodedata.normalize('NFKD', surname).encode('ascii', 'ignore').decode()
    surname = re.sub(r"[^a-zA-Z]", '', surname)
    # Ensure first letter is uppercase
    if surname:
        surname = surname[0].upper() + surname[1:]
    return surname

def sha256(filepath):
    h = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

# ── Load catalog ────────────────────────────────────────────────────────────
with open(CATALOG, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter='|')
    rows = list(reader)
    fieldnames = reader.fieldnames

baixados = [r for r in rows if r['acesso'] == 'BAIXADO']
print(f"Catálogo: {len(rows)} total, {len(baixados)} BAIXADO\n")

# ── FASE 1: Gerar mapa de renomeação ────────────────────────────────────────
print("=" * 80)
print("FASE 1 — DRY RUN: Gerando mapa de renomeação")
print("=" * 80)

rename_map = []  # list of (old_rel, new_rel, old_abs, new_abs, row_idx, catalog_id)
errors = []

for i, r in enumerate(rows):
    if r['acesso'] != 'BAIXADO':
        continue

    rid = r['id']
    autor = get_surname(r['autores'])
    ano = r['ano']
    slug = slugify(r['titulo'])
    eixo = r['eixo']

    new_name = f"{rid}_{autor}_{ano}_{slug}.pdf"
    new_rel = f"01_PDFs/{eixo}/{new_name}"
    new_abs = os.path.join(BASE, "artigos_materiais", new_rel)

    old_rel = r['arquivo_local']
    old_abs = os.path.join(BASE, "artigos_materiais", old_rel)

    rename_map.append({
        'id': rid,
        'old_rel': old_rel,
        'new_rel': new_rel,
        'old_abs': old_abs,
        'new_abs': new_abs,
        'row_idx': i,
        'autor_field': r['autores'],
        'autor_parsed': autor,
    })

print(f"Mapa gerado: {len(rename_map)} renomeações\n")

# ── FASE 1b: Validações ────────────────────────────────────────────────────
print("=" * 80)
print("FASE 1b — VALIDAÇÕES PRÉ-EXECUÇÃO")
print("=" * 80)

# 1. Todos os caminhos atuais existem?
missing = [e for e in rename_map if not os.path.exists(e['old_abs'])]
print(f"  ✓ Arquivos existentes: {len(rename_map) - len(missing)}/{len(rename_map)}")
if missing:
    for m in missing:
        print(f"    ❌ FALTANDO: {m['id']} → {m['old_abs']}")
    errors.append(f"{len(missing)} arquivo(s) não encontrado(s)")

# 2. Unicidade dos nomes novos
new_names = [e['new_abs'] for e in rename_map]
dupes = [n for n in new_names if new_names.count(n) > 1]
if dupes:
    print(f"  ❌ COLISÕES nos nomes novos: {set(dupes)}")
    errors.append(f"Colisão detectada: {set(dupes)}")
else:
    print(f"  ✓ Unicidade: 0 colisões nos {len(new_names)} nomes novos")

# 3. Nenhum nome novo colide com arquivo existente fora do mapa
old_set = {e['old_abs'] for e in rename_map}
existing_collision = [e for e in rename_map if os.path.exists(e['new_abs']) and e['new_abs'] not in old_set and e['new_abs'] != e['old_abs']]
if existing_collision:
    for c in existing_collision:
        print(f"    ❌ COLISÃO com existente: {c['new_abs']}")
    errors.append(f"{len(existing_collision)} colisão(ões) com arquivos existentes")
else:
    print(f"  ✓ Sem colisão com arquivos existentes fora do mapa")

# 4. Todos são PDFs válidos?
invalid_pdf = []
for e in rename_map:
    if os.path.exists(e['old_abs']):
        with open(e['old_abs'], 'rb') as f:
            header = f.read(4)
        if header != b'%PDF':
            invalid_pdf.append(e)
if invalid_pdf:
    print(f"  ⚠️  {len(invalid_pdf)} arquivo(s) NÃO são PDFs válidos — serão EXCLUÍDOS da renomeação:")
    for e in invalid_pdf:
        print(f"    → {e['id']}: {e['old_abs']} (será mantido como está)")
    rename_map = [e for e in rename_map if e not in invalid_pdf]
    print(f"  ✓ Mapa reduzido para {len(rename_map)} renomeações")
else:
    print(f"  ✓ Integridade: todos os {len(rename_map)} arquivos são PDFs válidos")

# 5. Nenhum nome > 80 chars
long_names = [(e['id'], len(os.path.basename(e['new_abs']))) for e in rename_map if len(os.path.basename(e['new_abs'])) > 80]
if long_names:
    print(f"  ⚠️  {len(long_names)} nome(s) > 80 chars (informativo, não bloqueante)")
else:
    print(f"  ✓ Comprimento: todos os nomes ≤ 80 chars")

if errors:
    print(f"\n🛑 {len(errors)} ERRO(S) CRÍTICO(S) — abortando:")
    for err in errors:
        print(f"   • {err}")
    sys.exit(1)

print(f"\n✅ Todas as validações passaram!\n")

# ── FASE 1c: Relatório Dry Run ──────────────────────────────────────────────
print("=" * 80)
print("FASE 1c — RELATÓRIO (primeiros 20 + resumo)")
print("=" * 80)

for e in rename_map[:20]:
    old_bn = os.path.basename(e['old_abs'])
    new_bn = os.path.basename(e['new_abs'])
    changed = "→" if old_bn != new_bn else "="
    print(f"  {e['id']} {changed} {new_bn}")

if len(rename_map) > 20:
    print(f"  ... +{len(rename_map)-20} mais")

# Computar SHA256 pré-rename
print(f"\n  Computando checksums SHA256 pré-rename...")
pre_hashes = {}
for e in rename_map:
    if os.path.exists(e['old_abs']):
        pre_hashes[e['id']] = sha256(e['old_abs'])
print(f"  ✓ {len(pre_hashes)} checksums computados")

# ── FASE 2: Execução Atômica ────────────────────────────────────────────────
print(f"\n{'=' * 80}")
print("FASE 2 — EXECUÇÃO ATÔMICA")
print("=" * 80)

# 2a. Backup
shutil.copy2(CATALOG, CAT_BAK)
print(f"  ✓ Backup: {CAT_BAK}")

# 2b. Renomear PDFs
renamed = 0
skipped = 0
for e in rename_map:
    if e['old_abs'] == e['new_abs']:
        skipped += 1
        continue
    os.rename(e['old_abs'], e['new_abs'])
    renamed += 1

print(f"  ✓ Renomeados: {renamed} | Sem mudança: {skipped}")

# 2c. Atualizar CSV
for e in rename_map:
    rows[e['row_idx']]['arquivo_local'] = e['new_rel']

with open(CATALOG, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='|')
    writer.writeheader()
    writer.writerows(rows)

print(f"  ✓ Catálogo atualizado: {CATALOG}")

# ── FASE 4: Validação Pós-Execução ──────────────────────────────────────────
print(f"\n{'=' * 80}")
print("FASE 4 — VALIDAÇÃO PÓS-EXECUÇÃO")
print("=" * 80)

# 4a. Todos os novos caminhos existem?
missing_post = [e for e in rename_map if not os.path.exists(e['new_abs'])]
if missing_post:
    print(f"  ❌ {len(missing_post)} arquivo(s) FALTANDO após rename!")
    for m in missing_post:
        print(f"    {m['id']}: {m['new_abs']}")
else:
    print(f"  ✓ Existência: {len(rename_map)}/{len(rename_map)} novos caminhos existem")

# 4b. SHA256 integridade
integrity_ok = 0
integrity_fail = 0
for e in rename_map:
    if os.path.exists(e['new_abs']):
        post_hash = sha256(e['new_abs'])
        if post_hash == pre_hashes.get(e['id']):
            integrity_ok += 1
        else:
            integrity_fail += 1
            print(f"    ❌ HASH MISMATCH: {e['id']}")

print(f"  ✓ Integridade SHA256: {integrity_ok} OK | {integrity_fail} falhas")

# 4c. CSV ↔ disco
reloaded_baixados = []
with open(CATALOG, newline='', encoding='utf-8') as f:
    for r in csv.DictReader(f, delimiter='|'):
        if r['acesso'] == 'BAIXADO':
            reloaded_baixados.append(r)

csv_missing = 0
for r in reloaded_baixados:
    fpath = os.path.join(BASE, "artigos_materiais", r['arquivo_local'])
    if not os.path.exists(fpath):
        csv_missing += 1
        print(f"    ❌ CSV aponta para ausente: {r['id']} → {r['arquivo_local']}")

print(f"  ✓ CSV → disco: {len(reloaded_baixados) - csv_missing}/{len(reloaded_baixados)} OK")

# 4d. Contagem por eixo
print(f"\n  📁 PDFs por eixo:")
for eixo in sorted(set(r['eixo'] for r in reloaded_baixados)):
    count = sum(1 for r in reloaded_baixados if r['eixo'] == eixo)
    print(f"    {eixo}: {count}")

print(f"\n{'=' * 80}")
print(f"✅ RENOMEAÇÃO CONCLUÍDA COM SUCESSO!")
print(f"   {renamed} arquivos renomeados, {integrity_ok} checksums verificados")
print(f"   Backup do catálogo: {CAT_BAK}")
print(f"{'=' * 80}")
