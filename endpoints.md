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


---

### 📄 `philosophy-context.md`

```markdown
# ZenQuote API – Philosophical Context

Zen koans are not intellectual puzzles; they are encounters with reality. Each quote returned by this API is a chance to stop the mind’s search for answers and instead experience the texture of direct perception.

### Why a Koan API?

In an age of algorithmic answers and relentless certainty, the koan reminds us of the value of *not-knowing*—of standing before the unknown without resistance.

This project bridges technical communication with meditative awareness. The interface may be digital, but the experience it invites is timeless.

> “When the mouth opens, all are lost.” — Zen Saying
