
\version "2.18.2"
\header
 {
  title = "TT SEE-HEAR"
  composer = "Python"
  tagline = "Copyright: -"
}\score{
 << \new Staff 
\set Staff.instrumentName = #"Piano  "
  \relative c'' {\tempo 4 = 88 \clef treble e8 r8 e8 d2 r8 bes8 g4 c8 a4 bes4 g4 g8 r8 e4 r8 d8 a8 bes4 e8 f4 r4 g4 d4 g8 a8 e8 e8 r4 d4 f8 r4 c8 c4 g4 r4 e4 e8 r4 e8 bes8 g4 a8 r4 e4 r8 r8 e4 d4 bes4 a8 bes4 e8 e8 r2 c4 g8 e8 g8 a4 bes4 bes4 r8 e8 bes4 a8 g4 g8 r8 e4 d4 f4 r8 e4 r8 d4 g8 bes4 r4 e4 c8 g4 g8 d4 r8 e8 bes2 g8 r4 g8 bes8 r4 e8 g4 c8 r4 e8 f4 e4 r8 c4 g4 bes8 g8 d4 r2 f8  <c e g>2  <bes d f>2  <bes d f>1 }
 \new Staff 
\with {midiInstrument = #"lead 1 (square)"}  
  {\clef treble g4 a8 bes4 bes8 g8 e8 e8 g8 r4 e4 r8 e8 f8 r4 c8 e4 bes4 c4 e4 r8 r4 e8 g8 a8 bes2 bes8 r8 e8 bes8 e8 a8 bes2 g4 r4 d8 r8 e8 r8 g4 c8 f4 bes4 d8 f8 r8 e4 c4 g8 g8 d8 r2 f8 r8 e8 bes8 g4 bes8 a4 r8 r8 d8 f4 c4 e8 g4 bes8 c2 r8 e4 e8 e4 f8 r4 r4 a4 bes8 e8 g4 c8 e8 e2 bes8 r8 a8 bes8 c8 a4 f4 d8 r4 e2 g8 a8 e8 bes8 r4 d4 bes8 r4 e8 bes8 e8 e8 r8 a2 }
 \new Staff 
 \with {midiInstrument = #"string ensemble 1"}  
  \relative c' {\clef treble bes1 d1 g1 f1 e1 bes1 a1 g1 g1 f1 e1 bes1 g1 bes1 c1 c1 f1 d1 bes1 c1 bes1 c2 bes2 bes1 }
 \new Staff 
\with {midiInstrument = #"Acoustic Grand Piano"}  
  {\clef bass  <bes d f>1  <bes d f>1  <c e g>2.  <c e g>4  \set tieWaitForNote = ##t \grace { c32 ~ e ~ g ~ c ~ } <c e g c>2. \unset tieWaitForNote  \set tieWaitForNote = ##t \grace { c32 ~ e ~ g ~ c ~ } <c e g c>4 \unset tieWaitForNote  <bes d f>2.  <bes d f>4  \set tieWaitForNote = ##t \grace { bes32 ~ d ~ f ~ bes ~ } <bes d f bes>2. \unset tieWaitForNote  \set tieWaitForNote = ##t \grace { bes32 ~ d ~ f ~ bes ~ } <bes d f bes>4 \unset tieWaitForNote  <bes d f>1  <bes d f>1  \set tieWaitForNote = ##t \grace { bes32 ~ d ~ f ~ bes ~ } <bes d f bes>2. \unset tieWaitForNote  \set tieWaitForNote = ##t \grace { bes32 ~ d ~ f ~ bes ~ } <bes d f bes>4 \unset tieWaitForNote  <bes d f>2.  <bes d f>4  \set tieWaitForNote = ##t \grace { c32 ~ e ~ g ~ c ~ } <c e g c>1 \unset tieWaitForNote  <c e g>2.  <c e g>4  \set tieWaitForNote = ##t \grace { bes32 ~ d ~ f ~ bes ~ } <bes d f bes>2. \unset tieWaitForNote  \set tieWaitForNote = ##t \grace { bes32 ~ d ~ f ~ bes ~ } <bes d f bes>4 \unset tieWaitForNote  <bes d f>2.  <bes d f>4  \set tieWaitForNote = ##t \grace { bes32 ~ d ~ f ~ bes ~ } <bes d f bes>1 \unset tieWaitForNote  <bes d f>2.  <bes d f>4  \set tieWaitForNote = ##t \grace { bes32 ~ d ~ f ~ bes ~ } <bes d f bes>1 \unset tieWaitForNote  <bes d f>1  <c e g>2.  <c e g>4  \set tieWaitForNote = ##t \grace { c32 ~ e ~ g ~ c ~ } <c e g c>2. \unset tieWaitForNote  \set tieWaitForNote = ##t \grace { c32 ~ e ~ g ~ c ~ } <c e g c>4 \unset tieWaitForNote  <bes d f>2.  <bes d f>4  <c e g>2  <bes d f>2  <bes d f>1 }
>>
\layout{}
\midi{}
}
