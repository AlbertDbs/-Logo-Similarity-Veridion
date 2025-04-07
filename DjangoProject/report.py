import csv

def generate_report(groups):
    for i, group in enumerate(groups, 1):
        print(f"\n Group {i} ({len(group)} websites):")
        for site in group:
            print(f"   - {site}")
    print(f"\nTotal groups found {len(groups)}")

    with open("groups_logo.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Group", "Website"])
        for i, group in enumerate(groups, 1):
            for site in group:
                writer.writerow([i, site])

    print("\nThe groups have been saved in the 'groups_logo.csv'.")