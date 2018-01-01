from guitarPractice.exercises import (
    arpeggio_picking,
    chord_changes,
    dexterity,
    major_scale,
    pentatonic_scale
)
from guitarPractice.exercises.exercise_group import ExerciseGroup


def list_exercises():
    exercises = _get_exercise_map()

    return list(exercises.values())


def make_exercise(exercise_name, difficulty):
    exercises = _get_exercise_map()

    try:
        exercise = exercises[exercise_name][difficulty]
    except KeyError:
        raise ValueError('Invalid exercise name or difficulty')

    return exercise()


def _get_exercise_map():
    exercise_groups = [
        arpeggio_picking_exercises(),
        chords_changes_exercises(),
        dexterity_exercises(),
        major_scale_exercises(),
        pentatonic_scale_exercises(),
    ]

    return {
        group.group_id: group
        for group in exercise_groups
    }


def arpeggio_picking_exercises():
    key = 'arpeggio-picking'
    name = 'Arpeggio Picking'
    description = 'Pick some arpeggios'

    group = ExerciseGroup(key, name, description)
    group[1] = arpeggio_picking.level_one
    group[2] = arpeggio_picking.level_two

    return group


def chords_changes_exercises():
    key = 'chord-changes'
    name = 'Chord Change'
    description = 'Change between chords'

    group = ExerciseGroup(key, name, description)

    group[1] = chord_changes.level_one
    group[2] = chord_changes.level_two

    return group


def dexterity_exercises():
    key = 'dexterity'
    name = 'Fretting hand dexterity'
    description = 'Improve the dexterity of your fretting hand'

    group = ExerciseGroup(key, name, description)
    group[1] = dexterity.level_one

    return group


def major_scale_exercises():
    key = 'major-scale'
    name = 'Major Scale Positions'
    description = 'Learn the modes of the major scale'

    group = ExerciseGroup(key, name, description)
    group[1] = major_scale.level_one

    return group


def pentatonic_scale_exercises():
    key = 'pentatonic-scale'
    name = 'Pentatonic Scale Positions'
    description = 'Learn the modes of the pentatonic scale'

    group = ExerciseGroup(key, name, description)
    group[1] = pentatonic_scale.level_one

    return group
