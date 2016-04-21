
\version "2.18.2"
\header
 {title = "TT SEE-HEAR lisa"composer = "TT SEE-HEAR"}\score{
 << \new Staff 
\set Staff.instrumentName = #"Piano  "
  \relative c'' {\tempo 4 = 60 \clef treble r8 b8 b8 e4 gis4 gis8 r8 e4 b8 e8 b4 gis8 r4 cis8 dis4 e8 b8 b8 fis1 e8 r8 cis4 dis2 gis1 r8 a8 r4 cis4 dis4 gis4 gis8 a8 fis8 e4 r8 gis1 r8 cis4 dis8 e8 dis8 cis4 e4 e8 e4 b4 b8 e8 e8 a8 fis4 r4 gis8 gis8 fis4 r4 a8 r8 e8 e2 e8 e8 gis8 r8 r4 gis8 b8 dis4 cis4 e8 b4 e4 b8 r8 gis8 r1 r8 dis4 b8 b8 fis8 r4 a2 cis8 r8 gis8 e8 e1 b1 b1 gis1  <b dis fis>2  <a cis e>2  <e gis b>1 }
 \new Staff 
\with {midiInstrument = #"xylophone"}  
  {\clef treble fis8 r2 a8 cis8 dis8 r4 r8 fis4 gis8 a8 e8 gis8 e4 r8 e8 gis4 r8 a1 b8 e4 b4 e8 r8 fis8 gis1 b8 e8 e4 b8 r4 r8 cis4 r8 r8 fis4 b8 b8 gis4 e8 e2 a8 r8 a8 fis8 r2 gis8 r4 gis8 b8 b8 r8 gis4 e8 r8 cis8 e2 b8 e8 b4 r8 gis8 cis8 dis4 a8 fis4 r8 cis8 dis4 b8 r8 fis8 a8 r4 gis8 e4 e8 e4 gis4 e8 b8 fis8 b4 r4 gis8 a4 cis8 gis8 e8 e4 e4 r4 gis8 a8 fis8 r8 r4 cis4 e1 b4 r4 gis8 e8 e8 e8 r1 }
 \new Staff 
 \with {midiInstrument = #"string ensemble 1"}  
  \relative c' {\clef treble fis1 gis1 gis1 a1 e1 e1 fis1 e1 dis1 e1 b1 cis1 b1 gis1 b1 cis1 cis1 fis1 fis1 e1 gis1 fis1 gis1 b2 a2 e1 }
 \new Staff 
\with {midiInstrument = #"acoustic grand"}  
  {\clef bass  <e gis b>2.  <e gis b>4  \set tieWaitForNote = ##t \grace { e32 ~ gis ~ b ~ e ~ } <e gis b e>2. \unset tieWaitForNote  \set tieWaitForNote = ##t \grace { e32 ~ gis ~ b ~ e ~ } <e gis b e>4 \unset tieWaitForNote  <b dis fis>1  \set tieWaitForNote = ##t \grace { b32 ~ dis ~ fis ~ b ~ } <b dis fis b>1 \unset tieWaitForNote  <a cis e>2.  <a cis e>4  <a cis e>1  \set tieWaitForNote = ##t \grace { e32 ~ gis ~ b ~ e ~ } <e gis b e>2. \unset tieWaitForNote  \set tieWaitForNote = ##t \grace { e32 ~ gis ~ b ~ e ~ } <e gis b e>4 \unset tieWaitForNote  <e gis b>2.  <e gis b>4  <e gis b>2.  <e gis b>4  \set tieWaitForNote = ##t \grace { e32 ~ gis ~ b ~ e ~ } <e gis b e>1 \unset tieWaitForNote  <b dis fis>1  <b dis fis>1  <a cis e>2.  <a cis e>4  <a cis e>1  \set tieWaitForNote = ##t \grace { e32 ~ gis ~ b ~ e ~ } <e gis b e>1 \unset tieWaitForNote  <e gis b>2.  <e gis b>4  <e gis b>1  \set tieWaitForNote = ##t \grace { e32 ~ gis ~ b ~ e ~ } <e gis b e>1 \unset tieWaitForNote  <b dis fis>1  \set tieWaitForNote = ##t \grace { b32 ~ dis ~ fis ~ b ~ } <b dis fis b>2. \unset tieWaitForNote  \set tieWaitForNote = ##t \grace { b32 ~ dis ~ fis ~ b ~ } <b dis fis b>4 \unset tieWaitForNote  <a cis e>2.  <a cis e>4  <a cis e>2.  <a cis e>4  <e gis b>2.  <e gis b>4  <b dis fis>2  <a cis e>2  <e gis b>1 }
>>
\layout{}
\midi{}
}
