
\version "2.18.2"
\header
 {
  title = "TT SEE-HEAR"
  composer = "Python"
  tagline = "Copyright: -"
}\score{
 << \new Staff 
\set Staff.instrumentName = #"Piano  "
  {\key g \major \clef treble e2 a2 g8 b8 b2 r4 g1 b1 r8 g2 a4 c8 e4 d2 r8 a8 g8 r4 f8 b2 d4 r8 r4 r8 f4 f2 d2 g2 b4 c8 g8 b8 r4 b2 r8 g4 e2 r2 r8 f4 a4 f8 c1 c4 f2 d2 g2 b4 a8 a2 b8 d4 r4 r2 f8 b1 f1 b4 d8 c8 b2 a8 r4 r8 b8 b1 r8 a1 e4 e8 c2 d2 c4 f2 f1 r4 a2 d4 d8 r2 b1 d2 f4 e4 c8 r4 f1 a8 e8 r8 r8 c2 b4 g2 g1 f2 e4 c2 c4 a1 a2 d8 b2 a8 g8 r8 r4 r2 f8 r8 a8 r8 r4 e8 f8 b8 b2 g1 c2 r8 d1 e4 b1 c1 r8 d2 f2 g4 f4 d1 d2 b1 r4 e4 c2 c1 d4 e2 r8 r2 e8 g8 d8 c1 c8 e1 g4 f2 d1 r4 g2 b4 b1 a1 b2 e2 r4 f8 a2 g8 f1 g1 d2 r8 b1 f4 a1 a4 c8 c2 c4 r8 r4 e2 r2 g8 g4 a1 c4 c8 f2 d1 e2 r8 r2 f8 b1 f1 d2 d4 g8 d8 a4 d1 r8 c2 e4 g4 f2 d2 g2 b1 f1 a2 e8 r2 g8 a1 r8 g1 d1 a4 e4 c2 r8 c4 b1 e2 r2 r8 g8 c1 c4 r8 a1 d4 b1 d1 g1 d2 r8 f1 a2 g4 c1 c8 a2 e4 g8 r2 r8 f2 e2 f8 }
 \new Staff 
\with {midiInstrument = #"cello"}  "
  {\key g \major \clef treble d4 a8 r8 d8 r2 e8 g4 f8 r4 d1 r8 a1 e1 c2 a2 b8 e2 e8 d8 r2 b1 d1 a4 e4 e1 g1 g4 f1 a1 r8 a8 d8 r8 b1 e1 d4 e8 a2 g1 e4 d1 a1 r4 c8 c2 r8 f1 r8 g8 d8 b2 g4 e8 e2 r8 r4 a4 d4 g4 r8 a2 g8 r2 e2 a4 r8 e1 g1 d1 c1 f4 r4 f8 g2 e2 b8 g4 g8 r8 f8 g1 a4 a1 e1 f2 g2 b4 d1 b2 c4 c1 r8 f1 r4 d1 f4 e1 c1 c8 r8 d4 g4 r8 b8 d2 b1 e2 e8 a4 g8 a2 d4 e2 r2 r8 d8 r4 g4 e1 a4 a1 f4 c8 c4 g2 f1 r8 a1 f2 a4 g1 r8 g2 c8 e1 a2 c4 b8 b2 r4 f1 f8 b4 c2 r8 e4 f4 r8 d2 g1 f1 a4 c4 r2 r8 e8 d4 b8 d8 b4 g2 r4 d1 f2 e4 g4 e1 b2 c1 a2 r8 d4 d8 b8 e8 e4 e1 c1 c2 f4 r8 a4 r4 r4 g1 r8 g2 e8 a2 b8 a8 b2 e2 c8 a1 c1 e1 f4 r8 g1 r4 c4 d4 r4 r8 b2 f4 g4 r4 g2 f1 f2 c8 c1 e1 d2 r4 d4 f8 b2 a2 c2 c8 e1 g4 f2 e4 a4 f4 r4 g2 r2 e1 c2 c4 r8 d4 a1 e8 f4 a4 d1 r4 }
>>
\layout{ }
\midi {}
}
