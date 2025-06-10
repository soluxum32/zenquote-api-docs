# ZenQuote API – Endpoint Reference

## GET /koan

Fetches a random Zen koan.

**Response:**
```json
{
  "koan": "What is your original face before your parents were born?",
  "master": "Hui-neng",
  "theme": "identity"
}

GET /koan/today

Returns the koan of the day.

Response:
 {
  "koan": "Not-knowing is most intimate.",
  "master": "Joshu",
  "theme": "intimacy"
}


GET /koan?master=Hakuin

Returns all koans by the specified master.

Response:
[
  {
    "koan": "You must carry the mountain itself.",
    "master": "Hakuin",
    "theme": "burden"
  },
  ...
]


GET /theme/emptiness

Returns koans that explore the theme of emptiness.

Response:
[
  {
    "koan": "If you meet the Buddha on the road, kill him.",
    "master": "Linji",
    "theme": "emptiness"
  }
]
