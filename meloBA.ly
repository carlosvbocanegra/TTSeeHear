
\version "2.18.2"
\header
 {
  title = "TT SEE-HEAR"
  composer = "Python"
  tagline = "Copyright: -"
}\score{
 << \new Staff 
\set Staff.instrumentName = #"Piano  "
  \relative c'' {\tempo 4 = 88 \clef treble c4 r4 c8 b8 r8 e8 f2 d8 a8 g8 g8 g2 d4 c8 e8 c4 g4 f8 c8 g8 e8 a4 d4 e8 c8 c8 e8 b2 g4 e8 a8 a2 d4 g8 c8 a2 c8 f8 d8 g8 r2 c8 g8 r8 c8 b4 g4 f8 e8 r8 c8 c2 g8 a8 d8 g8 b2 e8 g8 r8 f8 c4 r4 g8 e8 f8 d8 g4 c4 b8 e8 r8 c8 b4 d4 g8 r8 f8 e8 c2 a8 d8 e8 c8 c2 g8 e8 a8 d8 g4 r4 f8 r8 c8 e8 a2 c4 e8 r8 g2 a8 d8 f8 r8 r2 e2 }
 \new Staff 
\with {midiInstrument = #"lead 1 (square)"}  
  {\clef treble g4 r4 f8 d8 a8 c8 r4 c4 e8 c8 r8 c8 a2 r8 b8 r8 e8 c2 r8 b8 r8 c8 g2 r8 f8 r8 r8 c4 f4 c8 e8 r8 g8 r2 b8 r8 c8 g8 e4 e4 r8 c8 b8 r8 e2 r8 c8 a8 d8 b2 r8 e8 r8 c8 f4 r4 e8 r8 r8 c8 e2 a8 c8 d8 g8 a2 r4 c4 e2 r8 r8 c8 g8 c2 c8 a8 c8 g8 g4 r4 f8 r8 b8 r8 c2 e4 b8 r8 c2 r4 f8 d8 b2 g8 g8 c8 c8 g4 c4 c8 e8 r8 b8 }
 \new Staff 
\with {midiInstrument = #"string ensemble 1"}  
  {\clef treble c1 d1 e1 g1 e1 d1 a1 f1 g1 f1 g1 d1 c1 e1 d1 e1 c1 e1 c1 d1 e1 }
>>
\layout{}
\midi{}
}
