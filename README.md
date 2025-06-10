# zenquote-api-docs

## 🔗 Live Demo

🧘 [Try the ZenQuote API Demo](https://soluxum32.github.io/zenquote-api-docs/html-demo/)


# ZenQuote API Documentation

The **ZenQuote API** delivers daily koans and quotes from the Zen tradition in JSON format. This fictional API is designed as a technical writing sample and philosophical prompt engine.

## 🔍 Overview

This API allows users to:
- Retrieve a random Zen koan
- Get the koan of the day
- Browse by Zen master or theme (e.g., impermanence, emptiness, awakening)

## 📌 Base URL

https://api.zenquote.io/v1/


## 🔧 Endpoints

| Method | Endpoint              | Description                            |
|--------|-----------------------|----------------------------------------|
| GET    | /koan                 | Fetches a random Zen koan              |
| GET    | /koan/today           | Returns the koan of the day            |
| GET    | /koan?master=Name     | Filters koans by Zen master            |
| GET    | /theme/:topic         | Fetches koans by theme (e.g., emptiness)|

Full documentation is available in [`endpoints.md`](./endpoints.md)

## 🧪 Example Usage

Visit [`usage-examples/`](./usage-examples/) for:
- cURL usage samples
- Python script to fetch koans

## 🌸 Zen Philosophy Context

Koans are not riddles to be solved, but doorways to experience. This API is a meditation disguised as data. See [`philosophy-context.md`](./philosophy-context.md) for more.

## 📂 Project Files

- `endpoints.md` – Endpoint details with sample responses
- `usage-examples/` – Code examples using cURL and Python
- `philosophy-context.md` – Background on Zen and koan use

## ✍️ Author

Created by as a demonstration of technical writing, Markdown documentation, and API-oriented thinking.
