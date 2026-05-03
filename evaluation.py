import pandas as pd

def evaluate(qa_chain, questions):
    results = []

    for q in questions:
        res = qa_chain.invoke({"query": q})

        results.append({
            "question": q,
            "answer": res["result"]
        })

    df = pd.DataFrame(results)
    df.to_csv("outputs/eval_scored.csv", index=False)