# Example Python Package

<p align="center">
  <a href=""><img alt="logo" src="https://user-images.githubusercontent.com/25851824/200928507-a65327f9-bc70-4c12-beaa-bc6ba74d968e.svg" width="80%"></a>
</p>

## Where does this content come from?

This is the content of your Python package `README.md` file.

## Markdown language (`.md`)

The `.md` extension stands for [Markdown language](https://www.markdownguide.org/getting-started/), a lightweight markup language that allows us to style a digital text document using typical formatting techniques like headings, emphasis, lists, images, and links. This language can also be easily converted into HTML to display nicely in a browser, such as when you visit your Python package on [PyPI](https://pypi.org/) or the associated [GitHub](https://github.com/) repository.

Everything you need to learn [Markdown language](https://www.markdownguide.org/) can be found [here](https://www.markdownguide.org/). If you want to dive right into the syntax, then this [Cheat Sheet](https://www.markdownguide.org/cheat-sheet/) will come in handy as well as this [Basic Syntax](https://www.markdownguide.org/basic-syntax/) guide. There are several open-source tools that support Markdown and where you can experiment your syntax (e.g., [Markdown Live Preview](https://markdownlivepreview.com/)).

## How to include media (images, gifs, ...)?

There are several ways to include media in your `README.md` file such that it is properly displayed across different platforms. Here I'm adopting [GitHub gists](https://docs.github.com/en/get-started/writing-on-github/editing-and-sharing-content-with-gists/creating-gists) to accomplish such task. Each GitHub gist is basically a Git repository meant to share code snippets, images or very small projects with others in a simple way.

As demonstrated [here](https://docs.github.com/en/get-started/writing-on-github/editing-and-sharing-content-with-gists/creating-gists), creating a gist from your [gist home page](https://gist.github.com/) (you will need a [GitHub](https://github.com/) account) is a no-brainer when you want to share a code snippet. However, if you want to create a gist containing a media file (e.g., `image.png`, `gif_example.gif`), then you should follow one of two options:

- Option 1 (the 'proper' way):
  - Create a gist on your [gist home page](https://gist.github.com/) named `example_image.md`.
  - Get your gist `<hash>` by right-clicking on it and selecting 'Copy link address'.
  - Clone your gist (a gist is just [GitHub](https://github.com/) repository!) into your disk by executing:
  
		git clone https://gist.github.com/<hash>.git
		or
		git clone git@gist.github.com:<hash>.git

  - Place `image.png` in your gist's repository.
  - Add the image to your gist's repository: `git add image.png`
  - Commit the image to your gist's repository: `git commit -m 'Add image.'`
  - Update remote gist's repository: `git push origin master`


- Option 2 (the 'tricky' way)
  - Create a gist on your [gist home page](https://gist.github.com/) named `example_image.md`.
  - Get to the 'Issues' tab in your [GitHub](https://github.com/) repository and click on 'New issue'.
  - Drag and drop `image.png` on the comment box.
  - Once `image.png` is uploaded to [GitHub](https://github.com/) servers, copy the link displayed on the comment box.
  - Get back to your gist `example_image.md` page (click 'Edit' if needed) and paste the previous link.
  - Click 'Create secret/public gist'.

Now that you have created your gist `example_image.md`, you should be able to see your `image.png` on your gist's [page](https://gist.github.com/). Right-click on it and select 'Copy image address'. This is the address that you should use in the `src` of your HTML image element (see the Python logo in the beginning of this file). Follow the same procedure to include `gif_example.gif` as shown below!


<p align="center">
  <a href=""><img alt="logo" src="https://user-images.githubusercontent.com/25851824/200957013-9d8651dd-af3d-4718-a321-eb9a5eefe42c.gif" width="80%"></a>
</p>

- `VERSION`:

1.0.0

- `LICENSE`:

MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
