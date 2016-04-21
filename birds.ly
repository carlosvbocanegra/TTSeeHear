
\version "2.18.2"
\header
 {title = "TT SEE-HEAR birds"composer = "TT SEE-HEAR"}\score{
 << \new Staff 
\set Staff.instrumentName = #"Piano  "
  \relative c'' {\tempo 4 = 65 \clef treble bes2 f2 des2 ees2 f2 r2 ees2 r2 des2 f2 f2 des2 c2 f4 bes4 r4 bes2 r4 bes2 f2 des4 ees4 r8 des8 bes4 f2 r2 ees8 c4 bes8 r4 bes4 f2 des2 bes8 r4 des8 bes4 g4 bes8 des8 r4 r4 g4 ees4 des4 f2 des4 ees4 r4 bes8 c8 bes4 c2 f4 f2 bes2 des2 f4 bes4 ees8 r8 bes8 bes8 r2 r2 r2 bes2 aes2 des4 f4 bes2 g2 c4 aes4 des8 r4 bes4 ees8 c4 des2 aes4 f4 c4 bes4 bes4 r8 aes8 f2 des2  <ees g bes>2  <des f aes>2  <bes des f>1 }
 \new Staff 
\with {midiInstrument = #"viola"}  
  {\clef treble f2 c2 f2 des2 bes2 c2 f2 bes2 c2 r2 bes2 f2 c8 f4 ees8 des4 g4 bes2 aes2 c2 f2 g8 bes4 r4 aes4 des8 f2 bes2 des8 g8 r8 aes8 f2 bes4 c2 ees4 aes4 r2 bes4 f2 c2 bes4 bes4 r2 f4 g4 aes4 f8 des8 ees8 r8 r8 des8 g2 bes2 aes2 f2 c4 des4 g4 aes8 des8 r4 g8 des8 bes2 bes2 f4 c2 ees4 bes8 des8 r4 r4 ees4 f4 bes4 f2 bes8 bes8 g8 f2 r8 des2 ees4 r4 g2 bes2 }
 \new Staff 
 \with {midiInstrument = #"string ensemble 1"}  
  \relative c' {\clef treble bes1 bes1 c1 c1 bes1 des1 aes1 f1 g1 f1 c1 c1 des1 g1 g1 g1 f1 f1 aes1 aes1 g1 g1 f1 f1 bes1 des1 f1 g1 f1 ees2 des2 bes1 }
 \new Staff 
\with {midiInstrument = #"acoustic grand"}  
  {\clef bass  <bes des f>1  <bes des f>2.  <bes des f>4  <ees g bes>1  <ees g bes>1  \set tieWaitForNote = ##t \grace { des32 ~ f ~ aes ~ des ~ } <des f aes des>1 \unset tieWaitForNote  <des f aes>2.  <des f aes>4  <bes des f>1  \set tieWaitForNote = ##t \grace { bes32 ~ des ~ f ~ bes ~ } <bes des f bes>2. \unset tieWaitForNote  \set tieWaitForNote = ##t \grace { bes32 ~ des ~ f ~ bes ~ } <bes des f bes>4 \unset tieWaitForNote  <bes des f>1  \set tieWaitForNote = ##t \grace { bes32 ~ des ~ f ~ bes ~ } <bes des f bes>1 \unset tieWaitForNote  <ees g bes>2.  <ees g bes>4  \set tieWaitForNote = ##t \grace { ees32 ~ g ~ bes ~ ees ~ } <ees g bes ees>2. \unset tieWaitForNote  \set tieWaitForNote = ##t \grace { ees32 ~ g ~ bes ~ ees ~ } <ees g bes ees>4 \unset tieWaitForNote  <des f aes>2.  <des f aes>4  \set tieWaitForNote = ##t \grace { des32 ~ f ~ aes ~ des ~ } <des f aes des>2. \unset tieWaitForNote  \set tieWaitForNote = ##t \grace { des32 ~ f ~ aes ~ des ~ } <des f aes des>4 \unset tieWaitForNote  <bes des f>1  \set tieWaitForNote = ##t \grace { bes32 ~ des ~ f ~ bes ~ } <bes des f bes>1 \unset tieWaitForNote  <bes des f>2.  <bes des f>4  <bes des f>2.  <bes des f>4  <ees g bes>1  <ees g bes>2.  <ees g bes>4  <des f aes>2.  <des f aes>4  <des f aes>2.  <des f aes>4  <bes des f>1  \set tieWaitForNote = ##t \grace { bes32 ~ des ~ f ~ bes ~ } <bes des f bes>1 \unset tieWaitForNote  <bes des f>2.  <bes des f>4  \set tieWaitForNote = ##t \grace { bes32 ~ des ~ f ~ bes ~ } <bes des f bes>2. \unset tieWaitForNote  \set tieWaitForNote = ##t \grace { bes32 ~ des ~ f ~ bes ~ } <bes des f bes>4 \unset tieWaitForNote  <ees g bes>2.  <ees g bes>4  <ees g bes>1  <des f aes>2.  <des f aes>4  <ees g bes>2  <des f aes>2  <bes des f>1 }
>>
\layout{}
\midi{}
}
