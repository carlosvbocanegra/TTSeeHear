\version "2.18.2"
upper = \relative c'' {
  \clef treble
  \key c \major
  \time 4/4

  a4 b c d
}

\score{
	
  	
  	\new PianoStaff <<
    	\set PianoStaff.instrumentName = #"Piano  "
    	\new Staff = "upper" \upper
  	>>
  	\layout{}
	\midi {}
}