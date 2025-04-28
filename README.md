# Cluster Analysis of Eating Disorder Recovery Content on TikTok (#edrec0very)

Authors

Ammar Alabboodi (ana154@pitt.edu)

Havannah Tung (hat127@pitt.edu)

This repository contains all materials for our project, including the final presentation slides, final paper, code, and dataset(s).

## Contents
[Final Project Slides (PDF)](DM%20Spring%2025%20Group%203.pdf)

[Final Project Paper (PDF)](DM%20Spring25%20final%20paper.docx.pdf)

[Source Code](https://github.com/A00313/Data-Mining)

[Search Dataset](initial_dataset/search_result_edrec0very.csv)

[Profile Dataset](scrape_profiles/tiktok_hashtags.csv)

[Clean Dataset](clean_dataset/tiktok_hashtags.csv)


## 📖 Abstract

Since TikTok's rise in popularity among young users in early 2020, concerns have grown regarding the platform's lack of regulation against content promoting unrealistic beauty standards. TikTok responded by updating ad policies (September 2020) and introducing interventions for eating disorder (ED) related searches (February 2021), such as redirecting users to the National Alliance for Eating Disorders Helpline. However, misspelled hashtags like #edrec0very (using "0" instead of "o") emerged as workarounds.

This project applies unsupervised learning techniques to analyze TikTok videos associated with the workaround hashtag #edrec0very, aiming to uncover common themes and content patterns within this online recovery community.

## 🔑 Keywords

Data mining · Clustering · Mental health · Social media · Eating disorders · TikTok · Unsupervised learning

## 📚 Introduction

Inspired by prior thematic analysis work (e.g., Herrick et al., 2020), this project focuses on understanding the evolving ED-recovery community on TikTok, particularly how creators have adapted to new content restrictions.Using clustering techniques, we aim to answer:

What are the common themes posted with the hashtag #edrec0very?

Do certain themes gain more popularity than others?

For creators posting ED-recovery-related TikToks, is their content ED-specific or broader?

📂 Dataset

1. #edrec0very Search Results

Scraped using Apify TikTok Data Extractor on March 31, 2025.

127 videos initially collected.

After preprocessing: 10 numerical features (e.g., likes, shares, views) normalized and log-transformed.

Top 20 hashtags associated with #edrec0very identified.

2. User Profile Hashtag Dataset

Scraped up to 50 videos per user from profiles appearing in #edrec0very search results.

4771 videos collected → reduced to 2565 after de-duplication.

Top 20 hashtags used across these user profiles extracted.

## ⚙️ Methodology

Search Result Analysis

Binary encoding of hashtags.

Principal Component Analysis (PCA) for dimensionality reduction.

K-means clustering (k = 4).

Cluster evaluation based on video popularity metrics.

User Profile Analysis

Hashtag parsing and normalization.

Document-Term Matrix (DTM) construction with TF-IDF weighting.

K-means clustering.

PCA for 2D visualization of clustering results.

Cluster interpretation based on top hashtags.

## 📈 Evaluation Summary

Using top hashtag proportion and entropy as evaluation metrics:

Cluster 3: #exerciseaddictionrecovery (77.8%, entropy = 0.76) → Highly focused recovery content.

Cluster 4: #fitcheck (76.9%, entropy = 0.99) → Fitness-related content with recovery ties.

Cluster 1: #collegelife (44.4%, entropy = 1.53) → College experiences mixed with ED-recovery.

Cluster 2: #1 (9.1%, entropy = 5.56) → Highly diverse, less coherent.

Cluster 5: #1 (5.1%, entropy = 8.73) → Most diverse and noisy cluster.

Clusters ranged from highly cohesive (recovery/fitness themes) to very diverse (mixed topics).

## 💬 Discussion

Limitations

Sampling bias from scraping (favoring popular/recent videos).

Small dataset relative to TikTok’s overall scale.

No "ground truth" labels for validating cluster themes.

Platform dynamics and hashtag trends evolve rapidly.

Future Work

Collect larger, more representative datasets.

Analyze additional workaround hashtags.

Apply dynamic clustering to track theme evolution over time.

Integrate deeper metadata features (e.g., account longevity, audience size).

Explore embedding-based models (e.g., BERT) for richer content analysis.

## 📝 Conclusion

This project highlights the potential of unsupervised learning methods to explore sensitive health-related discussions on social media platforms. Despite limitations, the approach reveals meaningful thematic structures in ED-recovery content on TikTok and points toward promising directions for future computational social science research.

## 📖 References

Herrick et al., 2020

Greene et al., 2023

Hedrick et al., 2022

Goh et al., 2021

Additional Research on ED-recovery Communities, 2024

## 📣 Acknowledgments

This project was completed as part of coursework at the University of Pittsburgh. Special thanks to our professors, peers, and the broader academic community researching eating disorder recovery and social media influences
