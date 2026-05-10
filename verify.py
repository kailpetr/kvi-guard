from runtime.verifier import verify_response


def main():
    print("KVI Guard Core v1")
    print("Lightweight LLM stability verification")

    while True:

        text = input("\nEnter response to verify (or type 'exit'): ")

        if text.lower() == "exit":
            break

        result = verify_response(text)

        print("\n--- Verification Result ---")

        for key, value in result.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    main()
