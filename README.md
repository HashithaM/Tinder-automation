# Selenium Swipe Automation Experiment

An educational Selenium script that explores multi-window browser automation, third-party login forms, modal handling, and repeated button interaction on Tinder.

## What it demonstrates

- Opening and controlling Chrome with Selenium
- Switching between browser windows
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

## Security warning

> [!CAUTION]
> The source currently contains a hardcoded login email and password. Treat the password as exposed: rotate it immediately, remove both values from public source/history, and never use committed credentials for browser automation.

Use an approved interactive/OAuth flow or a protected secret store, and confirm that any automation complies with the services' terms before running it. Page XPaths are brittle and will require updates when the UI changes.
