\version "2.18.2"\header
 {
  title = "TT SEE-HEAR"
  composer = "Python"
  tagline = "Copyright: -"
}\score{
\new PianoStaff << 
\set PianoStaff.instrumentName = #"Piano  "
  \new Staff {a'4 <a' c'> g'4 a' e'4 c' a'4 <a' c'> r2 a'4 <a' c'> g'4 a' r2 a'4 <a' c'> a'4 a' }
  \new Staff { \clef bass <c g>2 a2 g2 <c g>2 a4 a4 <c g>2 a2 a4 a4 <c g>2 e4 g }
>>
\layout{ }
\midi {}
}

