\version "2.14.2"

\header {
  title = "Title"
  subtitle = "Subtitle"
  composer = "Composer"
}

bass = \relative c {
  \set Staff.instrumentName = #"Bass "
  \set Staff.midiInstrument = #"electric bass (finger)"
  \clef bass
  \key c \major
  \time 4/4

  | |
  
  }

\score {
  \new Staff \bass
  \layout { }
  \midi { }
}
