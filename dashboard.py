import matplotlib.pyplot as plt

# -------------------------------
# 1. Posts by Date
# -------------------------------
dates = [
    "2026-09-01",
    "2026-09-02",
    "2026-09-03",
    "2026-09-04",
    "2026-09-05"
]

posts = [7, 12, 12, 12, 1]

plt.figure(figsize=(9, 5))
plt.plot(dates, posts, marker='o')
plt.title("Social Media Posts by Date")
plt.xlabel("Date")
plt.ylabel("Number of Posts")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("posts_by_date.png", dpi=300)
plt.close()


# -------------------------------
# 2. Sentiment Analysis
# -------------------------------
sentiments = ["Positive", "Negative"]
sentiment_count = [26, 18]

plt.figure(figsize=(7, 5))
plt.bar(sentiments, sentiment_count)
plt.title("Social Media Sentiment Analysis")
plt.xlabel("Sentiment")
plt.ylabel("Number of Posts")
plt.tight_layout()
plt.savefig("sentiment_analysis.png", dpi=300)
plt.close()


# -------------------------------
# 3. Top Hashtags
# -------------------------------
hashtags = [
    "#technology",
    "#city",
    "#weekend",
    "#weather",
    "#update",
    "#traffic",
    "#today",
    "#success",
    "#sports",
    "#service"
]

frequency = [9, 6, 3, 3, 3, 3, 3, 3, 3, 3]

plt.figure(figsize=(10, 6))
plt.barh(hashtags[::-1], frequency[::-1])
plt.title("Top Hashtag Frequency")
plt.xlabel("Frequency")
plt.ylabel("Hashtag")
plt.tight_layout()
plt.savefig("hashtag_frequency.png", dpi=300)
plt.close()

print("Dashboard charts created successfully!")
