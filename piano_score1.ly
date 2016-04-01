\version "2.18.2"
\header {
  title = "Este es el inicio"
  composer = "Python"
  tagline = "Copyright: -"
}\score{
\new PianoStaff << 
\set PianoStaff.instrumentName = #"Piano  "
  \new Staff {a'4 <a' c'> g'4 a' e'4 c' a'4 <a' c'> r2 a'4 <a' c'> g'4 a' r2 a'4 <a' c'> a'4 a' r2 d'4 g' a'4 g' d'4 g' d'4 e' d'4 g' a'2 r2 e'4 a' a'4 <a' c'> r2 <a' g'>2a'4 g' r2 a'4 a' <e' a'>2 a'4 a' <g' a'>4 a' a'2 r2 a'4 c' d'4 g' <e' a'>2 g'4 g' a'4 <a' c'> r2r2 <a' g'>2a'4 g' <e' a'>2 r2 a'4 g' <a' g'>2a'4 <a' c'> a'4 c' <e' a'>2 r2 <e' a'>2 a'4 c' a'4 <a' c'> a'4 g' e'4 c' <a' g'>2a'4 a' <e' a'>2 }
  \new Staff { \clef bass <c g>2 a2 g2 <c g>2 a4 a4 <c g>2 a2 a4 a4 <c g>2 e4 g a4 a4 <c e>2 e4 c <c e>2 g2 <c e>2 <c a g>2  a4 a4 e2 <c g>2 a4 a4 <c e g>2  e4 c a4 a4 e4 g <c a>2 g4 e a2 <c a g>2  a4 a4 e4 e <c e>2 <c a>2 a4 a <c g>2 r2 a4 a4 <c e g>2  e4 c <c a>2 a4 a4 e4 c <c e g>2  <c g>2 e4 e <c a>2 a4 a4 <c a>2 e4 e <c g>2 e4 c g2 <c e g>2  g4 e <c a>2 }
>>
\layout{ }
\midi {}
}

