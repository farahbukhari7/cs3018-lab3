from logic import Symbol, Not, And, Or, Implication, KB, check_all

# ── Symbols ───────────────────────────────────────────────
sara_key    = Symbol("SaraHasKey")
lina_key    = Symbol("LinaHasKey")
lina_seen   = Symbol("LinaSeenNearRoom")
lina_guilty = Symbol("LinaIsGuilty")

all_symbols = ["SaraHasKey", "LinaHasKey", "LinaSeenNearRoom", "LinaIsGuilty"]

# ── Knowledge Base ────────────────────────────────────────
kb = KB()

# Clue 1: IF lina_key THEN lina_guilty
kb.tell(Implication(lina_key, lina_guilty))

# Clue 2: NOT sara_key
kb.tell(Not(sara_key))

# Clue 3: lina_seen is TRUE
#kb.tell(lina_seen)

# Clue 4: IF lina_seen THEN lina_key
kb.tell(Implication(lina_seen, lina_key))

# ── Original Queries ──────────────────────────────────────
print("=" * 50)
print("  CS3081 Lab 3 - Knowledge Base Detective")
print("=" * 50)

print("\nQuery: Is Lina guilty?")
answer = check_all(kb, lina_guilty, all_symbols)
if answer:
    print("YES -- The KB ENTAILS that Lina is guilty.")
else:
    print("NO -- The KB does NOT entail that Lina is guilty.")

print("\nQuery: Does Sara have a key?")
answer2 = check_all(kb, sara_key, all_symbols)
if answer2:
    print("YES -- The KB ENTAILS Sara has a key.")
else:
    print("NO -- The KB does NOT entail Sara has a key.")

# ── Exercise 3: Add Nora ──────────────────────────────────
nora_key = Symbol("NoraHasKey")
all_symbols.append("NoraHasKey")
kb.tell(nora_key)

nora_guilty = Symbol("NoraIsGuilty")
answer3 = check_all(kb, nora_guilty, all_symbols)

print("\nQuery: Is Nora guilty?")
if answer3:
    print("YES -- The KB ENTAILS that Nora is guilty.")
else:
    print("NO -- The KB does NOT entail Nora is guilty.")