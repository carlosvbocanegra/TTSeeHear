
\version "2.18.2"
\header
 {
  title = "TT SEE-HEAR"
  composer = "Python"
  tagline = "Copyright: -"
}\score{
 << \new Staff 
\set Staff.instrumentName = #"Piano  "
  {\tempo 4 = 60 \clef treble ees1 r2 g2 c2 ees2 bes2 ees2 ees2 ees2 r2 aes2 g1 d2 ees2 r1 g2 ees2 f1 ees1 ees1 ees1 r1 ees1 r2 ees2 c2 bes2 g2 g2 c2 aes2 ees1 g1 bes1 bes1 ees1 aes2 ees2 c2 ees2 bes1 r1 g1 r1 bes1 ees1 g1 ees2 bes2 r2 aes2 ees2 aes2 c2 g2 f1 ees2 bes2 c2 r2 bes1 bes1 ees1 r1 bes1 g1 f1 g1 r1 }
 \new Staff 
\with {midiInstrument = #"cello"}  
  {\clef treble ees2 bes2 bes2 r2 r2 bes2 r2 c2 r2 r2 c2 ees2 bes1 r1 g1 bes1 bes1 r1 bes1 bes1 r1 g2 ees2 bes2 r2 r2 ees2 f2 r2 r1 ees1 d1 ees1 r1 g2 r2 g2 f2 ees1 bes1 ees1 g1 ees1 ees1 bes1 bes1 ees2 r2 c2 g2 r2 g2 ees1 ees2 g2 g2 f2 r1 ees1 bes1 ees1 r2 ees2 g1 ees1 g1 f1 }
 \new Staff 
\with {midiInstrument = #"string ensemble 1"}  
  {\clef treble bes1 ees1 aes1 f1 g1 c1 d1 f1 ees1 d1 f1 ees1 c1 c1 c1 c1 g1 aes1 bes1 aes1 bes1 d1 g1 g1 g1 aes1 aes1 d1 c1 bes1 bes1 g1 bes1 ees1 ees1 f1 c1 ees1 d1 ees1 c1 g1 d1 c1 ees1 d1 bes1 c1 d1 ees1 }

  \new Staff 
\set Staff.instrumentName = #"Piano  "
  { 
>>
\layout{}
\midi{}
}
