from openai import OpenAI

OPENROUTER_API_KEY = (
    "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"
)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

TEST_MODEL = "openai/gpt-oss-120b:free"


def test_connection():
    print(f"Mengirim request ke OpenRouter...")
    print(f"Model: {TEST_MODEL}\n")

    try:
        response = client.chat.completions.create(
            model=TEST_MODEL,
            max_tokens=1000,
            messages=[
                {
                    "role": "system",
                    "content": "Kamu adalah asisten AI yang bertugas mengecek koneksi.",
                },
                {
                    "role": "user",
                    "content": "Halo! Tolong balas dengan singkat bahwa koneksi kita berhasil.",
                },
            ],
        )

        print("✅ KONEKSI BERHASIL!")
        print("-" * 30)
        print("Balasan AI:")
        print(response.choices[0].message.content)
        print("-" * 30)

    except Exception as e:
        print("❌ KONEKSI GAGAL!")
        print(f"Error: {e}")


if __name__ == "__main__":
    test_connection()
