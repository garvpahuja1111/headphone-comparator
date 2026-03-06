# ============================================
# 🎧 India Headphone Comparator
# By: Garv Pahuja (garvpahuja1111)
# Compare best headphones under 1k, 2k, 3k
# ============================================

# --- Headphone Database ---
headphones = [

    # --- Under ₹1,000 ---
    {
        "name": "Zebronics Thunder NEO",
        "price": 899,
        "type": "Over-ear",
        "wireless": True,
        "anc": False,
        "battery_hrs": 30,
        "mic": True,
        "aux_backup": True,
        "driver_mm": 40,
        "bluetooth": "5.3",
        "rating": 4.1,
        "best_for": "Wireless casual listening"
    },
    {
        "name": "boAt BassHeads 900",
        "price": 599,
        "type": "Over-ear",
        "wireless": False,
        "anc": False,
        "battery_hrs": 0,
        "mic": True,
        "aux_backup": True,
        "driver_mm": 40,
        "bluetooth": "Wired",
        "rating": 4.0,
        "best_for": "Best wired under 1k"
    },

    # --- Under ₹2,000 ---
    {
        "name": "pTron Studio Xtreme",
        "price": 1399,
        "type": "Over-ear",
        "wireless": True,
        "anc": False,
        "battery_hrs": 70,
        "mic": True,
        "aux_backup": True,
        "driver_mm": 40,
        "bluetooth": "5.3",
        "rating": 4.2,
        "best_for": "Best battery life under 2k"
    },
    {
        "name": "Boult Q",
        "price": 1599,
        "type": "Over-ear",
        "wireless": True,
        "anc": False,
        "battery_hrs": 70,
        "mic": True,
        "aux_backup": True,
        "driver_mm": 40,
        "bluetooth": "5.3",
        "rating": 4.2,
        "best_for": "Best EQ modes under 2k"
    },
    {
        "name": "Soundcore H30i",
        "price": 1799,
        "type": "On-ear",
        "wireless": True,
        "anc": False,
        "battery_hrs": 70,
        "mic": True,
        "aux_backup": False,
        "driver_mm": 40,
        "bluetooth": "5.3",
        "rating": 4.4,
        "best_for": "Best overall under 2k"
    },

    # --- Under ₹3,000 ---
    {
        "name": "boAt Rockerz 551 ANC Pro",
        "price": 2499,
        "type": "Over-ear",
        "wireless": True,
        "anc": True,
        "battery_hrs": 72,
        "mic": True,
        "aux_backup": True,
        "driver_mm": 40,
        "bluetooth": "5.3",
        "rating": 4.3,
        "best_for": "Best ANC under 3k"
    },
    {
        "name": "Anker Soundcore Life Q20",
        "price": 2999,
        "type": "Over-ear",
        "wireless": True,
        "anc": True,
        "battery_hrs": 40,
        "mic": True,
        "aux_backup": True,
        "driver_mm": 40,
        "bluetooth": "5.0",
        "rating": 4.5,
        "best_for": "Best sound quality under 3k"
    },
]


# --- Helper: Print a single headphone ---
def print_headphone(h):
    print(f"""
  🎧 {h['name']}
  ├─ 💰 Price       : ₹{h['price']}
  ├─ 📦 Type        : {h['type']}
  ├─ 📶 Wireless    : {'Yes ✅' if h['wireless'] else 'No (Wired)'}
  ├─ 🔇 ANC         : {'Yes ✅' if h['anc'] else 'No'}
  ├─ 🔋 Battery     : {str(h['battery_hrs']) + ' hrs' if h['battery_hrs'] > 0 else 'N/A (Wired)'}
  ├─ 🎙️  Mic         : {'Yes ✅' if h['mic'] else 'No'}
  ├─ 🔌 AUX Backup  : {'Yes ✅' if h['aux_backup'] else 'No'}
  ├─ 🎵 Driver      : {h['driver_mm']}mm
  ├─ ⭐ Rating      : {h['rating']}/5
  └─ 🏆 Best For    : {h['best_for']}
""")


# --- Feature 1: Browse by budget ---
def browse_by_budget():
    print("\n💰 SELECT YOUR BUDGET:")
    print("  1. Under ₹1,000")
    print("  2. Under ₹2,000")
    print("  3. Under ₹3,000")

    choice = input("\nEnter choice (1/2/3): ").strip()

    budget_map = {"1": 1000, "2": 2000, "3": 3000}

    if choice not in budget_map:
        print("❌ Invalid choice!")
        return

    budget = budget_map[choice]
    results = [h for h in headphones if h["price"] <= budget]

    if not results:
        print("❌ No headphones found in this range.")
        return

    print(f"\n🎧 Headphones under ₹{budget}:\n")
    print("=" * 50)
    for h in results:
        print_headphone(h)


# --- Feature 2: Filter by feature ---
def filter_by_feature():
    print("\n🔍 FILTER BY FEATURE:")
    print("  1. Only ANC headphones")
    print("  2. Only Wireless headphones")
    print("  3. Only Wired headphones")
    print("  4. Only headphones with AUX backup")
    print("  5. Best battery life (50+ hrs)")

    choice = input("\nEnter choice (1-5): ").strip()

    filters = {
        "1": ("ANC", lambda h: h["anc"]),
        "2": ("Wireless", lambda h: h["wireless"]),
        "3": ("Wired", lambda h: not h["wireless"]),
        "4": ("AUX Backup", lambda h: h["aux_backup"]),
        "5": ("50+ hrs battery", lambda h: h["battery_hrs"] >= 50),
    }

    if choice not in filters:
        print("❌ Invalid choice!")
        return

    label, condition = filters[choice]
    results = [h for h in headphones if condition(h)]

    if not results:
        print(f"❌ No headphones found with {label}.")
        return

    print(f"\n✅ Headphones with {label}:\n")
    print("=" * 50)
    for h in results:
        print_headphone(h)


# --- Feature 3: Compare two headphones ---
def compare_two():
    print("\n📋 AVAILABLE HEADPHONES:")
    for i, h in enumerate(headphones, 1):
        print(f"  {i}. {h['name']} — ₹{h['price']}")

    try:
        a = int(input("\nEnter first headphone number: ")) - 1
        b = int(input("Enter second headphone number: ")) - 1

        if a < 0 or b < 0 or a >= len(headphones) or b >= len(headphones):
            print("❌ Invalid selection!")
            return

        h1 = headphones[a]
        h2 = headphones[b]

        print(f"""
╔══════════════════════════════════════════════════════════════╗
║              🎧 HEADPHONE COMPARISON                        ║
╠══════════════════════╦═══════════════════════════════════════╣
║ Feature              ║ {h1['name'][:20]:<20} vs {h2['name'][:20]:<20} ║
╠══════════════════════╬═══════════════════════════════════════╣
║ 💰 Price             ║ ₹{h1['price']:<19} vs ₹{h2['price']:<19} ║
║ 📦 Type              ║ {h1['type']:<20} vs {h2['type']:<20} ║
║ 📶 Wireless          ║ {'Yes':<20} vs {'Yes' if h2['wireless'] else 'No':<20} ║
║ 🔇 ANC               ║ {'Yes' if h1['anc'] else 'No':<20} vs {'Yes' if h2['anc'] else 'No':<20} ║
║ 🔋 Battery           ║ {str(h1['battery_hrs'])+'hrs':<20} vs {str(h2['battery_hrs'])+'hrs':<20} ║
║ 🔌 AUX Backup        ║ {'Yes' if h1['aux_backup'] else 'No':<20} vs {'Yes' if h2['aux_backup'] else 'No':<20} ║
║ ⭐ Rating            ║ {str(h1['rating'])+'/ 5':<20} vs {str(h2['rating'])+'/ 5':<20} ║
╚══════════════════════╩═══════════════════════════════════════╝
""")

        # Simple winner suggestion
        score1 = h1["rating"] - (h1["price"] / 10000)
        score2 = h2["rating"] - (h2["price"] / 10000)

        winner = h1 if score1 >= score2 else h2
        print(f"  🏆 Recommended: {winner['name']} — {winner['best_for']}\n")

    except ValueError:
        print("❌ Please enter valid numbers!")


# --- Feature 4: Best picks ---
def best_picks():
    print("""
🏆 BEST PICKS — INDIA 2026
══════════════════════════════════════════

  Under ₹1,000:
  🥇 Wireless  → Zebronics Thunder NEO (₹899)
  🥇 Wired     → boAt BassHeads 900 (₹599)

  Under ₹2,000:
  🥇 Overall   → Soundcore H30i (₹1,799)
  🥇 Battery   → pTron Studio Xtreme (₹1,399)

  Under ₹3,000:
  🥇 ANC       → boAt Rockerz 551 ANC Pro (₹2,499)
  🥇 Sound     → Anker Soundcore Life Q20 (₹2,999)

══════════════════════════════════════════
""")


# --- Main Menu ---
def main():
    print("""
╔══════════════════════════════════════════╗
║   🎧 INDIA HEADPHONE COMPARATOR 2026    ║
║      by Garv Pahuja (garvpahuja1111)     ║
╚══════════════════════════════════════════╝
""")

    while True:
        print("📋 MAIN MENU:")
        print("  1. Browse by budget (1k / 2k / 3k)")
        print("  2. Filter by feature")
        print("  3. Compare two headphones")
        print("  4. See best picks")
        print("  5. Exit")

        choice = input("\nEnter choice (1-5): ").strip()

        if choice == "1":
            browse_by_budget()
        elif choice == "2":
            filter_by_feature()
        elif choice == "3":
            compare_two()
        elif choice == "4":
            best_picks()
        elif choice == "5":
            print("\n👋 Happy listening, Garv! 🎵\n")
            break
        else:
            print("❌ Invalid choice! Try again.")

        input("\nPress Enter to continue...")


# --- Run ---
if __name__ == "__main__":
    main()
