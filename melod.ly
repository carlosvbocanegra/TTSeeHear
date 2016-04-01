
\version "2.18.2"
\header
 {
  title = "TT SEE-HEAR"
  composer = "Python"
  tagline = "Copyright: -"
}\score{
 << \new Staff 
\set Staff.instrumentName = #"Piano  "
  {\clef treble r r e b c f e a r d r r g b c r d e b r r a g b r a b r r c g r f e f e r a r a g d r c r g c r b r a r f r d r b r r r g c r g c f e d f g r r f a b }
 \new Staff 
\with {midiInstrument = #"cello"}  
  {\clef treble f a g r r r b g c f a e d r f r a g c f r e d r f e g d c r a d r b r b g d r f r e b d a r f e c g r d e a f g e a f d r e a r d r b r a e r d r e }
>>
\layout{}
\midi{}
}
