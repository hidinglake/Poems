# My Poems

A small website for reading poems one at a time. Use the arrows, shuffle, or drag the timeline to move through a collection. Each `.txt` file in the `poems` folder gets its own tab under the heading.

## Folder layout

```
index.html                  the whole site
poems/Poems.txt             the poems, numbered /1 to /86
poems/files.json            which files appear as tabs, in order
scripts/build_manifest.py   keeps files.json up to date
.github/workflows/pages.yml publishes the site to GitHub Pages
```

## Putting it online

1. Create a new repository on GitHub and push this folder to the `main` branch.
2. In the repository, go to **Settings → Pages** and set **Source** to **GitHub Actions**.
3. Wait a minute. The site will be at `https://<your-username>.github.io/<repo-name>/`.

## Adding poems

Each poem starts with its number on a line of its own:

```
/1
First line of the first poem
Second line

/2
First line of the second poem
```

To add a collection, upload a `.txt` file into the `poems` folder (on GitHub: open the folder, then **Add file → Upload files**). Each push re-runs the publish workflow, which adds new files to `poems/files.json` automatically. The tab is named after the file, so `Winter.txt` becomes a tab called "Winter".

Clicking **My Poems** on the site and entering the password opens a list of the files and a link straight to GitHub's upload page for the `poems` folder.

To reorder tabs or give one a different name, edit `poems/files.json`:

```json
[
  { "file": "Poems.txt", "title": "Poems" },
  { "file": "Winter.txt", "title": "Winter, 2026" }
]
```

## Changing the password

The password is `mypoems`. The site stores a SHA-256 hash of it in `index.html` (`PW_HASH`). To set a new one, get the hash of your new password and paste it in:

```
printf '%s' 'your new password' | shasum -a 256
```

On Windows PowerShell:

```
$s=[Text.Encoding]::UTF8.GetBytes('your new password'); -join ([Security.Cryptography.SHA256]::Create().ComputeHash($s) | % { $_.ToString('x2') })
```

The password only hides the file list. Anyone can read the poems in a public repository, and only people with write access to the repository can add or change files.

## Using a custom domain

If the site isn't at a `github.io` address, open `index.html` and set `GITHUB_REPO` to your repository, for example `"yourname/my-poems"`, so the upload link points to the right place.

## Previewing on your own computer

Browsers block a page opened straight from disk from loading the poem files. Run a small local server from this folder instead:

```
python3 -m http.server
```

Then open http://localhost:8000.
