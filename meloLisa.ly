
\version "2.18.2"
\header
 {
  title = "TT SEE-HEAR"
  composer = "Python"
  tagline = "Copyright: -"
}\score{
 << \new Staff 
\set Staff.instrumentName = #"Piano  "
  \relative c'' {\tempo 4 = 60 \clef treble r8 a8 a8 dis4 fis8 fis4 r8 dis8 a8 dis4 a8 fis4 r4 b8 cis8 dis8 a8 a4 e1 dis4 r4 b4 cis4 fis1 r4 gis4 r8 b8 cis4 fis4 fis8 gis8 e4 dis8 r8 fis1 r8 b8 cis8 dis8 cis4 b4 dis8 dis8 dis8 a8 a2 dis8 dis4 gis8 e8 r8 fis4 fis4 e4 r8 gis8 r8 dis8 dis2 dis8 dis8 fis8 r8 r8 fis8 a2 cis8 b8 dis8 a4 dis8 a4 r8 fis8 r1 r8 cis4 a4 a8 e8 r8 gis2 b8 r8 fis8 dis8 dis1 a1 a1 fis1  <b dis fis>2  <a cis e>2  <a cis e>1 }
 \new Staff 
\with {midiInstrument = #"xylophone"}  
  {\clef treble e8 r8 gis4 b4 cis4 r8 r8 e8 fis4 gis4 dis8 fis8 dis8 r8 dis8 fis4 r4 gis1 a8 dis8 a4 dis8 r8 e4 fis1 a4 dis4 dis8 a8 r8 r8 b8 r8 r8 e4 a8 a4 fis4 dis8 dis2 gis8 r4 gis8 e8 r4 fis4 r4 fis8 a8 a4 r8 fis8 dis8 r4 b4 dis4 a8 dis8 a4 r8 fis8 b4 cis8 gis8 e4 r4 b8 cis8 a8 r8 e8 gis8 r8 fis4 dis4 dis8 dis8 fis4 dis8 a4 e8 a8 r8 fis8 gis2 b8 fis8 dis8 dis8 dis2 r8 fis4 gis8 e8 r8 r4 b8 dis1 a8 r8 fis4 dis8 dis8 dis4 r1 }
 \new Staff 
 \with {midiInstrument = #"string ensemble 1"}  
  \relative c' {\clef treble a1 a1 gis1 e1 a1 fis1 e1 dis1 cis1 dis1 dis1 b1 dis1 dis1 dis1 b1 dis1 e1 b1 dis1 fis1 e1 fis1 b2 a2 a1 }
 \new Staff 
\with {midiInstrument = #"acoustic grand"}  
  {\clef bass  <a cis e>1  \set tieWaitForNote = ##t \grace { a32 ~ cis ~ e ~ a ~ } <a cis e a>1 \unset tieWaitForNote  <b dis fis>1  <b dis fis>1  \set tieWaitForNote = ##t \grace { a32 ~ cis ~ e ~ a ~ } <a cis e a>1 \unset tieWaitForNote  <a cis e>1  <a cis e>1  \set tieWaitForNote = ##t \grace { a32 ~ cis ~ e ~ a ~ } <a cis e a>1 \unset tieWaitForNote  <a cis e>1  \set tieWaitForNote = ##t \grace { a32 ~ cis ~ e ~ a ~ } <a cis e a>1 \unset tieWaitForNote  <b dis fis>2.  <b dis fis>4  <b dis fis>1  \set tieWaitForNote = ##t \grace { a32 ~ cis ~ e ~ a ~ } <a cis e a>1 \unset tieWaitForNote  <a cis e>2.  <a cis e>4  <a cis e>1  \set tieWaitForNote = ##t \grace { a32 ~ cis ~ e ~ a ~ } <a cis e a>1 \unset tieWaitForNote  <a cis e>2.  <a cis e>4  <a cis e>2.  <a cis e>4  <b dis fis>1  <b dis fis>2.  <b dis fis>4  \set tieWaitForNote = ##t \grace { a32 ~ cis ~ e ~ a ~ } <a cis e a>1 \unset tieWaitForNote  <a cis e>1  \set tieWaitForNote = ##t \grace { a32 ~ cis ~ e ~ a ~ } <a cis e a>1 \unset tieWaitForNote  <b dis fis>2  <a cis e>2  <a cis e>1 }
>>
\layout{}
\midi{}
}
