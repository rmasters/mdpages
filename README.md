# mdpages

A simple Markdown page editor and viewer, written in Flask.

### Configuration

Copy the settings.py.base to settings.py, and replace the following values:

*   `ADMIN_USERNAME`, `ADMIN_PASSWORD` - the credentials to allowpages to be edited and deleted.
*   `PAGES_DIR` - where Markdown files are stored (an absolute path, or relative to the application directory).
