# Catanie Theming file

This is the theming file for the catanie client. The theming file allows the systems administrator to configure the color theme of the client. The theming file can either be served from the backend, via the `/client/theme.json` endpoint or mounted into `/usr/share/nginx/html/assets/theme.json`.

An example is shown below

```
catanie/src/assets/theme.json

{
  "name": "light",  // Name of the theme.
  "properties": {  // The different theme colors. The colors here are the default ones. If you, in your theme file, choose to leave one of the properties out, the default one will be used instead.
    "--theme-primary-default": "#0099c8",
    "--theme-primary-default-contrast": "#ffffff",
    "--theme-primary-lighter": "#99d5e9",
    "--theme-primary-lighter-contrast": "#000000",
    "--theme-primary-darker": "#32acd3",
    "--theme-primary-darker-contrast": "#ffffff",
    "--theme-accent-default": "#99be00",
    "--theme-accent-default-contrast": "#ffffff",
    "--theme-accent-lighter": "#d6e599",
    "--theme-accent-lighter-contrast": "#000000",
    "--theme-accent-darker": "#adcb32",
    "--theme-accent-darker-contrast": "#ffffff",
    "--theme-warn-default": "#c81919",
    "--theme-warn-default-contrast": "#ffffff",
    "--theme-warn-lighter": "#ff6e6e",
    "--theme-warn-lighter-contrast": "#000000",
    "--theme-warn-darker": "#820019",
    "--theme-warn-darker-contrast": "#ffffff",
    "--theme-warn-2-default": "#ffbe00",
    "--theme-warn-2-default-contrast": "#ffffff",
    "--theme-warn-2-lighter": "#e1dc7d",
    "--theme-warn-2-lighter-contrast": "#000000",
    "--theme-warn-2-darker": "#d28c14",
    "--theme-warn-2-darker-contrast": "#ffffff",
    "--theme-header-1-default": "#003366",
    "--theme-header-1-default-contrast": "#ffffff",
    "--theme-header-1-lighter": "#99adc1",
    "--theme-header-1-lighter-contrast": "#000000",
    "--theme-header-1-darker": "#325b84",
    "--theme-header-1-darker-contrast": "#ffffff",
    "--theme-header-2-default": "#006646",
    "--theme-header-2-default-contrast": "#ffffff",
    "--theme-header-2-lighter": "#99c1b5",
    "--theme-header-2-lighter-contrast": "#000000",
    "--theme-header-2-darker": "#32846a",
    "--theme-header-2-darker-contrast": "#ffffff",
    "--theme-header-3-default": "#ff7d00",
    "--theme-header-3-default-contrast": "#ffffff",
    "--theme-header-3-lighter": "#ffcb99",
    "--theme-header-3-lighter-contrast": "#000000",
    "--theme-header-3-darker": "#ff9732",
    "--theme-header-3-darker-contrast": "#ffffff",
    "--theme-header-4-default": "#821482",
    "--theme-header-4-default-contrast": "#ffffff",
    "--theme-header-4-lighter": "#cda1cd",
    "--theme-header-4-lighter-contrast": "#000000",
    "--theme-header-4-darker": "#9b429b",
    "--theme-header-4-darker-contrast": "#ffffff",
    "--theme-hover-default": "#7f7f7f",
    "--theme-hover-default-contrast": "#000000",
    "--theme-hover-lighter": "#e5e5e5",
    "--theme-hover-lighter-contrast": "#000000",
    "--theme-hover-darker": "#b2b2b2",
    "--theme-hover-darker-contrast": "#000000"
  }
}
```
