from utils.logger import setup_logger
from groq import Groq

logger = setup_logger('groq_api', 'groq_api.log')

def get_post_content(prompt = "Generate engaging content for reddit post"):
    try:
        prompt = prompt + " with output being like Title-{title} , Message-{message}, don't write any introductory text."

        client = Groq(
            api_key="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",
        )

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        
        content =  chat_completion.choices[0].message.content

        lines = content.split("\n")
        title = lines[0][6:] #Length of Title- is 6
        message = lines[1][8:] #Length of word message- is 8
        
        return title, message

    except Exception as e:
        logger.error(f'Failed to generate content: {e}')
        raise