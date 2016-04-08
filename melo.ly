
\version "2.18.2"
\header
 {
  title = "TT SEE-HEAR"
  composer = "Python"
  tagline = "Copyright: -"
}\score{
 << \new Staff 
\set Staff.instrumentName = #"Piano  "
  {\tempo 4 = 88 \clef treble bes4 r4 bes8 a8 r8 d8 e2 c8 g8 f8 f8 f2 c4 bes8 d8 bes4 f4 e8 bes8 f8 d8 g4 c4 d8 bes8 bes8 d8 a2 f4 d8 g8 g2 c4 f8 bes8 g2 bes8 e8 c8 f8 r2 bes8 f8 r8 bes8 a4 f4 e8 d8 r8 bes8 bes2 f8 g8 c8 f8 a2 d8 f8 r8 e8 bes4 r4 f8 d8 e8 c8 f4 bes4 a8 d8 r8 bes8 a4 c4 f8 r8 e8 d8 bes2 g8 c8 d8 bes8 bes2 f8 d8 g8 c8 f4 r4 e8 r8 bes8 d8 g2 bes4 d8 r8 f2 g8 c8 e8 r8 r2 d2 }
 \new Staff 
\with {midiInstrument = #"lead 1 (square)"}  
  {\clef treble f4 r4 e8 c8 g8 bes8 r4 bes4 d8 bes8 r8 bes8 g2 r8 a8 r8 d8 bes2 r8 a8 r8 bes8 f2 r8 e8 r8 r8 bes4 e4 bes8 d8 r8 f8 r2 a8 r8 bes8 f8 d4 d4 r8 bes8 a8 r8 d2 r8 bes8 g8 c8 a2 r8 d8 r8 bes8 e4 r4 d8 r8 r8 bes8 d2 g8 bes8 c8 f8 g2 r4 bes4 d2 r8 r8 bes8 f8 bes2 bes8 g8 bes8 f8 f4 r4 e8 r8 a8 r8 bes2 d4 a8 r8 bes2 r4 e8 c8 a2 f8 f8 bes8 bes8 f4 bes4 bes8 d8 r8 a8 }
>>
\layout{}
\midi{}
}
