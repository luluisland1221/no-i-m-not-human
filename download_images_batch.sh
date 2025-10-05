#!/bin/bash

# Create directories
mkdir -p temp_images/characters
mkdir -p temp_images/gameplay

# Character identification images
curl -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -o "temp_images/characters/neighbor_outside_door.jpg" "https://img1.entertainment14.net/images/090/03/1758109003_3572.jpg"
echo "✓ Downloaded neighbor_outside_door.jpg"

curl -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -o "temp_images/characters/neighbor_visitor_explanation.jpg" "https://img1.entertainment14.net/images/090/07/1758109007_3576.jpg"
echo "✓ Downloaded neighbor_visitor_explanation.jpg"

curl -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -o "temp_images/characters/neighbor_daughter.jpg" "https://img1.entertainment14.net/images/090/03/1758109003_3578.jpg"
echo "✓ Downloaded neighbor_daughter.jpg"

curl -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -o "temp_images/characters/tall_stranger.jpg" "https://img1.entertainment14.net/images/090/03/1758109003_3579.jpg"
echo "✓ Downloaded tall_stranger.jpg"

curl -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -o "temp_images/characters/confused_woman.jpg" "https://img1.entertainment14.net/images/090/04/1758109004_3580.jpg"
echo "✓ Downloaded confused_woman.jpg"

curl -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -o "temp_images/characters/medium_woman.jpg" "https://img1.entertainment14.net/images/090/07/1758109007_3581.jpg"
echo "✓ Downloaded medium_woman.jpg"

# Gameplay mechanism images
curl -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -o "temp_images/gameplay/news_tv.jpg" "https://img1.entertainment14.net/images/090/03/1758109003_3573.jpg"
echo "✓ Downloaded news_tv.jpg"

curl -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -o "temp_images/gameplay/radio_energy.jpg" "https://img1.entertainment14.net/images/090/03/1758109003_3574.jpg"
echo "✓ Downloaded radio_energy.jpg"

curl -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -o "temp_images/gameplay/neighbor_rules.jpg" "https://img1.entertainment14.net/images/090/03/1758109003_3575.jpg"
echo "✓ Downloaded neighbor_rules.jpg"

curl -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -o "temp_images/gameplay/player_bed.jpg" "https://img1.entertainment14.net/images/090/03/1758109003_3577.jpg"
echo "✓ Downloaded player_bed.jpg"

curl -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -o "temp_images/gameplay/visitor_identification_news.jpg" "https://img1.entertainment14.net/images/090/07/1758109007_3582.jpg"
echo "✓ Downloaded visitor_identification_news.jpg"

# Character check images
curl -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -o "temp_images/characters/checking_tall_stranger_teeth.jpg" "https://img1.entertainment14.net/images/090/07/1758109007_3583.jpg"
echo "✓ Downloaded checking_tall_stranger_teeth.jpg"

curl -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -o "temp_images/characters/checking_medium_woman_teeth.jpg" "https://img1.entertainment14.net/images/090/03/1758109003_3584.jpg"
echo "✓ Downloaded checking_medium_woman_teeth.jpg"

echo "All images downloaded successfully!"