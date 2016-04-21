
\version "2.14.2"

\header {
    title = "Untitled"
    subtitle = "Created on: Wed Apr 20 21:05:40 2016"
    composer = "Anonymous and Foox"
}

result = {
    <<
    \new Staff
    {
        \time 4/4
        \clef treble
        {
            g' 1 a' g' e' g' a' a' d'' d'' c'' e'' dis'' e''
        }
    }
    \new Staff
    {
        \time 4/4
        \clef treble
        {
            c' 1 c' e' c' e' c' c' b' f' c' g' g' e' \bar "|."
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
