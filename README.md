LLM-Powered Cryptocurrency Analysis Agent:
This project implements a multi-agent, LLM-powered system for cryptocurrency market analysis. It leverages LangChain for workflow orchestration, Groq for optimized inference with Llama 3 models, and external APIs for real-time data retrieval. The system produces consolidated reports by combining news sentiment analysis with historical price analysis.

Features:
LangChain Integration – Orchestrates LLM workflows and multi-agent interactions.
Agent-Based Architecture – Dedicated agents for communication, news analysis, price analysis, and report writing.
Cryptocurrency Price Tool – Fetches the last 60 days of historical closing prices.
News Tool (Exa API) – Retrieves and summarizes the latest cryptocurrency-related news.
LLM-Powered Agents – Performs price trend analysis, news sentiment analysis, and report synthesis.
Groq Inference – Runs Llama 3 efficiently for analysis and report generation.

Agents:
Customer Communicator – Identifies the cryptocurrency of interest based on user input.
News Analyst – Retrieves recent news articles and performs sentiment-based market prediction.
Price Analyst – Analyzes historical price data and generates technical predictions.
Report Writer – Compiles analyses from the news and price analysts into a final summary report.

Workflow:
Select Cryptocurrency – The system prompts the user for the cryptocurrency symbol (e.g., BTC, ETH).
News Retrieval and Analysis – The News Analyst fetches recent articles and produces a sentiment-based prediction.
Price Data Retrieval and Analysis – The Price Analyst gathers historical prices and identifies market trends.
Final Report Generation – The Report Writer consolidates outputs into a structured report summarizing both analyses.

Tools & APIs:
Exa API – For retrieving and summarizing real-time cryptocurrency news.
Alpha Vantage API – For accessing historical cryptocurrency price data.
Groq API – For running optimized inference with Llama 3.

Getting Started:
Prerequisites:
Python 3.8+
Google Colab (or Jupyter Notebook environment)

API keys for:
Groq
Exa
Alpha Vantage

Installation:
Clone the repository:
git clone https://github.com/your-username/your-repo.git
cd your-repo

Install dependencies:
pip install -r requirements.txt
Setup
Insert your API keys in the notebook before execution:
GROQ_API_KEY = "your_groq_api_key"
EXA_API_KEY = "your_exa_api_key"
ALPHA_VANTAGE_API_KEY = "your_alpha_vantage_api_key"

Running the Project:
Open the provided .ipynb notebook in Google Colab or Jupyter and run all cells. The system will guide you through the analysis process.
Example Output:
For BTC (Bitcoin):
News Analysis → Summarizes the latest Bitcoin-related news and provides sentiment-based prediction.
Price Analysis → Analyzes the past 60 days of BTC closing prices and projects short-term market direction.
Final Report → Combines both analyses into a structured one-paragraph summary.
Tech Stack:
Python
LangChain
Llama 3 (via Groq Inference)
Exa API
Alpha Vantage API

Acknowledgements:
Alpha Vantage – For cryptocurrency price data.
Groq – For optimized LLM inference.
Exa – For real-time news retrieval.
