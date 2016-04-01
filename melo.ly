
\version "2.18.2"
\header
 {
  title = "TT SEE-HEAR"
  composer = "Python"
  tagline = "Copyright: -"
}\score{
 << \new Staff 
\set Staff.instrumentName = #"Piano  "
  {\tempo 4 = 40 \clef treble e bes g r e bes e c e r a e bes e r g bes bes r bes bes r g r bes c r g f c r e d e r g a g c e bes e g e e bes bes bes r a g a g g f g bes f r bes bes e r e g e g f }
 \new Staff 
\with {midiInstrument = #"cello"}  
  {\clef treble e r bes c r bes r e r r c g d r g e f e e e r e e e r bes e g r a e g bes bes e r e f e bes r g r bes e g e e r c e r c e e e g c r e bes e r bes g f g r }
>>
\layout{}
\midi{}
}
