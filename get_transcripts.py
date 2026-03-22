from youtube_transcript_api import YouTubeTranscriptApi
import json

# Video IDs to fetch
video_ids = [
    ('FiHrWy2jGbA', 'Li Lu 2021 CBS Interview'),
]

results = []

yt_api = YouTubeTranscriptApi()

for vid_id, title in video_ids:
    try:
        # Use instance methods
        transcript_list = yt_api.list(vid_id)
        transcript = transcript_list.find_transcript(['en', 'zh-CN', 'zh-Hans'])
        data = transcript.fetch()
        # Combine all text
        full_text = ' '.join([seg['text'] for seg in data])
        results.append({
            'video_id': vid_id,
            'title': title,
            'segments': len(data),
            'text': full_text[:5000]
        })
        print(f'Got {title}: {len(data)} segments')
    except Exception as e:
        print(f'Error for {vid_id}: {e}')

# Save to file
with open('transcripts.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print('Saved to transcripts.json')
