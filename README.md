# Reddit AI Bot with Groq API 

Reddit Bot that that posts AI-generated content to Reddit daily using Groq API to generate engaging content

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Setup Instructions

### Generate Reddit App

- [Sign Up](https://www.reddit.com/register/) on Reddit
- [Create an app](https://www.reddit.com/prefs/apps/) of category script.
- Add Credentials in [main.py](src/main.py)

### Generate API Key for Groq API

- [Register](https://console.groq.com/login) on Groq
- [Generate Key](https://console.groq.com/keys)

### Additional Initial Setup needed
- Specify sub, prompt, posting, commenting times in [main.py](src/main.py)

## Usage

To run the Reddit Bot, execute :

```
python src/main.py
```

## Sample Output of Generated Posts
- [Generated Post](assets/post.png)
- [Generated Comment](assets/comment.png)

## License

This project is licensed under the MIT License.