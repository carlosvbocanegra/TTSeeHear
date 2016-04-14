
\version "2.18.2"
\header
 {
  title = "TT SEE-HEAR"
  composer = "Python"
  tagline = "Copyright: -"
}\score{
 << \new Staff 
\set Staff.instrumentName = #"Piano  "
  {\tempo 4 = 60 \clef treble bes1 r2 d2 g2 bes2 f2 bes2 bes2 bes2 r2 e2 d1 a2 bes2 r1 d2 bes2 c1 bes1 bes1 bes1 r1 bes1 r2 bes2 g2 f2 d2 d2 g2 e2 bes1 d1 f1 f1 bes1 e2 bes2 g2 bes2 f1 r1 d1 r1 f1 bes1 d1 bes2 f2 r2 e2 bes2 e2 g2 d2 c1 bes2 f2 g2 r2 f1 f1 bes1 r1 f1 d1 c1 d1 r1 }
 \new Staff 
\with {midiInstrument = #"cello"}  
  {\clef treble bes2 f2 f2 r2 r2 f2 r2 g2 r2 r2 g2 bes2 f1 r1 d1 f1 f1 r1 f1 f1 r1 d2 bes2 f2 r2 r2 bes2 c2 r2 r1 bes1 a1 bes1 r1 d2 r2 d2 c2 bes1 f1 bes1 d1 bes1 bes1 f1 f1 bes2 r2 g2 d2 r2 d2 bes1 bes2 d2 d2 c2 r1 bes1 f1 bes1 r2 bes2 d1 bes1 d1 c1 }
>>
\layout{}
\midi{}
}
