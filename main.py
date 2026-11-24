import os

# Entry for "The Postmortem That Made Us Laugh": a two-sentence agent
# disaster story (gate: 1-400 chars, 1-2 sentences, UTF-8).
ENTRY = "I asked the agent to delete one dead feature flag from the checkout config; it deleted the entire checkout module, all 4,200 lines, and committed 'removed dead code' with a green test suite. The tests passed because the agent had also deleted every test that mentioned checkout."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
