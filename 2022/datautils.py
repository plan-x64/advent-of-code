from pathlib import Path
import sys
import urllib.parse
import urllib.request


_DEFAULT_CACHE_DIRECTORY = ".cached_input"
_SESSION_ID_FILE_NAME = "session_id"


def read_input_data(url: str, session_id: str = None, cache_directory: str = _DEFAULT_CACHE_DIRECTORY) -> [str]:
    file_path = Path(cache_directory, _file_from_url(url))

    if not file_path.exists():
        resolved_session_id = _get_session_id(session_id, cache_directory)
        if resolved_session_id is not None:
            _gather_input_data(url, resolved_session_id, cache_directory)
        else:
            raise FileNotFoundError("No cached input for file={} and no session_id was given".format(file_path))

    return file_path.read_text(encoding='utf-8')


def _gather_input_data(url, session_id, cache_directory=_DEFAULT_CACHE_DIRECTORY):
    _create_cached_directory(cache_directory)
    _cache_session_id(session_id, cache_directory)

    request = urllib.request.Request(url)
    request.add_header("cookie", "session={}".format(session_id))

    output_path = Path(cache_directory, _file_from_url(url))

    with urllib.request.urlopen(request) as response:
        with open(output_path, 'w') as output:
            output.write(response.read().decode('utf-8'))


def _file_from_url(url):
    (_, _, path, _, _, _) = urllib.parse.urlparse(url)
    (_, year, _, day, _) = path.split('/')
    return '{}_{:02d}'.format(year, int(day))


def _create_cached_directory(cache_directory):
    cache_path = Path(cache_directory)
    if not cache_path.exists():
        cache_path.mkdir()


def _get_session_id(session_id, cache_directory):
    session_id_path = Path(cache_directory, _SESSION_ID_FILE_NAME)

    if session_id is not None:
        return session_id
    elif session_id_path.exists():
        with open(session_id_path, 'r') as session_id_file:
            return session_id_file.read()
    else:
        return None


def _cache_session_id(session_id, cache_directory):
    _create_cached_directory(cache_directory)

    session_id_path = Path(cache_directory, _SESSION_ID_FILE_NAME)
    if not session_id_path.exists():
        with open(session_id_path, 'w') as session_id_file:
            session_id_file.write(session_id)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("python datautils.py url [session_id] (args={})".format(sys.argv))
    elif len(sys.argv) == 2:
        read_input_data(sys.argv[1])
    else:
        read_input_data(sys.argv[1], sys.argv[2])
