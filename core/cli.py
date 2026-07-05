def display_header():
    print("=" * 60)
    print("      Multimodal AI Evaluation Framework (MAEF)")
    print("=" * 60)
    print()


def display_menu():
    """Display the available evaluation tasks."""

    print("Select an Evaluation Task:\n")
    print("1. Generic Image")
    print("2. Infographic")
    print("3. Product Advertisement")
    print("4. Prompt Iteration")
    print("5. Style Transfer")
    print("6. Image Editing")
    print("0. Exit")


def get_user_choice():
    """Ask the user to choose an evaluation task."""

    choice = input("\nEnter your choice: ")
    return choice


def collect_evaluation_inputs():
    """Collect evaluation details from the user."""

    print("\nPlease enter the evaluation details.\n")

    original_prompt = input("Original prompt: ")
    image_a_description = input("Image A description: ")
    image_b_description = input("Image B description: ")

    return {
        "original_prompt": original_prompt,
        "image_a_description": image_a_description,
        "image_b_description": image_b_description,
    }