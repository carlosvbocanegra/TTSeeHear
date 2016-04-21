
\version "2.18.2"
\header
 {
  title = "TT SEE-HEAR"
  composer = "Python"
  tagline = "Copyright: -"
}\score{
 << \new Staff 
\set Staff.instrumentName = #"Piano  "
  \relative c'' {\tempo 4 = 65 \clef treble g2 des2 bes2 c2 des2 r2 c2 r2 bes2 des2 des2 bes2 aes4 des2 g4 r2 g4 r4 g2 des2 bes8 c4 r4 bes8 g4 des2 r2 c8 aes8 g8 r8 g2 des2 bes2 g8 r4 bes8 g4 ees4 g8 bes8 r4 r4 ees4 c4 bes2 des4 bes8 c4 r8 g4 aes4 g2 aes4 des4 des2 g2 bes2 des4 g4 c4 r4 g8 g4 r8 r2 r2 g2 f2 bes4 des2 g4 ees4 aes4 f2 bes8 r8 g8 c2 aes8 bes2 f4 des4 aes8 g4 g8 r4 f4 des2 bes2  <ees g bes>2  <des f aes>2  <bes des f>1 }
 \new Staff 
\with {midiInstrument = #"cello"}  
  {\clef treble des2 aes2 des2 bes2 g2 aes2 des2 g2 aes2 r2 g2 des2 aes8 des4 c4 bes8 ees4 g2 f2 aes2 des2 ees8 g8 r8 f2 bes8 des2 g2 bes8 ees8 r8 f8 des2 g4 aes4 c2 f2 r4 g4 des2 aes2 g4 g4 r2 des8 ees8 f2 des8 bes8 c8 r4 r8 bes4 ees4 g2 f2 des4 aes4 bes2 ees8 f4 bes8 r8 ees4 bes8 g2 g2 des4 aes4 c2 g2 bes8 r8 r8 c8 des4 g4 des2 g8 g8 ees4 des4 r4 bes2 c4 r4 ees2 g2 }
 \new Staff 
 \with {midiInstrument = #"string ensemble 1"}  
  \relative c' {\clef treble g1 des1 f1 g1 des1 f1 c1 des1 ees1 des1 aes1 aes1 f1 g1 ees1 g1 g1 g1 f1 f1 ees1 bes1 ees1 g1 c1 bes1 des1 ees1 des1 ees2 des2 bes1 }
 \new Staff 
\with {midiInstrument = #"Acoustic Grand Piano"}  
  {\clef bass  <bes des f>1  <bes des f>1  \set tieWaitForNote = ##t \grace { ees32 ~ g ~ bes ~ ees ~ } <ees g bes ees>2. \unset tieWaitForNote  \set tieWaitForNote = ##t \grace { ees32 ~ g ~ bes ~ ees ~ } <ees g bes ees>4 \unset tieWaitForNote  <ees g bes>2.  <ees g bes>4  \set tieWaitForNote = ##t \grace { des32 ~ f ~ aes ~ des ~ } <des f aes des>1 \unset tieWaitForNote  <des f aes>2.  <des f aes>4  <bes des f>2.  <bes des f>4  \set tieWaitForNote = ##t \grace { bes32 ~ des ~ f ~ bes ~ } <bes des f bes>2. \unset tieWaitForNote  \set tieWaitForNote = ##t \grace { bes32 ~ des ~ f ~ bes ~ } <bes des f bes>4 \unset tieWaitForNote  <bes des f>2.  <bes des f>4  <bes des f>2.  <bes des f>4  <ees g bes>2.  <ees g bes>4  <ees g bes>2.  <ees g bes>4  \set tieWaitForNote = ##t \grace { des32 ~ f ~ aes ~ des ~ } <des f aes des>2. \unset tieWaitForNote  \set tieWaitForNote = ##t \grace { des32 ~ f ~ aes ~ des ~ } <des f aes des>4 \unset tieWaitForNote  <des f aes>2.  <des f aes>4  <bes des f>1  \set tieWaitForNote = ##t \grace { bes32 ~ des ~ f ~ bes ~ } <bes des f bes>2. \unset tieWaitForNote  \set tieWaitForNote = ##t \grace { bes32 ~ des ~ f ~ bes ~ } <bes des f bes>4 \unset tieWaitForNote  <bes des f>1  \set tieWaitForNote = ##t \grace { bes32 ~ des ~ f ~ bes ~ } <bes des f bes>2. \unset tieWaitForNote  \set tieWaitForNote = ##t \grace { bes32 ~ des ~ f ~ bes ~ } <bes des f bes>4 \unset tieWaitForNote  <ees g bes>2.  <ees g bes>4  <ees g bes>1  \set tieWaitForNote = ##t \grace { des32 ~ f ~ aes ~ des ~ } <des f aes des>1 \unset tieWaitForNote  <des f aes>2.  <des f aes>4  \set tieWaitForNote = ##t \grace { bes32 ~ des ~ f ~ bes ~ } <bes des f bes>1 \unset tieWaitForNote  <bes des f>2.  <bes des f>4  <bes des f>1  <bes des f>1  <ees g bes>2.  <ees g bes>4  \set tieWaitForNote = ##t \grace { ees32 ~ g ~ bes ~ ees ~ } <ees g bes ees>1 \unset tieWaitForNote  <des f aes>1  <ees g bes>2  <des f aes>2  <bes des f>1 }
>>
\layout{}
\midi{}
}
