from videohash import VideoHash
import numpy as np
import librosa
import os

def video_check(video_path1,video_dataset_paths):
    similar_videos = []
    path1 = video_path1
    videohash1 = VideoHash(path=path1)
    for i in video_dataset_paths:
        videohash2 = VideoHash(path=i)
        if(videohash1.is_similar(videohash2)):
            similar_videos.append(i)
    return similar_videos

def extract_audio(audio_path):
    audio,sr = librosa.load(audio_path)  # Or use torchaudio.load() for PyTorch usage
    return audio, sr

def pre_process_audio(audio, target_sr=16000):
    """Resamples and normalizes audio."""    
    audio = librosa.resample(audio, orig_sr=audio.sr, target_sr=target_sr)
    audio = librosa.util.normalize(audio)
    return audio


def extract_features(audio,sr):
    """Extracts MFCCs from the audio data."""
    if audio is None:
        raise ValueError("Audio data cannot be None.")  # Handle missing audio
    # Extract MFCCs
    mfccs = librosa.feature.mfcc(y=audio,sr=sr)  # Call with only the required argument
    return mfccs


def calculate_similarity(feature1, feature2):
    """Calculates Euclidean distance."""
    if feature1.shape[0] != feature2.shape[0]:
        raise ValueError("Features have different batch sizes.")
    
    # Check if second dimension (number of features) needs reshaping
    if feature1.shape[1] != feature2.shape[1]:
        # Choose your preferred reshaping strategy:

            # Option 2: Truncate/pad to match smaller size
            smaller_size = min(feature1.shape[1], feature2.shape[1])
            feature1 = feature1[:, :smaller_size]
            feature2 = feature2[:, :smaller_size]

    # Calculate similarity after reshaping (replace with your chosen metric)
    distance = np.linalg.norm(feature1 - feature2)
    return distance
 

def find_near_duplicates(audio_path, dataset_paths, threshold=0.7):
    audio,sr = extract_audio(audio_path)
    features = extract_features(audio,sr)
    matches = []
    for dataset_path in dataset_paths:
        dataset_audio,dataset_sr = extract_audio(dataset_path)
        dataset_features = extract_features(dataset_audio,dataset_sr)
        similarity = calculate_similarity(features, dataset_features)
        if similarity < threshold:
            matches.append(dataset_path)
    return matches

# Example usage:
input_path = "Deepfake Video"
video_path = input_path + ".mp4"
audio_path = input_path + ".mp3"
audio_database_path = "Dataset\Audio"
video_database_path = "Dataset\Video"
audio_dataset_paths = []
video_dataset_paths = []
for audio_file in os.listdir(audio_database_path):
            audio_dataset_paths.append(os.path.join(audio_database_path, audio_file))
for video_file in os.listdir(video_database_path):
            video_dataset_paths.append(os.path.join(video_database_path, video_file))

similar_videos = video_check(video_path,video_dataset_paths)
similar_videos = [os.path.splitext(os.path.basename(similar_video))[0] for similar_video in similar_videos]
matches = find_near_duplicates(audio_path, audio_dataset_paths)
matches = [os.path.splitext(os.path.basename(match))[0] for match in matches]
print("Near-duplicate Videos:", similar_videos)
print("\nNear-duplicate Audios:", matches)
new_list = [element for element in similar_videos if element not in matches] + [element for element in matches if element not in similar_videos]
print("Original Video(s):", new_list)
