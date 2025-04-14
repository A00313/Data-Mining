library(tidyverse)

# Load data
df <- read_csv("tiktok_hastags.csv")

# Convert hashtag strings to actual lists
df$hashtags <- str_extract_all(df$hashtags, "#\\w+")

# Normalize variants of #edrecovery
df$hashtags <- lapply(df$hashtags, function(x) {
  x <- tolower(x)
  x <- gsub("0", "o", x)  # edrec0very -> edrecovery
  return(x)
})

# Filter rows that contain #edrecovery
ed_df <- df[sapply(df$hashtags, function(tags) "#edrecovery" %in% tags), ]

# Get co-occurring hashtags
co_tags <- unlist(ed_df$hashtags)
co_tags <- co_tags[co_tags != "#edrecovery"]

# Count frequency
co_tag_counts <- sort(table(co_tags), decreasing = TRUE)
head(co_tag_counts, 20)

