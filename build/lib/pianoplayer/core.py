from music21 import stream
from pianoplayer.hand import Hand
from pianoplayer.scorereader import reader

def annotate_music21_score(temp_score: stream.Score, start_measure: int = 1, n_measures: int = None, hand_size: str = 'M', right_beam: int = 0, left_beam: int = 1, right_only: bool = False, left_only: bool = False, depth: int = 0, lyrics: bool = False, quiet: bool = True) -> stream.Score:
    """
    Annotates a music21 score with fingering information.

    Args:
        temp_score: The music21 score to annotate.
        start_measure: The starting measure number.
        n_measures: The number of measures to annotate. If None, annotates all measures.
        hand_size: The hand size ('XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL').
        right_beam: The beam number for the right hand.
        left_beam: The beam number for the left hand.
        right_only: If True, annotates only the right hand.
        left_only: If True, annotates only the left hand.
        depth: Depth of combinatorial search. 0 for auto.
        lyrics: Show fingering numbers below beam line.
        quiet: Switch off verbosity.

    Returns:
        The annotated music21 score.
    """

    if not left_only:
        rh = Hand("right", hand_size)
        rh.verbose = not quiet
        if depth == 0:
            rh.autodepth = True
        else:
            rh.autodepth = False
            rh.depth = depth
        rh.lyrics = lyrics

        rh.noteseq = reader(temp_score, beam=right_beam)
        rh.generate(start_measure, n_measures)

    if not right_only:
        lh = Hand("left", hand_size)
        lh.verbose = not quiet
        if depth == 0:
            lh.autodepth = True
        else:
            lh.autodepth = False
            lh.depth = depth
        lh.lyrics = lyrics

        lh.noteseq = reader(temp_score, beam=left_beam)
        lh.generate(start_measure, n_measures)

    return temp_score