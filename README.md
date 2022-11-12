# Terminal Bible Browser

## About
Terminal Bible Browser (TBB) is a simple, unofficial, terminal-based browser for the online 
[oremus Bible Browser](https://bible.oremus.org/). This started as a personal project as I 
wanted to improve my workflow. This project is focused on simplicity and eliminating any distracting
barriers in regards to reading the Bible.

## Plans
- [x] Implement a daily reading
- [ ] Improve the UI
- [ ] Add user inputted query parameters
- [ ] Implement input validation

## Usage
After cloning the repo and installing the listed requirements via `pip`, start TBB by running the
`/biblebrowser/biblebrowser.py` script. You will then be prompted to enter the passages you'd like
to view. **Note:** Please use a comma (,) to separate multiple passages. For example `Matthew
5:10,John 3:16`. See the list below for acceptable passage queries:

- Single verse: John 3:16
- Multiple verses: Matthew 5:1-12
- Whole Chapters: Proverbs 1
- Whole Books: James

**Note:** Due to copyright restrictions, oremus Bible Browser will only process up to 500 verses of
Scripture.
