# 📰 anytime-anywhere-any-news

A Python-based CLI app that delivers real-time news from around the world on any topic, anytime, anywhere — powered by NewsAPI.

## 🔧 Features

- Fetches real-time news articles for a given topic
- Displays the title, description, and link for each article
- User-specified number of articles to fetch
- Clean and interactive CLI interface

## 🛠️ Requirements

- Python 3.x
- `requests` library
- A free API key from [NewsAPI](https://newsapi.org/)

## 🚀 How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/anytime-anywhere-any-news.git
   cd anytime-anywhere-any-news
   ```

2. **Install dependencies**:
   ```bash
   pip install requests
   ```

3. **Set up your API key**:
   - Open the `config.py` file.
   - Replace the value of `API_KEY` with your own NewsAPI key:
     ```python
     API_KEY = "your_actual_api_key"
     ```

4. **Run the script**:
   ```bash
   python main.py
   ```

## 📝 Example

```bash
What type of news are you interested in reading today? science
How many articles do you want to see? 5
```

## ⚠️ Note

The date is currently hardcoded in the request URL. You may modify this in `main.py` to use the current date dynamically.

## 📁 File Structure

```
anytime-anywhere-any-news/
│
├── main.py       # Main script to fetch and display news
├── config.py     # Stores the API key
└── README.md     # Project documentation
```

## 📜 License

This project is licensed under the MIT License.

## 🙌 Acknowledgments

- [NewsAPI](https://newsapi.org/) for providing the news data.