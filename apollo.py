import mingus.core.notes as notes

from mingus.midi import fluidsynth


fluidsynth.init("soundfont.SF2")
fluidsynth.play_Note(Note("C-5"))

print(notes.is_valid_note("C"))
