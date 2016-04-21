
\version "2.18.2"
\header
 {
  title = "TT SEE-HEAR"
  composer = "Python"
  tagline = "Copyright: -"
}\score{
 << \new Staff 
\set Staff.instrumentName = #"Piano  "
  \relative c'' {\tempo 4 = 60 \clef treble r4 f8 f4 b8 d8 d8 b8 f8 b8 f4 d4 r8 g1 b8 r4 b8 d8 r4 c8 b1 g1 b8 r8 c8 d4 d8 r4 r1 f8 r4 r8 d8 d4 e8 c8 f8 f8 d2 d8 b1 r2 g8 a8 b4 d8 b8 b8 b8 f2 d4 b8 b8 e4 c8 r8 d8 c4 r8 e4 r4 g4 a4 b8 b8 b8 d8 f8 r8 d8 f4 a4 g8 b8 b8 f4 b4 f4 b8 f8 c4 r8 f8 r4 f1 r4 d4 b4 b8 b8 d4 e4 c8 r4 r8 r8 d8 b4 b8 b8 f4 d1 e1 g1 f2 f4 r4  <g b d>2  <f a c>2  <b d f>1 }
 \new Staff 
\with {midiInstrument = #"xylophone"}  
  {\clef treble c8 r8 e8 g8 a4 r4 r8 c8 d4 e8 b4 r8 a8 b8 f8 f8 d2 e1 r1 a8 f4 b8 f2 e1 g4 a8 f4 b8 b4 c4 b8 r8 g8 r8 r4 b1 e1 a8 g8 r8 e4 c4 r8 f8 r8 d8 f4 f8 r4 d8 b8 r8 g8 b4 f4 b4 b4 f8 r8 d4 r8 e8 c4 r8 g8 a4 r4 c4 e4 r8 d8 r4 d8 b4 b4 d8 d8 e8 g4 r8 a4 f8 c1 r4 e8 g8 r8 d4 b8 g4 b8 b4 f4 f8 r1 c1 r1 r8 f4 b8 b4 b4 }
 \new Staff 
 \with {midiInstrument = #"string ensemble 1"}  
  \relative c' {\clef treble f1 d1 b1 g1 b1 b1 g1 g1 a1 c1 f1 b1 b1 b1 a1 b1 a1 g1 g1 a1 f1 a1 f1 b1 e1 e1 f1 g2 f2 b1 }
 \new Staff 
\with {midiInstrument = #"Acoustic Grand Piano"}  
  {\clef bass  <b d f>1  \set tieWaitForNote = ##t \grace { b32 ~ d ~ f ~ b ~ } <b d f b>2. \unset tieWaitForNote  \set tieWaitForNote = ##t \grace { b32 ~ d ~ f ~ b ~ } <b d f b>4 \unset tieWaitForNote  <g b d>2.  <g b d>4  \set tieWaitForNote = ##t \grace { g32 ~ b ~ d ~ g ~ } <g b d g>1 \unset tieWaitForNote  <f a c>1  \set tieWaitForNote = ##t \grace { f32 ~ a ~ c ~ f ~ } <f a c f>2. \unset tieWaitForNote  \set tieWaitForNote = ##t \grace { f32 ~ a ~ c ~ f ~ } <f a c f>4 \unset tieWaitForNote  <b d f>2.  <b d f>4  \set tieWaitForNote = ##t \grace { b32 ~ d ~ f ~ b ~ } <b d f b>2. \unset tieWaitForNote  \set tieWaitForNote = ##t \grace { b32 ~ d ~ f ~ b ~ } <b d f b>4 \unset tieWaitForNote  <b d f>1  <b d f>1  <g b d>2.  <g b d>4  \set tieWaitForNote = ##t \grace { g32 ~ b ~ d ~ g ~ } <g b d g>1 \unset tieWaitForNote  <f a c>2.  <f a c>4  <f a c>2.  <f a c>4  <b d f>2.  <b d f>4  <b d f>1  \set tieWaitForNote = ##t \grace { b32 ~ d ~ f ~ b ~ } <b d f b>2. \unset tieWaitForNote  \set tieWaitForNote = ##t \grace { b32 ~ d ~ f ~ b ~ } <b d f b>4 \unset tieWaitForNote  <b d f>2.  <b d f>4  <g b d>1  \set tieWaitForNote = ##t \grace { g32 ~ b ~ d ~ g ~ } <g b d g>1 \unset tieWaitForNote  <f a c>1  <f a c>2.  <f a c>4  \set tieWaitForNote = ##t \grace { b32 ~ d ~ f ~ b ~ } <b d f b>2. \unset tieWaitForNote  \set tieWaitForNote = ##t \grace { b32 ~ d ~ f ~ b ~ } <b d f b>4 \unset tieWaitForNote  <b d f>2.  <b d f>4  \set tieWaitForNote = ##t \grace { b32 ~ d ~ f ~ b ~ } <b d f b>2. \unset tieWaitForNote  \set tieWaitForNote = ##t \grace { b32 ~ d ~ f ~ b ~ } <b d f b>4 \unset tieWaitForNote  <b d f>2.  <b d f>4  <g b d>1  <g b d>2  <f a c>2  <b d f>1 }
>>
\layout{}
\midi{}
}
