from rapidfuzz import process, fuzz
from names import NAMES

def find_matches(input_name, limit=5):
    results = process.extract(
        input_name,
        NAMES,
        scorer=fuzz.ratio,
        limit=limit
    )
    return results

if __name__ == "__main__":
    name = input("Enter a name: ")
    matches = find_matches(name)

    print("\nBest Match:")
    print(f"{matches[0][0]} - Score: {matches[0][1]}")

    print("\nOther Matches:")
    for match, score, _ in matches[1:]:
        print(f"{match} - Score: {score}")
