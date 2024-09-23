from gtts import gTTS
from pydub import AudioSegment


def text_to_speech(text: str, tts_audio_path: str) -> None:
    """Convert text to speech and save as MP3."""
    tts = gTTS(text)
    tts.save(tts_audio_path)
    audio = AudioSegment.from_file(tts_audio_path)
    sped_up_audio = audio.speedup(playback_speed=1.2)
    sped_up_audio.export(tts_audio_path, format="mp3")


def combine_audios(
    tts_audio_path: str,
    background_music_path: str,
    combined_audio_path: str,
    bgm_volume: int = -13,
    tts_volume: int = 6,
) -> None:
    """Overlay TTS audio on background music and save as a combined audio file."""
    background_music = AudioSegment.from_file(background_music_path)
    tts_audio = AudioSegment.from_file(tts_audio_path)

    background_music += bgm_volume
    tts_audio += tts_volume

    combined_audio = tts_audio.overlay(background_music)
    combined_audio.export(combined_audio_path, format="mp3")
