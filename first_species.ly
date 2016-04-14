
\version "2.14.2"

\header {
    title = "Untitled"
    subtitle = "Created on: Tue Apr 12 14:44:52 2016"
    composer = "Anonymous and Foox"
}

result = {
    <<
    \new Staff
    {
        \time 4/4
        \clef treble
        {
            d'' 1 a' g' b' e'' c'' c'' b' d'' cis'' d''
        }
    }
    \new Staff
    {
        \time 4/4
        \clef treble
        {
            d' 1 f' e' d' g' f' a' g' f' e' d' \bar "|."
        }
    }
    >>
}

\paper {
    raggedbottom = ##t
    indent = 7. \mm
    linewidth = 183.5 \mm
    betweensystemspace = 25\mm
    betweensystempadding = 0\mm
}

\score{
    \result
    \midi {
        \context {
            \Score
            tempoWholesPerMinute = #(ly:make-moment 160 4)
        }
    }
    \layout {}
}
