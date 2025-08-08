from modules.ai_strategy import load_data, train_ai

if __name__ == "__main__":
    X, y = load_data()
    if not X:
        print("No data to train on, bro.")
    else:
        train_ai(X, y)
        print("AI model retrained on all spicy data!")