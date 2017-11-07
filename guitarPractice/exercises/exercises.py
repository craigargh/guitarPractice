from guitarPractice.exercises import (
    arpeggio_picking,
    chord_changes,
    dexterity,
    major_scale
)


def make_exercise(exercise_name, difficulty):
    exercises = {
        'arpeggio-picking': arpeggio_picking_levels(),
        'chord-changes': chords_changes_levels(),
        'dexterity': dexterity_levels(),
        'major-scale': major_scale_levels(),
    }

    try:
        exercise = exercises[exercise_name][difficulty]
    except KeyError:
        raise ValueError('Invalid exercise name or difficulty')

    return exercise()


def arpeggio_picking_levels():
    return {
        1: arpeggio_picking.level_one,
        2: arpeggio_picking.level_two
    }


def chords_changes_levels():
    return {
        1: chord_changes.level_one
    }


def dexterity_levels():
    return {
        1: dexterity.level_one
    }


def major_scale_levels():
    return {
        1: major_scale.level_one
    }
