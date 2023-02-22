[![Generic badge](https://img.shields.io/badge/license-Unlicense-green.svg)](https://shields.io/)

<div align="center">
	<br>
	<br>
    <img src="res/icon.png" width="200" height="200">
	<h1>Media Files Arranger</h1>
	<p>
    <b>Parse scattered media files in a tree structure to store them in a
       same folder using a naming convention based on file creation time.</b>
	</p>
	<br>
	<br>
	<br>
</div>

## Usage

```shell
python main.py PATH1 PATH2
```

Where:
- `PATH1`: is the path to the existing tree structure to be parsed.
- `PATH2`: is the path to the existing output directory, in which the files 
  will be stored.

## Notes

The default renaming format and time zone can be modified on top of the 
`main.py` file:
- The default renaming format is `YYYY:mm:dd_HH:MM:SS:MM`.
- The default time zone is `Europe/Paris`.

## Attributions

<div>
  Icon made by 
    <a href="https://www.flaticon.com/authors/freepik" title="FlatIcons">
       Freepik - Flaticon
    </a>
  on
  <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a>
</div>