import cv2
from PIL import Image
from transformers import pipeline

BEHAVIOR_LABELS = {
    "Rolling": "a pet rolling on the floor",
    "Spinning": "a pet spinning excitedly",
    "Running toward owner": "a pet running toward a person",
    "Sitting still": "a pet sitting still and looking calm",
    "Sleeping": "a pet sleeping",
    "Stretching": "a pet stretching its body",
    "Yawning": "a pet yawning",
    "Head tilt": "a pet tilting its head",
    "Toy": "a pet holding or playing with a toy"
}

_classifier = None


def get_classifier():
    global _classifier
    if _classifier is None:
        _classifier = pipeline(
            "zero-shot-image-classification",
            model="openai/clip-vit-base-patch32"
        )
    return _classifier


def sample_frames(video_path, num_frames=5):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError("Could not open video for behavior detection.")

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    if total_frames <= 0:
        total_frames = 1

    frame_indices = []
    for i in range(num_frames):
        idx = int((i + 1) * total_frames / (num_frames + 1))
        frame_indices.append(idx)

    frames = []
    for idx in frame_indices:
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ret, frame = cap.read()
        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frames.append(Image.fromarray(frame_rgb))

    cap.release()
    return frames


def suggest_behaviors(video_path, top_k=3):
    classifier = get_classifier()
    frames = sample_frames(video_path, num_frames=5)

    candidate_labels = list(BEHAVIOR_LABELS.values())
    reverse_map = {v: k for k, v in BEHAVIOR_LABELS.items()}

    scores = {k: [] for k in BEHAVIOR_LABELS.keys()}

    for frame in frames:
        results = classifier(frame, candidate_labels=candidate_labels)
        for item in results:
            behavior_name = reverse_map[item["label"]]
            scores[behavior_name].append(item["score"])

    avg_scores = {}
    for behavior, vals in scores.items():
        avg_scores[behavior] = sum(vals) / len(vals) if vals else 0.0

    ranked = sorted(avg_scores.items(), key=lambda x: x[1], reverse=True)
    return ranked[:top_k]

