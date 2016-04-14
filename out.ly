
\version "2.14.2"

\header {
    title = "Untitled"
    subtitle = "Created on: Wed Apr 13 23:11:42 2016"
    composer = "Anonymous and Foox"
}

result = {
    <<
    \new Staff
    {
        \time 4/4
        \clef treble
        {
            a'' 1 e'' b' a' c'' b' g' a' b' c''
        }
    }
    \new Staff
    {
        \time 4/4
        \clef treble
        {
            a' 1 g' g' c' c' g' e' d' e' c' \bar "|."
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
