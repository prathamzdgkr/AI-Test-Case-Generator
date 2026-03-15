from google import genai

API_KEY = "YOUR_API_KEY"

client = genai.Client(api_key=API_KEY)

def generate_test_cases(feature):

    prompt = f"""
    Generate 5 software test cases for the following feature.

    Feature: {feature}

    For each test case include:
    Test Case
    Input
    Expected Output
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    print("\nGenerated Test Cases:\n")
    print(response.text)

feature = input("Enter software feature: ")
generate_test_cases(feature)