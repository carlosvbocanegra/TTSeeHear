
\version "2.18.2"
\header
 {title = "TT SEE-HEAR brill"composer = "TT SEE-HEAR"}\score{
 << \new Staff 
\set Staff.instrumentName = #"Piano  "
  \relative c'' {\tempo 4 = 88 \clef treble f8 r4 f4 e8 r4 c8 a4 d4 bes8 c4 a8 a8 r8 f8 r4 e4 bes8 c8 f8 g8 r2 a4 e8 a8 bes8 f8 f4 r8 e8 g2 r8 d8 d8 a4 r8 f2 f4 r8 f8 c8 a8 bes4 r4 f4 r8 r8 f4 e4 c4 bes8 c8 f4 f8 r2 d4 a8 f8 a8 bes8 c8 c2 r8 f8 c8 bes4 a8 a4 r4 f4 e8 g4 r8 f4 r8 e8 a4 c4 r8 f4 d4 a8 a4 e8 r2 f4 c8 a8 r8 a8 c4 r8 f4 a8 d8 r4 f4 g4 f8 r8 d8 a8 c2 a4 e4 r4 g4  <c e g>2  <bes d f>2  <f a c>1 }
 \new Staff 
\with {midiInstrument = #"lead 1 (square)"}  
  {\clef treble a4 bes8 c4 c8 a8 f8 f8 a8 r4 f4 r8 f8 g2 r8 d8 f8 c8 d4 f8 r8 r4 f4 a4 bes4 c8 c8 r4 f8 c8 f8 bes2 c8 a8 r8 e8 r4 f4 r8 a8 d4 g8 c4 e4 g4 r8 f8 d8 a4 a8 e8 r2 g8 r8 f8 c4 a4 c8 bes8 r8 r8 e8 g4 d8 f4 a4 c4 d4 r4 f4 f4 f8 g8 r4 r4 bes8 c8 f8 a4 d8 f4 f8 c8 r2 bes8 c8 d2 bes8 g8 e8 r8 f2 a8 bes8 f8 c8 r8 e4 c4 r4 f8 c4 f4 f8 r8 bes4 }
 \new Staff 
 \with {midiInstrument = #"string ensemble 1"}  
  \relative c' {\clef treble c1 e1 f1 d1 a1 g1 f1 a1 a1 g1 f1 a1 d1 f1 a1 f1 g1 f1 c1 d1 c1 c2 bes2 f1 }
 \new Staff 
\with {midiInstrument = #"acoustic grand"}  
  {\clef bass  <f a c>1  \set tieWaitForNote = ##t \grace { f32 ~ a ~ c ~ f ~ } <f a c f>2. \unset tieWaitForNote  \set tieWaitForNote = ##t \grace { f32 ~ a ~ c ~ f ~ } <f a c f>4 \unset tieWaitForNote  <c e g>2.  <c e g>4  \set tieWaitForNote = ##t \grace { c32 ~ e ~ g ~ c ~ } <c e g c>1 \unset tieWaitForNote  <bes d f>2.  <bes d f>4  <bes d f>1  <f a c>1  <f a c>1  <f a c>1  <f a c>1  \set tieWaitForNote = ##t \grace { c32 ~ e ~ g ~ c ~ } <c e g c>2. \unset tieWaitForNote  \set tieWaitForNote = ##t \grace { c32 ~ e ~ g ~ c ~ } <c e g c>4 \unset tieWaitForNote  <c e g>1  <bes d f>1  <bes d f>1  \set tieWaitForNote = ##t \grace { f32 ~ a ~ c ~ f ~ } <f a c f>1 \unset tieWaitForNote  <f a c>1  <f a c>2.  <f a c>4  \set tieWaitForNote = ##t \grace { f32 ~ a ~ c ~ f ~ } <f a c f>2. \unset tieWaitForNote  \set tieWaitForNote = ##t \grace { f32 ~ a ~ c ~ f ~ } <f a c f>4 \unset tieWaitForNote  <c e g>1  <c e g>1  <bes d f>2.  <bes d f>4  <c e g>2  <bes d f>2  <f a c>1 }
>>
\layout{}
\midi{}
}
