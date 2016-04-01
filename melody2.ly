
\version "2.18.2"
\header
 {
  title = "TT SEE-HEAR"
  composer = "Python"
  tagline = "Copyright: -"
}\score{
 << \new Staff 
\set Staff.instrumentName = #"Piano  "
  {\key g \major \clef treble r2 c2 e1 e8 r4 c8 e1 c4 e4 c1 r2 c2 e2 e8 r4 c2 c1 e1 e8 e4 c2 c4 e2 e8 r2 c4 e8 c2 e4 r4 e2 c2 c8 e1 c8 e1 c2 c4 e4 c4 e2 c1 r2 r4 c2 e2 r4 r2 e8 e4 c4 r2 c8 c2 c1 r2 e8 e4 r2 c2 e2 r4 c2 e2 r4 c8 e1 c1 c8 e2 e4 c2 c8 c4 e8 }
 \new Staff 
\with {midiInstrument = #"cello"}  "
  {\key g \major \clef treble c8 c4 e2 e4 c2 r2 e8 e2 r4 c8 c4 e1 c1 e4 c8 r2 c4 e2 r4 c8 r2 e1 c1 e4 c8 e1 e2 c1 r4 e4 c4 c1 r2 e8 r2 e8 e2 c1 c2 c8 e4 e1 e8 c1 c4 e4 c8 e1 r4 e2 c2 c1 e1 c4 c8 e2 e1 c4 c8 c1 e4 e1 c4 e4 c1 r2 e8 c2 c4 e1 r2 c1 r2 e1 }
>>
\layout{ }
\midi {}
}
