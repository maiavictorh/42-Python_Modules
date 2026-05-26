def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda artifacts:
                  artifacts['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mages: mages['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda mages: mages['power'])
    min_power = min(mages, key=lambda mages: mages['power'])

    total_power = 0
    for m in mages:
        total_power += m['power']

    avg_power = total_power / len(mages)

    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power
        }


if __name__ == '__main__':
    GREEN = "\33[32m"
    NC = "\33[0m"
    artifacts = [{'name': 'Wind Cloak', 'power': 97, 'type': 'armor'},
                 {'name': 'Shadow Blade', 'power': 78, 'type': 'accessory'},
                 {'name': 'Wind Cloak', 'power': 63, 'type': 'weapon'},
                 {'name': 'Water Chalice', 'power': 95, 'type': 'accessory'}]

    mages = [{'name': 'Ember', 'power': 85, 'element': 'shadow'},
             {'name': 'Alex', 'power': 53, 'element': 'wind'},
             {'name': 'Kai', 'power': 90, 'element': 'fire'},
             {'name': 'Zara', 'power': 50, 'element': 'water'},
             {'name': 'Zara', 'power': 82, 'element': 'wind'}]

    spells = ['heal', 'shield', 'fireball', 'blizzard']

    sorted_artifacts = artifact_sorter(artifacts)
    print(f"\n{GREEN}Testing artifact sorter...{NC}")
    i = 1
    for art in sorted_artifacts:
        print(f"{i}. {art['name']} ({art['power']} power) type: {art['type']}")
        i += 1

    filtered_mages = power_filter(mages, 82)
    print(f"\n{GREEN}Testing mage filter (min: 82)...{NC}")
    i = 1
    for mage in filtered_mages:
        print(f"{i}. {mage['name']} ({mage['power']} power)"
              f" element: {mage['element']}")
        i += 1

    transformed_spells = spell_transformer(spells)
    print(f"\n{GREEN}Testing spell transformer...{NC}")
    for spell in transformed_spells:
        print(spell, end=" ")
    print()

    stats = mage_stats(mages)
    print(f"\n{GREEN}Testing Mage statistics...{NC}")
    print(f"Max power: {stats['max_power']}\n"
          f"Min power: {stats['min_power']}\n"
          f"Average power: {stats['avg_power']}")
