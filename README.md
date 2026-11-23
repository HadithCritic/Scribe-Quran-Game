# Scribe — Quran copying practice

Scribe is a quiet, verse-by-verse writing practice game. It invites you to copy the Authorized English Translation of the Quran one passage at a time, slowly and attentively.

## About

The game presents 6,346 typing passages in sequence, including each surah's opening basmala except surah 9. As you copy, Scribe tracks progress through the whole text and by surah. When you finish, you can begin another copy.

## Features

- A focused writing desk with one passage displayed at a time.
- Exact-text typing practice; use Backspace to correct mistakes.
- Automatic progress saving in browser storage.
- A progress view showing completed copies, passages remaining, and completion by surah.
- A restart option and the ability to begin another full copy.
- A self-contained HTML game with its styles, behavior, text, fonts, and artwork embedded.

## Play

1. Download `Scribe.html` from this repository.
2. Open it in a modern browser.
3. Select **Begin writing**, then click the paper and type the displayed passage.
4. Continue passage by passage. Your progress is saved automatically.

No build step, package installation, or server is required. Progress stays in the browser profile and is associated with the address used to open the game. The downloaded file and any hosted copy therefore have separate saves.

## Repository contents

- `Scribe.html` — standalone playable game.
- `Artwork/Scribe_Coffee_Final_Artwork.png` — source artwork; the game also contains an embedded copy.
- `Assets/Fonts/*OFL.txt` — license notices for the fonts embedded in the game.

There are no runtime packages or external package dependencies to install. The game is implemented as a single HTML file.

## Text and credits

The English Quran translation is by Dr. Rashad Khalifa and was first published by Islamic Productions. The game reproduces the verse wording for free, credited sharing. See [WikiSubmission's rights and credits page](https://wikisubmission.org/legal/rights) for its sharing guidance. The Arabic Quran text is not subject to copyright.

The fonts embedded in the game are distributed under the SIL Open Font License; their notices are included under `Assets/Fonts/`.
