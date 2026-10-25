# Selenium Swipe Automation Experiment

An educational Selenium script that explores multi-window browser automation, interactive sign-in, modal handling, and repeated button interaction on Tinder.

## What it demonstrates

- Opening and controlling Chrome with Selenium
- Switching between browser windows
- Pausing for a user-completed interactive login
- Locating controls with XPath and CSS selectors
- Handling intercepted clicks and missing elements
- Adding delays around dynamic page content

## Requirements

- Python 3
- Google Chrome and a compatible ChromeDriver
- `selenium`

```bash
pip install selenium
```

## Security

The script does not store or type Facebook credentials. Complete sign-in manually in the browser when prompted. Never commit account credentials or place a primary password in automation source.

Confirm that any automation complies with the services' current terms before running it. Page XPaths are brittle and may require updates when the UI changes.
