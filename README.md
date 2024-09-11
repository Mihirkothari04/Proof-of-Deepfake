# Proof of Deepfake: Simplified Implementation

## Overview
This project presents a simplified implementation of a deepfake detection system. It uses lightweight tools like Librosa and VideoHash to provide a more resource-efficient approach compared to full-scale Near-Duplicate Video Retrieval (NDVR) systems, which are typically used for large-scale data processing.

## Features
- Video similarity detection using perceptual hashing
- Audio feature extraction and similarity analysis
- Comparison of video and audio similarities to identify potential deepfakes

## Technical Stack
- Python 3.x
- VideoHash for video similarity detection
- Librosa for audio processing and feature extraction
- NumPy for numerical operations

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/proof-of-deepfake.git
   cd proof-of-deepfake
   ```

2. Install the required packages:
   ```
   pip install videohash numpy librosa
   ```

## Project Structure
- `Duplicate_Audio_Video_detection.py`: Main script for deepfake detection
- `Dataset/`: Directory containing subdirectories for audio and video datasets
  - `Audio/`: Contains audio files for comparison
  - `Video/`: Contains video files for comparison

## Execution Process

1. **Prepare Your Data**:
   - Place your input video file (MP4 format) in the project directory.
   - Extract the audio from your input video and save it as an MP3 file in the project directory.
   - Ensure you have a dataset of comparison videos in the `Dataset/Video/` directory.
   - Ensure you have a dataset of comparison audio files in the `Dataset/Audio/` directory.

2. **Configure the Script**:
   - Open `Duplicate_Audio_Video_detection.py` in a text editor.
   - Locate the `input_path` variable near the bottom of the file.
   - Set `input_path` to the name of your input file (without the file extension).

3. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the project directory.
   - Run the script using Python:
     ```
     python Duplicate_Audio_Video_detection.py
     ```

4. **Interpret the Results**:
   The script will output three sets of results:
   - Near-duplicate Videos: Videos in the dataset that are visually similar to the input video.
   - Near-duplicate Audios: Audio files in the dataset that are similar to the input audio.
   - Original Video(s): Any discrepancies between video and audio matches, which may indicate a potential deepfake.

## How It Works
1. **Video Similarity Check**: 
   - Uses VideoHash to generate perceptual hashes of the input video and dataset videos.
   - Compares hashes to identify visually similar videos.

2. **Audio Similarity Check**:
   - Extracts Mel-frequency cepstral coefficients (MFCCs) from the input audio and dataset audio files.
   - Calculates Euclidean distances between MFCCs to identify similar audio.

3. **Deepfake Detection**:
   - Compares the results of video and audio similarity checks.
   - Identifies potential deepfakes based on discrepancies between video and audio matches.

## Limitations and Future Work
- This implementation is designed for smaller datasets and may not scale efficiently to very large video collections.
- Future improvements could include more advanced feature extraction techniques and machine learning models for better accuracy.
- Integration with social media APIs could provide additional metadata for verification.

## Conclusion
This project demonstrates a simplified approach to deepfake detection using readily available tools. While not as comprehensive as full-scale NDVR systems, it provides a practical solution for smaller-scale applications or as a proof-of-concept for more advanced implementations.
