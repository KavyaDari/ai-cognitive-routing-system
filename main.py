from app.phase1_router import route_post_to_bots, bots
from app.phase2_langgraph import decide_search, search, draft
from app.phase3_rag import generate_defense_reply

def run_all():

    print("\n=== PHASE 1 ===")
    post = "AI will replace developers and impact jobs"
    matched = route_post_to_bots(post)
    print("Matched Bots:", matched)

    print("\n=== PHASE 2 ===")

    phase2_outputs = {}   

    for bot_id in matched:
        print(f"\n--- Bot {bot_id} ---")

        state = {
            "persona": bots[bot_id],
            "bot_id": bot_id
        }

        state = decide_search(state)
        state = search(state)
        state = draft(state)

        print(state["final"])

        
        phase2_outputs[bot_id] = state["final"]["post_content"]

    print("\n=== PHASE 3 ===")

    for bot_id in matched:
        print(f"\n--- Defense by Bot {bot_id} ---")

        parent_post = phase2_outputs[bot_id]   

        reply = generate_defense_reply(
            bots[bot_id],
            parent_post,
            "Bot: initial argument...",
            "I disagree with you. This sounds unrealistic."
        )

        print(reply)


if __name__ == "__main__":
    run_all()