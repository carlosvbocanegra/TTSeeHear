
\version "2.14.2"

\header {
    title = "Untitled"
    subtitle = "Created on: Wed Apr 13 14:38:14 2016"
    composer = "Anonymous and Foox"
}

result = {
    <<
    \new Staff
    {
        \time 4/4
        \clef treble
        {
            b' 1 c'' g'' a' d'' c'' f'' c'' f' g' a' e' e' g' c'' e'' f'' a' g' d'' b' e' d'' c'' e'' c'' b' c''
        }
    }
    \new Staff
    {
        \time 4/4
        \clef treble
        {
            e' 1 a' g' c' f' e' b' e' d' c' c' c' c' c' a' e' a' c' e' g' g' c' f' a' g' e' g' c' \bar "|."
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
