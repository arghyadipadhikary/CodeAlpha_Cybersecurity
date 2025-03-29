import sys

def phishing_awareness():
    print("\n=== Phishing Awareness Training ===")
    print("This module will guide you through the risks of phishing and how to protect yourself using the CIA Triad (Confidentiality, Integrity, and Availability).\n")
    
    lessons = [
        ("Introduction to Phishing", "Phishing is a cyber threat where attackers impersonate trusted entities to steal sensitive information. It threatens the Confidentiality of your data."),
        ("Types of Phishing Attacks", "1. Email Phishing - Fraudulent emails pretending to be from legitimate sources.\n2. Spear Phishing - Targeted phishing attacks on individuals.\n3. Smishing - Phishing via SMS.\n4. Vishing - Phishing via voice calls.\n5. Website Spoofing - Fake websites mimicking real ones to steal credentials.\nPhishing attacks can compromise the Integrity of data by manipulating users into entering false information."),
        ("How to Identify Phishing Attempts", "Look out for: \n- Urgent requests and threats.\n- Grammar mistakes and odd formatting.\n- Suspicious links and attachments.\n- Unusual sender email addresses.\nPhishing attacks can disrupt Availability by locking users out of accounts.")
    ]
    
    for index, (title, content) in enumerate(lessons, 1):
        print("\n===", title, "===")
        print(content)
        if input("Press Enter to continue or type 'exit' to quit: ").strip().lower() == 'exit':
            sys.exit("Training exited. Stay safe!")
    
    print("\n=== Best Practices to Stay Secure ===")
    best_practices = [
        "Never share personal information via email.",
        "Verify links before clicking—hover over them to see the actual URL.",
        "Enable Multi-Factor Authentication (MFA) for added security.",
        "Use email filtering tools and report suspicious messages.",
        "Keep your software and security patches updated."
    ]
    for practice in best_practices:
        print(f"- {practice}")
    if input("\nPress Enter to proceed to the quiz or type 'exit' to quit: ").strip().lower() == 'exit':
        sys.exit("Training exited. Stay safe!")
    
    while True:
        print("\n=== Quiz Time! Answer True or False. ===")
        quiz_questions = {
            "Phishing emails often create a sense of urgency to trick users.": True,
            "Clicking on links in an email is the best way to verify legitimacy.": False,
            "Multi-Factor Authentication (MFA) enhances security against phishing.": True,
            "A legitimate bank will ask for your password via email.": False,
            "Phishing can impact the Availability of your accounts by locking you out.": True
        }
        
        score = 0
        for question, correct_answer in quiz_questions.items():
            while True:
                answer = input(f"{question} (True/False): ").strip().lower()
                if answer in ["true", "false"]:
                    answer = answer == "true"
                    if answer == correct_answer:
                        print("✔ Correct!")
                        score += 1
                    else:
                        print("✘ Incorrect! Be cautious of phishing attempts.")
                    break
                else:
                    print("Invalid input. Please enter 'True' or 'False'.")
        
        print(f"\n=== Training Complete! Your Score: {score}/{len(quiz_questions)} ===")
        if score < len(quiz_questions):
            retry = input("Would you like to retake the quiz? (yes/no): ").strip().lower()
            if retry == "yes":
                continue
        break
    
    print("Remember: Stay alert, verify sources, and report phishing attempts immediately!")

if __name__ == "__main__":
    phishing_awareness()
